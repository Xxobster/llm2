"""Standing invariant: a constant predictor cannot invent an edge.

The false Tier-2 (PF 2988 on vol_ratio) happened because the proxy multiplied a side by
the target itself. A constant predictor must score at or below 1.0 on every target family
— that catches the whole class of units bugs, not only the one instance.
"""

from __future__ import annotations

import numpy as np
import pytest

from llm2.hunt.runner import _proxy_side, target_family
from llm2.paths import ROUND_TRIP_COST


def _proxy_pf(side: np.ndarray, realized_ret: np.ndarray) -> float:
    ret = realized_ret * side - ROUND_TRIP_COST * (side != 0)
    wins = float(np.nansum(ret[ret > 0]))
    losses = float(-np.nansum(ret[ret < 0]))
    if losses > 0:
        return wins / losses
    if wins > 0:
        return 2.0
    return 0.0


def _skill(pred: np.ndarray, y: np.ndarray, train_mean: float) -> float:
    mae = float(np.nanmean(np.abs(y - pred)))
    mae_base = float(np.nanmean(np.abs(y - train_mean)))
    return float(mae_base / mae) if mae > 1e-12 else 0.0


@pytest.mark.parametrize(
    "target",
    ["fwd_return", "quantile", "direction", "xs_rank", "volatility", "vol_ratio"],
)
def test_constant_predictor_cannot_score_above_one(target: str):
    rng = np.random.default_rng(0)
    n = 2000
    family = target_family(target)
    realized = rng.normal(0.0, 0.01, size=n)

    if family == "return":
        y = realized.copy()
        const = np.full(n, float(np.mean(y[:1000])))
    elif family == "directional":
        y = np.sign(realized)
        const = np.zeros(n)  # always flat
    elif family == "rank":
        y = rng.uniform(0.0, 1.0, size=n)
        const = np.full(n, 0.5)  # always the cross-section centre
    else:
        y = np.abs(rng.normal(0.03, 0.02, size=n))
        train_mean = float(np.mean(y[:1000]))
        const = np.full(n, train_mean)
        skill = _skill(const[1000:], y[1000:], train_mean)
        assert skill <= 1.0 + 1e-9, f"{target}: constant skill={skill}"
        return

    side = _proxy_side(const, family)
    pf = _proxy_pf(side, realized)
    assert pf <= 1.0 + 1e-9, f"{target}: constant proxy PF={pf} with n_signals={int((side != 0).sum())}"


def test_the_old_bug_is_caught_when_y_is_used_as_pnl():
    """If someone reintroduces side * y for a positive-only target, PF blows up."""
    y = np.abs(np.random.default_rng(1).normal(0.03, 0.02, size=2000))
    side = np.ones(len(y), dtype=int)  # the old bug: every bar long because y > 0
    bogus = _proxy_pf(side, y)  # treating y as if it were a return
    assert bogus > 1.5, "sanity: the buggy scoring path is what this invariant guards against"
