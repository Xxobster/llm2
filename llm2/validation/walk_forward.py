"""Walk-forward fold utilities."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class FoldSpec:
    train_end: int
    val_start: int
    val_end: int
    purge_bars: int
    embargo_bars: int


def make_time_splits(
    n: int,
    *,
    n_folds: int = 3,
    train_min: int = 400,
    val_size: int = 150,
    purge_bars: int = 24,
    embargo_bars: int = 24,
) -> list[FoldSpec]:
    folds: list[FoldSpec] = []
    if n < train_min + val_size + purge_bars + embargo_bars:
        return folds
    step = max(val_size, (n - train_min) // (n_folds + 1))
    for i in range(n_folds):
        val_end = n - i * step
        val_start = max(train_min + purge_bars + embargo_bars, val_end - val_size)
        train_end = max(0, val_start - purge_bars - embargo_bars)
        if train_end < train_min or val_start >= val_end:
            continue
        folds.append(
            FoldSpec(
                train_end=train_end,
                val_start=val_start,
                val_end=val_end,
                purge_bars=purge_bars,
                embargo_bars=embargo_bars,
            )
        )
    return folds
