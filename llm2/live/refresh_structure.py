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


# Structure swings are path-dependent from the left edge of the series.
# Truncating to a few hundred/thousand bars changes confirmed swings vs research.
DEFAULT_STRUCTURE_HISTORY_BARS = {
    "1m": 20_000,
    "5m": 20_000,
    "15m": 20_000,
    "1h": 20_000,
    "4h": 10_000,
    "1d": 3_000,
    "1w": 800,
}
MIN_STRUCTURE_HISTORY_BARS = {
    "15m": 5_000,
    "1h": 5_000,
    "4h": 2_000,
    "1w": 200,
}


def fetch_ohlcv_shared(
    symbol: str,
    timeframe: str,
    *,
    source: str = DEFAULT_SIGNAL_SOURCE,
    limit: int | None = 1000,
) -> pd.DataFrame:
    """Read botsgeneral shared_candles.db when available.

    ``limit=None`` loads the full available history for that exchange/symbol/TF
    (capped only by what shared_candles holds). Prefer this for structure refresh.
    """
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
    # live_candles may require an int; use a large sentinel for "all".
    req = int(limit) if limit is not None else 5_000_000
    raw = shared_load(source, symbol, timeframe, limit=req)
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

def _latest_closed_bar_open_ms(timeframe: str, *, now_ms: int | None = None) -> int:
    """Open timestamp (ms) of the latest fully closed bar (wall-clock)."""
    from llm2.paths import TF_MS

    step = int(TF_MS[timeframe])
    now = int(
        now_ms
        if now_ms is not None
        else datetime.now(timezone.utc).timestamp() * 1000
    )
    forming_open = (now // step) * step
    return int(forming_open - step)


def _shared_is_fresh_enough(
    df: pd.DataFrame,
    timeframe: str,
    *,
    max_lag_bars: float = 2.0,
    now_ms: int | None = None,
) -> bool:
    """Reject shared rows that lag the latest closed bar or exceed max_lag_bars.

    Tip age alone is insufficient: a tip stuck one bar behind can still look
    \"fresh\" (its own close was recent) while catch-up cannot see the new bar,
    so Representational State Transfer (REST) fallback never runs → STALE_BAR loop.
    """
    if df is None or df.empty or "ts_ms" not in df.columns:
        return False
    from llm2.paths import TF_MS

    step = int(TF_MS.get(timeframe) or 0)
    if step <= 0:
        return False
    last = int(df["ts_ms"].iloc[-1])
    now = int(
        now_ms
        if now_ms is not None
        else datetime.now(timezone.utc).timestamp() * 1000
    )
    need = _latest_closed_bar_open_ms(timeframe, now_ms=now)
    if last < need:
        return False
    # Age after the tip bar's close instant.
    age_after_close = now - (last + step)
    return age_after_close <= max_lag_bars * step


def _merge_ohlcv_tip(base: pd.DataFrame, tip: pd.DataFrame) -> pd.DataFrame:
    """Append/override tip bars onto a deeper base history (dedupe by ts_ms)."""
    if base is None or base.empty:
        return tip.copy() if tip is not None else pd.DataFrame()
    if tip is None or tip.empty:
        return base.copy()
    out = pd.concat([base, tip], axis=0)
    out = out[~out.index.duplicated(keep="last")].sort_index()
    if "ts_ms" in out.columns:
        out = out.drop_duplicates(subset=["ts_ms"], keep="last").sort_values("ts_ms")
        out.index = pd.to_datetime(out["ts_ms"].astype("int64"), unit="ms", utc=True)
    return out


def fetch_signal_ohlcv(
    symbol: str,
    timeframe: str,
    *,
    source: str = DEFAULT_SIGNAL_SOURCE,
    limit: int | None = 1000,
    force_rest_tip: bool = False,
) -> pd.DataFrame:
    """Signal candles: fresh Binance shared → Binance REST (research parity).

    For structure refresh pass ``limit=None`` (or a large DEFAULT_STRUCTURE_HISTORY
    value). Decision-loop OHLCV for vol-normalised columns may stay short (e.g. 300).

    When shared history is deep but tip-lagged, merge a short REST tip onto shared
    — never replace full shared history with a short REST window (that rebuilds
    swings on ~20k bars and reintroduces live↔warehouse tip-drift).

    ``force_rest_tip=True`` always overlays a REST tip even when shared looks fresh.
    Required for tip-identity / live↔recompute parity: shared 15m tips on the VPS
    have been observed to revise after the live decide (e.g. SOL close 76.22→76.19),
    which moves scores while the gate action stays FLAT.
    """
    src = (source or DEFAULT_SIGNAL_SOURCE).strip().lower()
    rest_limit = int(limit) if limit is not None else int(
        DEFAULT_STRUCTURE_HISTORY_BARS.get(timeframe, 20_000)
    )
    tip_rest_limit = min(int(rest_limit), 1500)

    def _load(shared_fn, rest_fn) -> pd.DataFrame:
        shared = shared_fn(symbol, timeframe, source=src, limit=limit)
        shared_ok = len(shared) >= 50 and _shared_is_fresh_enough(shared, timeframe)
        if shared_ok and not force_rest_tip:
            return _drop_forming_bar(shared, timeframe)
        rest = rest_fn(
            symbol,
            timeframe,
            limit=tip_rest_limit if len(shared) >= 50 else rest_limit,
        )
        if len(shared) >= 50:
            return _drop_forming_bar(_merge_ohlcv_tip(shared, rest), timeframe)
        return _drop_forming_bar(rest, timeframe)

    if src == "binance":
        return _load(fetch_ohlcv_shared, fetch_ohlcv_binance_rest)
    if src == "bybit":
        return _load(fetch_ohlcv_shared, fetch_ohlcv_bybit_rest)
    raise ValueError(f"unsupported signal source {source!r}")


def refresh_symbol(
    *,
    symbol: str,
    timeframes: tuple[str, ...] = ("1h", "4h", "1w"),
    indicator_db: Path,
    limit: int | None = None,
    source: str = DEFAULT_SIGNAL_SOURCE,
) -> dict:
    """Recompute structure into ``indicator_db``.

    IMPORTANT: ``upsert_bundle`` replaces the entire series. The Open-High-Low-Close-
    Volume (OHLCV) window must therefore be long enough to match research swing
    geometry. Default ``limit=None`` loads full shared history (per-TF caps in
    ``DEFAULT_STRUCTURE_HISTORY_BARS`` only when REST fallback is required).
    Passing a short limit (e.g. 800) is a known cause of live vs warehouse
    ``pred_mean`` sign flips — refused when below ``MIN_STRUCTURE_HISTORY_BARS``.
    """
    if limit is not None:
        # Hard refuse the historical bug class (800-bar wipe/rebuild).
        blocked = []
        for tf in timeframes:
            min_need = int(MIN_STRUCTURE_HISTORY_BARS.get(tf, 50))
            if int(limit) < min_need:
                blocked.append(
                    {
                        "timeframe": tf,
                        "error": "structure_history_too_short",
                        "n_bars_requested": int(limit),
                        "min_required": min_need,
                        "hint": (
                            "Backtest uses full-history research warehouse swings. "
                            "Live must not truncate; pass limit=None."
                        ),
                    }
                )
        if blocked:
            return {
                "symbol": symbol,
                "db": str(indicator_db),
                "signal_source": source,
                "limit": limit,
                "series": blocked,
                "refreshed_utc": datetime.now(timezone.utc).isoformat(),
            }

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
        "limit": limit,
        "series": [],
    }
    try:
        for tf in timeframes:
            df = fetch_signal_ohlcv(symbol, tf, source=src, limit=limit)
            min_need = int(MIN_STRUCTURE_HISTORY_BARS.get(tf, 50))
            if df.empty or len(df) < 50:
                report["series"].append(
                    {"timeframe": tf, "error": "insufficient bars", "source": src}
                )
                continue
            if len(df) < min_need:
                report["series"].append(
                    {
                        "timeframe": tf,
                        "error": "structure_history_too_short",
                        "source": src,
                        "n_bars": int(len(df)),
                        "min_required": min_need,
                        "hint": (
                            "Refusing truncated structure refresh; would diverge from "
                            "research warehouse swings. Fix shared_candles depth or "
                            "pass limit=None."
                        ),
                    }
                )
                continue
            # Refuse silent depth regression (e.g. REST-only 20k replacing shared 230k+).
            prev = None
            try:
                import sqlite3 as _sqlite3

                con_p = _sqlite3.connect(f"file:{indicator_db}?mode=ro", uri=True)
                try:
                    row_p = con_p.execute(
                        "SELECT n_bars FROM series WHERE symbol=? AND timeframe=? "
                        "AND source=? ORDER BY computed_at_ms DESC LIMIT 1",
                        (symbol.upper(), tf, src),
                    ).fetchone()
                    prev = int(row_p[0]) if row_p and row_p[0] is not None else None
                finally:
                    con_p.close()
            except Exception:  # noqa: BLE001
                prev = None
            if prev is not None and prev >= min_need and int(len(df)) < int(prev * 0.95):
                report["series"].append(
                    {
                        "timeframe": tf,
                        "error": "structure_history_regression",
                        "source": src,
                        "n_bars": int(len(df)),
                        "previous_n_bars": int(prev),
                        "hint": (
                            "Refusing to wipe a deep structure series with a shorter "
                            "Open-High-Low-Close-Volume (OHLCV) window. Merge REST tip "
                            "onto shared history instead of REST-only rebuild."
                        ),
                    }
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


def sync_structure_from_research_warehouse(
    *,
    symbol: str,
    timeframes: tuple[str, ...],
    dest_db: Path,
    source: str = DEFAULT_SIGNAL_SOURCE,
    research_db: Path | None = None,
) -> dict:
    """Copy full-history structure rows from the research warehouse into the live slice.

    This is the strongest live↔backtest parity path when the research file is
    available (local research hosts). Virtual Private Server (VPS) hosts without
    the warehouse should use ``refresh_symbol(limit=None)`` instead.
    """
    import os
    import sqlite3

    src_path = Path(
        research_db
        or os.environ.get("LLM2_RESEARCH_INDICATORS_DB")
        or r"D:\projectsdata\indicators\indicators.sqlite"
    )
    out: dict = {
        "mode": "sync_from_research_warehouse",
        "research_db": str(src_path),
        "dest_db": str(dest_db),
        "symbol": symbol.upper(),
        "source": source,
        "timeframes": list(timeframes),
    }
    if not src_path.is_file():
        out["error"] = "research_warehouse_missing"
        return out
    dest_db.parent.mkdir(parents=True, exist_ok=True)
    # Ensure destination schema exists.
    ind_src = Path("/opt/botsgeneral/packages/indicators/src")
    if ind_src.is_dir() and str(ind_src) not in sys.path:
        sys.path.insert(0, str(ind_src))
    win_src = Path(r"C:\projects\botsgeneral\packages\indicators\src")
    if win_src.is_dir() and str(win_src) not in sys.path:
        sys.path.insert(0, str(win_src))
    from indicators.store import IndicatorDB

    IndicatorDB(dest_db).close()

    con = sqlite3.connect(str(dest_db))
    try:
        con.execute("ATTACH DATABASE ? AS research", (str(src_path),))
        tables = (
            "bar_features",
            "swings",
            "legs",
            "levels",
            "structure_events",
            "series",
        )
        copied: dict[str, int] = {}
        sym = symbol.upper()
        src = (source or DEFAULT_SIGNAL_SOURCE).strip().lower()
        tfs = tuple(str(t) for t in timeframes)
        tf_placeholders = ",".join("?" for _ in tfs)
        for table in tables:
            con.execute(
                f"DELETE FROM {table} WHERE symbol=? AND source=? AND timeframe IN ({tf_placeholders})",
                (sym, src, *tfs),
            )
            cols = [
                r[1]
                for r in con.execute(f"PRAGMA table_info({table})").fetchall()
            ]
            col_csv = ",".join(cols)
            cur = con.execute(
                f"INSERT INTO {table} ({col_csv}) "
                f"SELECT {col_csv} FROM research.{table} "
                f"WHERE symbol=? AND source=? AND timeframe IN ({tf_placeholders})",
                (sym, src, *tfs),
            )
            copied[table] = int(cur.rowcount)
        con.commit()
        out["copied"] = copied
        # Sanity: 1h must have deep history.
        row = con.execute(
            "SELECT COUNT(*), MIN(ts_ms), MAX(ts_ms) FROM bar_features "
            "WHERE symbol=? AND source=? AND timeframe=?",
            (sym, src, tfs[0] if tfs else "1h"),
        ).fetchone()
        out["bar_features_1h"] = {
            "n": int(row[0] or 0),
            "min_ts_ms": row[1],
            "max_ts_ms": row[2],
        }
        min_need = int(MIN_STRUCTURE_HISTORY_BARS.get(tfs[0] if tfs else "1h", 5000))
        if int(row[0] or 0) < min_need:
            out["error"] = "synced_history_too_short"
    finally:
        try:
            con.execute("DETACH DATABASE research")
        except sqlite3.Error:
            pass
        con.close()
    out["synced_utc"] = datetime.now(timezone.utc).isoformat()
    return out


def ensure_live_structure_parity(
    *,
    symbol: str,
    timeframes: tuple[str, ...],
    indicator_db: Path,
    source: str = DEFAULT_SIGNAL_SOURCE,
    bar_open_ms: int | None = None,
) -> dict:
    """Ensure pack slice structure matches backtest full-history geometry.

    Prefer research-warehouse sync when available; otherwise full-history refresh.
    Never uses a truncated Open-High-Low-Close-Volume (OHLCV) window.
    """
    sync = sync_structure_from_research_warehouse(
        symbol=symbol,
        timeframes=timeframes,
        dest_db=indicator_db,
        source=source,
    )
    tip_ok = False
    if not sync.get("error") and bar_open_ms is not None:
        import sqlite3

        con = sqlite3.connect(f"file:{indicator_db}?mode=ro", uri=True)
        try:
            tip_ok = (
                con.execute(
                    "SELECT 1 FROM bar_features WHERE symbol=? AND timeframe=? "
                    "AND source=? AND ts_ms=? LIMIT 1",
                    (symbol.upper(), timeframes[0], source, int(bar_open_ms)),
                ).fetchone()
                is not None
            )
        finally:
            con.close()
        if tip_ok:
            return {"action": "research_sync_tip_present", "sync": sync}
    elif not sync.get("error") and bar_open_ms is None:
        return {"action": "research_sync", "sync": sync}

    # Missing tip or no research warehouse → full-history recompute (never truncate).
    refresh = refresh_symbol(
        symbol=symbol,
        timeframes=timeframes,
        indicator_db=indicator_db,
        limit=None,
        source=source,
    )
    return {
        "action": "full_history_refresh",
        "sync_attempt": sync,
        "refresh": refresh,
    }
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
