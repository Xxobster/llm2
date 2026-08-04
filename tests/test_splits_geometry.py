"""Fold geometry tests."""

from __future__ import annotations

import pandas as pd

from llm2.paths import FORWARD_LOCKBOX_START
from llm2.validation.folds import (
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    OUTER_FOLD_RANGES_V1,
    OUTER_FOLD_RANGES_V2,
    build_outer_folds,
    index_to_ms,
)


def test_frozen_outer_fold_count_v2_covers_gap_to_lockbox():
    ts = pd.date_range("2021-01-01", "2026-04-30", freq="1h", tz="UTC")
    ts_ms = index_to_ms(ts)
    folds = build_outer_folds(ts_ms, purge_bars=24, embargo_bars=24)
    assert FOLD_GEOMETRY_VERSION == "v2"
    assert len(OUTER_FOLD_RANGES) == 6
    assert OUTER_FOLD_RANGES == OUTER_FOLD_RANGES_V2
    assert len(OUTER_FOLD_RANGES_V1) == 5
    assert len(folds) == 6
    assert OUTER_FOLD_RANGES[-1][1] == FORWARD_LOCKBOX_START
    # Last fold must include Oct 2025 (the former gap).
    last = folds[-1]
    assert last.oos_start_ms == int(pd.Timestamp("2025-10-01", tz="UTC").value // 1_000_000)


def test_train_precedes_oos_with_purge():
    ts = pd.date_range("2021-01-01", "2026-04-30", freq="1h", tz="UTC")
    ts_ms = index_to_ms(ts)
    folds = build_outer_folds(ts_ms, purge_bars=24, embargo_bars=24)
    for fold in folds:
        assert fold.train_indices.max() < fold.oos_indices.min()


def test_v1_ranges_still_build_five_folds():
    ts = pd.date_range("2021-01-01", "2026-04-30", freq="1h", tz="UTC")
    folds = build_outer_folds(
        index_to_ms(ts), purge_bars=24, embargo_bars=24, ranges=OUTER_FOLD_RANGES_V1
    )
    assert len(folds) == 5
