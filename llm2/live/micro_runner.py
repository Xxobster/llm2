"""Micro-live / shadow loop for frozen structure_v1 LightGBM pack.

Bar-close schedule (standard 22.1): idle until lead_sec before close, fast-poll,
decide once on the newly closed bar, persist last_processed_bar_ts.

Default mode is SHADOW (log decisions, no orders). LIVE_ORDERS requires certificate
AUTHORIZED + --live-orders flag + account credentials.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import signal
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd

from llm2.gates.evidence import resolve_operational_leverage
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family
from llm2.live.certificate import (
    DEFAULT_CERT,
    PACK_DIR,
    load_certificate,
    pack_fingerprint,
    refuse_vps_deploy_without_live_certificate,
)
from llm2.live.multitrade import decide_entry_gate, parse_multitrade_config
from llm2.live.refresh_structure import DEFAULT_SIGNAL_SOURCE, ensure_live_structure_parity, fetch_signal_ohlcv
from llm2.paths import ROUND_TRIP_COST, TF_MS
from llm2.research_policy import PolicyError
from llm2.sizing_policy import (
    DEFAULT_EQUITY_FRACTION,
    SIZING_MODE_EQUITY_LEVERAGE,
    equity_leverage_notional,
    parse_pack_sizing,
)
from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
from tradesim.sizing import minimum_executable_qty  # noqa: E402
from tradesim.contracts import InstrumentSpec, round_to_step  # noqa: E402

BYBIT_REST = "https://api.bybit.com"
STATE_DB_DEFAULT = "state/micro_live_state.sqlite"
# Vol-normalised structure cols need >= VOL_WINDOW(168) closes; use a wide tip so
# live decide Open-High-Low-Close-Volume matches research warm-up (not a 300-bar stub).
LIVE_SIGNAL_OHLCV_BARS = 2000


def resolve_signal_source(strategy: dict[str, Any] | None = None) -> str:
    """Binance for research-parity features; Bybit remains execution-only."""
    import os

    env = (os.environ.get("LLM2_STRUCTURE_SOURCE") or "").strip().lower()
    if env:
        return env
    if strategy:
        for key in ("signal_source", "structure_source"):
            val = strategy.get(key)
            if val:
                return str(val).strip().lower()
    return DEFAULT_SIGNAL_SOURCE


def _bybit_signed_request(
    *,
    api_key: str,
    api_secret: str,
    method: str,
    path: str,
    body: dict[str, Any] | None = None,
    query: dict[str, str] | None = None,
    recv: str = "5000",
) -> dict[str, Any]:
    """Bybit V5 signed REST. Never logs key/secret."""
    import hashlib
    import hmac
    import time as _time
    import urllib.request

    ts = str(int(_time.time() * 1000))
    if method.upper() == "GET":
        q = urllib.parse.urlencode(query or {})
        sign = hmac.new(
            api_secret.encode(), f"{ts}{api_key}{recv}{q}".encode(), hashlib.sha256
        ).hexdigest()
        req = urllib.request.Request(
            f"{BYBIT_REST}{path}?{q}",
            headers={
                "X-BAPI-API-KEY": api_key,
                "X-BAPI-TIMESTAMP": ts,
                "X-BAPI-RECV-WINDOW": recv,
                "X-BAPI-SIGN": sign,
                "User-Agent": "llm2-micro-live/1.0",
            },
        )
    else:
        payload = json.dumps(body or {}, separators=(",", ":"))
        sign = hmac.new(
            api_secret.encode(),
            f"{ts}{api_key}{recv}{payload}".encode(),
            hashlib.sha256,
        ).hexdigest()
        req = urllib.request.Request(
            f"{BYBIT_REST}{path}",
            data=payload.encode(),
            headers={
                "Content-Type": "application/json",
                "X-BAPI-API-KEY": api_key,
                "X-BAPI-TIMESTAMP": ts,
                "X-BAPI-RECV-WINDOW": recv,
                "X-BAPI-SIGN": sign,
                "User-Agent": "llm2-micro-live/1.0",
            },
            method="POST",
        )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def resolve_pack_leverage(
    strategy: dict[str, Any],
    tiers_doc: dict[str, Any],
    *,
    mark_price: float | None = None,
    qty: float | None = None,
) -> dict[str, float | int]:
    """SL-derived operational leverage with venue-tier cap (research parity)."""
    sl_pct = float(strategy["sl_pct"])
    inst = tiers_doc.get("instrument") or {}
    qty_f = float(qty if qty is not None else inst.get("min_qty") or 0.0)
    px = float(mark_price or 0.0)
    notional = abs(qty_f * px) if px > 0 and qty_f > 0 else 0.0
    return resolve_operational_leverage(
        sl_pct,
        pack_leverage=float(strategy["leverage"]) if strategy.get("leverage") is not None else None,
        notional=notional,
        tiers=list(tiers_doc.get("tiers") or []),
        instrument_max=float(inst["max_leverage"]) if inst.get("max_leverage") is not None else None,
    )


def ensure_exchange_leverage(
    *,
    account: str,
    symbol: str,
    leverage: float,
) -> dict[str, Any]:
    """Set Bybit buy/sell leverage to the SL-derived value. Fail closed on error."""
    api_key, api_secret = _load_account_keys(account)
    lev_str = str(int(leverage)) if float(leverage).is_integer() else f"{float(leverage):.2f}"
    data = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/position/set-leverage",
        body={
            "category": "linear",
            "symbol": symbol.upper(),
            "buyLeverage": lev_str,
            "sellLeverage": lev_str,
        },
    )
    ret = int(data.get("retCode", -1))
    # 110043 = leverage not modified (already at target) — treat as OK.
    if ret not in (0, 110043):
        raise RuntimeError(
            f"set-leverage failed retCode={ret} retMsg={data.get('retMsg')}"
        )
    return data


def ensure_hedge_mode(*, account: str, symbol: str) -> dict[str, Any]:
    """Force Bybit Both-Sides (hedge) mode so Buy=1 / Sell=2 positionIdx works."""
    api_key, api_secret = _load_account_keys(account)
    data = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/position/switch-mode",
        body={
            "category": "linear",
            "symbol": symbol.upper(),
            "mode": 3,  # 3 = Both Sides (hedge); 0 = Merged Single
        },
    )
    ret = int(data.get("retCode", -1))
    # 110025 / 110026 often mean already in requested mode.
    if ret not in (0, 110025, 110026):
        raise RuntimeError(
            f"switch-mode failed retCode={ret} retMsg={data.get('retMsg')}"
        )
    return data


def _get_json(path: str, params: dict[str, str]) -> dict[str, Any]:
    query = urllib.parse.urlencode(params)
    url = f"{BYBIT_REST}{path}?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "llm2-micro-live/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _bybit_retcode(resp: dict[str, Any] | None) -> int:
    """Parse Bybit retCode; treat missing/None as -1. Never use ``x or -1`` (0 is success)."""
    if not resp or "retCode" not in resp or resp["retCode"] is None:
        return -1
    return int(resp["retCode"])


def fetch_ohlcv_rest(symbol: str, interval: str, *, limit: int = 200) -> pd.DataFrame:
    """Public Bybit kline → OHLCV indexed by bar open UTC."""
    # Bybit interval: 60 for 1h
    iv_map = {"1m": "1", "5m": "5", "15m": "15", "1h": "60", "4h": "240", "1d": "D"}
    iv = iv_map.get(interval, interval)
    data = _get_json(
        "/v5/market/kline",
        {
            "category": "linear",
            "symbol": symbol.upper(),
            "interval": iv,
            "limit": str(limit),
        },
    )
    if int(data.get("retCode", -1)) != 0:
        raise RuntimeError(f"kline failed: {data.get('retMsg')}")
    rows = data.get("result", {}).get("list") or []
    # Bybit returns newest first
    rows = list(reversed(rows))
    idx = pd.to_datetime([int(r[0]) for r in rows], unit="ms", utc=True)
    df = pd.DataFrame(
        {
            "open": [float(r[1]) for r in rows],
            "high": [float(r[2]) for r in rows],
            "low": [float(r[3]) for r in rows],
            "close": [float(r[4]) for r in rows],
            "volume": [float(r[5]) for r in rows],
        },
        index=idx,
    )
    return df[~df.index.duplicated(keep="last")].sort_index()


def fetch_mark_last(symbol: str) -> float:
    data = _get_json(
        "/v5/market/tickers",
        {"category": "linear", "symbol": symbol.upper()},
    )
    rows = data.get("result", {}).get("list") or []
    if not rows:
        raise RuntimeError("no ticker")
    return float(rows[0].get("markPrice") or rows[0].get("lastPrice"))


def _state_conn(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(path))
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS state (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS decisions (
            bar_ts_ms INTEGER PRIMARY KEY,
            decided_utc TEXT NOT NULL,
            side INTEGER NOT NULL,
            pred_mean REAL,
            mark REAL,
            mode TEXT NOT NULL,
            detail TEXT
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS open_books (
            book_id TEXT PRIMARY KEY,
            side INTEGER NOT NULL,
            entry_bar_ms INTEGER NOT NULL,
            max_hold_bars INTEGER NOT NULL,
            qty REAL NOT NULL,
            tp_pct REAL NOT NULL,
            sl_pct REAL NOT NULL,
            book_idx INTEGER NOT NULL,
            order_id TEXT,
            status TEXT NOT NULL DEFAULT 'open'
        )
        """
    )
    con.commit()
    return con


def _load_strength_hist(con: sqlite3.Connection) -> list[float]:
    raw = _get_state(con, "strength_hist_json")
    if not raw:
        return []
    try:
        vals = json.loads(raw)
        return [float(x) for x in vals if np.isfinite(float(x))]
    except (TypeError, ValueError, json.JSONDecodeError):
        return []


def _save_strength_hist(
    con: sqlite3.Connection, hist: list[float], *, lookback: int = 168
) -> None:
    trimmed = [float(x) for x in hist[-int(lookback) :]]
    _set_state(con, "strength_hist_json", json.dumps(trimmed))


