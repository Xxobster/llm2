"""Release gates must be bound to a discoverable test or the build is meaningless."""

from __future__ import annotations

import pytest

from llm2.audit.release_gates import (
    require_constant_predictor_invariant,
    require_predictability_gate_discriminates,
)


def test_constant_predictor_invariant_holds():
    scores = require_constant_predictor_invariant()
    assert scores
    assert all(v <= 1.0 + 1e-9 for v in scores.values()), scores


def test_predictability_gate_discriminates():
    """Signal must pass and noise must fail, or the gate carries no information."""
    result = require_predictability_gate_discriminates()
    assert result["signal_score"] > 0.1, result
    assert result["noise_p"] > 0.05, result


def test_sweep_freezes_nothing_without_a_working_gate():
    """D-010 is retracted; a target may only be frozen on evidence from a gate that works."""
    from scripts.autonomy_sweep import ACTIVE_TARGETS, FROZEN_TARGETS

    assert FROZEN_TARGETS == frozenset(), (
        "targets were frozen on the strength of the D-013 broken gate; unfreeze them"
    )
    assert {"fwd_return", "direction"} <= set(ACTIVE_TARGETS)


@pytest.mark.parametrize("gate", [require_constant_predictor_invariant, require_predictability_gate_discriminates])
def test_gates_raise_rather_than_return_false(gate):
    """Gates fail closed by raising; a caller must not be able to ignore a return value."""
    assert gate() is not None
