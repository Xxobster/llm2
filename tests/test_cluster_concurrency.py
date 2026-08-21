"""Unit tests for cluster concurrency signal builder."""

from __future__ import annotations

import numpy as np

from llm2.signals.cluster_concurrency import build_cluster_concurrent_signals
from llm2.signals.singlebook_clarity import SingleBookArm

ARM = SingleBookArm(clarity="none", horizon_bars=6, tp_pct=0.01, sl_pct=0.02)


def test_k1_emits_at_most_one_overlapping() -> None:
    # Signals every bar; with hold=6, K=1 should skip while "open"
    n = 20
    ts = np.arange(n, dtype=np.int64) * 3_600_000
    side = np.ones(n, dtype=int)
    mean = np.full(n, 0.2)
    sigs, stats = build_cluster_concurrent_signals(
        ts, side, mean, arm=ARM, min_edge=0.10, max_per_side=1, cluster_bars=None
    )
    assert stats["n_emitted"] < n
    assert stats["n_skipped_cap"] > 0
    assert all(s.meta["book_idx"] == 1 for s in sigs)


def test_k3_allows_addons_without_cluster() -> None:
    n = 10
    ts = np.arange(n, dtype=np.int64) * 3_600_000
    side = np.ones(n, dtype=int)
    mean = np.full(n, 0.2)
    sigs, stats = build_cluster_concurrent_signals(
        ts, side, mean, arm=ARM, min_edge=0.10, max_per_side=3, cluster_bars=None
    )
    assert stats["n_addon"] >= 1
    assert stats["n_emitted"] >= 3
    assert max(s.meta["book_idx"] for s in sigs) <= 3


def test_cluster_gate_blocks_late_addon() -> None:
    # Book1 at t=0; next signal at t=10h (> cluster 3) while still "open" → skip cluster
    ts = np.array([0, 10 * 3_600_000], dtype=np.int64)
    side = np.array([1, 1], dtype=int)
    mean = np.array([0.2, 0.2])
    arm = SingleBookArm(clarity="none", horizon_bars=12, tp_pct=0.01, sl_pct=0.02)
    sigs, stats = build_cluster_concurrent_signals(
        ts, side, mean, arm=arm, min_edge=0.10, max_per_side=3, cluster_bars=3
    )
    assert stats["n_emitted"] == 1
    assert stats["n_skipped_cluster"] == 1
    assert len(sigs) == 1


def test_cluster_gate_allows_near_addon() -> None:
    ts = np.array([0, 2 * 3_600_000], dtype=np.int64)
    side = np.array([1, 1], dtype=int)
    mean = np.array([0.2, 0.2])
    arm = SingleBookArm(clarity="none", horizon_bars=12, tp_pct=0.01, sl_pct=0.02)
    sigs, stats = build_cluster_concurrent_signals(
        ts, side, mean, arm=arm, min_edge=0.10, max_per_side=3, cluster_bars=3
    )
    assert stats["n_emitted"] == 2
    assert stats["n_addon"] == 1
    assert len(sigs) == 2


def test_size_double_within_3h() -> None:
    from tradesim.contracts import InstrumentSpec
    from llm2.signals.cluster_concurrency import build_cluster_size_signals

    spec = InstrumentSpec(
        symbol="ETHUSDT",
        tick_size=0.01,
        qty_step=0.01,
        min_qty=0.01,
        min_notional=5.0,
    )
    # t=0 -> 1x; t=2h -> 2x; t=10h is 8h after last entry -> 1x
    ts = np.array([0, 2, 10], dtype=np.int64) * 3_600_000
    side = np.ones(3, dtype=int)
    mean = np.full(3, 0.2)
    close = np.full(3, 3000.0)
    arm = SingleBookArm(clarity="none", horizon_bars=12, tp_pct=0.01, sl_pct=0.02)
    sigs, stats = build_cluster_size_signals(
        ts,
        side,
        mean,
        close,
        arm=arm,
        min_edge=0.10,
        max_per_side=3,
        instrument=spec,
        size_double_within_bars=3,
    )
    assert stats["n_size_2x"] == 1
    assert stats["n_size_1x"] == 2
    assert sigs[0].meta["size_mult"] == 1
    assert sigs[1].meta["size_mult"] == 2
    assert sigs[2].meta["size_mult"] == 1
    # qty is left unset; engine applies meta size_mult on sizing
    assert sigs[0].qty is None and sigs[1].qty is None
