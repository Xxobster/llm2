"""Causal hunt-011 second formula pack must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.causal_math import hurst_rs
from llm2.ml_lab.idea_catalog_h import IDEA_IDS_H, signals_h


def _ohlcv(n: int = 1200, seed: int = 41) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    op = np.empty_like(close)
    op[0] = close[0]
    op[1:] = close[:-1]
    idx = pd.date_range("2019-01-01", periods=n, freq="1h", tz="UTC")
    return pd.DataFrame(
        {
            "open": op,
            "high": np.maximum(op, close) * 1.004,
            "low": np.minimum(op, close) * 0.996,
            "close": close,
            "volume": rng.random(n) * 100 + 1,
        },
        index=idx,
    )


def test_eight_ideas():
    assert len(IDEA_IDS_H) == 8


def test_hurst_prefix():
    r = np.random.default_rng(2).normal(size=400)
    a = hurst_rs(r)
    b = hurst_rs(r[:-40])
    m = np.isfinite(a[:-40]) & np.isfinite(b)
    np.testing.assert_allclose(a[:-40][m], b[m], rtol=1e-9, atol=1e-9)


def test_prefix_all_1h():
    df = _ohlcv(1500)
    full = signals_h(df, "1h")
    prefix = signals_h(df.iloc[:-80], "1h")
    assert set(full) == set(IDEA_IDS_H)
    for name in IDEA_IDS_H:
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)
