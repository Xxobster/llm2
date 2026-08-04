"""Tests for the boundary-break study: confirmation causality, coil fencing, placebo, donchian."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagnostics.structurebreak import (
    BOUNDARY_LEVEL_CLAIM,
    CoilLookaheadError,
    channel_line,
    coil_filter,
    detect_breaks,
    donchian_boundaries,
    placebo_boundaries,
)
from llm2.research_policy import require_placebo_arm


def _index(n: int) -> pd.DatetimeIndex:
    return pd.date_range("2020-01-01", periods=n, freq="1h", tz="UTC")


def _ohlcv_from_close(close: np.ndarray) -> pd.DataFrame:
    idx = _index(close.size)
    return pd.DataFrame(
        {"open": close, "high": close * 1.002, "low": close * 0.998, "close": close, "volume": 1.0},
        index=idx,
    )


# --------------------------------------------------------------------------------------
# Channel line never cites an unconfirmed swing
# --------------------------------------------------------------------------------------


def test_channel_line_only_uses_swings_confirmed_at_or_before_the_decision_bar():
    idx = _index(200)
    # Two confirmed swings: pivot at bar 10 (confirmed at bar 14), pivot at bar 50
    # (confirmed at bar 54). Price = 100 at pivot_i=10, 110 at pivot_i=50 -> slope = 0.25/bar.
    swings = pd.DataFrame(
        {
            "pivot_i": [10, 50],
            "pivot_ts_ms": [int(idx[10].value // 1_000_000), int(idx[50].value // 1_000_000)],
            "confirm_ts_ms": [int(idx[14].value // 1_000_000), int(idx[54].value // 1_000_000)],
            "price": [100.0, 110.0],
        }
    )
    pos = np.arange(len(idx))
    line = channel_line(swings, idx, pos)

    # Before the second swing is confirmed (bar 54), the channel cannot use it at all: the
    # line must be flat/undefined (NaN, since only one confirmed swing exists yet).
    assert line.iloc[:54].isna().all(), "channel used a swing before its confirmation bar"

    # From bar 54 onward the line is defined and equals the projected two-point line.
    assert line.iloc[54:].notna().all()
    expected_at_100 = 100.0 + 0.25 * (100 - 10)
    assert abs(line.iloc[100] - expected_at_100) < 1e-9


def test_channel_line_with_no_swings_is_all_nan():
    idx = _index(50)
    empty = pd.DataFrame(columns=["pivot_i", "pivot_ts_ms", "confirm_ts_ms", "price"])
    line = channel_line(empty, idx, np.arange(len(idx)))
    assert line.isna().all()


# --------------------------------------------------------------------------------------
# Coil filter: strictly before the break
# --------------------------------------------------------------------------------------


def test_coil_filter_rejects_zero_or_negative_lookback():
    amp_rank = pd.Series(np.linspace(0, 100, 200))
    with pytest.raises(CoilLookaheadError):
        coil_filter(amp_rank, np.array([50, 60]), lookback_bars=0)
    with pytest.raises(CoilLookaheadError):
        coil_filter(amp_rank, np.array([50, 60]), lookback_bars=-1)


def test_coil_filter_reads_the_bar_before_the_break_not_the_break_bar():
    n = 200
    amp_rank = pd.Series(np.full(n, 90.0))  # everywhere high...
    amp_rank.iloc[49] = 5.0  # ...except exactly one bar before the break at 50
    mask = coil_filter(amp_rank, np.array([50]), lookback_bars=1, tercile=100 / 3)
    assert mask[0], "coil filter did not see the low amplitude one bar before the break"

    amp_rank2 = pd.Series(np.full(n, 90.0))
    amp_rank2.iloc[50] = 5.0  # low AT the break bar itself, not before it
    mask2 = coil_filter(amp_rank2, np.array([50]), lookback_bars=1, tercile=100 / 3)
    assert not mask2[0], "coil filter used the break bar's own amplitude"


# --------------------------------------------------------------------------------------
# Placebo arm is mandatory and produces boundaries inside the range
# --------------------------------------------------------------------------------------


def test_boundary_level_claim_has_a_valid_placebo_arm():
    require_placebo_arm(BOUNDARY_LEVEL_CLAIM)  # must not raise


def test_placebo_boundaries_sit_strictly_inside_the_trailing_range():
    rng = np.random.default_rng(0)
    close = 100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=500)))
    ohlcv = _ohlcv_from_close(close)

    placebo = placebo_boundaries(ohlcv, window=50)
    donchian = donchian_boundaries(ohlcv, windows=(50,))

    joined = placebo.join(donchian).dropna()
    assert len(joined) > 50
    assert (joined["placebo_upper"] <= joined["donchian50_upper"]).all()
    assert (joined["placebo_lower"] >= joined["donchian50_lower"]).all()
    assert (joined["placebo_upper"] > joined["placebo_lower"]).all()


# --------------------------------------------------------------------------------------
# Donchian boundary excludes the current bar's own extreme (no self-referential break)
# --------------------------------------------------------------------------------------


def test_donchian_boundary_is_shifted_and_cannot_be_broken_by_its_own_bar():
    n = 300
    high = np.full(n, 100.0)
    low = np.full(n, 99.0)
    # A single spike bar: if the boundary were not shifted, this bar's own high would BE
    # the boundary and could never register as a break of it.
    high[150] = 150.0
    ohlcv = pd.DataFrame(
        {"open": low, "high": high, "low": low, "close": low, "volume": 1.0}, index=_index(n)
    )
    donchian = donchian_boundaries(ohlcv, windows=(20,))
    assert donchian["donchian20_upper"].iloc[150] == 100.0, "the boundary saw its own bar's high"
    assert donchian["donchian20_upper"].iloc[151] == 150.0, "the spike never entered the boundary"


# --------------------------------------------------------------------------------------
# Break detection: donchian and swing go through the same confirmation machinery
# --------------------------------------------------------------------------------------


def test_detect_breaks_reports_the_same_confirmation_kinds_for_any_boundary_pair():
    n = 1000
    rng = np.random.default_rng(1)
    close = pd.Series(100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=n))), index=_index(n))
    ohlcv = pd.DataFrame(
        {"open": close, "high": close * 1.01, "low": close * 0.99, "close": close, "volume": 1.0},
        index=close.index,
    )
    atr = (ohlcv["high"] - ohlcv["low"]).rolling(14, min_periods=7).mean()

    donchian = donchian_boundaries(ohlcv, windows=(20,))
    events = detect_breaks(ohlcv, donchian["donchian20_upper"], donchian["donchian20_lower"], atr=atr)

    expected_keys = {
        "close_beyond_up",
        "close_beyond_down",
        "close_beyond_atr_up",
        "close_beyond_atr_down",
        "retest_up",
        "retest_down",
    }
    assert set(events.keys()) == expected_keys
    for key, series in events.items():
        assert series.dtype == bool
        assert len(series) == n


def test_close_beyond_atr_is_stricter_than_plain_close_beyond():
    n = 1000
    rng = np.random.default_rng(2)
    close = pd.Series(100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=n))), index=_index(n))
    ohlcv = pd.DataFrame(
        {"open": close, "high": close * 1.01, "low": close * 0.99, "close": close, "volume": 1.0},
        index=close.index,
    )
    atr = (ohlcv["high"] - ohlcv["low"]).rolling(14, min_periods=7).mean()
    donchian = donchian_boundaries(ohlcv, windows=(20,))
    events = detect_breaks(ohlcv, donchian["donchian20_upper"], donchian["donchian20_lower"], atr=atr)

    assert events["close_beyond_atr_up"].sum() <= events["close_beyond_up"].sum()
    assert events["close_beyond_atr_down"].sum() <= events["close_beyond_down"].sum()
