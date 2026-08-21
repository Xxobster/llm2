"""Forecast filters may only skip — never invent side."""

from __future__ import annotations

import numpy as np

from llm2.experiments.forecast_filter_on_direction import (
    asof_sparse_to_bars,
    retrace_agree_mask,
    vol_skip_mask,
)


def test_retrace_agree_keeps_only_matching_side():
    side = np.array([1, 1, -1, -1, 0], dtype=int)
    # leg_dir=+1, pred=0.2 → score=+0.3 → wants long
    # leg_dir=+1, pred=0.8 → score=-0.3 → wants short
    pred = np.array([0.2, 0.8, 0.2, 0.8, 0.2], dtype=float)
    leg = np.array([1, 1, 1, 1, 1], dtype=float)
    keep = retrace_agree_mask(side=side, pred_retrace=pred, leg_dir=leg)
    assert keep.tolist() == [True, False, False, True, False]


def test_vol_skip_mask():
    pred = np.array([0.1, 0.5, np.nan, 0.3], dtype=float)
    keep = vol_skip_mask(pred, threshold=0.4)
    assert keep.tolist() == [True, False, False, True]


def test_asof_sparse_causal():
    bars = np.array([10, 20, 30, 40], dtype=np.int64)
    dec = np.array([15, 35], dtype=np.int64)
    vals = np.array([1.0, 2.0], dtype=float)
    out = asof_sparse_to_bars(bars, dec, vals)
    assert np.isnan(out[0])
    assert out[1] == 1.0
    assert out[2] == 1.0
    assert out[3] == 2.0
