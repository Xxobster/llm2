"""Frozen V2.1 remainder battery for nested settles (always-on).

Deflated Sharpe Ratio, 10,000-sample block bootstrap, moderate stress
(2× slippage, all-taker cost book), mark-to-market drawdown, peak margin.
Does not retune stops, Exponential Moving Average spans, or efficiency ratio.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from llm2.gates.dsr import deflated_sharpe_ratio
from llm2.gates.evidence import mdd_fraction_from_daily_returns
from llm2.gates.v21 import evaluate_v21_gates

# Hunt 004 event-study rows that produced the EMA-stack names. Frozen trial count
# for Deflated Sharpe Ratio — not 1, and not tuned after viewing outer numbers.
HUNT004_EVENT_ROWS = 449
HUNT004_TRADESIM_PICKS = 9

# Bootstrap defaults were the library values before nested-settle 004 outer was viewed.
V21_N_BOOTSTRAP = 10_000
V21_BOOTSTRAP_BLOCK = 20
V21_BOOTSTRAP_SEED = 42


def _f(x: Any) -> float:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return float("nan")
    return v


def dsr_sensitivity(daily: np.ndarray, *, trials: tuple[int, ...]) -> dict[str, float]:
    r = np.asarray(daily, dtype=float)
    r = r[np.isfinite(r)]
    out: dict[str, float] = {}
    if r.size < 3:
        return {f"dsr_n{n}": float("nan") for n in trials}
    sr = float(np.mean(r) / (np.std(r, ddof=1) + 1e-12) * np.sqrt(252))
    for n in trials:
        out[f"dsr_n{n}"] = float(deflated_sharpe_ratio(r, sr, n_trials=int(n)))
    out["daily_mtm_sharpe_used"] = sr
    return out


def evaluate_nested_v21(
    *,
    fold_rows: list[dict[str, Any]],
    baseline: dict[str, Any],
    stress: dict[str, Any],
    n_trials: int = HUNT004_EVENT_ROWS,
) -> dict[str, Any]:
    """Score one frozen arm. Probability of Backtest Overfitting is unavailable (one name)."""
    fold_pnls = [_f(r.get("net_pnl")) for r in fold_rows]
    fold_pfs = [_f(r.get("profit_factor")) for r in fold_rows]
    fold_trades = [int(r.get("n_trades") or 0) for r in fold_rows]
    daily = np.asarray(baseline.get("daily_returns") or [], dtype=float)
    stress_daily = np.asarray(stress.get("daily_returns") or [], dtype=float)
    gates = evaluate_v21_gates(
        fold_pnls=fold_pnls,
        fold_pfs=fold_pfs,
        fold_trades=fold_trades,
        daily_returns=daily if daily.size else None,
        pooled_pf=_f(baseline.get("profit_factor")),
        pooled_trades=int(baseline.get("n_trades") or 0),
        metric_kind="profit_factor",
        n_trials=int(n_trials),
        n_bootstrap=V21_N_BOOTSTRAP,
        bootstrap_block_size=V21_BOOTSTRAP_BLOCK,
        bootstrap_seed=V21_BOOTSTRAP_SEED,
        stress_pnl=_f(stress.get("net_pnl")),
        stress_pf=_f(stress.get("profit_factor")),
        baseline_mdd=mdd_fraction_from_daily_returns(daily) if daily.size else None,
        stress_mdd=mdd_fraction_from_daily_returns(stress_daily) if stress_daily.size else None,
        margin_util=_f(baseline.get("peak_margin_util")),
        candidate_matrix=None,
        liquidation=bool(
            int(baseline.get("n_liquidations") or 0) > 0 or int(stress.get("n_liquidations") or 0) > 0
        ),
    )
    gates["dsr_sensitivity"] = dsr_sensitivity(
        daily, trials=(1, 2, HUNT004_TRADESIM_PICKS, 30, HUNT004_EVENT_ROWS)
    )
    gates["baseline_trades_per_month"] = _f(baseline.get("trades_per_month"))
    gates["stress_trades_per_month"] = _f(stress.get("trades_per_month"))
    gates["baseline_entry_bar_exit_rate"] = _f(baseline.get("entry_bar_exit_rate"))
    gates["stress_entry_bar_exit_rate"] = _f(stress.get("entry_bar_exit_rate"))
    gates["n_daily_returns"] = int(daily.size)
    return gates
