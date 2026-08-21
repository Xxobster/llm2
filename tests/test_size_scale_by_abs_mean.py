"""Unit tests: size mult proportional to |pred_mean|."""

from __future__ import annotations

import numpy as np
import pytest

from llm2.live.multitrade import scale_size_mult_by_abs_mean, scale_tp_by_abs_mean
from llm2.signals.cluster_concurrency import build_cluster_size_signals
from llm2.signals.singlebook_clarity import SingleBookArm
from tradesim.contracts import InstrumentSpec


def test_size_factor_matches_tp_kernel() -> None:
    assert scale_size_mult_by_abs_mean(0.10) == pytest.approx(1.0)
    assert scale_size_mult_by_abs_mean(0.75) == pytest.approx(1.5)
    assert scale_size_mult_by_abs_mean(2.0) == pytest.approx(2.0)
    assert scale_size_mult_by_abs_mean(0.5) == pytest.approx(1.0)
    # TP uses same factor times base
    assert scale_tp_by_abs_mean(0.01, 0.75) == pytest.approx(
        0.01 * scale_size_mult_by_abs_mean(0.75)
    )


def test_cluster_size_scale_by_abs_mean() -> None:
    spec = InstrumentSpec(
        symbol="ETHUSDT",
        tick_size=0.01,
        qty_step=0.01,
        min_qty=0.01,
        min_notional=5.0,
    )
    # Three isolated entries (far apart): no time double; strength scale only
    ts = np.array([0, 20, 40], dtype=np.int64) * 3_600_000
    side = np.ones(3, dtype=int)
    mean = np.array([0.10, 0.50, 1.00])  # factors 1.0, 1.0, 2.0 at ref=0.5
    close = np.full(3, 3000.0)
    arm = SingleBookArm(clarity="none", horizon_bars=6, tp_pct=0.01, sl_pct=0.02)
    sigs, stats = build_cluster_size_signals(
        ts,
        side,
        mean,
        close,
        arm=arm,
        min_edge=0.10,
        max_per_side=3,
        instrument=spec,
        size_double_within_bars=0,
        size_scale_by_abs_mean=True,
        size_scale_ref=0.5,
        size_scale_factor_min=1.0,
        size_scale_factor_max=2.0,
    )
    assert len(sigs) == 3
    assert sigs[0].meta["size_mult"] == pytest.approx(1.0)
    assert sigs[1].meta["size_mult"] == pytest.approx(1.0)
    assert sigs[2].meta["size_mult"] == pytest.approx(2.0)
    assert stats["n_size_strength_scaled"] == 3
    assert stats["mean_size_mult"] == pytest.approx(4.0 / 3.0)