def _count_open_books(con: sqlite3.Connection, *, side: int) -> int:
    row = con.execute(
        "SELECT COUNT(*) FROM open_books WHERE status='open' AND side=?",
        (int(side),),
    ).fetchone()
    return int(row[0] if row else 0)


def _insert_open_book(
    con: sqlite3.Connection,
    *,
    book_id: str,
    side: int,
    entry_bar_ms: int,
    max_hold_bars: int,
    qty: float,
    tp_pct: float,
    sl_pct: float,
    book_idx: int,
    order_id: str | None,
) -> None:
    con.execute(
        "INSERT OR REPLACE INTO open_books("
        "book_id,side,entry_bar_ms,max_hold_bars,qty,tp_pct,sl_pct,book_idx,order_id,status"
        ") VALUES (?,?,?,?,?,?,?,?,?,'open')",
        (
            book_id,
            int(side),
            int(entry_bar_ms),
            int(max_hold_bars),
            float(qty),
            float(tp_pct),
            float(sl_pct),
            int(book_idx),
            order_id,
        ),
    )
    con.commit()


def _mark_book_closed(con: sqlite3.Connection, book_id: str) -> None:
    con.execute(
        "UPDATE open_books SET status='closed' WHERE book_id=?",
        (book_id,),
    )
    con.commit()


def _expired_books(
    con: sqlite3.Connection, *, bar_ms: int, timeframe: str
) -> list[dict[str, Any]]:
    tf_ms = int(TF_MS[timeframe])
    rows = con.execute(
        "SELECT book_id,side,entry_bar_ms,max_hold_bars,qty FROM open_books "
        "WHERE status='open'"
    ).fetchall()
    out: list[dict[str, Any]] = []
    for book_id, side, entry_ms, hold, qty in rows:
        # Hold counted in closed bars after entry bar open; expire when
        # current closed-bar open >= entry_open + hold * tf.
        deadline = int(entry_ms) + int(hold) * tf_ms
        if int(bar_ms) >= deadline:
            out.append(
                {
                    "book_id": str(book_id),
                    "side": int(side),
                    "qty": float(qty),
                }
            )
    return out


def _reconcile_books_to_exchange(
    con: sqlite3.Connection,
    *,
    account: str,
    symbol: str,
    qty_unit: float,
) -> dict[str, Any]:
    """Drop oldest local books when exchange size is smaller (TP/SL filled).

    Compares summed local book ``qty`` to exchange size so 1×/2× mixes reconcile
    correctly (counting books as equal min-qty units would mis-count size-doubled
    entries).
    """
    sizes = _position_sizes(account=account, symbol=symbol)
    dropped = 0
    tol = max(float(qty_unit) * 0.25, 1e-12)
    for side_name, side_sign in (("Buy", 1), ("Sell", -1)):
        exch = float(sizes.get(side_name, 0.0))
        rows = con.execute(
            "SELECT book_id, qty FROM open_books WHERE status='open' AND side=? "
            "ORDER BY entry_bar_ms ASC, book_id ASC",
            (side_sign,),
        ).fetchall()
        local_sum = sum(float(q) for _, q in rows)
        while rows and local_sum > exch + tol:
            bid, bqty = rows[0]
            _mark_book_closed(con, str(bid))
            local_sum -= float(bqty)
            rows = rows[1:]
            dropped += 1
    return {"dropped": dropped, "sizes": sizes}


def _last_live_entry_bar_ms(con: sqlite3.Connection, *, side: int) -> int | None:
    """Best-effort entry bar from decisions (successful LIVE order, matching side)."""
    rows = con.execute(
        "SELECT bar_ts_ms, side, detail FROM decisions WHERE mode='LIVE' "
        "ORDER BY bar_ts_ms DESC LIMIT 500"
    ).fetchall()
    for bar_ts_ms, dec_side, detail_raw in rows:
        if int(dec_side or 0) != int(side):
            continue
        try:
            detail = json.loads(detail_raw or "{}")
        except Exception:  # noqa: BLE001
            continue
        if "order_retCode" not in detail:
            continue
        if int(detail["order_retCode"]) != 0:
            continue
        if detail.get("skip_reason"):
            continue
        return int(bar_ts_ms)
    return None


def _ensure_single_book_ledger(
    con: sqlite3.Connection,
    *,
    account: str,
    symbol: str,
    bar_ms: int,
    timeframe: str,
    horizon_bars: int,
    tp_pct: float,
    sl_pct: float,
    min_qty: float,
) -> dict[str, Any]:
    """Sync single-book open_books to exchange and restore Full TP/SL if missing.

    If exchange has a position but the local ledger is empty (bots started after the
    fill, or older builds never inserted books), recover entry time from decisions
    when possible; otherwise insert a synthetic overdue book so max-hold can close.
    """
    out: dict[str, Any] = {"synced": [], "ensure_tpsl": []}
    sizes = _position_sizes(account=account, symbol=symbol)
    positions = {
        str(p.get("side") or ""): p
        for p in _position_list(account=account, symbol=symbol)
        if float(p.get("size") or 0) > 0
    }
    tf_ms = int(TF_MS[timeframe])
    hold = max(int(horizon_bars), 1)
    for side_name, side_sign in (("Buy", 1), ("Sell", -1)):
        exch = float(sizes.get(side_name, 0.0))
        n_local = _count_open_books(con, side=side_sign)
        if exch <= 0:
            # Flat on exchange: close any stale local books.
            rows = con.execute(
                "SELECT book_id FROM open_books WHERE status='open' AND side=?",
                (side_sign,),
            ).fetchall()
            for (bid,) in rows:
                _mark_book_closed(con, str(bid))
                out["synced"].append({"side": side_name, "action": "close_stale_local", "book_id": bid})
            continue
        if n_local == 0:
            # Prefer last successful LIVE entry bar from decisions; else overdue so
            # orphan positions past max-hold are force-closed this cycle.
            entry_ms = _last_live_entry_bar_ms(con, side=side_sign)
            action = "insert_from_decisions"
            if entry_ms is None:
                entry_ms = int(bar_ms) - hold * tf_ms
                action = "insert_overdue_book"
            book_id = f"sync_{side_name}_{int(bar_ms)}"
            _insert_open_book(
                con,
                book_id=book_id,
                side=side_sign,
                entry_bar_ms=int(entry_ms),
                max_hold_bars=hold,
                qty=float(exch),
                tp_pct=float(tp_pct),
                sl_pct=float(sl_pct),
                book_idx=1,
                order_id=None,
            )
            out["synced"].append(
                {
                    "side": side_name,
                    "action": action,
                    "book_id": book_id,
                    "qty": float(exch),
                    "entry_bar_ms": int(entry_ms),
                }
            )
        # Ensure Full TP/SL exists on the position (single-book uses trading-stop).
        pos = positions.get(side_name) or {}
        tp = str(pos.get("takeProfit") or "").strip()
        sl = str(pos.get("stopLoss") or "").strip()
        if tp in {"", "0", "0.0"} or sl in {"", "0", "0.0"}:
            avg = float(pos.get("avgPrice") or 0.0)
            if avg > 0:
                try:
                    resp = ensure_full_position_tpsl(
                        account=account,
                        symbol=symbol,
                        side=side_sign,
                        avg_price=avg,
                        tp_pct=float(tp_pct),
                        sl_pct=float(sl_pct),
                    )
                    out["ensure_tpsl"].append(
                        {
                            "side": side_name,
                            "retCode": resp.get("retCode"),
                            "retMsg": resp.get("retMsg"),
                            "avgPrice": avg,
                        }
                    )
                    print(
                        f"ENSURE_TPSL {symbol} {side_name} "
                        f"retCode={resp.get('retCode')} retMsg={resp.get('retMsg')}",
                        flush=True,
                    )
                except Exception as exc:  # noqa: BLE001
                    out["ensure_tpsl"].append(
                        {"side": side_name, "error": f"{type(exc).__name__}: {exc}"}
                    )
    return out


def _get_state(con: sqlite3.Connection, key: str) -> str | None:
    row = con.execute("SELECT value FROM state WHERE key=?", (key,)).fetchone()
    return None if row is None else str(row[0])


def _set_state(con: sqlite3.Connection, key: str, value: str) -> None:
    con.execute(
        "INSERT INTO state(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (key, value),
    )
    con.commit()


def _load_pack(pack_dir: Path) -> dict[str, Any]:
    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    raw = joblib.load(pack_dir / "model.joblib")
    # Accept both research dumps (bare estimator) and live packs ({model, cols}).
    if isinstance(raw, dict) and "model" in raw:
        blob = raw
        if not blob.get("feature_columns") and strategy.get("feature_columns"):
            blob = {**blob, "feature_columns": list(strategy["feature_columns"])}
    else:
        cols = list(strategy.get("feature_columns") or [])
        if not cols:
            raise RuntimeError("model.joblib is bare but strategy.json lacks feature_columns")
        blob = {"model": raw, "feature_columns": cols}
    tiers = json.loads((pack_dir / "risk_tiers.json").read_text(encoding="utf-8"))
    return {"strategy": strategy, "blob": blob, "tiers": tiers}


