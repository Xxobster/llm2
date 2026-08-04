"""Wrap tradesim candle refresh."""

from __future__ import annotations

from typing import Sequence

from llm2.paths import BINANCE_PERPS, PRIMARY_SYMBOLS


def ensure_candles(
    symbols: Sequence[str] | None = None,
    timeframes: Sequence[str] | None = None,
    *,
    price_types: Sequence[str] = ("last", "mark"),
    incremental: bool = True,
    quiet: bool = False,
) -> int:
    """Refresh candles in shared warehouse. Returns download exit code."""
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()
    from tradesim.research.candles import ensure_candles as _ensure

    syms = list(symbols) if symbols is not None else list(BINANCE_PERPS)
    tfs = list(timeframes) if timeframes is not None else ["1m", "5m", "15m", "1h", "4h"]
    return int(
        _ensure(
            symbols=syms,
            timeframes=tfs,
            price_types=price_types,
            incremental=incremental,
            quiet=quiet,
        )
    )


def refresh_primary(*, include_1m_all: bool = False) -> int:
    """Refresh primary symbols quickly; optionally start 1m for all perps."""
    code = ensure_candles(
        PRIMARY_SYMBOLS,
        ["5m", "15m", "1h", "4h", "1m"],
        price_types=("last", "mark"),
        quiet=False,
    )
    if include_1m_all:
        code2 = ensure_candles(
            BINANCE_PERPS,
            ["1m", "5m", "15m", "1h", "4h"],
            price_types=("last", "mark"),
            quiet=False,
        )
        return code2 if code2 != 0 else code
    return code
