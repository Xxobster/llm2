"""Multi-head walk-forward: P(any), P(high|event), time-to-pivot, level move."""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.metrics import (
    average_precision_score,
    brier_score_loss,
    mean_absolute_error,
    roc_auc_score,
)
from sklearn.preprocessing import StandardScaler

from llm2.validation.folds import build_outer_folds
from llm2.pivot.train.walk_forward import ModelSpec


def _safe_ap(y: np.ndarray, s: np.ndarray) -> float:
    if len(y) < 10 or len(np.unique(y)) < 2:
        return float("nan")
    return float(average_precision_score(y, s))


def _safe_auc(y: np.ndarray, s: np.ndarray) -> float:
    if len(y) < 10 or len(np.unique(y)) < 2:
        return float("nan")
    return float(roc_auc_score(y, s))


def expected_calibration_error(
    y: np.ndarray, p: np.ndarray, *, n_bins: int = 10
) -> float:
    """Binary ECE (equal-width bins on predicted probability)."""
    y = np.asarray(y, dtype=float)
    p = np.clip(np.asarray(p, dtype=float), 1e-6, 1 - 1e-6)
    if len(y) < 20:
        return float("nan")
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    n = len(y)
    for i in range(n_bins):
        lo, hi = edges[i], edges[i + 1]
        if i == n_bins - 1:
            m = (p >= lo) & (p <= hi)
        else:
            m = (p >= lo) & (p < hi)
        if not m.any():
            continue
        ece += (m.sum() / n) * abs(float(y[m].mean()) - float(p[m].mean()))
    return float(ece)


def _binary_baserate(y_tr: np.ndarray, n: int) -> np.ndarray:
    p = float(np.mean(y_tr)) if len(y_tr) else 0.5
    return np.full(n, p, dtype=float)


def _fit_predict_binary(
    X_tr: np.ndarray,
    y_tr: np.ndarray,
    X_te: np.ndarray,
    *,
    model_spec: ModelSpec | None,
    is_baserate: bool,
) -> np.ndarray:
    if is_baserate or model_spec is None:
        return _binary_baserate(y_tr, len(X_te))
    if len(np.unique(y_tr)) < 2:
        return _binary_baserate(y_tr, len(X_te))
    model = model_spec.builder()
    Xtr, Xte = X_tr, X_te
    if model_spec.needs_scale:
        sc = StandardScaler()
        Xtr = sc.fit_transform(np.nan_to_num(Xtr, nan=0.0))
        Xte = sc.transform(np.nan_to_num(Xte, nan=0.0))
    else:
        Xtr = np.nan_to_num(Xtr, nan=0.0)
        Xte = np.nan_to_num(Xte, nan=0.0)
    model.fit(Xtr, y_tr)
    if hasattr(model, "predict_proba"):
        pr = model.predict_proba(Xte)
        classes = list(getattr(model, "classes_", [0, 1]))
        if 1 in classes:
            return pr[:, classes.index(1)]
        return pr[:, -1]
    pred = np.asarray(model.predict(Xte), dtype=float)
    return pred


def _fit_predict_reg(
    X_tr: np.ndarray,
    y_tr: np.ndarray,
    X_te: np.ndarray,
    *,
    model_name: str,
    is_baserate: bool,
    quantile_alpha: float | None = None,
) -> np.ndarray:
    mask = np.isfinite(y_tr)
    if is_baserate or mask.sum() < 30:
        mu = float(np.nanmean(y_tr[mask])) if mask.any() else 0.0
        return np.full(len(X_te), mu)
    Xtr = np.nan_to_num(X_tr[mask], nan=0.0)
    ytr = y_tr[mask]
    Xte = np.nan_to_num(X_te, nan=0.0)
    try:
        import lightgbm as lgb

        kw: dict = {
            "n_estimators": 150,
            "num_leaves": 31,
            "learning_rate": 0.05,
            "verbosity": -1,
            "random_state": 20260810,
        }
        if quantile_alpha is not None:
            kw["objective"] = "quantile"
            kw["alpha"] = float(quantile_alpha)
        reg = lgb.LGBMRegressor(**kw)
        reg.fit(Xtr, ytr)
        return np.asarray(reg.predict(Xte), dtype=float)
    except Exception:  # noqa: BLE001
        from sklearn.ensemble import HistGradientBoostingRegressor

        reg = HistGradientBoostingRegressor(max_depth=6, learning_rate=0.05, max_iter=120)
        reg.fit(Xtr, ytr)
        return np.asarray(reg.predict(Xte), dtype=float)