def _features_from_rest_ohlcv(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str,
    feature_columns: list[str],
    pack_dir: Path | None = None,
) -> pd.DataFrame | None:
    """Use structure warehouse / pack slice; refuse if last closed bar lacks features."""
    import os

    if pack_dir is not None:
        slice_db = pack_dir / "indicators_live_slice.sqlite"
        if slice_db.is_file():
            os.environ["LLM2_INDICATORS_DB"] = str(slice_db.resolve())
    # Research parity: Binance structure rows. Execution venue stays Bybit.
    strat = None
    if pack_dir is not None:
        try:
            strat = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            strat = None
    os.environ["LLM2_STRUCTURE_SOURCE"] = resolve_signal_source(strat)
    try:
        from llm2.data.indicators import clear_indicator_cache
        from llm2.features.registry import build_space

        clear_indicator_cache()
        feats = build_space(
            ohlcv,
            "structure_v1",
            symbol=symbol,
            timeframe=timeframe,
            recent_only=True,
        )
        feats = feats.reindex(columns=feature_columns)
        # Align to last closed bar in ohlcv
        last = ohlcv.index[-1]
        if last not in feats.index:
            # asof: last available feature row at or before last bar
            feats = feats.loc[:last]
        if len(feats) == 0:
            print("FEATURES_EMPTY after align", flush=True)
            return None
        # Stale if feature timestamp lags the closed bar by more than one bar
        lag = (last - feats.index[-1]).total_seconds()
        if lag > TF_MS.get(timeframe, 3_600_000) / 1000.0 + 1:
            print(
                f"FEATURES_STALE last={last} feat_ts={feats.index[-1]} lag_s={lag}",
                flush=True,
            )
            return None
        # Retrace columns used to be NaN on the newest leg and were zero-filled here,
        # because the warehouse only knew a leg's retracement once the *next* leg
        # confirmed. Training dropped those rows, so live was feeding the model a value
        # research never scored — a silent parity break, on top of the look-ahead in
        # the warehouse itself. With CAUS-STRUCT-001 fixed the column is published only
        # once it is knowable and is defined on every bar, so a NaN now means genuinely
        # missing structure: refuse the bar instead of inventing a zero.
        nan_cols = feats.columns[feats.iloc[-1].isna()].tolist()
        if nan_cols:
            print(f"FEATURES_NAN cols={nan_cols[:12]}", flush=True)
            return None
        return feats
    except Exception as exc:  # noqa: BLE001
        print(f"FEATURES_EXC {type(exc).__name__}: {exc}", flush=True)
        return None


def decide_once(
    *,
    pack: dict[str, Any],
    ohlcv: pd.DataFrame,
    pack_dir: Path | None = None,
) -> dict[str, Any]:
    strategy = pack["strategy"]
    blob = pack["blob"]
    model = blob["model"]
    cols = list(blob["feature_columns"])
    feats = _features_from_rest_ohlcv(
        ohlcv,
        symbol=strategy["symbol"],
        timeframe=strategy["timeframe"],
        feature_columns=cols,
        pack_dir=pack_dir,
    )
    if feats is None or len(feats) == 0:
        return {
            "side": 0,
            "pred_mean": None,
            "reason": "features_unavailable_or_nan",
            "bar_ts": ohlcv.index[-1],
        }
    tip = feats.iloc[-1]
    x = tip.to_numpy(dtype=float)
    pred = model.predict(x.reshape(1, -1))
    mean = float(np.asarray(pred.mean if hasattr(pred, "mean") else pred).reshape(-1)[0])
    family = target_family(str(strategy.get("target", "fwd_return")))
    # Research/live gate parity: return targets use fee hurdle; direction uses ±0.10 band.
    default_edge = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    edge = float(strategy.get("min_edge", default_edge))
    if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
        # Refuse silent mis-config that would trade almost every bar.
        edge = DIRECTION_BAND
    side = int(proxy_side(np.asarray([mean], dtype=float), family)[0])
    # Clarity strength history, derived from candles rather than accumulated since
    # process start. Research seeds the quantile from the bars preceding the window;
    # a bot that only remembers bars it happened to be running for gates on a
    # different quantile after every restart, downtime or redeploy. Same rule as the
    # research pre-pass: keep |pred_mean| for prior bars that had a side and cleared
    # the edge, most recent last, current bar excluded.
    strength_hist: list[float] = []
    prior = feats.iloc[:-1]
    if len(prior) > 0:
        prior_pred = model.predict(prior.to_numpy(dtype=float))
        prior_mean = np.asarray(
            prior_pred.mean if hasattr(prior_pred, "mean") else prior_pred,
            dtype=float,
        ).reshape(-1)
        prior_side = proxy_side(prior_mean, family)
        keep = (prior_side != 0) & np.isfinite(prior_mean) & (np.abs(prior_mean) >= edge)
        strength_hist = [float(abs(v)) for v in prior_mean[keep]]
    # Freeze decide-time features for live↔recompute audits (no peeping required).
    feat_vals = {
        str(c): (None if not np.isfinite(float(tip[c])) else float(tip[c])) for c in cols
    }
    raw = np.asarray([feat_vals[c] if feat_vals[c] is not None else 0.0 for c in cols], dtype=np.float64)
    feat_sha = hashlib.sha256(raw.tobytes()).hexdigest()
    return {
        "side": side,
        "pred_mean": mean,
        "reason": "ok",
        "bar_ts": feats.index[-1],
        "edge": edge,
        "target": strategy.get("target"),
        "tp_pct": strategy["tp_pct"],
        "sl_pct": strategy["sl_pct"],
        "strength_hist": strength_hist,
        "feature_snapshot": {
            "columns": cols,
            "values": feat_vals,
            "sha256": feat_sha,
            "n_cols": len(cols),
        },
    }


def _load_account_keys(account: str) -> tuple[str, str]:
    """Resolve API keys from env / secrets.env. Never log values."""
    import os
    import re
    from pathlib import Path

    token = re.sub(r"[^A-Za-z0-9_]", "_", account.strip())
    key = os.environ.get(f"{token}_API_KEY")
    secret = os.environ.get(f"{token}_API_SECRET")
    if key and secret:
        return key, secret
    path = Path(os.environ.get("TRADING_SECRETS_ENV") or (Path.home() / ".trading" / "secrets.env"))
    if path.is_file():
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k.strip() == f"{token}_API_KEY":
                key = v.strip().strip('"').strip("'")
            elif k.strip() == f"{token}_API_SECRET":
                secret = v.strip().strip('"').strip("'")
    if not key or not secret:
        raise RuntimeError(f"credentials missing for account {account!r}")
    return key, secret


def _position_list(*, account: str, symbol: str) -> list[dict[str, Any]]:
    api_key, api_secret = _load_account_keys(account)
    data = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="GET",
        path="/v5/position/list",
        query={"category": "linear", "symbol": symbol.upper()},
        recv="60000",
    )
    return list((data.get("result") or {}).get("list") or [])


def _position_sizes(*, account: str, symbol: str) -> dict[str, float]:
    out: dict[str, float] = {"Buy": 0.0, "Sell": 0.0}
    for p in _position_list(account=account, symbol=symbol):
        size = float(p.get("size") or 0)
        if size <= 0:
            continue
        side = str(p.get("side") or "")
        if side in out:
            out[side] = size
    return out


def _open_position_sides(*, account: str, symbol: str) -> list[str]:
    """Return open side names (Buy/Sell) for symbol; empty if flat."""
    sizes = _position_sizes(account=account, symbol=symbol)
    return [s for s, sz in sizes.items() if sz > 0]


def fetch_wallet_equity_usdt(*, account: str) -> float:
    """Unified USDT equity for sizing (totalWalletBalance, fail closed if missing)."""
    api_key, api_secret = _load_account_keys(account)
    data = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="GET",
        path="/v5/account/wallet-balance",
        query={"accountType": "UNIFIED"},
        recv="60000",
    )
    lst = list((data.get("result") or {}).get("list") or [])
    if not lst:
        raise RuntimeError(f"empty wallet balance for account {account!r}")
    row = lst[0]
    for key in ("totalEquity", "totalWalletBalance", "totalAvailableBalance"):
        val = row.get(key)
        if val is not None and str(val) != "":
            eq = float(val)
            if eq > 0:
                return eq
    # Coin breakdown fallback
    for coin in row.get("coin") or []:
        if str(coin.get("coin") or "").upper() == "USDT":
            for key in ("equity", "walletBalance", "availableToWithdraw"):
                val = coin.get(key)
                if val is not None and str(val) != "":
                    eq = float(val)
                    if eq > 0:
                        return eq
    raise RuntimeError(f"could not parse positive USDT equity for account {account!r}")


def instrument_spec_from_tiers(tiers_doc: dict[str, Any], symbol: str) -> InstrumentSpec:
    inst = tiers_doc.get("instrument") or {}
    return InstrumentSpec(
        symbol=symbol.upper(),
        tick_size=float(inst.get("tick_size") or 0.01),
        qty_step=float(inst.get("qty_step") or inst.get("min_qty") or 0.001),
        min_qty=float(inst.get("min_qty") or 0.001),
        min_notional=float(inst.get("min_notional") or 0.0),
        max_qty=float(inst.get("max_qty") or 1e9),
        max_leverage=float(inst.get("max_leverage") or 100.0),
    )


def resolve_order_qty(
    *,
    sizing: dict[str, Any],
    equity: float | None,
    leverage: float,
    price: float,
    size_mult: float,
    instrument: InstrumentSpec,
    min_qty_fallback: float,
    force_min_exchange: bool = False,
) -> tuple[float, dict[str, Any]]:
    """Base qty from pack sizing policy; mult applies (double-within-window).

    Live bots always use venue minimum per pair (``force_min_exchange=True`` /
    pack MIN_EXCHANGE). ``EQUITY_LEVERAGE_NOTIONAL`` is research-only — if a pack
    claims it under live force, it is forced to min and the detail records that.
    """
    mode = str(sizing.get("mode") or "MIN_EXCHANGE").upper()
    mult = max(float(size_mult), 0.0)
    detail: dict[str, Any] = {
        "sizing_mode": mode,
        "size_mult": mult,
        "equity_fraction": sizing.get("equity_fraction"),
    }
    if force_min_exchange and mode == SIZING_MODE_EQUITY_LEVERAGE:
        detail["live_override"] = "force_MIN_EXCHANGE"
        detail["pack_sizing_ignored"] = mode
        mode = "MIN_EXCHANGE"
        detail["sizing_mode"] = mode

    if mode == SIZING_MODE_EQUITY_LEVERAGE and not force_min_exchange:
        if equity is None or equity <= 0:
            raise RuntimeError("equity_leverage sizing needs positive wallet equity")
        frac = float(sizing.get("equity_fraction") or DEFAULT_EQUITY_FRACTION)
        notional = equity_leverage_notional(
            equity=float(equity),
            equity_fraction=frac,
            leverage=float(leverage),
            size_mult=mult,
        )
        raw = notional / float(price) if price > 0 else 0.0
        qty = float(round_to_step(raw, instrument.qty_step, "floor"))
        detail.update(
            {
                "wallet_equity_usdt": float(equity),
                "target_notional_usdt": float(notional),
                "raw_qty": float(raw),
            }
        )
        if qty < instrument.min_qty - 1e-12 or (
            instrument.min_notional > 0 and qty * price < instrument.min_notional - 1e-12
        ):
            detail["skip_below_venue_min"] = True
            return 0.0, detail
        return qty, detail

    # MIN_EXCHANGE (live default / residual packs)
    base = float(minimum_executable_qty(instrument, price)) if price > 0 else float(min_qty_fallback)
    qty = float(base) * mult
    detail["base_min_qty"] = float(base)
    return qty, detail


