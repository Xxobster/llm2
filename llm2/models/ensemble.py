"""Simple ensemble over predictors."""

from __future__ import annotations

import numpy as np

from llm2.models.base import Prediction, Predictor


class MeanEnsemble:
    name = "mean_ensemble"

    def __init__(self, models: list[Predictor]) -> None:
        self.models = models

    def fit(self, X: np.ndarray, y: np.ndarray) -> "MeanEnsemble":
        for m in self.models:
            m.fit(X, y)
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        preds = [m.predict(X).mean for m in self.models]
        valid = [p for p in preds if p is not None]
        if not valid:
            return Prediction()
        stacked = np.vstack(valid)
        mean = np.nanmean(stacked, axis=0)
        return Prediction(mean=mean, q50=mean)
