#!/usr/bin/env python3
"""Live vs backtest audit for the two LLM2 pivot bots on ln1.

Evidence class: LIVE_BT_PIVOT_RECONCILE_CONTAMINATED (window after lockbox).
Does not authorize deploy. Does not promote readiness.

  python -u scripts/audit_llm2_pivot_live_vs_bt.py --i-accept-lockbox-contamination
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
if "botsgeneral" not in __import__("tradesim").__file__.replace("\\", "/"):
    raise SystemExit("tradesim must load from botsgeneral")

from tradesim import Side
from tradesim.contracts import InstrumentSpec

from llm2.backtest.run import run_strategy_backtest
from llm2.data.loader import load_ohlcv
from llm2.data.macro import load_funding
from llm2.evidence.lockbox_guard import add_lockbox_guard_args, require_lockbox_access
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline
from llm2.live.pivot_runner import LIVE_OHLCV_BARS, load_pack, tip_decide
from llm2.paths import ARTIFACTS, TF_MS
from llm2.pivot.features.packs import build_feature_frame
from llm2.pivot.strategy.score_oos import _atr_frac
from llm2.pivot.train.calibration import apply_calibrator
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits
from llm2.validation.folds import index_to_ms
from tradesim import research_margin, research_sim_limit_entry, research_sizing

DUMP = ARTIFACTS / "reports" / "_xx7_pivot_live_full.json"
VPS_15M = ARTIFACTS / "reports" / "_vps_15m_eth_sol.json"
OUT_JSON = ARTIFACTS / "reports" / "audit_llm2_pivot_live_vs_bt_latest.json"
OUT_MD = ARTIFACTS / "reports" / "audit_llm2_pivot_live_vs_bt_latest.md"
SINCE = datetime(2026, 8, 12, tzinfo=timezone.utc)
SINCE_MS = int(SINCE.timestamp() * 1000)
P_EPS = 1e-9
PX_REL = 1e-8
OHLC_REL = 1e-8

ARMS = (
    {
        "name": "sol",
        "pack": ARTIFACTS / "live_packs" / "pivot_sol_geo_tp1_sl1_p75_w4",
        "vps_key": "SOLUSDT_15m",
        "unit": "llm2-pivot-sol-geo-p75-w4",
    },
    {
        "name": "eth",
        "pack": ARTIFACTS / "live_packs" / "pivot_eth_p75_ctrl_atr_w4",
        "vps_key": "ETHUSDT_15m",
        "unit": "llm2-pivot-eth-p75-ctrl-atr-w4",
    },
)


def utc(ms: int | None) -> str | None:
    if ms is None:
        return None
    return datetime.fromtimestamp(int(ms) / 1000, timezone.utc).isoformat()


def _payloads(dump: dict, arm: str) -> list[dict]:
    rows = dump[arm].get("pivot_decisions") or []
    out = []
    for r in rows:
        p = json.loads(r["payload_json"]) if isinstance(r.get("payload_json"), str) else r["payload_json"]
        out.append(p)
    return out


def _near(a: float, b: float, rel: float = PX_REL) -> bool:
    return abs(float(a) - float(b)) <= max(abs(float(b)) * rel, rel)


def compare_candles(symbol: str, vps_rows: list[dict], ohlcv: pd.DataFrame) -> dict[str, Any]:
    if not vps_rows:
        return {"status": "NO_VPS_SERIES"}
    wh = ohlcv.loc[ohlcv["ts_ms"].astype("int64") >= int(vps_rows[0]["ts_ms"])].copy()
    wh_map = {int(t): (float(o), float(h), float(l), float(c)) for t, o, h, l, c in zip(
        wh["ts_ms"].astype("int64"), wh["open"], wh["high"], wh["low"], wh["close"]
    )}
    n = 0
    mismatch = 0
    missing = 0
    samples = []
    for r in vps_rows:
        ts = int(r["ts_ms"])
        n += 1
        w = wh_map.get(ts)
        if w is None:
            missing += 1
            if len(samples) < 6:
                samples.append({"ts_ms": ts, "utc": utc(ts), "kind": "warehouse_missing"})
            continue
        ok = all(_near(float(r[k]), w[i], OHLC_REL) for i, k in enumerate(("open", "high", "low", "close")))
        if not ok:
            mismatch += 1
            if len(samples) < 8:
                samples.append(
                    {
                        "ts_ms": ts,
                        "utc": utc(ts),
                        "vps": {k: r[k] for k in ("open", "high", "low", "close")},
                        "warehouse": {"open": w[0], "high": w[1], "low": w[2], "close": w[3]},
                    }
                )
    return {
        "n_vps_bars": n,
        "warehouse_missing": missing,
        "ohlc_mismatch": mismatch,
        "match_rate": float((n - missing - mismatch) / n) if n else float("nan"),
        "vps_tip_utc": utc(int(vps_rows[-1]["ts_ms"])),
        "warehouse_tip_utc": utc(int(ohlcv["ts_ms"].astype("int64").iloc[-1])),
        "samples": samples,
        "pass": missing == 0 and mismatch == 0,
    }


def _score_all(ohlcv: pd.DataFrame, strat: dict, blob: dict) -> pd.DataFrame:
    cols = list(blob["feature_columns"])
    feats = build_feature_frame(ohlcv, pack=str(strat["feature_pack"])).reindex(columns=cols)
    ts = ohlcv["ts_ms"].astype("int64").to_numpy()
    close = ohlcv["close"].to_numpy(float)
    atr = _atr_frac(ohlcv)
    X = feats.to_numpy(dtype=float)
    finite = np.isfinite(X).all(axis=1)
    p_raw = np.full(len(ohlcv), np.nan)
    p_high = np.full(len(ohlcv), np.nan)
    level = np.full(len(ohlcv), np.nan)
    if finite.any():
        proba = np.asarray(blob["any_model"].predict_proba(X[finite]), dtype=float)
        raw = proba[:, 1] if proba.ndim == 2 and proba.shape[1] > 1 else proba.reshape(-1)
        p_raw[finite] = raw
        if blob.get("high_model") is not None:
            ph = np.asarray(blob["high_model"].predict_proba(X[finite]), dtype=float)
            p_high[finite] = ph[:, 1] if ph.ndim == 2 and ph.shape[1] > 1 else ph.reshape(-1)
        if blob.get("level_model") is not None:
            level[finite] = np.asarray(blob["level_model"].predict(X[finite]), dtype=float).reshape(-1)
    p_any = apply_calibrator(blob["cal_any"], np.where(np.isfinite(p_raw), p_raw, 0.0))
    p_any = np.where(np.isfinite(p_raw), p_any, np.nan)
    if blob.get("cal_high") is not None and np.isfinite(p_high).any():
        p_high = np.where(
            np.isfinite(p_high),
            apply_calibrator(blob["cal_high"], np.where(np.isfinite(p_high), p_high, 0.0)),
            p_high,
        )
    is_short = p_high >= 0.5
    if str(strat.get("level_mode")) == "atr":
        level_ret = level * atr
    else:
        level_ret = level
    move = np.where(
        is_short,
        np.clip(np.where(np.isfinite(level_ret), level_ret, 0.005), 0.0015, 0.03),
        np.clip(np.where(np.isfinite(level_ret), level_ret, -0.005), -0.03, -0.0015),
    )
    limit = close * (1.0 + move)
    thr = float(blob["thr_any"])
    action = np.where(~np.isfinite(p_any), "SKIP", np.where(p_any >= thr, "ENTER_LIMIT", "FLAT"))
    out = pd.DataFrame(
        {
            "ts_ms": ts,
            "p_any": p_any,
            "p_high": p_high,
            "level_ret": level_ret,
            "limit_px": limit,
            "is_short": is_short,
            "action": action,
        },
        index=ohlcv.index,
    )
    for c in cols:
        out[c] = feats[c].to_numpy(dtype=float)
    return out


def replay_decisions(ohlcv: pd.DataFrame, strat: dict, blob: dict, live_decs: list[dict]) -> dict[str, Any]:
    scored_df = _score_all(ohlcv, strat, blob)
    by_ts = {int(t): i for i, t in enumerate(scored_df["ts_ms"].astype("int64").to_numpy())}
    cols = list(blob["feature_columns"])
    n_action = 0
    n_p = 0
    n_feat = 0
    n_both = 0
    n_tip_bind = 0
    flips = []
    feat_diffs = []
    ts_all = ohlcv["ts_ms"].astype("int64").to_numpy()
    for live in live_decs:
        bar = int(live["bar_ts_ms"])
        i = by_ts.get(bar)
        if i is None:
            continue
        rec = scored_df.iloc[i]
        tip_l = live.get("tip_ohlc") or {}
        tip_row = ohlcv.iloc[i]
        tip_diff = False
        if tip_l:
            for col in ("open", "high", "low", "close"):
                if col in tip_l and tip_l[col] is not None:
                    if not _near(float(tip_l[col]), float(tip_row[col]), OHLC_REL):
                        tip_diff = True
                        break
        if tip_diff:
            n_tip_bind += 1
            frame = ohlcv.loc[ts_all <= bar].iloc[-LIVE_OHLCV_BARS:].copy()
            if frame.empty or int(frame["ts_ms"].astype("int64").iloc[-1]) != bar:
                continue
            for col in ("open", "high", "low", "close", "volume"):
                if col in tip_l and col in frame.columns and tip_l[col] is not None:
                    frame.iloc[-1, frame.columns.get_loc(col)] = float(tip_l[col])
            bt = tip_decide(ohlcv=frame, strategy=strat, blob=blob)
            act = bt.get("action")
            p_any = bt.get("p_any")
            side = bt.get("side")
            feat_bt = (bt.get("feature_snapshot") or {}).get("values") or {}
        else:
            act = rec["action"]
            p_any = rec["p_any"]
            side = "Sell" if bool(rec["is_short"]) else "Buy"
            feat_bt = {c: float(rec[c]) for c in cols if c in rec.index}
        n_both += 1
        act_ok = live.get("action") == act
        p_ok = (
            live.get("p_any") is not None
            and p_any == p_any
            and abs(float(live["p_any"]) - float(p_any)) < P_EPS
        )
        n_action += int(act_ok)
        n_p += int(p_ok)
        lv = (live.get("feature_snapshot") or {}).get("values") or {}
        feat_ok = True
        if lv and feat_bt:
            for k, v in lv.items():
                if k not in feat_bt or abs(float(v) - float(feat_bt[k])) > max(
                    abs(float(feat_bt[k])) * 1e-8, 1e-10
                ):
                    feat_ok = False
                    if len(feat_diffs) < 8:
                        feat_diffs.append({"utc": utc(bar), "col": k, "live": v, "bt": feat_bt.get(k)})
                    break
            n_feat += int(feat_ok)
        if (not act_ok or not p_ok) and len(flips) < 12:
            flips.append(
                {
                    "utc": utc(bar),
                    "live_action": live.get("action"),
                    "bt_action": act,
                    "live_p": live.get("p_any"),
                    "bt_p": float(p_any) if p_any == p_any else None,
                    "live_side": live.get("side"),
                    "bt_side": side,
                    "tip_bound": tip_diff,
                }
            )
    return {
        "n_live_decisions": len(live_decs),
        "n_replayed": n_both,
        "n_tip_bound_recompute": n_tip_bind,
        "action_match": n_action,
        "p_any_match": n_p,
        "feature_match": n_feat,
        "action_match_rate": float(n_action / n_both) if n_both else float("nan"),
        "p_any_match_rate": float(n_p / n_both) if n_both else float("nan"),
        "feature_match_rate": float(n_feat / n_both) if n_both else float("nan"),
        "flips": flips,
        "feature_diffs": feat_diffs,
        "n_feature_compared": sum(
            1 for live in live_decs if (live.get("feature_snapshot") or {}).get("values")
        ),
        "pass": n_both > 0 and n_action == n_both,
    }


def live_intents(live_decs: list[dict], strat: dict) -> tuple[list[LimitIntent], dict[str, int]]:
    counts = {"ENTER_LIMIT": 0, "filled": 0, "cancelled_data_unsafe": 0, "cancelled": 0, "no_result": 0, "place_fail": 0}
    intents: list[LimitIntent] = []
    for p in live_decs:
        if p.get("action") != "ENTER_LIMIT":
            continue
        counts["ENTER_LIMIT"] += 1
        orr = p.get("order_result") or {}
        status = str(orr.get("status") or "")
        if orr.get("filled"):
            counts["filled"] += 1
        elif "CancelledDataUnsafe" in status:
            counts["cancelled_data_unsafe"] += 1
        elif status.startswith("Cancelled") or status == "Cancelled":
            counts["cancelled"] += 1
        elif orr.get("ok") is False:
            counts["place_fail"] += 1
        else:
            counts["no_result"] += 1
        intents.append(
            LimitIntent(
                decision_ts_ms=int(p["bar_ts_ms"]),
                side=Side.SHORT if p.get("is_short") or p.get("side") == "Sell" else Side.LONG,
                limit_price=float(p["limit_px"]),
                stop_offset=float(strat["sl_pct"]),
                target_offset=float(strat["tp_pct"]),
                max_hold_bars=int(strat["max_hold_bars"]),
                work_bars=int(strat["work_bars"]),
                meta={"live_status": status or "unknown", "live_filled": bool(orr.get("filled"))},
            )
        )
    return intents, counts


def _instrument(strat: dict) -> InstrumentSpec:
    inst = strat.get("instrument") or {}
    return InstrumentSpec(
        symbol=str(strat["symbol"]),
        tick_size=float(inst.get("tick_size") or 0.01),
        qty_step=float(inst.get("qty_step") or 0.1),
        min_qty=float(inst.get("min_qty") or 0.1),
        min_notional=float(inst.get("min_notional") or 5.0),
        max_qty=float(inst.get("max_qty") or 1e9),
        max_leverage=float(inst.get("max_leverage") or 100.0),
        maintenance_rate=float(inst.get("maintenance_rate") or 0.005),
        source="pack_strategy_json",
    )


def run_bt(symbol: str, ohlcv: pd.DataFrame, signals: list, *, max_hold: int, tag: str, inst: InstrumentSpec) -> dict:
    if not signals:
        return {"status": "NO_SIGNALS", "n_trades": 0, "trades": []}
    touch = load_ohlcv(symbol, "1m", price_type="last")
    try:
        funding = load_funding(symbol)
        f_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
        f_rt = funding.to_numpy(dtype=float)
    except Exception:
        f_ts = np.asarray([], dtype=np.int64)
        f_rt = np.asarray([], dtype=float)
    bar_ms = ohlcv["ts_ms"].astype("int64").to_numpy()
    sig_ts = np.array([s.ts_ms for s in signals], dtype=np.int64)
    i0 = int(np.searchsorted(bar_ms, int(sig_ts.min()), side="left"))
    i1 = int(np.searchsorted(bar_ms, int(sig_ts.max()), side="right"))
    window = ohlcv.iloc[max(0, i0 - 80) : min(len(ohlcv), i1 + 80)].copy()
    w_ts = window["ts_ms"].astype("int64").to_numpy()
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1])) if len(f_ts) else np.asarray([], dtype=bool)
    start, end = window.index[0], window.index[-1]
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS["15m"])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe="15m",
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe="1m",
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(0.01))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe="15m"),
        instrument=inst,
        funding_ts_ms=f_ts[fmask] if len(f_ts) else None,
        funding_rate=f_rt[fmask] if len(f_ts) else None,
        plot=False,
        print_headline=False,
        store_path=None,
    )
    m = bundle.metrics
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    rows = []
    for t in trades:
        rows.append(
            {
                "entry_ts_ms": int(getattr(t, "entry_ts_ms", 0) or 0),
                "entry_utc": utc(getattr(t, "entry_ts_ms", None)),
                "exit_ts_ms": int(getattr(t, "exit_ts_ms", 0) or 0),
                "exit_utc": utc(getattr(t, "exit_ts_ms", None)),
                "side": int(getattr(t, "side", 0) or 0),
                "entry_price": float(getattr(t, "entry_price", 0) or 0),
                "exit_price": float(getattr(t, "exit_price", 0) or 0),
                "pnl": float(getattr(t, "realized_pnl", 0) or getattr(t, "pnl", 0) or 0),
                "hold_bars": float(getattr(t, "hold_bars", 0) or 0),
                "exit_reason": str(getattr(t, "exit_reason", "") or getattr(t, "tag", "") or ""),
            }
        )
    return {
        "status": "RAN",
        "n_trades": int(getattr(m, "n_trades", len(rows)) or len(rows)),
        "profit_factor": float(getattr(m, "profit_factor", float("nan"))),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "net_pnl": float(getattr(m, "net_pnl", 0.0) or 0.0),
        "trades": rows,
    }


def match_fills(live_decs: list[dict], bt_trades: list[dict], sl_pct: float) -> dict[str, Any]:
    live_fills = []
    for p in live_decs:
        orr = p.get("order_result") or {}
        if p.get("action") != "ENTER_LIMIT" or not orr.get("filled"):
            continue
        live_fills.append(
            {
                "utc": p.get("created_utc"),
                "bar_ts_ms": int(p["bar_ts_ms"]),
                "side": p.get("side"),
                "limit_px": float(p["limit_px"]),
                "avg_price": float(orr.get("avg_price") or p["limit_px"]),
                "status": orr.get("status"),
                "entry_bar_ms": orr.get("entry_bar_ms"),
                "max_hold_deadline_ms": orr.get("max_hold_deadline_ms"),
            }
        )
    matched = []
    used = set()
    for lf in live_fills:
        best = None
        best_dt = 10**18
        for i, bt in enumerate(bt_trades):
            if i in used:
                continue
            dt = abs(int(bt["entry_ts_ms"]) - int(lf["bar_ts_ms"]))
            if dt < best_dt:
                best_dt = dt
                best = (i, bt)
        if best is None:
            matched.append({"live": lf, "bt": None, "note": "no_bt_trade"})
            continue
        i, bt = best
        used.add(i)
        slip = abs(float(lf["avg_price"]) - float(bt["entry_price"])) / max(float(bt["entry_price"]), 1e-9)
        matched.append(
            {
                "live": lf,
                "bt": bt,
                "entry_slip_frac": slip,
                "entry_slip_ok": slip <= max(2.0 * sl_pct, 0.003),
                "same_side": (lf["side"] == "Sell" and int(bt["side"]) < 0)
                or (lf["side"] == "Buy" and int(bt["side"]) > 0),
                "dt_ms": best_dt,
            }
        )
    extra_bt = [bt_trades[i] for i in range(len(bt_trades)) if i not in used]
    return {
        "n_live_fills": len(live_fills),
        "n_bt_trades": len(bt_trades),
        "pairs": matched,
        "extra_bt_trades": extra_bt[:12],
        "n_extra_bt": len(extra_bt),
    }


def write_md(report: dict) -> None:
    lines = [
        "# LLM2 pivot live vs backtest",
        "",
        f"**Maximum earned readiness:** `{report['maximum_earned_readiness']}`",
        f"**Evidence class:** `{report['evidence_class']}`",
        f"**Principal blocker:** {report['principal_blocker']}",
        f"Generated: {report['generated_utc']}",
        "",
        "Only this project's live bots: `llm2-pivot-sol-geo-p75-w4` and `llm2-pivot-eth-p75-ctrl-atr-w4` on ln1. ln3 has no LLM2 units. Structure units stay live-stop.",
        "",
    ]
    for arm in report["arms"]:
        lines += [
            f"## {arm['name'].upper()} `{arm['unit']}`",
            "",
            f"- Candles 15-minute VPS vs warehouse: match_rate={arm['candles'].get('match_rate')} missing={arm['candles'].get('warehouse_missing')} mismatch={arm['candles'].get('ohlc_mismatch')}",
            f"- Decision replay (tip-bound): action {arm['replay'].get('action_match')}/{arm['replay'].get('n_replayed')} ; p_any {arm['replay'].get('p_any_match')}/{arm['replay'].get('n_replayed')} ; features {arm['replay'].get('feature_match')}/{arm['replay'].get('n_replayed')}",
            f"- Live ENTER / filled / cancelled-data-unsafe: {arm['live_counts']}",
            f"- Backtest trades: n={arm['bt'].get('n_trades')} PF={arm['bt'].get('profit_factor')} net={arm['bt'].get('net_pnl')}",
            f"- Fill pairs: live_fills={arm['fills'].get('n_live_fills')} bt={arm['fills'].get('n_bt_trades')} extra_bt={arm['fills'].get('n_extra_bt')}",
            f"- Live fill ledger (pivot_fills): n={arm.get('fill_ledger_n')}",
            "",
        ]
        if arm["replay"].get("flips"):
            lines.append("Action / probability flips:")
            for f in arm["replay"]["flips"][:8]:
                lines.append(f"- {f}")
            lines.append("")
    lines += [
        "## What is working as designed",
        "",
        "- Same frozen pack, threshold 0.35, take-profit 1%, stop 1%, work 4 bars, max-hold 6 bars, minimum-exchange size.",
        "- Live refuses new entries when candle-stale / data-unsafe; backtest has no collector gate, so extra backtest fills are expected.",
        "- Small entry/exit price differences from slippage are allowed.",
        "",
        "## Fixes applied or refused",
        "",
    ]
    for note in report.get("fix_notes") or []:
        lines.append(f"- {note}")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    add_lockbox_guard_args(ap)
    args = ap.parse_args(argv)
    require_lockbox_access(
        experiment_id="audit_llm2_pivot_live_vs_bt",
        window_start=SINCE.date().isoformat(),
        window_end=datetime.now(timezone.utc).date().isoformat(),
        purpose="live_vs_bt_reconcile",
        symbols=["ETHUSDT", "SOLUSDT"],
        accepted_contamination=bool(args.i_accept_lockbox_contamination),
    )
    dump = json.loads(DUMP.read_text(encoding="utf-8"))
    vps15 = json.loads(VPS_15M.read_text(encoding="utf-8")) if VPS_15M.is_file() else {}
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "LIVE_BT_PIVOT_RECONCILE_CONTAMINATED",
        "principal_blocker": "pending",
        "scope": "llm2 pivot units on ln1 only",
        "since_utc": SINCE.isoformat(),
        "arms": [],
        "fix_notes": [],
    }
    blockers = []
    for spec in ARMS:
        print("ARM", spec["name"], flush=True)
        strat, blob = load_pack(spec["pack"])
        symbol = str(strat["symbol"])
        ohlcv = load_ohlcv(symbol, "15m", price_type="last")
        if str(ohlcv.attrs.get("price_type")) != "last":
            raise SystemExit(f"{symbol} 15m loaded price_type={ohlcv.attrs.get('price_type')!r}, want last")
        live_decs = [p for p in _payloads(dump, spec["name"]) if int(p["bar_ts_ms"]) >= SINCE_MS]
        candles = compare_candles(symbol, vps15.get(spec["vps_key"]) or [], ohlcv)
        replay = replay_decisions(ohlcv, strat, blob, live_decs)
        intents, live_counts = live_intents(live_decs, strat)
        sigs, stats = materialize_working_limits(
            ohlcv,
            intents,
            work_bars=int(strat["work_bars"]),
        )
        bt = run_bt(
            symbol,
            ohlcv,
            sigs,
            max_hold=int(strat["max_hold_bars"]),
            tag=f"pivot_{spec['name']}_live_window",
            inst=_instrument(strat),
        )
        fills = match_fills(live_decs, bt.get("trades") or [], float(strat["sl_pct"]))
        fill_ledger = dump.get(spec["name"], {}).get("pivot_fills") or []
        if not candles.get("pass"):
            blockers.append(f"{spec['name']}_candle_mismatch")
        if not replay.get("pass"):
            blockers.append(f"{spec['name']}_signal_mismatch")
        report["arms"].append(
            {
                "name": spec["name"],
                "unit": spec["unit"],
                "symbol": symbol,
                "candles": {k: v for k, v in candles.items() if k != "samples"} | {"samples": candles.get("samples")},
                "replay": {k: v for k, v in replay.items() if k != "scored"},
                "live_counts": live_counts,
                "materialize": stats,
                "bt": {k: v for k, v in bt.items() if k != "trades"} | {"trades": bt.get("trades")},
                "fills": fills,
                "fill_ledger_n": len(fill_ledger),
                "fill_ledger_events": [
                    {
                        "event": r.get("event"),
                        "created_utc": r.get("created_utc"),
                    }
                    for r in fill_ledger[-8:]
                ],
            }
        )
    extra_bt = sum(int(a["fills"].get("n_extra_bt") or 0) for a in report["arms"])
    unsafe = sum(int((a["live_counts"] or {}).get("cancelled_data_unsafe") or 0) for a in report["arms"])
    if any("signal_mismatch" in b for b in blockers):
        report["principal_blocker"] = "live vs backtest ENTER/FLAT action mismatch"
    elif any("candle_mismatch" in b for b in blockers):
        report["principal_blocker"] = "15-minute VPS vs warehouse Open-High-Low-Close mismatch"
    elif unsafe:
        report["principal_blocker"] = (
            f"{unsafe} live ENTER cancelled as data-unsafe; backtest still fills those limits. "
            "Operational gate, not a frozen-pack bug."
        )
    elif extra_bt:
        report["principal_blocker"] = f"{extra_bt} extra backtest fills vs live (data-unsafe / no-touch / skip-open)"
    else:
        report["principal_blocker"] = "none — live signals match backtest; fill count gap is operational"
    report["fix_notes"] = [
        "Did not change take-profit, stop, gate, or work/hold. Those are frozen pack values.",
        "Did not disable the live-data-001 fail-closed gate. Extra backtest trades vs cancelled-data-unsafe lives are expected.",
        "Refreshed warehouse Last+Mark locally (Binance REST reachable) and also fetched on live-network-1 then merged.",
        "Mark stored as source=binance_mark so it cannot overwrite Last (same timestamp primary key).",
        "Live collector still has zero 1-minute rows. Research 1-minute stays in the local warehouse only.",
        "Deployed pivot_fills + 2-second fill poll on live-network-1 (2026-08-20T21:04:07Z). No fills in the three post-restart flat bars.",
    ]
    OUT_JSON.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    write_md(report)
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)
    print("blocker", report["principal_blocker"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
