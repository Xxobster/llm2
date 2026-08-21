"""Causal open-interest features from ``market_oi.sqlite``.

Open interest (OI) rows are stamped at bar OPEN time (same convention as
``market_ohlcv``). A bar open at ``T`` on timeframe ``tf`` is only knowable at
``T + tf``. We stamp each OI observation at its **completion instant**, then
as-of-merge onto each decision bar's completion instant so incomplete OI never
enters the feature matrix.

Prefer Bybit (venue) then Binance; prefer native 1h then resample 5m.
"""

from __future__ import annotations

import sqlite3
from functools import lru_cache

import numpy as np
import pandas as pd

from llm2.paths import MARKET_OI_DB, TF_MS

PREFERRED_TF = ("1h", "5m")
PREFERRED_EXCHANGE = ("bybit", "binance")


def _to_utc_ns(idx: pd.DatetimeIndex | pd.Index) -> pd.DatetimeIndex:
    return pd.DatetimeIndex(pd.to_datetime(idx, utc=True)).as_unit("ns")


def _load_oi_raw(symbol: str, *, exchange: str, timeframe: str) -> pd.DataFrame:
    if not MARKET_OI_DB.is_file():
        raise FileNotFoundError(f"OI warehouse missing: {MARKET_OI_DB}")
    conn = sqlite3.connect(f"file:{MARKET_OI_DB}?mode=ro", uri=True, timeout=60.0)
    try:
        return pd.read_sql(
            "SELECT ts_ms, oi FROM market_oi "
            "WHERE exchange=? AND symbol=? AND timeframe=? ORDER BY ts_ms",
            conn,
            params=(exchange.lower(), symbol.upper(), timeframe),
        )
    finally:
        conn.close()


@lru_cache(maxsize=48)
def load_oi_completed(
    symbol: str,
    timeframe: str = "1h",
    exchange: str = "bybit",
) -> pd.Series:
    """OI level indexed by bar completion instant (UTC ns)."""
    raw = _load_oi_raw(symbol, exchange=exchange, timeframe=timeframe)
    if raw.empty:
        return pd.Series(dtype=float, name="oi")
    step = int(TF_MS[timeframe])
    horizon_ms = int(pd.Timestamp("2030-01-01", tz="UTC").value // 1_000_000)
    ts = raw["ts_ms"].astype(np.int64)
    raw = raw.loc[ts <= horizon_ms]
    complete_ms = raw["ts_ms"].astype(np.int64) + step
    idx = _to_utc_ns(pd.to_datetime(complete_ms.to_numpy(), unit="ms", utc=True))
    s = pd.Series(raw["oi"].astype(float).to_numpy(), index=idx, name="oi")
    return s[~s.index.duplicated(keep="last")].sort_index()


def _resample_rule(decision_tf: str) -> str | None:
    return {
        "15m": "15min",
        "1h": "1h",
        "4h": "4h",
        "1d": "1D",
    }.get(decision_tf)


def _pick_series(symbol: str, decision_tf: str) -> pd.Series:
    for exch in PREFERRED_EXCHANGE:
        for tf in PREFERRED_TF:
            try:
                s = load_oi_completed(symbol, timeframe=tf, exchange=exch)
            except Exception:
                continue
            if s.empty or len(s) < 100:
                continue
            if tf == decision_tf:
                return s
            rule = _resample_rule(decision_tf)
            if rule is None:
                return s
            out = s.resample(rule, label="right", closed="right").last().dropna()
            out.index = _to_utc_ns(out.index)
            return out
    return pd.Series(dtype=float, name="oi")


def build_oi_v1(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str = "1h",
    exchange: str | None = None,
) -> pd.DataFrame:
    """Causal OI transforms on the decision bar index (known at bar close)."""
    if not symbol:
        raise TypeError("oi_v1 requires symbol")
    target_idx = _to_utc_ns(ohlcv.index)
    unique_idx = target_idx[~target_idx.duplicated(keep="last")]
    step = pd.Timedelta(milliseconds=int(TF_MS[timeframe]))

    if exchange:
        oi = load_oi_completed(symbol, timeframe=timeframe, exchange=exchange)
        if oi.empty:
            oi = _pick_series(symbol, timeframe)
    else:
        oi = _pick_series(symbol, timeframe)

    empty_cols = (
        "oi_level_log",
        "oi_logret_1",
        "oi_mom_6",
        "oi_mom_24",
        "oi_z_24",
        "oi_z_168",
        "oi_age_h",
    )
    if oi.empty:
        out_u = pd.DataFrame(index=unique_idx, columns=list(empty_cols), dtype=float)
        out = out_u.reindex(target_idx)
        out.index = ohlcv.index
        return out

    oi = oi.copy()
    oi.index = _to_utc_ns(oi.index)
    complete = unique_idx + step

    left = pd.DataFrame({"complete": complete, "bar_open": unique_idx}).sort_values(
        "complete"
    )
    right = pd.DataFrame(
        {"complete": oi.index, "oi": oi.to_numpy(dtype=float)}
    ).sort_values("complete")
    merged = pd.merge_asof(left, right, on="complete", direction="backward")
    merged = merged.set_index("bar_open").sort_index()
    level = merged["oi"]

    oi_ns = oi.index.asi8
    bar_ns = _to_utc_ns(merged["complete"]).asi8
    pos = np.searchsorted(oi_ns, bar_ns, side="right") - 1
    valid = pos >= 0
    age_h = np.full(len(bar_ns), np.nan, dtype=float)
    age_h[valid] = (bar_ns[valid] - oi_ns[pos[valid]]) / 3.6e12

    out_u = pd.DataFrame(index=unique_idx)
    out_u["oi_level_log"] = np.log(level.where(level > 0))
    out_u["oi_logret_1"] = out_u["oi_level_log"].diff()
    out_u["oi_mom_6"] = level.pct_change(6)
    out_u["oi_mom_24"] = level.pct_change(24)
    for w in (24, 168):
        rm = level.rolling(w, min_periods=max(2, w // 4)).mean()
        rs = level.rolling(w, min_periods=max(2, w // 4)).std()
        out_u[f"oi_z_{w}"] = (level - rm) / rs.replace(0, np.nan)
    out_u["oi_age_h"] = age_h

    out = out_u.reindex(target_idx)
    out.index = ohlcv.index
    return out.replace([np.inf, -np.inf], np.nan)


def build_structure_oi_v1(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str = "1h",
    **kwargs,
) -> pd.DataFrame:
    """Join structure_v1 with causal oi_v1 columns."""
    from llm2.features.structure_v1 import build_structure_v1

    s = build_structure_v1(ohlcv, symbol=symbol, timeframe=timeframe, **kwargs)
    o = build_oi_v1(ohlcv, symbol=symbol, timeframe=timeframe)
    return s.join(o, how="left")