def evaluate_binary(y: np.ndarray, p: np.ndarray) -> dict[str, float]:
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return {
        "n": float(len(y)),
        "frac_pos": float(np.mean(y)),
        "pr_auc": _safe_ap(y, p),
        "roc_auc": _safe_auc(y, p),
        "brier": float(brier_score_loss(y, p)) if len(y) else float("nan"),
        "ece": expected_calibration_error(y, p),
    }


def multihead_walk_forward(
    samp: dict[str, Any],
    *,
    model_spec: ModelSpec | None,
    purge_bars: int,
    embargo_bars: int,
    is_baserate: bool = False,
) -> dict[str, Any]:
    """Outer walk-forward for any / high|event / time / level heads."""
    X = samp["X"]
    y_any = samp["y_any"]
    y_high = samp["y_high_given"]
    y_time = samp["y_time_bars"]
    y_level = samp["y_level_ret"]
    ts = samp["ts_ms"]
    folds = build_outer_folds(ts, purge_bars=purge_bars, embargo_bars=embargo_bars)

    store: dict[str, list] = {
        "any": [],
        "high_given": [],
        "time": [],
        "level": [],
    }
    oos: dict[str, list] = {k: {"y": [], "p": []} for k in store}

    for fold in folds:
        tr, te = fold.train_indices, fold.oos_indices
        if tr.size < 400 or te.size < 80:
            continue
        # --- head: any ---
        p_any = _fit_predict_binary(
            X[tr], y_any[tr], X[te], model_spec=model_spec, is_baserate=is_baserate
        )
        m_any = evaluate_binary(y_any[te], p_any)
        m_any["fold"] = fold.fold_index
        store["any"].append(m_any)
        oos["any"]["y"].append(y_any[te])
        oos["any"]["p"].append(p_any)

        # --- head: high | event ---
        tr_ev = tr[y_high[tr] >= 0]
        te_ev = te[y_high[te] >= 0]
        if tr_ev.size >= 80 and te_ev.size >= 20:
            p_hg = _fit_predict_binary(
                X[tr_ev],
                y_high[tr_ev],
                X[te_ev],
                model_spec=model_spec,
                is_baserate=is_baserate,
            )
            m_hg = evaluate_binary(y_high[te_ev], p_hg)
            m_hg["fold"] = fold.fold_index
            store["high_given"].append(m_hg)
            oos["high_given"]["y"].append(y_high[te_ev])
            oos["high_given"]["p"].append(p_hg)

        # --- head: time-to-event (train on events only; score OOS events) ---
        tr_t = tr[np.isfinite(y_time[tr])]
        te_t = te[np.isfinite(y_time[te])]
        if tr_t.size >= 50 and te_t.size >= 15:
            pred_t = _fit_predict_reg(
                X[tr_t],
                y_time[tr_t],
                X[te_t],
                model_name="lgbm" if not is_baserate else "base",
                is_baserate=is_baserate,
            )
            mae = float(mean_absolute_error(y_time[te_t], pred_t))
            # correlation skill
            if np.std(pred_t) > 1e-12 and np.std(y_time[te_t]) > 1e-12:
                corr = float(np.corrcoef(y_time[te_t], pred_t)[0, 1])
            else:
                corr = float("nan")
            store["time"].append(
                {
                    "fold": fold.fold_index,
                    "n": float(te_t.size),
                    "mae_bars": mae,
                    "corr": corr,
                    "mean_true_bars": float(np.mean(y_time[te_t])),
                }
            )
            oos["time"]["y"].append(y_time[te_t])
            oos["time"]["p"].append(pred_t)

        # --- head: level return at pivot ---
        tr_l = tr[np.isfinite(y_level[tr])]
        te_l = te[np.isfinite(y_level[te])]
        if tr_l.size >= 50 and te_l.size >= 15:
            pred_l = _fit_predict_reg(
                X[tr_l],
                y_level[tr_l],
                X[te_l],
                model_name="lgbm" if not is_baserate else "base",
                is_baserate=is_baserate,
            )
            mae = float(mean_absolute_error(y_level[te_l], pred_l))
            if np.std(pred_l) > 1e-12 and np.std(y_level[te_l]) > 1e-12:
                corr = float(np.corrcoef(y_level[te_l], pred_l)[0, 1])
            else:
                corr = float("nan")
            store["level"].append(
                {
                    "fold": fold.fold_index,
                    "n": float(te_l.size),
                    "mae_ret": mae,
                    "corr": corr,
                    "mean_abs_true": float(np.mean(np.abs(y_level[te_l]))),
                }
            )
            oos["level"]["y"].append(y_level[te_l])
            oos["level"]["p"].append(pred_l)

    def _pool_bin(key: str) -> dict[str, float] | None:
        if not oos[key]["y"]:
            return None
        y = np.concatenate(oos[key]["y"])
        p = np.concatenate(oos[key]["p"])
        return evaluate_binary(y, p)

    def _pool_reg(key: str, mae_name: str) -> dict[str, float] | None:
        if not oos[key]["y"]:
            return None
        y = np.concatenate(oos[key]["y"])
        p = np.concatenate(oos[key]["p"])
        mae = float(mean_absolute_error(y, p))
        corr = (
            float(np.corrcoef(y, p)[0, 1])
            if np.std(y) > 1e-12 and np.std(p) > 1e-12
            else float("nan")
        )
        return {"n": float(len(y)), mae_name: mae, "corr": corr}

    if not store["any"]:
        return {"status": "NO_FOLDS"}
    return {
        "status": "OK",
        "n_folds_any": len(store["any"]),
        "pooled": {
            "any": _pool_bin("any"),
            "high_given_event": _pool_bin("high_given"),
            "time_to_event": _pool_reg("time", "mae_bars"),
            "level_ret": _pool_reg("level", "mae_ret"),
        },
        "folds": store,
    }


