"""A magnitude target must never be scored as if it were a direction.

Feeding vol_ratio through the directional proxy scored a constant predictor at PF 2.0 and
ridge at PF 2988, because the proxy multiplied the side by the target itself and a
volatility target is positive by construction.
"""

from __future__ import annotations

import numpy as np
import pytest

from llm2.hunt.runner import _proxy_side, _tier_from_gates, target_family


def test_magnitude_targets_never_produce_a_side():
    for target in ("volatility", "vol_ratio"):
        assert target_family(target) == "magnitude"
        mean = np.array([0.5, 1.2, 3.0, 0.01])
        assert np.all(_proxy_side(mean, target_family(target)) == 0)


def test_rank_target_is_centred_on_one_half():
    side = _proxy_side(np.array([0.9, 0.5, 0.1, 0.52]), "rank")
    assert side.tolist() == [1, 0, -1, 0]


def test_return_target_uses_the_cost_hurdle_as_its_deadband():
    from llm2.paths import ROUND_TRIP_COST

    mean = np.array([ROUND_TRIP_COST * 2, 0.0, -ROUND_TRIP_COST * 2, ROUND_TRIP_COST / 2])
    assert _proxy_side(mean, "return").tolist() == [1, 0, -1, 0]


def test_unknown_target_is_rejected_rather_than_defaulted():
    with pytest.raises(ValueError):
        target_family("no_such_target")


def test_a_failed_surrogate_screen_caps_the_tier_at_zero():
    profitable_gates = {
        "overall": "PASS",
        "dsr": "PASS",
        "pooled_pf": "PASS",
        "pooled_trades": "PASS",
        "positive_fold_frac": "PASS",
    }
    assert _tier_from_gates(profitable_gates, screen_pass=True) == 3
    assert _tier_from_gates(profitable_gates, screen_pass=False) == 0
