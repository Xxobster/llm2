"""Market data quality audit."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from llm2.data.loader import load_ohlcv
from llm2.paths import FORWARD_LOCKBOX_START, MARKET_DB


@dataclass
class DataAuditReport:
    symbol: str
    timeframe: str
    n_bars: int
    start: str
    end: str
    gap_count: int
    invalid_ohlc: int
    duplicate_ts: int
    pre_launch_bars: int
    lockbox_contamination: int
    passed: bool
    notes: list[str]


def audit_ohlcv(
    symbol: str,
    timeframe: str,
    *,
    source: str = "binance",
    expected_ms: int | None = None,
) -> DataAuditReport:
    from llm2.paths import TF_MS

    df = load_ohlcv(symbol, timeframe, source=source)
    notes: list[str] = []
    ts = (pd.DatetimeIndex(df.index).astype("int64") // 1_000_000).astype(np.int64)
    step = expected_ms or TF_MS.get(timeframe, 3_600_000)
    gaps = int(np.sum(np.diff(ts) > step * 1.5)) if len(ts) > 1 else 0

    invalid = int(
        ((df["high"] < df[["open", "close", "low"]].max(axis=1))
         | (df["low"] > df[["open", "close", "high"]].min(axis=1))
         | (df[["open", "high", "low", "close"]] <= 0).any(axis=1)).sum()
    )
    dup = int(df.index.duplicated().sum())
    lockbox_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    lockbox = int((ts >= lockbox_ms).sum())

    passed = gaps == 0 and invalid == 0 and dup == 0
    if gaps:
        notes.append(f"{gaps} gaps detected")
    if invalid:
        notes.append(f"{invalid} invalid OHLC rows")
    if dup:
        notes.append(f"{dup} duplicate timestamps")
    if not MARKET_DB.is_file():
        notes.append("market warehouse missing")
        passed = False

    return DataAuditReport(
        symbol=symbol.upper(),
        timeframe=timeframe,
        n_bars=len(df),
        start=str(df.index[0]),
        end=str(df.index[-1]),
        gap_count=gaps,
        invalid_ohlc=invalid,
        duplicate_ts=dup,
        pre_launch_bars=0,
        lockbox_contamination=lockbox,
        passed=passed,
        notes=notes,
    )
