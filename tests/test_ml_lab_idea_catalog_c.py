"""Causal hunt-006 signals must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_c import IDEA_IDS_C, close_streak_fade, close_streak_follow, signals_c


def _ohlcv(n: int = 900, seed: int = 11) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    idx = pd.date_range("2019-01-01", periods=n, freq="1h", tz="UTC")
    return pd.DataFrame(
        {
            "open": close,
            "high": close * 1.002,
            "low": close * 0.998,
            "close": close,
            "volume": rng.random(n) * 100 + 1,
        },
        index=idx,
    )


def test_eight_ideas():
    assert len(IDEA_IDS_C) == 8


def test_fade_is_opposite_of_follow():
    df = _ohlcv(400)
    np.testing.assert_array_equal(close_streak_fade(df), -close_streak_follow(df))


def test_prefix_asia_vwap_rsi():
    df = _ohlcv(1500)
    full = signals_c(df, "1h")
    prefix = signals_c(df.iloc[:-80], "1h")
    for name in ("asia_range_break", "utc_vwap_reclaim", "rsi_hook", "macd_hist_cross"):
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)
