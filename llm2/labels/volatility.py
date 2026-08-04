"""Realized volatility over forward window (label uses future — features must not)."""

from __future__ import annotations

import pandas as pd


def build_volatility_labels(ohlcv: pd.DataFrame, *, horizon: int = 24) -> pd.DataFrame:
    h = ohlcv["high"].astype(float)
    l = ohlcv["low"].astype(float)
    c = ohlcv["close"].astype(float)
    fwd_hi = h.rolling(horizon, min_periods=1).max().shift(-horizon + 1)
    fwd_lo = l.rolling(horizon, min_periods=1).min().shift(-horizon + 1)
    realized_range = (fwd_hi - fwd_lo) / c.replace(0, float("nan"))
    return pd.DataFrame({"volatility": realized_range, "horizon": horizon}, index=ohlcv.index)
