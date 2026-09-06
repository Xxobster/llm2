"""Causal hunt-014 higher-timeframe Fair Value Gap signals must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_k import IDEA_IDS_K, htf_fvg_follow, signals_k, utc_midnight_fade


def _ohlcv(n: int = 1200, seed: int = 13, freq: str = "1h") -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    op = np.empty_like(close)
    op[0] = close[0]
    op[1:] = close[:-1]
    idx = pd.date_range("2019-01-01", periods=n, freq=freq, tz="UTC")
    high = np.maximum(op, close) * 1.006
    low = np.minimum(op, close) * 0.994
    return pd.DataFrame(
        {"open": op, "high": high, "low": low, "close": close, "volume": rng.random(n) * 100 + 1},
        index=idx,
    )


def test_eight_ideas():
    assert len(IDEA_IDS_K) == 8
    assert "htf_fvg_follow" in IDEA_IDS_K
    assert "utc_midnight_fade" in IDEA_IDS_K


def test_htf_follow_only_on_bucket_open():
    df = _ohlcv(800)
    sig = htf_fvg_follow(df, "1h")
    assert sig.dtype == np.float64
    assert set(np.unique(sig)).issubset({-1.0, 0.0, 1.0})
    hour = df.index.tz_convert("UTC").hour
    fired = np.flatnonzero(sig != 0.0)
    if fired.size:
        assert np.all(np.isin(hour[fired], (0, 4, 8, 12, 16, 20)))


def test_utc_midnight_only_hour_zero():
    df = _ohlcv(400)
    sig = utc_midnight_fade(df, "1h")
    fired = np.flatnonzero(sig != 0.0)
    if fired.size:
        assert np.all(df.index[fired].tz_convert("UTC").hour == 0)


def test_prefix_all_1h():
    df = _ohlcv(1600)
    full = signals_k(df, "1h")
    prefix = signals_k(df.iloc[:-80], "1h")
    assert set(full) == set(IDEA_IDS_K)
    for name in IDEA_IDS_K:
        a = full[name][:-80]
        b = prefix[name]
        cut = 16
        np.testing.assert_allclose(a[:-cut], b[:-cut], rtol=1e-9, atol=1e-9)
