"""Baseline predictor interface."""

from __future__ import annotations

import numpy as np

from llm2.models.baselines import HistoricalMeanBaseline, ZeroBaseline
from llm2.models.base import Prediction


def test_zero_baseline_prediction_shape():
    X = np.random.randn(10, 3)
    y = np.random.randn(10)
    m = ZeroBaseline().fit(X, y)
    pred = m.predict(X)
    assert isinstance(pred, Prediction)
    assert pred.mean is not None
    assert len(pred.mean) == 10
    assert np.all(pred.mean == 0)


def test_historical_mean_matches_train_mean():
    X = np.ones((5, 2))
    y = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    m = HistoricalMeanBaseline().fit(X, y)
    pred = m.predict(X)
    assert pred.mean is not None
    assert np.allclose(pred.mean, 3.0)
