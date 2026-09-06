"""Causal 15-minute sign-reversal control must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.regime_audit import fit_assign_regimes, regime_features
from llm2.ml_lab.reversal import (
    DEFAULT_ROLL,
    bar_return,
    reversal_confidence,
    reversal_signal,
)


def _series(n: int = 800, seed: int = 11) -> np.ndarray:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    return 100.0 * np.exp(np.cumsum(r))


def test_signal_is_minus_sign_of_current_return():
    c = _series()
    r = bar_return(c)
    s = reversal_signal(c)
    m = np.isfinite(r) & (np.sign(r) != 0)
    np.testing.assert_array_equal(s[m], -np.sign(r[m]))
    assert s[0] == 0.0


def test_reversal_signal_prefix_invariance():
    c = _series()
    full = reversal_signal(c)
    prefix = reversal_signal(c[:-40])
    np.testing.assert_allclose(full[:-40], prefix, rtol=1e-12, atol=1e-12)


def test_reversal_confidence_prefix_invariance():
    c = _series(1200)
    full = reversal_confidence(c, roll=DEFAULT_ROLL)
    prefix = reversal_confidence(c[:-40], roll=DEFAULT_ROLL)
    a = full[:-40]
    b = prefix
    m = np.isfinite(a) & np.isfinite(b)
    assert int(m.sum()) > 200
    np.testing.assert_allclose(a[m], b[m], rtol=1e-12, atol=1e-12)


def test_last_bar_does_not_change_earlier_confidence():
    c = _series(1200)
    c2 = c.copy()
    c2[-1] *= 1.05
    a = reversal_confidence(c, roll=DEFAULT_ROLL)
    b = reversal_confidence(c2, roll=DEFAULT_ROLL)
    cut = DEFAULT_ROLL + 5
    m = np.isfinite(a[:-cut]) & np.isfinite(b[:-cut])
    assert int(m.sum()) > 200
    np.testing.assert_allclose(a[:-cut][m], b[:-cut][m], rtol=1e-12, atol=1e-12)
    s1 = reversal_signal(c)
    s2 = reversal_signal(c2)
    np.testing.assert_array_equal(s1[:-1], s2[:-1])


def test_confidence_does_not_use_current_hit():
    """At t, confidence windows end at hit[t-1], never hit[t] (which needs t+1)."""
    c = _series(400)
    conf = reversal_confidence(c, roll=32)
    c2 = c.copy()
    c2[-1] *= 1.08
    conf2 = reversal_confidence(c2, roll=32)
    # hit[-1] is always unused; mutating the last close may change conf[-1]
    # (via hit[-2]) but not conf[:-33].
    m = np.isfinite(conf[:-33]) & np.isfinite(conf2[:-33])
    np.testing.assert_allclose(conf[:-33][m], conf2[:-33][m], rtol=1e-12, atol=1e-12)


def test_regime_centres_ignore_suffix():
    n = 600
    rng = np.random.default_rng(3)
    idx = pd.RangeIndex(n)
    close = 100 * np.exp(np.cumsum(rng.normal(0, 0.01, n)))
    high = close * (1.0 + rng.random(n) * 0.002)
    low = close * (1.0 - rng.random(n) * 0.002)
    ohlcv = pd.DataFrame({"open": close, "high": high, "low": low, "close": close}, index=idx)
    feat = regime_features(ohlcv)
    lab1 = fit_assign_regimes(feat, train_end=250, k=3, seed=7)
    feat2 = feat.copy()
    feat2[400:] *= 3.0
    lab2 = fit_assign_regimes(feat2, train_end=250, k=3, seed=7)
    m = (lab1[:250] >= 0) & (lab2[:250] >= 0)
    assert int(m.sum()) > 50
    np.testing.assert_array_equal(lab1[:250][m], lab2[:250][m])
