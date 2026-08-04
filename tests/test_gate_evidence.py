"""V2.1 stress / MDD / margin / PBO evidence bindings."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.gates.evidence import (
    build_candidate_return_matrix,
    cap_leverage_by_risk_tiers,
    leverage_ceiling_from_stop,
    leverage_from_stop,
    mdd_fraction_from_daily_returns,
    mdd_fraction_from_equity,
    peak_margin_utilization,
    pooled_profit_factor,
    resolve_operational_leverage,
)
from llm2.gates.v21 import evaluate_v21_gates
from llm2.hunt.runner import _tier_from_gates


def test_mdd_from_equity_and_returns():
    eq = np.array([100.0, 110.0, 90.0, 95.0])
    assert mdd_fraction_from_equity(eq) == pytest.approx(20 / 110, rel=1e-6)
    r = np.array([0.1, -0.2 / 1.1, 95 / 90 - 1])
    assert mdd_fraction_from_daily_returns(r) == pytest.approx(20 / 110, rel=1e-3)


def test_pooled_pf_not_mean_of_folds():
    # One big win and many small losses — pooled PF differs from mean fold PF.
    pnls = [10.0, -1.0, -1.0, -1.0]
    assert pooled_profit_factor(pnls) == pytest.approx(10 / 3)


def test_peak_margin_utilization_from_trades():
    class T:
        def __init__(self, entry, exit_, im):
            self.entry_ts_ms = entry
            self.exit_ts_ms = exit_
            self.initial_margin = im
            self.qty = 0
            self.entry_price = 0
            self.leverage = 1

    trades = [T(1, 3, 40.0), T(2, 4, 30.0)]  # overlap → 70 open
    eq = pd.DataFrame({"ts_ms": [1, 2, 3, 4], "equity": [100.0, 100.0, 100.0, 100.0]})
    util = peak_margin_utilization(trades, equity=eq, starting_equity=100.0)
    assert util == pytest.approx(0.70)


def test_pbo_unavailable_does_not_block_overall_pass():
    r = np.random.default_rng(0).normal(0.002, 0.005, 400)
    gates = evaluate_v21_gates(
        fold_pnls=[10, 12, 8, 9, 11],
        fold_pfs=[1.3, 1.4, 1.25, 1.3, 1.35],
        fold_trades=[20, 22, 18, 19, 21],
        pooled_pf=1.3,
        pooled_trades=100,
        daily_returns=r,
        stress_pnl=50.0,
        stress_pf=1.1,
        baseline_mdd=0.10,
        stress_mdd=0.12,
        margin_util=0.30,
        candidate_matrix=None,  # PBO unavailable
        n_trials=4,
    )
    assert gates["pbo"] == "UNKNOWN"
    assert gates["pbo_note"] == "PBO_UNAVAILABLE_INSUFFICIENT_MATRIX"
    assert gates["stress_pnl"] == "PASS"
    assert gates["baseline_mdd"] == "PASS"
    assert gates["margin_utilization"] == "PASS"
    assert gates["overall"] == "PASS"


def test_tier2_requires_full_gates_on_backtest_path():
    gates = {
        "overall": "UNKNOWN",
        "pooled_pf": "PASS",
        "pooled_trades": "PASS",
        "positive_fold_frac": "PASS",
        "stress_pnl": "UNKNOWN",
        "stress_pf": "UNKNOWN",
        "baseline_mdd": "UNKNOWN",
        "stress_mdd": "UNKNOWN",
        "margin_utilization": "UNKNOWN",
        "dsr": "PASS",
    }
    assert _tier_from_gates(gates, True, require_full_gates=True) == 1
    gates_ok = {
        **gates,
        "overall": "PASS",
        "stress_pnl": "PASS",
        "stress_pf": "PASS",
        "baseline_mdd": "PASS",
        "stress_mdd": "PASS",
        "margin_utilization": "PASS",
    }
    assert _tier_from_gates(gates_ok, True, require_full_gates=True) == 3


def test_candidate_matrix_refuses_unequal_stitches():
    from llm2.gates.evidence import build_candidate_return_matrix, build_fold_return_matrix

    assert build_candidate_return_matrix({"a": [0.01] * 40, "b": [-0.01] * 30}) is None
    m = build_candidate_return_matrix({"a": [0.01] * 40, "b": [-0.01] * 40})
    assert m is not None and m.shape == (40, 2)
    folds = build_fold_return_matrix({"a": [1.0, 2.0, 3.0], "b": [0.5, -1.0, 1.5]})
    assert folds is not None and folds.shape == (3, 2)


def test_leverage_from_stop_includes_security_margin():
    # sl=2% → ceiling floor(1/0.027)=37 → haircut 0.5 → 18
    assert leverage_ceiling_from_stop(0.02) == 37
    assert leverage_from_stop(0.02) == 18.0
    assert leverage_from_stop(0.04) == 10.0  # ceiling 21 → 10
    with pytest.raises(ValueError):
        leverage_from_stop(0.0)


def test_resolve_operational_leverage_refuses_pack_mismatch():
    info = resolve_operational_leverage(0.02, pack_leverage=18.0, notional=64.0)
    assert info["leverage"] == 18.0
    assert info["ceiling"] == 37
    with pytest.raises(ValueError, match="pack leverage"):
        resolve_operational_leverage(0.02, pack_leverage=45.0)


def test_cap_leverage_by_risk_tiers():
    tiers = [
        {"notional_floor": 0.0, "max_leverage": 100.0},
        {"notional_floor": 50.0, "max_leverage": 10.0},
    ]
    assert cap_leverage_by_risk_tiers(18.0, notional=64.0, tiers=tiers) == 10.0
    assert cap_leverage_by_risk_tiers(18.0, notional=10.0, tiers=tiers) == 18.0
