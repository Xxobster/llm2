"""Causal hunt-009 invented formulas must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.causal_math import fracdiff, permutation_entropy, spectral_log_slope, teager_causal
from llm2.ml_lab.idea_catalog_f import IDEA_IDS_F, signals_f


def _ohlcv(n: int = 1200, seed: int = 3, freq: str = "1h") -> pd.DataFrame:
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


def test_twelve_ideas():
    assert len(IDEA_IDS_F) == 12
    assert "lag_beta_residual" in IDEA_IDS_F
    assert "value_pullback_er" in IDEA_IDS_F
    assert "perm_entropy_switch" in IDEA_IDS_F
    assert "spec_log_slope_switch" in IDEA_IDS_F


def test_fracdiff_causal():
    x = np.linspace(0.0, 1.0, 80)
    y = fracdiff(x)
    x2 = x.copy()
    x2[-5:] = 9.0
    y2 = fracdiff(x2)
    np.testing.assert_allclose(y[:-5], y2[:-5], rtol=1e-9, atol=1e-9)


def test_teager_no_future():
    r = np.arange(10, dtype=float)
    psi = teager_causal(r)
    assert np.isnan(psi[0]) and np.isnan(psi[1])
    np.testing.assert_allclose(psi[2], 1.0 - 0.0 * 2.0)


def test_perm_entropy_and_slope_prefix():
    r = np.random.default_rng(0).normal(size=400)
    pe = permutation_entropy(r)
    pe2 = permutation_entropy(r[:-40])
    m = np.isfinite(pe[:-40]) & np.isfinite(pe2)
    np.testing.assert_allclose(pe[:-40][m], pe2[m], rtol=1e-9, atol=1e-9)
    sl = spectral_log_slope(r)
    sl2 = spectral_log_slope(r[:-40])
    m2 = np.isfinite(sl[:-40]) & np.isfinite(sl2)
    np.testing.assert_allclose(sl[:-40][m2], sl2[m2], rtol=1e-9, atol=1e-9)


def test_prefix_signals_1h():
    df = _ohlcv(1500)
    other = df["close"].to_numpy(dtype=float) * 1.01
    full = signals_f(df, "1h", other_close=other)
    prefix = signals_f(df.iloc[:-80], "1h", other_close=other[:-80])
    assert set(full) == set(IDEA_IDS_F)
    for name in IDEA_IDS_F:
        a = full[name][:-80]
        b = prefix[name]
        m = np.isfinite(a) & np.isfinite(b)
        if int(m.sum()) < 20:
            continue
        np.testing.assert_allclose(a[m], b[m], rtol=1e-8, atol=1e-8)
