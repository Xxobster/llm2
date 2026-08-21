"""Unit tests for 1m indicator parity helpers (no network, no orders)."""

from __future__ import annotations

from llm2.live.indicator_parity_1m import (
    MIN_1M_STRUCTURE_BARS,
    diff_frames_for_test,
    refuse_short_structure_limit,
)


def test_diff_identical_frames_pass():
    row = {
        "close": 1875.22,
        "structure_bias": -1.0,
        "dist_last_sh_pct": 0.0123456789,
        "last_sh_price": 1900.0,
    }
    d = diff_frames_for_test(row, dict(row), abs_eps=1e-9)
    assert d.identical is True
    assert d.n_mismatch == 0
    assert d.ohlc_tip_equal is True
    assert d.n_cols == 4


def test_diff_mutated_close_fail():
    live = {"close": 1875.22, "structure_bias": 1.0}
    research = {"close": 1875.23, "structure_bias": 1.0}
    d = diff_frames_for_test(live, research, abs_eps=1e-9)
    assert d.identical is False
    assert d.n_mismatch == 1
    assert d.first_mismatches[0]["col"] == "close"
    assert d.ohlc_tip_equal is False


def test_refuse_short_structure_limit():
    assert refuse_short_structure_limit(None) is None
    assert refuse_short_structure_limit(MIN_1M_STRUCTURE_BARS) is None
    assert refuse_short_structure_limit(MIN_1M_STRUCTURE_BARS + 1) is None
    bad = refuse_short_structure_limit(800)
    assert bad is not None
    assert bad["error"] == "structure_history_too_short"
    assert bad["n_bars_requested"] == 800
    assert bad["min_required"] == MIN_1M_STRUCTURE_BARS
    bad2 = refuse_short_structure_limit(MIN_1M_STRUCTURE_BARS - 1)
    assert bad2 is not None
    assert bad2["error"] == "structure_history_too_short"
