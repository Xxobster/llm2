"""Unit tests for eth multitrade nested signal clarity_scope."""

from __future__ import annotations

import numpy as np
import pytest

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


def test_seed_strength_hist_warms_gate():
    cfg = live_control_cfg()
    cfg["clarity_scope"] = "all"
    cfg["strength_quantile"] = 0.75
    cfg["mean_lookback"] = 8
    n = 4
    ts = (np.arange(n) * 3_600_000).astype(np.int64)
    side = np.ones(n, dtype=int)
    # Weak signals vs high seed → p75 gate should reject.
    seed = [0.80] * 8
    mean = np.array([0.20, 0.22, 0.21, 0.23], dtype=float)
    _sigs, stats = build_multitrade_signals(
        ts, side, mean, cfg=cfg, seed_strength_hist=seed
    )
    assert stats["n_skipped_clarity"] >= 1
    assert stats["n_emitted"] == 0


def test_tp_scale_by_abs_mean_on_book_tp():
    cfg = live_control_cfg()
    cfg["clarity"] = "none"
    cfg["tp_scale_by_abs_mean"] = True
    cfg["tp_scale_ref"] = 0.5
    cfg["tp_scale_factor_min"] = 1.0
    cfg["tp_scale_factor_max"] = 2.0
    n = 1
    ts = np.array([0], dtype=np.int64)
    side = np.array([1], dtype=int)
    mean = np.array([0.75], dtype=float)  # factor 1.5 → TP 1.5%
    sigs, _stats = build_multitrade_signals(ts, side, mean, cfg=cfg)
    assert len(sigs) == 1
    assert float(sigs[0].target_offset) == pytest.approx(0.015)
