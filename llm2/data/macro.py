"""Causal access to the external (non-crypto) series in the shared market warehouse.

Three defects in the previous access path are fixed here.

**Open-time stamping.** ``market_ohlcv.ts_ms`` is the bar's *open* instant. A bar stamped
``T`` on timeframe ``tf`` is therefore only knowable at ``T + tf``. The previous macro
loader forward-filled a daily bar stamped ``D 00:00`` across every hour of day ``D``, so at
01:00 the model received the close of a day that had 23 hours left to run. Every series
here is re-indexed to its **completion instant** before anything else touches it.

**Vendor collision.** The previous loader selected on ``(symbol, timeframe)`` only. That is
safe for the six symbols it used because each has a single vendor, but ``EURUSD``,
``XAUUSD``, ``USDJPY``, ``WTI``, ``COPPER`` and others exist under both ``dukascopy`` and
``yahoo``; selecting without a source silently interleaves two vendors' bars. Every lookup
here requires an explicit ``(symbol, source, timeframe)`` triple.

**Silent staleness.** Foreign exchange, indices and commodities close overnight and at
weekends; crypto does not. Forward-filling them onto a 24/7 index produces long constant
runs that a model can read as information. Every aligned series is accompanied by an age
column so staleness is an explicit feature rather than an invisible artefact.

``is_complete`` in the warehouse is not trustworthy on the newest bar (the daily BTCUSDT bar
for the current day is flagged complete while still in progress), so completeness is
recomputed from ``ts_ms + timeframe`` rather than read from the flag.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

from llm2.paths import MARKET_DB, TF_MS

FUNDING_DB = Path(r"D:\projectsdata\candles\binance_funding.sqlite")
COVERAGE_CSV = Path(r"D:\projectsdata\candles\coverage.csv")

DAY = pd.Timedelta(days=1)
ZERO = pd.Timedelta(0)


@dataclass(frozen=True)
class ExternalSeries:
    """One external series, pinned to a single vendor with an explicit publication lag."""

    symbol: str
    source: str
    category: str
    timeframes: tuple[str, ...]
    publication_lag: pd.Timedelta
    description: str
    # True when the series is already stationary and its *level* is the meaningful quantity.
    # A yield, a volatility index, a term spread and a sentiment index all carry their
    # information in the level; log-differencing them, as is correct for a price, throws
    # that information away and leaves noise.
    stationary_level: bool = False

    @property
    def key(self) -> str:
        return f"{self.symbol}@{self.source}"


# Vendor choice is pinned, not inferred. Dukascopy is preferred for foreign exchange,
# metals and energy because it carries genuine intraday bars back to 2003; Yahoo is the
# only source for the equity indices and VIX; FRED for the yield curve; DefiLlama for
# stablecoin supply. Publication lag is *additional* to bar completion: market data is
# known at its close, whereas a statistical release is not.
EXTERNAL_REGISTRY: tuple[ExternalSeries, ...] = (
    # --- Dollar and foreign exchange -------------------------------------------------
    ExternalSeries("DXY", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "US dollar index"),
    ExternalSeries("EURUSD", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "Euro / US dollar"),
    ExternalSeries("GBPUSD", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "Sterling / US dollar"),
    ExternalSeries("USDJPY", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "US dollar / yen"),
    ExternalSeries("USDCHF", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "US dollar / Swiss franc"),
    ExternalSeries("USDCAD", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "US dollar / Canadian dollar"),
    ExternalSeries("AUDUSD", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "Australian dollar / US dollar"),
    ExternalSeries("NZDUSD", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "NZ dollar / US dollar"),
    ExternalSeries("EURJPY", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "Euro / yen"),
    ExternalSeries("EURGBP", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "Euro / sterling"),
    ExternalSeries("EURCHF", "dukascopy", "fx", ("1h", "4h", "1d", "1w"), ZERO, "Euro / Swiss franc"),
    # --- Metals and energy -----------------------------------------------------------
    ExternalSeries("XAUUSD", "dukascopy", "metals", ("1h", "4h", "1d", "1w"), ZERO, "Gold spot"),
    ExternalSeries("XAGUSD", "dukascopy", "metals", ("1h", "4h", "1d", "1w"), ZERO, "Silver spot"),
    ExternalSeries("COPPER", "dukascopy", "metals", ("1h", "4h", "1d", "1w"), ZERO, "Copper"),
    ExternalSeries("WTI", "dukascopy", "energy", ("1h", "4h", "1d", "1w"), ZERO, "WTI crude"),
    ExternalSeries("BRENT", "dukascopy", "energy", ("1h", "4h", "1d", "1w"), ZERO, "Brent crude"),
    # --- Equity indices and volatility -----------------------------------------------
    ExternalSeries("SPX", "yahoo", "index", ("1d", "1w"), ZERO, "S&P 500"),
    ExternalSeries("NDX", "yahoo", "index", ("1d", "1w"), ZERO, "Nasdaq 100"),
    ExternalSeries("DJI", "yahoo", "index", ("1d", "1w"), ZERO, "Dow Jones Industrial Average"),
    ExternalSeries("HSI", "yahoo", "index", ("1h", "4h", "1d", "1w"), ZERO, "Hang Seng"),
    ExternalSeries("HKG40", "dukascopy", "index", ("1h", "4h", "1d", "1w"), ZERO, "Hong Kong 40"),
    ExternalSeries("VIX", "yahoo", "vol", ("1d", "1w"), ZERO, "CBOE volatility index", True),
    # --- Rates -----------------------------------------------------------------------
    # FRED republishes with a lag; a value dated D is not reliably retrievable until D+1.
    ExternalSeries("US02Y", "fred", "rates", ("1d", "1w"), DAY, "2-year Treasury yield", True),
    ExternalSeries("US10Y", "fred", "rates", ("1d", "1w"), DAY, "10-year Treasury yield", True),
    ExternalSeries("US03M", "fred", "rates", ("1d", "1w"), DAY, "3-month Treasury yield", True),
    ExternalSeries("T10Y2Y", "fred", "rates", ("1d", "1w"), DAY, "10y minus 2y term spread", True),
    # --- Crypto-native macro and sentiment -------------------------------------------
    # Stablecoin supply is a flow-of-funds proxy: minting precedes deployment into risk.
    ExternalSeries("STABLE_MCAP", "defillama", "stablecoin", ("1d", "1w"), DAY, "Total stablecoin supply"),
    ExternalSeries("STABLE_FLOW", "defillama", "stablecoin", ("1d", "1w"), DAY, "Stablecoin net flow"),
    ExternalSeries("USDT_MCAP", "defillama", "stablecoin", ("1d", "1w"), DAY, "Tether supply"),
    ExternalSeries("USDC_MCAP", "defillama", "stablecoin", ("1d", "1w"), DAY, "USD Coin supply"),
    ExternalSeries(
        "FNG", "alternative", "sentiment", ("1d", "1w"), ZERO, "Crypto fear and greed index", True
    ),
)

# Columns that are stationary levels but are not warehouse series (funding is attached
# separately from its own database).
EXTRA_STATIONARY_LEVELS = frozenset({"FUNDING_RATE"})


def stationary_level_columns() -> set[str]:
    """Panel columns whose level, not log-difference, carries the information."""
    return {s.symbol for s in EXTERNAL_REGISTRY if s.stationary_level} | set(EXTRA_STATIONARY_LEVELS)

# BTC_MCAP and ETH_MCAP are deliberately absent: market capitalisation is price times a
# slow-moving supply, so they are near-linear transforms of the very series being predicted
# and produce hard forward-correlation findings. Do not add them without a non-leaky
# transform and a fresh audit.
EXCLUDED_SYMBOLS = frozenset({"BTC_MCAP", "ETH_MCAP", "DAI_MCAP"})

_BY_SYMBOL = {s.symbol: s for s in EXTERNAL_REGISTRY}


def get_series_spec(symbol: str) -> ExternalSeries:
    try:
        return _BY_SYMBOL[symbol.upper()]
    except KeyError:
        raise KeyError(
            f"{symbol} is not in EXTERNAL_REGISTRY; add it with an explicit source and "
            "publication lag rather than querying by symbol alone"
        ) from None


def registry_for(category: str | None = None, timeframe: str | None = None) -> list[ExternalSeries]:
    """Registry entries filtered by category and/or availability at a timeframe."""
    out = list(EXTERNAL_REGISTRY)
    if category is not None:
        out = [s for s in out if s.category == category]
    if timeframe is not None:
        out = [s for s in out if timeframe in s.timeframes]
    return out


def _completion_index(ts_ms: np.ndarray, timeframe: str) -> pd.DatetimeIndex:
    """Instant at which a bar stamped at open time ``ts_ms`` is fully known."""
    step = TF_MS.get(timeframe)
    if step is None:
        step = int(pd.Timedelta(timeframe).total_seconds() * 1000)
    return pd.to_datetime(np.asarray(ts_ms, dtype="int64") + step, unit="ms", utc=True)


@lru_cache(maxsize=256)
def _load_raw(symbol: str, source: str, timeframe: str) -> pd.DataFrame:
    """Raw bars for one pinned (symbol, source, timeframe), indexed by completion instant.

    Cached because a diagnostics run re-reads the same series across lag grids and
    bootstrap draws, and an unindexed scan of this 17.9 GB table costs about two minutes.
    """
    if not MARKET_DB.is_file():
        raise FileNotFoundError(f"Market warehouse missing: {MARKET_DB}")

    sql = (
        "SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv "
        "WHERE symbol = ? AND source = ? AND timeframe = ? ORDER BY ts_ms"
    )
    conn = sqlite3.connect(f"file:{MARKET_DB}?mode=ro", uri=True, timeout=120.0)
    try:
        conn.execute("PRAGMA busy_timeout=120000")
        df = pd.read_sql(sql, conn, params=(symbol.upper(), source, timeframe))
    finally:
        conn.close()

    if df.empty:
        raise ValueError(f"No bars for {symbol} source={source} timeframe={timeframe}")

    df.index = _completion_index(df["ts_ms"].to_numpy(), timeframe)
    df.index.name = "known_at"
    df = df[~df.index.duplicated(keep="last")].sort_index()
    for col in ("open", "high", "low", "close", "volume"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def load_external(
    symbol: str,
    timeframe: str,
    *,
    source: str | None = None,
    field: str = "close",
) -> pd.Series:
    """One external series indexed by the instant its value becomes knowable.

    The publication lag from the registry is added on top of bar completion, so the index
    is a hard "not before" boundary for using the value in a decision.
    """
    spec = get_series_spec(symbol) if source is None else None
    src = source or spec.source  # type: ignore[union-attr]
    lag = spec.publication_lag if spec is not None else ZERO

    raw = _load_raw(symbol.upper(), src, timeframe)
    series = raw[field].copy()
    series.index = series.index + lag
    series.name = symbol.upper()
    return series.dropna()


def align_causal(
    series: pd.Series,
    target_index: pd.DatetimeIndex,
    *,
    max_age: pd.Timedelta | None = None,
) -> pd.DataFrame:
    """As-of join a knowable-at series onto a decision index.

    Returns the last value known strictly at or before each decision instant, plus its age.
    ``merge_asof`` with the default ``direction="backward"`` is exactly the causal
    operation; ``reindex(method="ffill")`` on an open-stamped index is not.
    """
    target_index = pd.DatetimeIndex(target_index)
    if target_index.tz is None:
        target_index = target_index.tz_localize("UTC")

    # merge_asof requires identical datetime unit/tz dtypes (ms vs ns fails hard).
    decision_at = pd.to_datetime(pd.DatetimeIndex(target_index), utc=True).astype(
        "datetime64[ns, UTC]"
    )
    known_at = pd.to_datetime(pd.DatetimeIndex(series.index), utc=True).astype(
        "datetime64[ns, UTC]"
    )

    left = pd.DataFrame({"decision_at": decision_at})
    right = pd.DataFrame(
        {"known_at": known_at, "value": series.to_numpy()}
    ).sort_values("known_at")

    merged = pd.merge_asof(left, right, left_on="decision_at", right_on="known_at", direction="backward")
    age = merged["decision_at"] - merged["known_at"]

    out = pd.DataFrame(
        {
            "value": merged["value"].to_numpy(),
            "age_sec": age.dt.total_seconds().to_numpy(),
        },
        index=target_index,
    )
    if max_age is not None:
        too_old = out["age_sec"] > max_age.total_seconds()
        out.loc[too_old, "value"] = np.nan
    return out


def build_external_panel(
    target_index: pd.DatetimeIndex,
    symbols: list[str],
    timeframe: str,
    *,
    field: str = "close",
    max_age: pd.Timedelta | None = None,
    include_age: bool = True,
) -> pd.DataFrame:
    """Causally aligned panel of external series on a crypto decision index.

    Series unavailable at ``timeframe`` fall back to the coarsest available timeframe in
    their registry entry, which is correct because alignment is as-of rather than
    positional. Symbols missing from the warehouse are skipped rather than filled.
    """
    target_index = pd.DatetimeIndex(target_index)
    frames: dict[str, pd.Series] = {}

    for sym in symbols:
        spec = get_series_spec(sym)
        tf = timeframe if timeframe in spec.timeframes else _coarsest(spec.timeframes)
        try:
            series = load_external(sym, tf, field=field)
        except (ValueError, FileNotFoundError):
            continue
        aligned = align_causal(series, target_index, max_age=max_age)
        frames[sym] = aligned["value"]
        if include_age:
            frames[f"{sym}__age_sec"] = aligned["age_sec"]

    if not frames:
        return pd.DataFrame(index=target_index)
    return pd.DataFrame(frames, index=target_index)


def _coarsest(timeframes: tuple[str, ...]) -> str:
    order = ["1h", "4h", "1d", "1w"]
    for tf in order:
        if tf in timeframes:
            return tf
    return timeframes[0]


def load_funding(symbol: str, *, source: str = "binance") -> pd.Series:
    """Realised funding rate indexed by settlement instant.

    A settlement at ``T`` is treated as knowable at ``T``: the rate is charged then, and
    although Binance publishes a running prediction earlier, that prediction is not what is
    stored here. Using the realised value before its settlement would be look-ahead.
    """
    if not FUNDING_DB.is_file():
        raise FileNotFoundError(f"Funding warehouse missing: {FUNDING_DB}")

    conn = sqlite3.connect(f"file:{FUNDING_DB}?mode=ro", uri=True, timeout=60.0)
    try:
        df = pd.read_sql(
            "SELECT funding_time_ms, funding_rate FROM funding_rate "
            "WHERE symbol = ? AND source = ? ORDER BY funding_time_ms",
            conn,
            params=(symbol.upper(), source),
        )
    finally:
        conn.close()

    if df.empty:
        raise ValueError(f"No funding for {symbol} source={source}")

    idx = pd.to_datetime(df["funding_time_ms"].to_numpy(), unit="ms", utc=True)
    series = pd.Series(df["funding_rate"].astype(float).to_numpy(), index=idx, name=f"funding_{symbol.upper()}")
    return series[~series.index.duplicated(keep="last")].sort_index()


@lru_cache(maxsize=1)
def warehouse_inventory() -> pd.DataFrame:
    """Coverage table for the warehouse, so callers never scan the 17.9 GB bar table."""
    if not COVERAGE_CSV.is_file():
        raise FileNotFoundError(f"Coverage file missing: {COVERAGE_CSV}")
    df = pd.read_csv(COVERAGE_CSV)
    df["first"] = pd.to_datetime(df["first"], utc=True)
    df["last"] = pd.to_datetime(df["last"], utc=True)
    return df


def available_externals(timeframe: str, *, min_bars: int = 500) -> list[ExternalSeries]:
    """Registry entries that genuinely have data at ``timeframe`` in the warehouse."""
    inv = warehouse_inventory()
    have = {
        (row.symbol, row.source)
        for row in inv.itertuples()
        if row.timeframe == timeframe and row.bars >= min_bars
    }
    return [s for s in EXTERNAL_REGISTRY if (s.symbol, s.source) in have]


def clear_macro_cache() -> None:
    _load_raw.cache_clear()
    warehouse_inventory.cache_clear()
