"""Causality bindings for the Fibonacci market-structure warehouse.

Swing structure is the highest-risk indicator family for look-ahead: a pivot only becomes a
pivot once ``swing_right`` further bars have printed, so a warehouse that stamps it at the
pivot bar leaks that many bars at every swing. Prefix-invariance cannot catch it, because
truncating the bar frame does not truncate the database — the stored values come back
unchanged and the test passes trivially. These tests therefore interrogate the stored
confirmation instants directly, which is where the real evidence lives.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.data.indicators import (
    INDICATORS_DB,
    PRICE_COLUMNS,
    RETRACE_CLIP,
    SWING_RIGHT,
    align_multi_timeframe,
    load_bar_features,
    structure_frame,
    timeframe_ms,
)
from llm2.paths import TF_MS

warehouse = pytest.mark.skipif(
    not INDICATORS_DB.is_file(), reason=f"indicator warehouse absent: {INDICATORS_DB}"
)

CASES = [("BTCUSDT", "1h"), ("BTCUSDT", "4h"), ("ETHUSDT", "1h"), ("XRPUSDT", "1h"), ("VETUSDT", "1h"), ("BNBUSDT", "1h")]


def _swings(symbol: str, timeframe: str, source: str = "binance") -> pd.DataFrame:
    import sqlite3

    conn = sqlite3.connect(f"file:{INDICATORS_DB}?mode=ro", uri=True)
    try:
        return pd.read_sql(
            "SELECT kind, pivot_i, confirm_i, pivot_ts_ms, confirm_ts_ms, price FROM swings "
            "WHERE symbol=? AND timeframe=? AND source=? ORDER BY swing_id",
            conn,
            params=(symbol, timeframe, source),
        )
    finally:
        conn.close()


# --------------------------------------------------------------------------------------
# The stored structure itself
# --------------------------------------------------------------------------------------


@warehouse
@pytest.mark.parametrize("symbol,timeframe", CASES)
def test_confirmation_lags_the_pivot_by_swing_right(symbol, timeframe):
    """A pivot is only knowable ``swing_right`` bars after it prints."""
    sw = _swings(symbol, timeframe)
    assert len(sw) > 100
    assert (sw["confirm_i"] - sw["pivot_i"] == SWING_RIGHT).all()
    step = timeframe_ms(timeframe)
    assert (sw["confirm_ts_ms"] - sw["pivot_ts_ms"] == SWING_RIGHT * step).all()


@warehouse
@pytest.mark.parametrize("symbol,timeframe", CASES)
@pytest.mark.parametrize("kind,ts_col", [("high", "last_sh_ts_ms"), ("low", "last_sl_ts_ms")])
def test_no_bar_cites_an_unconfirmed_swing(symbol, timeframe, kind, ts_col):
    """The decisive test: the swing a bar refers to was already confirmed at that bar.

    If the builder had stamped pivots at ``pivot_ts_ms`` instead of ``confirm_ts_ms``, every
    bar in the two-bar window after a swing would be quoting a level that had not yet come
    into existence, and any model would learn to trade the resulting free peek.
    """
    sw = _swings(symbol, timeframe)
    confirm_of_pivot = sw[sw.kind == kind].set_index("pivot_ts_ms")["confirm_ts_ms"]

    bf = load_bar_features(symbol, timeframe)
    cited = bf.dropna(subset=[ts_col])
    assert len(cited) > 100

    confirm = cited[ts_col].astype("int64").map(confirm_of_pivot)
    assert confirm.notna().all(), "a cited swing timestamp is not a known pivot"
    unconfirmed = int((confirm > cited["ts_ms"]).sum())
    assert unconfirmed == 0, f"{unconfirmed} bars cite a {kind} confirmed in their future"


@warehouse
@pytest.mark.parametrize("symbol,timeframe", CASES)
def test_support_and_resistance_bracket_the_close(symbol, timeframe):
    """Support below, resistance above. A crossed pair means a future extreme leaked in."""
    bf = load_bar_features(symbol, timeframe)
    s = bf.dropna(subset=["nearest_support", "close"])
    r = bf.dropna(subset=["nearest_resistance", "close"])
    assert (s["nearest_support"] <= s["close"]).all()
    assert (r["nearest_resistance"] >= r["close"]).all()


@warehouse
def test_fibonacci_anchors_are_confirmed_swing_prices():
    """The grid must be spanned by real swings, not by a future high or low."""
    bf = load_bar_features("BTCUSDT", "1h").dropna(subset=["fib_0000", "fib_1000"])
    prices = set(np.round(_swings("BTCUSDT", "1h")["price"].to_numpy(), 10))
    for col in ("fib_0000", "fib_1000"):
        assert np.isin(np.round(bf[col].to_numpy(), 10), list(prices)).all()
    # Internal consistency: the 0.5 line is the midpoint of the anchors by construction.
    mid = 0.5 * (bf["fib_0000"] + bf["fib_1000"])
    assert np.allclose(bf["fib_0500"], mid, atol=1e-9)


# --------------------------------------------------------------------------------------
# The feature layer
# --------------------------------------------------------------------------------------


@warehouse
def test_structure_frame_exposes_no_raw_price_level():
    """A price level encodes the calendar on a series that ran from $8k to six figures."""
    frame = structure_frame("BTCUSDT", "1h")
    leaked = sorted(set(frame.columns) & set(PRICE_COLUMNS))
    assert leaked == [], f"raw price levels reached the feature frame: {leaked}"
    assert not any(c.startswith("fib_0") or c.startswith("fib_1") for c in frame.columns
                   if c != "fib_position")


@warehouse
def test_retracement_outliers_are_clipped():
    """Raw retracement reaches 963 on BTCUSDT 1h; unclipped it would dominate any fit."""
    frame = structure_frame("BTCUSDT", "1h")
    v = frame["last_retrace_pct"].dropna()
    assert v.min() >= RETRACE_CLIP[0]
    assert v.max() <= RETRACE_CLIP[1]


@warehouse
@pytest.mark.parametrize("symbol", ["BTCUSDT", "ETHUSDT", "XAUUSD", "DXY"])
def test_label_derived_direction_is_balanced_where_structure_bias_is_not(symbol):
    """``structure_bias`` is unusable as a trend state; the Dow reading of the label is not.

    The warehouse column sits at +1 on 93.7% of BTCUSDT 1h bars and 99.2% of XAUUSD's, so a
    joint confluence table built on it puts nearly every observation into one cell and
    cannot answer the question that was asked of it. ``struct_dir`` splits near evenly.
    """
    frame = structure_frame(symbol, "1h")
    raw = load_bar_features(symbol, "1h")

    bias_share = raw["structure_bias"].value_counts(normalize=True).max()
    dir_share = frame["struct_dir"].value_counts(normalize=True).max()

    assert bias_share > 0.85, "structure_bias became usable; revisit the confluence state"
    assert dir_share < 0.60, f"struct_dir is unbalanced for {symbol}: {dir_share:.3f}"
    assert set(frame["struct_dir"].dropna().unique()) <= {-1.0, 1.0}


@warehouse
def test_bars_since_a_swing_is_never_negative():
    frame = structure_frame("BTCUSDT", "1h")
    for col in ("bars_since_sh", "bars_since_sl"):
        assert (frame[col].dropna() >= 0).all()


# --------------------------------------------------------------------------------------
# Cross-timeframe alignment
# --------------------------------------------------------------------------------------


def test_every_warehouse_timeframe_has_a_known_bar_length():
    """Regression: ``1w`` was missing from TF_MS.

    ``align_multi_timeframe`` shifts a higher-timeframe row to its completion instant. With
    a silent one-hour fallback a weekly bar was declared complete one hour after it opened,
    exposing six days and twenty-three hours of the future in every weekly context column
    while the leakage audit still reported PASS. Guessing is now a hard error.
    """
    for tf in ("15m", "1h", "4h", "1d", "1w"):
        assert timeframe_ms(tf) == TF_MS[tf]
    assert timeframe_ms("1w") == 7 * 86_400_000
    with pytest.raises(KeyError):
        timeframe_ms("3w")


def test_higher_timeframe_value_is_invisible_until_its_bar_closes():
    """A 4-hour reading must not reach the 1-hour bars inside its own bar."""
    higher = pd.DataFrame(
        {"v": [1.0, 2.0, 3.0]},
        index=pd.to_datetime(["2024-01-01 00:00", "2024-01-01 04:00", "2024-01-01 08:00"], utc=True),
    )
    target = pd.date_range("2024-01-01 00:00", "2024-01-01 11:00", freq="1h", tz="UTC")
    out = align_multi_timeframe(higher, target, "4h")["v"]

    # The bar opening at 00:00 closes at 04:00, so 00:00-03:00 know nothing at all.
    assert out.loc["2024-01-01 00:00":"2024-01-01 03:00"].isna().all()
    # From 04:00 the first bar's value is available, and only that one.
    assert (out.loc["2024-01-01 04:00":"2024-01-01 07:00"] == 1.0).all()
    assert (out.loc["2024-01-01 08:00":"2024-01-01 11:00"] == 2.0).all()


def test_weekly_alignment_holds_a_value_for_a_full_week():
    """The specific case the missing TF_MS entry broke."""
    higher = pd.DataFrame(
        {"v": [10.0, 20.0]}, index=pd.to_datetime(["2024-01-01", "2024-01-08"], utc=True)
    )
    target = pd.date_range("2024-01-01", "2024-01-20", freq="1h", tz="UTC")
    out = align_multi_timeframe(higher, target, "1w")["v"]

    assert out.loc["2024-01-01":"2024-01-07 23:00"].isna().all()
    assert (out.loc["2024-01-08":"2024-01-14 23:00"] == 10.0).all()
    assert (out.loc["2024-01-15":"2024-01-20"] == 20.0).all()


@warehouse
def test_weekly_context_on_the_hourly_index_never_moves_mid_week():
    """End-to-end: real weekly structure must be a step function on the hourly index."""
    from llm2.data.loader import load_ohlcv
    from llm2.features.structure_v1 import build_structure_v1

    ohlcv = load_ohlcv("BTCUSDT", "1h").tail(20_000)
    feats = build_structure_v1(ohlcv, symbol="BTCUSDT", timeframe="1h")
    col = feats["fib_position_1w"].dropna()
    assert len(col) > 1000

    changed = col.index[col.diff().abs() > 0]
    # Every change must land on a weekly boundary; a mid-week change means the value was
    # revealed before its bar completed.
    offsets = {(t - pd.Timestamp("1970-01-01", tz="UTC")) % pd.Timedelta("7D") for t in changed}
    assert len(offsets) == 1, f"weekly context changes at {len(offsets)} distinct week offsets"
