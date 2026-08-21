"""Unit tests for proportional TP scaling (frozen nested formula)."""

from __future__ import annotations

import math

import pytest

from llm2.live.multitrade import scale_tp_by_abs_mean


def test_floor_at_base_when_weak() -> None:
    # |mean|=0.10 → factor 0.2 → clipped to 1 → TP 1%
    assert scale_tp_by_abs_mean(0.01, 0.10) == pytest.approx(0.01)


def test_proportional_mid() -> None:
    # |mean|=0.75 → factor 1.5 → TP 1.5%
    assert scale_tp_by_abs_mean(0.01, 0.75) == pytest.approx(0.015)


def test_cap_at_2x() -> None:
    # |mean|=2.0 → factor 4 → clipped to 2 → TP 2%
    assert scale_tp_by_abs_mean(0.01, 2.0) == pytest.approx(0.02)


def test_exact_ref_is_1x() -> None:
    assert scale_tp_by_abs_mean(0.01, 0.5) == pytest.approx(0.01)


def test_bad_ref() -> None:
    with pytest.raises(ValueError):
        scale_tp_by_abs_mean(0.01, 0.5, ref=0.0)


def test_finite() -> None:
    v = scale_tp_by_abs_mean(0.01, 1.0)
    assert math.isfinite(v)
    assert 0.01 <= v <= 0.02
