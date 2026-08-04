"""Unit tests for gen-1 single-book clarity × hold × TP signal builder."""

from __future__ import annotations

import numpy as np

from llm2.live.multitrade import mean_strength_ok
from llm2.signals.singlebook_clarity import (
    SingleBookArm,
    arm_grid,
    build_singlebook_signals,
)


def test_grid_has_twelve_arms() -> None:
    arms = arm_grid()
    assert len(arms) == 12
    assert {a.clarity for a in arms} == {"none", "mean_strength"}
    assert {a.horizon_bars for a in arms} == {6, 12}
    assert {a.tp_pct for a in arms} == {0.01, 0.015, 0.02618}


def test_mean_strength_primary_filters_weak_entries() -> None:
    n = 20
    ts = np.arange(n, dtype=np.int64) * 3_600_000
    side = np.ones(n, dtype=int)
    mean = np.full(n, 0.20, dtype=float)
    # Above min_edge but below median of prior 0.20 strengths
    mean[10:] = 0.11

    arm = SingleBookArm(clarity="mean_strength", horizon_bars=6, tp_pct=0.01)
    sigs, stats = build_singlebook_signals(ts, side, mean, arm=arm, min_edge=0.10, lookback=5)
    assert stats["n_candidates"] == n
    assert stats["n_skipped_clarity"] > 0
    assert stats["n_emitted"] < n
    assert all(s.target_offset == 0.01 for s in sigs)
    assert all(s.max_hold_bars == 6 for s in sigs)
    assert all(s.stop_offset == 0.02 for s in sigs)


def test_clarity_none_emits_all_above_edge() -> None:
    n = 10
    ts = np.arange(n, dtype=np.int64) * 3_600_000
    side = np.ones(n, dtype=int)
    mean = np.full(n, 0.15, dtype=float)
    arm = SingleBookArm(clarity="none", horizon_bars=12, tp_pct=0.02618)
    sigs, stats = build_singlebook_signals(ts, side, mean, arm=arm, min_edge=0.10)
    assert stats["n_emitted"] == n
    assert stats["n_skipped_clarity"] == 0
    assert len(sigs) == n
    assert sigs[0].max_hold_bars == 12
    assert sigs[0].target_offset == 0.02618


def test_mean_strength_ok_helper() -> None:
    assert mean_strength_ok(0.2, []) is True
    assert mean_strength_ok(0.2, [0.1, 0.1, 0.1]) is True
    assert mean_strength_ok(0.05, [0.2, 0.2, 0.2]) is False
