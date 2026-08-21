"""Adverse-path cancel unit tests."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.pivot.strategy.adverse_cancel import first_touch_or_adverse
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits
from llm2.validation.folds import index_to_ms
from tradesim import Side


def test_adverse_cancels_short_before_touch():
    # decision close=100; short limit=101; price drops to 99 first -> adverse
    idx = pd.date_range("2024-01-01", periods=6, freq="15min", tz="UTC")
    close = np.array([100.0, 99.5, 99.0, 101.5, 101.5, 101.5])
    high = np.array([100.2, 99.6, 99.2, 101.6, 101.6, 101.6])
    low = np.array([99.8, 99.0, 98.5, 101.0, 101.0, 101.0])
    ohlcv = pd.DataFrame(
        {"open": close, "high": high, "low": low, "close": close, "volume": 1.0},
        index=idx,
    )
    ts0 = int(index_to_ms(ohlcv.index)[0])
    intents = [
        LimitIntent(
            decision_ts_ms=ts0,
            side=Side.SHORT,
            limit_price=101.0,
            stop_offset=0.01,
            target_offset=0.01,
            max_hold_bars=6,
            work_bars=4,
        )
    ]
    sigs, st = materialize_working_limits(
        ohlcv, intents, work_bars=4, adverse_mode="pct", adverse_pct=0.005
    )
    assert st["n_adverse_cancel"] == 1
    assert len(sigs) == 0


def test_touch_wins_if_before_adverse():
    high = np.array([100.0, 101.2, 99.0])
    low = np.array([99.5, 100.0, 98.0])
    close = np.array([100.0, 100.5, 98.5])
    i, reason = first_touch_or_adverse(
        side_is_short=True,
        lim=101.0,
        i0=1,
        i1=3,
        high=high,
        low=low,
        close=close,
        decision_close=100.0,
        adverse_frac=0.005,
    )
    assert reason == "touch"
    assert i == 1
