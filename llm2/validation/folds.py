"""Frozen outer OOS calendar folds (UTC)."""



from __future__ import annotations



from dataclasses import dataclass

from typing import Sequence



import numpy as np

import pandas as pd



from llm2.paths import FORWARD_LOCKBOX_START

from llm2.validation.walk_forward import FoldSpec, make_time_splits



# V1 — used by all hunts/settles before D-033. Kept for provenance / replay.

OUTER_FOLD_RANGES_V1: list[tuple[str, str]] = [

    ("2022-01-01", "2022-10-01"),

    ("2022-10-01", "2023-07-01"),

    ("2023-07-01", "2024-04-01"),

    ("2024-04-01", "2025-01-01"),

    ("2025-01-01", "2025-10-01"),

]



# V2 — preregistered in configs/preregister/structure_v1_fold_extension_001.yaml (D-033).

# Closes the Oct-2025 → lockbox gap. End of last fold == FORWARD_LOCKBOX_START (exclusive).

OUTER_FOLD_RANGES_V2: list[tuple[str, str]] = [

    *OUTER_FOLD_RANGES_V1,

    ("2025-10-01", FORWARD_LOCKBOX_START),

]



# Canonical default for new research after D-033.

OUTER_FOLD_RANGES: list[tuple[str, str]] = list(OUTER_FOLD_RANGES_V2)

FOLD_GEOMETRY_VERSION = "v2"





@dataclass(frozen=True)

class OuterFoldSpec:

    fold_index: int

    oos_start_ms: int

    oos_end_ms: int

    train_indices: np.ndarray

    oos_indices: np.ndarray

    purge_bars: int

    embargo_bars: int





def _to_ms(date_str: str) -> int:

    return int(pd.Timestamp(date_str, tz="UTC").value // 1_000_000)





def index_to_ms(index: pd.Index) -> np.ndarray:

    """UTC epoch milliseconds — safe across pandas 2/3 datetime storage."""

    idx = pd.DatetimeIndex(pd.to_datetime(index))

    if idx.tz is not None:

        idx = idx.tz_convert("UTC")

    else:

        idx = idx.tz_localize("UTC")

    return (idx.to_numpy(dtype="datetime64[ns]").astype(np.int64) // 1_000_000).astype(np.int64)





def build_outer_folds(

    ts_ms: np.ndarray,

    purge_bars: int = 24,

    embargo_bars: int = 24,

    *,

    ranges: Sequence[tuple[str, str]] | None = None,

) -> list[OuterFoldSpec]:

    fold_ranges = list(ranges) if ranges is not None else list(OUTER_FOLD_RANGES)

    folds: list[OuterFoldSpec] = []

    for i, (start_str, end_str) in enumerate(fold_ranges):

        oos_start = _to_ms(start_str)

        oos_end = _to_ms(end_str)

        oos_mask = (ts_ms >= oos_start) & (ts_ms < oos_end)

        oos_indices = np.flatnonzero(oos_mask)

        if oos_indices.size == 0:

            continue

        first_oos_pos = int(oos_indices[0])

        train_end = max(0, first_oos_pos - purge_bars - embargo_bars)

        train_indices = np.arange(0, train_end, dtype=np.int64)

        if train_indices.size < 500:

            continue

        folds.append(

            OuterFoldSpec(

                fold_index=i,

                oos_start_ms=oos_start,

                oos_end_ms=oos_end,

                train_indices=train_indices,

                oos_indices=oos_indices,

                purge_bars=purge_bars,

                embargo_bars=embargo_bars,

            )

        )

    return folds





def make_inner_folds(

    train_indices: np.ndarray,

    n_folds: int = 3,

    purge_bars: int = 24,

    embargo_bars: int = 24,

) -> list[FoldSpec]:

    n_train = len(train_indices)

    return make_time_splits(

        n_train,

        n_folds=n_folds,

        train_min=max(400, n_train // 6),

        val_size=max(150, n_train // 12),

        purge_bars=purge_bars,

        embargo_bars=embargo_bars,

    )


