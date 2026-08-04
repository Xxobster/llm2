"""The diagnostics statistics must not manufacture significance from dependence."""

from __future__ import annotations

import numpy as np
import pytest

from llm2.diagnostics.stats import (
    Effect,
    apply_fdr,
    benjamini_hochberg,
    bootstrap_corr_test,
    newey_west_tstat,
    optimal_block_length,
    safe_corr,
    stationary_bootstrap_indices,
)


def test_benjamini_hochberg_matches_known_values():
    p = np.array([0.001, 0.008, 0.039, 0.041, 0.042, 0.06, 0.074, 0.205])
    q = benjamini_hochberg(p)
    assert q[0] == pytest.approx(0.008, abs=1e-9)
    assert np.all(np.diff(q) >= -1e-12), "q-values must be monotone in p"
    assert np.all(q >= p - 1e-12), "q must never be smaller than p"


def test_benjamini_hochberg_controls_false_discoveries_under_the_null():
    rng = np.random.default_rng(0)
    p = rng.uniform(size=2000)  # all null
    q = benjamini_hochberg(p)
    assert (q <= 0.05).sum() <= 5, f"{(q <= 0.05).sum()} false discoveries from pure noise"


def test_a_lone_marginal_hit_does_not_survive_a_large_scan():
    """One p=0.03 among 99 nulls is what a 40-series lag scan produces by chance."""
    rng = np.random.default_rng(11)
    effects = [Effect(name="hit", statistic=0.1, n=1000, p_value=0.03)]
    effects += [
        Effect(name=f"null{i}", statistic=0.0, n=1000, p_value=float(p))
        for i, p in enumerate(rng.uniform(0.1, 1.0, size=99))
    ]

    apply_fdr(effects)

    assert not effects[0].significant, (
        f"a single marginal result in a 100-test scan survived FDR (q={effects[0].q_value:.3f})"
    )


def test_a_coherent_block_of_hits_does_survive():
    """FDR is not Bonferroni: many concordant small p-values should still be reported."""
    rng = np.random.default_rng(12)
    effects = [Effect(name=f"hit{i}", statistic=0.2, n=1000, p_value=1e-5) for i in range(20)]
    effects += [
        Effect(name=f"null{i}", statistic=0.0, n=1000, p_value=float(p))
        for i, p in enumerate(rng.uniform(0.1, 1.0, size=80))
    ]

    apply_fdr(effects)

    assert sum(e.significant for e in effects) == 20


def test_safe_corr_is_nan_not_zero_when_undefined():
    assert np.isnan(safe_corr(np.ones(200), np.arange(200.0)))
    assert np.isnan(safe_corr(np.arange(5.0), np.arange(5.0)))


def test_safe_corr_recovers_a_known_relationship():
    rng = np.random.default_rng(1)
    x = rng.normal(size=5000)
    y = 0.5 * x + rng.normal(0, 0.5, size=5000)
    assert safe_corr(x, y) == pytest.approx(0.707, abs=0.03)


def test_spearman_is_robust_to_a_monotone_transform():
    rng = np.random.default_rng(2)
    x = rng.normal(size=3000)
    y = np.exp(3 * x)  # monotone but wildly non-linear
    assert safe_corr(x, y, method="spearman") > 0.99
    assert safe_corr(x, y, method="pearson") < 0.9


def test_block_length_grows_with_persistence():
    rng = np.random.default_rng(3)
    n = 5000
    white = rng.normal(size=n)
    persistent = np.zeros(n)
    for i in range(1, n):
        persistent[i] = 0.9 * persistent[i - 1] + rng.normal()
    assert optimal_block_length(persistent) > optimal_block_length(white)


def test_stationary_bootstrap_indices_are_in_range_and_blocky():
    rng = np.random.default_rng(4)
    n, block = 500, 20
    idx = stationary_bootstrap_indices(n, block, rng, n_boot=50)
    assert idx.shape == (50, n)
    assert idx.min() >= 0 and idx.max() < n
    # Consecutive-by-one steps should dominate if blocks are being preserved.
    steps = np.diff(idx, axis=1)
    assert (steps == 1).mean() > 0.7


def test_circular_shift_null_does_not_call_spurious_correlation_significant():
    """Two independent but strongly autocorrelated series must not look related.

    This is the failure mode the whole module exists to prevent: a naive p-value on two
    random walks reports overwhelming significance.
    """
    rng = np.random.default_rng(5)
    n = 4000
    a = np.cumsum(rng.normal(size=n))
    b = np.cumsum(rng.normal(size=n))

    effect = bootstrap_corr_test(a, b, n_boot=300, seed=7)

    assert not effect.significant or np.isnan(effect.p_value), (
        f"independent random walks flagged as related: r={effect.statistic:.3f} p={effect.p_value:.4f}"
    )
    apply_fdr([effect])
    assert not effect.significant


def test_bootstrap_corr_test_still_detects_a_real_relationship():
    rng = np.random.default_rng(6)
    n = 4000
    x = rng.normal(size=n)
    y = 0.4 * x + rng.normal(0, 0.5, size=n)

    effect = bootstrap_corr_test(x, y, n_boot=300, seed=8)

    assert effect.statistic > 0.4
    assert effect.p_value < 0.05
    assert effect.ci_low > 0.0, "interval should exclude zero for a genuine relationship"


def test_newey_west_tstat_shrinks_under_overlap():
    """Overlapping windows inflate the naive t-statistic; the correction must undo that."""
    rng = np.random.default_rng(9)
    base = rng.normal(0.01, 1.0, size=6000)
    overlapping = np.convolve(base, np.ones(24) / 24, mode="valid")  # 24-bar overlap

    mean, t_hac = newey_west_tstat(overlapping)
    t_naive = mean / (overlapping.std(ddof=1) / np.sqrt(overlapping.size))

    assert abs(t_hac) < abs(t_naive), f"hac={t_hac:.2f} naive={t_naive:.2f}"
