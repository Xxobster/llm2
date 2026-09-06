"""Training-free retrieval forecast (KReF-style), causal on closed bars only.

KReF (Kolmogorov–Arnold Representation Features is a different paper; this module
implements the **training-free retrieval** recipe: embed each lookback, retrieve
similar historical lookbacks whose futures are already known, and use the
similarity-weighted future returns as the forecast.

No warehouse join. Embeddings are built from the handed Open-High-Low-Close
series only, so a later bar cannot change an earlier prediction.
"""

from __future__ import annotations

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

DEFAULT_LOOKBACK = 32
DEFAULT_ARCHIVE = 512
DEFAULT_NEIGHBORS = 32
DEFAULT_PURGE = 1
DEFAULT_CHUNK = 4096


def log_returns(close: np.ndarray) -> np.ndarray:
    c = np.asarray(close, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        r = np.diff(np.log(np.clip(c, 1e-12, None)), prepend=np.nan)
    r[0] = 0.0
    r = np.where(np.isfinite(r), r, 0.0)
    return r.astype(np.float32)


def lookback_embeddings(close: np.ndarray, *, lookback: int = DEFAULT_LOOKBACK) -> np.ndarray:
    """L2-normalised return windows ending at each bar. Row t uses bars t-L+1..t."""
    r = log_returns(close)
    L = int(lookback)
    n = int(r.size)
    if n < L:
        return np.zeros((n, L), dtype=np.float32)
    windows = sliding_window_view(r, L)  # (n-L+1, L)
    pad = np.zeros((L - 1, L), dtype=np.float32)
    emb = np.concatenate([pad, windows.astype(np.float32)], axis=0)
    nrm = np.linalg.norm(emb, axis=1, keepdims=True)
    nrm = np.maximum(nrm, 1e-8)
    return (emb / nrm).astype(np.float32)


def forward_return(close: np.ndarray, horizon: int) -> np.ndarray:
    c = np.asarray(close, dtype=np.float64)
    h = int(horizon)
    out = np.full(c.size, np.nan, dtype=np.float64)
    if h <= 0 or c.size <= h:
        return out
    with np.errstate(divide="ignore", invalid="ignore"):
        out[:-h] = c[h:] / np.where(c[:-h] > 0, c[:-h], np.nan) - 1.0
    return out


def retrieve_forecast(
    embeddings: np.ndarray,
    fwd: np.ndarray,
    *,
    archive: int = DEFAULT_ARCHIVE,
    neighbors: int = DEFAULT_NEIGHBORS,
    horizon: int = 8,
    purge: int = DEFAULT_PURGE,
    chunk: int = DEFAULT_CHUNK,
) -> np.ndarray:
    """Causal weighted-mean future return from similar past lookbacks.

    For query bar ``t`` the archive ends at ``t - horizon - purge`` so every
    retrieved future is fully observed before ``t``.
    """
    emb = np.asarray(embeddings, dtype=np.float32)
    y = np.asarray(fwd, dtype=np.float32)
    n, _d = emb.shape
    W = int(archive)
    K = int(neighbors)
    offset = int(horizon) + int(purge)
    pred = np.full(n, np.nan, dtype=np.float32)
    if n < W + offset + 2:
        return pred
    windows = np.moveaxis(sliding_window_view(emb, W, axis=0), -1, 1)  # (n-W+1, W, d)
    y_win = sliding_window_view(y, W)  # (n-W+1, W)
    q_idx = np.arange(W + offset, n, dtype=np.int64)
    csz = max(1, int(chunk))
    for s in range(0, q_idx.size, csz):
        idx = q_idx[s : s + csz]
        arch_i = idx - offset - W
        arch = np.ascontiguousarray(windows[arch_i])
        yy = np.ascontiguousarray(y_win[arch_i])
        q = emb[idx][:, None, :]
        sim = (arch * q).sum(axis=-1)
        kk = min(K, W)
        part = np.argpartition(sim, W - kk, axis=1)[:, -kk:]
        row = np.arange(idx.size)[:, None]
        top_sim = sim[row, part]
        top_y = yy[row, part]
        w = np.exp(top_sim - top_sim.max(axis=1, keepdims=True))
        w_sum = np.maximum(w.sum(axis=1, keepdims=True), 1e-8)
        pred[idx] = (w * np.where(np.isfinite(top_y), top_y, 0.0)).sum(axis=1) / w_sum.ravel()
        finite = np.isfinite(top_y).sum(axis=1)
        pred[idx] = np.where(finite > 0, pred[idx], np.nan)
    return pred


def kref_predict(
    close: np.ndarray,
    *,
    lookback: int = DEFAULT_LOOKBACK,
    archive: int = DEFAULT_ARCHIVE,
    neighbors: int = DEFAULT_NEIGHBORS,
    horizon: int = 8,
    purge: int = DEFAULT_PURGE,
) -> np.ndarray:
    emb = lookback_embeddings(close, lookback=lookback)
    fwd = forward_return(close, horizon)
    return retrieve_forecast(
        emb,
        fwd,
        archive=archive,
        neighbors=neighbors,
        horizon=horizon,
        purge=purge,
    )
