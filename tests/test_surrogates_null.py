"""Surrogate null generators."""

from __future__ import annotations

import numpy as np

from llm2.audit.surrogates import apply_surrogate, list_surrogates


def test_surrogates_preserve_length():
    rng = np.random.default_rng(0)
    y = np.linspace(-1, 1, 50)
    for name in list_surrogates():
        out = apply_surrogate(y, name, rng=rng)
        assert len(out) == len(y)


def test_row_shuffle_permutation():
    rng = np.random.default_rng(1)
    y = np.arange(20, dtype=float)
    shuffled = apply_surrogate(y, "row_shuffle", rng=rng)
    assert set(shuffled) == set(y)
    assert not np.array_equal(shuffled, y)
