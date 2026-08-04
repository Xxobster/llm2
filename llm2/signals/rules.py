"""Signal gating rules."""

from __future__ import annotations

import numpy as np

from llm2.audit.cost_hurdle import CostHurdle


def probability_gate(proba_up: np.ndarray, hurdle: CostHurdle | None = None) -> np.ndarray:
    h = hurdle or CostHurdle()
    pi = h.break_even_probability()
    return (proba_up >= pi).astype(int)


def direction_gate(scores: np.ndarray, *, threshold: float = 0.0) -> np.ndarray:
    side = np.zeros(len(scores), dtype=int)
    side[scores > threshold] = 1
    side[scores < -threshold] = -1
    return side
