"""Live structure path must read the Bybit-refreshed source, not stale Binance rows."""

from __future__ import annotations

import os

from llm2.data import indicators as ind


def test_structure_source_env_override(monkeypatch):
    monkeypatch.setenv("LLM2_STRUCTURE_SOURCE", "bybit")
    assert ind._default_source("BTCUSDT") == "bybit"


def test_structure_source_default_without_env(monkeypatch):
    monkeypatch.delenv("LLM2_STRUCTURE_SOURCE", raising=False)
    # Crypto perps fall through to binance research warehouse when no override.
    assert ind._default_source("BTCUSDT") == "binance"


def test_drop_forming_bar_keeps_closed_only():
    import pandas as pd

    from llm2.live.refresh_structure import _drop_forming_bar

    now = pd.Timestamp.now(tz="UTC").floor("h")
    idx = pd.date_range(now - pd.Timedelta(hours=3), periods=4, freq="h", tz="UTC")
    df = pd.DataFrame(
        {
            "ts_ms": [int(ts.value // 1_000_000) for ts in idx],
            "open": 1.0,
            "high": 1.0,
            "low": 1.0,
            "close": 1.0,
            "volume": 1.0,
        },
        index=idx,
    )
    out = _drop_forming_bar(df, "1h")
    # Current hour is still forming → dropped.
    assert len(out) == 3
    assert int(out["ts_ms"].iloc[-1]) == int(idx[-2].value // 1_000_000)
