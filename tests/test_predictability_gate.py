"""The Stage-B predictability gate must be able to both pass and fail.

The previous implementation probed with a constant predictor, so its score was exactly 0
while the pass condition demanded > 1e-6. It returned False for every dataset ever tested
and silently capped all 148 generations at tier 0 (D-013). These tests fail the build if a
gate that cannot discriminate is reintroduced.
"""

from __future__ import annotations

import numpy as np
import pytest

from llm2.audit.predictability import (
    MIN_TRAIN_ROWS,
    audit_predictability,
    oos_skill,
    required_draws,
    required_surrogates_per_family,
)
from llm2.audit.surrogates import list_surrogates

N = 4000
N_FEATURES = 8

# An add-one permutation p-value cannot go below 1/(1+draws), so the draw count has to be
# large enough to express alpha at all.
DRAWS = required_surrogates_per_family(0.05, len(list_surrogates()))


def _design(seed: int) -> np.ndarray:
    return np.random.default_rng(seed).normal(size=(N, N_FEATURES))


def test_linear_signal_passes():
    """A label that genuinely is a linear function of X must be detected."""
    rng = np.random.default_rng(0)
    X = _design(0)
    y = 0.6 * X[:, 0] - 0.4 * X[:, 3] + rng.normal(0.0, 0.5, size=N)

    report = audit_predictability(X, y, target="synthetic_linear", n_surrogates=DRAWS, probes=("ridge",))

    assert report.passed, report.summary()
    assert report.real_score > 0.1, report.summary()
    assert report.p_value <= 0.05, report.summary()


def test_pure_noise_fails():
    """Labels independent of X must not pass, whatever the probe."""
    y = np.random.default_rng(1).normal(size=N)
    X = _design(2)

    report = audit_predictability(X, y, target="synthetic_noise", n_surrogates=DRAWS)

    assert not report.passed, report.summary()
    assert report.p_value > 0.05, report.summary()


def test_nonlinear_signal_is_reachable_by_the_boosted_probe():
    """An interaction a linear probe cannot see must still be detectable."""
    pytest.importorskip("lightgbm")
    rng = np.random.default_rng(3)
    X = _design(3)
    # Pure interaction: every marginal correlation with y is ~0.
    y = 1.5 * np.sign(X[:, 0]) * np.sign(X[:, 1]) + rng.normal(0.0, 0.5, size=N)

    report = audit_predictability(X, y, target="synthetic_xor", n_surrogates=DRAWS)

    assert report.passed, report.summary()
    assert report.per_probe_real.get("lgbm", -9.9) > report.per_probe_real.get("ridge", 9.9), (
        f"boosted probe should beat the linear probe here: {report.per_probe_real}"
    )


def test_constant_predictor_scores_exactly_zero():
    """The metric must give a constant predictor 0, not a tiny positive epsilon.

    This is the precise defect that made the old gate unconditionally false.
    """
    y_train = np.random.default_rng(4).normal(1.7, 0.3, size=1000)
    y_test = np.random.default_rng(5).normal(1.7, 0.3, size=1000)
    train_mean = float(np.mean(y_train))

    skill = oos_skill(y_test, np.full(len(y_test), train_mean), train_mean)

    assert skill == pytest.approx(0.0, abs=1e-12), skill


def test_gate_is_not_unconditionally_false():
    """Guard the class of bug, not the instance: pass and fail must both be reachable."""
    rng = np.random.default_rng(6)
    X = _design(6)
    signal = 0.8 * X[:, 2] + rng.normal(0.0, 0.4, size=N)
    noise = rng.normal(size=N)

    passing = audit_predictability(X, signal, n_surrogates=DRAWS, probes=("ridge",))
    failing = audit_predictability(X, noise, n_surrogates=DRAWS, probes=("ridge",))

    assert passing.passed and not failing.passed, (
        f"gate cannot discriminate: signal={passing.summary()} noise={failing.summary()}"
    )


def test_underpowered_draw_count_is_reported_not_silently_failed():
    """Too few draws cannot express alpha; that must be labelled, not read as 'no signal'.

    A structural inability to reject is exactly what D-013 was, and it must never again be
    presented as a negative result.
    """
    rng = np.random.default_rng(11)
    X = _design(11)
    y = 0.9 * X[:, 0] + rng.normal(0.0, 0.3, size=N)

    report = audit_predictability(X, y, n_surrogates=1, alpha=0.05, probes=("ridge",))

    assert not report.passed
    assert "underpowered" in report.reason, report.summary()
    # The signal is overwhelming; only the draw count stopped it passing.
    assert report.real_score > 0.5, report.summary()
    assert report.real_score > report.surrogate_max, report.summary()


def test_required_draws_matches_the_add_one_floor():
    for alpha in (0.05, 0.01, 0.10):
        n = required_draws(alpha)
        assert 1.0 / (1.0 + n) <= alpha
        assert 1.0 / (1.0 + (n - 1)) > alpha


def test_insufficient_rows_fails_closed_with_a_reason():
    X = np.random.default_rng(7).normal(size=(MIN_TRAIN_ROWS, N_FEATURES))
    y = np.random.default_rng(8).normal(size=MIN_TRAIN_ROWS)

    report = audit_predictability(X, y, n_surrogates=2, probes=("ridge",))

    assert not report.passed
    assert "insufficient rows" in report.reason


def test_degenerate_label_fails_closed_with_a_reason():
    X = _design(9)
    y = np.full(N, 0.02)

    report = audit_predictability(X, y, n_surrogates=2, probes=("ridge",))

    assert not report.passed
    assert "degenerate label" in report.reason


def test_non_finite_rows_are_dropped_not_imputed():
    """NaN features must not silently become zeros and manufacture structure."""
    rng = np.random.default_rng(10)
    X = _design(10)
    y = 0.6 * X[:, 0] + rng.normal(0.0, 0.5, size=N)
    X[::7, 1] = np.nan

    report = audit_predictability(X, y, n_surrogates=DRAWS, probes=("ridge",))

    assert report.passed, report.summary()
