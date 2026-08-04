"""Unit tests for multitrade live helpers (no exchange calls)."""

from __future__ import annotations

from llm2.live.multitrade import (
    book_tp_hold,
    decide_entry_gate,
    extended_tp_offset,
    mean_strength_ok,
    parse_multitrade_config,
)


def test_extended_tp_fib_1618():
    assert abs(extended_tp_offset(1.618) - 0.02618) < 1e-9


def test_book_tp_hold_tiers():
    tp1, h1 = book_tp_hold(1, fib_ext=1.618, hold_addon=12)
    tp2, h2 = book_tp_hold(2, fib_ext=1.618, hold_addon=12)
    tp3, h3 = book_tp_hold(3, fib_ext=1.618, hold_addon=12)
    assert (tp1, h1) == (0.01, 6)
    assert (tp2, h2) == (0.01, 6)
    assert abs(tp3 - 0.02618) < 1e-9 and h3 == 12


def test_mean_strength_median_gate():
    assert mean_strength_ok(0.5, []) is True
    assert mean_strength_ok(0.2, [0.1, 0.3, 0.5]) is False  # median 0.3
    assert mean_strength_ok(0.3, [0.1, 0.3, 0.5]) is True


def test_parse_multitrade_config():
    assert parse_multitrade_config({"max_positions": 1}) is None
    cfg = parse_multitrade_config(
        {
            "execution_mode": "multitrade",
            "multitrade": {
                "max_positions_per_side": 6,
                "clarity": "mean_strength",
                "fib_ext": 1.618,
                "hold_addon": 12,
                "version_id": "eth_multitrade_v1",
            },
        }
    )
    assert cfg is not None
    assert cfg["max_positions_per_side"] == 6
    assert cfg["clarity"] == "mean_strength"


def test_decide_entry_gate_cap_and_clarity():
    cfg = {
        "max_positions_per_side": 6,
        "clarity": "mean_strength",
        "fib_ext": 1.618,
        "hold_addon": 12,
        "base_tp": 0.01,
        "base_sl": 0.02,
        "base_hold": 6,
        "mean_lookback": 168,
    }
    # first book always allowed
    g0 = decide_entry_gate(
        side=1, pred_mean=0.5, n_open_same_side=0, strength_hist=[], cfg=cfg
    )
    assert g0["allow"] and g0["book_idx"] == 1 and g0["tp_pct"] == 0.01
    # addon blocked by clarity
    g1 = decide_entry_gate(
        side=1,
        pred_mean=0.15,
        n_open_same_side=1,
        strength_hist=[0.4, 0.5, 0.6],
        cfg=cfg,
    )
    assert not g1["allow"] and g1["skip_reason"] == "clarity_mean_strength"
    # book 3+ fib TP
    g3 = decide_entry_gate(
        side=-1,
        pred_mean=-0.9,
        n_open_same_side=2,
        strength_hist=[0.1],
        cfg=cfg,
    )
    assert g3["allow"] and g3["book_idx"] == 3
    assert abs(g3["tp_pct"] - 0.02618) < 1e-9 and g3["max_hold_bars"] == 12
    # cap
    gcap = decide_entry_gate(
        side=1,
        pred_mean=0.9,
        n_open_same_side=6,
        strength_hist=[],
        cfg=cfg,
    )
    assert not gcap["allow"] and "cap_reached" in gcap["skip_reason"]
