"""Causal hunt-010 contaminated-tune signals must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_g import IDEA_IDS_G, ema_stack_first_on, failed_break_wick, signals_g
from llm2.validation.folds import index_to_ms


def _ohlcv(n: int = 1200, seed: int = 11, freq: str = "1h") -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    op = np.empty_like(close)
    op[0] = close[0]
    op[1:] = close[:-1]
    idx = pd.date_range("2019-01-01", periods=n, freq=freq, tz="UTC")
    high = np.maximum(op, close) * 1.01
    low = np.minimum(op, close) * 0.99
    return pd.DataFrame(
        {"open": op, "high": high, "low": low, "close": close, "volume": rng.random(n) * 100 + 1},
        index=idx,
    )


def test_ten_ideas():
    assert len(IDEA_IDS_G) == 10
    assert "failed_break_hold2" in IDEA_IDS_G
    assert "failed_break_n55" in IDEA_IDS_G
    assert "ema_stack_pullback" in IDEA_IDS_G
    assert "ema_stack_first_on" in IDEA_IDS_G


def test_wick_same_bar_not_next():
    df = _ohlcv(400)
    sig = failed_break_wick(df)
    assert sig.dtype == np.float64
    assert set(np.unique(sig)).issubset({-1.0, 0.0, 1.0})


def test_first_on_sparser_than_always_stack():
    df = _ohlcv(800)
    first = ema_stack_first_on(df)
    assert int(np.count_nonzero(first)) < 400


def test_prefix_all_ideas_1h():
    df = _ohlcv(1600)
    full = signals_g(df, "1h")
    prefix = signals_g(df.iloc[:-80], "1h")
    assert set(full) == set(IDEA_IDS_G)
    for name in IDEA_IDS_G:
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)


def test_ny_orb_hold_not_before_14():
    df = _ohlcv(400)
    sig = signals_g(df, "1h")["ny_orb_hold"]
    hour = (index_to_ms(df.index) % 86_400_000) // 3_600_000
    fired = np.flatnonzero(sig != 0)
    if fired.size:
        assert np.all(hour[fired] >= 14)
