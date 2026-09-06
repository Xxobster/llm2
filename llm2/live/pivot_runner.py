"""Pivot tip runner — working LIMIT arms (SOL geo / ETH p75_ctrl_atr).

SHADOW by default (log decide only). LIVE_ORDERS requires certificate AUTHORIZED
+ --live-orders + account secrets. Entry is Bybit LIMIT with work_bars cancel —
not structure market micro_runner.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd

from llm2.live.candle_freshness import LIVE_DATA_001, signal_entry_gate
from llm2.live.certificate import refuse_vps_deploy_without_live_certificate
from llm2.live.micro_runner import (
    _bybit_retcode,
    _bybit_signed_request,
    _load_account_keys,
    _position_list,
    _qty_str,
    close_reduce_only,
    ensure_exchange_leverage,
    ensure_full_position_tpsl,
    ensure_hedge_mode,
    fetch_wallet_equity_usdt,
    latest_closed_bar_open_ms,
    maker_exit_bracket_present,
    resolve_order_qty,
    sleep_until_next_close,
    stop_trigger_px_from_open_orders,
)
from llm2.live.refresh_structure import (
    DEFAULT_SIGNAL_SOURCE,
    fetch_ohlcv_binance_rest,
    fetch_signal_ohlcv,
    _drop_forming_bar,
    _merge_ohlcv_tip,
)
from llm2.paths import TF_MS
from llm2.pivot.features.packs import build_feature_frame
from llm2.pivot.strategy.score_oos import _atr_frac
from llm2.pivot.train.calibration import apply_calibrator
from llm2.research_policy import PolicyError
from llm2.sizing_policy import SIZING_MODE_RISK_FRACTION
from llm2.validation.folds import index_to_ms
from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
from tradesim import research_instrument  # noqa: E402

LIVE_OHLCV_BARS = 3000
LEAD_SEC = 25.0
CLOSE_POLL_SEC = 2.0
FILL_POLL_SEC = 2.0
CONFIRM_TIMEOUT_SEC = 120.0
# Instant cancel only for collector-down / invented tip. Transient HTTP and
# bar-boundary lag wait the same confirm window as decide (LIVE-DATA-001
# thresholds stay 5s / exact tip).
FILL_WAIT_INSTANT_CANCEL_CODES = frozenset({"COLLECTOR_ERROR", "CANDLE_AHEAD"})
FILL_WAIT_CONFIRM_CODES = frozenset(
    {"CANDLE_STALE", "CANDLE_MISSING", "CLOCK_SKEW", "SERVER_TIME_FAIL"}
)
_RISK_FRACTION_MODES = frozenset(
    {SIZING_MODE_RISK_FRACTION, "STOP_RISK_FRACTION", "PCT_EQUITY_AT_SL"}
)


def pack_uses_stop_risk_sizing(strategy: dict[str, Any]) -> bool:
    mode = str((strategy.get("sizing") or {}).get("mode") or "MIN_EXCHANGE").upper()
    return mode in _RISK_FRACTION_MODES


def resolve_pivot_live_qty(
    *,
    strategy: dict[str, Any],
    decide: dict[str, Any],
    instrument: Any,
    equity: float | None,
) -> tuple[float, dict[str, Any]]:
    """Pack ``MIN_EXCHANGE`` stays min-lot. ``RISK_FRACTION`` uses 5% equity at stop."""
    risk = pack_uses_stop_risk_sizing(strategy)
    sizing = dict(strategy.get("sizing") or {"mode": "MIN_EXCHANGE"})
    return resolve_order_qty(
        sizing=sizing,
        equity=float(equity) if risk else None,
        leverage=float(decide["leverage"]),
        price=float(decide["limit_px"]),
        size_mult=float(sizing.get("size_mult") or 1.0),
        instrument=instrument,
        min_qty_fallback=float(getattr(instrument, "min_qty", 0.001) or 0.001),
        force_min_exchange=not risk,
        sl_pct=float(decide["sl_pct"]) if risk else None,
    )


def _log(msg: str) -> None:
    print(f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} {msg}", flush=True)


def fill_wait_gate_action(
    tip_code: str,
    *,
    first_fail_mono: float | None,
    now_mono: float,
    confirm_timeout_sec: float = CONFIRM_TIMEOUT_SEC,
) -> str:
    """Return ``wait`` or ``cancel`` when LIVE-DATA-001 fails during fill-wait.

    Does not change gate thresholds. A single 2-second poll must not cancel a
    resting LIMIT on CLOCK_SKEW / SERVER_TIME_FAIL / CANDLE_STALE (HTTP RTT
    and collector close lag). Cancel immediately on COLLECTOR_ERROR / CANDLE_AHEAD,
    or if a confirm-class code lasts longer than ``confirm_timeout_sec``.
    """
    code = str(tip_code or "DATA_UNSAFE")
    if code in FILL_WAIT_INSTANT_CANCEL_CODES:
        return "cancel"
    if code in FILL_WAIT_CONFIRM_CODES:
        if first_fail_mono is None:
            return "wait"
        if (float(now_mono) - float(first_fail_mono)) < float(confirm_timeout_sec):
            return "wait"
        return "cancel"
    return "cancel"


def _persist_decision_order_result(
    con: sqlite3.Connection,
    *,
    bar_ms: int,
    decide: dict[str, Any],
    result: dict[str, Any],
) -> None:
    created = str(decide.get("created_utc") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    payload = {**decide, "order_result": result}
    con.execute(
        "INSERT OR REPLACE INTO pivot_decisions(bar_ts_ms, payload_json, created_utc) VALUES (?,?,?)",
        (int(bar_ms), json.dumps(payload, default=str), created),
    )
    con.commit()


class TipCandleUnstableError(RuntimeError):
    """Tip close moved between two REST reads — refuse decide (hard gate)."""


def load_pivot_ohlcv(symbol: str, timeframe: str, *, limit: int = LIVE_OHLCV_BARS) -> pd.DataFrame:
    """Live-safe OHLCV with forced Binance REST tip + hard tip-identity gate.

    Always overlays REST on the tip so decides do not bind to a revisable shared tip.
    Then re-reads REST; if tip close/open/high/low moves beyond a tight relative
    epsilon, raise ``TipCandleUnstableError`` so the runner skips the bar (fail closed).
    Persisted tip OHLC is attached later in the decide payload for forensic identity.
    """
    df = fetch_signal_ohlcv(
        symbol,
        timeframe,
        source=DEFAULT_SIGNAL_SOURCE,
        limit=int(limit),
        force_rest_tip=True,
    )
    if df is None or df.empty:
        raise RuntimeError(f"no live OHLCV for {symbol} {timeframe}")
    tip_rest_a = fetch_ohlcv_binance_rest(symbol, timeframe, limit=min(200, int(limit)))
    tip_rest_a = _drop_forming_bar(tip_rest_a, timeframe)
    time.sleep(0.35)
    tip_rest_b = fetch_ohlcv_binance_rest(symbol, timeframe, limit=min(200, int(limit)))
    tip_rest_b = _drop_forming_bar(tip_rest_b, timeframe)
    if tip_rest_a is None or tip_rest_a.empty or tip_rest_b is None or tip_rest_b.empty:
        raise TipCandleUnstableError("REST tip missing on double-read")
    ts_a = int(tip_rest_a["ts_ms"].iloc[-1]) if "ts_ms" in tip_rest_a.columns else int(
        tip_rest_a.index[-1].value // 1_000_000
    )
    ts_b = int(tip_rest_b["ts_ms"].iloc[-1]) if "ts_ms" in tip_rest_b.columns else int(
        tip_rest_b.index[-1].value // 1_000_000
    )
    if ts_a != ts_b:
        raise TipCandleUnstableError(f"REST tip bar moved {ts_a} -> {ts_b}")
    # Tolerance must catch a still-forming tip without rejecting normal venue
    # rounding jitter. A 1e-8 *relative* tolerance is effectively zero: it
    # rejected Ethereum reads of 2495.88 vs 2495.89 (one tick), which fired
    # TIP_UNSTABLE on most bars and pushed each decide minutes past the close.
    # A forming bar moves far more than a couple of ticks, so allow two.
    try:
        tick = float(getattr(research_instrument(symbol), "tick_size", 0.0) or 0.0)
    except Exception:  # noqa: BLE001
        tick = 0.0
    for col in ("open", "high", "low", "close"):
        a = float(tip_rest_a[col].iloc[-1])
        b = float(tip_rest_b[col].iloc[-1])
        tol = max(2.0 * tick, abs(b) * 1e-6, 1e-8)
        if abs(a - b) > tol:
            raise TipCandleUnstableError(
                f"REST tip {col} unstable {a} -> {b} (tol={tol})"
            )
    df = _merge_ohlcv_tip(df, tip_rest_b)
    if len(df) > int(limit):
        df = df.iloc[-int(limit) :].copy()
    return df


def _state_conn(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(path))
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS pivot_state (
            k TEXT PRIMARY KEY,
            v TEXT NOT NULL
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS pivot_decisions (
            bar_ts_ms INTEGER PRIMARY KEY,
            payload_json TEXT NOT NULL,
            created_utc TEXT NOT NULL
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS pivot_orders (
            order_id TEXT PRIMARY KEY,
            bar_ts_ms INTEGER,
            payload_json TEXT NOT NULL,
            created_utc TEXT NOT NULL
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS pivot_fills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT NOT NULL,
            created_utc TEXT NOT NULL,
            payload_json TEXT NOT NULL
        )
        """
    )
    con.commit()
    return con


