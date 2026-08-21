"""Causal running-retrace features (tradable leg-state; never oracle_leaky).

These series are knowable at bar T from completed legs and price path up to T.
They are **not** the look-ahead orange label (`oracle_leaky` / pre-CAUS-STRUCT-001
``last_retrace_pct`` publish). Use them as alpha features or diagnostics only under
a fresh pre-registration (D-058 / D-060).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

from llm2.paths import TF_MS

_INDICATORS = Path(r"C:\projects\botsgeneral\packages\indicators\src")


def _prefer_indicators() -> None:
    if _INDICATORS.is_dir() and str(_INDICATORS) not in sys.path:
        sys.path.insert(0, str(_INDICATORS))


def _ohlcv_raw(ohlcv: pd.DataFrame) -> pd.DataFrame:
    idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
    raw = ohlcv.reset_index(drop=True).copy()
    if "ts_ms" not in raw.columns:
        raw["ts_ms"] = (idx.asi8 // 1_000_000).astype("int64")
    for col in ("open", "high", "low", "close"):
        if col not in raw.columns:
            raise ValueError(f"ohlcv missing {col}")
    return raw


def build_causal_run_retrace(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str = "1h",
    source: str = "binance",
) -> pd.DataFrame:
    """As-of running retrace depth + nearby causal leg/swing context (vectorized)."""
    _prefer_indicators()
    from indicators.compute import compute_structure

    raw = _ohlcv_raw(ohlcv)
    bundle = compute_structure(
        raw, source=source, symbol=str(symbol).upper(), timeframe=timeframe
    )
    ts = raw["ts_ms"].to_numpy(dtype=np.int64)
    close = pd.to_numeric(raw["close"], errors="coerce").to_numpy(dtype=float)
    high = pd.to_numeric(raw["high"], errors="coerce").to_numpy(dtype=float)
    low = pd.to_numeric(raw["low"], errors="coerce").to_numpy(dtype=float)
    n = len(ts)
    idx = pd.to_datetime(ts, unit="ms", utc=True)
    step = float(TF_MS.get(timeframe, 3_600_000))

    legs = bundle.legs
    swings = bundle.swings
    swing_confirm = {s.swing_id: s.confirm_ts_ms for s in swings}

    if not legs:
        return pd.DataFrame(index=pd.DatetimeIndex(idx))

    known_ts = np.asarray(
        [
            max(
                swing_confirm.get(lg.start_swing_id, lg.end_ts_ms),
                swing_confirm.get(lg.end_swing_id, lg.end_ts_ms),
            )
            for lg in legs
        ],
        dtype=np.int64,
    )
    order = np.argsort(known_ts, kind="mergesort")
    known_ts = known_ts[order]
    legs_o = [legs[i] for i in order.tolist()]
    retr = np.asarray([lg.retrace_pct for lg in legs_o], dtype=float)
    dirs = np.asarray([1.0 if lg.direction == "up" else -1.0 for lg in legs_o], dtype=float)
    end_px = np.asarray([lg.end_price for lg in legs_o], dtype=float)
    length_abs = np.asarray([lg.length_abs for lg in legs_o], dtype=float)
    length_pct = np.asarray([lg.length_pct for lg in legs_o], dtype=float)
    end_ts = np.asarray([lg.end_ts_ms for lg in legs_o], dtype=np.int64)
    kind_imp = np.asarray([1.0 if lg.kind == "impulse" else 0.0 for lg in legs_o])

    # Last completed leg known by bar T (successor publish time).
    li = np.searchsorted(known_ts, ts, side="right") - 1
    ok = li >= 0
    li_safe = np.clip(li, 0, len(legs_o) - 1)
    ep = np.where(ok, end_px[li_safe], np.nan)
    la = np.where(ok, length_abs[li_safe], np.nan)
    lp = np.where(ok, length_pct[li_safe], np.nan)
    d = np.where(ok, dirs[li_safe], np.nan)
    kt = np.where(ok, known_ts[li_safe].astype(float), np.nan)
    et = np.where(ok, end_ts[li_safe].astype(float), np.nan)
    imp = np.where(ok, kind_imp[li_safe], np.nan)

    move_against = np.where(d > 0, ep - close, close - ep)
    run_retrace = np.where(ok & (la > 1e-12), np.maximum(0.0, move_against) / la, np.nan)
    against_hi = np.where(d > 0, ep - low, high - ep)
    run_retrace_ext = np.where(ok & (la > 1e-12), np.maximum(0.0, against_hi) / la, np.nan)

    # Previous completed leg's final retrace is causal once the current last leg is known
    # (retrace of leg i-1 is measured against end of leg i).
    prev_ok = li >= 1
    li_p = np.clip(li - 1, 0, len(legs_o) - 1)
    prev_retr_causal = np.where(prev_ok, retr[li_p], np.nan)
    prev_len = np.where(prev_ok, length_pct[li_p], np.nan)
    prev_dir = np.where(prev_ok, dirs[li_p], np.nan)

    sw_ts = np.asarray([s.confirm_ts_ms for s in swings], dtype=np.int64)
    sw_px = np.asarray([s.price for s in swings], dtype=float)
    sw_k = np.asarray([1.0 if s.kind == "high" else -1.0 for s in swings], dtype=float)
    if len(swings):
        order_s = np.argsort(sw_ts, kind="mergesort")
        sw_ts = sw_ts[order_s]
        sw_px = sw_px[order_s]
        sw_k = sw_k[order_s]
        high_mask = sw_k > 0
        low_mask = sw_k < 0
        h_ts, h_px = sw_ts[high_mask], sw_px[high_mask]
        l_ts, l_px = sw_ts[low_mask], sw_px[low_mask]
        if len(h_ts):
            hi = np.searchsorted(h_ts, ts, side="right") - 1
            last_sh = np.where(hi >= 0, h_px[np.clip(hi, 0, len(h_px) - 1)], np.nan)
        else:
            last_sh = np.full(n, np.nan)
        if len(l_ts):
            li2 = np.searchsorted(l_ts, ts, side="right") - 1
            last_sl = np.where(li2 >= 0, l_px[np.clip(li2, 0, len(l_px) - 1)], np.nan)
        else:
            last_sl = np.full(n, np.nan)
        dist_sh = (close - last_sh) / close
        dist_sl = (close - last_sl) / close
        t0_24 = ts - 24 * int(step)
        t0_72 = ts - 72 * int(step)
        t0_168 = ts - 168 * int(step)
        right = np.searchsorted(sw_ts, ts, side="right")
        n_sw_24 = (right - np.searchsorted(sw_ts, t0_24, side="left")).astype(float)
        n_sw_72 = (right - np.searchsorted(sw_ts, t0_72, side="left")).astype(float)
        n_sw_168 = (right - np.searchsorted(sw_ts, t0_168, side="left")).astype(float)
    else:
        dist_sh = dist_sl = np.full(n, np.nan)
        n_sw_24 = n_sw_72 = n_sw_168 = np.zeros(n)

    out = pd.DataFrame(
        {
            "run_retrace": run_retrace,
            "run_retrace_ext": run_retrace_ext,
            "run_leg_id": np.where(ok, li.astype(float), np.nan),
            "run_last_leg_len_pct": lp,
            "run_last_leg_dir": d,
            "run_last_leg_impulse": imp,
            "run_bars_since_leg_known": np.where(ok, (ts.astype(float) - kt) / step, np.nan),
            "run_bars_since_leg_end": np.where(ok, (ts.astype(float) - et) / step, np.nan),
            "run_dist_to_leg_end_pct": np.where(
                ok & (close != 0), (close - ep) / close, np.nan
            ),
            "run_prev_leg_retrace_causal": prev_retr_causal,
            "run_prev_leg_len_pct": prev_len,
            "run_prev_leg_dir": prev_dir,
            "run_dist_last_sh_pct": dist_sh,
            "run_dist_last_sl_pct": dist_sl,
            "run_n_sw_24": n_sw_24,
            "run_n_sw_72": n_sw_72,
            "run_n_sw_168": n_sw_168,
        },
        index=idx,
    )
    leg_id_s = pd.Series(np.where(ok, li, -1), index=idx)
    run_s = pd.Series(run_retrace_ext, index=idx)
    out["run_retrace_expand_max"] = run_s.groupby(leg_id_s, sort=False).cummax()
    out["run_minus_prev_retr"] = (
        out["run_retrace_expand_max"] - out["run_prev_leg_retrace_causal"]
    )
    out["run_retrace_diff1"] = out["run_retrace"].diff(1)
    out["run_retrace_diff3"] = out["run_retrace"].diff(3)
    out["run_retrace_mean6"] = out["run_retrace"].rolling(6, min_periods=2).mean()
    # Align to caller index order (handles duplicates / original index objects).
    target = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
    out = out.reindex(target[~target.duplicated(keep="last")])
    out = out.reindex(target)
    out.index = ohlcv.index
    return out.replace([np.inf, -np.inf], np.nan)


def build_structure_v1_run_retrace(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str = "1h",
    higher_timeframes: tuple[str, ...] | None = None,
    include_volatility_normalised: bool = True,
    source: str | None = None,
    recent_only: bool = False,
) -> pd.DataFrame:
    """``structure_v1_no_retrace`` + causal running-retrace columns (no orange label)."""
    from llm2.features.structure_v1 import build_structure_v1_no_retrace

    struct = build_structure_v1_no_retrace(
        ohlcv,
        symbol=symbol,
        timeframe=timeframe,
        higher_timeframes=higher_timeframes,
        include_volatility_normalised=include_volatility_normalised,
        source=source,
        recent_only=recent_only,
    )
    run = build_causal_run_retrace(
        ohlcv,
        symbol=symbol,
        timeframe=timeframe,
        source=str(source or "binance"),
    )
    # Prefer explicit run_* column names; drop accidental overlap.
    overlap = [c for c in run.columns if c in struct.columns]
    if overlap:
        run = run.drop(columns=overlap)
    out = struct.join(run, how="left")
    bad = [
        c
        for c in out.columns
        if "oracle_leaky" in str(c).lower() or str(c).startswith("pred_leaky")
    ]
    if bad:
        raise RuntimeError(f"structure_v1_run_retrace refused leaky columns: {bad}")
    return out
