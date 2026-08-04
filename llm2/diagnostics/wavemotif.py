"""Causal shape k-nearest-neighbours: do similar recent wave shapes forecast similarly?

The query is "the last L bars of the causal wave, right now, z-normalised" — a shape, not a
level, so it is comparable across regimes and price scales. Its nearest neighbours are drawn
from a **training-fold-only** pool: every neighbour's own window must end before the
forward-looking split point used for this study (``train_end``), and additionally end at
least ``embargo_bars`` (the forecast horizon, by default) before that split — otherwise a
neighbour sitting right at the boundary would carry a forward-return label that overlaps the
query period it is being used to predict, which is leakage through the label rather than
through the shape.

Both the sliding-window extraction and the nearest-neighbour search are vectorized. The
window matrix is a *view*, not a copy (``numpy.lib.stride_tricks.sliding_window_view``), and
distances are computed via ``||a - b||^2 = ||a||^2 + ||b||^2 - 2 a.b``, one matrix
multiplication per chunk of queries rather than a python loop over query bars. The only loop
in this module is over chunks of queries and over the small grid of ``(L, k)`` settings.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.stats import newey_west_tstat, normal_two_sided_p, safe_corr
from llm2.diagnostics.wave import causal_wave
from llm2.diagnostics.wave_mining_guard import forbid_analytic_import

forbid_analytic_import(globals())

L_WINDOWS: tuple[int, ...] = (16, 32)
K_NEIGHBOURS: tuple[int, ...] = (10, 50)
MIN_VALID = 100


def _sliding_z_windows(wave: np.ndarray, L: int) -> tuple[np.ndarray, np.ndarray]:
    """z-normalised windows of length ``L`` ending at each bar, and their end-positions."""
    n = wave.size
    if n < L:
        return np.empty((0, L)), np.empty((0,), dtype=int)
    windows = np.lib.stride_tricks.sliding_window_view(wave, L)  # (n-L+1, L); row i ends at i+L-1
    end_idx = np.arange(L - 1, n)
    mean = windows.mean(axis=1, keepdims=True)
    std = windows.std(axis=1, keepdims=True)
    std_safe = np.where(std > 1e-12, std, np.nan)
    z = (windows - mean) / std_safe
    return z, end_idx


def _knn_predict(
    train_windows: np.ndarray,
    train_labels: np.ndarray,
    query_windows: np.ndarray,
    k: int,
    *,
    chunk_size: int = 2000,
) -> np.ndarray:
    """Mean label of the k nearest (by Euclidean distance) train windows, per query."""
    q_total = query_windows.shape[0]
    preds = np.full(q_total, np.nan)

    finite_train = np.isfinite(train_labels) & np.isfinite(train_windows).all(axis=1)
    train_windows = train_windows[finite_train]
    train_labels = train_labels[finite_train]
    t_total = train_windows.shape[0]
    if t_total == 0 or q_total == 0:
        return preds

    kk = min(k, t_total)
    train_sq = np.sum(train_windows**2, axis=1)

    for start in range(0, q_total, chunk_size):
        end = min(q_total, start + chunk_size)
        chunk = query_windows[start:end]
        chunk_finite = np.isfinite(chunk).all(axis=1)
        if not chunk_finite.any():
            continue
        q = chunk[chunk_finite]
        q_sq = np.sum(q**2, axis=1)
        dot = q @ train_windows.T
        dist2 = q_sq[:, None] + train_sq[None, :] - 2.0 * dot
        nn_idx = np.argpartition(dist2, kk - 1, axis=1)[:, :kk]
        chunk_preds = train_labels[nn_idx].mean(axis=1)
        out = np.full(chunk.shape[0], np.nan)
        out[chunk_finite] = chunk_preds
        preds[start:end] = out
    return preds


def _corr_with_nw_se(pred: np.ndarray, realised: np.ndarray, *, lags: int) -> tuple[float, float, float]:
    """Correlation and its Newey-West-adjusted significance.

    ``corr(x, y) = mean(z_x * z_y)`` for standardised ``z_x``, ``z_y``, so the elementwise
    product series is a legitimate input to :func:`newey_west_tstat`: its mean *is* the
    correlation, and the HAC t-statistic on that mean is the dependence-aware significance
    of the correlation, appropriate here because overlapping ``horizon``-bar forward returns
    make consecutive products mechanically correlated.
    """
    mask = np.isfinite(pred) & np.isfinite(realised)
    p, r = pred[mask], realised[mask]
    if p.size < MIN_VALID:
        return float("nan"), float("nan"), float("nan")
    sp, sr = p.std(), r.std()
    if sp <= 1e-18 or sr <= 1e-18:
        return float("nan"), float("nan"), float("nan")
    product = ((p - p.mean()) / sp) * ((r - r.mean()) / sr)
    mean, t_stat = newey_west_tstat(product, lags=lags)
    return float(mean), float(t_stat), normal_two_sided_p(t_stat)


def run_shape_knn_study(
    close: pd.Series,
    *,
    period: float,
    train_end: pd.Timestamp,
    L_windows: tuple[int, ...] = L_WINDOWS,
    k_values: tuple[int, ...] = K_NEIGHBOURS,
    horizon: int = 24,
    embargo_bars: int | None = None,
) -> list[dict]:
    """Predict the ``horizon``-bar forward return from the k most similar past wave shapes.

    One row per ``(L, k)`` combination, reporting the correlation between the k-NN prediction
    and the realised forward return on the query fold (everything from ``train_end``
    onward), with a Newey-West-adjusted significance.
    """
    log_c = np.log(close.where(close > 0)).interpolate(limit_direction="both")
    wave, _, _ = causal_wave(log_c, period)
    wave_arr = wave.to_numpy()
    idx = close.index

    fwd = (log_c.shift(-horizon) - log_c).to_numpy()
    embargo = embargo_bars if embargo_bars is not None else horizon
    train_end_pos = int(idx.searchsorted(pd.Timestamp(train_end), side="right"))

    results: list[dict] = []
    for L in L_windows:
        z, end_idx = _sliding_z_windows(wave_arr, L)
        if end_idx.size == 0:
            continue
        finite = np.isfinite(z).all(axis=1)
        labels = fwd[end_idx]
        label_finite = np.isfinite(labels)

        train_mask = finite & label_finite & (end_idx < (train_end_pos - embargo))
        query_mask = finite & (end_idx >= train_end_pos)

        train_windows = z[train_mask]
        train_labels = labels[train_mask]
        query_windows = z[query_mask]
        query_labels = labels[query_mask]

        for k in k_values:
            preds = _knn_predict(train_windows, train_labels, query_windows, k)
            corr, t_stat, p_val = _corr_with_nw_se(preds, query_labels, lags=horizon)
            n_valid = int(np.sum(np.isfinite(preds) & np.isfinite(query_labels)))
            results.append(
                {
                    "L": int(L),
                    "k": int(k),
                    "n_train": int(train_windows.shape[0]),
                    "n_query": int(query_windows.shape[0]),
                    "n_valid": n_valid,
                    "corr_pred_vs_realised": corr,
                    "t_hac": t_stat,
                    "p_value": p_val,
                    "horizon": int(horizon),
                    "embargo_bars": int(embargo),
                    "train_end": str(pd.Timestamp(train_end)),
                }
            )
    return results
