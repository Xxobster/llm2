"""Causal hunt-008 US-inventory signals must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_e import (
    IDEA_IDS_E,
    NY_LUNCH_HOUR,
    US_CLOSE_HOUR,
    signals_e,
    utc_calendar,
    weekend_range_break,
)


def _ohlcv(n: int = 900, seed: int = 17, freq: str = "1h") -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    op = np.empty_like(close)
    op[0] = close[0]
    op[1:] = close[:-1]
    idx = pd.date_range("2019-01-01", periods=n, freq=freq, tz="UTC")
    return pd.DataFrame(
        {
            "open": op,
            "high": close * 1.004,
            "low": close * 0.996,
            "close": close,
            "volume": rng.random(n) * 100 + 1,
        },
        index=idx,
    )


def test_eight_ideas():
    assert len(IDEA_IDS_E) == 8


def test_2019_01_01_is_tuesday():
    df = _ohlcv(24)
    _day, _hour, weekday, _wm = utc_calendar(df)
    assert int(weekday[0]) == 1


def test_us_open_only_hour_13_on_1h():
    df = _ohlcv(400)
    sig = signals_e(df, "1h")["us_open_drive"]
    _day, hour, _wd, _wm = utc_calendar(df)
    fired = np.flatnonzero(sig != 0)
    assert fired.size > 0
    assert np.all(hour[fired] == 13)


def test_weekend_break_only_monday():
    df = _ohlcv(2000)
    sig = weekend_range_break(df, "1h")
    _day, _hour, weekday, _wm = utc_calendar(df)
    fired = np.flatnonzero(sig != 0)
    if fired.size:
        assert np.all(weekday[fired] == 0)


def test_4h_lunch_is_zero_when_same_as_close():
    assert NY_LUNCH_HOUR["4h"] == US_CLOSE_HOUR["4h"]
    df = _ohlcv(400, freq="4h")
    assert np.all(signals_e(df, "4h")["ny_lunch_fade"] == 0.0)


def test_prefix_all_ideas_1h():
    df = _ohlcv(1500)
    full = signals_e(df, "1h")
    prefix = signals_e(df.iloc[:-80], "1h")
    for name in IDEA_IDS_E:
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)
