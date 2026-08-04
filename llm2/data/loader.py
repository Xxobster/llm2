"""Load OHLCV from shared market warehouse."""

from __future__ import annotations

import sqlite3

import pandas as pd

from llm2.paths import MARKET_DB

# Warehouse historically used both ``last`` and ``last_price`` labels for the same
# Binance last-trade series. Prefer the long canonical series; never mix types in one load.
_PRICE_TYPE_PREFERENCE = ("last_price", "last")


def _resolve_price_type(
    conn: sqlite3.Connection,
    *,
    symbol: str,
    timeframe: str,
    source: str,
) -> str:
    rows = conn.execute(
        "SELECT price_type, COUNT(*) AS n FROM market_ohlcv "
        "WHERE symbol = ? AND timeframe = ? AND source = ? "
        "AND (is_complete = 1 OR is_complete IS NULL) "
        "GROUP BY price_type ORDER BY n DESC",
        (symbol, timeframe, source),
    ).fetchall()
    if not rows:
        raise ValueError(f"No OHLCV for {symbol} {timeframe} source={source}")
    available = {str(r[0]): int(r[1]) for r in rows}
    # ``last`` and ``last_price`` are warehouse synonyms for Binance last-trade.
    # Prefer the densest synonym so a short newly labelled ``last_price`` series
    # cannot shadow a long ``last`` history (or the reverse).
    synonyms = [
        (pref, available[pref])
        for pref in _PRICE_TYPE_PREFERENCE
        if available.get(pref, 0) > 0
    ]
    if synonyms:
        return max(synonyms, key=lambda item: item[1])[0]
    # Fall back to the densest remaining type (never mix).
    return str(rows[0][0])


def load_ohlcv(
    symbol: str,
    timeframe: str,
    *,
    source: str = "binance",
    start_ms: int | None = None,
    end_ms: int | None = None,
    price_type: str | None = None,
) -> pd.DataFrame:
    """Return sorted OHLCV with UTC DatetimeIndex and ts_ms column.

    Pins a single ``price_type`` so ``last`` and ``last_price`` rows are never concatenated.
    """
    if not MARKET_DB.is_file():
        raise FileNotFoundError(f"Market warehouse missing: {MARKET_DB}")

    symbol_u = symbol.upper()
    # Shared warehouse: a long hunt can hold read locks; wait rather than fail closed.
    conn = sqlite3.connect(f"file:{MARKET_DB}?mode=ro", uri=True, timeout=120.0)
    try:
        conn.execute("PRAGMA busy_timeout=120000")
        chosen = price_type or _resolve_price_type(
            conn, symbol=symbol_u, timeframe=timeframe, source=source
        )
        clauses = [
            "symbol = ?",
            "timeframe = ?",
            "source = ?",
            "price_type = ?",
            "(is_complete = 1 OR is_complete IS NULL)",
        ]
        params: list[object] = [symbol_u, timeframe, source, chosen]
        if start_ms is not None:
            clauses.append("ts_ms >= ?")
            params.append(int(start_ms))
        if end_ms is not None:
            clauses.append("ts_ms < ?")
            params.append(int(end_ms))

        sql = (
            "SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv "
            f"WHERE {' AND '.join(clauses)} ORDER BY ts_ms"
        )
        df = pd.read_sql(sql, conn, params=params)
    finally:
        conn.close()

    if df.empty:
        raise ValueError(
            f"No OHLCV for {symbol_u} {timeframe} source={source} price_type={chosen}"
        )

    df["timestamp"] = pd.to_datetime(df["ts_ms"], unit="ms", utc=True)
    df = df.set_index("timestamp").sort_index()
    if df.index.has_duplicates:
        raise ValueError(
            f"Duplicate timestamps for {symbol_u} {timeframe} price_type={chosen}"
        )
    for col in ("open", "high", "low", "close", "volume"):
        df[col] = df[col].astype(float)
    df.attrs["price_type"] = chosen
    return df
