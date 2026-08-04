"""Causality tests for label builders."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.labels.direction import build_direction_labels
from llm2.labels.first_touch import FirstTouchConfig, build_first_touch_labels
from llm2.labels.fwd_return import build_fwd_return_labels
from llm2.labels.volatility import build_volatility_labels


def _synthetic_ohlcv(n: int = 200) -> pd.DataFrame:
    idx = pd.date_range("2022-01-01", periods=n, freq="1h", tz="UTC")
    rng = np.random.default_rng(0)
    close = 100 + np.cumsum(rng.normal(0, 0.5, n))
    high = close + rng.uniform(0.1, 1.0, n)
    low = close - rng.uniform(0.1, 1.0, n)
    open_ = close + rng.normal(0, 0.2, n)
    vol = rng.uniform(100, 1000, n)
    return pd.DataFrame({"open": open_, "high": high, "low": low, "close": close, "volume": vol}, index=idx)


def test_fwd_return_uses_future_only_in_label():
    ohlcv = _synthetic_ohlcv()
    labels = build_fwd_return_labels(ohlcv, horizon=3)
    manual = np.log(ohlcv["close"].shift(-3) / ohlcv["close"])
    pd.testing.assert_series_equal(labels["fwd_return"], manual, check_names=False)


def test_direction_sign_matches_fwd_return():
    ohlcv = _synthetic_ohlcv()
    d = build_direction_labels(ohlcv, horizon=2)
    f = build_fwd_return_labels(ohlcv, horizon=2)["fwd_return"]
    expected = np.sign(f).astype(float)
    expected[f.abs() < 1e-12] = 0.0
    np.testing.assert_array_equal(d["direction"].values, expected.values)


def test_first_touch_prefix_invariance_on_past_decision_bars():
    ohlcv = _synthetic_ohlcv(120)
    touch = ohlcv.copy()
    cfg = FirstTouchConfig(decision_timeframe="1h", touch_timeframe="1h", horizon_hours=12, barrier_pct=0.02)
    full = build_first_touch_labels(ohlcv, touch, cfg)
    cut = 80
    partial = build_first_touch_labels(ohlcv.iloc[:cut], touch.iloc[: cut + 24], cfg)
    pd.testing.assert_frame_equal(full.iloc[: cut - 1], partial.iloc[: cut - 1])


def test_volatility_label_finite_tail():
    ohlcv = _synthetic_ohlcv(100)
    vol = build_volatility_labels(ohlcv, horizon=5)
    assert vol["volatility"].iloc[:-5].notna().any()