def model_specs_tight() -> list[ModelSpec]:
    """LGBM + HistGB only (MLP de-prioritized)."""
    from llm2.pivot.train.walk_forward import ModelSpec

    specs: list[ModelSpec] = []
    try:
        import lightgbm as lgb

        specs.append(
            ModelSpec(
                "lgbm_m",
                lambda: lgb.LGBMClassifier(
                    n_estimators=200,
                    num_leaves=31,
                    learning_rate=0.05,
                    subsample=0.8,
                    colsample_bytree=0.8,
                    class_weight="balanced",
                    verbosity=-1,
                    random_state=20260810,
                ),
            )
        )
        specs.append(
            ModelSpec(
                "lgbm_s",
                lambda: lgb.LGBMClassifier(
                    n_estimators=100,
                    num_leaves=15,
                    learning_rate=0.05,
                    class_weight="balanced",
                    verbosity=-1,
                    random_state=20260810,
                ),
            )
        )
    except ImportError:
        pass
    try:
        from sklearn.ensemble import HistGradientBoostingClassifier

        specs.append(
            ModelSpec(
                "hist_gb",
                lambda: HistGradientBoostingClassifier(
                    max_depth=6, learning_rate=0.05, max_iter=150, random_state=20260810
                ),
            )
        )
    except ImportError:
        pass
    return specs
