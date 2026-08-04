"""Live structure path defaults to Binance (research parity); Bybit is execution-only."""

from __future__ import annotations

from llm2.data import indicators as ind
from llm2.live.micro_runner import resolve_signal_source


def test_structure_source_env_override(monkeypatch):
    monkeypatch.setenv("LLM2_STRUCTURE_SOURCE", "bybit")
    assert ind._default_source("BTCUSDT") == "bybit"


def test_structure_source_default_without_env(monkeypatch):
    monkeypatch.delenv("LLM2_STRUCTURE_SOURCE", raising=False)
    assert ind._default_source("BTCUSDT") == "binance"


def test_resolve_signal_source_defaults_binance(monkeypatch):
    monkeypatch.delenv("LLM2_STRUCTURE_SOURCE", raising=False)
    assert resolve_signal_source({}) == "binance"
    assert resolve_signal_source({"signal_source": "binance"}) == "binance"


def test_resolve_signal_source_env(monkeypatch):
    monkeypatch.setenv("LLM2_STRUCTURE_SOURCE", "binance")
    assert resolve_signal_source({"signal_source": "bybit"}) == "binance"


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
    assert len(out) == 3
    assert int(out["ts_ms"].iloc[-1]) == int(idx[-2].value // 1_000_000)
