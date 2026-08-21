"""Tests for additive pivot label + schema modules."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.pivot.data.resampler import refuse_illegal_resample, resample_ohlcv_from_base
from llm2.pivot.labels.config import PivotLabelConfig, default_configs
from llm2.pivot.labels.fractal import (
    first_pivot_target_at_decisions,
    label_fractal_pivots,
    wilder_atr,
)
from llm2.pivot.schema import ensure_pivot_db


def _synthetic_ohlcv(n: int = 200, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    # Random walk with planted peaks/troughs
    close = 100 + np.cumsum(rng.normal(0, 0.2, size=n))
    high = close + rng.uniform(0.1, 0.5, size=n)
    low = close - rng.uniform(0.1, 0.5, size=n)
    # Plant a clear high around bar 80 and low around 120
    high[80] = close[80] + 5.0
    for k in range(1, 4):
        high[80 - k] = high[80] - 1.0 * k
        high[80 + k] = high[80] - 1.2 * k
        low[80 + k] = close[80] - 2.0 - 0.3 * k
    low[120] = close[120] - 5.0
    for k in range(1, 4):
        low[120 - k] = low[120] + 1.0 * k
        low[120 + k] = low[120] + 1.2 * k
        high[120 + k] = close[120] + 2.0 + 0.3 * k
    open_ = close.copy()
    ts = pd.date_range("2024-01-01", periods=n, freq="5min", tz="UTC")
    df = pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": 1.0},
        index=ts,
    )
    df["ts_ms"] = (df.index.asi8 // 1_000_000).astype(np.int64)
    return df


def test_schema_creates_db(tmp_path):
    path = tmp_path / "pivot.sqlite"
    out = ensure_pivot_db(path)
    assert out.is_file()
    # idempotent
    ensure_pivot_db(path)


def test_config_version_stable():
    a = default_configs()["5m"]
    b = PivotLabelConfig(
        timeframe="5m",
        left_bars=3,
        right_bars=3,
        confirm_bars=3,
        min_left_prominence_atr=0.5,
        min_right_reversal_atr=0.5,
        min_reversal_pct=0.001,
    )
    assert a.version == b.version


def test_wilder_atr_positive():
    df = _synthetic_ohlcv()
    atr = wilder_atr(
        df["high"].to_numpy(),
        df["low"].to_numpy(),
        df["close"].to_numpy(),
        period=14,
    )
    assert np.isfinite(atr[50:]).all()
    assert (atr[50:] > 0).all()


def test_label_fractal_confirm_after_origin():
    df = _synthetic_ohlcv(300)
    cfg = PivotLabelConfig(
        timeframe="5m",
        left_bars=3,
        right_bars=3,
        confirm_bars=3,
        min_left_prominence_atr=0.1,
        min_right_reversal_atr=0.1,
        min_reversal_pct=0.0001,
        suppress_neighbor_bars=2,
    )
    ev = label_fractal_pivots(df, cfg)
    assert len(ev) > 0
    assert (ev["confirmed_at_ts_ms"] >= ev["pivot_origin_ts_ms"]).all()
    assert set(ev["pivot_side"]).issubset({"high", "low"})


def test_first_pivot_target_window():
    # Manual event at t=1000, decision at 500, H=600 → inside; H=400 → none
    events = pd.DataFrame(
        {
            "pivot_origin_ts_ms": [1000, 2000],
            "pivot_side": ["high", "low"],
        }
    )
    dec = np.array([500, 1500, 2500], dtype=np.int64)
    lab = first_pivot_target_at_decisions(dec, events, horizon_ms=600)
    assert lab.loc[0, "side"] == "high"
    assert lab.loc[1, "side"] == "low"
    assert lab.loc[2, "side"] == "none"
    lab2 = first_pivot_target_at_decisions(dec, events, horizon_ms=400)
    assert lab2.loc[0, "side"] == "none"


def test_refuse_manufacture_5m_from_1h():
    with pytest.raises(ValueError, match="Illegal|upsample|Cannot"):
        refuse_illegal_resample("1h", "5m")
    with pytest.raises(ValueError):
        refuse_illegal_resample("15m", "5m")


def test_resample_1m_to_5m_complete_only():
    # Explicit open timestamps: 12 consecutive 1-minute bars from a 5m boundary.
    base = 1_704_067_200_000  # 2024-01-01 00:00:00 UTC ms
    ts_ms = base + np.arange(12, dtype=np.int64) * 60_000
    close = np.arange(12, dtype=float) + 100
    df = pd.DataFrame(
        {
            "open": close,
            "high": close + 0.1,
            "low": close - 0.1,
            "close": close,
            "volume": 1.0,
            "ts_ms": ts_ms,
        },
        index=pd.to_datetime(ts_ms, unit="ms", utc=True),
    )
    out = resample_ohlcv_from_base(df, source_tf="1m", target_tf="5m")
    assert len(out) == 2
    assert int(out["n_base"].min()) >= 5
    # Incomplete third bucket (only 2 bars) dropped
    assert (out["ts_ms"].to_numpy() % 300_000 == 0).all()
