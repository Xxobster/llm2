"""Causal hunt-015 bar-shape / session ideas must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_l import IDEA_IDS_L, close_streak_fade, signals_l


def _ohlcv(n: int = 1200, seed: int = 17, freq: str = "1h") -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    op = np.empty_like(close)
    op[0] = close[0]
    op[1:] = close[:-1]
    idx = pd.date_range("2019-01-01", periods=n, freq=freq, tz="UTC")
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
    assert len(IDEA_IDS_L) == 8
    assert "nr7_break" in IDEA_IDS_L
    assert "utc_vwap_pullback" in IDEA_IDS_L


def test_streak_fade_is_signed():
    df = _ohlcv(400)
    sig = close_streak_fade(df, "1h")
    assert set(np.unique(sig)).issubset({-1.0, 0.0, 1.0})


def test_prefix_all_1h():
    df = _ohlcv(1600)
    full = signals_l(df, "1h")
    prefix = signals_l(df.iloc[:-80], "1h")
    assert set(full) == set(IDEA_IDS_L)
    for name in IDEA_IDS_L:
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)
