"""Causal hunt-007 confirm/session signals must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_d import IDEA_IDS_D, ny_cash_orb_follow, signals_d
from llm2.validation.folds import index_to_ms


def _ohlcv(n: int = 900, seed: int = 7, freq: str = "1h") -> pd.DataFrame:
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
            "high": np.maximum(op, close) * 1.004,
            "low": np.minimum(op, close) * 0.996,
            "close": close,
            "volume": rng.random(n) * 100 + 1,
        },
        index=idx,
    )


def test_eight_ideas():
    assert len(IDEA_IDS_D) == 8
    assert "failed_break_fade" in IDEA_IDS_D
    assert "ny_cash_orb_follow" in IDEA_IDS_D


def test_ny_cash_not_utc_midnight_1h():
    df = _ohlcv(400)
    sig = ny_cash_orb_follow(df, "1h")
    hour = (index_to_ms(df.index) % 86_400_000) // 3_600_000
    fired = np.flatnonzero(sig != 0)
    if fired.size:
        assert np.all(hour[fired] >= 14)


def test_prefix_core_ideas_1h():
    df = _ohlcv(1500)
    full = signals_d(df, "1h")
    prefix = signals_d(df.iloc[:-80], "1h")
    for name in ("failed_break_fade", "inside_break_follow", "ny_cash_orb_follow", "impulse_stall_fade"):
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)
