"""Unit tests for eth multitrade nested signal clarity_scope."""

from __future__ import annotations

import numpy as np

from llm2.experiments.eth_multitrade_nested import build_multitrade_signals, live_control_cfg


def test_clarity_scope_all_can_skip_primary():
    cfg = live_control_cfg()
    cfg["clarity_scope"] = "all"
    # First bar weak, second stronger than median history after first append path
    n = 5
    ts = (np.arange(n) * 3_600_000).astype(np.int64)
    side = np.array([1, 1, 1, 1, 1], dtype=int)
    # Starts with a medium signal that passes empty-history clarity, then a weaker
    # one that fails median gate while stack is empty (primary skip).
    mean = np.array([0.50, 0.12, 0.55, 0.11, 0.60], dtype=float)
    sigs, stats = build_multitrade_signals(ts, side, mean, cfg=cfg)
    assert stats["n_skipped_clarity"] >= 1
    assert stats["n_emitted"] >= 1
    # Weak primary after history exists should not open a new book-1 freely
    books = [int((s.meta or {}).get("book_idx", 0)) for s in sigs]
    assert 1 in books


def test_addon_scope_allows_weak_primary():
    cfg = live_control_cfg()
    cfg["clarity_scope"] = "addon"
    n = 3
    ts = (np.arange(n) * 3_600_000).astype(np.int64)
    side = np.ones(n, dtype=int)
    mean = np.array([0.11, 0.11, 0.11], dtype=float)  # above DIRECTION_BAND 0.10
    sigs, stats = build_multitrade_signals(ts, side, mean, cfg=cfg)
    assert stats["n_primary"] >= 1
    assert stats["n_skipped_clarity"] == 0 or stats["n_emitted"] >= 1
    assert any(int((s.meta or {}).get("book_idx", 0)) == 1 for s in sigs)
