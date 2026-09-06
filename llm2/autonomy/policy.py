"""Autonomy research-loop policy (hard gates; no live deploy)."""

from __future__ import annotations

from typing import Any

# Hard methodological caps — never relax after viewing a generation's test numbers.
ENTRY_BAR_EXIT_CAP = 0.35
MIN_TRADES_FLAG = 50
MIN_TRADES_QUOTE = 12
MIN_TRADES_PER_MONTH = 4.0
# Soft max: filters that fire denser than this are over-trading noise on 15m.
MAX_TRADES_PER_MONTH = 40.0
# Must clear control Profit Factor by this relative floor (same as confluence 001).
PF_VS_CONTROL_FLOOR = 0.85
# Prefer beating control PF outright for a gate_candidate alert.
PF_BEAT_CONTROL = 1.0

STOP_REL = "artifacts/autonomy/STOP"
STATUS_REL = "artifacts/autonomy/STATUS.md"
QUEUE_REL = "configs/autonomy/research_loop_v1.yaml"


def is_gate_candidate(arm: dict[str, Any], control: dict[str, Any] | None) -> bool:
    if arm.get("status") != "RAN":
        return False
    if arm.get("mode") == "control":
        return False
    n = int(arm.get("n_trades") or 0)
    if n < MIN_TRADES_FLAG:
        return False
    ebr = arm.get("entry_bar_exit_rate")
    if ebr is None or float(ebr) > ENTRY_BAR_EXIT_CAP:
        return False
    tpm = arm.get("trades_per_month")
    if tpm is None or float(tpm) < MIN_TRADES_PER_MONTH:
        return False
    if float(tpm) > MAX_TRADES_PER_MONTH:
        return False
    pf = arm.get("profit_factor")
    if pf is None or not (float(pf) == float(pf)):  # NaN check
        return False
    if control is None:
        return float(pf) >= 1.20
    cpf = control.get("profit_factor")
    if cpf is None:
        return float(pf) >= 1.20
    # Beat control PF and clear absolute floor.
    return float(pf) >= max(1.20, float(cpf) * PF_BEAT_CONTROL)


def rank_key(arm: dict[str, Any]) -> tuple:
    return (
        0 if arm.get("status") == "RAN" else 1,
        -(arm.get("expectancy_intent_all") or -1e9),
        -(arm.get("profit_factor") or -1e9),
        -(arm.get("sharpe_annualised") or -1e9),
    )
