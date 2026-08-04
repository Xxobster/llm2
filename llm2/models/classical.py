"""Classical linear and optional ARIMA models."""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import Ridge

from llm2.models.base import Prediction


class RidgePredictor:
    name = "ridge"

    def __init__(self, alpha: float = 1.0) -> None:
        self.alpha = alpha
        self._model = Ridge(alpha=alpha)

    def fit(self, X: np.ndarray, y: np.ndarray) -> "RidgePredictor":
        mask = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
        self._model.fit(X[mask], y[mask])
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        pred = self._model.predict(X)
        return Prediction(mean=pred, q50=pred)


class ARIMAPredictor:
    name = "arima"
    available = True

    def __init__(self, order: tuple[int, int, int] = (1, 0, 1)) -> None:
        self.order = order
        self._fitted = None
        try:
            from statsmodels.tsa.arima.model import ARIMA  # noqa: F401

            self._ARIMA = ARIMA
        except ImportError:
            self.available = False

    def fit(self, X: np.ndarray, y: np.ndarray) -> "ARIMAPredictor":
        if not self.available:
            raise ImportError("statsmodels required for ARIMA")
        _ = X
        y_clean = y[np.isfinite(y)]
        self._fitted = self._ARIMA(y_clean, order=self.order).fit()
        self._n = len(y_clean)
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        if self._fitted is None:
            raise RuntimeError("Model not fit")
        n = len(X)
        fc = self._fitted.forecast(steps=n)
        arr = np.asarray(fc, dtype=float)
        return Prediction(mean=arr, q50=arr)
