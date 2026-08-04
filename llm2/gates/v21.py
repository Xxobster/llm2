"""Frozen V2.1 readiness gate table."""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
import pandas as pd

from llm2.gates.bootstrap import block_bootstrap_mean
from llm2.gates.dsr import deflated_sharpe_ratio
from llm2.gates.hac import newey_west_sharpe
from llm2.gates.pbo import pbo_cscv

GateStatus = Literal["PASS", "FAIL", "UNKNOWN"]

V21_THRESHOLDS = {
    "min_outer_folds": 5,
    "min_trades_per_fold": 10,
    "min_pooled_oos_trades": 50,
    "pooled_pf": 1.20,
    "daily_mtm_sharpe": 1.00,
    "hac_sharpe": 0.75,
    "positive_fold_frac": 0.80,
    "bootstrap_positive_frac": 0.90,
    "dsr": 0.95,
    "stress_pf": 1.05,
    "baseline_mdd": 0.20,
    "stress_mdd": 0.25,
    "margin_utilization": 0.60,
    "pbo": 0.20,
}


def _status(value: float, threshold: float, *, ge: bool = True) -> GateStatus:
    if not np.isfinite(value):
        return "UNKNOWN"
    if ge:
        return "PASS" if value >= threshold else "FAIL"
    return "PASS" if value <= threshold else "FAIL"


