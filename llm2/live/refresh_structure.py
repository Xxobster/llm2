"""Refresh structure features into the live pack indicators slice.

Default signal source is Binance USD-M futures (research parity). Execution stays on
Bybit. Prefers botsgeneral ``shared_candles.db``; falls back to Binance fapi REST.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

BINANCE_FUTURES = "https://fapi.binance.com"
BYBIT_REST = "https://api.bybit.com"
BINANCE_INTERVAL = {"1m": "1m", "5m": "5m", "15m": "15m", "1h": "1h", "4h": "4h", "1d": "1d", "1w": "1w"}
BYBIT_INTERVAL = {"1m": "1", "5m": "5", "15m": "15", "1h": "60", "4h": "240", "1d": "D", "1w": "W"}
DEFAULT_SIGNAL_SOURCE = "binance"


def _drop_forming_bar(df: pd.DataFrame, timeframe: str) -> pd.DataFrame:
    """Keep only fully closed candles (kline timestamp = bar open)."""
    if df.empty:
        return df
    from llm2.paths import TF_MS

    step = int(TF_MS[timeframe])
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    last_open = int(df["ts_ms"].iloc[-1])
    if last_open + step > now_ms:
        return df.iloc[:-1]
    return df


def _frame_from_rows(rows: list[list[Any]], *, source: str) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    idx = pd.to_datetime([int(r[0]) for r in rows], unit="ms", utc=True)
    df = pd.DataFrame(
        {
            "ts_ms": [int(r[0]) for r in rows],
            "open": [float(r[1]) for r in rows],
            "high": [float(r[2]) for r in rows],
            "low": [float(r[3]) for r in rows],
            "close": [float(r[4]) for r in rows],
            "volume": [float(r[5]) for r in rows],
            "source": source,
        },
        index=idx,
    )
    return df[~df.index.duplicated(keep="last")].sort_index()


def fetch_ohlcv_binance_rest(symbol: str, timeframe: str, *, limit: int = 1000) -> pd.DataFrame:
    """Binance USD-M futures klines (same product family as research warehouse)."""
    iv = BINANCE_INTERVAL.get(timeframe)
    if not iv:
        raise ValueError(f"unsupported Binance timeframe {timeframe}")
    frames: list[pd.DataFrame] = []
    end: int | None = None
    remaining = int(limit)
    while remaining > 0:
        batch = min(1500, remaining)
        params: dict[str, str] = {
            "symbol": symbol.upper(),
            "interval": iv,
            "limit": str(batch),
        }
        if end is not None:
            params["endTime"] = str(end)
        q = urllib.parse.urlencode(params)
        req = urllib.request.Request(
            f"{BINANCE_FUTURES}/fapi/v1/klines?{q}",
            headers={"User-Agent": "llm2-structure-refresh/1.0"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            lst = json.loads(resp.read().decode())
        if not lst:
            break
        # Binance returns oldest→newest
        rows = [[int(r[0]), r[1], r[2], r[3], r[4], r[5]] for r in lst]
        frames.append(_frame_from_rows(rows, source="binance"))
        remaining -= len(rows)
        end = int(rows[0][0]) - 1
        if len(lst) < batch:
            break
    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames).sort_index()
    return out[~out.index.duplicated(keep="last")]


def fetch_ohlcv_bybit_rest(symbol: str, timeframe: str, *, limit: int = 1000) -> pd.DataFrame:
    """Legacy Bybit path (not used for LLM2 signal parity)."""
    iv = BYBIT_INTERVAL.get(timeframe, timeframe)
    frames: list[pd.DataFrame] = []
    end: int | None = None
    remaining = int(limit)
    while remaining > 0:
        batch = min(1000, remaining)
        params: dict[str, str] = {
            "category": "linear",
            "symbol": symbol.upper(),
            "interval": iv,
            "limit": str(batch),
        }
        if end is not None:
            params["end"] = str(end)
        q = urllib.parse.urlencode(params)
        req = urllib.request.Request(
            f"{BYBIT_REST}/v5/market/kline?{q}",
            headers={"User-Agent": "llm2-structure-refresh/1.0"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        if int(data.get("retCode", -1)) != 0:
            raise RuntimeError(data.get("retMsg"))
        rows = list(reversed(data.get("result", {}).get("list") or []))
        if not rows:
            break
        frames.append(
            _frame_from_rows(
                [[int(r[0]), r[1], r[2], r[3], r[4], r[5]] for r in rows],
                source="bybit",
            )
        )
        remaining -= len(rows)
        end = int(rows[0][0]) - 1
        if len(rows) < batch:
            break
    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames).sort_index()
    return out[~out.index.duplicated(keep="last")]


def fetch_ohlcv_shared(
    symbol: str,
    timeframe: str,
    *,
    source: str = DEFAULT_SIGNAL_SOURCE,
    limit: int = 1000,
) -> pd.DataFrame:
    """Read botsgeneral shared_candles.db when available."""
    try:
        from live_candles.reader import load_ohlcv as shared_load
    except ImportError:
        # VPS often has botsgeneral on PYTHONPATH
        bg = Path("/opt/botsgeneral")
        pkg = bg / "packages" / "live_candles" / "src"
        if pkg.is_dir() and str(pkg) not in sys.path:
            sys.path.insert(0, str(pkg))
        try:
            from live_candles.reader import load_ohlcv as shared_load
        except ImportError:
            return pd.DataFrame()
    raw = shared_load(source, symbol, timeframe, limit=int(limit))
    if raw is None or raw.empty:
        return pd.DataFrame()
    idx = pd.to_datetime(raw["ts_ms"].astype("int64"), unit="ms", utc=True)
    df = pd.DataFrame(
        {
            "ts_ms": raw["ts_ms"].astype("int64").to_numpy(),
            "open": raw["open"].astype(float).to_numpy(),
            "high": raw["high"].astype(float).to_numpy(),
            "low": raw["low"].astype(float).to_numpy(),
            "close": raw["close"].astype(float).to_numpy(),
            "volume": raw["volume"].astype(float).to_numpy(),
            "source": source,
        },
        index=idx,
    )
    return df[~df.index.duplicated(keep="last")].sort_index()


def _shared_is_fresh_enough(df: pd.DataFrame, timeframe: str, *, max_lag_bars: float = 2.0) -> bool:
    """Reject shared rows that lag more than max_lag_bars after the last close."""
    if df is None or df.empty or "ts_ms" not in df.columns:
        return False
    from llm2.paths import TF_MS

    step = int(TF_MS.get(timeframe) or 0)
    if step <= 0:
        return False
    last = int(df["ts_ms"].iloc[-1])
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    # Age after the bar's close instant.
    age_after_close = now_ms - (last + step)
    return age_after_close <= max_lag_bars * step


def fetch_signal_ohlcv(
    symbol: str,
    timeframe: str,
    *,
    source: str = DEFAULT_SIGNAL_SOURCE,
    limit: int = 1000,
) -> pd.DataFrame:
    """Signal candles: fresh Binance shared → Binance REST (research parity)."""
    src = (source or DEFAULT_SIGNAL_SOURCE).strip().lower()
    if src == "binance":
        df = fetch_ohlcv_shared(symbol, timeframe, source="binance", limit=limit)
        if len(df) >= 50 and _shared_is_fresh_enough(df, timeframe):
            return _drop_forming_bar(df, timeframe)
        df = fetch_ohlcv_binance_rest(symbol, timeframe, limit=limit)
        return _drop_forming_bar(df, timeframe)
    if src == "bybit":
        df = fetch_ohlcv_shared(symbol, timeframe, source="bybit", limit=limit)
        if len(df) >= 50 and _shared_is_fresh_enough(df, timeframe):
            return _drop_forming_bar(df, timeframe)
        df = fetch_ohlcv_bybit_rest(symbol, timeframe, limit=limit)
        return _drop_forming_bar(df, timeframe)
    raise ValueError(f"unsupported signal source {source!r}")


def refresh_symbol(
    *,
    symbol: str,
    timeframes: tuple[str, ...] = ("1h", "4h", "1w"),
    indicator_db: Path,
    limit: int = 1500,
    source: str = DEFAULT_SIGNAL_SOURCE,
) -> dict:
    # Prefer botsgeneral indicators package
    ind_src = Path("/opt/botsgeneral/packages/indicators/src")
    if ind_src.is_dir() and str(ind_src) not in sys.path:
        sys.path.insert(0, str(ind_src))
    win_src = Path(r"C:\projects\botsgeneral\packages\indicators\src")
    if win_src.is_dir() and str(win_src) not in sys.path:
        sys.path.insert(0, str(win_src))

    from indicators.compute import compute_structure
    from indicators.store import IndicatorDB

    src = (source or DEFAULT_SIGNAL_SOURCE).strip().lower()
    ind = IndicatorDB(indicator_db)
    report: dict = {
        "symbol": symbol,
        "db": str(indicator_db),
        "signal_source": src,
        "series": [],
    }
    try:
        for tf in timeframes:
            df = fetch_signal_ohlcv(symbol, tf, source=src, limit=limit)
            if df.empty or len(df) < 50:
                report["series"].append(
                    {"timeframe": tf, "error": "insufficient bars", "source": src}
                )
                continue
            bundle = compute_structure(
                df.reset_index(drop=True),
                source=src,
                symbol=symbol.upper(),
                timeframe=tf,
            )
            counts = ind.upsert_bundle(bundle)
            last = int(df["ts_ms"].iloc[-1])
            report["series"].append(
                {
                    "timeframe": tf,
                    "source": src,
                    "n_bars": int(len(df)),
                    "last_ts_ms": last,
                    "last_utc": datetime.fromtimestamp(
                        last / 1000, tz=timezone.utc
                    ).isoformat(),
                    "counts": counts,
                }
            )
    finally:
        ind.close()
    report["refreshed_utc"] = datetime.now(timezone.utc).isoformat()
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--db", type=Path, required=True)
    ap.add_argument("--timeframes", default="1h,4h,1w")
    ap.add_argument(
        "--source",
        default=DEFAULT_SIGNAL_SOURCE,
        help="Signal candle/indicator vendor (default binance = research parity)",
    )
    args = ap.parse_args(argv)
    tfs = tuple(x.strip() for x in args.timeframes.split(",") if x.strip())
    rep = refresh_symbol(
        symbol=args.symbol,
        timeframes=tfs,
        indicator_db=args.db,
        source=str(args.source),
    )
    print(json.dumps(rep, indent=2))
    bad = [s for s in rep["series"] if s.get("error")]
    return 1 if bad and len(bad) == len(rep["series"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
