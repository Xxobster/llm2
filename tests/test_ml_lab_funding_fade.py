"""Causal funding alignment must ignore later settlements and the open-bar print."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.funding_fade import (
    align_funding_to_bars,
    attach_causal_funding,
    funding_event_mask,
    funding_signal,
)


def test_settlement_at_bar_open_is_not_used_on_that_bar():
    opens = np.array([0, 3_600_000, 7_200_000], dtype=np.int64)
    fts = np.array([3_600_000], dtype=np.int64)  # settlement = second bar open
    fr = np.array([0.001], dtype=np.float64)
    rate, new = align_funding_to_bars(opens, fts, fr)
    assert not np.isfinite(rate[0])
    assert not np.isfinite(rate[1])  # open equals print → excluded
    assert rate[2] == 0.001
    assert bool(new[2])
    assert not bool(new[1])


def test_new_flag_fires_once_per_print():
    opens = np.arange(0, 8, dtype=np.int64) * 3_600_000
    fts = np.array([0, 8 * 3_600_000], dtype=np.int64)  # 0 is before first open? 0 < 0 is false
    # print at t=1ms before first open would apply to bar 0; use print at -1
    fts = np.array([-1, 4 * 3_600_000], dtype=np.int64)
    fr = np.array([0.0004, -0.0006], dtype=np.float64)
    rate, new = align_funding_to_bars(opens, fts, fr)
    assert float(rate[0]) == 0.0004
    assert bool(new[0])
    # bars 1..4 still the first print; bar 5 (open 5h) first sees print at 4h
    assert int(new.sum()) == 2
    assert bool(new[5])
    assert float(rate[5]) == -0.0006


def test_prefix_invariance():
    idx = pd.date_range("2020-01-01", periods=200, freq="1h", tz="UTC")
    close = 100.0 + np.linspace(0, 1, 200)
    ohlcv = pd.DataFrame(
        {"open": close, "high": close + 0.1, "low": close - 0.1, "close": close, "volume": 1.0},
        index=idx,
    )
    fidx = pd.date_range("2020-01-01", periods=25, freq="8h", tz="UTC")
    funding = pd.Series(np.linspace(0.0001, 0.0008, 25), index=fidx)
    full = attach_causal_funding(ohlcv, funding)
    prefix = attach_causal_funding(ohlcv.iloc[:-40], funding)
    for col in ("funding_rate", "funding_new"):
        a = full[col].to_numpy()[:-40]
        b = prefix[col].to_numpy()
        m = np.isfinite(a) & np.isfinite(b)
        np.testing.assert_allclose(a[m], b[m], rtol=1e-12, atol=1e-12)


def test_fade_shorts_positive_funding():
    rate = np.array([np.nan, 0.001, -0.001])
    new = np.array([False, True, True])
    mask = funding_event_mask(rate, new, abs_tau=0.0003)
    fade = funding_signal(rate, mask, fade=True)
    ride = funding_signal(rate, mask, fade=False)
    assert fade[1] == -1.0
    assert fade[2] == 1.0
    assert ride[1] == 1.0
    assert ride[2] == -1.0
    assert fade[0] == 0.0
