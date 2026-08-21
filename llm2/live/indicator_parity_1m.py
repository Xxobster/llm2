"""1-minute indicator parity: live-path slice vs local research indicators.

SHADOW / research diagnostic only. No model training, no orders.
Compares ``bar_features`` on closed Binance USD-M Last 1m tips after both
paths recompute structure from the same deep Open-High-Low-Close-Volume window
(seed once, then recompute to tip — never a short wipe like limit=800).
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from llm2.paths import ARTIFACTS, MARKET_DB, PROJECTSDATA, TF_MS

# Dedicated warehouses so the hunt indicators DB is not thrashed.
DEFAULT_LIVE_SLICE = ARTIFACTS / "indicator_parity_1m" / "live_slice.sqlite"
DEFAULT_RESEARCH_IND = (
    PROJECTSDATA / "indicators" / "indicators_1m_parity.sqlite"
)
DEFAULT_PARITY_LEDGER = ARTIFACTS / "indicator_parity_1m" / "parity.sqlite"
DEFAULT_CANDLES_DB = MARKET_DB

# Refuse truncated structure windows (same bug class as 800-bar 1h wipe).
MIN_1M_STRUCTURE_BARS = 20_000
DEFAULT_SEED_BARS = 25_000
TIMEFRAME = "1m"
SOURCE = "binance"
PRICE_TYPE = "last_price"


@dataclass(frozen=True)
class TipDiff:
    ts_ms: int
    n_cols: int
    n_mismatch: int
    max_abs: float
    identical: bool
    first_mismatches: list[dict[str, Any]]
    tip50_hash_live: str | None
    tip50_hash_research: str | None
    tip50_hash_equal: bool
    live_close: float | None
    research_close: float | None
    ohlc_tip_equal: bool


def _ensure_indicators_on_path() -> None:
    for p in (
        Path(r"C:\projects\botsgeneral\packages\indicators\src"),
        Path("/opt/botsgeneral/packages/indicators/src"),
    ):
        if p.is_dir() and str(p) not in sys.path:
            sys.path.insert(0, str(p))


def _ensure_market_data_on_path() -> None:
    for p in (
        Path(r"C:\projects\botsgeneral\packages\market_data\src"),
        Path("/opt/botsgeneral/packages/market_data/src"),
    ):
        if p.is_dir() and str(p) not in sys.path:
            sys.path.insert(0, str(p))


def refuse_short_structure_limit(limit: int | None, *, min_bars: int = MIN_1M_STRUCTURE_BARS) -> dict | None:
    """Return an error report if limit is set and too short; else None."""
    if limit is None:
        return None
    if int(limit) < int(min_bars):
        return {
            "error": "structure_history_too_short",
            "n_bars_requested": int(limit),
            "min_required": int(min_bars),
            "timeframe": TIMEFRAME,
            "hint": (
                "Do not truncate 1m structure refresh; same bug class as 1h limit=800."
            ),
        }
    return None


def latest_closed_bar_open_ms(
    timeframe: str = TIMEFRAME, *, now_ms: int | None = None
) -> int:
    step = int(TF_MS[timeframe])
    now = int(now_ms if now_ms is not None else time.time() * 1000)
    forming_open = (now // step) * step
    return int(forming_open - step)


def drop_incomplete_ohlcv(df: pd.DataFrame, timeframe: str = TIMEFRAME) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()
    step = int(TF_MS[timeframe])
    now_ms = int(time.time() * 1000)
    out = df.loc[df["ts_ms"].astype("int64") + step <= now_ms].copy()
    return out.sort_values("ts_ms").reset_index(drop=True)


def fetch_binance_last_1m(
    symbol: str,
    *,
    start_ms: int | None = None,
    limit_bars: int | None = None,
) -> pd.DataFrame:
    """Closed Binance USD-M Last 1m via market_data fetcher."""
    _ensure_market_data_on_path()
    from market_data.fetch_binance import drop_incomplete_bars, drop_junk_bars, fetch_klines

    sm = start_ms
    if sm is None and limit_bars is not None:
        step = int(TF_MS[TIMEFRAME])
        sm = int(time.time() * 1000) - int(limit_bars + 5) * step
    df = fetch_klines(
        symbol.upper(),
        TIMEFRAME,
        market="binance",
        price_type="last",
        start_ms=sm,
        include_aux=False,
        drop_incomplete=True,
        drop_junk=True,
    )
    df = drop_junk_bars(drop_incomplete_bars(df, TIMEFRAME))
    if limit_bars is not None and len(df) > int(limit_bars):
        df = df.tail(int(limit_bars)).reset_index(drop=True)
    return df


def upsert_warehouse_ohlcv(
    df: pd.DataFrame,
    *,
    symbol: str,
    candles_db: Path = DEFAULT_CANDLES_DB,
) -> int:
    _ensure_market_data_on_path()
    from market_data.db import ResearchCandleDB

    if df is None or df.empty:
        return 0
    db = ResearchCandleDB(candles_db)
    try:
        return int(
            db.upsert_df(
                df,
                source=SOURCE,
                symbol=symbol.upper(),
                timeframe=TIMEFRAME,
                price_type=PRICE_TYPE,
                product="USDⓈ-M",
                source_endpoint="/fapi/v1/klines",
                is_complete=1,
            )
        )
    finally:
        db.close()


def load_warehouse_1m(
    symbol: str,
    *,
    candles_db: Path = DEFAULT_CANDLES_DB,
    tail: int | None = None,
    end_ms: int | None = None,
) -> pd.DataFrame:
    con = sqlite3.connect(f"file:{candles_db}?mode=ro", uri=True)
    try:
        # pin densest last synonym
        rows_pt = con.execute(
            "SELECT price_type, COUNT(*) AS n FROM market_ohlcv "
            "WHERE symbol=? AND timeframe=? AND source=? "
            "AND (is_complete=1 OR is_complete IS NULL) GROUP BY price_type",
            (symbol.upper(), TIMEFRAME, SOURCE),
        ).fetchall()
        avail = {str(r[0]): int(r[1]) for r in rows_pt}
        # Prefer market_data canonical last_price (densest synonym may be a
        # stale/partial `last` series in the warehouse).
        pt: str | None = None
        for cand in (PRICE_TYPE, "last"):
            if avail.get(cand, 0) > 0:
                pt = cand
                break
        if pt is None:
            return pd.DataFrame()
        # If both exist, use the price_type whose tip is fresher (closed).
        if avail.get(PRICE_TYPE, 0) > 0 and avail.get("last", 0) > 0:
            tips = {}
            for cand in (PRICE_TYPE, "last"):
                row = con.execute(
                    "SELECT MAX(ts_ms) FROM market_ohlcv WHERE symbol=? AND timeframe=? "
                    "AND source=? AND price_type=? AND (is_complete=1 OR is_complete IS NULL)",
                    (symbol.upper(), TIMEFRAME, SOURCE, cand),
                ).fetchone()
                tips[cand] = int(row[0] or 0)
            pt = max(tips, key=tips.get)  # type: ignore[arg-type]
        clauses = [
            "symbol=?",
            "timeframe=?",
            "source=?",
            "price_type=?",
            "(is_complete=1 OR is_complete IS NULL)",
        ]
        params: list[object] = [symbol.upper(), TIMEFRAME, SOURCE, pt]
        if end_ms is not None:
            clauses.append("ts_ms <= ?")
            params.append(int(end_ms))
        sql = (
            f"SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv "
            f"WHERE {' AND '.join(clauses)} ORDER BY ts_ms"
        )
        if tail is not None:
            # load last N via subquery
            sql = (
                "SELECT ts_ms, open, high, low, close, volume FROM ("
                f"SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv "
                f"WHERE {' AND '.join(clauses)} ORDER BY ts_ms DESC LIMIT ?"
                ") ORDER BY ts_ms"
            )
            params.append(int(tail))
        rows = con.execute(sql, params).fetchall()
    finally:
        con.close()
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(
        rows, columns=["ts_ms", "open", "high", "low", "close", "volume"]
    )
    return drop_incomplete_ohlcv(df, TIMEFRAME)


def _ohlcv_for_compute(df: pd.DataFrame) -> pd.DataFrame:
    """Frame shape expected by indicators.compute_structure."""
    out = df.copy()
    if "source" not in out.columns:
        out["source"] = SOURCE
    if out.index.name is None or not isinstance(out.index, pd.DatetimeIndex):
        out.index = pd.to_datetime(out["ts_ms"].astype("int64"), unit="ms", utc=True)
    return out.reset_index(drop=True) if "ts_ms" in out.columns else out


def compute_structure_into(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    indicator_db: Path,
    source: str = SOURCE,
) -> dict[str, Any]:
    """Full-window structure recompute into indicator_db (refuse empty / short)."""
    _ensure_indicators_on_path()
    from indicators.compute import compute_structure
    from indicators.store import IndicatorDB

    if ohlcv is None or ohlcv.empty:
        return {"error": "no_ohlcv", "n_bars": 0}
    n = len(ohlcv)
    if n < MIN_1M_STRUCTURE_BARS:
        return {
            "error": "structure_history_too_short",
            "n_bars": n,
            "min_required": MIN_1M_STRUCTURE_BARS,
        }
    indicator_db.parent.mkdir(parents=True, exist_ok=True)
    df = _ohlcv_for_compute(ohlcv)
    bundle = compute_structure(
        df,
        source=source,
        symbol=symbol.upper(),
        timeframe=TIMEFRAME,
    )
    ind = IndicatorDB(indicator_db)
    try:
        counts = ind.upsert_bundle(bundle)
    finally:
        ind.close()
    last = int(ohlcv["ts_ms"].iloc[-1])
    return {
        "n_bars": n,
        "last_ts_ms": last,
        "last_utc": datetime.fromtimestamp(last / 1000, tz=timezone.utc).isoformat(),
        "counts": counts,
        "db": str(indicator_db),
    }


def ensure_seed(
    *,
    symbol: str,
    seed_bars: int = DEFAULT_SEED_BARS,
    candles_db: Path = DEFAULT_CANDLES_DB,
    live_slice: Path = DEFAULT_LIVE_SLICE,
    research_ind: Path = DEFAULT_RESEARCH_IND,
) -> dict[str, Any]:
    """Fetch/seed warehouse 1m history and materialise both indicator DBs."""
    seed_bars = max(int(seed_bars), MIN_1M_STRUCTURE_BARS)
    fetched = fetch_binance_last_1m(symbol, limit_bars=seed_bars + 10)
    if fetched.empty or len(fetched) < MIN_1M_STRUCTURE_BARS:
        return {
            "error": "insufficient_fetch",
            "n_fetched": 0 if fetched is None else len(fetched),
            "min_required": MIN_1M_STRUCTURE_BARS,
        }
    n_up = upsert_warehouse_ohlcv(fetched, symbol=symbol, candles_db=candles_db)
    ohlcv = load_warehouse_1m(symbol, candles_db=candles_db, tail=seed_bars)
    if len(ohlcv) < MIN_1M_STRUCTURE_BARS:
        return {
            "error": "warehouse_too_short_after_upsert",
            "n_bars": len(ohlcv),
            "upserted": n_up,
        }
    live_rep = compute_structure_into(ohlcv, symbol=symbol, indicator_db=live_slice)
    res_rep = compute_structure_into(ohlcv, symbol=symbol, indicator_db=research_ind)
    return {
        "upserted_candles": n_up,
        "n_ohlcv": len(ohlcv),
        "tip_ts_ms": int(ohlcv["ts_ms"].iloc[-1]),
        "live": live_rep,
        "research": res_rep,
        "seed_ok": "error" not in live_rep and "error" not in res_rep,
    }


def update_research_and_live_tips(
    *,
    symbol: str,
    seed_bars: int = DEFAULT_SEED_BARS,
    candles_db: Path = DEFAULT_CANDLES_DB,
    live_slice: Path = DEFAULT_LIVE_SLICE,
    research_ind: Path = DEFAULT_RESEARCH_IND,
    bar_ts_ms: int | None = None,
) -> dict[str, Any]:
    """Refresh closed tip from fapi, recompute both structure paths on deep window."""
    seed_bars = max(int(seed_bars), MIN_1M_STRUCTURE_BARS)
    # Poll tip window only, merge into warehouse, recompute from tail seed_bars.
    tip_fetch = fetch_binance_last_1m(symbol, limit_bars=min(500, seed_bars))
    if tip_fetch.empty:
        return {"error": "tip_fetch_empty"}
    upsert_warehouse_ohlcv(tip_fetch, symbol=symbol, candles_db=candles_db)
    end = int(bar_ts_ms) if bar_ts_ms is not None else int(tip_fetch["ts_ms"].iloc[-1])
    ohlcv = load_warehouse_1m(
        symbol, candles_db=candles_db, tail=seed_bars, end_ms=end
    )
    if ohlcv.empty or int(ohlcv["ts_ms"].iloc[-1]) != end:
        # ensure tip bar present
        if not ohlcv.empty and int(ohlcv["ts_ms"].iloc[-1]) < end:
            return {
                "error": "tip_bar_missing_in_warehouse",
                "want": end,
                "got": int(ohlcv["ts_ms"].iloc[-1]),
            }
    live_rep = compute_structure_into(ohlcv, symbol=symbol, indicator_db=live_slice)
    res_rep = compute_structure_into(ohlcv, symbol=symbol, indicator_db=research_ind)
    return {
        "bar_ts_ms": end,
        "n_ohlcv": len(ohlcv),
        "ohlc_tip": {
            "open": float(ohlcv["open"].iloc[-1]),
            "high": float(ohlcv["high"].iloc[-1]),
            "low": float(ohlcv["low"].iloc[-1]),
            "close": float(ohlcv["close"].iloc[-1]),
        }
        if len(ohlcv)
        else None,
        "live": live_rep,
        "research": res_rep,
    }


def _load_tip_features(
    ind_db: Path, *, symbol: str, ts_ms: int
) -> dict[str, Any] | None:
    if not ind_db.is_file():
        return None
    con = sqlite3.connect(f"file:{ind_db}?mode=ro", uri=True)
    try:
        cols = [r[1] for r in con.execute("PRAGMA table_info(bar_features)").fetchall()]
        skip = {"symbol", "timeframe", "source", "kind"}
        use = [c for c in cols if c not in skip]
        if "ts_ms" not in use:
            return None
        row = con.execute(
            f"SELECT {','.join(use)} FROM bar_features "
            "WHERE symbol=? AND timeframe=? AND source=? AND ts_ms=?",
            (symbol.upper(), TIMEFRAME, SOURCE, int(ts_ms)),
        ).fetchone()
        if not row:
            return None
        return dict(zip(use, row))
    finally:
        con.close()


def _tip50_ohlc_hash(ind_db: Path, *, symbol: str, end_ts: int) -> str | None:
    if not ind_db.is_file():
        return None
    con = sqlite3.connect(f"file:{ind_db}?mode=ro", uri=True)
    try:
        # bar_features may store close
        cols = [r[1] for r in con.execute("PRAGMA table_info(bar_features)").fetchall()]
        if "close" not in cols:
            return None
        rows = con.execute(
            "SELECT ts_ms, close FROM bar_features "
            "WHERE symbol=? AND timeframe=? AND source=? AND ts_ms<=? "
            "ORDER BY ts_ms DESC LIMIT 50",
            (symbol.upper(), TIMEFRAME, SOURCE, int(end_ts)),
        ).fetchall()
    finally:
        con.close()
    if not rows:
        return None
    rows = list(reversed(rows))
    blob = "".join(f"{int(r[0])}|{float(r[1])}\n" for r in rows).encode()
    return hashlib.sha256(blob).hexdigest()


def diff_tip(
    *,
    symbol: str,
    ts_ms: int,
    live_slice: Path = DEFAULT_LIVE_SLICE,
    research_ind: Path = DEFAULT_RESEARCH_IND,
    abs_eps: float = 1e-9,
) -> TipDiff:
    live = _load_tip_features(live_slice, symbol=symbol, ts_ms=ts_ms)
    research = _load_tip_features(research_ind, symbol=symbol, ts_ms=ts_ms)
    if live is None or research is None:
        return TipDiff(
            ts_ms=int(ts_ms),
            n_cols=0,
            n_mismatch=-1,
            max_abs=float("inf"),
            identical=False,
            first_mismatches=[
                {
                    "error": "missing_tip_row",
                    "live_present": live is not None,
                    "research_present": research is not None,
                }
            ],
            tip50_hash_live=_tip50_ohlc_hash(live_slice, symbol=symbol, end_ts=ts_ms),
            tip50_hash_research=_tip50_ohlc_hash(
                research_ind, symbol=symbol, end_ts=ts_ms
            ),
            tip50_hash_equal=False,
            live_close=None if live is None else live.get("close"),
            research_close=None if research is None else research.get("close"),
            ohlc_tip_equal=False,
        )
    keys = sorted(set(live) & set(research))
    mismatches: list[dict[str, Any]] = []
    max_abs = 0.0
    for k in keys:
        a, b = live.get(k), research.get(k)
        if a is None and b is None:
            continue
        try:
            fa, fb = float(a), float(b)
            d = abs(fa - fb)
            max_abs = max(max_abs, d)
            if d > abs_eps:
                mismatches.append({"col": k, "live": fa, "research": fb, "abs": d})
        except (TypeError, ValueError):
            if a != b:
                mismatches.append({"col": k, "live": a, "research": b})
    h_l = _tip50_ohlc_hash(live_slice, symbol=symbol, end_ts=ts_ms)
    h_r = _tip50_ohlc_hash(research_ind, symbol=symbol, end_ts=ts_ms)
    lc = live.get("close")
    rc = research.get("close")
    try:
        ohlc_eq = abs(float(lc) - float(rc)) <= abs_eps
    except (TypeError, ValueError):
        ohlc_eq = lc == rc
    return TipDiff(
        ts_ms=int(ts_ms),
        n_cols=len(keys),
        n_mismatch=len(mismatches),
        max_abs=float(max_abs),
        identical=len(mismatches) == 0,
        first_mismatches=mismatches[:12],
        tip50_hash_live=h_l,
        tip50_hash_research=h_r,
        tip50_hash_equal=bool(h_l and h_r and h_l == h_r),
        live_close=None if lc is None else float(lc),
        research_close=None if rc is None else float(rc),
        ohlc_tip_equal=bool(ohlc_eq),
    )


def diff_frames_for_test(
    live_row: dict[str, float],
    research_row: dict[str, float],
    *,
    abs_eps: float = 1e-9,
) -> TipDiff:
    """Pure tip-row compare (unit tests; no sqlite)."""
    keys = sorted(set(live_row) & set(research_row))
    mismatches: list[dict[str, Any]] = []
    max_abs = 0.0
    for k in keys:
        fa, fb = float(live_row[k]), float(research_row[k])
        d = abs(fa - fb)
        max_abs = max(max_abs, d)
        if d > abs_eps:
            mismatches.append({"col": k, "live": fa, "research": fb, "abs": d})
    return TipDiff(
        ts_ms=0,
        n_cols=len(keys),
        n_mismatch=len(mismatches),
        max_abs=float(max_abs),
        identical=len(mismatches) == 0,
        first_mismatches=mismatches[:12],
        tip50_hash_live=None,
        tip50_hash_research=None,
        tip50_hash_equal=True,
        live_close=live_row.get("close"),
        research_close=research_row.get("close"),
        ohlc_tip_equal=abs(
            float(live_row.get("close", 0)) - float(research_row.get("close", 0))
        )
        <= abs_eps,
    )


def init_parity_ledger(path: Path = DEFAULT_PARITY_LEDGER) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(path))
    try:
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS parity_runs (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              recorded_utc TEXT NOT NULL,
              symbol TEXT NOT NULL,
              timeframe TEXT NOT NULL,
              bar_ts_ms INTEGER NOT NULL,
              pass INTEGER NOT NULL,
              n_cols INTEGER,
              n_mismatch INTEGER,
              max_abs REAL,
              tip50_equal INTEGER,
              live_close REAL,
              research_close REAL,
              detail_json TEXT
            )
            """
        )
        con.commit()
    finally:
        con.close()


