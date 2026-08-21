"""Train/test SQLite split + multi-head P(event) for surviving confluence events.

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

from llm2.confluence.events import EVENT_IDS, EventPack, build_event_pack
from llm2.pivot.train.multihead import _fit_predict_binary, expected_calibration_error
from llm2.pivot.train.walk_forward import ModelSpec

try:
    import lightgbm as lgb
except ImportError:  # pragma: no cover
    lgb = None


FEATURE_COLS = (
    "rsi_14",
    "rsi_below_30",
    "rsi_above_70",
    "macd_hist",
    "macd_hist_sign",
    "adx_14",
    "plus_di",
    "minus_di",
    "adx_slope",
    "adx_stretched",
    "stoch_k",
    "stoch_d",
    "vol_z_48",
    "atr_frac",
    "ema21_dist",
    "dist_confirmed_high",
    "dist_confirmed_low",
    "broke_confirmed_high",
    "broke_confirmed_low",
    "fresh_break_high",
    "fresh_break_low",
    "pulse_dir",
    "pulse_flag",
    "range20_width",
    "close_pos_in_range20",
    "atr_pos_100",
    "ret4",
)


def chronological_cut_index(n: int, *, train_frac: float = 0.7) -> int:
    cut = int(n * float(train_frac))
    if cut < 200 or n - cut < 100:
        raise ValueError(f"split too small n={n} cut={cut}")
    return cut


def write_ohlcv_sqlite(path: Path, ohlcv: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    df = ohlcv.copy()
    if "ts_ms" not in df.columns:
        idx = pd.DatetimeIndex(pd.to_datetime(df.index, utc=True))
        df = df.assign(ts_ms=(idx.asi8 // 1_000_000).astype(np.int64))
    with sqlite3.connect(str(path)) as con:
        df.reset_index(drop=True).to_sql("ohlcv", con, index=False, if_exists="replace")


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


def pack_to_xy(pack: EventPack, event_id: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    feat = pack.features[list(FEATURE_COLS)].to_numpy(dtype=float)
    y = pack.labels[event_id].to_numpy(dtype=float)
    ok = np.isfinite(y) & np.isfinite(feat).all(axis=1)
    return feat[ok], y[ok].astype(np.int32), ok


def _lgbm() -> ModelSpec:
    if lgb is None:
        raise RuntimeError("lightgbm is required")
    return ModelSpec(
        "lgbm_m",
        lambda: lgb.LGBMClassifier(
            n_estimators=200,
            num_leaves=31,
            learning_rate=0.05,
            class_weight="balanced",
            verbosity=-1,
            random_state=20260819,
        ),
    )


def fit_event_head(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_test: np.ndarray,
) -> dict[str, Any]:
    """Fit one binary head on train; calibrate on the last 20% of train; apply to test."""
    n = len(y_train)
    cut = max(50, int(0.8 * n))
    x_fit, y_fit = x_train[:cut], y_train[:cut]
    x_cal, y_cal = x_train[cut:], y_train[cut:]
    ms = _lgbm()
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
        "test_rate": float("nan"),
    }


def fit_one_head(train_pack: EventPack, test_pack: EventPack, event_id: str) -> dict[str, Any]:
    x_tr, y_tr, _ = pack_to_xy(train_pack, event_id)
    x_te, y_te, ok_te = pack_to_xy(test_pack, event_id)
    p = np.full(len(test_pack.labels), np.nan)
    if x_tr.shape[0] < 200 or len(np.unique(y_tr)) < 2:
        return {"p_test": p, "fitted": False, "n_train": int(x_tr.shape[0])}
    head = fit_event_head(x_tr, y_tr, x_te)
    p[ok_te] = head["p_test"]
    return {
        "p_test": p,
        "fitted": True,
        "n_train": int(x_tr.shape[0]),
        "n_test": int(x_te.shape[0]),
        "ece_inner": head["ece_inner"],
        "train_rate": head["train_rate"],
        "test_rate": float(np.mean(y_te)) if y_te.size else float("nan"),
    }


def all_heads_ge_pi_star(
    probs: dict[str, np.ndarray],
    *,
    pi_star: float,
    n: int,
) -> np.ndarray:
    if not probs:
        return np.zeros(n, dtype=bool)
    mask = np.ones(n, dtype=bool)
    for p in probs.values():
        arr = np.asarray(p, dtype=float)
        if arr.size != n:
            raise ValueError("probability length mismatch")
        mask &= np.isfinite(arr) & (arr >= float(pi_star))
    return mask
