"""Causal KReF / MoFE-lite forecasts must ignore later bars."""

from __future__ import annotations

import numpy as np

from llm2.ml_lab.kref import forward_return, kref_predict, lookback_embeddings
from llm2.ml_lab.mofe_lite import mofe_lite_predict


def _series(n: int = 800, seed: int = 7) -> np.ndarray:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    return 100.0 * np.exp(np.cumsum(r))


def test_kref_prefix_invariance():
    c = _series()
    full = kref_predict(c, lookback=16, archive=64, neighbors=8, horizon=4, purge=1)
    prefix = kref_predict(c[:-40], lookback=16, archive=64, neighbors=8, horizon=4, purge=1)
    a = full[:-40]
    b = prefix
    m = np.isfinite(a) & np.isfinite(b)
    assert int(m.sum()) > 50
    np.testing.assert_allclose(a[m], b[m], rtol=1e-5, atol=1e-6)


def test_mofe_prefix_invariance():
    c = _series()
    full = mofe_lite_predict(c, lookback=16)
    prefix = mofe_lite_predict(c[:-40], lookback=16)
    a = full[:-40]
    b = prefix
    m = np.isfinite(a) & np.isfinite(b)
    assert int(m.sum()) > 50
    np.testing.assert_allclose(a[m], b[m], rtol=1e-5, atol=1e-6)


def test_kref_is_not_the_label():
    c = _series()
    pred = kref_predict(c, lookback=16, archive=64, neighbors=8, horizon=4, purge=1)
    y = forward_return(c, 4)
    m = np.isfinite(pred) & np.isfinite(y)
    err = np.nanmean(np.abs(pred[m] - y[m]))
    assert err > 1e-4


def test_embeddings_row_t_uses_only_through_t():
    c = _series(200)
    emb = lookback_embeddings(c, lookback=8)
    c2 = c.copy()
    c2[-1] *= 1.05
    emb2 = lookback_embeddings(c2, lookback=8)
    np.testing.assert_allclose(emb[:-1], emb2[:-1], rtol=1e-6, atol=1e-7)
    assert not np.allclose(emb[-1], emb2[-1])
