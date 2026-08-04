"""LightGBM regressors and classifiers."""

from __future__ import annotations

import numpy as np

from llm2.models.base import Prediction

try:
    import lightgbm as lgb

    _HAS_LGB = True
except ImportError:
    _HAS_LGB = False


class LGBMRegressorPredictor:
    name = "lgbm_regressor"

    def __init__(self, **kwargs) -> None:
        if not _HAS_LGB:
            raise ImportError("lightgbm not installed")
        self._kwargs = {"verbosity": -1, "n_estimators": 100, **kwargs}
        self._model = lgb.LGBMRegressor(**self._kwargs)

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LGBMRegressorPredictor":
        mask = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
        self._model.fit(X[mask], y[mask])
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        pred = self._model.predict(X)
        return Prediction(mean=pred, q50=pred)


class LGBMClassifierPredictor:
    name = "lgbm_classifier"

    def __init__(self, **kwargs) -> None:
        if not _HAS_LGB:
            raise ImportError("lightgbm not installed")
        self._kwargs = {"verbosity": -1, "n_estimators": 100, **kwargs}
        self._model = lgb.LGBMClassifier(**self._kwargs)
        self._classes: np.ndarray | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LGBMClassifierPredictor":
        mask = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
        y_int = y[mask].astype(int)
        self._model.fit(X[mask], y_int)
        self._classes = self._model.classes_
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        proba = self._model.predict_proba(X)
        pred = self._model.predict(X)
        side = np.where(pred > 0, 1, np.where(pred < 0, -1, 0))
        return Prediction(proba=proba, side=side.astype(int), mean=pred.astype(float))
