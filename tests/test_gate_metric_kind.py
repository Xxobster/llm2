"""Skill ratios must not be graded as Profit Factors."""

from __future__ import annotations

from llm2.gates.v21 import evaluate_v21_gates


def test_forecast_skill_does_not_fill_pooled_pf_gate():
    gates = evaluate_v21_gates(
        fold_pnls=[0.01, 0.02, 0.01, 0.0, 0.01],
        fold_pfs=[1.05, 1.10, 1.02, 0.99, 1.08],  # skill ratios
        fold_trades=[100, 100, 100, 100, 100],
        pooled_skill=1.05,
        pooled_trades=500,
        metric_kind="forecast_skill",
    )
    assert gates["metric_kind"] == "forecast_skill"
    assert gates["pooled_pf"] == "UNKNOWN"
    assert gates["pooled_skill"] == "PASS"
    assert gates["pooled_skill_value"] == 1.05


def test_profit_factor_metric_kind_still_gates_pooled_pf():
    gates = evaluate_v21_gates(
        fold_pnls=[1.0] * 5,
        fold_pfs=[1.3] * 5,
        fold_trades=[20] * 5,
        pooled_pf=1.3,
        pooled_trades=100,
        metric_kind="profit_factor",
    )
    assert gates["pooled_pf"] == "PASS"
    assert "pooled_skill" not in gates or gates.get("pooled_skill") in (None, "UNKNOWN")