def evaluate_v21_gates(
    *,
    fold_pnls: list[float] | None = None,
    fold_pfs: list[float] | None = None,
    fold_trades: list[int] | None = None,
    daily_returns: np.ndarray | None = None,
    pooled_pf: float | None = None,
    pooled_skill: float | None = None,
    pooled_trades: int | None = None,
    metric_kind: Literal["profit_factor", "forecast_skill"] = "profit_factor",
    stress_pnl: float | None = None,
    stress_pf: float | None = None,
    baseline_mdd: float | None = None,
    stress_mdd: float | None = None,
    margin_util: float | None = None,
    n_trials: int = 1,
    candidate_matrix: pd.DataFrame | None = None,
    liquidation: bool = False,
) -> dict[str, GateStatus | float | Any]:
    """Evaluate frozen V2.1 gates.

    ``metric_kind`` keeps units honest. ``profit_factor`` is the deployment gate; a
    magnitude forecast's skill ratio must not be written into ``pooled_pf`` or it will
    be graded against the Profit Factor threshold 1.20 as if it were a trade result.
    """
    fold_pnls = fold_pnls or []
    fold_pfs = fold_pfs or []
    fold_trades = fold_trades or []
    n_folds = len(fold_pnls)

    gates: dict[str, GateStatus | float | Any] = {"metric_kind": metric_kind}

    gates["outer_folds"] = _status(float(n_folds), V21_THRESHOLDS["min_outer_folds"])
    gates["outer_folds_value"] = int(n_folds)
    if fold_trades:
        min_tr = min(fold_trades)
        gates["trades_per_fold"] = _status(float(min_tr), V21_THRESHOLDS["min_trades_per_fold"])
        gates["trades_per_fold_min"] = int(min_tr)
        gates["fold_trades"] = [int(t) for t in fold_trades]
    else:
        gates["trades_per_fold"] = "UNKNOWN"

    if pooled_trades is not None:
        gates["pooled_trades"] = _status(float(pooled_trades), V21_THRESHOLDS["min_pooled_oos_trades"])
        gates["pooled_trades_value"] = int(pooled_trades)
    else:
        gates["pooled_trades"] = "UNKNOWN"

    if metric_kind == "forecast_skill":
        # Skill is reported, never graded against the Profit Factor threshold.
        gates["pooled_pf"] = "UNKNOWN"
        gates["pooled_pf_note"] = "not applicable for forecast_skill metric_kind"
        if pooled_skill is not None and np.isfinite(pooled_skill):
            gates["pooled_skill"] = "PASS" if pooled_skill > 1.0 else "FAIL"
            gates["pooled_skill_value"] = float(pooled_skill)
        else:
            gates["pooled_skill"] = "UNKNOWN"
    elif pooled_pf is not None and np.isfinite(pooled_pf):
        gates["pooled_pf"] = _status(float(pooled_pf), V21_THRESHOLDS["pooled_pf"])
        gates["pooled_pf_value"] = float(pooled_pf)
    elif pooled_pf is not None and not np.isfinite(pooled_pf):
        gates["pooled_pf"] = "FAIL"  # inf/nan PF is not quotable evidence
        gates["pooled_pf_value"] = str(pooled_pf)
    else:
        gates["pooled_pf"] = "UNKNOWN"

    if daily_returns is not None:
        r = daily_returns[np.isfinite(daily_returns)]
        if len(r) >= 3:
            sr = float(np.mean(r) / (np.std(r, ddof=1) + 1e-12) * np.sqrt(252))
            hac = float(newey_west_sharpe(r))
            dsr = float(deflated_sharpe_ratio(r, sr, n_trials=n_trials))
            boot = block_bootstrap_mean(r)
            boot_frac = float(boot["positive_frac"])
            gates["daily_mtm_sharpe"] = _status(sr, V21_THRESHOLDS["daily_mtm_sharpe"])
            gates["daily_mtm_sharpe_value"] = sr
            gates["hac_sharpe"] = _status(hac, V21_THRESHOLDS["hac_sharpe"])
            gates["hac_sharpe_value"] = hac
            gates["dsr"] = _status(dsr, V21_THRESHOLDS["dsr"])
            gates["dsr_value"] = dsr
            gates["bootstrap_positive_frac"] = _status(
                boot_frac, V21_THRESHOLDS["bootstrap_positive_frac"]
            )
            gates["bootstrap_positive_frac_value"] = boot_frac
        else:
            gates["daily_mtm_sharpe"] = "UNKNOWN"
            gates["hac_sharpe"] = "UNKNOWN"
            gates["dsr"] = "UNKNOWN"
            gates["bootstrap_positive_frac"] = "UNKNOWN"
    else:
        gates["daily_mtm_sharpe"] = "UNKNOWN"
        gates["hac_sharpe"] = "UNKNOWN"
        gates["dsr"] = "UNKNOWN"
        gates["bootstrap_positive_frac"] = "UNKNOWN"

    if fold_pnls and fold_pfs:
        gates["fold_pnls"] = [float(p) for p in fold_pnls]
        gates["fold_pfs"] = [float(pf) for pf in fold_pfs]
        eligible = [
            (p, pf)
            for p, pf, t in zip(fold_pnls, fold_pfs, fold_trades or [0] * len(fold_pnls))
            if t >= V21_THRESHOLDS["min_trades_per_fold"]
        ]
        if eligible:
            if metric_kind == "forecast_skill":
                # For skill, "positive" means beat the train-mean baseline (skill > 1).
                pos_frac = sum(1 for p, pf in eligible if p > 0 and pf > 1.0) / len(eligible)
            else:
                pos_frac = sum(1 for p, pf in eligible if p > 0 and pf > 1.0) / len(eligible)
            gates["positive_fold_frac"] = _status(pos_frac, V21_THRESHOLDS["positive_fold_frac"])
            gates["positive_fold_frac_value"] = float(pos_frac)
        else:
            gates["positive_fold_frac"] = "UNKNOWN"
    else:
        gates["positive_fold_frac"] = "UNKNOWN"

    if stress_pnl is not None and stress_pf is not None:
        gates["stress_pnl"] = "PASS" if stress_pnl > 0 else "FAIL"
        gates["stress_pnl_value"] = float(stress_pnl)
        gates["stress_pf"] = _status(float(stress_pf), V21_THRESHOLDS["stress_pf"])
        gates["stress_pf_value"] = float(stress_pf)
    else:
        gates["stress_pnl"] = "UNKNOWN"
        gates["stress_pf"] = "UNKNOWN"

    if baseline_mdd is not None:
        gates["baseline_mdd"] = _status(float(baseline_mdd), V21_THRESHOLDS["baseline_mdd"], ge=False)
        gates["baseline_mdd_value"] = float(baseline_mdd)
    else:
        gates["baseline_mdd"] = "UNKNOWN"

    if stress_mdd is not None:
        gates["stress_mdd"] = _status(float(stress_mdd), V21_THRESHOLDS["stress_mdd"], ge=False)
        gates["stress_mdd_value"] = float(stress_mdd)
    else:
        gates["stress_mdd"] = "UNKNOWN"

    if margin_util is not None:
        gates["margin_utilization"] = _status(float(margin_util), V21_THRESHOLDS["margin_utilization"], ge=False)
        gates["margin_utilization_value"] = float(margin_util)
    else:
        gates["margin_utilization"] = "UNKNOWN"

    gates["liquidation"] = "FAIL" if liquidation else "PASS"

    if candidate_matrix is not None and candidate_matrix.shape[1] >= 2:
        pbo_res = pbo_cscv(candidate_matrix)
        pbo_val = pbo_res["pbo"]
        if np.isfinite(pbo_val):
            gates["pbo"] = _status(float(pbo_val), V21_THRESHOLDS["pbo"], ge=False)
            gates["pbo_value"] = float(pbo_val)
        else:
            gates["pbo"] = "UNKNOWN"
            gates["pbo_note"] = "PBO_UNAVAILABLE_INSUFFICIENT_MATRIX"
    else:
        gates["pbo"] = "UNKNOWN"
        gates["pbo_note"] = "PBO_UNAVAILABLE_INSUFFICIENT_MATRIX"

    # Blocking gates for overall. PBO may stay UNKNOWN without blocking (V2.1 §3).
    blocking_keys = [
        "outer_folds",
        "trades_per_fold",
        "pooled_trades",
        "daily_mtm_sharpe",
        "hac_sharpe",
        "dsr",
        "bootstrap_positive_frac",
        "positive_fold_frac",
        "stress_pnl",
        "stress_pf",
        "baseline_mdd",
        "stress_mdd",
        "margin_utilization",
        "liquidation",
    ]
    if metric_kind == "forecast_skill":
        blocking_keys.append("pooled_skill")
    else:
        blocking_keys.append("pooled_pf")

    blocking = [gates[k] for k in blocking_keys if k in gates]
    if any(s == "FAIL" for s in blocking):
        gates["overall"] = "FAIL"
    elif any(s == "UNKNOWN" for s in blocking):
        gates["overall"] = "UNKNOWN"
    elif all(s == "PASS" for s in blocking):
        gates["overall"] = "PASS"
    else:
        gates["overall"] = "UNKNOWN"

    return gates


def format_gates_table(gates: dict[str, Any]) -> str:
    lines = ["| Gate | Status |", "| --- | --- |"]
    for k, v in gates.items():
        lines.append(f"| {k} | {v} |")
    return "\n".join(lines)
