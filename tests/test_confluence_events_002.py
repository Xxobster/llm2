"""Generation-002 consolidation events stay causal and fire on a channel."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.confluence.events import (
    EVENT_IDS,
    EVENT_IDS_002,
    build_event_pack,
    build_known_now_features,
)


def _channel(n: int = 400, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    close = 100.0 + 0.4 * np.sin(np.arange(n) / 6.0) + rng.normal(0, 0.02, size=n)
    high = close + 0.08
    low = close - 0.08
    idx = pd.date_range("2023-01-01", periods=n, freq="15min", tz="UTC")
    return pd.DataFrame(
        {
            "open": close,
            "high": high,
            "low": low,
            "close": close,
            "volume": rng.uniform(10, 20, size=n),
        },
        index=idx,
    )


def _breakout(n: int = 400) -> pd.DataFrame:
    close = np.full(n, 100.0)
    close[280:] = 100.0 + np.linspace(0.0, 8.0, n - 280)
    high = close + 0.1
    low = close - 0.1
    idx = pd.date_range("2023-01-01", periods=n, freq="15min", tz="UTC")
    return pd.DataFrame(
        {"open": close, "high": high, "low": low, "close": close, "volume": 10.0},
        index=idx,
    )


def test_001_columns_unchanged_without_flag():
    pack = build_event_pack(_channel(300), horizon=4, include_002=False)
    assert list(pack.labels.columns) == list(EVENT_IDS)


def test_002_columns_present_with_flag():
    pack = build_event_pack(_channel(300), horizon=4, include_002=True)
    assert list(pack.labels.columns) == list(EVENT_IDS + EVENT_IDS_002)
    assert pack.labels.iloc[-4:].isna().all().all()


def test_range_hold_fires_in_channel():
    pack = build_event_pack(_channel(), horizon=8, include_002=True)
    n = int(np.nansum(pack.labels["range_hold"].to_numpy()))
    assert n >= 20


def test_range_break_up_fires_after_breakout():
    pack = build_event_pack(_breakout(), horizon=8, include_002=True)
    n = int(np.nansum(pack.labels["range_break_up"].to_numpy()))
    assert n >= 1


def test_new_features_prefix_invariant():
    df = _channel(500)
    full = build_known_now_features(df)
    trunc = build_known_now_features(df.iloc[:350])
    for c in ("range20_width", "close_pos_in_range20", "atr_pos_100", "ret4"):
        a = full[c].iloc[:350].to_numpy(dtype=float)
        b = trunc[c].to_numpy(dtype=float)
        both = np.isfinite(a) & np.isfinite(b)
        assert both.sum() >= 20
        np.testing.assert_allclose(a[both], b[both], rtol=1e-9, atol=1e-9, err_msg=c)
