"""Persistable one-head event filter used by autonomy hunt gens 013/376/705.

Matches ``scripts/run_autonomy_public_indicator_hunt.py``:
Light Gradient Boosting Machine on train, isotonic on the last 20% of train,
then a second model fit on all train for live / test scores.

Live must refuse a NaN feature row. Do not zero-fill.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression

from llm2.confluence.train import FEATURE_COLS as BASE_FEATURE_COLS
from llm2.confluence.train import _lgbm
from llm2.pivot.strategy.ev import net_bracket_magnitudes
from llm2.pivot.train.multihead import expected_calibration_error
from llm2.research_policy import PolicyError

from llm2.autonomy.packs import EXTRA_FEATURE_COLS, build_features_for_guard


FILTER_FEATURE_CANDIDATES: tuple[str, ...] = tuple(BASE_FEATURE_COLS) + tuple(EXTRA_FEATURE_COLS)


def pi_star_1pct() -> float:
    return float(net_bracket_magnitudes(0.01, 0.01).pi_star)


def feature_columns_present(frame: pd.DataFrame) -> list[str]:
    return [c for c in FILTER_FEATURE_CANDIDATES if c in frame.columns]


def _positive_class_proba(model: Any, x: np.ndarray) -> np.ndarray:
    pr = np.asarray(model.predict_proba(x), dtype=float)
    classes = list(getattr(model, "classes_", [0, 1]))
    if 1 in classes:
        return pr[:, classes.index(1)]
    return pr[:, -1]


def fit_filter_head(
    x_train: np.ndarray,
    y_train: np.ndarray,
) -> dict[str, Any]:
    """Fit the hunt head and keep the live model + isotonic calibrator."""
    y = np.asarray(y_train, dtype=np.int32)
    x = np.asarray(x_train, dtype=float)
    if x.shape[0] < 200 or len(np.unique(y)) < 2:
        raise PolicyError(f"filter head too thin n={x.shape[0]} classes={np.unique(y)}")
    n = len(y)
    cut = max(50, int(0.8 * n))
    x_fit, y_fit = x[:cut], y[:cut]
    x_cal, y_cal = x[cut:], y[cut:]
    spec = _lgbm()
    cal_model = spec.builder()
    cal_model.fit(x_fit, y_fit)
    p_cal_raw = _positive_class_proba(cal_model, x_cal)
    iso: IsotonicRegression | None
    finite = np.isfinite(p_cal_raw) & np.isfinite(y_cal)
    if int(finite.sum()) >= 30 and len(np.unique(y_cal[finite])) >= 2:
        iso = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip")
        iso.fit(p_cal_raw[finite], y_cal[finite])
        p_cal = np.clip(iso.predict(p_cal_raw), 1e-6, 1.0 - 1e-6)
        ece = expected_calibration_error(y_cal[finite], p_cal[finite])
    else:
        iso = None
        ece = float("nan")
    live_model = spec.builder()
    live_model.fit(x, y)
    return {
        "model": live_model,
        "iso": iso,
        "ece_inner": float(ece) if np.isfinite(ece) else float("nan"),
        "train_rate": float(np.mean(y)),
        "n_train": int(n),
    }


def predict_filter_proba(model: Any, iso: Any, x: np.ndarray) -> np.ndarray:
    raw = _positive_class_proba(model, np.asarray(x, dtype=float))
    if iso is not None:
        return np.clip(np.asarray(iso.predict(raw), dtype=float), 1e-6, 1.0 - 1e-6)
    return np.clip(raw, 1e-6, 1.0 - 1e-6)


def score_filter_tip(
    ohlcv: pd.DataFrame,
    *,
    feature_columns: list[str],
    model: Any,
    iso: Any,
) -> dict[str, Any]:
    """Score the last closed bar. Refuse NaN features (no fill)."""
    if build_features_for_guard is None:
        raise PolicyError("autonomy feature builder missing")
    feats = build_features_for_guard(ohlcv)
    cols = list(feature_columns)
    row = feats.reindex(columns=cols).iloc[-1]
    nan_cols = [c for c in cols if pd.isna(row[c])]
    if nan_cols:
        return {"ok": False, "reason": "nan_features", "nan_cols": nan_cols, "p_event": float("nan")}
    x = row.to_numpy(dtype=float).reshape(1, -1)
    if not np.isfinite(x).all():
        return {"ok": False, "reason": "nan_features", "nan_cols": nan_cols, "p_event": float("nan")}
    p = float(predict_filter_proba(model, iso, x)[0])
    return {"ok": True, "reason": "scored", "nan_cols": [], "p_event": p, "values": {c: float(row[c]) for c in cols}}


def save_filter_head(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(payload, path)


def load_filter_head(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)
    return joblib.load(path)
