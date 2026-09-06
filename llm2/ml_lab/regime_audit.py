"""Train-only latent-regime audit (paper 3 Aug 2026), NumPy K-means not TS2Vec.

Fit cluster centres on a prefix. Assign later bars by nearest centre.
Never used as a selection input in the same run that views the labels.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view


def _causal_roll_std(x: np.ndarray, win: int) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    n = x.size
    out = np.full(n, np.nan, dtype=np.float64)
    w = int(win)
    if n < w:
        return out
    windows = sliding_window_view(np.nan_to_num(x, nan=0.0), w)
    out[w - 1 :] = windows.std(axis=1)
    return out


def regime_features(ohlcv: pd.DataFrame, *, vol_win: int = 96) -> np.ndarray:
    c = ohlcv["close"].to_numpy(dtype=np.float64)
    h = ohlcv["high"].to_numpy(dtype=np.float64)
    l = ohlcv["low"].to_numpy(dtype=np.float64)
    r = np.full(c.size, np.nan)
    r[1:] = np.diff(c) / np.where(c[:-1] > 0, c[:-1], np.nan)
    vol = _causal_roll_std(r, vol_win)
    rng = (h - l) / np.where(c > 0, c, np.nan)
    return np.column_stack([vol, np.abs(r), rng])


def _kmeans_fit_predict(
    train: np.ndarray,
    all_rows: np.ndarray,
    *,
    k: int,
    seed: int,
    n_iter: int = 25,
) -> np.ndarray:
    rng = np.random.default_rng(int(seed))
    n_k = int(k)
    pick = rng.choice(train.shape[0], size=n_k, replace=False)
    cents = train[pick].copy()
    labels = np.zeros(train.shape[0], dtype=np.int32)
    for _ in range(int(n_iter)):
        d = ((train[:, None, :] - cents[None, :, :]) ** 2).sum(axis=2)
        labels = d.argmin(axis=1).astype(np.int32)
        for j in range(n_k):
            m = labels == j
            if int(m.sum()) > 0:
                cents[j] = train[m].mean(axis=0)
    d_all = ((all_rows[:, None, :] - cents[None, :, :]) ** 2).sum(axis=2)
    return d_all.argmin(axis=1).astype(np.int32)


def fit_assign_regimes(
    feat: np.ndarray,
    *,
    train_end: int,
    k: int = 3,
    seed: int = 20260828,
) -> np.ndarray:
    """K-means centres from ``feat[:train_end]`` only; labels for all rows."""
    x = np.asarray(feat, dtype=np.float64)
    labels = np.full(x.shape[0], -1, dtype=np.int32)
    train = x[: int(train_end)]
    mask = np.isfinite(train).all(axis=1)
    if int(mask.sum()) < max(30, int(k) * 10):
        return labels
    ok = np.isfinite(x).all(axis=1)
    pred = np.full(int(ok.sum()), -1, dtype=np.int32)
    pred[:] = _kmeans_fit_predict(train[mask], x[ok], k=int(k), seed=int(seed))
    labels[ok] = pred
    return labels


def regime_skill_table(
    labels: np.ndarray,
    signal: np.ndarray,
    next_ret: np.ndarray,
    *,
    eval_start: int,
) -> list[dict[str, Any]]:
    """Directional accuracy and signed next-return by regime on the eval suffix."""
    lab = np.asarray(labels)
    sig = np.asarray(signal, dtype=float)
    nxt = np.asarray(next_ret, dtype=float)
    i0 = int(eval_start)
    idx = np.arange(lab.size)
    rows: list[dict[str, Any]] = []
    groups = np.unique(lab[i0:])
    for g in groups.tolist():
        if int(g) < 0:
            continue
        m = (lab == g) & (idx >= i0) & (sig != 0) & np.isfinite(nxt)
        n = int(m.sum())
        if n < 20:
            rows.append({"regime": int(g), "n": n, "directional_acc": float("nan")})
            continue
        da = float(np.mean(np.sign(sig[m]) == np.sign(nxt[m])))
        pnl = float(np.mean(sig[m] * nxt[m]))
        rows.append(
            {
                "regime": int(g),
                "n": n,
                "directional_acc": da,
                "mean_signed_next_return": pnl,
            }
        )
    return rows
