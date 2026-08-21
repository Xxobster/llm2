"""LIVE-DATA-001 tip freshness (llm2 surface over botsgeneral live_candles)."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any


def _ensure_live_candles() -> None:
    try:
        import live_candles  # noqa: F401
        return
    except ImportError:
        pass
    pkg = Path(r"C:\projects\botsgeneral\packages\live_candles\src")
    if pkg.is_dir() and str(pkg) not in sys.path:
        sys.path.insert(0, str(pkg))


_ensure_live_candles()

from live_candles.freshness import (  # noqa: E402
    LIVE_DATA_001,
    TipFreshnessResult,
    check_series_live_data_001,
    clear_data_unsafe,
    evaluate_tip_freshness,
    expected_closed_open_ms,
    fetch_binance_server_time_ms,
    fetch_server_time_ms,
    gate_allows_new_entries,
    is_data_unsafe,
    read_data_unsafe,
    write_data_unsafe,
)

SIGNAL_EXCHANGE = "binance"

__all__ = [
    "LIVE_DATA_001",
    "SIGNAL_EXCHANGE",
    "TipFreshnessResult",
    "expected_closed_open_ms",
    "evaluate_tip_freshness",
    "fetch_binance_server_time_ms",
    "fetch_server_time_ms",
    "check_series_live_data_001",
    "gate_allows_new_entries",
    "write_data_unsafe",
    "clear_data_unsafe",
    "read_data_unsafe",
    "is_data_unsafe",
    "signal_entry_gate",
]


def signal_entry_gate(
    *,
    symbol: str,
    timeframe: str,
    local_tip_ms: int | None,
    db_path: str | Path | None = None,
    persist_flag: bool = True,
) -> tuple[bool, TipFreshnessResult, dict[str, Any] | None]:
    """Pivot/micro signal gate: Binance tip vs Binance server time."""
    return gate_allows_new_entries(
        exchange=SIGNAL_EXCHANGE,
        symbol=symbol,
        timeframe=timeframe,
        local_tip_ms=local_tip_ms,
        db_path=db_path,
        persist_flag=persist_flag,
    )