def _qty_str(qty: float) -> str:
    qty_str = f"{float(qty):.6f}".rstrip("0").rstrip(".")
    if "." not in qty_str:
        qty_str = f"{qty_str}.0"
    return qty_str


def _list_stop_orders(*, account: str, symbol: str) -> list[dict[str, Any]]:
    """Untriggered stop / partial TP-SL orders for one symbol."""
    api_key, api_secret = _load_account_keys(account)
    data = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="GET",
        path="/v5/order/realtime",
        query={
            "category": "linear",
            "symbol": symbol.upper(),
            "orderFilter": "StopOrder",
            "limit": "50",
        },
        recv="60000",
    )
    return list((data.get("result") or {}).get("list") or [])


def _cancel_order(*, account: str, symbol: str, order_id: str) -> dict[str, Any]:
    api_key, api_secret = _load_account_keys(account)
    return _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/order/cancel",
        body={
            "category": "linear",
            "symbol": symbol.upper(),
            "orderId": str(order_id),
        },
    )


def _prune_partial_stops(
    *,
    account: str,
    symbol: str,
    keep_budget: int = 16,
) -> dict[str, Any]:
    """Cancel oldest Untriggered Partial TP/SL until under Bybit's ~20 bracket cap.

    Bybit rejects new partial brackets with retCode 110061 once tp+sl count exceeds 20.
    """
    stops = _list_stop_orders(account=account, symbol=symbol)
    partials = [
        o
        for o in stops
        if str(o.get("orderStatus") or "") == "Untriggered"
        and "Partial" in str(o.get("stopOrderType") or "")
    ]
    # Oldest first (createdTime ascending).
    partials.sort(key=lambda o: int(o.get("createdTime") or 0))
    cancelled = []
    while len(partials) > int(keep_budget):
        victim = partials.pop(0)
        oid = str(victim.get("orderId") or "")
        if not oid:
            continue
        try:
            resp = _cancel_order(account=account, symbol=symbol, order_id=oid)
            cancelled.append(
                {
                    "orderId": oid,
                    "stopOrderType": victim.get("stopOrderType"),
                    "retCode": resp.get("retCode"),
                }
            )
        except Exception as exc:  # noqa: BLE001
            cancelled.append({"orderId": oid, "error": f"{type(exc).__name__}: {exc}"})
            break
    return {"n_partials_before": len(partials) + len(cancelled), "cancelled": cancelled}


def ensure_full_position_tpsl(
    *,
    account: str,
    symbol: str,
    side: int,
    avg_price: float,
    tp_pct: float,
    sl_pct: float,
) -> dict[str, Any]:
    """Attach Full-mode trading-stop TP/SL to a hedge position (single-book path)."""
    api_key, api_secret = _load_account_keys(account)
    position_idx = 1 if side > 0 else 2
    px = float(avg_price)
    if side > 0:
        take = px * (1.0 + float(tp_pct))
        stop = px * (1.0 - float(sl_pct))
    else:
        take = px * (1.0 - float(tp_pct))
        stop = px * (1.0 + float(sl_pct))
    return _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/position/trading-stop",
        body={
            "category": "linear",
            "symbol": symbol.upper(),
            "takeProfit": f"{take:.2f}",
            "stopLoss": f"{stop:.2f}",
            "tpTriggerBy": "MarkPrice",
            "slTriggerBy": "MarkPrice",
            "tpslMode": "Full",
            "positionIdx": position_idx,
        },
    )


def place_min_order(
    *,
    account: str,
    symbol: str,
    side: int,
    qty: float,
    tp_pct: float,
    sl_pct: float,
    leverage: float,
    partial_tpsl: bool = False,
) -> dict[str, Any]:
    """Place market entry + attach TP/SL via Bybit V5. Never logs secrets.

    ``partial_tpsl=True`` (multitrade): attach take-profit / stop-loss to this order
    fill only so concurrent books keep independent brackets. ``False`` (single-book):
    set full-position trading-stop after fill (legacy path).

    Fail closed: if protection cannot be attached after entry, reduce-only close the fill.
    """
    api_key, api_secret = _load_account_keys(account)
    last = fetch_mark_last(symbol)
    mode_resp = ensure_hedge_mode(account=account, symbol=symbol)
    lev_resp = ensure_exchange_leverage(
        account=account, symbol=symbol, leverage=float(leverage)
    )
    qty_str = _qty_str(qty)
    # Hedge-mode: Buy→positionIdx 1, Sell→positionIdx 2.
    position_idx = 1 if side > 0 else 2
    if side > 0:
        take = last * (1.0 + float(tp_pct))
        stop = last * (1.0 - float(sl_pct))
    else:
        take = last * (1.0 - float(tp_pct))
        stop = last * (1.0 + float(sl_pct))
    body: dict[str, Any] = {
        "category": "linear",
        "symbol": symbol.upper(),
        "side": "Buy" if side > 0 else "Sell",
        "orderType": "Market",
        "qty": qty_str,
        "positionIdx": position_idx,
    }
    prune_info: dict[str, Any] | None = None
    stops: dict[str, Any] = {}
    if partial_tpsl:
        # Free bracket slots before attach (Bybit hard cap ≈ 20 tp+sl).
        try:
            prune_info = _prune_partial_stops(account=account, symbol=symbol, keep_budget=16)
        except Exception as exc:  # noqa: BLE001
            prune_info = {"error": f"{type(exc).__name__}: {exc}"}
        body.update(
            {
                "takeProfit": f"{take:.2f}",
                "stopLoss": f"{stop:.2f}",
                "tpTriggerBy": "MarkPrice",
                "slTriggerBy": "MarkPrice",
                "tpslMode": "Partial",
                "tpOrderType": "Market",
                "slOrderType": "Market",
            }
        )
        order = _bybit_signed_request(
            api_key=api_key,
            api_secret=api_secret,
            method="POST",
            path="/v5/order/create",
            body=body,
        )
        # Retry once after prune if bracket cap hit.
        if _bybit_retcode(order) == 110061:
            try:
                prune_info = {
                    **(prune_info or {}),
                    "retry_prune": _prune_partial_stops(
                        account=account, symbol=symbol, keep_budget=14
                    ),
                }
            except Exception as exc:  # noqa: BLE001
                prune_info = {**(prune_info or {}), "retry_prune_error": str(exc)}
            order = _bybit_signed_request(
                api_key=api_key,
                api_secret=api_secret,
                method="POST",
                path="/v5/order/create",
                body=body,
            )
        stops = {"mode": "partial_on_order", "take": take, "stop": stop, "order_ret": order}
        # Entry accepted but bracket missing → fail closed (flatten this fill).
        if _bybit_retcode(order) == 0:
            # Partial brackets are on the order; retCode 0 means they were accepted.
            pass
        elif _bybit_retcode(order) == 110061:
            # No fill when create fails with 110061 typically — still attempt flatten if size rose.
            try:
                close_reduce_only(account=account, symbol=symbol, side=side, qty=float(qty))
            except Exception:  # noqa: BLE001
                pass
    else:
        order = _bybit_signed_request(
            api_key=api_key,
            api_secret=api_secret,
            method="POST",
            path="/v5/order/create",
            body=body,
        )
        if _bybit_retcode(order) == 0:
            stops = _bybit_signed_request(
                api_key=api_key,
                api_secret=api_secret,
                method="POST",
                path="/v5/position/trading-stop",
                body={
                    "category": "linear",
                    "symbol": symbol.upper(),
                    "takeProfit": f"{take:.2f}",
                    "stopLoss": f"{stop:.2f}",
                    "tpTriggerBy": "MarkPrice",
                    "slTriggerBy": "MarkPrice",
                    "tpslMode": "Full",
                    "positionIdx": position_idx,
                },
            )
            stops = {
                **stops,
                "mode": "full_trading_stop",
                "take": take,
                "stop": stop,
            }
            if _bybit_retcode(stops) != 0:
                # Protection missing after fill — flatten immediately.
                try:
                    flat = close_reduce_only(
                        account=account, symbol=symbol, side=side, qty=float(qty)
                    )
                except Exception as exc:  # noqa: BLE001
                    flat = {"error": f"{type(exc).__name__}: {exc}"}
                stops = {
                    **stops,
                    "fail_closed_flatten": flat,
                    "take": take,
                    "stop": stop,
                }
        else:
            stops = {"mode": "full_trading_stop_skipped", "order_retCode": order.get("retCode")}
    return {
        "order": order,
        "stops": stops,
        "ref_mark": last,
        "leverage": float(leverage),
        "leverage_set": lev_resp,
        "mode_set": mode_resp,
        "partial_tpsl": bool(partial_tpsl),
        "tp_pct": float(tp_pct),
        "sl_pct": float(sl_pct),
        "prune": prune_info,
    }


