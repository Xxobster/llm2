"""Regime classification using past features; training target uses forward window stats."""

from __future__ import annotations

import numpy as np
import pandas as pd


def build_regime_labels(ohlcv: pd.DataFrame, *, horizon: int = 24) -> pd.DataFrame:
    c = ohlcv["close"].astype(float)
    log_ret = np.log(c.replace(0, np.nan)).diff()
    past_vol = log_ret.rolling(48, min_periods=12).std()
    past_trend = c.pct_change(48)

    # Forward window stats for training target (labels may use future)
    fwd_ret = np.log(c.shift(-horizon) / c.replace(0, np.nan))
    fwd_vol = log_ret.shift(-horizon).rolling(horizon, min_periods=max(4, horizon // 4)).std().shift(-horizon + 1)

    vol_med = past_vol.median()
    trend_abs_med = past_trend.abs().median()
    regime = np.full(len(ohlcv), "RANGE", dtype=object)
    high_vol = past_vol > vol_med
    strong_trend = past_trend.abs() > trend_abs_med
    regime[(~high_vol) & (~strong_trend)] = "RANGE"
    regime[(~high_vol) & strong_trend & (past_trend > 0)] = "TREND_UP"
    regime[(~high_vol) & strong_trend & (past_trend <= 0)] = "TREND_DOWN"
    regime[high_vol] = "HIGH_VOL"

    return pd.DataFrame(
        {
            "regime": regime,
            "fwd_return": fwd_ret,
            "fwd_vol": fwd_vol,
            "horizon": horizon,
        },
        index=ohlcv.index,
    )
