"""Soft Volume Spread Analysis (VSA) absorption score (0..1), train-thresholded."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.validation.folds import index_to_ms


def _squash(x: np.ndarray, lo: float, hi: float) -> np.ndarray:
    out = (np.asarray(x, dtype=float) - lo) / max(hi - lo, 1e-9)
    out = np.clip(out, 0.0, 1.0)
    return np.where(np.isfinite(out), out, 0.0)


def absorption_scores(
    ohlcv: pd.DataFrame,
    decision_ts_ms: np.ndarray,
    is_short: np.ndarray,
) -> np.ndarray:
    """Continuous absorption score in [0, 1] at each decision bar (causal)."""
    bar_ts = index_to_ms(ohlcv.index)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = (
        ohlcv["volume"].to_numpy(dtype=float)
        if "volume" in ohlcv.columns
        else np.ones(len(c), dtype=float)
    )
    spread = np.maximum(h - l, 1e-12)
    vol_ma = pd.Series(v).rolling(48, min_periods=12).mean().to_numpy()
    sp_ma = pd.Series(spread).rolling(48, min_periods=12).mean().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        rel_vol = v / np.where(vol_ma > 0, vol_ma, np.nan)
        rel_sp = spread / np.where(sp_ma > 0, sp_ma, np.nan)
        off_hi = (h - c) / spread
        off_lo = (c - l) / spread

    s_vol = _squash(rel_vol, 0.8, 2.0)
    s_sp = _squash(rel_sp, 0.7, 1.8)
    s_loc_short = _squash(off_hi, 0.35, 0.85)
    s_loc_long = _squash(off_lo, 0.35, 0.85)

    # Map decision timestamps onto bar indices (vectorized via searchsorted).
    ts = np.asarray(decision_ts_ms, dtype=np.int64)
    short = np.asarray(is_short, dtype=bool)
    idx = np.searchsorted(bar_ts, ts, side="left")
    ok = (idx < len(bar_ts)) & (bar_ts[np.clip(idx, 0, len(bar_ts) - 1)] == ts)
    idx_safe = np.where(ok, idx, 0)
    s_loc = np.where(short, s_loc_short[idx_safe], s_loc_long[idx_safe])
    out = (s_vol[idx_safe] + s_sp[idx_safe] + s_loc) / 3.0
    return np.where(ok, out, 0.0)


def train_threshold(scores: np.ndarray, *, q: float = 0.70) -> float:
    s = np.asarray(scores, dtype=float)
    s = s[np.isfinite(s)]
    if s.size < 30:
        return 0.55
    return float(np.nanpercentile(s, 100.0 * q))
