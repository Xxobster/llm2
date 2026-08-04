"""Purge and embargo index masks."""

from __future__ import annotations

import numpy as np


def apply_purge_embargo(
    train_indices: np.ndarray,
    test_indices: np.ndarray,
    *,
    purge_bars: int,
    embargo_bars: int,
) -> tuple[np.ndarray, np.ndarray]:
    if train_indices.size == 0 or test_indices.size == 0:
        return train_indices, test_indices
    first_test = int(test_indices[0])
    last_train_allowed = max(0, first_test - purge_bars - embargo_bars)
    trimmed = train_indices[train_indices < last_train_allowed]
    return trimmed, test_indices
