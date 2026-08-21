"""Multi-head label fields + ECE helper."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.pivot.labels.config import PivotLabelConfig
from llm2.pivot.labels.fractal import first_pivot_target_at_decisions, label_fractal_pivots
from llm2.pivot.train.multihead import expected_calibration_error
from llm2.pivot.train.samples import _attach_event_fields


def test_ece_perfect_and_bad():
    # Base rate 0.8 → constant 0.5 is miscalibrated; near-corrects are better.
    y = np.array([1, 1, 1, 1, 0] * 20, dtype=float)
    p_good = np.where(y > 0.5, 0.85, 0.15)
    p_bad = np.full(len(y), 0.5)
    assert expected_calibration_error(y, p_good) < expected_calibration_error(y, p_bad)


def test_attach_time_and_level():
    # 40 bars, plant one high pivot origin at bar 20
    n = 40
    close = np.linspace(100, 110, n)
    high = close + 0.5
    low = close - 0.5
    high[20] = 120.0
    for k in range(1, 4):
        high[20 - k] = 120 - k
        high[20 + k] = 115 - k
        low[20 + k] = 100
    df = pd.DataFrame(
        {
            "open": close,
            "high": high,
            "low": low,
            "close": close,
            "volume": 1.0,
            "ts_ms": np.arange(n, dtype=np.int64) * 60_000,
        }
    )
    cfg = PivotLabelConfig(
        timeframe="5m",
        left_bars=3,
        right_bars=3,
        confirm_bars=3,
        min_left_prominence_atr=0.05,
        min_right_reversal_atr=0.05,
        min_reversal_pct=0.0001,
    )
    ev = label_fractal_pivots(df, cfg)
    assert len(ev) >= 1
    ts = df["ts_ms"].to_numpy()
    ydf = first_pivot_target_at_decisions(ts, ev, horizon_ms=10 * 60_000)
    ydf = _attach_event_fields(
        ydf, ev, decision_ts_ms=ts, decision_close=close, tf_ms=60_000
    )
    hit = ydf["side"].to_numpy() != "none"
    assert hit.any()
    assert np.isfinite(ydf.loc[hit, "time_to_event_bars"]).all()
