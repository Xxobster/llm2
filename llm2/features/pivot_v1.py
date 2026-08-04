"""Pivot / swing proximity features (v1)."""

from __future__ import annotations

import numpy as np
import pandas as pd


def build_pivot_v1(ohlcv: pd.DataFrame, *, window: int = 5) -> pd.DataFrame:
    """Distance to rolling swing high/low normalized by ATR proxy."""
    df = ohlcv.sort_index()
    h, l, c = df["high"].astype(float), df["low"].astype(float), df["close"].astype(float)
    out = pd.DataFrame(index=df.index)

    prev = c.shift(1)
    tr = pd.concat([(h - l), (h - prev).abs(), (l - prev).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14, min_periods=1).mean().replace(0, np.nan)

    for w in (window, window * 3, window * 6):
        swing_hi = h.rolling(w, min_periods=1).max()
        swing_lo = l.rolling(w, min_periods=1).min()
        out[f"dist_swing_hi_{w}"] = (c - swing_hi) / atr
        out[f"dist_swing_lo_{w}"] = (c - swing_lo) / atr
        out[f"pivot_mid_dist_{w}"] = (c - (swing_hi + swing_lo) / 2.0) / atr

    typical = (h + l + c) / 3.0
    v = df["volume"].astype(float) if "volume" in df.columns else pd.Series(1.0, index=df.index)
    for w in (24, 48):
        v_sum = v.rolling(w, min_periods=1).sum().replace(0, np.nan)
        vwap = (typical * v).rolling(w, min_periods=1).sum() / v_sum
        out[f"vwap_dist_{w}"] = (c - vwap) / atr

    return out.replace([np.inf, -np.inf], np.nan)
