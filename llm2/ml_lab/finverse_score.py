"""FinVerse-style point-forecast metrics (not a model).

FinVerse is an evaluation protocol: point accuracy, then a decision/portfolio
score. Cross-sectional ranking is skipped here because this lab trades one
symbol at a time. Portfolio scoring is the tradesim arm, not this helper.
"""

from __future__ import annotations

from typing import Any

import numpy as np


def point_metrics(pred: np.ndarray, y: np.ndarray) -> dict[str, Any]:
    p = np.asarray(pred, dtype=float)
    t = np.asarray(y, dtype=float)
    m = np.isfinite(p) & np.isfinite(t)
    n = int(m.sum())
    if n < 40:
        return {"n_skill": n, "spearman_ic": float("nan"), "directional_acc": float("nan")}
    pp = p[m]
    tt = t[m]
    if np.std(pp) < 1e-12 or np.std(tt) < 1e-12:
        ic = 0.0
    else:
        ic = float(np.corrcoef(pp.argsort().argsort(), tt.argsort().argsort())[0, 1])
    da = float(np.mean(np.sign(pp) == np.sign(tt)))
    return {"n_skill": n, "spearman_ic": ic, "directional_acc": da}
