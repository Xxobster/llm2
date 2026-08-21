"""Position size from calibrated p(any) — train-only edges, no outer-OOS fit."""

from __future__ import annotations

import numpy as np


def size_mult_linear(
    p_any: np.ndarray,
    thr: np.ndarray | float,
    *,
    lo: float = 0.5,
    hi: float = 2.0,
) -> np.ndarray:
    """``clip(p_any / threshold, lo, hi)``. At the gate this is about 1×."""
    p = np.asarray(p_any, dtype=float)
    t = np.asarray(thr, dtype=float)
    if t.ndim == 0:
        t = np.full(p.shape, float(t))
    t = np.where(np.isfinite(t) & (t > 1e-6), t, 0.35)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = p / t
    out = np.clip(out, float(lo), float(hi))
    out[~np.isfinite(out)] = 1.0
    return out.astype(float)


def size_mult_tertile(
    p_any: np.ndarray,
    gated: np.ndarray,
    *,
    train_frac: float = 0.7,
    levels: tuple[float, float, float] = (0.5, 1.0, 1.5),
) -> tuple[np.ndarray, dict]:
    """Map gated p(any) into three sizes. Edges from the first ``train_frac`` gated rows."""
    p = np.asarray(p_any, dtype=float)
    g = np.asarray(gated, dtype=bool)
    idx = np.flatnonzero(g)
    out = np.ones(len(p), dtype=float)
    if idx.size < 30:
        return out, {"status": "TOO_FEW", "edges": None}
    cut = max(10, int(float(train_frac) * idx.size))
    train_p = p[idx[:cut]]
    train_p = train_p[np.isfinite(train_p)]
    if train_p.size < 20:
        return out, {"status": "TOO_FEW", "edges": None}
    e1, e2 = np.nanpercentile(train_p, [100.0 / 3.0, 200.0 / 3.0])
    gp = p[g]
    bucket = np.zeros(gp.size, dtype=np.int64)
    bucket[np.isfinite(gp) & (gp >= e1)] = 1
    bucket[np.isfinite(gp) & (gp >= e2)] = 2
    lv = np.asarray(levels, dtype=float)
    out[g] = lv[bucket]
    return out, {"status": "OK", "edges": [float(e1), float(e2)], "levels": list(lv)}
