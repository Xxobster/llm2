"""Backtest entrypoint via tradesim.run_backtest."""

from __future__ import annotations

from typing import Any, Sequence

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import BarSeries, Signal, run_backtest  # noqa: E402

from llm2.paths import TF_MS  # noqa: E402


def ohlcv_to_bar_series(ohlcv: pd.DataFrame, *, symbol: str, timeframe: str) -> BarSeries:
    """Convert warehouse OHLCV frame to tradesim BarSeries."""
    if "ts_ms" in ohlcv.columns:
        ts = ohlcv["ts_ms"].to_numpy(dtype=np.int64)
    else:
        idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
        ts = (idx.asi8 // 1_000_000).astype(np.int64)
    tf_ms = TF_MS.get(timeframe)
    if tf_ms is None:
        raise ValueError(f"unknown timeframe: {timeframe}")
    return BarSeries(
        ts_ms=np.asarray(ts, dtype=np.int64),
        open=ohlcv["open"].to_numpy(dtype=float),
        high=ohlcv["high"].to_numpy(dtype=float),
        low=ohlcv["low"].to_numpy(dtype=float),
        close=ohlcv["close"].to_numpy(dtype=float),
        volume=ohlcv["volume"].to_numpy(dtype=float) if "volume" in ohlcv.columns else None,
        timeframe_ms=int(tf_ms),
        symbol=symbol.upper(),
    )


def _infer_touch_timeframe(touch_ohlcv: pd.DataFrame) -> str:
    """Infer touch timeframe from bar spacing; snap to a known TF_MS key."""
    if "ts_ms" in touch_ohlcv.columns:
        ts = np.asarray(touch_ohlcv["ts_ms"].to_numpy(dtype=np.int64), dtype=np.int64)
    else:
        idx = pd.DatetimeIndex(pd.to_datetime(touch_ohlcv.index, utc=True))
        ts = (idx.asi8 // 1_000_000).astype(np.int64)
    if ts.size < 2:
        raise ValueError("touch_ohlcv needs >= 2 bars to infer timeframe")
    positive = np.diff(np.sort(np.unique(ts)))
    positive = positive[positive > 0]
    if positive.size == 0:
        raise ValueError("touch_ohlcv has no positive spacing")
    med_ms = int(np.median(positive))
    name, ms = min(TF_MS.items(), key=lambda item: abs(int(item[1]) - med_ms))
    if abs(int(ms) - med_ms) > max(1, int(ms) // 10):
        raise ValueError(f"cannot infer touch timeframe from median spacing {med_ms} ms")
    return str(name)


def run_strategy_backtest(
    ohlcv: pd.DataFrame,
    signals: Sequence[Signal],
    *,
    symbol: str,
    timeframe: str,
    strategy_id: str = "llm2",
    strategy_version: str = "0.1.0",
    touch_ohlcv: pd.DataFrame | None = None,
    touch_timeframe: str | None = None,
    strategy_meta: dict[str, Any] | None = None,
    plot: bool = False,
    print_headline: bool = False,
    store_path: str | None = None,
    costs: Any = None,
    margin: Any = None,
    sizing: Any = None,
    sim: Any = None,
    instrument: Any = None,
    funding_ts_ms: np.ndarray | None = None,
    funding_rate: np.ndarray | None = None,
) -> Any:
    """Run tradesim research backtest. Returns BacktestBundle.

    Leaving ``costs`` / ``margin`` / ``sizing`` / ``sim`` unset accepts tradesim's own
    defaults, which are **not** a deployable scenario: sizing defaults to one whole unit of
    the base asset, so a single BTCUSDT trade carries roughly six times the default ten
    thousand dollar wallet. Callers that quote a profit factor should pass the research
    factories (``tradesim.research_costs`` / ``research_margin`` / ``research_sizing``) and
    an ``instrument`` so quantities are rounded to venue rules.
    """
    bars = ohlcv_to_bar_series(ohlcv, symbol=symbol, timeframe=timeframe)
    touch = None
    if touch_ohlcv is not None and len(touch_ohlcv) > 0:
        touch_tf = touch_timeframe or _infer_touch_timeframe(touch_ohlcv)
        touch = ohlcv_to_bar_series(touch_ohlcv, symbol=symbol, timeframe=touch_tf)

    meta = {"name": strategy_id, "batch": "llm2-research", **(strategy_meta or {})}
    extra: dict[str, Any] = {}
    for key, value in (
        ("costs", costs),
        ("margin", margin),
        ("sizing", sizing),
        ("sim", sim),
        ("instrument", instrument),
        ("funding_ts_ms", funding_ts_ms),
        ("funding_rate", funding_rate),
    ):
        if value is not None:
            extra[key] = value

    return run_backtest(
        strategy_id=strategy_id,
        strategy_version=strategy_version,
        bars=bars,
        signals=list(signals),
        symbol=symbol.upper(),
        touch_bars=touch,
        strategy_meta=meta,
        plot=plot,
        print_headline=print_headline,
        store_path=store_path,
        report=store_path is not None,
        **extra,
    )
