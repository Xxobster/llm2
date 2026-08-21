"""Walk-forward pivot first-event classification: multi model × feature × param."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Callable

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    brier_score_loss,
    log_loss,
    roc_auc_score,
)
from sklearn.preprocessing import StandardScaler

from llm2.validation.folds import build_outer_folds


def _safe_ap(y_true: np.ndarray, score: np.ndarray) -> float:
    if len(np.unique(y_true)) < 2:
        return float("nan")
    return float(average_precision_score(y_true, score))


def _safe_auc(y_true: np.ndarray, score: np.ndarray) -> float:
    if len(np.unique(y_true)) < 2:
        return float("nan")
    return float(roc_auc_score(y_true, score))


def _brier_multiclass(y: np.ndarray, proba: np.ndarray, n_classes: int = 3) -> float:
    # one-hot Brier mean
    oh = np.zeros((len(y), n_classes), dtype=float)
    m = (y >= 0) & (y < n_classes)
    oh[np.arange(len(y))[m], y[m]] = 1.0
    return float(np.mean(np.sum((proba - oh) ** 2, axis=1)))


@dataclass
class ModelSpec:
    name: str
    builder: Callable[[], Any]
    needs_scale: bool = False


def model_catalog() -> list[ModelSpec]:
    specs: list[ModelSpec] = [
        ModelSpec(
            "logistic",
            lambda: LogisticRegression(
                max_iter=800,
                class_weight="balanced",
                solver="lbfgs",
            ),
            needs_scale=True,
        ),
    ]
    try:
        import lightgbm as lgb

        for n_est, leaves, lr, tag in (
            (80, 15, 0.05, "lgbm_s"),
            (200, 31, 0.05, "lgbm_m"),
            (150, 63, 0.03, "lgbm_deep"),
        ):
            specs.append(
                ModelSpec(
                    tag,
                    lambda n_est=n_est, leaves=leaves, lr=lr: lgb.LGBMClassifier(
                        n_estimators=n_est,
                        num_leaves=leaves,
                        learning_rate=lr,
                        subsample=0.8,
                        colsample_bytree=0.8,
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
                    max_depth=6,
                    learning_rate=0.05,
                    max_iter=150,
                    random_state=20260810,
                ),
            )
        )
    except ImportError:
        pass
    # Neural MLP (tabular) — not a chat LLM; numerical multi-class soft head
    try:
        from sklearn.neural_network import MLPClassifier

        specs.append(
            ModelSpec(
                "mlp_sklearn",
                lambda: MLPClassifier(
                    hidden_layer_sizes=(64, 32),
                    max_iter=80,
                    early_stopping=True,
                    random_state=20260810,
                ),
                needs_scale=True,
            )
        )
    except ImportError:
        pass
    return specs


def baserate_proba(y_train: np.ndarray, n: int) -> np.ndarray:
    counts = np.bincount(y_train, minlength=3).astype(float)
    if counts.sum() <= 0:
        p = np.array([1.0, 0.0, 0.0])
    else:
        p = counts / counts.sum()
    return np.tile(p, (n, 1))


def evaluate_proba(y: np.ndarray, proba: np.ndarray) -> dict[str, float]:
    proba = np.clip(proba, 1e-6, 1 - 1e-6)
    proba = proba / proba.sum(axis=1, keepdims=True)
    # any-pivot score
    p_any = 1.0 - proba[:, 0]
    y_any = (y != 0).astype(int)
    # side among events: restrict to y!=0 for high vs low hard
    metrics = {
        "n": float(len(y)),
        "brier_mc": _brier_multiclass(y, proba),
        "log_loss": float(log_loss(y, proba, labels=[0, 1, 2])),
        "pr_auc_any": _safe_ap(y_any, p_any),
        "roc_auc_any": _safe_auc(y_any, p_any),
        "brier_any": float(brier_score_loss(y_any, p_any)) if y_any.size else float("nan"),
        "frac_any": float(y_any.mean()) if len(y) else float("nan"),
        "acc_side_argmax": float(np.mean(np.argmax(proba, axis=1) == y)),
    }
    # precision@top-k% of p_any for "any pivot" — crude early-warning
    if len(y) >= 50:
        k = max(1, int(0.05 * len(y)))
        top = np.argsort(-p_any)[:k]
        metrics["precision_top5pct_any"] = float(y_any[top].mean())
    else:
        metrics["precision_top5pct_any"] = float("nan")
    return metrics


def walk_forward_eval(
    X: np.ndarray,
    y: np.ndarray,
    ts_ms: np.ndarray,
    *,
    model_spec: ModelSpec | None,
    purge_bars: int,
    embargo_bars: int,
    is_baserate: bool = False,
) -> dict[str, Any]:
    folds = build_outer_folds(
        ts_ms, purge_bars=purge_bars, embargo_bars=embargo_bars
    )
    fold_metrics = []
    oos_y = []
    oos_p = []
    for fold in folds:
        tr, te = fold.train_indices, fold.oos_indices
        if tr.size < 300 or te.size < 50:
            continue
        y_tr, y_te = y[tr], y[te]
        if len(np.unique(y_tr)) < 2:
            continue
        if is_baserate:
            proba = baserate_proba(y_tr, len(te))
        else:
            assert model_spec is not None
            model = model_spec.builder()
            X_tr, X_te = X[tr], X[te]
            if model_spec.needs_scale:
                sc = StandardScaler()
                X_tr = sc.fit_transform(np.nan_to_num(X_tr, nan=0.0))
                X_te = sc.transform(np.nan_to_num(X_te, nan=0.0))
            else:
                X_tr = np.nan_to_num(X_tr, nan=0.0)
                X_te = np.nan_to_num(X_te, nan=0.0)
            model.fit(X_tr, y_tr)
            if hasattr(model, "predict_proba"):
                raw = model.predict_proba(X_te)
                # align to classes 0,1,2
                proba = np.zeros((len(te), 3), dtype=float)
                classes = list(getattr(model, "classes_", [0, 1, 2]))
                for j, cls in enumerate(classes):
                    if int(cls) in (0, 1, 2):
                        proba[:, int(cls)] = raw[:, j]
                # fill missing class prob with small mass
                if proba.sum(axis=1).min() <= 0:
                    proba = proba + 1e-6
                proba = proba / proba.sum(axis=1, keepdims=True)
            else:
                pred = np.asarray(model.predict(X_te)).astype(int)
                proba = np.zeros((len(te), 3))
                for i, p in enumerate(pred):
                    proba[i, int(np.clip(p, 0, 2))] = 1.0
        m = evaluate_proba(y_te, proba)
        m["fold"] = fold.fold_index
        fold_metrics.append(m)
        oos_y.append(y_te)
        oos_p.append(proba)
    if not fold_metrics:
        return {"status": "NO_FOLDS", "folds": []}
    pooled_y = np.concatenate(oos_y)
    pooled_p = np.vstack(oos_p)
    pooled = evaluate_proba(pooled_y, pooled_p)
    # mean outer
    keys = [k for k in fold_metrics[0] if k not in {"fold", "n"}]
    summary = {
        "status": "OK",
        "n_folds": len(fold_metrics),
        "pooled": pooled,
        "mean_fold": {
            k: float(np.nanmean([f[k] for f in fold_metrics])) for k in keys
        },
        "folds": fold_metrics,
    }
    return summary
