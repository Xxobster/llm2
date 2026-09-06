"""Solana 1-hour Exponential Moving Average stack live runner (Post-Only LIMIT).

No model. The decide is ``llm2.ml_lab.live_signal.tip_signal`` — the same bit and
Average-True-Range bracket the nested settle scores.

SHADOW by default. ``--live-orders`` requires an AUTHORIZED certificate with
four-proof hashes. Expired Post-Only is cancel-and-flat (never a taker rescue).

Quantity is pack-defined:
- Bitcoin ``quad_slope_follow`` and Solana ``hilbert_amp_fade``: 5% of equity
  at that bar's stop, nearest venue step (not the exchange minimum lot).
- Solana ``fvg_confluence``: venue-minimum lot.
- Solana Exponential Moving Average stack: 5% of equity at the bar's stop, floor.
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

from llm2.live.candle_freshness import LIVE_DATA_001
from llm2.live.certificate import refuse_vps_deploy_without_live_certificate
from llm2.live.micro_runner import (
    _load_account_keys,
    ensure_exchange_leverage,
    ensure_hedge_mode,
    fetch_wallet_equity_usdt,
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
from llm2.ml_lab.live_guards import (
    live_spec_for,
    refuse_taker_entry_fallback,
    refuse_venue_min_qty_fallback,
)
from llm2.ml_lab.live_signal import MIN_PREFIX_BARS, tip_signal
from llm2.research_policy import PolicyError
from llm2.sizing_policy import SIZING_MODE_MIN_EXCHANGE, SIZING_MODE_RISK_FRACTION
from llm2.validation.folds import index_to_ms
from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
from tradesim import research_instrument  # noqa: E402
from tradesim.contracts import InstrumentSpec  # noqa: E402

REQUIRED_PACK_KEYS = (
    "arm_id",
    "symbol",
    "timeframe",
    "idea",
    "k_sl",
    "tp_ratio",
    "sl_cap",
    "work_bars",
    "max_hold_bars",
    "leverage",
    "risk_fraction",
)


def load_pack(pack_dir: Path) -> dict[str, Any]:
    strat = json.loads((Path(pack_dir) / "strategy.json").read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED_PACK_KEYS if strat.get(k) in (None, "")]
    if missing:
        raise PolicyError(
            f"ema_stack pack {pack_dir} incomplete: missing {missing}. "
            "Refusing a phantom default cost/bracket/leverage."
        )
    spec = live_spec_for(str(strat["symbol"]), str(strat["timeframe"]), str(strat["idea"]))
    if spec is None:
        raise PolicyError(
            f"pack idea {strat.get('idea')!r} on {strat.get('symbol')} {strat.get('timeframe')} "
            "is not an authorized live formula spec"
        )
    sizing = strat.get("sizing") or {}
    mode = str(sizing.get("mode") or "").upper()
    if mode in {"STOP_RISK_FRACTION", "PCT_EQUITY_AT_SL"}:
        mode = SIZING_MODE_RISK_FRACTION
    idea = str(strat["idea"])
    if idea == "quad_slope_follow":
        if mode != SIZING_MODE_RISK_FRACTION:
            raise PolicyError("Bitcoin quad_slope_follow must size RISK_FRACTION (5% equity at stop)")
        if str(sizing.get("qty_round") or "floor").lower() != "nearest":
            raise PolicyError(
                "Bitcoin quad_slope_follow must use qty_round=nearest "
                "(5% stop-risk, not min-lot floor)"
            )
    elif idea == "hilbert_amp_fade":
        if mode != SIZING_MODE_RISK_FRACTION:
            raise PolicyError(
                "Solana hilbert_amp_fade must size RISK_FRACTION (5% of equity at "
                "that bar's stop), not the exchange minimum lot"
            )
        if str(sizing.get("qty_round") or "floor").lower() != "nearest":
            raise PolicyError(
                "Solana hilbert_amp_fade must use qty_round=nearest "
                "(5% stop-risk, not min-lot floor)"
            )
        pack_rf = float(strat.get("risk_fraction") or 0)
        size_rf = float(sizing.get("risk_fraction") if sizing.get("risk_fraction") is not None else pack_rf)
        if abs(pack_rf - 0.05) > 1e-12 or abs(size_rf - 0.05) > 1e-12:
            raise PolicyError(
                f"Solana hilbert_amp_fade must risk 5% of equity at the bar stop, "
                f"got risk_fraction={pack_rf} sizing.risk_fraction={size_rf}"
            )
    elif idea == "fvg_confluence":
        if mode != SIZING_MODE_MIN_EXCHANGE:
            raise PolicyError(
                "Solana fvg_confluence live pack is venue-minimum size (MIN_EXCHANGE)"
            )
    elif mode != SIZING_MODE_RISK_FRACTION:
        raise PolicyError("ema_stack live pack must size RISK_FRACTION (5% equity at stop)")
    if str(strat.get("expired_entry") or "") != "cancel_and_flat":
        raise PolicyError("expired Post-Only must be cancel_and_flat")
    refuse_taker_entry_fallback(market_on_unfilled=False)
    return strat


def _spec_from_pack(strategy: dict[str, Any]) -> dict[str, Any]:
    spec = live_spec_for(
        str(strategy["symbol"]), str(strategy["timeframe"]), str(strategy["idea"])
    )
    if spec is None:
        raise PolicyError(
            f"pack idea {strategy.get('idea')!r} is not an authorized live formula spec"
        )
    spec.update(
        {
            "symbol": str(strategy["symbol"]),
            "timeframe": str(strategy["timeframe"]),
            "idea": str(strategy["idea"]),
            "k_sl": float(strategy["k_sl"]),
            "tp_ratio": float(strategy["tp_ratio"]),
            "sl_cap": float(strategy["sl_cap"]),
            "work_bars": int(strategy["work_bars"]),
            "max_hold_bars": int(strategy["max_hold_bars"]),
        }
    )
    return spec


def resolve_formula_live_qty(
    *,
    strategy: dict[str, Any],
    decide: dict[str, Any],
    equity: float,
) -> tuple[float, dict[str, Any]]:
    """Quantity from 5% of wallet equity at this bar's stop, not venue minimum."""
    inst = instrument_from_pack(strategy)
    sizing = dict(strategy.get("sizing") or {"mode": SIZING_MODE_RISK_FRACTION, "risk_fraction": 0.05})
    if str(sizing.get("mode") or "").upper() != SIZING_MODE_RISK_FRACTION:
        raise PolicyError("formula live qty must be RISK_FRACTION (5% equity at stop)")
    sizing["risk_fraction"] = float(sizing.get("risk_fraction") or strategy.get("risk_fraction") or 0.05)
    round_mode = str(sizing.get("qty_round") or "floor").lower()
    qty, detail = resolve_order_qty(
        sizing=sizing,
        equity=float(equity),
        leverage=float(decide["leverage"]),
        price=float(decide["limit_px"]),
        size_mult=float(sizing.get("size_mult") or 1.0),
        instrument=inst,
        min_qty_fallback=float(getattr(inst, "min_qty", 0.1) or 0.1),
        force_min_exchange=False,
        sl_pct=float(decide["sl_pct"]),
    )
    refuse_venue_min_qty_fallback(
        qty=float(qty),
        raw_qty=float(detail.get("raw_qty") or 0.0),
        min_qty=float(inst.min_qty),
        qty_step=float(inst.qty_step),
    )
    actual = float(detail.get("actual_risk_fraction") or 0.0)
    if round_mode != "nearest" and float(qty) > 0 and actual > 0.05 + 1e-9:
        raise PolicyError(
            f"qty={qty} would risk {actual:.4%} of equity, above the 5% cap"
        )
    return float(qty), detail


