"""Lightweight bar series for tradesim arms without full pivot scoring."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from llm2.validation.folds import index_to_ms


def _atr_frac(ohlcv: pd.DataFrame, period: int = 14) -> np.ndarray:
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    prev_c = np.roll(c, 1)
    prev_c[0] = c[0]
    tr = np.maximum(h - l, np.maximum(np.abs(h - prev_c), np.abs(l - prev_c)))
    atr = pd.Series(tr).ewm(alpha=1.0 / period, adjust=False).mean().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        out = atr / np.where(c > 0, c, np.nan)
    return out.astype(float)


@dataclass
class BarSeries:
    """Minimal stand-in for ScoredOOS fields used by confluence.sim_arms."""

    symbol: str
    timeframe: str
    ohlcv: pd.DataFrame
    ts_ms: np.ndarray
    close: np.ndarray
    atr_frac: np.ndarray


def make_bar_series(symbol: str, timeframe: str, ohlcv: pd.DataFrame) -> BarSeries:
    return BarSeries(
        symbol=symbol,
        timeframe=timeframe,
        ohlcv=ohlcv,
        ts_ms=index_to_ms(ohlcv.index),
        close=ohlcv["close"].to_numpy(dtype=float),
        atr_frac=_atr_frac(ohlcv),
    )
