"""Causal hunt-012 FVG signals must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_i import (
    IDEA_IDS_I,
    _fvg_arrays,
    fvg_follow,
    fvg_pullback_long,
    signals_i,
)


def _ohlcv(n: int = 1200, seed: int = 55) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    op = np.empty_like(close)
    op[0] = close[0]
    op[1:] = close[:-1]
    idx = pd.date_range("2019-01-01", periods=n, freq="1h", tz="UTC")
    high = np.maximum(op, close) * 1.005
    low = np.minimum(op, close) * 0.995
    return pd.DataFrame(
        {"open": op, "high": high, "low": low, "close": close, "volume": rng.random(n) * 100 + 1},
        index=idx,
    )


def test_eight_ideas():
    assert len(IDEA_IDS_I) == 8


def test_fvg_arrays_causal():
    """Changing future bars must not alter past FVG detections."""
    df = _ohlcv(600)
    h = df["high"].to_numpy(float)
    l = df["low"].to_numpy(float)
    bt, bb, _, _ = _fvg_arrays(h, l)
    h2, l2 = h.copy(), l.copy()
    h2[-50:] *= 1.1
    l2[-50:] *= 0.9
    bt2, bb2, _, _ = _fvg_arrays(h2, l2)
    np.testing.assert_allclose(bt[:-50], bt2[:-50], rtol=1e-9, atol=1e-9)
    np.testing.assert_allclose(bb[:-50], bb2[:-50], rtol=1e-9, atol=1e-9)


def test_fvg_follow_values():
    df = _ohlcv(400)
    sig = fvg_follow(df, "1h")
    assert sig.dtype == np.float64
    assert set(np.unique(sig)).issubset({-1.0, 0.0, 1.0})


def test_fvg_pullback_long_no_future():
    """No fire before bar 2 (need two prior bars for gap detection)."""
    df = _ohlcv(400)
    sig = fvg_pullback_long(df, "1h")
    assert sig[0] == 0.0 and sig[1] == 0.0


def test_prefix_all_1h():
    df = _ohlcv(1500)
    full = signals_i(df, "1h")
    prefix = signals_i(df.iloc[:-80], "1h")
    assert set(full) == set(IDEA_IDS_I)
    for name in IDEA_IDS_I:
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)
