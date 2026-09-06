"""Diagonal support/resistance rule-event live runner (working LIMIT arms).

No model, no calibrator. The decide is the causal occurrence bit from
``llm2.diagonal_sr.live_signal.tip_signal`` — the same function the nested
settle scores — plus the frozen bracket in the pack.

SHADOW by default. ``--live-orders`` requires an AUTHORIZED certificate with
four-proof hashes, plus ``--account``. Missing geometry is refused (no fill).
Order plumbing, LIVE-DATA-001 tip gating, work-bar cancel, take-profit /
stop-loss attach and max-hold flatten are reused from the pivot runner so both
books share one audited execution path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from llm2.diagonal_sr.live_signal import tip_signal
from llm2.live.candle_freshness import LIVE_DATA_001
from llm2.live.certificate import refuse_vps_deploy_without_live_certificate
from llm2.live.micro_runner import (
    _load_account_keys,
    ensure_exchange_leverage,
    ensure_hedge_mode,
    latest_closed_bar_open_ms,
    resolve_order_qty,
    sleep_until_next_close,
)
from llm2.live.pivot_runner import (
    CLOSE_POLL_SEC,
    CONFIRM_TIMEOUT_SEC,
    LEAD_SEC,
    LIVE_OHLCV_BARS,
    TipCandleUnstableError,
    _live_data_gate,
    _log,
    _max_hold_due,
    _persist_decision_order_result,
    _state_conn,
    _state_get,
    _state_set,
    cancel_unfilled_entry_keep_exits,
    has_open_exposure,
    load_pivot_ohlcv,
    manage_working_limit,
    maybe_gap_flatten_taker,
    maybe_max_hold_flatten,
    reconcile_exchange_position,
)
from llm2.research_policy import PolicyError
from llm2.validation.folds import index_to_ms
from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
from tradesim import research_instrument  # noqa: E402

REQUIRED_PACK_KEYS = (
    "arm_id",
    "symbol",
    "timeframe",
    "event",
    "generation",
    "tp_pct",
    "sl_pct",
    "work_bars",
    "max_hold_bars",
    "leverage",
)


def load_pack(pack_dir: Path) -> dict[str, Any]:
    """Load and validate the frozen rule-event strategy (fail loud on gaps)."""
    strat = json.loads((Path(pack_dir) / "strategy.json").read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED_PACK_KEYS if strat.get(k) in (None, "")]
    if missing:
        raise PolicyError(
            f"diagonal_sr pack {pack_dir} incomplete: missing {missing}. "
            "Refusing a phantom default cost/bracket/leverage."
        )
    return strat


def tip_decide(*, ohlcv: pd.DataFrame, strategy: dict[str, Any]) -> dict[str, Any]:
    """Score the latest closed bar for one frozen rule-event arm (no orders)."""
    sig = tip_signal(
        ohlcv,
        event=str(strategy["event"]),
        generation=str(strategy["generation"]),
    )
    base: dict[str, Any] = {
        "bar_ts_ms": sig.bar_ts_ms,
        "close": sig.close,
        "atr_frac": sig.atr_frac,
        "n_prefix_bars": sig.n_prefix_bars,
        "event": sig.event,
        "generation": str(strategy["generation"]),
        "symbol": str(strategy["symbol"]),
        "timeframe": str(strategy["timeframe"]),
        "arm_id": str(strategy["arm_id"]),
        "geometry": sig.geometry,
    }
    if not sig.ok:
        return {
            **base,
            "action": "SKIP",
            "reason": "nan_features",
            "nan_cols": list(sig.nan_cols),
        }

    tip_row = ohlcv.iloc[-1]
    geom_sha = hashlib.sha256(
        json.dumps(
            [sig.geometry.get(k) for k in ("upper", "lower", "channel_upper", "channel_lower", "atr")],
            separators=(",", ":"),
            default=str,
        ).encode("utf-8")
    ).hexdigest()
    return {
        **base,
        "action": "ENTER_LIMIT" if sig.fires else "FLAT",
        "reason": "event_fired" if sig.fires else "no_event",
        "event_fired": bool(sig.fires),
        "side": sig.side,
        "is_short": sig.is_short,
        "limit_px": sig.limit_px,
        "market_entry": sig.market_entry,
        "geometry_sha256": geom_sha,
        "tip_ohlc": {
            "open": float(tip_row["open"]),
            "high": float(tip_row["high"]),
            "low": float(tip_row["low"]),
            "close": float(tip_row["close"]),
            "volume": float(tip_row["volume"]) if "volume" in tip_row.index else None,
        },
        "tp_pct": float(strategy["tp_pct"]),
        "sl_pct": float(strategy["sl_pct"]),
        "work_bars": int(strategy["work_bars"]),
        "max_hold_bars": int(strategy["max_hold_bars"]),
        "leverage": float(strategy["leverage"]),
    }


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
    strategy = load_pack(pack_dir)
    symbol = str(strategy["symbol"])
    timeframe = str(strategy["timeframe"])
    con = _state_conn(state_path)
    _log(
        f"diagonal_sr_runner start arm={strategy['arm_id']} symbol={symbol} tf={timeframe} "
        f"event={strategy['event']} gen={strategy['generation']} mode={mode} "
        f"live_orders={live_orders} tp={strategy['tp_pct']} sl={strategy['sl_pct']} "
        f"lev={strategy['leverage']}"
    )

    if live_orders:
        if cert_path is None:
            raise PolicyError("LIVE_ORDERS requires --cert")
        refuse_vps_deploy_without_live_certificate(path=cert_path, host=vps_host)
        if not account:
            raise PolicyError("LIVE_ORDERS requires --account")
        _load_account_keys(account)
        try:
            ensure_hedge_mode(account=account, symbol=symbol)
            ensure_exchange_leverage(
                account=account, symbol=symbol, leverage=float(strategy["leverage"])
            )
        except Exception as exc:  # noqa: BLE001
            _log(f"MODE_OR_LEVERAGE_WARN {type(exc).__name__}: {exc}")

    while True:
        if live_orders and account:
            # Reconcile before max-hold: an entry that filled while the process
            # was mid-exception is otherwise invisible to local state and carries
            # no protective orders.
            try:
                rc = reconcile_exchange_position(
                    account=account,
                    symbol=symbol,
                    timeframe=timeframe,
                    con=con,
                    tp_pct=float(strategy["tp_pct"]),
                    sl_pct=float(strategy["sl_pct"]),
                    max_hold_bars=int(strategy["max_hold_bars"]),
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

        allow0, gate0 = _live_data_gate(
            symbol=symbol, timeframe=timeframe, local_tip_ms=None
        )
        if not allow0:
            tip_code = (gate0.get("tip") or {}).get("code")
            _log(f"DATA_UNSAFE heartbeat code={tip_code}")
            if live_orders and account:
                cancel_unfilled_entry_keep_exits(
                    account=account,
                    symbol=symbol,
                    con=con,
                    reason=str(tip_code or "DATA_UNSAFE"),
                )
            time.sleep(max(CLOSE_POLL_SEC, 15.0))
            continue

        last = _state_get(con, "last_processed_bar_ts")
        try:
            from llm2.live.candle_freshness import fetch_binance_server_time_ms

            latest_closed = latest_closed_bar_open_ms(
                timeframe, now_ms=fetch_binance_server_time_ms()
            )
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
                    (lambda: _max_hold_due(con, timeframe)) if live_orders else None
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
            if frame is None or len(frame) < 60:
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
                time.sleep(CLOSE_POLL_SEC)
                continue
            if tip_ms < int(want):
                _log(f"STALE tip_ms={tip_ms} want={want} — wait")
                time.sleep(CLOSE_POLL_SEC)
                continue
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

        try:
            decide = tip_decide(ohlcv=ohlcv, strategy=strategy)
        except Exception as exc:  # noqa: BLE001
            _log(f"DECIDE_FAIL {type(exc).__name__}: {exc}")
            time.sleep(CLOSE_POLL_SEC)
            continue
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
                "— protective exits untouched"
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
            qty, qty_detail = resolve_order_qty(
                sizing={"mode": "MIN_EXCHANGE"},
                equity=None,
                leverage=float(decide["leverage"]),
                price=float(decide["limit_px"]),
                size_mult=1.0,
                instrument=inst,
                min_qty_fallback=float(getattr(inst, "min_qty", 0.001) or 0.001),
                force_min_exchange=True,
            )
            decide["qty"] = float(qty)
            decide["qty_detail"] = qty_detail
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
        _persist_decision_order_result(con, bar_ms=bar_ms, decide=decide, result=result)


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
        strategy = load_pack(args.pack)
        ohlcv = load_pivot_ohlcv(
            str(strategy["symbol"]),
            str(strategy["timeframe"]),
            limit=LIVE_OHLCV_BARS,
        )
        decide = tip_decide(ohlcv=ohlcv, strategy=strategy)
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
