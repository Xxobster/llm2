"""Inner-fold Platt/isotonic calibration and time-bucket heads (research-only)."""

from __future__ import annotations

import numpy as np
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression


def fit_binary_calibrator(
    y: np.ndarray,
    p_raw: np.ndarray,
    *,
    method: str = "isotonic",
) -> object:
    """Fit calibrator on (inner) raw probabilities. Never use outer OOS labels."""
    y = np.asarray(y, dtype=int)
    p = np.clip(np.asarray(p_raw, dtype=float), 1e-6, 1 - 1e-6)
    m = np.isfinite(p) & np.isfinite(y)
    y, p = y[m], p[m]
    if len(y) < 50 or len(np.unique(y)) < 2:
        return ("identity", None)
    if method == "platt":
        # logistic on logit(p)
        logit = np.log(p / (1.0 - p)).reshape(-1, 1)
        lr = LogisticRegression(max_iter=500)
        lr.fit(logit, y)
        return ("platt", lr)
    iso = IsotonicRegression(out_of_bounds="clip", y_min=0.0, y_max=1.0)
    iso.fit(p, y)
    return ("isotonic", iso)


def apply_calibrator(cal: object, p_raw: np.ndarray) -> np.ndarray:
    p = np.clip(np.asarray(p_raw, dtype=float), 1e-6, 1 - 1e-6)
    kind, model = cal  # type: ignore[misc]
    if kind == "identity" or model is None:
        return p
    if kind == "platt":
        logit = np.log(p / (1.0 - p)).reshape(-1, 1)
        return model.predict_proba(logit)[:, 1]
    return np.asarray(model.predict(p), dtype=float)


def time_bucket_labels(y_time_bars: np.ndarray, *, horizon_bars: int) -> np.ndarray:
    """Discretize time-to-pivot into bins: 0=no event, 1=early, 2=mid, 3=late within H."""
    y = np.zeros(len(y_time_bars), dtype=np.int64)
    t = y_time_bars
    hit = np.isfinite(t) & (t > 0)
    # thirds of horizon
    h = max(int(horizon_bars), 1)
    e1, e2 = h / 3.0, 2.0 * h / 3.0
    y[hit & (t <= e1)] = 1
    y[hit & (t > e1) & (t <= e2)] = 2
    y[hit & (t > e2)] = 3
    return y
