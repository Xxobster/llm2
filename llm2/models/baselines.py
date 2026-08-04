"""Simple baselines without heavy sklearn pipelines."""

from __future__ import annotations

import numpy as np

from llm2.models.base import Prediction


class HistoricalMeanBaseline:
    name = "historical_mean"

    def __init__(self) -> None:
        self._mean: float = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray) -> "HistoricalMeanBaseline":
        _ = X
        self._mean = float(np.nanmean(y))
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        n = len(X)
        arr = np.full(n, self._mean, dtype=float)
        return Prediction(mean=arr, q50=arr)


class LastValueBaseline:
    name = "last_value"

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LastValueBaseline":
        _ = X
        self._last = float(y[np.isfinite(y)][-1]) if np.isfinite(y).any() else 0.0
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        arr = np.full(len(X), self._last, dtype=float)
        return Prediction(mean=arr, q50=arr)


class ZeroBaseline:
    name = "zero"

    def fit(self, X: np.ndarray, y: np.ndarray) -> "ZeroBaseline":
        _ = (X, y)
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        arr = np.zeros(len(X), dtype=float)
        return Prediction(mean=arr, q50=arr, side=np.zeros(len(X), dtype=int))


class SignMomentumBaseline:
    name = "sign_momentum"

    def fit(self, X: np.ndarray, y: np.ndarray) -> "SignMomentumBaseline":
        _ = y
        self._X = X
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        col = X[:, 0] if X.ndim == 2 and X.shape[1] else X
        side = np.sign(col).astype(int)
        return Prediction(mean=col, side=side)


class SeasonalNaiveBaseline:
    """Predict using the value from ``season`` bars ago on the training series mean seasonal pattern."""

    name = "seasonal_naive"

    def __init__(self, season: int = 24) -> None:
        self.season = int(season)
        self._seasonal: np.ndarray | None = None
        self._fallback: float = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray) -> "SeasonalNaiveBaseline":
        _ = X
        y_clean = y[np.isfinite(y)]
        self._fallback = float(np.nanmean(y_clean)) if y_clean.size else 0.0
        if y_clean.size < self.season * 2:
            self._seasonal = None
            return self
        # average by season index (vectorized via bincount)
        n = len(y_clean)
        idx = np.arange(n) % self.season
        sums = np.bincount(idx, weights=y_clean, minlength=self.season)
        counts = np.bincount(idx, minlength=self.season).astype(float)
        means = np.where(counts > 0, sums / np.maximum(counts, 1.0), self._fallback)
        self._seasonal = means
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        n = len(X)
        if self._seasonal is None:
            arr = np.full(n, self._fallback, dtype=float)
        else:
            arr = self._seasonal[np.arange(n) % self.season]
        return Prediction(mean=arr, q50=arr)
