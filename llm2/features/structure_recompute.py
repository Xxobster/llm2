"""Warehouse-aware structure builder for the leakage engine (CAUS-WAREHOUSE-001).

``build_structure_v1`` joins a pre-computed indicator warehouse. Feeding it a truncated
OHLCV frame does not truncate that warehouse, so the shared prefix-invariance check
false-PASSes unless the builder recomputes indicators from the candles it is handed.

This module is the only builder the leakage guard may use for ``structure_v1`` (and
spaces that wrap it). Research/live keep using the warehouse for speed; the audit path
must pay the recompute cost.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Any

import pandas as pd

from llm2.features.structure_v1 import HIGHER_TIMEFRAMES, build_structure_v1


def _prefer_indicators() -> None:
    import sys

    src = Path(r"C:\projects\botsgeneral\packages\indicators\src")
    if src.is_dir() and str(src) not in sys.path:
        sys.path.insert(0, str(src))


def recompute_structure_warehouse(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str,
    higher_timeframes: tuple[str, ...],
    source: str = "binance",
) -> Path:
    """Materialise a temporary indicator DB from ``ohlcv`` (+ HTF truncated to its tip)."""
    _prefer_indicators()
    from indicators.compute import compute_structure
    from indicators.store import IndicatorDB

    from llm2.data.loader import load_ohlcv

    tip = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True)).max()
    tmp = Path(tempfile.mkdtemp(prefix="leak_struct_"))
    db_path = tmp / "indicators.sqlite"
    ind = IndicatorDB(db_path)

    # Decision timeframe: use the frame the checker handed us (already truncated).
    series: dict[str, pd.DataFrame] = {timeframe: ohlcv}
    for htf in higher_timeframes:
        if htf == timeframe:
            continue
        try:
            full = load_ohlcv(symbol, htf, source=source)
        except Exception:  # noqa: BLE001
            continue
        series[htf] = full.loc[pd.to_datetime(full.index, utc=True) <= tip]

    for tf, frame in series.items():
        if frame is None or len(frame) < 60:
            continue
        # compute_structure expects a RangeIndex frame with OHLCV columns.
        raw = frame.reset_index(drop=True)
        # Preserve ts_ms if the loader left it as index name / column.
        if "ts_ms" not in raw.columns:
            ts = pd.DatetimeIndex(pd.to_datetime(frame.index, utc=True))
            raw = raw.copy()
            raw["ts_ms"] = (ts.asi8 // 1_000_000).astype("int64")
        bundle = compute_structure(raw, source=source, symbol=symbol.upper(), timeframe=tf)
        ind.upsert_bundle(bundle)
    return db_path


def build_structure_v1_for_leakage(
    ohlcv: pd.DataFrame,
    *,
    interval: str = "1h",
    symbol: str = "ETHUSDT",
    higher_timeframes: tuple[str, ...] | None = None,
    **kwargs: Any,
) -> pd.DataFrame:
    """Recompute structure into a temp warehouse, then run the normal join path."""
    from llm2.data.indicators import clear_indicator_cache

    tf = str(interval)
    htfs = (
        higher_timeframes
        if higher_timeframes is not None
        else HIGHER_TIMEFRAMES.get(tf, ())
    )
    # Include the decision TF itself so the warehouse has a native series.
    all_tfs = tuple(dict.fromkeys((tf, *htfs)))
    db_path = recompute_structure_warehouse(
        ohlcv,
        symbol=symbol,
        timeframe=tf,
        higher_timeframes=all_tfs,
        source=str(kwargs.get("source") or "binance"),
    )
    prev = os.environ.get("LLM2_INDICATORS_DB")
    os.environ["LLM2_INDICATORS_DB"] = str(db_path)
    try:
        clear_indicator_cache()
        return build_structure_v1(
            ohlcv,
            symbol=symbol,
            timeframe=tf,
            higher_timeframes=htfs,
            recent_only=False,
            source=kwargs.get("source"),
        )
    finally:
        clear_indicator_cache()
        if prev is None:
            os.environ.pop("LLM2_INDICATORS_DB", None)
        else:
            os.environ["LLM2_INDICATORS_DB"] = prev
