"""Hunt 019: Crowding–Absorption State Machine + Hilbert phase router.

Audit agenda P1-A + P4. Not an OHLCV indicator grid. Thresholds are module
constants (including Hilbert z=1.5 from hunt 013). Do not search them.

Variant A uses only open-interest change, funding, price impact, and Average
True Range expansion — no order-book refill (not in the historical warehouse).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import wilder_atr
from llm2.data.macro import load_funding
from llm2.features.oi_v1 import build_oi_v1
from llm2.ml_lab.causal_math import WIN, Z_FIRE, bar_return, inst_amplitude, log_price, sign_nz, zscore
from llm2.paths import TF_MS
from llm2.validation.folds import index_to_ms

CROWD_Z = 1.0
VOL_FLOOR = 0.25

IDEA_IDS_CASM: tuple[str, ...] = (
    "casm_healthy_follow",
    "casm_exhaust_fade",
    "phase_router",
)


def _funding_at_close(
    ohlcv: pd.DataFrame, symbol: str, timeframe: str
) -> tuple[np.ndarray, np.ndarray]:
    """Last settlement at or before bar close, plus z-score on the *print* series.

    A bar-level z-score of a forward-filled 8-hour rate is degenerate (rolling
    standard deviation ≈ 0). z(funding) is defined on successive settlements.
    """
    n = len(ohlcv)
    rate = np.full(n, np.nan, dtype=np.float64)
    z = np.full(n, np.nan, dtype=np.float64)
    try:
        fund = load_funding(symbol)
    except Exception:
        return rate, z
    if fund.empty:
        return rate, z
    close_ms = index_to_ms(ohlcv.index).astype(np.int64) + int(TF_MS[timeframe])
    f_ts = (fund.index.asi8 // 1_000_000).astype(np.int64)
    f_rt = fund.to_numpy(dtype=float)
    f_z = zscore(f_rt)
    idx = np.searchsorted(f_ts, close_ms, side="right") - 1
    ok = idx >= 0
    rate[ok] = f_rt[idx[ok]]
    z[ok] = f_z[idx[ok]]
    return rate, z


def _oi_dlog(ohlcv: pd.DataFrame, symbol: str, timeframe: str) -> np.ndarray:
    if "oi_logret_1" in ohlcv.columns:
        return ohlcv["oi_logret_1"].to_numpy(dtype=float)
    try:
        oi = build_oi_v1(ohlcv, symbol=symbol, timeframe=timeframe)
    except Exception:
        return np.full(len(ohlcv), np.nan, dtype=np.float64)
    if "oi_logret_1" not in oi.columns:
        return np.full(len(ohlcv), np.nan, dtype=np.float64)
    return oi["oi_logret_1"].to_numpy(dtype=float)


def _state(ohlcv: pd.DataFrame, symbol: str, timeframe: str) -> dict[str, np.ndarray]:
    c = ohlcv["close"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    v = ohlcv["volume"].to_numpy(dtype=float)
    r = bar_return(c)
    lp = log_price(c)
    r3 = pd.Series(r).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    r8 = pd.Series(r).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    atr_med = pd.Series(atr).rolling(WIN, min_periods=WIN).median().to_numpy(dtype=float)
    rel_v = pd.Series(v).rolling(WIN, min_periods=WIN).mean().to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        rel = v / np.where(np.isfinite(rel_v) & (rel_v > 0.0), rel_v, np.nan)
    rel = np.clip(rel, VOL_FLOOR, np.inf)
    with np.errstate(divide="ignore", invalid="ignore"):
        impact = np.abs(r) / rel
    dlog = _oi_dlog(ohlcv, symbol, timeframe)
    if "funding_rate" in ohlcv.columns:
        fund = ohlcv["funding_rate"].to_numpy(dtype=float)
        fund_z = zscore(fund)
    else:
        fund, fund_z = _funding_at_close(ohlcv, symbol, timeframe)
    dlog_z = zscore(dlog)
    impact_z = zscore(impact)
    amp_z = zscore(inst_amplitude(lp))
    aligned = (
        np.isfinite(dlog)
        & np.isfinite(dlog_z)
        & np.isfinite(r8)
        & (sign_nz(dlog) == sign_nz(r8))
        & (sign_nz(dlog) != 0.0)
    )
    expanding = np.isfinite(atr) & np.isfinite(atr_med) & (atr >= atr_med)
    healthy = aligned & (dlog_z >= CROWD_Z) & np.isfinite(impact_z) & (impact_z >= 0.0) & expanding
    crowded_same = (
        np.isfinite(fund_z)
        & (np.abs(fund_z) >= CROWD_Z)
        & np.isfinite(r3)
        & (sign_nz(fund) == sign_nz(r3))
        & (sign_nz(fund) != 0.0)
    )
    exhaust = crowded_same & np.isfinite(impact_z) & (impact_z <= 0.0)
    hilbert = np.isfinite(amp_z) & (amp_z >= Z_FIRE)
    return {
        "r3": r3,
        "r8": r8,
        "dlog": dlog,
        "dlog_z": dlog_z,
        "fund": fund,
        "fund_z": fund_z,
        "impact": impact,
        "impact_z": impact_z,
        "amp_z": amp_z,
        "atr": atr,
        "healthy": healthy,
        "exhaust": exhaust,
        "hilbert": hilbert,
    }


def casm_healthy_follow(
    ohlcv: pd.DataFrame, timeframe: str, symbol: str = "ETHUSDT", st: dict | None = None
) -> np.ndarray:
    """Follow when open-interest flow aligns with price, impact is efficient, ATR expands."""
    st = st or _state(ohlcv, symbol, timeframe)
    out = np.zeros(st["r8"].size, dtype=np.float64)
    fire = st["healthy"]
    out[fire] = sign_nz(st["r8"])[fire]
    return out


def casm_exhaust_fade(
    ohlcv: pd.DataFrame, timeframe: str, symbol: str = "ETHUSDT", st: dict | None = None
) -> np.ndarray:
    """Fade when funding crowding matches the move but price impact has stalled."""
    st = st or _state(ohlcv, symbol, timeframe)
    out = np.zeros(st["r3"].size, dtype=np.float64)
    fire = st["exhaust"]
    out[fire] = -sign_nz(st["r3"])[fire]
    return out


def phase_router(
    ohlcv: pd.DataFrame, timeframe: str, symbol: str = "ETHUSDT", st: dict | None = None
) -> np.ndarray:
    """Exact Hilbert-envelope trigger; continue, fade, or skip using CASM-A state.

    Exhaustion wins over continuation at the trigger (forced-flow absorption).
    No trade when Hilbert fires without a clear crowding state.
    """
    st = st or _state(ohlcv, symbol, timeframe)
    out = np.zeros(st["r3"].size, dtype=np.float64)
    trig = st["hilbert"]
    fade = trig & st["exhaust"]
    cont = trig & st["healthy"] & ~st["exhaust"]
    out[fade] = -sign_nz(st["r3"])[fade]
    out[cont] = sign_nz(st["r3"])[cont]
    return out


def signals_casm(ohlcv: pd.DataFrame, timeframe: str, symbol: str = "ETHUSDT") -> dict[str, np.ndarray]:
    st = _state(ohlcv, symbol, timeframe)
    return {
        "casm_healthy_follow": casm_healthy_follow(ohlcv, timeframe, symbol, st=st),
        "casm_exhaust_fade": casm_exhaust_fade(ohlcv, timeframe, symbol, st=st),
        "phase_router": phase_router(ohlcv, timeframe, symbol, st=st),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Candle-derived slice for the shared leakage engine.

    Open-interest / funding are as-of warehouse joins. Tip-shocking OHLCV cannot
    move those columns, so they are not in this frame (CAUS-WAREHOUSE-001).
    Their completion-time alignment is covered by ``tests/test_oi_news_causality.py``.
    """
    del kwargs
    c = ohlcv["close"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    v = ohlcv["volume"].to_numpy(dtype=float)
    r = bar_return(c)
    rel_v = pd.Series(v).rolling(WIN, min_periods=WIN).mean().to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        rel = v / np.where(np.isfinite(rel_v) & (rel_v > 0.0), rel_v, np.nan)
    rel = np.clip(rel, VOL_FLOOR, np.inf)
    with np.errstate(divide="ignore", invalid="ignore"):
        impact = np.abs(r) / rel
    return pd.DataFrame(
        {
            "bar_return": r,
            "impact": impact,
            "amp": inst_amplitude(log_price(c)),
            "atr": wilder_atr(h, l, c, 14),
        },
        index=ohlcv.index,
    )
