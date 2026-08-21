"""Unit tests for llm2 LIVE-DATA-001 surface (no network)."""

from __future__ import annotations

from llm2.live.candle_freshness import (
    LIVE_DATA_001,
    evaluate_tip_freshness,
    expected_closed_open_ms,
)


def test_live_data_001_constant():
    assert LIVE_DATA_001 == "LIVE-DATA-001"


def test_expected_and_codes_match_shared():
    server = 1_704_067_620_000
    expected = expected_closed_open_ms("15m", server_now_ms=server)
    missing = evaluate_tip_freshness(
        exchange="binance",
        symbol="BTCUSDT",
        timeframe="15m",
        local_tip_ms=None,
        server_now_ms=server,
        local_wall_ms=server,
        fetch_server_time=False,
    )
    assert missing.code == "CANDLE_MISSING"
    stale = evaluate_tip_freshness(
        exchange="binance",
        symbol="BTCUSDT",
        timeframe="15m",
        local_tip_ms=expected - 900_000,
        server_now_ms=server,
        local_wall_ms=server,
        fetch_server_time=False,
    )
    assert stale.code == "CANDLE_STALE"
    ahead = evaluate_tip_freshness(
        exchange="binance",
        symbol="BTCUSDT",
        timeframe="15m",
        local_tip_ms=expected + 900_000,
        server_now_ms=server,
        local_wall_ms=server,
        fetch_server_time=False,
    )
    assert ahead.code == "CANDLE_AHEAD"
    skew = evaluate_tip_freshness(
        exchange="binance",
        symbol="BTCUSDT",
        timeframe="15m",
        local_tip_ms=expected,
        server_now_ms=server,
        local_wall_ms=server + 20_000,
        clock_skew_max_ms=5_000,
        fetch_server_time=False,
    )
    assert skew.code == "CLOCK_SKEW"
