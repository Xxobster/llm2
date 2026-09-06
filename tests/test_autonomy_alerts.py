"""Autonomy alert + gate policy stay conservative."""

from llm2.autonomy.policy import is_gate_candidate


def test_overtrade_rejected():
    arm = {
        "status": "RAN",
        "mode": "one_head_filter_pi_star",
        "n_trades": 80,
        "entry_bar_exit_rate": 0.2,
        "trades_per_month": 50.0,
        "profit_factor": 2.0,
    }
    assert not is_gate_candidate(arm, {"profit_factor": 1.5})


def test_beats_control_accepted():
    arm = {
        "status": "RAN",
        "mode": "one_head_filter_pi_star",
        "n_trades": 80,
        "entry_bar_exit_rate": 0.2,
        "trades_per_month": 10.0,
        "profit_factor": 1.8,
    }
    assert is_gate_candidate(arm, {"profit_factor": 1.5})
