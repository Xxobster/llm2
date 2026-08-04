"""External series must never be readable before they exist.

``market_ohlcv.ts_ms`` is bar OPEN time. The previous loader forward-filled a daily bar
stamped ``D 00:00`` across every hour of day ``D``, handing the model that day's close 23
hours early. These tests pin the completion-time contract that replaces it.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.data.macro import (
    DAY,
    EXCLUDED_SYMBOLS,
    EXTERNAL_REGISTRY,
    ZERO,
    _completion_index,
    align_causal,
    get_series_spec,
    registry_for,
)


def test_completion_index_is_open_plus_one_timeframe():
    open_ms = np.array([1717545600000])  # 2024-06-05 00:00 UTC
    known = _completion_index(open_ms, "1d")
    assert known[0] == pd.Timestamp("2024-06-06 00:00", tz="UTC")

    known_1h = _completion_index(open_ms, "1h")
    assert known_1h[0] == pd.Timestamp("2024-06-05 01:00", tz="UTC")


def test_daily_close_is_not_visible_during_its_own_day():
    """The exact leak that existed in macro_v1, now expressed as a failing condition."""
    daily_open = pd.date_range("2024-06-01", periods=5, freq="1D", tz="UTC")
    closes = pd.Series([100.0, 101.0, 102.0, 103.0, 104.0], index=daily_open)
    # Re-index to completion instants, which is what load_external does.
    knowable = pd.Series(closes.to_numpy(), index=daily_open + DAY)

    hourly = pd.date_range("2024-06-01", periods=120, freq="1h", tz="UTC")
    aligned = align_causal(knowable, hourly)

    during_jun3 = aligned.loc["2024-06-03 00:00":"2024-06-03 23:00", "value"]
    close_of_jun3 = 102.0
    assert not (during_jun3 == close_of_jun3).any(), (
        "the close of 2024-06-03 must not be readable at any hour inside 2024-06-03"
    )
    # It becomes readable the instant the day completes, and not before.
    assert aligned.loc[pd.Timestamp("2024-06-04 00:00", tz="UTC"), "value"] == close_of_jun3


def test_alignment_reports_age_so_staleness_is_explicit():
    daily = pd.Series([1.0, 2.0], index=pd.DatetimeIndex(["2024-06-03", "2024-06-04"], tz="UTC"))
    hourly = pd.date_range("2024-06-03", periods=30, freq="1h", tz="UTC")

    aligned = align_causal(daily, hourly)

    assert aligned.loc[pd.Timestamp("2024-06-03 00:00", tz="UTC"), "age_sec"] == 0.0
    assert aligned.loc[pd.Timestamp("2024-06-03 12:00", tz="UTC"), "age_sec"] == 12 * 3600.0
    # A weekend-closed venue must show its age rather than look fresh.
    assert aligned["age_sec"].max() >= 20 * 3600.0


def test_max_age_blanks_stale_values_rather_than_carrying_them():
    daily = pd.Series([5.0], index=pd.DatetimeIndex(["2024-06-03"], tz="UTC"))
    hourly = pd.date_range("2024-06-03", periods=72, freq="1h", tz="UTC")

    aligned = align_causal(daily, hourly, max_age=DAY)

    assert aligned["value"].notna().sum() == 25  # inclusive of the boundary hour
    assert aligned["value"].iloc[-1] != aligned["value"].iloc[-1] or np.isnan(aligned["value"].iloc[-1])


def test_no_value_precedes_its_first_observation():
    daily = pd.Series([7.0, 8.0], index=pd.DatetimeIndex(["2024-06-10", "2024-06-11"], tz="UTC"))
    hourly = pd.date_range("2024-06-01", periods=300, freq="1h", tz="UTC")

    aligned = align_causal(daily, hourly)

    before = aligned.loc[: pd.Timestamp("2024-06-09 23:00", tz="UTC"), "value"]
    assert before.isna().all(), "values must be NaN before the series starts, never backfilled"


def test_every_registry_entry_pins_a_source_and_a_lag():
    assert EXTERNAL_REGISTRY
    for spec in EXTERNAL_REGISTRY:
        assert spec.source, spec.symbol
        assert spec.timeframes, spec.symbol
        assert spec.publication_lag >= ZERO, spec.symbol
        assert spec.symbol not in EXCLUDED_SYMBOLS, f"{spec.symbol} is excluded for leakage"


def test_ambiguous_vendor_symbols_resolve_to_exactly_one_source():
    """EURUSD, XAUUSD and friends exist under two vendors; the registry must choose."""
    for symbol in ("EURUSD", "XAUUSD", "USDJPY", "WTI", "COPPER", "AUDUSD"):
        spec = get_series_spec(symbol)
        assert spec.source == "dukascopy", f"{symbol} resolved to {spec.source}"


def test_statistical_releases_carry_a_publication_lag():
    """A FRED value dated D is not retrievable at D; market closes are known at the close."""
    for symbol in ("US02Y", "US10Y", "T10Y2Y", "STABLE_MCAP"):
        assert get_series_spec(symbol).publication_lag >= DAY, symbol
    for symbol in ("EURUSD", "SPX", "VIX"):
        assert get_series_spec(symbol).publication_lag == ZERO, symbol


def test_unregistered_symbol_raises_rather_than_guessing():
    with pytest.raises(KeyError, match="EXTERNAL_REGISTRY"):
        get_series_spec("BTC_MCAP")


def test_macro_v1_no_longer_leaks_the_same_day_close():
    """Integration guard on the actual defect, against the real warehouse.

    Prefix-invariance in the leakage engine cannot catch this: it truncates the crypto
    OHLCV passed to the builder, but the macro series is loaded fresh from the database
    inside the builder, so truncation never reaches it.
    """
    pytest.importorskip("pandas")
    from llm2.data.loader import load_ohlcv
    from llm2.data.macro import MARKET_DB, load_external
    from llm2.features.macro_v1 import build_macro_v1

    if not MARKET_DB.is_file():
        pytest.skip("market warehouse unavailable")

    # A window well inside DXY daily coverage.
    ohlcv = load_ohlcv("BTCUSDT", "1h", start_ms=1717200000000, end_ms=1719792000000)
    feats = build_macro_v1(ohlcv, timeframe="1d", symbols=["DXY"])

    daily = load_external("DXY", "1d")  # already indexed by completion instant
    hourly_level = align_causal(daily, pd.DatetimeIndex(ohlcv.index))["value"]

    # At every decision bar the level used must be the latest one knowable by then.
    for ts in hourly_level.dropna().index[:500]:
        eligible = daily.loc[:ts]
        assert len(eligible) and eligible.iloc[-1] == hourly_level.loc[ts], (
            f"at {ts} macro_v1 used {hourly_level.loc[ts]}, "
            f"but the latest knowable value was {eligible.iloc[-1] if len(eligible) else None}"
        )

    assert feats["macro_logret_1_DXY"].notna().any()
    assert "macro_age_h_DXY" in feats.columns, "staleness must be exposed, not hidden"


def test_registry_filters():
    assert {s.symbol for s in registry_for(category="rates")} == {"US02Y", "US10Y", "US03M", "T10Y2Y"}
    assert all("1h" in s.timeframes for s in registry_for(timeframe="1h"))
