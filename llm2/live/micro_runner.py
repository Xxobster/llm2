"""Micro-live / shadow loop for frozen structure_v1 LightGBM pack.

Bar-close schedule (standard 22.1): idle until lead_sec before close, fast-poll,
decide once on the newly closed bar, persist last_processed_bar_ts.

Default mode is SHADOW (log decisions, no orders). LIVE_ORDERS requires certificate
AUTHORIZED + --live-orders flag + account credentials.
"""

from __future__ import annotations

import argparse
import json
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
from llm2.paths import ROUND_TRIP_COST, TF_MS
from llm2.research_policy import PolicyError

BYBIT_REST = "https://api.bybit.com"
STATE_DB_DEFAULT = "state/micro_live_state.sqlite"


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
    con.commit()
    return con


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
    blob = joblib.load(pack_dir / "model.joblib")
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
    # Live refresh writes source=bybit; research default remains binance warehouse.
    os.environ["LLM2_STRUCTURE_SOURCE"] = "bybit"
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
        # Warehouse can leave last_retrace_pct undefined on the newest leg; training
        # dropped those rows. For live, zero-fill retrace columns (base + HTF aliases).
        for col in feats.columns:
            if col == "last_retrace_pct" or col.startswith("last_retrace_pct_"):
                feats[col] = feats[col].fillna(0.0)
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
    x = feats.iloc[[-1]].to_numpy(dtype=float)
    pred = model.predict(x)
    mean = float(np.asarray(pred.mean if hasattr(pred, "mean") else pred).reshape(-1)[0])
    family = target_family(str(strategy.get("target", "fwd_return")))
    # Research/live gate parity: return targets use fee hurdle; direction uses ±0.10 band.
    default_edge = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    edge = float(strategy.get("min_edge", default_edge))
    if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
        # Refuse silent mis-config that would trade almost every bar.
        edge = DIRECTION_BAND
    side = int(proxy_side(np.asarray([mean], dtype=float), family)[0])
    return {
        "side": side,
        "pred_mean": mean,
        "reason": "ok",
        "bar_ts": feats.index[-1],
        "edge": edge,
        "target": strategy.get("target"),
        "tp_pct": strategy["tp_pct"],
        "sl_pct": strategy["sl_pct"],
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


def _open_position_sides(*, account: str, symbol: str) -> list[str]:
    """Return open side names (Buy/Sell) for symbol; empty if flat."""
    import hashlib
    import hmac
    import time as _time
    import urllib.parse
    import urllib.request

    api_key, api_secret = _load_account_keys(account)
    params = {"category": "linear", "symbol": symbol.upper()}
    q = urllib.parse.urlencode(params)
    ts = str(int(_time.time() * 1000))
    recv = "60000"
    sign = hmac.new(
        api_secret.encode(), f"{ts}{api_key}{recv}{q}".encode(), hashlib.sha256
    ).hexdigest()
    req = urllib.request.Request(
        f"{BYBIT_REST}/v5/position/list?{q}",
        headers={
            "X-BAPI-API-KEY": api_key,
            "X-BAPI-TIMESTAMP": ts,
            "X-BAPI-RECV-WINDOW": recv,
            "X-BAPI-SIGN": sign,
            "User-Agent": "llm2-micro-live/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    sides: list[str] = []
    for p in (data.get("result") or {}).get("list") or []:
        if float(p.get("size") or 0) == 0:
            continue
        sides.append(str(p.get("side") or "?"))
    return sides


def place_min_order(
    *,
    account: str,
    symbol: str,
    side: int,
    qty: float,
    tp_pct: float,
    sl_pct: float,
    leverage: float,
) -> dict[str, Any]:
    """Place market entry + attach TP/SL via Bybit V5. Never logs secrets."""
    api_key, api_secret = _load_account_keys(account)
    last = fetch_mark_last(symbol)
    mode_resp = ensure_hedge_mode(account=account, symbol=symbol)
    lev_resp = ensure_exchange_leverage(
        account=account, symbol=symbol, leverage=float(leverage)
    )
    # Minimal market order (strings only — Bybit rejects numeric qty / stray flags).
    qty_str = f"{float(qty):.6f}".rstrip("0").rstrip(".")
    if "." not in qty_str:
        qty_str = f"{qty_str}.0"
    # Hedge-mode: Buy→positionIdx 1, Sell→positionIdx 2.
    position_idx = 1 if side > 0 else 2
    body = {
        "category": "linear",
        "symbol": symbol.upper(),
        "side": "Buy" if side > 0 else "Sell",
        "orderType": "Market",
        "qty": qty_str,
        "positionIdx": position_idx,
    }
    order = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/order/create",
        body=body,
    )
    # trading stop
    if side > 0:
        take = last * (1.0 + float(tp_pct))
        stop = last * (1.0 - float(sl_pct))
    else:
        take = last * (1.0 - float(tp_pct))
        stop = last * (1.0 + float(sl_pct))
    stop_body = {
        "category": "linear",
        "symbol": symbol.upper(),
        "takeProfit": f"{take:.2f}",
        "stopLoss": f"{stop:.2f}",
        "tpTriggerBy": "MarkPrice",
        "slTriggerBy": "MarkPrice",
        "positionIdx": position_idx,
    }
    stops = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/position/trading-stop",
        body=stop_body,
    )
    return {
        "order": order,
        "stops": stops,
        "ref_mark": last,
        "leverage": float(leverage),
        "leverage_set": lev_resp,
        "mode_set": mode_resp,
    }


def sleep_until_next_close(timeframe: str, *, lead_sec: float = 5.0) -> None:
    tf_ms = TF_MS[timeframe]
    now_ms = int(time.time() * 1000)
    next_close = ((now_ms // tf_ms) + 1) * tf_ms
    wait = (next_close - now_ms) / 1000.0 - lead_sec
    if wait > 0:
        time.sleep(wait)


def _slice_has_closed_bar(
    slice_db: Path,
    *,
    symbol: str,
    timeframe: str,
    bar_open_ms: int,
    source: str = "bybit",
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
    tiers_doc = json.loads((pack_dir / "risk_tiers.json").read_text(encoding="utf-8"))
    qty = float(tiers_doc.get("instrument", {}).get("min_qty", 0.001))
    mark0 = fetch_mark_last(symbol)
    lev_info = resolve_pack_leverage(
        strategy, tiers_doc, mark_price=mark0, qty=qty
    )
    leverage = float(lev_info["leverage"])
    con = _state_conn(state_path)
    print(
        f"micro_runner mode={mode} symbol={symbol} tf={timeframe} qty={qty} "
        f"leverage={leverage} (sl={lev_info['sl_pct']} ceiling={lev_info['ceiling']} "
        f"haircut={lev_info['haircut']} mm={lev_info['mm_buffer']} "
        f"mark_buf={lev_info['mark_buffer']}) "
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

    while True:
        skip_schedule = bool(force_now)
        force_now = False
        if not skip_schedule:
            sleep_until_next_close(timeframe, lead_sec=lead_sec)
        deadline = time.time() + (5.0 if skip_schedule else confirm_timeout_sec)
        closed_bar = None
        ohlcv_closed = None
        while time.time() < deadline:
            ohlcv = fetch_ohlcv_rest(symbol, timeframe, limit=300)
            # last bar is the currently-forming candle; use previous as closed
            if len(ohlcv) < 3:
                time.sleep(close_poll_sec)
                continue
            # Prefer last fully closed bar (drop the still-forming candle).
            candidate = ohlcv.index[-2]
            last_ms = _get_state(con, "last_processed_bar_ts")
            cand_ms = str(int(candidate.value // 1_000_000))
            if (not skip_schedule) and last_ms is not None and cand_ms <= last_ms:
                time.sleep(close_poll_sec)
                continue
            closed_bar = candidate
            ohlcv_closed = ohlcv.iloc[:-1]
            break
        if closed_bar is None or ohlcv_closed is None:
            print("STALE_BAR: no new closed bar within confirm_timeout", flush=True)
            if once:
                return 3
            continue

        # Refresh structure features from Bybit REST so warehouse lag cannot skip bars.
        # The :55 timer warms 1h/4h/1w; on close we only recompute the decision timeframe
        # when that closed bar is not already in the pack slice.
        t_path = time.perf_counter()
        refresh_ms = 0.0
        refresh_skipped = False
        try:
            from llm2.data.indicators import clear_indicator_cache
            from llm2.live.refresh_structure import refresh_symbol

            slice_db = pack_dir / "indicators_live_slice.sqlite"
            bar_open_ms = int(pd.Timestamp(closed_bar).value // 1_000_000)
            if slice_db.is_file():
                if _slice_has_closed_bar(
                    slice_db,
                    symbol=symbol,
                    timeframe=timeframe,
                    bar_open_ms=bar_open_ms,
                ):
                    refresh_skipped = True
                    clear_indicator_cache()
                else:
                    t0 = time.perf_counter()
                    refresh_symbol(
                        symbol=symbol,
                        timeframes=(timeframe,),
                        indicator_db=slice_db,
                        limit=350,
                    )
                    refresh_ms = (time.perf_counter() - t0) * 1000.0
                    clear_indicator_cache()
        except Exception as exc:  # noqa: BLE001
            print(f"STRUCTURE_REFRESH_WARN {type(exc).__name__}: {exc}", flush=True)

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
            "timing_ms": {
                "refresh": round(refresh_ms, 1),
                "refresh_skipped": refresh_skipped,
                "decide": round(decide_ms, 1),
                "mark": round(mark_ms, 1),
                "total": round((time.perf_counter() - t_path) * 1000.0, 1),
            },
        }
        order_result = None
        if mode == "LIVE" and int(decision["side"]) != 0:
            # One bot handles both directions; do not open a second book while in a position.
            open_books = _open_position_sides(account=account, symbol=symbol)
            if open_books:
                detail["skip_reason"] = f"position_already_open:{','.join(open_books)}"
                print(f"SKIP_ENTRY {detail['skip_reason']}", flush=True)
            else:
                try:
                    # Refresh mark so tier cap matches current notional.
                    mark_now = fetch_mark_last(symbol)
                    lev_now = resolve_pack_leverage(
                        strategy, tiers_doc, mark_price=mark_now, qty=qty
                    )
                    leverage = float(lev_now["leverage"])
                    detail["leverage"] = leverage
                    detail["leverage_ceiling"] = lev_now["ceiling"]
                    order_result = place_min_order(
                        account=account,
                        symbol=symbol,
                        side=int(decision["side"]),
                        qty=qty,
                        tp_pct=float(decision["tp_pct"]),
                        sl_pct=float(decision["sl_pct"]),
                        leverage=leverage,
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
                        f"leverage={leverage}",
                        flush=True,
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
