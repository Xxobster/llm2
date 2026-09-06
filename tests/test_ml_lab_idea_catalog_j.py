"""Causal hunt-013 third formula pack must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.causal_math import dfa_alpha, fisher_rank, inst_amplitude, volterra_quad_resid
from llm2.ml_lab.idea_catalog_j import IDEA_IDS_J, signals_j


def _ohlcv(n: int = 1200, seed: int = 13) -> pd.DataFrame:
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
            "high": np.maximum(op, close) * 1.004,
            "low": np.minimum(op, close) * 0.996,
            "close": close,
            "volume": rng.random(n) * 100 + 1,
        },
        index=idx,
    )


def test_ten_ideas():
    assert len(IDEA_IDS_J) == 10
    assert "hilbert_amp_fade" in IDEA_IDS_J
    assert "dfa_alpha_switch" in IDEA_IDS_J
    assert "volterra_resid_fade" in IDEA_IDS_J


def test_signals_are_signed():
    sigs = signals_j(_ohlcv(800), "1h")
    for name, arr in sigs.items():
        uniq = set(np.unique(arr[~np.isnan(arr)]))
        assert uniq <= {-1.0, 0.0, 1.0}, name


def test_primitives_prefix():
    r = np.random.default_rng(4).normal(size=500)
    for fn in (dfa_alpha, fisher_rank, inst_amplitude, volterra_quad_resid):
        a = fn(r)
        b = fn(r[:-50])
        m = np.isfinite(a[:-50]) & np.isfinite(b)
        assert int(m.sum()) > 20, fn.__name__
        np.testing.assert_allclose(a[:-50][m], b[m], rtol=1e-8, atol=1e-8)


def test_prefix_all_1h():
    df = _ohlcv(1500)
    full = signals_j(df, "1h")
    prefix = signals_j(df.iloc[:-80], "1h")
    assert set(full) == set(IDEA_IDS_J)
    for name in IDEA_IDS_J:
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-8, atol=1e-8)