def close_reduce_only(
    *,
    account: str,
    symbol: str,
    side: int,
    qty: float,
) -> dict[str, Any]:
    """Market reduce-only close for one book qty (max-hold exit)."""
    api_key, api_secret = _load_account_keys(account)
    position_idx = 1 if side > 0 else 2
    # Closing a long = Sell; closing a short = Buy.
    close_side = "Sell" if side > 0 else "Buy"
    body = {
        "category": "linear",
        "symbol": symbol.upper(),
        "side": close_side,
        "orderType": "Market",
        "qty": _qty_str(qty),
        "positionIdx": position_idx,
        "reduceOnly": True,
    }
    return _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/order/create",
        body=body,
    )


def flatten_symbol_on_shutdown(
    *,
    account: str,
    symbol: str,
    state_con: sqlite3.Connection | None = None,
) -> dict[str, Any]:
    """Cancel conditional orders and close every open position for ``symbol``.

    Stopping the runner used to abandon max-hold exits (those live in-process, not on
    the exchange). A LIVE unit must therefore flatten on SIGTERM/SIGINT so "stop the
    bot" never means "leave unprotected leverage open".
    """
    sym = symbol.upper()
    report: dict[str, Any] = {"symbol": sym, "cancels": [], "closes": []}
    # Cancel stop / partial TP-SL first so nothing races a close.
    try:
        for o in _list_stop_orders(account=account, symbol=sym):
            oid = str(o.get("orderId") or "")
            if not oid:
                continue
            try:
                resp = _cancel_order(account=account, symbol=sym, order_id=oid)
                report["cancels"].append(
                    {"orderId": oid, "retCode": resp.get("retCode"), "retMsg": resp.get("retMsg")}
                )
            except Exception as exc:  # noqa: BLE001
                report["cancels"].append({"orderId": oid, "error": f"{type(exc).__name__}: {exc}"})
    except Exception as exc:  # noqa: BLE001
        report["cancel_list_error"] = f"{type(exc).__name__}: {exc}"

    try:
        positions = _position_list(account=account, symbol=sym)
    except Exception as exc:  # noqa: BLE001
        report["position_list_error"] = f"{type(exc).__name__}: {exc}"
        positions = []
    for p in positions:
        size = float(p.get("size") or 0)
        if size <= 0:
            continue
        side_s = str(p.get("side") or "")
        side_i = 1 if side_s == "Buy" else -1
        try:
            resp = close_reduce_only(account=account, symbol=sym, side=side_i, qty=size)
            report["closes"].append(
                {
                    "side": side_s,
                    "size": size,
                    "retCode": resp.get("retCode"),
                    "retMsg": resp.get("retMsg"),
                }
            )
        except Exception as exc:  # noqa: BLE001
            report["closes"].append(
                {"side": side_s, "size": size, "error": f"{type(exc).__name__}: {exc}"}
            )

    if state_con is not None:
        try:
            state_con.execute(
                "UPDATE open_books SET status='closed' WHERE status='open'"
            )
            state_con.commit()
            report["books_marked_closed"] = True
        except Exception as exc:  # noqa: BLE001
            report["books_mark_error"] = f"{type(exc).__name__}: {exc}"
    return report


