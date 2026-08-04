"""Cost hurdle math."""

from __future__ import annotations

from llm2.audit.cost_hurdle import CostHurdle
from llm2.paths import ROUND_TRIP_COST


def test_frozen_round_trip_cost():
    h = CostHurdle()
    assert abs(h.screening_hurdle_return() - ROUND_TRIP_COST) < 1e-9


def test_break_even_probability_between_zero_and_one():
    h = CostHurdle(tp_pct=0.01, sl_pct=0.02)
    pi = h.break_even_probability()
    assert 0.0 < pi < 1.0


def test_positive_ev_when_probability_high_enough():
    h = CostHurdle(tp_pct=0.02, sl_pct=0.01)
    pi = h.break_even_probability()
    assert h.should_trade(min(0.99, pi + 0.05))
