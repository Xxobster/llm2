"""Causal hunt-016 oscillator / pivot signals must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_m import IDEA_IDS_M, rsi_extreme_fade, signals_m


def _ohlcv(n: int = 1200, seed: int = 19) -> pd.DataFrame:
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
            "high": np.maximum(op, close) * 1.005,
            "low": np.minimum(op, close) * 0.995,
            "close": close,
            "volume": rng.random(n) * 100 + 1,
        },
        index=idx,
    )


def test_eight_ideas():
    assert len(IDEA_IDS_M) == 8
    assert "classic_pivot_fade" in IDEA_IDS_M
    assert "macd_hist_flip" in IDEA_IDS_M


def test_rsi_signed():
    sig = rsi_extreme_fade(_ohlcv(400), "1h")
    assert set(np.unique(sig)).issubset({-1.0, 0.0, 1.0})


def test_prefix_all_1h():
    df = _ohlcv(1600)
    full = signals_m(df, "1h")
    prefix = signals_m(df.iloc[:-80], "1h")
    assert set(full) == set(IDEA_IDS_M)
    for name in IDEA_IDS_M:
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)
