"""Quantile-band + ATR-residual level predictions (walk-forward helpers)."""

from __future__ import annotations

import numpy as np

from llm2.pivot.train.multihead import _fit_predict_reg
from llm2.validation.folds import build_outer_folds


def score_level_bands(
    X: np.ndarray,
    y_level_ret: np.ndarray,
    atr_frac: np.ndarray,
    ts_ms: np.ndarray,
    *,
    horizon_bars: int = 4,
    target: str = "ret",  # ret | atr_resid
) -> dict[str, np.ndarray]:
    """Outer WF q25/q50/q75 level predictions in return space.

    ``atr_resid`` trains on y/atr then multiplies predictions by atr at apply time.
    """
    n = len(ts_ms)
    q25 = np.full(n, np.nan)
    q50 = np.full(n, np.nan)
    q75 = np.full(n, np.nan)
    purge = max(horizon_bars + 6, 24)
    folds = build_outer_folds(ts_ms, purge_bars=purge, embargo_bars=purge)

    y = np.asarray(y_level_ret, dtype=float)
    atr = np.asarray(atr_frac, dtype=float)
    if target == "atr_resid":
        with np.errstate(divide="ignore", invalid="ignore"):
            y_tr_base = np.where(np.isfinite(atr) & (atr > 1e-8), y / atr, np.nan)
    else:
        y_tr_base = y

    for fold in folds:
        tr, te = fold.train_indices, fold.oos_indices
        if tr.size < 400 or te.size < 80:
            continue
        tr_ok = tr[np.isfinite(y_tr_base[tr])]
        if tr_ok.size < 80:
            continue
        for alpha, dest in ((0.25, q25), (0.50, q50), (0.75, q75)):
            pred = _fit_predict_reg(
                X[tr_ok],
                y_tr_base[tr_ok],
                X[te],
                model_name="lgbm",
                is_baserate=False,
                quantile_alpha=float(alpha),
            )
            if target == "atr_resid":
                pred = pred * atr[te]
            dest[te] = pred
    width = q75 - q25
    return {"q25": q25, "q50": q50, "q75": q75, "width": width}