def sleep_until_next_close(
    timeframe: str,
    *,
    lead_sec: float = 5.0,
    abort_check: Any | None = None,
    slice_sec: float = 1.0,
) -> None:
    """Idle until ``lead_sec`` before the next bar close.

    ``abort_check`` is an optional zero-arg callable; when it returns true the sleep
    ends early so a SIGTERM flatten can run without waiting out the whole bar.
    """
    tf_ms = TF_MS[timeframe]
    now_ms = int(time.time() * 1000)
    next_close = ((now_ms // tf_ms) + 1) * tf_ms
    deadline = (next_close / 1000.0) - lead_sec
    while True:
        if abort_check is not None and abort_check():
            return
        remaining = deadline - time.time()
        if remaining <= 0:
            return
        time.sleep(min(float(slice_sec), remaining))


def latest_closed_bar_open_ms(timeframe: str, *, now_ms: int | None = None) -> int:
    """Open timestamp (ms) of the latest fully closed bar."""
    tf_ms = int(TF_MS[timeframe])
    now = int(now_ms if now_ms is not None else time.time() * 1000)
    forming_open = (now // tf_ms) * tf_ms
    return int(forming_open - tf_ms)


def _slice_has_closed_bar(
    slice_db: Path,
    *,
    symbol: str,
    timeframe: str,
    bar_open_ms: int,
    source: str = DEFAULT_SIGNAL_SOURCE,
) -> bool:
    """True when the live slice already holds features for this closed bar open."""
    if not slice_db.is_file():
        return False
    con = sqlite3.connect(f"file:{slice_db}?mode=ro", uri=True, timeout=5.0)
    try:
        row = con.execute(
            "SELECT 1 FROM bar_features WHERE symbol = ? AND timeframe = ? "
            "AND source = ? AND ts_ms = ? LIMIT 1",
            (symbol.upper(), timeframe, source, int(bar_open_ms)),
        ).fetchone()
        return row is not None
    except sqlite3.Error:
        return False
    finally:
        con.close()


def _slice_structure_deep_enough(
    slice_db: Path,
    *,
    symbol: str,
    timeframe: str,
    source: str = DEFAULT_SIGNAL_SOURCE,
    min_bars: int | None = None,
    require_htf: bool = True,
) -> bool:
    """False when series was built from a truncated window (live↔BT divergence risk).

    For decision TFs that join higher-timeframe structure (e.g. 15m→1h/4h), also
    require those HTF series to exist at minimum depth — otherwise skip-tip leaves
    NaN HTF columns and blocks every decide.
    """
    from llm2.features.structure_v1 import HIGHER_TIMEFRAMES
    from llm2.live.refresh_structure import MIN_STRUCTURE_HISTORY_BARS

    need = int(min_bars if min_bars is not None else MIN_STRUCTURE_HISTORY_BARS.get(timeframe, 50))
    if not slice_db.is_file():
        return False
    check_tfs = [str(timeframe)]
    if require_htf:
        check_tfs.extend(str(t) for t in HIGHER_TIMEFRAMES.get(str(timeframe), ()))
    con = sqlite3.connect(f"file:{slice_db}?mode=ro", uri=True, timeout=5.0)
    try:
        for tf in check_tfs:
            need_tf = int(MIN_STRUCTURE_HISTORY_BARS.get(tf, need if tf == timeframe else 50))
            row = con.execute(
                "SELECT n_bars FROM series WHERE symbol=? AND timeframe=? AND source=? "
                "ORDER BY computed_at_ms DESC LIMIT 1",
                (symbol.upper(), tf, source),
            ).fetchone()
            if row is None or int(row[0] or 0) < need_tf:
                return False
        return True
    except sqlite3.Error:
        return False
    finally:
        con.close()


def _required_completed_htf_open_ms(bar_open_ms: int, htf: str) -> int:
    """Last higher-timeframe bar open visible to a decision bar stamped ``bar_open_ms``.

    ``align_multi_timeframe`` shifts HTF rows by one HTF step (completion), then
    as-of joins onto the decision open. So a 15m bar at 14:15 only sees the 1h
    bar that opened at 13:00.
    """
    step_h = int(TF_MS[str(htf)])
    floored = (int(bar_open_ms) // step_h) * step_h
    return int(floored - step_h)


def _slice_htf_tips_cover_bar(
    slice_db: Path,
    *,
    symbol: str,
    timeframe: str,
    bar_open_ms: int,
    source: str = DEFAULT_SIGNAL_SOURCE,
) -> bool:
    """True when each joined HTF has bar_features through the required completed open."""
    from llm2.features.structure_v1 import HIGHER_TIMEFRAMES

    htfs = tuple(str(t) for t in HIGHER_TIMEFRAMES.get(str(timeframe), ()))
    if not htfs:
        return True
    if not slice_db.is_file():
        return False
    con = sqlite3.connect(f"file:{slice_db}?mode=ro", uri=True, timeout=5.0)
    try:
        for htf in htfs:
            need_ts = _required_completed_htf_open_ms(int(bar_open_ms), htf)
            if need_ts < 0:
                return False
            row = con.execute(
                "SELECT MAX(ts_ms) FROM bar_features WHERE symbol=? AND timeframe=? "
                "AND source=?",
                (symbol.upper(), htf, source),
            ).fetchone()
            tip = int(row[0] or 0) if row and row[0] is not None else 0
            if tip < need_ts:
                return False
        return True
    except sqlite3.Error:
        return False
    finally:
        con.close()


def _timeframes_needing_structure_refresh(
    slice_db: Path,
    *,
    symbol: str,
    timeframe: str,
    bar_open_ms: int,
    source: str = DEFAULT_SIGNAL_SOURCE,
) -> tuple[str, ...]:
    """Which structure TFs must be recomputed for this decision bar.

    When the pack slice is already deep, only recompute series whose tip no longer
    covers the decision (decision TF) or the HTF completion-join requirement.
    This avoids a ~7min full 15m+1h+4h rebuild every 15m when only the 15m tip
    advanced; 1h/4h are skipped until their completed bars are actually required.
    """
    from llm2.features.structure_v1 import HIGHER_TIMEFRAMES
    from llm2.live.refresh_structure import MIN_STRUCTURE_HISTORY_BARS

    decision_tf = str(timeframe)
    htf = tuple(str(t) for t in HIGHER_TIMEFRAMES.get(decision_tf, ()))
    all_tfs = (decision_tf, *htf)
    if not slice_db.is_file() or not _slice_structure_deep_enough(
        slice_db,
        symbol=symbol,
        timeframe=decision_tf,
        source=source,
        require_htf=True,
    ):
        return all_tfs

    need: list[str] = []
    con = sqlite3.connect(f"file:{slice_db}?mode=ro", uri=True, timeout=5.0)
    try:
        # Decision TF always needs its own bar row.
        tip_d = con.execute(
            "SELECT MAX(ts_ms) FROM bar_features WHERE symbol=? AND timeframe=? "
            "AND source=?",
            (symbol.upper(), decision_tf, source),
        ).fetchone()
        tip_d_ms = int(tip_d[0] or 0) if tip_d and tip_d[0] is not None else 0
        if tip_d_ms < int(bar_open_ms):
            need.append(decision_tf)
        for tf in htf:
            need_ts = _required_completed_htf_open_ms(int(bar_open_ms), tf)
            tip = con.execute(
                "SELECT MAX(ts_ms) FROM bar_features WHERE symbol=? AND timeframe=? "
                "AND source=?",
                (symbol.upper(), tf, source),
            ).fetchone()
            tip_ms = int(tip[0] or 0) if tip and tip[0] is not None else 0
            # Also force refresh if series depth marker is missing (schema churn).
            n_row = con.execute(
                "SELECT n_bars FROM series WHERE symbol=? AND timeframe=? AND source=? "
                "ORDER BY computed_at_ms DESC LIMIT 1",
                (symbol.upper(), tf, source),
            ).fetchone()
            need_n = int(MIN_STRUCTURE_HISTORY_BARS.get(tf, 50))
            if n_row is None or int(n_row[0] or 0) < need_n or tip_ms < need_ts:
                need.append(tf)
    except sqlite3.Error:
        return all_tfs
    finally:
        con.close()
    # Preserve stable order: decision first, then HTF declaration order.
    order = {tf: i for i, tf in enumerate(all_tfs)}
    return tuple(sorted(set(need), key=lambda t: order.get(t, 99)))


def _structure_ready_for_decide(
    slice_db: Path,
    *,
    symbol: str,
    timeframe: str,
    bar_open_ms: int,
    source: str = DEFAULT_SIGNAL_SOURCE,
    refresh_errors: list[dict[str, Any]] | None = None,
) -> tuple[bool, str]:
    """Fail-closed gate: refuse decide on truncated / incomplete / mid-refresh structure.

    Historical bug: ``STRUCTURE_REFRESH_BLOCKED`` still fell through to ``decide_once``,
    so live ``pred_mean`` was computed on a partial slice; a later full-history rebuild
    made pack tip match research while early feature_snapshots stayed wrong forever.
    """
    if refresh_errors:
        return False, "structure_refresh_errors"
    if not slice_db.is_file():
        return False, "slice_missing"
    if not _slice_structure_deep_enough(
        slice_db,
        symbol=symbol,
        timeframe=timeframe,
        source=source,
        require_htf=True,
    ):
        return False, "structure_depth_insufficient"
    if not _slice_has_closed_bar(
        slice_db,
        symbol=symbol,
        timeframe=timeframe,
        bar_open_ms=int(bar_open_ms),
        source=source,
    ):
        return False, "decision_bar_missing_in_slice"
    if not _slice_htf_tips_cover_bar(
        slice_db,
        symbol=symbol,
        timeframe=timeframe,
        bar_open_ms=int(bar_open_ms),
        source=source,
    ):
        return False, "htf_tip_stale_or_incomplete"
    return True, "ok"


def run_loop(
    *,
    pack_dir: Path,
    state_path: Path,
    mode: str,
    account: str,
    lead_sec: float = 5.0,
    close_poll_sec: float = 2.0,
    confirm_timeout_sec: float = 120.0,
    once: bool = False,
    force_now: bool = False,
) -> int:
    pack = _load_pack(pack_dir)
    strategy = pack["strategy"]
    symbol = strategy["symbol"]
    timeframe = strategy["timeframe"]
    mt_cfg = parse_multitrade_config(strategy)
    signal_source = resolve_signal_source(strategy)
    tiers_doc = json.loads((pack_dir / "risk_tiers.json").read_text(encoding="utf-8"))
    min_qty = float(tiers_doc.get("instrument", {}).get("min_qty", 0.001))
    sizing_cfg = parse_pack_sizing(strategy)
    instrument = instrument_spec_from_tiers(tiers_doc, symbol)
    mark0 = fetch_mark_last(symbol)
    lev_info = resolve_pack_leverage(
        strategy, tiers_doc, mark_price=mark0, qty=min_qty
    )
    leverage = float(lev_info["leverage"])
    con = _state_conn(state_path)
    exec_label = (
        f"multitrade/{mt_cfg.get('version_id')} K={mt_cfg['max_positions_per_side']} "
        f"clarity={mt_cfg['clarity']} clarity_scope={mt_cfg.get('clarity_scope', 'addon')} "
        f"fib_ext={mt_cfg['fib_ext']} hold_addon={mt_cfg['hold_addon']}"
        if mt_cfg
        else "single_book"
    )
    print(
        f"micro_runner mode={mode} symbol={symbol} tf={timeframe} "
        f"sizing=MIN_EXCHANGE (live always min qty/pair; pack_declared={sizing_cfg['mode']}) "
        f"min_qty_ref={min_qty} signal_source={signal_source} execution_venue=bybit "
        f"execution={exec_label} leverage={leverage} (sl={lev_info['sl_pct']} "
        f"ceiling={lev_info['ceiling']} haircut={lev_info['haircut']} "
        f"mm={lev_info['mm_buffer']} mark_buf={lev_info['mark_buffer']}) "
        f"tiers={pack['tiers'].get('n_tiers')} pack={pack_dir}",
        flush=True,
    )
    if mode == "LIVE":
        try:
            mode_resp = ensure_hedge_mode(account=account, symbol=symbol)
            print(
                f"MODE_SET symbol={symbol} hedge "
                f"retCode={mode_resp.get('retCode')} retMsg={mode_resp.get('retMsg')}",
                flush=True,
            )
            lev_resp = ensure_exchange_leverage(
                account=account, symbol=symbol, leverage=leverage
            )
            print(
                f"LEVERAGE_SET symbol={symbol} leverage={leverage} "
                f"retCode={lev_resp.get('retCode')} retMsg={lev_resp.get('retMsg')}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"MODE_OR_LEVERAGE_FAIL {type(exc).__name__}: {exc}", flush=True)
            return 6

    shutdown_requested = {"flag": False}

    def _request_shutdown(signum: int, _frame: Any) -> None:
        shutdown_requested["flag"] = True
        print(f"SHUTDOWN_SIGNAL signum={signum} — flatten then exit", flush=True)

    # SIGTERM is what systemd sends on `systemctl stop`. Without a flatten hook,
    # max-hold exits die with the process while exchange positions remain.
    for sig in (signal.SIGTERM, signal.SIGINT):
        try:
            signal.signal(sig, _request_shutdown)
        except Exception:  # noqa: BLE001
            pass

    while True:
        if shutdown_requested["flag"]:
            if mode == "LIVE":
                flat = flatten_symbol_on_shutdown(
                    account=account, symbol=symbol, state_con=con
                )
                print(f"SHUTDOWN_FLATTEN {json.dumps(flat, default=str)}", flush=True)
            return 0
        skip_schedule = bool(force_now)
        force_now = False
        if not skip_schedule:
            # Startup / mid-hour catch-up: never sleep past an unprocessed closed bar.
            last_ms = _get_state(con, "last_processed_bar_ts")
            latest_closed = latest_closed_bar_open_ms(timeframe)
            if last_ms is None or int(last_ms) < int(latest_closed):
                skip_schedule = True
                print(
                    f"CATCH_UP last_processed={last_ms} latest_closed={latest_closed}",
                    flush=True,
                )
            else:
                sleep_until_next_close(
                    timeframe,
                    lead_sec=lead_sec,
                    abort_check=lambda: shutdown_requested["flag"],
                )
                if shutdown_requested["flag"]:
                    continue
        deadline = time.time() + (5.0 if skip_schedule else confirm_timeout_sec)
        closed_bar = None
        ohlcv_closed = None
        while time.time() < deadline:
            # Signal candles = Binance (research parity). Orders still use Bybit.
            ohlcv = fetch_signal_ohlcv(
                symbol, timeframe, source=signal_source, limit=LIVE_SIGNAL_OHLCV_BARS
            )
            if len(ohlcv) < 2:
                time.sleep(close_poll_sec)
                continue
            # fetch_signal_ohlcv already drops the forming bar.
            last_ms = _get_state(con, "last_processed_bar_ts")
            # Catch-up must be chronological: process the earliest unprocessed closed bar,
            # not jump to the tip (that would skip intermediate hours after a restart).
            if last_ms is not None:
                pending = ohlcv.loc[ohlcv["ts_ms"].astype("int64") > int(last_ms)]
                if pending.empty:
                    if not skip_schedule:
                        time.sleep(close_poll_sec)
                        continue
                    # force/catch-up with nothing pending — fall through to tip only if newer
                    candidate = ohlcv.index[-1]
                    cand_ms = str(int(candidate.value // 1_000_000))
                    if cand_ms <= str(last_ms):
                        time.sleep(close_poll_sec)
                        continue
                    closed_bar = candidate
                    ohlcv_closed = ohlcv
                    break
                candidate = pending.index[0]
                ohlcv_closed = ohlcv.loc[:candidate]
                closed_bar = candidate
                break
            candidate = ohlcv.index[-1]
            closed_bar = candidate
            ohlcv_closed = ohlcv
            break
        if closed_bar is None or ohlcv_closed is None:
            print("STALE_BAR: no new closed bar within confirm_timeout", flush=True)
            if once:
                return 3
            continue

        # LIVE-DATA-001: exchange-server tip freshness + shared DATA_UNSAFE flag.
        try:
            from llm2.live.candle_freshness import LIVE_DATA_001, signal_entry_gate

            tip_ms = int(pd.Timestamp(closed_bar).value // 1_000_000)
            allow_data, tip_res, flagged = signal_entry_gate(
                symbol=symbol,
                timeframe=timeframe,
                local_tip_ms=tip_ms,
                persist_flag=True,
            )
            if not allow_data:
                print(
                    f"DATA_UNSAFE {LIVE_DATA_001} code={tip_res.code} "
                    f"tip={tip_res.to_dict()} flagged={flagged} "
                    f"— refuse new entries; protective exits untouched",
                    flush=True,
                )
                if once:
                    return 5
                time.sleep(max(float(close_poll_sec), 5.0))
                continue
        except Exception as exc:  # noqa: BLE001
            print(
                f"LIVE_DATA_001_WARN {type(exc).__name__}: {exc} — refuse decide (fail closed)",
                flush=True,
            )
            if once:
                return 5
            time.sleep(max(float(close_poll_sec), 5.0))
            continue

        # Refresh structure into pack slice with BACKTEST parity (full history).
        # Never truncate (limit=800 wipe/rebuild flipped live pred vs warehouse).
        t_path = time.perf_counter()
        refresh_ms = 0.0
        refresh_skipped = False
        refresh_errors: list[dict[str, Any]] = []
        slice_db = pack_dir / "indicators_live_slice.sqlite"
        bar_open_ms = int(pd.Timestamp(closed_bar).value // 1_000_000)
        try:
            from llm2.data.indicators import clear_indicator_cache

            if (
                slice_db.is_file()
                and _slice_structure_deep_enough(
                    slice_db,
                    symbol=symbol,
                    timeframe=timeframe,
                    source=signal_source,
                )
                and _slice_has_closed_bar(
                    slice_db,
                    symbol=symbol,
                    timeframe=timeframe,
                    bar_open_ms=bar_open_ms,
                    source=signal_source,
                )
                and _slice_htf_tips_cover_bar(
                    slice_db,
                    symbol=symbol,
                    timeframe=timeframe,
                    bar_open_ms=bar_open_ms,
                    source=signal_source,
                )
            ):
                refresh_skipped = True
                clear_indicator_cache()
                # Still emit depth so logs prove full-history parity (not truncated).
                try:
                    con_d = sqlite3.connect(f"file:{slice_db}?mode=ro", uri=True)
                    n_bars = con_d.execute(
                        "SELECT n_bars FROM series WHERE symbol=? AND timeframe=? "
                        "AND source=? ORDER BY computed_at_ms DESC LIMIT 1",
                        (symbol.upper(), timeframe, signal_source),
                    ).fetchone()
                    con_d.close()
                    print(
                        f"STRUCTURE_PARITY action=skip_tip_present "
                        f"{timeframe}={int(n_bars[0]) if n_bars else -1}",
                        flush=True,
                    )
                except Exception:  # noqa: BLE001
                    pass
            else:
                t0 = time.perf_counter()
                from llm2.features.structure_v1 import HIGHER_TIMEFRAMES

                htf = tuple(HIGHER_TIMEFRAMES.get(str(timeframe), ("4h", "1w")))
                all_tfs = (str(timeframe), *htf)
                need_tfs = _timeframes_needing_structure_refresh(
                    slice_db,
                    symbol=symbol,
                    timeframe=timeframe,
                    bar_open_ms=bar_open_ms,
                    source=signal_source,
                )
                if not need_tfs:
                    # Depth/tip checks raced; fall through to full set to stay fail-closed.
                    need_tfs = all_tfs
                parity = ensure_live_structure_parity(
                    symbol=symbol,
                    timeframes=need_tfs,
                    indicator_db=slice_db,
                    source=signal_source,
                    bar_open_ms=bar_open_ms,
                )
                refresh_ms = (time.perf_counter() - t0) * 1000.0
                clear_indicator_cache()
                refresh_rep = parity.get("refresh") or parity.get("sync") or parity
                refresh_errors = [
                    s
                    for s in (refresh_rep.get("series") or [])
                    if isinstance(s, dict) and s.get("error")
                ]
                if parity.get("sync_attempt", {}).get("error") and parity.get("action") == "full_history_refresh":
                    # Expected on VPS without research warehouse.
                    pass
                if refresh_errors:
                    print(f"STRUCTURE_REFRESH_BLOCKED {refresh_errors}", flush=True)
                else:
                    n_info = ""
                    if parity.get("action") == "full_history_refresh":
                        n_info = ",".join(
                            f"{s.get('timeframe')}={s.get('n_bars')}"
                            for s in (refresh_rep.get("series") or [])
                            if isinstance(s, dict)
                        )
                    elif parity.get("sync"):
                        bf = (parity.get("sync") or {}).get("bar_features_1h") or {}
                        n_info = f"synced_1h={bf.get('n')}"
                    skipped = [t for t in all_tfs if t not in need_tfs]
                    skip_info = f" skipped={','.join(skipped)}" if skipped else ""
                    print(
                        f"STRUCTURE_PARITY action={parity.get('action')} "
                        f"need={','.join(need_tfs)}{skip_info} {n_info}",
                        flush=True,
                    )
        except Exception as exc:  # noqa: BLE001
            print(f"STRUCTURE_REFRESH_WARN {type(exc).__name__}: {exc}", flush=True)
            refresh_errors = [{"error": f"{type(exc).__name__}: {exc}"}]

        structure_ok, structure_why = _structure_ready_for_decide(
            slice_db,
            symbol=symbol,
            timeframe=timeframe,
            bar_open_ms=bar_open_ms,
            source=signal_source,
            refresh_errors=refresh_errors,
        )
        if not structure_ok:
            # Fail closed: do not decide/trade on a partial slice, and do not advance
            # last_processed — retry this bar once structure is deep + tip-complete.
            # Still run max-hold / reconcile so open risk is not stranded on refresh failure.
            print(
                f"STRUCTURE_NOT_READY reason={structure_why} bar_open_ms={bar_open_ms} "
                f"tf={timeframe} — refuse decide (fail-closed; last_processed unchanged)",
                flush=True,
            )
            if mode == "LIVE":
                try:
                    if mt_cfg is not None:
                        _reconcile_books_to_exchange(
                            con, account=account, symbol=symbol, qty_unit=min_qty
                        )
                    for expired in _expired_books(
                        con, bar_ms=bar_open_ms, timeframe=timeframe
                    ):
                        try:
                            close_resp = close_reduce_only(
                                account=account,
                                symbol=symbol,
                                side=int(expired["side"]),
                                qty=float(expired["qty"]),
                            )
                            _mark_book_closed(con, str(expired["book_id"]))
                            print(
                                f"MAX_HOLD_CLOSE book={expired['book_id']} "
                                f"retCode={close_resp.get('retCode')} "
                                f"retMsg={close_resp.get('retMsg')} "
                                f"(during STRUCTURE_NOT_READY)",
                                flush=True,
                            )
                        except Exception as exc:  # noqa: BLE001
                            print(
                                f"MAX_HOLD_FAIL book={expired['book_id']} "
                                f"{type(exc).__name__}: {exc}",
                                flush=True,
                            )
                except Exception as exc:  # noqa: BLE001
                    print(
                        f"RECONCILE_WARN during STRUCTURE_NOT_READY "
                        f"{type(exc).__name__}: {exc}",
                        flush=True,
                    )
            if once:
                return 4
            time.sleep(max(float(close_poll_sec), 5.0))
            continue

        # Mark price is independent of the model path — overlap the REST call with predict.
        from concurrent.futures import ThreadPoolExecutor

        t0 = time.perf_counter()
        with ThreadPoolExecutor(max_workers=1) as pool:
            mark_fut = pool.submit(fetch_mark_last, symbol)
            decision = decide_once(pack=pack, ohlcv=ohlcv_closed, pack_dir=pack_dir)
            mark = mark_fut.result()
        decide_ms = (time.perf_counter() - t0) * 1000.0
        mark_ms = 0.0  # overlapped with decide
        bar_ms = int(pd.Timestamp(decision["bar_ts"]).value // 1_000_000)
        detail = {
            "reason": decision.get("reason"),
            "edge": decision.get("edge"),
            "structure_ready": True,
            "timing_ms": {
                "refresh": round(refresh_ms, 1),
                "refresh_skipped": refresh_skipped,
                "decide": round(decide_ms, 1),
                "mark": round(mark_ms, 1),
                "total": round((time.perf_counter() - t_path) * 1000.0, 1),
            },
        }
        if decision.get("feature_snapshot"):
            # Persist decide-time features so later warehouse rebuilds cannot erase evidence.
            snap = decision["feature_snapshot"]
            detail["feature_snapshot"] = {
                "sha256": snap.get("sha256"),
                "n_cols": snap.get("n_cols"),
                "values": snap.get("values"),
            }
        order_result = None
        detail["execution"] = "multitrade" if mt_cfg else "single_book"

        # Reconcile ledger vs exchange, then force max-hold exits (single-book AND multitrade).
        if mode == "LIVE":
            try:
                if mt_cfg is not None:
                    recon = _reconcile_books_to_exchange(
                        con, account=account, symbol=symbol, qty_unit=min_qty
                    )
                    detail["reconcile"] = recon
                else:
                    # Single-book: ensure one local book tracks the exchange position so
                    # max-hold can fire (previously only multitrade tracked open_books).
                    sync = _ensure_single_book_ledger(
                        con,
                        account=account,
                        symbol=symbol,
                        bar_ms=bar_ms,
                        timeframe=timeframe,
                        horizon_bars=int(strategy.get("horizon_bars") or 6),
                        tp_pct=float(strategy.get("tp_pct") or 0.01),
                        sl_pct=float(strategy.get("sl_pct") or 0.02),
                        min_qty=min_qty,
                    )
                    detail["single_book_sync"] = sync
                    # Re-attach Full TP/SL if exchange position lost protection.
                    if sync.get("ensure_tpsl"):
                        detail["ensure_tpsl"] = sync["ensure_tpsl"]

                for expired in _expired_books(con, bar_ms=bar_ms, timeframe=timeframe):
                    try:
                        close_resp = close_reduce_only(
                            account=account,
                            symbol=symbol,
                            side=int(expired["side"]),
                            qty=float(expired["qty"]),
                        )
                        _mark_book_closed(con, str(expired["book_id"]))
                        print(
                            f"MAX_HOLD_CLOSE book={expired['book_id']} "
                            f"retCode={close_resp.get('retCode')} "
                            f"retMsg={close_resp.get('retMsg')}",
                            flush=True,
                        )
                        detail.setdefault("max_hold_closes", []).append(
                            {
                                "book_id": expired["book_id"],
                                "retCode": close_resp.get("retCode"),
                                "retMsg": close_resp.get("retMsg"),
                            }
                        )
                    except Exception as exc:  # noqa: BLE001
                        print(
                            f"MAX_HOLD_FAIL book={expired['book_id']} "
                            f"{type(exc).__name__}: {exc}",
                            flush=True,
                        )
            except Exception as exc:  # noqa: BLE001
                detail["reconcile_error"] = f"{type(exc).__name__}: {exc}"
                print(f"RECONCILE_WARN {detail['reconcile_error']}", flush=True)

        if mode == "LIVE" and int(decision["side"]) != 0:
            side_i = int(decision["side"])
            tp_use = float(decision["tp_pct"])
            sl_use = float(decision["sl_pct"])
            hold_use = int(strategy.get("horizon_bars") or 6)
            book_idx = 1
            allow_entry = True

            order_qty = 0.0
            if mt_cfg is not None:
                # Prefer the candle-derived history (research parity); the persisted
                # one is only a fallback for a decision that could not recompute it.
                derived = decision.get("strength_hist")
                strength_hist = (
                    [float(x) for x in derived]
                    if derived
                    else _load_strength_hist(con)
                )
                detail["strength_hist_source"] = "derived" if derived else "persisted"
                detail["strength_hist_n"] = len(strength_hist)
                n_open = _count_open_books(con, side=side_i)
                last_key = "last_entry_ts_long" if side_i > 0 else "last_entry_ts_short"
                last_raw = _get_state(con, last_key)
                last_entry_ts = int(last_raw) if last_raw not in (None, "") else None
                gate = decide_entry_gate(
                    side=side_i,
                    pred_mean=float(decision.get("pred_mean") or 0.0),
                    n_open_same_side=n_open,
                    strength_hist=strength_hist,
                    cfg=mt_cfg,
                    bar_ts_ms=bar_ms,
                    last_entry_ts_ms=last_entry_ts,
                )
                detail["multitrade_gate"] = {
                    k: gate[k]
                    for k in (
                        "allow",
                        "skip_reason",
                        "book_idx",
                        "tp_pct",
                        "max_hold_bars",
                        "is_addon",
                        "size_mult",
                    )
                    if k in gate
                }
                if gate.get("append_strength"):
                    strength_hist.append(float(gate.get("abs_mean") or abs(float(decision.get("pred_mean") or 0.0))))
                    _save_strength_hist(
                        con, strength_hist, lookback=int(mt_cfg["mean_lookback"])
                    )
                if not gate["allow"]:
                    allow_entry = False
                    detail["skip_reason"] = str(gate.get("skip_reason") or "multitrade_gate")
                    print(f"SKIP_ENTRY {detail['skip_reason']}", flush=True)
                else:
                    book_idx = int(gate["book_idx"])
                    tp_use = float(gate["tp_pct"])
                    sl_use = float(gate["sl_pct"])
                    hold_use = int(gate["max_hold_bars"])
                    size_mult = float(gate.get("size_mult") or 1.0)
                    detail["size_mult"] = size_mult
            else:
                # Single-book: one bot, at most one open book on this symbol.
                open_books = _open_position_sides(account=account, symbol=symbol)
                if open_books:
                    allow_entry = False
                    detail["skip_reason"] = f"position_already_open:{','.join(open_books)}"
                    print(f"SKIP_ENTRY {detail['skip_reason']}", flush=True)
                size_mult = 1.0
                detail["size_mult"] = size_mult

            if allow_entry:
                try:
                    mark_now = fetch_mark_last(symbol)
                    # Live always min exchange size per pair (never wallet % notional).
                    equity_live: float | None = None
                    lev_now = resolve_pack_leverage(
                        strategy, tiers_doc, mark_price=mark_now, qty=min_qty
                    )
                    leverage = float(lev_now["leverage"])
                    order_qty, qty_detail = resolve_order_qty(
                        sizing=sizing_cfg,
                        equity=equity_live,
                        leverage=leverage,
                        price=float(mark_now),
                        size_mult=float(detail.get("size_mult") or 1.0),
                        instrument=instrument,
                        min_qty_fallback=min_qty,
                        force_min_exchange=True,
                    )
                    detail.update(qty_detail)
                    if order_qty <= 0:
                        allow_entry = False
                        detail["skip_reason"] = "qty_below_venue_min_or_zero"
                        print(
                            f"SKIP_ENTRY qty_below_venue_min_or_zero detail={qty_detail}",
                            flush=True,
                        )
                    else:
                        lev_now = resolve_pack_leverage(
                            strategy, tiers_doc, mark_price=mark_now, qty=order_qty
                        )
                        leverage = float(lev_now["leverage"])
                        detail["leverage"] = leverage
                        detail["leverage_ceiling"] = lev_now["ceiling"]
                        detail["tp_pct"] = tp_use
                        detail["sl_pct"] = sl_use
                        detail["book_idx"] = book_idx
                        detail["max_hold_bars"] = hold_use
                        detail["order_qty"] = float(order_qty)
                        order_result = place_min_order(
                            account=account,
                            symbol=symbol,
                            side=side_i,
                            qty=order_qty,
                            tp_pct=tp_use,
                            sl_pct=sl_use,
                            leverage=leverage,
                            partial_tpsl=bool(mt_cfg is not None),
                        )
                        order_body = order_result.get("order") or {}
                        detail["order_retCode"] = order_body.get("retCode")
                        detail["order_retMsg"] = order_body.get("retMsg")
                        stops_body = order_result.get("stops") or {}
                        detail["stops_retCode"] = stops_body.get("retCode")
                        detail["stops_retMsg"] = stops_body.get("retMsg")
                        print(
                            f"ORDER retCode={detail.get('order_retCode')} "
                            f"retMsg={detail.get('order_retMsg')} "
                            f"stops={detail.get('stops_retCode')} "
                            f"book={book_idx} tp={tp_use} hold={hold_use} "
                            f"qty={order_qty} size_mult={detail.get('size_mult', 1)} "
                            f"leverage={leverage} sizing={sizing_cfg['mode']}",
                            flush=True,
                        )
                        if _bybit_retcode(order_body) == 0:
                            # Track max-hold for both single-book and multitrade.
                            oid = None
                            try:
                                oid = str(
                                    ((order_body.get("result") or {}).get("orderId"))
                                    or ""
                                ) or None
                            except Exception:  # noqa: BLE001
                                oid = None
                            _insert_open_book(
                                con,
                                book_id=f"{bar_ms}_{side_i}_{book_idx}",
                                side=side_i,
                                entry_bar_ms=bar_ms,
                                max_hold_bars=hold_use,
                                qty=float(order_qty),
                                tp_pct=tp_use,
                                sl_pct=sl_use,
                                book_idx=book_idx,
                                order_id=oid,
                            )
                            last_key = (
                                "last_entry_ts_long" if side_i > 0 else "last_entry_ts_short"
                            )
                            _set_state(con, last_key, str(bar_ms))
                            # Fail-closed: if Full TP/SL attach failed and flattened, close book.
                            if stops_body.get("fail_closed_flatten") is not None:
                                _mark_book_closed(
                                    con, f"{bar_ms}_{side_i}_{book_idx}"
                                )
                except Exception as exc:  # noqa: BLE001
                    detail["order_error"] = f"{type(exc).__name__}: {exc}"
                    print(f"ORDER_FAIL {detail['order_error']}", flush=True)

        con.execute(
            "INSERT OR REPLACE INTO decisions(bar_ts_ms,decided_utc,side,pred_mean,mark,mode,detail) "
            "VALUES (?,?,?,?,?,?,?)",
            (
                bar_ms,
                datetime.now(timezone.utc).isoformat(),
                int(decision["side"]),
                decision.get("pred_mean"),
                mark,
                mode,
                json.dumps(detail),
            ),
        )
        _set_state(con, "last_processed_bar_ts", str(bar_ms))
        timing = detail.get("timing_ms") or {}
        print(
            f"DECISION bar={decision['bar_ts']} side={decision['side']} "
            f"pred={decision.get('pred_mean')} mark={mark} mode={mode} "
            f"timing_ms={timing}",
            flush=True,
        )
        if once:
            return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="structure_v1 micro-live / shadow runner")
    ap.add_argument("--pack", type=Path, default=PACK_DIR)
    ap.add_argument("--state", type=Path, default=Path(STATE_DB_DEFAULT))
    ap.add_argument("--mode", choices=("SHADOW", "LIVE"), default="SHADOW")
    ap.add_argument("--account", default="Xxobster7")
    ap.add_argument("--cert", type=Path, default=DEFAULT_CERT)
    ap.add_argument("--once", action="store_true")
    ap.add_argument(
        "--force-now",
        action="store_true",
        help="decide on the latest already-closed bar without waiting for the next close",
    )
    ap.add_argument("--live-orders", action="store_true", help="required with --mode LIVE")
    args = ap.parse_args(argv)

    fp = pack_fingerprint(args.pack)
    if not fp:
        raise SystemExit("pack fingerprint missing — run build_structure_live_pack.py")

    if args.mode == "LIVE":
        if not args.live_orders:
            raise SystemExit("LIVE mode requires --live-orders")
        try:
            cert = refuse_vps_deploy_without_live_certificate(path=args.cert)
        except PolicyError as exc:
            print(f"REFUSED: {exc}", flush=True)
            return 5
        if cert.pack_hash and cert.pack_hash != fp:
            print(
                f"REFUSED: pack_hash mismatch cert={cert.pack_hash[:16]}… pack={fp[:16]}…",
                flush=True,
            )
            return 5
        # also require tiers
        tiers = json.loads((args.pack / "risk_tiers.json").read_text(encoding="utf-8"))
        if int(tiers.get("n_tiers") or 0) < 1:
            print("REFUSED: risk tiers missing in pack", flush=True)
            return 5

    return run_loop(
        pack_dir=args.pack,
        state_path=args.state,
        mode=args.mode,
        account=args.account,
        once=bool(args.once) or bool(args.force_now),
        force_now=bool(args.force_now),
    )


if __name__ == "__main__":
    raise SystemExit(main())
