"""Causality tests for diagonal support/resistance geometry."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagonal_sr.events import build_event_pack, build_features_for_guard
from llm2.diagonal_sr.geometry import (
    build_geometry_frame,
    last2_line,
    ols_line,
    swings_from_ohlcv,
)


def _index(n: int, freq: str = "1h") -> pd.DatetimeIndex:
    return pd.date_range("2020-01-01", periods=n, freq=freq, tz="UTC")


def _synthetic_ohlcv(n: int = 400) -> pd.DataFrame:
    """Descending zigzag so swings exist and last2 lines are defined."""
    idx = _index(n)
    t = np.arange(n, dtype=float)
    # Lower highs / lower lows channel.
    base = 100.0 - 0.05 * t
    wave = 3.0 * np.sin(t / 8.0)
    close = base + wave
    high = close + 0.8 + 0.2 * np.abs(np.cos(t / 8.0))
    low = close - 0.8 - 0.2 * np.abs(np.sin(t / 8.0))
    open_ = close.copy()
    vol = 1000.0 + 50.0 * np.sin(t / 11.0)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": vol},
        index=idx,
    )


def test_last2_line_only_uses_swings_confirmed_at_or_before_decision_bar():
    idx = _index(200)
    swings = pd.DataFrame(
        {
            "pivot_i": [10, 50],
            "confirm_ts_ms": [int(idx[14].value // 1_000_000), int(idx[54].value // 1_000_000)],
            "price": [100.0, 110.0],
        }
    )
    pos = np.arange(len(idx))
    line, slope = last2_line(swings, idx, pos)
    assert line.iloc[:54].isna().all()
    assert line.iloc[54:].notna().all()
    expected_at_100 = 100.0 + 0.25 * (100 - 10)
    assert abs(float(line.iloc[100]) - expected_at_100) < 1e-9
    assert abs(float(slope.iloc[100]) - 0.25) < 1e-9


def test_future_swing_cannot_move_earlier_line_value():
    ohlcv = _synthetic_ohlcv(500)
    full = build_geometry_frame(ohlcv)
    trunc = build_geometry_frame(ohlcv.iloc[:300].copy())
    # Prefix of full must match truncated build on overlapping bars for last2 lines.
    for col in ("last2_upper", "last2_lower", "ols3_upper", "channel_upper"):
        a = full[col].iloc[:300].to_numpy(dtype=float)
        b = trunc[col].to_numpy(dtype=float)
        both = np.isfinite(a) & np.isfinite(b)
        if both.sum() == 0:
            continue
        assert np.allclose(a[both], b[both], rtol=0, atol=1e-9), col


def test_ols3_nan_until_three_confirmed_swings():
    idx = _index(100)
    swings = pd.DataFrame(
        {
            "pivot_i": [10, 30],
            "confirm_ts_ms": [int(idx[12].value // 1_000_000), int(idx[32].value // 1_000_000)],
            "price": [100.0, 95.0],
        }
    )
    line, _ = ols_line(swings, idx, np.arange(len(idx)), n_points=3)
    assert line.isna().all()


def test_prefix_invariance_features_guard():
    ohlcv = _synthetic_ohlcv(600)
    full = build_features_for_guard(ohlcv)
    trunc = build_features_for_guard(ohlcv.iloc[:400].copy())
    common = [c for c in trunc.columns if c in full.columns]
    a = full.iloc[:400][common].to_numpy(dtype=float)
    b = trunc[common].to_numpy(dtype=float)
    both = np.isfinite(a) & np.isfinite(b)
    assert both.sum() > 100
    assert np.allclose(a[both], b[both], rtol=0, atol=1e-8)


def test_labels_nan_on_last_horizon_rows():
    ohlcv = _synthetic_ohlcv(300)
    pack = build_event_pack(ohlcv, horizon=4, generation="A")
    assert pack.labels.iloc[-4:].isna().all().all()
    assert pack.labels.iloc[:-4].notna().any().any()


def test_swings_from_ohlcv_produces_high_and_low():
    ohlcv = _synthetic_ohlcv(400)
    sw = swings_from_ohlcv(ohlcv)
    assert not sw.empty
    assert set(sw["kind"].unique()) <= {"high", "low"}
    # confirm after pivot
    assert (sw["confirm_i"] >= sw["pivot_i"] + 2).all()


def test_generation_b_adds_confluence_columns():
    ohlcv = _synthetic_ohlcv(400)
    pack = build_event_pack(ohlcv, horizon=4, generation="B")
    for eid in (
        "confluence_bounce_long",
        "confluence_bounce_short",
        "confluence_break_up",
        "confluence_break_down",
    ):
        assert eid in pack.labels.columns
    assert "confluence_upper" in pack.features.columns
