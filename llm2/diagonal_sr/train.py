"""Train/test SQLite split + multi-model P(event) heads for diagonal S/R.

Train and test features are built on separate OHLCV frames (never a joint
scaler / joint builder pass).
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression

from llm2.confluence.train import chronological_cut_index, write_ohlcv_sqlite
from llm2.diagonal_sr.events import EventPack, feature_cols_for
from llm2.pivot.train.multihead import _fit_predict_binary, expected_calibration_error
from llm2.pivot.train.walk_forward import ModelSpec

__all__ = [
    "chronological_cut_index",
    "fit_one_head",
    "load_ohlcv_sqlite",
    "split_ohlcv_files",
]

try:
    import lightgbm as lgb
except ImportError:  # pragma: no cover
    lgb = None


def split_ohlcv_files(
    ohlcv: pd.DataFrame,
    *,
    train_path: Path,
    test_path: Path,
    train_frac: float = 0.7,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    cut = chronological_cut_index(len(ohlcv), train_frac=train_frac)
    train = ohlcv.iloc[:cut].copy()
    test = ohlcv.iloc[cut:].copy()
    write_ohlcv_sqlite(train_path, train)
    write_ohlcv_sqlite(test_path, test)
    return train, test


def pack_to_xy(
    pack: EventPack, event_id: str, *, generation: str
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    cols = [c for c in feature_cols_for(generation) if c in pack.features.columns]
    # Also allow HTF columns present in the pack.
    extra = [c for c in pack.features.columns if c.startswith("htf_") and c not in cols]
    cols = cols + sorted(extra)
    feat = pack.features[cols].to_numpy(dtype=float)
    y = pack.labels[event_id].to_numpy(dtype=float)
    ok = np.isfinite(y) & np.isfinite(feat).all(axis=1)
    return feat[ok], y[ok].astype(np.int32), ok


def model_spec(name: str) -> ModelSpec:
    if name == "lgbm":
        if lgb is None:
            raise RuntimeError("lightgbm is required")
        return ModelSpec(
            "lgbm",
            lambda: lgb.LGBMClassifier(
                n_estimators=200,
                num_leaves=31,
                learning_rate=0.05,
                class_weight="balanced",
                verbosity=-1,
                random_state=20260821,
            ),
        )
    if name == "lgbm_shallow":
        if lgb is None:
            raise RuntimeError("lightgbm is required")
        return ModelSpec(
            "lgbm_shallow",
            lambda: lgb.LGBMClassifier(
                n_estimators=150,
                max_depth=3,
                num_leaves=8,
                learning_rate=0.05,
                class_weight="balanced",
                verbosity=-1,
                random_state=20260821,
            ),
        )
    if name == "ridge":
        return ModelSpec(
            "ridge",
            lambda: LogisticRegression(
                penalty="l2",
                C=1.0,
                class_weight="balanced",
                max_iter=500,
                random_state=20260821,
            ),
        )
    raise ValueError(f"unknown model {name}")


def fit_event_head(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_test: np.ndarray,
    *,
    model_name: str = "lgbm",
) -> dict[str, Any]:
    n = len(y_train)
    cut = max(50, int(0.8 * n))
    x_fit, y_fit = x_train[:cut], y_train[:cut]
    x_cal, y_cal = x_train[cut:], y_train[cut:]
    ms = model_spec(model_name)
    p_cal_raw = _fit_predict_binary(x_fit, y_fit, x_cal, model_spec=ms, is_baserate=False)
    iso = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip")
    finite = np.isfinite(p_cal_raw) & np.isfinite(y_cal)
    if finite.sum() >= 30 and len(np.unique(y_cal[finite])) >= 2:
        iso.fit(p_cal_raw[finite], y_cal[finite])
        p_cal = np.clip(iso.predict(p_cal_raw), 1e-6, 1 - 1e-6)
        ece = expected_calibration_error(y_cal[finite], p_cal[finite])
    else:
        iso = None
        p_cal = p_cal_raw
        ece = float("nan")
    p_te_raw = _fit_predict_binary(x_train, y_train, x_test, model_spec=ms, is_baserate=False)
    if iso is not None:
        p_te = np.clip(iso.predict(p_te_raw), 1e-6, 1 - 1e-6)
    else:
        p_te = np.clip(p_te_raw, 1e-6, 1 - 1e-6)
    return {
        "p_test": p_te,
        "ece_inner": float(ece) if np.isfinite(ece) else float("nan"),
        "train_rate": float(np.mean(y_train)),
        "model": model_name,
    }


def fit_one_head(
    train_pack: EventPack,
    test_pack: EventPack,
    event_id: str,
    *,
    generation: str = "A",
    model_name: str = "lgbm",
) -> dict[str, Any]:
    x_tr, y_tr, _ = pack_to_xy(train_pack, event_id, generation=generation)
    x_te, y_te, ok_te = pack_to_xy(test_pack, event_id, generation=generation)
    p = np.full(len(test_pack.labels), np.nan)
    if x_tr.shape[0] < 200 or len(np.unique(y_tr)) < 2:
        return {
            "p_test": p,
            "fitted": False,
            "n_train": int(x_tr.shape[0]),
            "model": model_name,
        }
    head = fit_event_head(x_tr, y_tr, x_te, model_name=model_name)
    p[ok_te] = head["p_test"]
    return {
        "p_test": p,
        "fitted": True,
        "n_train": int(x_tr.shape[0]),
        "n_test": int(x_te.shape[0]),
        "ece_inner": head["ece_inner"],
        "train_rate": head["train_rate"],
        "test_rate": float(np.mean(y_te)) if y_te.size else float("nan"),
        "model": model_name,
    }


def load_ohlcv_sqlite(path: Path) -> pd.DataFrame:
    with sqlite3.connect(str(path)) as con:
        df = pd.read_sql("SELECT * FROM ohlcv", con)
    if "ts_ms" in df.columns:
        idx = pd.to_datetime(df["ts_ms"].to_numpy(dtype=np.int64), unit="ms", utc=True)
        df = df.drop(columns=["ts_ms"])
        df.index = idx
    return df