def instrument_from_pack(strategy: dict[str, Any]) -> InstrumentSpec:
    inst = strategy.get("instrument") or {}
    if inst.get("qty_step") is None:
        return research_instrument(str(strategy["symbol"]))
    return InstrumentSpec(
        symbol=str(strategy["symbol"]).upper(),
        tick_size=float(inst.get("tick_size") or 0.01),
        qty_step=float(inst["qty_step"]),
        min_qty=float(inst.get("min_qty") or inst["qty_step"]),
        min_notional=float(inst.get("min_notional") or 5.0),
        max_qty=float(inst.get("max_qty") or 1e9),
        max_leverage=float(inst.get("max_leverage") or 100.0),
    )


def tip_decide(*, ohlcv: pd.DataFrame, strategy: dict[str, Any]) -> dict[str, Any]:
    spec = _spec_from_pack(strategy)
    sig = tip_signal(ohlcv, spec=spec)
    base: dict[str, Any] = {
        "bar_ts_ms": sig.bar_ts_ms,
        "close": sig.close,
        "atr_frac": sig.atr_frac,
        "n_prefix_bars": sig.n_prefix_bars,
        "idea": sig.idea,
        "symbol": str(strategy["symbol"]),
        "timeframe": str(strategy["timeframe"]),
        "arm_id": str(strategy["arm_id"]),
        "geometry": sig.geometry,
        "risk_fraction": float(strategy["risk_fraction"]),
        "leverage": float(strategy["leverage"]),
        "work_bars": int(strategy["work_bars"]),
        "max_hold_bars": int(strategy["max_hold_bars"]),
        "entry": "post_only_limit",
        "expired_entry": "cancel_and_flat",
        "sizing_mode": str((strategy.get("sizing") or {}).get("mode") or SIZING_MODE_RISK_FRACTION),
    }
    if not sig.ok:
        return {
            **base,
            "action": "SKIP",
            "reason": "nan_features",
            "nan_cols": list(sig.nan_cols),
        }
    geom_sha = hashlib.sha256(
        json.dumps(
            [sig.atr_frac, sig.sl_pct, sig.tp_pct, sig.limit_px],
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    tip_row = ohlcv.iloc[-1]
    return {
        **base,
        "action": "ENTER_LIMIT" if sig.fires else "FLAT",
        "reason": "event_fired" if sig.fires else "no_event",
        "event_fired": bool(sig.fires),
        "side": sig.side,
        "is_short": sig.is_short,
        "limit_px": sig.limit_px,
        "tp_pct": sig.tp_pct,
        "sl_pct": sig.sl_pct,
        "geometry_sha256": geom_sha,
        "tip_ohlc": {
            "open": float(tip_row["open"]),
            "high": float(tip_row["high"]),
            "low": float(tip_row["low"]),
            "close": float(tip_row["close"]),
            "volume": float(tip_row["volume"]) if "volume" in tip_row.index else None,
        },
    }


def _reconcile_bracket(con, strategy: dict[str, Any]) -> tuple[float, float]:
    sl_raw = _state_get(con, "open_sl_pct")
    tp_raw = _state_get(con, "open_tp_pct")
    sl_cap = float(strategy["sl_cap"])
    tp_ratio = float(strategy["tp_ratio"])
    sl = float(sl_raw) if sl_raw not in (None, "") else sl_cap
    tp = float(tp_raw) if tp_raw not in (None, "") else (sl_cap * tp_ratio)
    return tp, sl


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
        f"ema_stack_runner start arm={strategy['arm_id']} symbol={symbol} tf={timeframe} "
        f"idea={strategy['idea']} mode={mode} live_orders={live_orders} "
        f"k_sl={strategy['k_sl']} sl_cap={strategy['sl_cap']} lev={strategy['leverage']} "
        f"risk_fraction={strategy['risk_fraction']}"
    )

    if live_orders:
        if cert_path is None:
            raise PolicyError("LIVE_ORDERS requires --cert")
        refuse_vps_deploy_without_live_certificate(
            path=cert_path, host=vps_host, account=account
        )
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
            try:
                tp_r, sl_r = _reconcile_bracket(con, strategy)
                rc = reconcile_exchange_position(
                    account=account,
                    symbol=symbol,
                    timeframe=timeframe,
                    con=con,
                    tp_pct=tp_r,
                    sl_pct=sl_r,
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
                    _state_set(con, "open_sl_pct", "")
                    _state_set(con, "open_tp_pct", "")
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
            if frame is None or len(frame) < MIN_PREFIX_BARS:
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
            equity = float(fetch_wallet_equity_usdt(account=account))
            sizing_mode = str((strategy.get("sizing") or {}).get("mode") or "").upper()
            if sizing_mode in {
                SIZING_MODE_RISK_FRACTION,
                "STOP_RISK_FRACTION",
                "PCT_EQUITY_AT_SL",
            }:
                qty, qty_detail = resolve_formula_live_qty(
                    strategy=strategy, decide=decide, equity=equity
                )
                _log(f"QTY_RISK_FRACTION {json.dumps(qty_detail, default=str)[:800]}")
            else:
                inst = instrument_from_pack(strategy)
                qty, qty_detail = resolve_order_qty(
                    sizing=dict(strategy.get("sizing") or {"mode": SIZING_MODE_MIN_EXCHANGE}),
                    equity=equity,
                    leverage=float(decide["leverage"]),
                    price=float(decide["limit_px"]),
                    size_mult=float((strategy.get("sizing") or {}).get("size_mult") or 1.0),
                    instrument=inst,
                    min_qty_fallback=float(getattr(inst, "min_qty", 0.1) or 0.1),
                    force_min_exchange=False,
                    sl_pct=float(decide["sl_pct"]),
                )
            decide["qty"] = float(qty)
            decide["qty_detail"] = qty_detail
            decide["wallet_equity_usdt"] = equity
            if qty <= 0:
                _log(f"SKIP_QTY_BELOW_VENUE_OR_RISK_CAP {json.dumps(qty_detail, default=str)[:600]}")
                _persist_decision_order_result(
                    con,
                    bar_ms=bar_ms,
                    decide=decide,
                    result={"ok": False, "stage": "skip_qty_below_min_or_risk_cap", "qty_detail": qty_detail},
                )
                continue
            _state_set(con, "open_sl_pct", str(float(decide["sl_pct"])))
            _state_set(con, "open_tp_pct", str(float(decide["tp_pct"])))
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
            if not result.get("filled"):
                _state_set(con, "open_sl_pct", "")
                _state_set(con, "open_tp_pct", "")
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
            path=args.cert, host=str(args.vps_host), account=args.account
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
