"""Tests for hit-probability calibration helpers."""

from __future__ import annotations

import numpy as np

from llm2.audit.cost_hurdle import CostHurdle
from llm2.decision.calibrate import (
    bracket_path_hit_labels,
    direction_hit_labels,
    fit_hit_calibrator,
    train_calib_split,
)


def test_cost_hurdle_pi_star_above_half_for_asymmetric_bracket():
    h = CostHurdle(tp_pct=0.01, sl_pct=0.02)
    pi = h.break_even_probability()
    assert 0.65 < pi < 0.85  # ~0.72 with fees


def test_isotonic_monotonic_on_synthetic():
    rng = np.random.default_rng(0)
    x = rng.uniform(0.05, 0.9, size=400)
    # higher score → higher hit rate
    y = (rng.random(400) < (0.3 + 0.6 * x)).astype(float)
    cal = fit_hit_calibrator(x, y, min_points=50)
    assert cal.fitted
    p_lo = float(cal.predict_proba_hit(np.array([0.1]))[0])
    p_hi = float(cal.predict_proba_hit(np.array([0.8]))[0])
    assert p_hi >= p_lo - 1e-6


def test_direction_hit_labels():
    mean = np.array([0.5, -0.5, 0.05, 0.3])
    y = np.array([1.0, -1.0, 1.0, -1.0])
    abs_m, hit, over = direction_hit_labels(mean, y, min_edge=0.10)
    assert over.tolist() == [True, True, False, True]
    assert hit[0] == 1.0
    assert hit[1] == 1.0
    assert hit[3] == 0.0


def test_train_calib_split_not_collapsed():
    split, n_cal = train_calib_split(15072, calib_frac=0.20, min_calib=200, min_fit=500)
    assert n_cal >= 200
    assert split + n_cal == 15072
    assert abs(n_cal / 15072 - 0.20) < 0.02


def test_bracket_path_hit_tp_long():
    # flat then spike high to +1% TP
    n = 20
    close = np.full(n, 100.0)
    high = np.full(n, 100.0)
    low = np.full(n, 100.0)
    high[5] = 101.5  # TP hit
    mean = np.zeros(n)
    mean[0] = 0.5  # long signal at bar 0
    abs_m, hit, over = bracket_path_hit_labels(
        high, low, close, mean, tp_pct=0.01, sl_pct=0.02, hold_bars=12, min_edge=0.10
    )
    assert over[0]
    assert hit[0] == 1.0
