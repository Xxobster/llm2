"""Soft VSA score unit tests."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.pivot.strategy.soft_vsa import absorption_scores, train_threshold
from llm2.validation.folds import index_to_ms


def _ohlcv(n: int = 200) -> pd.DataFrame:
    idx = pd.date_range("2024-01-01", periods=n, freq="15min", tz="UTC")
    close = 100 + np.cumsum(np.random.default_rng(0).normal(0, 0.2, size=n))
    high = close + 0.5
    low = close - 0.5
    open_ = close
    vol = np.random.default_rng(1).uniform(100, 500, size=n)
    # spike volume + upper wick on last bar
    vol[-1] = 2000
    high[-1] = close[-1] + 2.0
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": vol},
        index=idx,
    )


def test_absorption_scores_in_unit_interval():
    ohlcv = _ohlcv()
    ts = index_to_ms(ohlcv.index)[-20:]
    short = np.ones(len(ts), dtype=bool)
    s = absorption_scores(ohlcv, ts, short)
    assert s.shape == ts.shape
    assert np.all((s >= 0.0) & (s <= 1.0))
    assert float(s[-1]) > float(np.median(s[:-1]))


def test_train_threshold_percentile():
    scores = np.linspace(0, 1, 100)
    thr = train_threshold(scores, q=0.70)
    assert abs(thr - 0.70) < 0.02