def record_pivot_fill(con: sqlite3.Connection, event: str, payload: dict[str, Any]) -> None:
    """Append a fill/exit event so live-vs-backtest audits have exit prices."""
    con.execute(
        "INSERT INTO pivot_fills(event, created_utc, payload_json) VALUES (?,?,?)",
        (
            str(event),
            datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            json.dumps(payload, default=str),
        ),
    )
    con.commit()


def _state_get(con: sqlite3.Connection, key: str) -> str | None:
    row = con.execute("SELECT v FROM pivot_state WHERE k=?", (key,)).fetchone()
    return None if row is None else str(row[0])


def _state_set(con: sqlite3.Connection, key: str, val: str) -> None:
    con.execute(
        "INSERT INTO pivot_state(k,v) VALUES(?,?) ON CONFLICT(k) DO UPDATE SET v=excluded.v",
        (key, val),
    )
    con.commit()


def max_hold_deadline_ms(entry_bar_ms: int, max_hold_bars: int, tf_ms: int) -> int:
    """Wall time of the expiry-bar open (tradesim: hold >= max_hold at that open)."""
    return int(entry_bar_ms) + int(max_hold_bars) * int(tf_ms)


def entry_bar_open_ms_from_fill(fill_ms: int, timeframe: str) -> int:
    """Open of the 15m (or other) bar that was forming when the limit filled."""
    step = int(TF_MS[timeframe])
    return (int(fill_ms) // step) * step


def should_flatten_max_hold(
    *,
    now_ms: int,
    entry_bar_ms: int,
    max_hold_bars: int,
    tf_ms: int,
) -> bool:
    if int(max_hold_bars) <= 0:
        return False
    return int(now_ms) >= max_hold_deadline_ms(entry_bar_ms, max_hold_bars, tf_ms)


_OPEN_STATE_KEYS = (
    "open_entry_bar_ms",
    "open_side",
    "open_qty",
    "open_max_hold_bars",
    "open_sl_px",
    "open_tp_px",
)


def _read_open_pos(con: sqlite3.Connection) -> dict[str, Any] | None:
    raw = _state_get(con, "open_entry_bar_ms")
    if raw in (None, ""):
        return None
    side = _state_get(con, "open_side") or ""
    qty_raw = _state_get(con, "open_qty") or "0"
    hold_raw = _state_get(con, "open_max_hold_bars") or "0"
    sl_raw = _state_get(con, "open_sl_px") or ""
    tp_raw = _state_get(con, "open_tp_px") or ""
    return {
        "entry_bar_ms": int(raw),
        "side": str(side),
        "qty": float(qty_raw),
        "max_hold_bars": int(hold_raw),
        "sl_px": float(sl_raw) if sl_raw not in {"", None} else 0.0,
        "tp_px": float(tp_raw) if tp_raw not in {"", None} else 0.0,
    }


def _clear_open_pos(con: sqlite3.Connection) -> None:
    for key in _OPEN_STATE_KEYS:
        _state_set(con, key, "")


def _record_open_pos(
    con: sqlite3.Connection,
    *,
    entry_bar_ms: int,
    side: str,
    qty: float,
    max_hold_bars: int,
    sl_px: float | None = None,
    tp_px: float | None = None,
) -> None:
    _state_set(con, "open_entry_bar_ms", str(int(entry_bar_ms)))
    _state_set(con, "open_side", str(side))
    _state_set(con, "open_qty", str(float(qty)))
    _state_set(con, "open_max_hold_bars", str(int(max_hold_bars)))
    if sl_px is not None:
        _state_set(con, "open_sl_px", str(float(sl_px)))
    if tp_px is not None:
        _state_set(con, "open_tp_px", str(float(tp_px)))


def _max_hold_due(con: sqlite3.Connection, timeframe: str, *, now_ms: int | None = None) -> bool:
    pos = _read_open_pos(con)
    if pos is None:
        return False
    now = int(now_ms if now_ms is not None else time.time() * 1000)
    return should_flatten_max_hold(
        now_ms=now,
        entry_bar_ms=int(pos["entry_bar_ms"]),
        max_hold_bars=int(pos["max_hold_bars"]),
        tf_ms=int(TF_MS[timeframe]),
    )


def reconcile_exchange_position(
    *,
    account: str,
    symbol: str,
    timeframe: str,
    con: sqlite3.Connection,
    tp_pct: float,
    sl_pct: float,
    max_hold_bars: int,
) -> dict[str, Any]:
    """Heal a position the exchange has but local state does not know about.

    Why this exists: ``manage_working_limit`` places the entry LIMIT and only
    then waits for the fill and attaches Take-Profit / Stop-Loss. If the process
    raises between those steps — a network timeout is enough — the order can fill
    on the exchange while local state still calls it a *working* order. Nothing
    else notices: ``maybe_max_hold_flatten`` starts from ``_read_open_pos`` and
    returns ``no_local_open``, so the position is invisible to the bot and holds
    **no protective orders**.

    That happened live on 2026-08-26: an Ethereum entry filled after
    ``URLError: handshake operation timed out``, leaving a naked short with
    ``to_TP/SL = -`` and no max-hold deadline.

    So on every heartbeat: if the exchange reports exposure and either local
    state has no open position or the maker exit bracket is missing, attach the
    frozen Post-Only take-profit and stop-limit, then record the fill so
    max-hold can fire. Fail closed and loud.
    """
    out: dict[str, Any] = {"action": "none"}
    rows = [p for p in _position_list(account=account, symbol=symbol) if float(p.get("size") or 0) > 0]
    if not rows:
        return {"action": "none", "reason": "exchange_flat"}
    pos = rows[0]
    size = float(pos.get("size") or 0)
    avg_px = float(pos.get("avgPrice") or pos.get("avg_price") or 0)
    side = str(pos.get("side") or "")
    side_i = -1 if side == "Sell" else 1
    has_maker = False
    if avg_px > 0 and side in ("Buy", "Sell"):
        try:
            has_maker = maker_exit_bracket_present(
                account=account,
                symbol=symbol,
                side=side_i,
                avg_price=avg_px,
                tp_pct=float(tp_pct),
                sl_pct=float(sl_pct),
            )
        except Exception as exc:  # noqa: BLE001
            _log(f"RECONCILE_EXIT_SCAN_FAIL {type(exc).__name__}: {exc}")
    local = _read_open_pos(con)
    out.update(
        {"size": size, "avg_price": avg_px, "side": side, "has_maker_exits": has_maker,
         "local_known": local is not None}
    )
    if local is not None and has_maker:
        return {**out, "action": "none", "reason": "tracked_and_protected"}
    if avg_px <= 0 or side not in ("Buy", "Sell"):
        _log(f"RECONCILE_UNKNOWN_POSITION {json.dumps(out, default=str)[:300]}")
        return {**out, "action": "unknown_position"}

    if not has_maker:
        tpsl = ensure_full_position_tpsl(
            account=account,
            symbol=symbol,
            side=side_i,
            avg_price=avg_px,
            tp_pct=float(tp_pct),
            sl_pct=float(sl_pct),
            qty=size,
        )
        out["tpsl"] = tpsl
        if _bybit_retcode(tpsl) not in (0, 34040):
            _log(f"RECONCILE_TPSL_FAIL ret={tpsl.get('retCode')} msg={tpsl.get('retMsg')}")
            return {**out, "action": "tpsl_failed"}
        _log(
            f"RECONCILE_TPSL_ATTACHED symbol={symbol} side={side} avg={avg_px} "
            f"tp={tpsl.get('tp_price')} sl={tpsl.get('sl_price')} mode={tpsl.get('mode')}"
        )
        if local is not None:
            _state_set(con, "open_sl_px", str(float(tpsl.get("sl_price") or 0)))
            _state_set(con, "open_tp_px", str(float(tpsl.get("tp_price") or 0)))

    if local is None:
        entry_bar_ms = entry_bar_open_ms_from_fill(int(time.time() * 1000), timeframe)
        tpsl_info = out.get("tpsl") if isinstance(out.get("tpsl"), dict) else {}
        _record_open_pos(
            con,
            entry_bar_ms=entry_bar_ms,
            side=side,
            qty=size,
            max_hold_bars=int(max_hold_bars),
            sl_px=float((tpsl_info or {}).get("sl_price") or 0) or None,
            tp_px=float((tpsl_info or {}).get("tp_price") or 0) or None,
        )
        # The entry LIMIT is gone: it became this position.
        _state_set(con, "working_order_id", "")
        _state_set(con, "working_deadline_ms", "")
        record_pivot_fill(
            con,
            "reconciled_orphan_entry",
            {
                "side": side,
                "qty": size,
                "avg_price": avg_px,
                "entry_bar_ms": entry_bar_ms,
                "note": "position found on exchange with no local record",
            },
        )
        out["entry_bar_ms"] = entry_bar_ms
        _log(
            f"RECONCILE_ADOPTED symbol={symbol} side={side} qty={size} avg={avg_px} "
            f"entry_bar_ms={entry_bar_ms} max_hold_bars={max_hold_bars}"
        )
    return {**out, "action": "reconciled"}


def maybe_gap_flatten_taker(
    *,
    account: str,
    symbol: str,
    con: sqlite3.Connection,
) -> dict[str, Any]:
    """Market-flatten if mark is through the attached stop (maker limit skipped the gap).

    A limit stop on the far side of a gap does not fill. Taker flatten is the
    last-resort required by the maker-first fee rule.
    """
    rows = [p for p in _position_list(account=account, symbol=symbol) if float(p.get("size") or 0) > 0]
    if not rows:
        return {"action": "none", "reason": "exchange_flat"}
    pos = rows[0]
    size = float(pos.get("size") or 0)
    side = str(pos.get("side") or "")
    sl = float(pos.get("stopLoss") or 0)
    mark = float(pos.get("markPrice") or pos.get("mark_price") or 0)
    side_i = -1 if side == "Sell" else 1
    if sl <= 0:
        try:
            sl = float(
                stop_trigger_px_from_open_orders(
                    account=account, symbol=symbol, side=side_i
                )
                or 0
            )
        except Exception:  # noqa: BLE001
            sl = 0.0
    if sl <= 0:
        local = _read_open_pos(con)
        if local is not None:
            sl = float(local.get("sl_px") or 0)
    if sl <= 0 or mark <= 0 or side not in ("Buy", "Sell") or size <= 0:
        return {
            "action": "none",
            "reason": "no_stop_or_mark",
            "side": side,
            "sl": sl,
            "mark": mark,
        }
    through = (side == "Sell" and mark >= sl) or (side == "Buy" and mark <= sl)
    if not through:
        return {"action": "none", "reason": "mark_inside_stop", "mark": mark, "sl": sl}
    resp = close_reduce_only(account=account, symbol=symbol, side=side_i, qty=size)
    record_pivot_fill(
        con,
        "gap_flatten_taker",
        {"side": side, "qty": size, "mark": mark, "sl": sl, "response": resp},
    )
    _clear_open_pos(con)
    _log(
        f"GAP_FLATTEN_TAKER symbol={symbol} side={side} qty={size} mark={mark} sl={sl} "
        f"ret={resp.get('retCode')} msg={resp.get('retMsg')}"
    )
    return {"action": "flattened", "mark": mark, "sl": sl, "side": side, "response": resp}


def maybe_max_hold_flatten(
    *,
    account: str,
    symbol: str,
    timeframe: str,
    con: sqlite3.Connection,
    now_ms: int | None = None,
) -> dict[str, Any]:
    """Market flatten when pack max_hold_bars is reached. Safe no-op if flat."""
    pos = _read_open_pos(con)
    if pos is None:
        return {"action": "none", "reason": "no_local_open"}
    if not has_open_exposure(account=account, symbol=symbol):
        record_pivot_fill(
            con,
            "exchange_flat",
            {
                "entry_bar_ms": int(pos["entry_bar_ms"]),
                "side": pos["side"],
                "qty": pos["qty"],
                "reason": "exchange_flat",
            },
        )
        _clear_open_pos(con)
        return {"action": "cleared", "reason": "exchange_flat"}
    now = int(now_ms if now_ms is not None else time.time() * 1000)
    deadline = max_hold_deadline_ms(
        int(pos["entry_bar_ms"]), int(pos["max_hold_bars"]), int(TF_MS[timeframe])
    )
    if not should_flatten_max_hold(
        now_ms=now,
        entry_bar_ms=int(pos["entry_bar_ms"]),
        max_hold_bars=int(pos["max_hold_bars"]),
        tf_ms=int(TF_MS[timeframe]),
    ):
        return {"action": "hold", "deadline_ms": deadline, "now_ms": now}
    side_i = -1 if str(pos["side"]) == "Sell" else 1
    qty = float(pos["qty"])
    if qty <= 0:
        _clear_open_pos(con)
        return {"action": "cleared", "reason": "qty_zero"}
    resp = close_reduce_only(account=account, symbol=symbol, side=side_i, qty=qty)
    record_pivot_fill(
        con,
        "max_hold_flatten",
        {
            "entry_bar_ms": int(pos["entry_bar_ms"]),
            "side": pos["side"],
            "qty": qty,
            "deadline_ms": deadline,
            "response": resp,
        },
    )
    _clear_open_pos(con)
    _log(
        f"MAX_HOLD_FLATTEN side={pos['side']} qty={qty} entry_bar={pos['entry_bar_ms']} "
        f"deadline={deadline} ret={resp.get('retCode')} msg={resp.get('retMsg')}"
    )
    return {
        "action": "flattened",
        "deadline_ms": deadline,
        "entry_bar_ms": int(pos["entry_bar_ms"]),
        "response": resp,
    }


def load_pack(pack_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    strat = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(pack_dir / "model.joblib")
    filt = pack_dir / "filter_head.joblib"
    if filt.is_file():
        blob = dict(blob)
        blob["filter_head"] = joblib.load(filt)
    return strat, blob


def tip_decide(
    *,
    ohlcv: pd.DataFrame,
    strategy: dict[str, Any],
    blob: dict[str, Any],
) -> dict[str, Any]:
    """Score the latest closed bar; return decide payload (no orders)."""
    cols = list(blob["feature_columns"])
    feats = build_feature_frame(ohlcv, pack=str(strategy["feature_pack"]))
    feats = feats.reindex(columns=cols)
    row = feats.iloc[-1]
    bar_ts = int(index_to_ms(ohlcv.index)[-1])
    if row.isna().any():
        return {
            "action": "SKIP",
            "reason": "nan_features",
            "nan_cols": [c for c in cols if pd.isna(row[c])],
            "bar_ts_ms": bar_ts,
        }
    x = row.to_numpy(dtype=float).reshape(1, -1)
    p_raw = np.asarray(blob["any_model"].predict_proba(x), dtype=float).reshape(-1)
    p_any_raw = float(p_raw[1] if p_raw.size > 1 else p_raw[0])
    p_any = float(apply_calibrator(blob["cal_any"], np.array([p_any_raw]))[0])
    thr = float(blob["thr_any"])
    close = float(ohlcv["close"].iloc[-1])
    atr = float(_atr_frac(ohlcv)[-1])

    p_high = 0.5
    if blob.get("high_model") is not None:
        ph = np.asarray(blob["high_model"].predict_proba(x), dtype=float).reshape(-1)
        p_high_raw = float(ph[1] if ph.size > 1 else ph[0])
        if blob.get("cal_high") is not None:
            p_high = float(apply_calibrator(blob["cal_high"], np.array([p_high_raw]))[0])
        else:
            p_high = p_high_raw

    level_ret = 0.0
    if blob.get("level_model") is not None:
        lv = float(np.asarray(blob["level_model"].predict(x), dtype=float).reshape(-1)[0])
        if str(strategy.get("level_mode")) == "atr":
            level_ret = lv * atr if np.isfinite(atr) else lv
        else:
            level_ret = lv

    if str(strategy.get("limit_level") or "") == "atr_clip" and np.isfinite(level_ret) and np.isfinite(atr) and atr > 0:
        # Hunt SOL control: clip |level_ret| into [0.8, 1.5] × ATR fraction.
        level_ret = float(np.sign(level_ret) * np.clip(abs(level_ret), 0.8 * atr, 1.5 * atr))

    gated = p_any >= thr
    filter_payload: dict[str, Any] | None = None
    filt_cfg = strategy.get("filter") if isinstance(strategy.get("filter"), dict) else None
    if filt_cfg:
        head = blob.get("filter_head")
        if not isinstance(head, dict) or head.get("model") is None:
            return {
                "action": "SKIP",
                "reason": "filter_head_missing",
                "bar_ts_ms": bar_ts,
            }
        from llm2.autonomy.filter_head import score_filter_tip

        scored = score_filter_tip(
            ohlcv,
            feature_columns=list(head.get("feature_columns") or filt_cfg.get("feature_columns") or []),
            model=head["model"],
            iso=head.get("iso"),
        )
        pi_star = float(filt_cfg.get("pi_star") or head.get("pi_star") or 0.0)
        filter_payload = {
            "generation": str(filt_cfg.get("generation") or ""),
            "event": str(filt_cfg.get("event") or ""),
            "horizon_bars": int(filt_cfg.get("horizon_bars") or 0),
            "pi_star": pi_star,
            "p_event": scored.get("p_event"),
            "ok": bool(scored.get("ok")),
            "reason": str(scored.get("reason") or ""),
        }
        if not scored.get("ok"):
            return {
                "action": "SKIP",
                "reason": "nan_features",
                "nan_cols": list(scored.get("nan_cols") or []),
                "bar_ts_ms": bar_ts,
                "filter": filter_payload,
            }
        p_evt = float(scored["p_event"])
        if not (np.isfinite(p_evt) and p_evt >= pi_star):
            gated = False
            filter_payload["passed"] = False
        else:
            filter_payload["passed"] = True

    is_short = p_high >= 0.5
    if is_short:
        move = float(np.clip(level_ret if np.isfinite(level_ret) else 0.005, 0.0015, 0.03))
        limit_px = close * (1.0 + move)
        side = "Sell"
    else:
        move = float(np.clip(level_ret if np.isfinite(level_ret) else -0.005, -0.03, -0.0015))
        limit_px = close * (1.0 + move)
        side = "Buy"

    tip_row = ohlcv.iloc[-1]
    feat_vals = [float(row[c]) for c in cols]
    feat_sha = hashlib.sha256(
        json.dumps(feat_vals, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    if gated:
        reason = "p75_and_filter" if filter_payload and filter_payload.get("passed") else "p75_gate"
    elif filter_payload is not None and filter_payload.get("passed") is False:
        reason = "filter_below_pi_star"
    else:
        reason = "below_thr"
    out = {
        "action": "ENTER_LIMIT" if gated else "FLAT",
        "reason": reason,
        "bar_ts_ms": bar_ts,
        "close": close,
        "n_prefix_bars": int(len(ohlcv)),
        "feature_snapshot": {
            "sha256": feat_sha,
            "n_cols": len(cols),
            "values": {c: float(row[c]) for c in cols},
        },
        "tip_ohlc": {
            "open": float(tip_row["open"]),
            "high": float(tip_row["high"]),
            "low": float(tip_row["low"]),
            "close": float(tip_row["close"]),
            "volume": float(tip_row["volume"]) if "volume" in tip_row.index else None,
        },
        "atr_frac": atr,
        "p_any": p_any,
        "p_any_raw": p_any_raw,
        "thr_any": thr,
        "p_high": p_high,
        "level_ret": level_ret,
        "side": side,
        "is_short": bool(is_short),
        "limit_px": float(limit_px),
        "tp_pct": float(strategy["tp_pct"]),
        "sl_pct": float(strategy["sl_pct"]),
        "work_bars": int(strategy["work_bars"]),
        "max_hold_bars": int(strategy["max_hold_bars"]),
        "leverage": float(strategy["leverage"]),
        "symbol": str(strategy["symbol"]),
        "timeframe": str(strategy["timeframe"]),
        "arm_id": str(strategy.get("arm_id")),
    }
    if filter_payload is not None:
        out["filter"] = filter_payload
        out["p_event"] = filter_payload.get("p_event")
        out["pi_star"] = filter_payload.get("pi_star")
    return out


def _round_price(price: float, tick: float) -> float:
    if tick <= 0:
        return float(price)
    return float(round(price / tick) * tick)


def place_working_limit(
    *,
    account: str,
    symbol: str,
    side: str,
    qty: float,
    price: float,
    leverage: float,
) -> dict[str, Any]:
    """Place Bybit Post-Only LIMIT (maker or cancel). TP/SL attached only after fill."""
    ensure_hedge_mode(account=account, symbol=symbol)
    ensure_exchange_leverage(account=account, symbol=symbol, leverage=leverage)
    api_key, api_secret = _load_account_keys(account)
    inst = research_instrument(symbol)
    tick = float(getattr(inst, "tick_size", 0.0) or 0.0)
    px = _round_price(price, tick)
    body = {
        "category": "linear",
        "symbol": symbol.upper(),
        "side": side,
        "orderType": "Limit",
        "qty": _qty_str(qty),
        "price": str(px),
        "timeInForce": "PostOnly",
        "positionIdx": 2 if side == "Sell" else 1,
    }
    resp = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/order/create",
        body=body,
    )
    return {"request": body, "response": resp}


def cancel_order(*, account: str, symbol: str, order_id: str) -> dict[str, Any]:
    api_key, api_secret = _load_account_keys(account)
    return _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="POST",
        path="/v5/order/cancel",
        body={"category": "linear", "symbol": symbol.upper(), "orderId": order_id},
    )


def _order_status(*, account: str, symbol: str, order_id: str) -> dict[str, Any]:
    api_key, api_secret = _load_account_keys(account)
    data = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="GET",
        path="/v5/order/realtime",
        query={"category": "linear", "symbol": symbol.upper(), "orderId": order_id},
        recv="60000",
    )
    rows = list((data.get("result") or {}).get("list") or [])
    if rows:
        return rows[0]
    # Fall back to history
    hist = _bybit_signed_request(
        api_key=api_key,
        api_secret=api_secret,
        method="GET",
        path="/v5/order/history",
        query={"category": "linear", "symbol": symbol.upper(), "orderId": order_id},
        recv="60000",
    )
    hrows = list((hist.get("result") or {}).get("list") or [])
    return hrows[0] if hrows else {"orderStatus": "Unknown", "orderId": order_id}


def cancel_unfilled_entry_keep_exits(
    *,
    account: str | None,
    symbol: str,
    con: sqlite3.Connection,
    reason: str,
) -> dict[str, Any]:
    """Fail-closed for new risk: cancel resting entry LIMIT; never touch TP/SL."""
    out: dict[str, Any] = {"reason": reason, "cancelled": False, "order_id": ""}
    working = _state_get(con, "working_order_id") or ""
    if not working:
        return out
    out["order_id"] = working
    if not account:
        _log(f"DATA_UNSAFE skip cancel (no account) orderId={working} reason={reason}")
        return out
    try:
        cancel_order(account=account, symbol=symbol, order_id=working)
        out["cancelled"] = True
        _log(f"ENTRY_CANCEL_DATA_UNSAFE orderId={working} reason={reason}")
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"{type(exc).__name__}: {exc}"
        _log(f"ENTRY_CANCEL_FAIL orderId={working} err={exc}")
    _state_set(con, "working_order_id", "")
    return out


def _live_data_gate(
    *,
    symbol: str,
    timeframe: str,
    local_tip_ms: int | None,
    persist_flag: bool = True,
) -> tuple[bool, dict[str, Any]]:
    allow, tip_res, flagged = signal_entry_gate(
        symbol=symbol,
        timeframe=timeframe,
        local_tip_ms=local_tip_ms,
        persist_flag=persist_flag,
    )
    payload = {
        "conformance": LIVE_DATA_001,
        "allow_new_entries": bool(allow),
        "tip": tip_res.to_dict(),
        "data_unsafe": flagged,
    }
    return bool(allow), payload


def manage_working_limit(
    *,
    account: str,
    symbol: str,
    side: str,
    qty: float,
    price: float,
    tp_pct: float,
    sl_pct: float,
    leverage: float,
    work_bars: int,
    timeframe: str,
    bar_ts_ms: int,
    con: sqlite3.Connection,
    max_hold_bars: int,
) -> dict[str, Any]:
    """Place LIMIT → wait fill or cancel after work_bars → attach maker exits on fill."""
    placed = place_working_limit(
        account=account,
        symbol=symbol,
        side=side,
        qty=qty,
        price=price,
        leverage=leverage,
    )
    resp = placed.get("response") or {}
    if _bybit_retcode(resp) != 0:
        return {"ok": False, "stage": "place", "placed": placed}
    order_id = str((resp.get("result") or {}).get("orderId") or "")
    if not order_id:
        return {"ok": False, "stage": "place_no_id", "placed": placed}

    work_ms = int(work_bars) * int(TF_MS[timeframe])
    deadline = int(bar_ts_ms) + work_ms + int(TF_MS[timeframe])
    _state_set(con, "working_order_id", order_id)
    _state_set(con, "working_deadline_ms", str(deadline))
    con.execute(
        "INSERT OR REPLACE INTO pivot_orders(order_id, bar_ts_ms, payload_json, created_utc) VALUES (?,?,?,?)",
        (
            order_id,
            int(bar_ts_ms),
            json.dumps({"side": side, "qty": qty, "price": price}, default=str),
            datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        ),
    )
    con.commit()
    _log(f"LIMIT_PLACED orderId={order_id} side={side} qty={qty} px={price}")

    filled = False
    avg_px = float(price)
    last_status = "New"
    st_row: dict[str, Any] = {}
    unsafe_since: float | None = None
    while int(time.time() * 1000) < deadline:
        time.sleep(FILL_POLL_SEC)
        # Heartbeat: if tip/collector goes unsafe, cancel resting entry only.
        # Do not persist a 2-second flap into the shared DATA_UNSAFE flag.
        allow_hb, gate_hb = _live_data_gate(
            symbol=symbol,
            timeframe=timeframe,
            local_tip_ms=None,
            persist_flag=False,
        )
        if allow_hb:
            unsafe_since = None
        else:
            tip_code = str((gate_hb.get("tip") or {}).get("code") or "DATA_UNSAFE")
            now_mono = time.monotonic()
            if unsafe_since is None:
                unsafe_since = now_mono
                _log(f"FILL_WAIT_DATA_UNSAFE wait code={tip_code} orderId={order_id}")
            action = fill_wait_gate_action(
                tip_code,
                first_fail_mono=unsafe_since,
                now_mono=now_mono,
                confirm_timeout_sec=CONFIRM_TIMEOUT_SEC,
            )
            if action == "cancel":
                try:
                    cancel_order(account=account, symbol=symbol, order_id=order_id)
                    _log(
                        f"LIMIT_CANCEL_DATA_UNSAFE orderId={order_id} "
                        f"code={tip_code}"
                    )
                except Exception as exc:  # noqa: BLE001
                    _log(f"CANCEL_FAIL_DATA_UNSAFE orderId={order_id} err={exc}")
                last_status = "CancelledDataUnsafe"
                break
        st_row = _order_status(account=account, symbol=symbol, order_id=order_id)
        last_status = str(st_row.get("orderStatus") or "Unknown")
        if last_status == "Filled":
            filled = True
            avg_px = float(st_row.get("avgPrice") or st_row.get("price") or price)
            break
        if last_status in {
            "Cancelled",
            "Deactivated",
            "Rejected",
            "PartiallyFilledCanceled",
        }:
            # Partial fill still needs protection if size > 0
            cum = float(st_row.get("cumExecQty") or 0)
            if cum > 0:
                filled = True
                avg_px = float(st_row.get("avgPrice") or price)
            break
        # Also detect position if order list races
        pos = _position_list(account=account, symbol=symbol)
        want = "Sell" if side == "Sell" else "Buy"
        for p in pos:
            if str(p.get("side")) == want and float(p.get("size") or 0) > 0:
                filled = True
                avg_px = float(p.get("avgPrice") or price)
                last_status = "FilledViaPosition"
                break
        if filled:
            break
    else:
        # Timeout — cancel resting LIMIT
        try:
            cancel_order(account=account, symbol=symbol, order_id=order_id)
            _log(f"LIMIT_CANCEL_TIMEOUT orderId={order_id}")
        except Exception as exc:  # noqa: BLE001
            _log(f"CANCEL_FAIL orderId={order_id} err={exc}")
        # Re-check fill race
        st_row = _order_status(account=account, symbol=symbol, order_id=order_id)
        last_status = str(st_row.get("orderStatus") or last_status)
        cum = float(st_row.get("cumExecQty") or 0)
        if last_status == "Filled" or cum > 0:
            filled = True
            avg_px = float(st_row.get("avgPrice") or price)

    _state_set(con, "working_order_id", "")
    out: dict[str, Any] = {
        "ok": True,
        "order_id": order_id,
        "filled": filled,
        "status": last_status,
        "avg_price": avg_px,
        "placed": placed,
    }
    if not filled:
        out["stage"] = "not_filled"
        return out

    side_i = -1 if side == "Sell" else 1
    tpsl = ensure_full_position_tpsl(
        account=account,
        symbol=symbol,
        side=side_i,
        avg_price=float(avg_px),
        tp_pct=float(tp_pct),
        sl_pct=float(sl_pct),
        qty=float(qty),
    )
    fill_ms = int(time.time() * 1000)
    for key in ("updatedTime", "updated_time", "createdTime"):
        raw_t = st_row.get(key)
        if raw_t not in (None, ""):
            try:
                fill_ms = int(raw_t)
                break
            except (TypeError, ValueError):
                pass
    entry_bar_ms = entry_bar_open_ms_from_fill(fill_ms, timeframe)
    _record_open_pos(
        con,
        entry_bar_ms=entry_bar_ms,
        side=side,
        qty=float(qty),
        max_hold_bars=int(max_hold_bars),
        sl_px=float(tpsl.get("sl_price") or 0) or None,
        tp_px=float(tpsl.get("tp_price") or 0) or None,
    )
    out["tpsl"] = tpsl
    out["stage"] = "filled_tpsl"
    out["entry_bar_ms"] = entry_bar_ms
    out["max_hold_deadline_ms"] = max_hold_deadline_ms(
        entry_bar_ms, int(max_hold_bars), int(TF_MS[timeframe])
    )
    if _bybit_retcode(tpsl) not in (0, 34040):
        _log(f"TPSL_ATTACH_FAIL ret={tpsl.get('retCode')} msg={tpsl.get('retMsg')} — flatten")
        try:
            flat = close_reduce_only(
                account=account, symbol=symbol, side=side_i, qty=float(qty)
            )
        except Exception as exc:  # noqa: BLE001
            flat = {"error": f"{type(exc).__name__}: {exc}"}
        _clear_open_pos(con)
        out["tpsl"] = tpsl
        out["fail_closed_flatten"] = flat
        out["stage"] = "tpsl_attach_failed"
        out["ok"] = False
        return out
    _log(
        f"TPSL_ATTACHED orderId={order_id} avg={avg_px} mode={tpsl.get('mode')} "
        f"tp={tpsl.get('tp_price')} sl={tpsl.get('sl_price')} tp_ok={tpsl.get('tp_ok')}"
    )
    record_pivot_fill(
        con,
        "entry_filled",
        {
            "order_id": order_id,
            "bar_ts_ms": int(bar_ts_ms),
            "side": side,
            "qty": float(qty),
            "avg_price": float(avg_px),
            "status": last_status,
            "entry_bar_ms": entry_bar_ms,
            "max_hold_deadline_ms": out["max_hold_deadline_ms"],
        },
    )
    return out


def has_open_exposure(*, account: str, symbol: str) -> bool:
    for p in _position_list(account=account, symbol=symbol):
        if float(p.get("size") or 0) > 0:
            return True
    return False


def run_loop(
    *,
    pack_dir: Path,
    state_path: Path,
    mode: str,
    account: str | None,
    cert_path: Path | None,
    live_orders: bool,
    vps_host: str | None,
) -> int:
    strategy, blob = load_pack(pack_dir)
    symbol = str(strategy["symbol"])
    timeframe = str(strategy["timeframe"])
    con = _state_conn(state_path)
    _log(
        f"pivot_runner start arm={strategy.get('arm_id')} symbol={symbol} tf={timeframe} "
        f"mode={mode} live_orders={live_orders} lev={strategy.get('leverage')}"
    )

    if live_orders:
        if cert_path is None:
            raise PolicyError("LIVE_ORDERS requires --cert")
        refuse_vps_deploy_without_live_certificate(path=cert_path, host=vps_host)
        if not account:
            raise PolicyError("LIVE_ORDERS requires --account")
        _load_account_keys(account)  # fail early
        try:
            ensure_hedge_mode(account=account, symbol=symbol)
            ensure_exchange_leverage(
                account=account,
                symbol=symbol,
                leverage=float(strategy.get("leverage") or 29.0),
            )
        except Exception as exc:  # noqa: BLE001
            _log(f"MODE_OR_LEVERAGE_WARN {type(exc).__name__}: {exc}")

    while True:
        # Heartbeat exits: protect orphans, gap-flatten, then max-hold.
        # These run even when DATA_UNSAFE blocks new entries.
        if live_orders and account:
            try:
                rc = reconcile_exchange_position(
                    account=account,
                    symbol=symbol,
                    timeframe=timeframe,
                    con=con,
                    tp_pct=float(strategy.get("tp_pct") or 0.01),
                    sl_pct=float(strategy.get("sl_pct") or 0.01),
                    max_hold_bars=int(strategy.get("max_hold_bars") or 6),
                )
                if rc.get("action") not in {"none"}:
                    _log(f"RECONCILE_TICK {json.dumps(rc, default=str)[:500]}")
            except Exception as exc:  # noqa: BLE001
                _log(f"RECONCILE_WARN {type(exc).__name__}: {exc}")
            try:
                gf = maybe_gap_flatten_taker(account=account, symbol=symbol, con=con)
                if gf.get("action") not in {"none"}:
                    _log(f"GAP_FLATTEN_TICK {json.dumps(gf, default=str)[:500]}")
            except Exception as exc:  # noqa: BLE001
                _log(f"GAP_FLATTEN_WARN {type(exc).__name__}: {exc}")
            try:
                mh = maybe_max_hold_flatten(
                    account=account, symbol=symbol, timeframe=timeframe, con=con
                )
                if mh.get("action") in {"flattened", "cleared"}:
                    _log(f"MAX_HOLD_TICK {json.dumps(mh, default=str)[:400]}")
            except Exception as exc:  # noqa: BLE001
                _log(f"MAX_HOLD_WARN {type(exc).__name__}: {exc}")

        # Heartbeat / catch-up: refuse new entries when tip or collector is unsafe.
        allow0, gate0 = _live_data_gate(
            symbol=symbol, timeframe=timeframe, local_tip_ms=None
        )
        if not allow0:
            tip_code = (gate0.get("tip") or {}).get("code")
            _log(f"DATA_UNSAFE heartbeat code={tip_code} gate={json.dumps(gate0, default=str)[:500]}")
            if live_orders and account:
                cancel_unfilled_entry_keep_exits(
                    account=account,
                    symbol=symbol,
                    con=con,
                    reason=str(tip_code or "DATA_UNSAFE"),
                )
            # Do not spin in the pre-close lead window: retry the inexpensive
            # server-time gate at a bounded heartbeat cadence while fail-closed.
            time.sleep(max(CLOSE_POLL_SEC, 15.0))
            continue

        # Standard 22.1: catch up unprocessed closed bars, else idle until lead_sec
        # before the next close, then fast-poll until the new tip is visible.
        last = _state_get(con, "last_processed_bar_ts")
        # Prefer exchange-server clock for "latest closed" when available.
        try:
            from llm2.live.candle_freshness import fetch_binance_server_time_ms

            server_now = fetch_binance_server_time_ms()
            latest_closed = latest_closed_bar_open_ms(timeframe, now_ms=server_now)
        except Exception:  # noqa: BLE001
            latest_closed = latest_closed_bar_open_ms(timeframe)
        catch_up = last is None or int(last) < int(latest_closed)
        if catch_up:
            _log(f"CATCH_UP last_processed={last} latest_closed={latest_closed}")
        else:
            sleep_until_next_close(
                timeframe,
                lead_sec=LEAD_SEC,
                slice_sec=CLOSE_POLL_SEC,
                abort_check=(
                    (lambda: _max_hold_due(con, timeframe))
                    if live_orders
                    else None
                ),
            )
            if live_orders and account and _max_hold_due(con, timeframe):
                continue

        deadline = time.time() + (5.0 if catch_up else CONFIRM_TIMEOUT_SEC)
        ohlcv: pd.DataFrame | None = None
        bar_ms: int | None = None
        while time.time() < deadline:
            try:
                frame = load_pivot_ohlcv(symbol, timeframe, limit=LIVE_OHLCV_BARS)
            except TipCandleUnstableError as exc:
                _log(f"TIP_UNSTABLE refuse_decide {exc}")
                time.sleep(CLOSE_POLL_SEC)
                continue
            except Exception as exc:  # noqa: BLE001
                _log(f"LOAD_FAIL {exc}")
                time.sleep(CLOSE_POLL_SEC)
                continue
            if frame is None or len(frame) < 2:
                time.sleep(CLOSE_POLL_SEC)
                continue
            tip_ms = int(index_to_ms(frame.index)[-1])
            allow_tip, gate_tip = _live_data_gate(
                symbol=symbol, timeframe=timeframe, local_tip_ms=tip_ms
            )
            if not allow_tip:
                _log(
                    f"CANDLE_STALE refuse_decide {LIVE_DATA_001} "
                    f"code={(gate_tip.get('tip') or {}).get('code')} tip_ms={tip_ms}"
                )
                time.sleep(CLOSE_POLL_SEC)
                continue
            last_now = _state_get(con, "last_processed_bar_ts")
            try:
                from llm2.live.candle_freshness import fetch_binance_server_time_ms

                want = latest_closed_bar_open_ms(
                    timeframe, now_ms=fetch_binance_server_time_ms()
                )
            except Exception:  # noqa: BLE001
                want = latest_closed_bar_open_ms(timeframe)
            if last_now is not None and int(last_now) >= int(want):
                # Woke in the lead window before the bar actually closed.
                time.sleep(CLOSE_POLL_SEC)
                continue
            if tip_ms < int(want):
                _log(f"STALE tip_ms={tip_ms} want={want} — wait")
                time.sleep(CLOSE_POLL_SEC)
                continue
            # Chronological: earliest unprocessed closed bar (not jump to tip).
            if last_now is not None and "ts_ms" in frame.columns:
                pending = frame.loc[frame["ts_ms"].astype("int64") > int(last_now)]
                if pending.empty:
                    time.sleep(CLOSE_POLL_SEC)
                    continue
                bar_ms = int(pending["ts_ms"].astype("int64").iloc[0])
                ohlcv = frame.loc[frame["ts_ms"].astype("int64") <= bar_ms].copy()
            else:
                bar_ms = int(want)
                ohlcv = frame
            break

        if ohlcv is None or bar_ms is None:
            _log("STALE_BAR: no new closed bar within confirm_timeout")
            continue

        decide = tip_decide(ohlcv=ohlcv, strategy=strategy, blob=blob)
        decide["mode"] = mode
        decide["live_orders"] = bool(live_orders)
        decide["created_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        tip_decide_ms = int(index_to_ms(ohlcv.index)[-1])
        allow_dec, gate_dec = _live_data_gate(
            symbol=symbol, timeframe=timeframe, local_tip_ms=tip_decide_ms
        )
        decide["live_data_001"] = gate_dec
        con.execute(
            "INSERT OR REPLACE INTO pivot_decisions(bar_ts_ms, payload_json, created_utc) VALUES (?,?,?)",
            (bar_ms, json.dumps(decide, default=str), decide["created_utc"]),
        )
        con.commit()
        _state_set(con, "last_processed_bar_ts", str(bar_ms))
        _log(f"DECIDE {json.dumps(decide, default=str)}")

        if not allow_dec:
            _log(
                f"DATA_UNSAFE block_entry code={(gate_dec.get('tip') or {}).get('code')} "
                f"— protective exits untouched"
            )
            if live_orders and account:
                cancel_unfilled_entry_keep_exits(
                    account=account,
                    symbol=symbol,
                    con=con,
                    reason=str((gate_dec.get("tip") or {}).get("code") or "DATA_UNSAFE"),
                )
            continue

        if not live_orders or decide.get("action") != "ENTER_LIMIT":
            if (not live_orders) and decide.get("action") == "ENTER_LIMIT":
                _persist_decision_order_result(
                    con,
                    bar_ms=bar_ms,
                    decide=decide,
                    result={"ok": False, "stage": "skip_live_orders_off"},
                )
            continue
        assert account is not None

        # One book: skip if already in a position or working order
        working = _state_get(con, "working_order_id") or ""
        if working:
            _log(f"SKIP_ALREADY_WORKING orderId={working}")
            _persist_decision_order_result(
                con,
                bar_ms=bar_ms,
                decide=decide,
                result={"ok": False, "stage": "skip_already_working", "order_id": working},
            )
            continue
        if has_open_exposure(account=account, symbol=symbol):
            _log("SKIP_OPEN_POSITION")
            _persist_decision_order_result(
                con,
                bar_ms=bar_ms,
                decide=decide,
                result={"ok": False, "stage": "skip_open_position"},
            )
            continue

        # Re-check immediately before placing entry.
        allow_pl, gate_pl = _live_data_gate(
            symbol=symbol, timeframe=timeframe, local_tip_ms=tip_decide_ms
        )
        if not allow_pl:
            pre_code = str((gate_pl.get("tip") or {}).get("code") or "DATA_UNSAFE")
            _log(f"DATA_UNSAFE pre_place block code={pre_code}")
            _persist_decision_order_result(
                con,
                bar_ms=bar_ms,
                decide=decide,
                result={"ok": False, "stage": "pre_place_data_unsafe", "code": pre_code},
            )
            continue

        try:
            inst = research_instrument(symbol)
            equity = None
            if pack_uses_stop_risk_sizing(strategy):
                equity = float(fetch_wallet_equity_usdt(account=account))
            qty, qty_detail = resolve_pivot_live_qty(
                strategy=strategy,
                decide=decide,
                instrument=inst,
                equity=equity,
            )
            decide["qty"] = float(qty)
            decide["qty_detail"] = qty_detail
            if equity is not None:
                decide["wallet_equity_usdt"] = equity
            if qty <= 0:
                _log(f"SKIP_QTY_BELOW_VENUE_OR_RISK_CAP {json.dumps(qty_detail, default=str)[:600]}")
                _persist_decision_order_result(
                    con,
                    bar_ms=bar_ms,
                    decide=decide,
                    result={
                        "ok": False,
                        "stage": "skip_qty_below_min_or_risk_cap",
                        "qty_detail": qty_detail,
                    },
                )
                continue
            result = manage_working_limit(
                account=account,
                symbol=symbol,
                side=str(decide["side"]),
                qty=float(qty),
                price=float(decide["limit_px"]),
                tp_pct=float(decide["tp_pct"]),
                sl_pct=float(decide["sl_pct"]),
                leverage=float(decide["leverage"]),
                work_bars=int(decide["work_bars"]),
                timeframe=timeframe,
                bar_ts_ms=bar_ms,
                con=con,
                max_hold_bars=int(decide["max_hold_bars"]),
            )
        except Exception as exc:  # noqa: BLE001
            _log(f"PLACE_FAIL {type(exc).__name__}: {exc}")
            result = {
                "ok": False,
                "stage": "place_exception",
                "error": f"{type(exc).__name__}: {exc}",
            }
        _log(f"ORDER_RESULT {json.dumps(result, default=str)[:1200]}")
        _persist_decision_order_result(
            con, bar_ms=bar_ms, decide=decide, result=result
        )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pack", type=Path, required=True)
    ap.add_argument("--state", type=Path, required=True)
    ap.add_argument("--mode", choices=("SHADOW", "LIVE"), default="SHADOW")
    ap.add_argument("--account", default=None)
    ap.add_argument("--cert", type=Path, default=None)
    ap.add_argument("--live-orders", action="store_true")
    ap.add_argument("--vps-host", default="94.156.189.76")
    ap.add_argument(
        "--once",
        action="store_true",
        help="Decide tip once and exit (no loop). For parity smoke.",
    )
    args = ap.parse_args(argv)

    if args.live_orders and args.mode != "LIVE":
        raise SystemExit("--live-orders requires --mode LIVE")
    if args.live_orders:
        if args.cert is None:
            raise SystemExit("--live-orders requires --cert")
        refuse_vps_deploy_without_live_certificate(
            path=args.cert, host=str(args.vps_host)
        )

    if args.once:
        strategy, blob = load_pack(args.pack)
        ohlcv = load_pivot_ohlcv(
            str(strategy["symbol"]),
            str(strategy["timeframe"]),
            limit=LIVE_OHLCV_BARS,
        )
        decide = tip_decide(ohlcv=ohlcv, strategy=strategy, blob=blob)
        print(json.dumps(decide, indent=2, default=str))
        return 0

    return run_loop(
        pack_dir=args.pack,
        state_path=args.state,
        mode=args.mode,
        account=args.account,
        cert_path=args.cert,
        live_orders=bool(args.live_orders),
        vps_host=str(args.vps_host) if args.live_orders else None,
    )


if __name__ == "__main__":
    raise SystemExit(main())
