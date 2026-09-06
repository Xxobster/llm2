"""V2.1 gates smoke tests."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.gates.bootstrap import block_bootstrap_mean
from llm2.gates.dsr import deflated_sharpe_ratio
from llm2.gates.hac import newey_west_sharpe
from llm2.gates.pbo import pbo_cscv
from llm2.gates.v21 import evaluate_v21_gates


def test_dsr_finite_on_random_returns():
    rng = np.random.default_rng(0)
    r = rng.normal(0.001, 0.02, 252)
    sr = float(np.mean(r) / np.std(r) * np.sqrt(252))
    dsr = deflated_sharpe_ratio(r, sr, n_trials=10)
    assert np.isfinite(dsr)


def test_bootstrap_positive_frac():
    r = np.full(100, 0.01)
    res = block_bootstrap_mean(r, n_samples=100, block_size=10, seed=0)
    assert res["positive_frac"] == 1.0


def test_pbo_unknown_with_single_strategy():
    m = pd.DataFrame({"a": np.random.randn(50)})
    res = pbo_cscv(m, n_blocks=8)
    assert np.isnan(res["pbo"])


def test_evaluate_v21_gates_smoke():
    gates = evaluate_v21_gates(
        fold_pnls=[100, 50, -10, 20, 30],
        fold_pfs=[1.3, 1.1, 0.9, 1.2, 1.4],
        fold_trades=[12, 15, 11, 20, 14],
        pooled_pf=1.25,
        pooled_trades=72,
        daily_returns=np.random.default_rng(1).normal(0.001, 0.01, 300),
        n_bootstrap=200,
    )
    assert "overall" in gates
    assert gates["hac_sharpe"] in ("PASS", "FAIL", "UNKNOWN")
    assert int(gates.get("n_bootstrap") or 0) == 200
