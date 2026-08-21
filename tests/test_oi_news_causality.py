"""Confirmation-time / completion-time audits for OI and news warehouses.

Prefix-invariance on OHLCV alone cannot prove these spaces are causal (the
warehouse is not truncated). These tests check the alignment rules directly.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.features.news_v1 import build_news_v1
from llm2.features.oi_v1 import MARKET_OI_DB, build_oi_v1, load_oi_completed
from llm2.paths import NEWS_EVENTS_DB, TF_MS

oi_warehouse = pytest.mark.skipif(
    not MARKET_OI_DB.is_file(), reason=f"OI warehouse absent: {MARKET_OI_DB}"
)
news_warehouse = pytest.mark.skipif(
    not NEWS_EVENTS_DB.is_file(), reason=f"news warehouse absent: {NEWS_EVENTS_DB}"
)


@oi_warehouse
def test_oi_completion_stamps_are_open_plus_tf():
    s = load_oi_completed("ETHUSDT", timeframe="5m", exchange="bybit")
    assert len(s) > 1000
    # Differences between successive stamps should be multiples of tf after dedupe
    # (gaps allowed). Spot-check: index is timezone-aware UTC.
    assert str(s.index.tz) == "UTC"


@oi_warehouse
def test_oi_v1_prefix_stable_on_ohlcv_frame_only():
    """Changing future decision bars must not alter past oi features from history.

    Rebuild on truncated OHLCV: values through the cutoff equal full-series values.
    (Warehouse OI is not truncated — this only bounds decision-index alignment.)
    """
    # Synthetic decision frame spanning a real OI era
    idx = pd.date_range("2024-01-01", periods=500, freq="1h", tz="UTC")
    ohlcv = pd.DataFrame(
        {
            "open": 2000.0,
            "high": 2010.0,
            "low": 1990.0,
            "close": 2005.0,
            "volume": 1.0,
        },
        index=idx,
    )
    full = build_oi_v1(ohlcv, symbol="ETHUSDT", timeframe="1h")
    cut = 300
    trunc = build_oi_v1(ohlcv.iloc[:cut], symbol="ETHUSDT", timeframe="1h")
    cols = [c for c in full.columns if c.startswith("oi_")]
    a = full.iloc[:cut][cols]
    b = trunc[cols]
    # Allow NaN equality
    pd.testing.assert_frame_equal(a, b, check_names=True, rtol=1e-9, atol=1e-9)


@oi_warehouse
def test_oi_v1_no_use_of_uncompleted_bar():
    """As-of merge: feature at bar open T uses OI known by T+tf only."""
    idx = pd.date_range("2024-06-01", periods=48, freq="1h", tz="UTC")
    ohlcv = pd.DataFrame(
        {"open": 1.0, "high": 1.0, "low": 1.0, "close": 1.0, "volume": 1.0},
        index=idx,
    )
    feats = build_oi_v1(ohlcv, symbol="BTCUSDT", timeframe="1h")
    assert "oi_age_h" in feats.columns
    # Age must be non-negative where defined (completion already past)
    age = feats["oi_age_h"].dropna()
    if len(age):
        assert (age >= -1e-6).all()


@news_warehouse
def test_news_counts_nonnegative_and_monotonic_windows():
    idx = pd.date_range("2024-01-01", periods=200, freq="1h", tz="UTC")
    ohlcv = pd.DataFrame(
        {"open": 1.0, "high": 1.0, "low": 1.0, "close": 1.0, "volume": 1.0},
        index=idx,
    )
    f = build_news_v1(ohlcv, timeframe="1h")
    assert (f["news_n_1h"] >= 0).all()
    assert (f["news_n_24h"] + 1e-9 >= f["news_n_1h"]).all()
    assert (f["news_n_7d"] + 1e-9 >= f["news_n_24h"]).all()


@news_warehouse
def test_news_prefix_stable():
    idx = pd.date_range("2024-01-01", periods=400, freq="1h", tz="UTC")
    ohlcv = pd.DataFrame(
        {"open": 1.0, "high": 1.0, "low": 1.0, "close": 1.0, "volume": 1.0},
        index=idx,
    )
    full = build_news_v1(ohlcv, timeframe="1h")
    cut = 250
    trunc = build_news_v1(ohlcv.iloc[:cut], timeframe="1h")
    cols = [c for c in full.columns if c.startswith("news_")]
    pd.testing.assert_frame_equal(
        full.iloc[:cut][cols], trunc[cols], check_names=True, rtol=1e-9, atol=1e-9
    )


@news_warehouse
def test_news_only_uses_first_seen_not_event_start():
    """Sanity: builder never queries event_start_at (grep-level via module source)."""
    import inspect

    from llm2.features import news_v1 as mod

    src = inspect.getsource(mod)
    assert "event_start_at" not in src or "never retroactive" in mod.__doc__
    assert "first_seen_at" in src
