"""Probability of Backtest Overfitting via CSCV."""

from __future__ import annotations

from itertools import combinations

import numpy as np
import pandas as pd
from scipy import stats


def pbo_cscv(matrix: pd.DataFrame, n_blocks: int = 16) -> dict[str, float]:
    m = matrix.dropna(how="all", axis=1).fillna(0.0)
    t, n = m.shape
    if n < 2 or t < n_blocks:
        return {"pbo": float("nan"), "n_splits": 0, "n_strategies": float(n)}
    n_blocks -= n_blocks % 2
    blocks = np.array_split(np.arange(t), n_blocks)
    vals = m.to_numpy(float)
    logits: list[float] = []
    ranks: list[float] = []

    for is_idx in combinations(range(n_blocks), n_blocks // 2):
        is_rows = np.concatenate([blocks[b] for b in is_idx])
        oos_rows = np.concatenate([blocks[b] for b in range(n_blocks) if b not in is_idx])

        def score(rows: np.ndarray) -> np.ndarray:
            sub = vals[rows]
            sd = sub.std(axis=0, ddof=1)
            return np.where(sd > 0, sub.mean(axis=0) / np.where(sd > 0, sd, 1.0), 0.0)

        best = int(np.argmax(score(is_rows)))
        oos = score(oos_rows)
        rank = float(stats.rankdata(oos)[best]) / (n + 1)
        ranks.append(rank)
        rank = min(max(rank, 1e-6), 1 - 1e-6)
        logits.append(float(np.log(rank / (1 - rank))))

    logits_arr = np.array(logits)
    return {
        "pbo": float((logits_arr <= 0).mean()),
        "n_splits": float(len(logits)),
        "n_strategies": float(n),
        "median_oos_rank": float(np.median(ranks)),
    }
