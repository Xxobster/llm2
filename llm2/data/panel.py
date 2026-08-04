"""Multi-symbol close panel for cross-sectional targets."""

from __future__ import annotations

from functools import lru_cache

import pandas as pd

from llm2.data.loader import load_ohlcv


@lru_cache(maxsize=32)
def _cached_close_series(symbol: str, timeframe: str, source: str) -> pd.Series:
    df = load_ohlcv(symbol, timeframe, source=source)
    return df["close"].rename(symbol.upper())


def build_close_panel(
    symbols: list[str],
    timeframe: str,
    *,
    source: str = "binance",
) -> pd.DataFrame:
    """Wide panel of close prices, aligned on union of timestamps (forward-filled)."""
    series: dict[str, pd.Series] = {}
    for sym in symbols:
        series[sym.upper()] = _cached_close_series(sym.upper(), timeframe, source)
    panel = pd.concat(series.values(), axis=1).sort_index()
    return panel.ffill()


def clear_panel_cache() -> None:
    _cached_close_series.cache_clear()
