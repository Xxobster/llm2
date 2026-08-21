"""Unit tests for pivot timing gates."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.pivot.strategy.timing_gates import (
    funding_near_mask,
    medium_atr_mask,
    time_bucket_work_bars,
    vsa_absorption_ok,
)


def test_medium_atr_mask_keeps_middle():
    a = np.linspace(0.001, 0.01, 200)
    m = medium_atr_mask(a, lo_q=0.25, hi_q=0.75)
    assert m.sum() < len(a)
    assert m.sum() > 50


def test_time_bucket_cancel_late():
    wb = time_bucket_work_bars(np.array([1.0, 5.0, np.nan]), horizon=4, default_work=4)
    assert wb[0] >= 1
    assert wb[1] == 0
    assert wb[2] == 4


def test_funding_near_mask():
    # 2024-01-01 00:10 UTC near funding
    ts = np.array([int(pd.Timestamp("2024-01-01 00:10:00", tz="UTC").value // 1_000_000)])
    m = funding_near_mask(ts, avoid_minutes=30)
    assert not bool(m[0])


def test_vsa_absorption_shape():
    idx = pd.date_range("2024-01-01", periods=60, freq="15min", tz="UTC")
    close = np.full(60, 100.0)
    high = close + 1.0
    low = close - 1.0
    # last bar: wide + high vol + close near low (rejection for short)
    high[-1] = 103.0
    low[-1] = 99.0
    close[-1] = 99.2
    vol = np.full(60, 10.0)
    vol[-1] = 40.0
    ohlcv = pd.DataFrame(
        {"open": close, "high": high, "low": low, "close": close, "volume": vol},
        index=idx,
    )
    ts = np.array([int(idx[-1].value // 1_000_000)])
    ok_short = vsa_absorption_ok(ohlcv, ts, np.array([True]))
    assert bool(ok_short[0])
