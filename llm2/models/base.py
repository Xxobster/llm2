"""Unified prediction interface."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, runtime_checkable

import numpy as np


@dataclass
class Prediction:
    mean: np.ndarray | None = None
    q10: np.ndarray | None = None
    q50: np.ndarray | None = None
    q90: np.ndarray | None = None
    proba: np.ndarray | None = None  # (n, n_classes)
    side: np.ndarray | None = None  # +1/-1/0


@runtime_checkable
class Predictor(Protocol):
    name: str

    def fit(self, X: np.ndarray, y: np.ndarray) -> "Predictor": ...

    def predict(self, X: np.ndarray) -> Prediction: ...