def record_parity(
    diff: TipDiff,
    *,
    symbol: str,
    pass_ok: bool,
    detail: dict[str, Any] | None = None,
    path: Path = DEFAULT_PARITY_LEDGER,
) -> None:
    init_parity_ledger(path)
    con = sqlite3.connect(str(path))
    try:
        con.execute(
            "INSERT INTO parity_runs("
            "recorded_utc, symbol, timeframe, bar_ts_ms, pass, n_cols, n_mismatch, "
            "max_abs, tip50_equal, live_close, research_close, detail_json"
            ") VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                datetime.now(timezone.utc).isoformat(),
                symbol.upper(),
                TIMEFRAME,
                int(diff.ts_ms),
                1 if pass_ok else 0,
                int(diff.n_cols),
                int(diff.n_mismatch),
                float(diff.max_abs) if np.isfinite(diff.max_abs) else None,
                1 if diff.tip50_hash_equal else 0,
                diff.live_close,
                diff.research_close,
                json.dumps(detail or {}, default=str),
            ),
        )
        con.commit()
    finally:
        con.close()


def tip_diff_to_dict(d: TipDiff) -> dict[str, Any]:
    return {
        "ts_ms": d.ts_ms,
        "n_cols": d.n_cols,
        "n_mismatch": d.n_mismatch,
        "max_abs": d.max_abs,
        "identical": d.identical,
        "first_mismatches": d.first_mismatches,
        "tip50_hash_live": d.tip50_hash_live,
        "tip50_hash_research": d.tip50_hash_research,
        "tip50_hash_equal": d.tip50_hash_equal,
        "live_close": d.live_close,
        "research_close": d.research_close,
        "ohlc_tip_equal": d.ohlc_tip_equal,
    }
