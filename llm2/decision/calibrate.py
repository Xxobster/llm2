"""Train-window probability calibration for directional scores.

Maps |model score| → estimated hit probability using isotonic regression
fitted only on a held-out slice of the training window (no OOS refit).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

try:
    from sklearn.isotonic import IsotonicRegression

    _HAS_SK = True
except ImportError:  # pragma: no cover
    _HAS_SK = False


@dataclass
class HitCalibrator:
    """Isotonic P(direction correct | |score|) on train calib slice."""

    model: Any
    fitted: bool
    n_fit: int
    ece: float | None = None

    def predict_proba_hit(self, abs_score: np.ndarray) -> np.ndarray:
        a = np.asarray(abs_score, dtype=float)
        if not self.fitted or self.model is None:
            # degenerate: raw abs-score squashed (not for production evidence)
            return np.clip(a, 0.0, 1.0)
        out = self.model.predict(a)
        return np.clip(np.asarray(out, dtype=float), 1e-6, 1.0 - 1e-6)


def fit_hit_calibrator(
    abs_scores: np.ndarray,
    hits: np.ndarray,
    *,
    min_points: int = 80,
) -> HitCalibrator:
    """Fit isotonic P(hit=1 | |score|). ``hits`` is 0/1 (direction match)."""
    x = np.asarray(abs_scores, dtype=float)
    y = np.asarray(hits, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y) & (x >= 0)
    x, y = x[mask], y[mask]
    if not _HAS_SK or x.size < int(min_points):
        return HitCalibrator(model=None, fitted=False, n_fit=int(x.size), ece=None)
    ir = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip")
    ir.fit(x, y)
    p = np.clip(ir.predict(x), 1e-6, 1.0 - 1e-6)
    # Expected Calibration Error (10 bins) on fit slice — diagnostic only
    ece = _ece(p, y, n_bins=10)
    return HitCalibrator(model=ir, fitted=True, n_fit=int(x.size), ece=ece)


def _ece(p: np.ndarray, y: np.ndarray, *, n_bins: int = 10) -> float:
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    n = len(p)
    if n == 0:
        return float("nan")
    for i in range(n_bins):
        lo, hi = bins[i], bins[i + 1]
        m = (p >= lo) & (p < hi if i < n_bins - 1 else p <= hi)
        if not np.any(m):
            continue
        ece += (np.sum(m) / n) * abs(float(np.mean(p[m])) - float(np.mean(y[m])))
    return float(ece)


def direction_hit_labels(
    pred_mean: np.ndarray,
    y_direction: np.ndarray,
    *,
    min_edge: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Rows with |mean|>=edge; hit=1 if sign(mean) matches sign(y_direction).

    Flats in y (0) count as misses when a side is taken.
    Returns abs_score, hit, mask_over_edge for full arrays.
    """
    m = np.asarray(pred_mean, dtype=float)
    y = np.asarray(y_direction, dtype=float)
    abs_m = np.abs(m)
    over = np.isfinite(m) & np.isfinite(y) & (abs_m >= float(min_edge))
    side = np.sign(m)
    side[side == 0] = 0
    y_side = np.sign(y)
    hit = ((side * y_side) > 0).astype(float)
    hit[y_side == 0] = 0.0
    return abs_m, hit, over


def train_calib_split(
    n_train: int,
    *,
    calib_frac: float = 0.20,
    min_calib: int = 200,
    min_fit: int = 500,
) -> tuple[int, int]:
    """Chronological split of train indices: [0:split) fit, [split:n) calib.

    Never use max(n*0.8, n-1) — that collapses the calib slice to 1 row.
    Returns (split, n_cal).
    """
    n = int(n_train)
    if n <= 0:
        return 0, 0
    frac = float(calib_frac)
    if frac <= 0 or frac >= 1:
        return n, 0
    n_cal_want = max(int(min_calib), int(round(n * frac)))
    n_cal_want = min(n_cal_want, max(0, n - int(min_fit)))
    if n_cal_want < int(min_calib) and n > int(min_calib) + 50:
        n_cal_want = int(min_calib)
    split = n - n_cal_want
    if split < 1:
        split = max(1, n // 2)
        n_cal_want = n - split
    return int(split), int(n_cal_want)


def bracket_path_hit_labels(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    pred_mean: np.ndarray,
    *,
    tp_pct: float,
    sl_pct: float,
    hold_bars: int,
    min_edge: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Path-aware win labels for the frozen TP/SL / max-hold bracket.

    Adverse resolution when both TP and SL would touch on the same bar
    (same spirit as engine EXEC same-bar adverse). Max-hold exit counts as
    miss if signed close move is not positive beyond fee noise (0).
    ``hit`` is 0/1 where ``over`` (eligible decision rows).
    """
    h = np.asarray(high, dtype=float)
    lo = np.asarray(low, dtype=float)
    c = np.asarray(close, dtype=float)
    m = np.asarray(pred_mean, dtype=float)
    n = len(c)
    abs_m = np.abs(m)
    over = np.isfinite(m) & np.isfinite(c) & (c > 0) & (abs_m >= float(min_edge))
    hit = np.zeros(n, dtype=float)
    hold = max(1, int(hold_bars))
    tp = float(tp_pct)
    sl = float(sl_pct)

    # Sequential path resolve only over eligible rows (calib slice ~thousands).
    idxs = np.flatnonzero(over)
    for i in idxs:
        entry = float(c[i])
        if not np.isfinite(entry) or entry <= 0:
            over[i] = False
            continue
        side = 1.0 if m[i] > 0 else -1.0
        if side > 0:
            tp_px = entry * (1.0 + tp)
            sl_px = entry * (1.0 - sl)
        else:
            tp_px = entry * (1.0 - tp)
            sl_px = entry * (1.0 + sl)
        resolved = False
        end = min(n, int(i) + 1 + hold)
        for j in range(int(i) + 1, end):
            hj, lj = float(h[j]), float(lo[j])
            if not (np.isfinite(hj) and np.isfinite(lj)):
                continue
            if side > 0:
                hit_tp = hj >= tp_px
                hit_sl = lj <= sl_px
            else:
                hit_tp = lj <= tp_px
                hit_sl = hj >= sl_px
            if hit_tp and hit_sl:
                hit[i] = 0.0  # adverse: assume SL first
                resolved = True
                break
            if hit_sl:
                hit[i] = 0.0
                resolved = True
                break
            if hit_tp:
                hit[i] = 1.0
                resolved = True
                break
        if not resolved:
            # max-hold MTM sign vs entry (path unresolved)
            j = min(n - 1, int(i) + hold)
            cj = float(c[j])
            if np.isfinite(cj) and entry > 0:
                signed = side * (cj / entry - 1.0)
                hit[i] = 1.0 if signed > 0 else 0.0
            else:
                hit[i] = 0.0
    return abs_m, hit, over
