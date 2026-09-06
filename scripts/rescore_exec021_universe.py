"""Rescore this project's live units and frozen limit-entry ideas on tradesim 1.1.0.

Fill clock (EXEC-021): decision timeframe places the limit; 1-minute finds the
fill at the limit; take-profit/stop only after that fill.

Does not retune. Does not deploy. Does not peep FORWARD_LOCKBOX_START (2026-05-01+).
Event-study-only rows (no tradesim) are listed as not applicable.

    python -u scripts/rescore_exec021_universe.py --smoke
    python -u scripts/rescore_exec021_universe.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from tradesim import Side  # noqa: E402
from tradesim.version import ENGINE_VERSION  # noqa: E402

from llm2.autonomy.filter_head import predict_filter_proba  # noqa: E402
from llm2.autonomy.packs import build_features_for_guard as autonomy_features  # noqa: E402
from llm2.confluence.sim_arms import (  # noqa: E402
    arm_done,
    jsonable,
    load_arms,
    open_checkpoint,
    run_limit_arm,
    run_market_arm,
    run_signals_bt,
    save_arm,
)
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.diagonal_sr.bar_series import make_bar_series  # noqa: E402
from llm2.edge_lab.sim_atr import run_atr_bracket_arm, run_offset_bracket_arm  # noqa: E402
from llm2.gates.evidence import research_costs_baseline, research_maker_first_costs  # noqa: E402
from llm2.live.pivot_runner import load_pack  # noqa: E402
from llm2.ml_lab.funding_fade import attach_causal_funding, funding_event_mask, funding_signal  # noqa: E402
from llm2.ml_lab.idea_catalog import CHANNEL_IDEAS, channel_levels, channel_offsets, signals_from_ohlcv  # noqa: E402
from llm2.ml_lab.idea_catalog_b import signals_b, signals_b5  # noqa: E402
from llm2.ml_lab.idea_catalog_c import signals_c  # noqa: E402
from llm2.ml_lab.reversal import reversal_confidence, reversal_signal  # noqa: E402
from llm2.ops.process_priority import demote_competitors, raise_current_process  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.pivot.features.packs import build_feature_frame  # noqa: E402
from llm2.pivot.strategy.score_oos import _atr_frac  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.pivot.train.calibration import apply_calibrator  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import build_outer_folds, index_to_ms  # noqa: E402
from scripts.run_diagonal_sr_nested_settle_001 import (  # noqa: E402
    WORK as DSR_WORK,
    MAX_HOLD as DSR_HOLD,
    _Ctx as DsrCtx,
    _limit_atr,
    _run_mask as dsr_run_mask,
)
from scripts.run_edge_lab_hunt_001 import SCREEN_END, _fmt, _screen_end_ms  # noqa: E402
from scripts.run_edge_lab_nested_settle_003_structure_mtf import (  # noqa: E402
    Ctx as EdgeCtx,
    _run as edge_run,
)
from scripts.run_ml_lab_hunt_001_kref_mofe import _plan as plan_001, _predict as predict_001  # noqa: E402
from scripts.run_ml_lab_hunt_002_reversal_control import _plan as plan_002  # noqa: E402
from scripts.run_ml_lab_hunt_003_funding_fade import _plan as plan_003  # noqa: E402
from scripts.run_ml_lab_nested_settle_004_ema_stack import Ctx as EmaCtx, _run as ema_run  # noqa: E402

OUT = ARTIFACTS / "reports" / "exec021"
DB_DIR = ARTIFACTS / "sqlite" / "exec021_universe"
PACKS = _ROOT / "artifacts" / "live_packs"
DROP = ("daily_returns", "trade_pnls", "_bundle", "_window")

# Snapshot 2026-09-01 UTC: systemd llm2* running on ln1/ln2. ln3 had none.
LIVE_FLEET = [
    {
        "host": "ln1",
        "account": "Xxobster4",
        "unit": "llm2-dsr-eth-bu-1h",
        "pack": "diagonal_sr_eth_bounce_upper_1h",
        "family": "dsr",
        "kind": "live",
    },
    {
        "host": "ln1",
        "account": "Xxobster4",
        "unit": "llm2-dsr-sol-bu-1h",
        "pack": "diagonal_sr_sol_bounce_upper_1h",
        "family": "dsr",
        "kind": "live",
    },
    {
        "host": "ln1",
        "account": "Xxobster7",
        "unit": "llm2-pivot-eth-p75-ctrl-atr-w4",
        "pack": "pivot_eth_p75_ctrl_atr_w4",
        "family": "pivot",
        "kind": "live",
    },
    {
        "host": "ln1",
        "account": "Xxobster7",
        "unit": "llm2-pivot-sol-geo-p75-w4",
        "pack": "pivot_sol_geo_tp1_sl1_p75_w4",
        "family": "pivot",
        "kind": "live",
    },
    {
        "host": "ln2",
        "account": "Xxobster8",
        "unit": "llm2-pivot-eth-p75-ctrl-atr-w4",
        "pack": "pivot_eth_p75_ctrl_atr_w4",
        "family": "pivot",
        "kind": "live",
        "note": "same frozen pack as Xxobster7",
    },
    {
        "host": "ln2",
        "account": "Xxobster8",
        "unit": "llm2-pivot-sol-geo-p75-w4",
        "pack": "pivot_sol_geo_tp1_sl1_p75_w4",
        "family": "pivot",
        "kind": "live",
        "note": "same frozen pack as Xxobster7",
    },
    {
        "host": "ln2",
        "account": "Xxobster9",
        "unit": "llm2-pivot-eth-p50-tp05-sl05",
        "pack": "pivot_eth_p50_tp05_sl05_w4",
        "family": "pivot",
        "kind": "live",
    },
    {
        "host": "ln2",
        "account": "Xxobster9",
        "unit": "llm2-pivot-sol-p50-tp05-sl05",
        "pack": "pivot_sol_p50_tp05_sl05_w4",
        "family": "pivot",
        "kind": "live",
    },
    {
        "host": "ln2",
        "account": "Xxobster2",
        "unit": "llm2-autonomy-376-sol-sma540",
        "pack": "autonomy_gen376_sol_sma540_below_h4",
        "family": "autonomy",
        "kind": "live",
    },
    {
        "host": "ln2",
        "account": "Xxobster2",
        "unit": "llm2-autonomy-705-eth-ema1320",
        "pack": "autonomy_gen705_eth_ema1320_below_h4",
        "family": "autonomy",
        "kind": "live",
    },
    {
        "host": "ln2",
        "account": "Xxobster10",
        "unit": "llm2-autonomy-013-sol-atrrel",
        "pack": "autonomy_gen013_sol_atr_rel_cross_up_h8",
        "family": "autonomy",
        "kind": "live",
    },
]


def _lock_ms() -> int:
    return int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)


def _oos_start_ms() -> int:
    return int(pd.Timestamp("2022-01-01", tz="UTC").value // 1_000_000)


def _slim(payload: dict[str, Any]) -> dict[str, Any]:
    out = dict(payload)
    for k in DROP:
        out.pop(k, None)
    return out


def _print_row(aid: str, payload: dict[str, Any]) -> None:
    print(
        f"  {aid} status={payload.get('status')} n={payload.get('n_trades')} "
        f"t/m={_fmt(payload.get('trades_per_month'))} PF={_fmt(payload.get('profit_factor'))} "
        f"WR={_fmt(payload.get('win_rate'))} Sharpe={_fmt(payload.get('sharpe_annualised'))} "
        f"ebr={_fmt(payload.get('entry_bar_exit_rate'))} fill={_fmt(payload.get('fill_pct'))}",
        flush=True,
    )


def _oos_union(ts_ms: np.ndarray) -> np.ndarray:
    folds = build_outer_folds(ts_ms, purge_bars=24, embargo_bars=24)
    mask = np.zeros(len(ts_ms), dtype=bool)
    for f in folds:
        mask |= (ts_ms >= f.oos_start_ms) & (ts_ms < f.oos_end_ms)
    return mask


def _min_live_verdict(row: dict[str, Any]) -> tuple[bool, list[str]]:
    """Operational dust-size test only. Not Shadow-Ready. Not a promotion."""
    fails: list[str] = []
    if row.get("kind") != "live":
        fails.append("not_live")
    if str(row.get("entry_mode") or "limit") == "market" and row.get("family") != "pivot":
        # hunt-002 taker control is not a live candidate
        pass
    n = int(row.get("n_trades") or 0)
    pf = float(row.get("profit_factor") or 0)
    tpm = float(row.get("trades_per_month") or 0)
    ebr = float(row.get("entry_bar_exit_rate") or 1)
    fill = float(row.get("fill_pct") or 0)
    liq = int(row.get("n_liquidations") or 0)
    if n < 50:
        fails.append("n<50")
    if not (np.isfinite(pf) and pf >= 1.20):
        fails.append("pf<1.20")
    if not (np.isfinite(tpm) and 2.0 <= tpm <= 40.0):
        fails.append("trades_per_month")
    if not (np.isfinite(ebr) and ebr <= 0.25):
        fails.append("entry_bar>0.25")
    if not (np.isfinite(fill) and fill >= 0.25):
        fails.append("fill<0.25")
    if liq > 0:
        fails.append("liquidation")
    if float(row.get("tp_pct") or 0) <= 0.005 and float(row.get("sl_pct") or 0) <= 0.005:
        fails.append("0.5pct_geometry")
    return (not fails), fails


def _score_pivot_pack(pack_dir: Path) -> dict[str, Any]:
    strat, blob = load_pack(pack_dir)
    symbol = str(strat["symbol"]).upper()
    tf = str(strat["timeframe"])
    ohlcv = load_ohlcv(symbol, tf)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < _lock_ms()].copy()
    cols = list(blob["feature_columns"])
    feats = build_feature_frame(ohlcv, pack=str(strat["feature_pack"])).reindex(columns=cols)
    x = feats.to_numpy(dtype=float)
    valid = np.isfinite(x).all(axis=1)
    p_any = np.full(len(ohlcv), np.nan)
    p_high = np.full(len(ohlcv), 0.5)
    level = np.zeros(len(ohlcv), dtype=float)
    if int(valid.sum()) < 50:
        return {"status": "TOO_FEW_FEATURES", "n_trades": 0, "n_intent": 0, "symbol": symbol, "timeframe": tf}
    xv = x[valid]
    pr = np.asarray(blob["any_model"].predict_proba(xv), dtype=float)
    raw = pr[:, 1] if pr.ndim == 2 and pr.shape[1] > 1 else pr.reshape(-1)
    p_any[valid] = apply_calibrator(blob["cal_any"], raw)
    if blob.get("high_model") is not None:
        ph = np.asarray(blob["high_model"].predict_proba(xv), dtype=float)
        hraw = ph[:, 1] if ph.ndim == 2 and ph.shape[1] > 1 else ph.reshape(-1)
        if blob.get("cal_high") is not None:
            p_high[valid] = apply_calibrator(blob["cal_high"], hraw)
        else:
            p_high[valid] = hraw
    if blob.get("level_model") is not None:
        level[valid] = np.asarray(blob["level_model"].predict(xv), dtype=float).reshape(-1)
    atr = _atr_frac(ohlcv)
    level_ret = level * atr if str(strat.get("level_mode")) == "atr" else level
    if str(strat.get("limit_level") or "") == "atr_clip":
        mag = np.clip(np.abs(level_ret), 0.8 * np.where(np.isfinite(atr), atr, 0.005), 1.5 * np.where(np.isfinite(atr), atr, 0.03))
        level_ret = np.sign(level_ret) * mag
    thr = float(blob["thr_any"])
    gated = valid & np.isfinite(p_any) & (p_any >= thr)
    filt_cfg = strat.get("filter") if isinstance(strat.get("filter"), dict) else None
    if filt_cfg:
        head = blob.get("filter_head") or {}
        fcols = list(head.get("feature_columns") or filt_cfg.get("feature_columns") or [])
        fx = autonomy_features(ohlcv).reindex(columns=fcols).to_numpy(dtype=float)
        fvalid = np.isfinite(fx).all(axis=1)
        p_evt = np.full(len(ohlcv), np.nan)
        if int(fvalid.sum()):
            p_evt[fvalid] = predict_filter_proba(head["model"], head.get("iso"), fx[fvalid])
        pi_star = float(filt_cfg.get("pi_star") or head.get("pi_star") or 0.0)
        gated = gated & fvalid & np.isfinite(p_evt) & (p_evt >= pi_star)
    ts = index_to_ms(ohlcv.index)
    gated = gated & _oos_union(ts)
    close = ohlcv["close"].to_numpy(dtype=float)
    short = p_high >= 0.5
    lr = np.where(np.isfinite(level_ret), level_ret, np.where(short, 0.005, -0.005))
    move = np.where(short, np.clip(lr, 0.0015, 0.03), np.clip(lr, -0.03, -0.0015))
    limit_px = close * (1.0 + move)
    idx = np.flatnonzero(gated)
    tp = float(strat["tp_pct"])
    sl = float(strat["sl_pct"])
    work = int(strat["work_bars"])
    hold = int(strat["max_hold_bars"])
    sc = make_bar_series(symbol, tf, ohlcv)
    if idx.size < 15:
        return {
            "status": "TOO_FEW_GATED",
            "n_trades": 0,
            "n_intent": int(idx.size),
            "symbol": symbol,
            "timeframe": tf,
            "tp_pct": tp,
            "sl_pct": sl,
        }
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[i]),
            side=Side.SHORT if bool(short[i]) else Side.LONG,
            limit_price=float(limit_px[i]),
            stop_offset=sl,
            target_offset=tp,
            max_hold_bars=hold,
            work_bars=work,
        )
        for i in idx.tolist()
    ]
    sigs, fill = materialize_working_limits(ohlcv, intents, work_bars=work)
    out = run_signals_bt(
        symbol,
        tf,
        ohlcv,
        sigs,
        tag=str(strat.get("arm_id") or pack_dir.name),
        max_hold=hold,
        sl=sl,
        market=False,
        n_intent=int(idx.size),
        fill_pct=float(fill["fill_rate"]),
        costs=research_costs_baseline(),
    )
    out.update(
        {
            "symbol": symbol,
            "timeframe": tf,
            "tp_pct": tp,
            "sl_pct": sl,
            "work_bars": work,
            "max_hold_bars": hold,
            "entry_mode": "limit",
            "n_gated": int(idx.size),
            "pack": pack_dir.name,
            "window": "outer_oos_union_pre_lockbox",
            "engine_version": ENGINE_VERSION,
        }
    )
    return out


def _json_ran(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    blob = json.loads(path.read_text(encoding="utf-8"))
    rows = blob.get("rows") or blob.get("stitched") or []
    return [r for r in rows if str(r.get("status")) == "RAN" and r.get("profit_factor") is not None]


def _other_close_inner(symbol: str, tf: str, index) -> np.ndarray | None:
    other = "ETHUSDT" if symbol == "BTCUSDT" else "BTCUSDT"
    try:
        raw = load_ohlcv(other, tf)
        raw = raw.loc[index_to_ms(raw.index) < _screen_end_ms()]
        aligned = raw["close"].reindex(index).ffill()
        return aligned.to_numpy(dtype=float)
    except Exception:  # noqa: BLE001
        return None


def _atr_from_cfg(symbol: str, tf: str, ohlcv: pd.DataFrame, sig: np.ndarray, cfg: dict, tag: str) -> dict[str, Any]:
    sc = make_bar_series(symbol, tf, ohlcv)
    mask = sig != 0
    gated = np.flatnonzero(mask)
    if gated.size < 15:
        return {"status": "TOO_FEW_GATED", "n_trades": 0, "n_intent": int(gated.size), "tag": tag}
    is_short = sig[gated] < 0
    work_map = cfg.get("work_bars") or {}
    hold_map = cfg.get("max_hold_bars") or {}
    work = int(work_map[tf] if isinstance(work_map, dict) else work_map)
    hold = int(hold_map[tf] if isinstance(hold_map, dict) else hold_map)
    idea = str(cfg.get("idea") or tag.split("|")[-1])
    if idea in CHANNEL_IDEAS:
        lv = channel_levels(ohlcv, idea, timeframe=tf)
        if lv is None:
            return {"status": "NO_CHANNEL", "n_trades": 0, "tag": tag}
        lo, hi = lv
        sl_arr, tp_arr = channel_offsets(sc.close[gated], lo[gated], hi[gated], is_short)
        return run_offset_bracket_arm(
            symbol,
            sc,
            mask,
            is_short,
            sl_arr,
            tp_arr,
            tag=tag,
            market=False,
            work=work,
            max_hold=hold,
            sl_cap=float(cfg["sl_cap"]),
        )
    return run_atr_bracket_arm(
        symbol,
        sc,
        mask,
        is_short,
        tag=tag,
        market=False,
        work=work,
        max_hold=hold,
        k_sl=float(cfg["k_sl"][0] if isinstance(cfg.get("k_sl"), list) else cfg["k_sl"]),
        tp_ratio=float(cfg["tp_ratio"][0] if isinstance(cfg.get("tp_ratio"), list) else cfg["tp_ratio"]),
        sl_cap=float(cfg["sl_cap"]),
    )


def write_report(con, extra: dict[str, Any]) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = [_slim(r) for r in load_arms(con)]
    for r in rows:
        ok, fails = _min_live_verdict(r)
        r["min_live_ok"] = bool(ok) if r.get("kind") == "live" else False
        r["min_live_fails"] = fails if r.get("kind") == "live" else ["not_live"]
    live = [r for r in rows if r.get("kind") == "live"]
    research = [r for r in rows if r.get("kind") != "live"]
    payload = {
        "generation_id": "exec021_universe_rescore",
        "engine_name": "tradesim",
        "engine_version": ENGINE_VERSION,
        "conformance": "EXEC-021",
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "lockbox": FORWARD_LOCKBOX_START,
        "n_rows": len(rows),
        "n_live": len(live),
        "n_research": len(research),
        "n_min_live_ok": sum(1 for r in live if r.get("min_live_ok")),
        "extra": extra,
        "live": live,
        "research": research,
        "all": rows,
    }
    (OUT / "universe_latest.json").write_text(json.dumps(jsonable(payload), indent=2), encoding="utf-8")
    md = [
        "# EXEC-021 fill-clock rescore (tradesim " + ENGINE_VERSION + ")",
        "",
        "**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Not a promotion. Not lockbox.",
        "Fill clock: decision bar places the limit; first 1-minute touch is the fill; take-profit/stop after that fill.",
        "",
        f"Rows: {len(rows)}. Live unique packs scored: {len({r.get('pack') for r in live})}.",
        "",
        "## Live (Virtual Private Server units, this project only)",
        "",
        "| Host | Account | Unit | Pack | n | /month | PF | WR | Sharpe | HAC | ebr | fill | hold | min-live |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    seen_live = set()
    for r in live:
        key = (r.get("unit"), r.get("host"))
        if key in seen_live:
            continue
        seen_live.add(key)
        verdict = "YES" if r.get("min_live_ok") else ",".join(r.get("min_live_fails") or [])
        md.append(
            "| {h} | {a} | `{u}` | `{p}` | {n} | {tm} | {pf} | {wr} | {sh} | {hac} | {ebr} | {fl} | {ho} | {v} |".format(
                h=r.get("host"),
                a=r.get("account"),
                u=r.get("unit"),
                p=r.get("pack"),
                n=r.get("n_trades"),
                tm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")),
                wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")),
                hac=_fmt(r.get("sharpe_hac_annualised")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                fl=_fmt(r.get("fill_pct")),
                ho=_fmt(r.get("avg_hold_bars")),
                v=verdict,
            )
        )
    md += [
        "",
        "## Research (not live)",
        "",
        "| Family | Window | Arm | n | /month | PF | WR | Sharpe | HAC | ebr | fill |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in sorted(research, key=lambda x: (-(float(x.get("profit_factor") or -1)), str(x.get("arm_id")))):
        md.append(
            "| {f} | {w} | `{a}` | {n} | {tm} | {pf} | {wr} | {sh} | {hac} | {ebr} | {fl} |".format(
                f=r.get("family"),
                w=r.get("window"),
                a=r.get("arm_id"),
                n=r.get("n_trades"),
                tm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")),
                wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")),
                hac=_fmt(r.get("sharpe_hac_annualised")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                fl=_fmt(r.get("fill_pct")),
            )
        )
    (OUT / "universe_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return payload


def _save(con, arm_id: str, spec: dict[str, Any], payload: dict[str, Any]) -> None:
    merged = _slim({**spec, **payload, "arm_id": arm_id, "engine_version": ENGINE_VERSION})
    save_arm(con, arm_id, spec, merged)
    _print_row(arm_id, merged)


def run_live(con, *, smoke: bool) -> None:
    unique_packs: dict[str, dict[str, Any]] = {}
    for unit in LIVE_FLEET:
        unique_packs.setdefault(unit["pack"], unit)
    scored: dict[str, dict[str, Any]] = {}
    for pack_name, meta in unique_packs.items():
        if smoke and "eth_bounce_upper" not in pack_name:
            continue
        aid = f"live|{pack_name}"
        if arm_done(con, aid):
            print(f"  skip {aid}", flush=True)
            continue
        print(f"=== LIVE PACK {pack_name} family={meta['family']} ===", flush=True)
        if meta["family"] == "dsr":
            strat = json.loads((PACKS / pack_name / "strategy.json").read_text(encoding="utf-8"))
            spec = {
                "symbol": strat["symbol"],
                "timeframe": strat["timeframe"],
                "generation": strat["generation"],
                "event": strat["event"],
                "tp": float(strat["tp_pct"]),
                "sl": float(strat["sl_pct"]),
            }
            ctx = DsrCtx(spec["symbol"], spec["timeframe"], spec["generation"])
            payload = dsr_run_mask(ctx, spec, ctx.oos_union, aid)
            payload.update(
                {
                    "tp_pct": spec["tp"],
                    "sl_pct": spec["sl"],
                    "work_bars": DSR_WORK[spec["timeframe"]],
                    "max_hold_bars": DSR_HOLD[spec["timeframe"]],
                    "entry_mode": "limit",
                    "window": "outer_oos_union_pre_lockbox",
                    "family": "dsr",
                    "pack": pack_name,
                }
            )
        else:
            payload = _score_pivot_pack(PACKS / pack_name)
            payload["family"] = meta["family"]
        scored[pack_name] = payload
        _save(
            con,
            aid,
            {
                "symbol": payload.get("symbol"),
                "timeframe": payload.get("timeframe"),
                "kind": "live",
                "family": meta["family"],
                "pack": pack_name,
                "window": payload.get("window"),
            },
            payload,
        )
    for unit in LIVE_FLEET:
        if smoke and unit["pack"] not in scored and not arm_done(con, f"live|{unit['pack']}"):
            continue
        aid = f"live|{unit['host']}|{unit['unit']}"
        if arm_done(con, aid):
            continue
        src = f"live|{unit['pack']}"
        rows = {r["arm_id"]: r for r in load_arms(con)}
        if src not in rows:
            continue
        payload = dict(rows[src])
        payload.update({**unit, "kind": "live", "shared_pack": unit["pack"]})
        _save(con, aid, payload, payload)


def run_dsr_research(con) -> None:
    cfg = yaml.safe_load((_ROOT / "configs/preregister/diagonal_sr_nested_settle_001.yaml").read_text(encoding="utf-8"))
    live_events = {("ETHUSDT", "bounce_upper"), ("SOLUSDT", "bounce_upper")}
    for spec in cfg["survivors"]:
        if (spec["symbol"], spec["event"]) in live_events and spec["timeframe"] == "1h":
            continue
        aid = (
            f"research|dsr|{spec['symbol']}|{spec['timeframe']}|{spec['generation']}|"
            f"{spec['event']}|tp{spec['tp']}|sl{spec['sl']}"
        )
        if arm_done(con, aid):
            continue
        print(f"=== DSR research {aid} ===", flush=True)
        ctx = DsrCtx(spec["symbol"], spec["timeframe"], spec["generation"])
        payload = dsr_run_mask(ctx, spec, ctx.oos_union, aid)
        payload.update(
            {
                "kind": "research",
                "family": "dsr",
                "window": "outer_oos_union_pre_lockbox",
                "entry_mode": "limit",
                **spec,
            }
        )
        _save(con, aid, payload, payload)


def run_ema_settle(con) -> None:
    cfg = yaml.safe_load((_ROOT / "configs/preregister/ml_lab_nested_settle_004_ema_stack.yaml").read_text(encoding="utf-8"))
    for spec in cfg["survivors"]:
        aid = f"research|ema004|{spec['symbol']}|{spec['timeframe']}|{spec['idea']}|stitched"
        if arm_done(con, aid):
            continue
        print(f"=== nested settle 004 {aid} ===", flush=True)
        ctx = EmaCtx(spec["symbol"], spec["timeframe"])
        payload = ema_run(ctx, spec, ctx.oos_union, aid, cfg, market=False)
        payload.update(
            {
                "kind": "research",
                "family": "ml_lab_004_ema_stack",
                "window": "outer_oos_union_pre_lockbox",
                "entry_mode": "limit",
                **spec,
            }
        )
        _save(con, aid, payload, payload)


def run_hunt_catalog(con, *, family: str, json_name: str, signals_fn, cfg_path: Path) -> None:
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    picks = _json_ran(ARTIFACTS / "reports" / "ml_lab" / json_name)
    if family == "ml_lab_005b" and not picks:
        picks = [
            {"symbol": s, "timeframe": tf, "idea": idea}
            for tf in cfg["universe"]["event_study_timeframes"]
            for s in cfg["universe"]["symbols"]
            for idea in ("cvd_slope_cross", "cvd_z_fire")
        ]
    ctx: tuple[str, str] | None = None
    ohlcv = None
    sigs = None
    for p in picks:
        symbol, tf, idea = p["symbol"], p["timeframe"], p["idea"]
        aid = f"research|{family}|{symbol}|{tf}|{idea}|inner"
        if arm_done(con, aid):
            continue
        print(f"=== {family} {aid} ===", flush=True)
        key = (symbol, tf)
        if ctx != key:
            raw = load_ohlcv(symbol, tf)
            ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
            if family == "ml_lab_004":
                other = _other_close_inner(symbol, tf, ohlcv.index)
                sigs = signals_from_ohlcv(ohlcv, tf, other_close=other)
            else:
                sigs = signals_fn(ohlcv, tf)
            ctx = key
        assert ohlcv is not None and sigs is not None
        cfg_arm = dict(cfg)
        cfg_arm["idea"] = idea
        payload = _atr_from_cfg(symbol, tf, ohlcv, sigs[idea], cfg_arm, aid)
        payload.update(
            {
                "kind": "research",
                "family": family,
                "window": f"inner_screen_before_{SCREEN_END}",
                "entry_mode": "limit",
                "symbol": symbol,
                "timeframe": tf,
                "idea": idea,
            }
        )
        _save(con, aid, payload, payload)


def run_hunt_001(con) -> None:
    cfg = yaml.safe_load((_ROOT / "configs/preregister/ml_lab_hunt_001_kref_mofe.yaml").read_text(encoding="utf-8"))
    ctx = None
    sc = None
    close = None
    ohlcv = None
    for spec in plan_001(cfg):
        aid = f"research|ml_lab_001|{spec['symbol']}|{spec['timeframe']}|{spec['model']}|inner"
        if arm_done(con, aid):
            continue
        print(f"=== hunt 001 {aid} ===", flush=True)
        key = (spec["symbol"], spec["timeframe"])
        if ctx != key:
            raw = load_ohlcv(spec["symbol"], spec["timeframe"])
            ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
            sc = make_bar_series(spec["symbol"], spec["timeframe"], ohlcv)
            close = sc.close
            ctx = key
        assert sc is not None and close is not None
        pred = predict_001(spec["model"], close, cfg)
        tau = float(cfg["abs_pred_tau"])
        mask = np.isfinite(pred) & (np.abs(pred) >= tau)
        is_short = pred[np.flatnonzero(mask)] < 0
        tf = spec["timeframe"]
        payload = run_atr_bracket_arm(
            spec["symbol"],
            sc,
            mask,
            is_short,
            tag=aid,
            market=False,
            work=int(cfg["work_bars"][tf]),
            max_hold=int(cfg["max_hold_bars"][tf]),
            k_sl=float(cfg["k_sl"][0]),
            tp_ratio=float(cfg["tp_ratio"][0]),
            sl_cap=float(cfg["sl_cap"]),
        )
        payload.update({**spec, "kind": "research", "family": "ml_lab_001", "window": f"inner_screen_before_{SCREEN_END}", "entry_mode": "limit"})
        _save(con, aid, payload, payload)


def run_hunt_002(con) -> None:
    cfg = yaml.safe_load((_ROOT / "configs/preregister/ml_lab_hunt_002_reversal_control.yaml").read_text(encoding="utf-8"))
    ctx = None
    sc = None
    sig = None
    conf = None
    ohlcv = None
    for spec in plan_002(cfg):
        aid = f"research|ml_lab_002|{spec['symbol']}|{spec['timeframe']}|{spec['cost_mode']}|c{spec['conf_min']:.2f}|inner"
        if arm_done(con, aid):
            continue
        print(f"=== hunt 002 {aid} ===", flush=True)
        key = (spec["symbol"], spec["timeframe"])
        if ctx != key:
            raw = load_ohlcv(spec["symbol"], spec["timeframe"])
            ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
            sc = make_bar_series(spec["symbol"], spec["timeframe"], ohlcv)
            sig = reversal_signal(sc.close)
            conf = reversal_confidence(sc.close, roll=int(cfg["roll_bars"]))
            ctx = key
        assert sc is not None and sig is not None and conf is not None
        tau = float(spec["conf_min"])
        mask = (sig != 0) & np.isfinite(conf) & (conf >= tau)
        gated = np.flatnonzero(mask)
        is_short = sig[gated] < 0
        if spec["cost_mode"] == "taker":
            payload = run_market_arm(
                spec["symbol"], sc, mask, is_short, tag=aid, max_hold=int(cfg["max_hold_bars"]),
                tp=float(cfg["tp"]), sl=float(cfg["sl"]), costs=research_costs_baseline(),
            )
            payload["entry_mode"] = "market"
        else:
            lim = sc.close[gated]
            payload = run_limit_arm(
                spec["symbol"], sc, mask, is_short, lim, tag=aid, work=int(cfg["work_bars_maker"]),
                max_hold=int(cfg["max_hold_bars"]), tp=float(cfg["tp"]), sl=float(cfg["sl"]),
                costs=research_maker_first_costs(),
            )
            payload["entry_mode"] = "limit"
        payload.update({**spec, "kind": "research", "family": "ml_lab_002", "window": f"inner_screen_before_{SCREEN_END}"})
        _save(con, aid, payload, payload)


def run_hunt_003(con) -> None:
    cfg = yaml.safe_load((_ROOT / "configs/preregister/ml_lab_hunt_003_funding_fade.yaml").read_text(encoding="utf-8"))
    ctx = None
    sc = None
    rate = None
    new = None
    for spec in plan_003(cfg):
        aid = f"research|ml_lab_003|{spec['symbol']}|{spec['timeframe']}|{spec['side']}|t{spec['abs_tau']:.4f}|inner"
        if arm_done(con, aid):
            continue
        print(f"=== hunt 003 {aid} ===", flush=True)
        key = (spec["symbol"], spec["timeframe"])
        if ctx != key:
            raw = load_ohlcv(spec["symbol"], spec["timeframe"])
            ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
            ohlcv = attach_causal_funding(ohlcv, load_funding(spec["symbol"]))
            sc = make_bar_series(spec["symbol"], spec["timeframe"], ohlcv)
            rate = ohlcv["funding_rate"].to_numpy(dtype=float)
            new = ohlcv["funding_new"].to_numpy(dtype=float) > 0
            ctx = key
        assert sc is not None and rate is not None and new is not None
        mask = funding_event_mask(rate, new, abs_tau=float(spec["abs_tau"]))
        fade = spec["side"] == "fade"
        sig = funding_signal(rate, mask, fade=fade)
        gated = np.flatnonzero(mask)
        is_short = sig[gated] < 0
        payload = run_atr_bracket_arm(
            spec["symbol"], sc, mask, is_short, tag=aid, market=False,
            work=int(cfg["work_bars"]), max_hold=int(cfg["max_hold_bars"]),
            k_sl=float(cfg["k_sl"]), tp_ratio=float(cfg["tp_ratio"]), sl_cap=float(cfg["sl_cap"]),
        )
        payload.update({**spec, "kind": "research", "family": "ml_lab_003", "window": f"inner_screen_before_{SCREEN_END}", "entry_mode": "limit"})
        _save(con, aid, payload, payload)


def run_edge_003(con) -> None:
    cfg = yaml.safe_load((_ROOT / "configs/preregister/edge_lab_nested_settle_003_structure_mtf.yaml").read_text(encoding="utf-8"))
    cache: dict[tuple[str, str, str, int], EdgeCtx] = {}
    survivors = sorted(cfg["survivors"], key=lambda s: (s["timeframe"] != "5m", s["timeframe"], s["symbol"]))
    for spec in survivors:
        aid = (
            f"research|edge003|{spec['symbol']}|{spec['timeframe']}|{spec['event']}|"
            f"{spec['session_filter']}|ksl{spec['k_sl']}|r{spec['tp_ratio']}|stitched"
        )
        if arm_done(con, aid):
            continue
        print(f"=== edge 003 {aid} ===", flush=True)
        key = (spec["symbol"], spec["timeframe"], spec["htf"], int(spec["swing_wing"]))
        if key not in cache:
            cache[key] = EdgeCtx(spec["symbol"], spec["timeframe"], htf=spec["htf"], wing=int(spec["swing_wing"]))
        payload = edge_run(cache[key], spec, cache[key].oos_union, aid, cfg)
        payload.update(
            {
                **spec,
                "kind": "research",
                "family": "edge_lab_003",
                "window": "outer_oos_union_pre_lockbox",
                "entry_mode": "market" if "break" in spec["event"] else "limit",
            }
        )
        _save(con, aid, payload, payload)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--smoke", action="store_true", help="only Ether 1-hour bounce_upper live pack")
    ap.add_argument("--phase", choices=["all", "live", "research"], default="all")
    args = ap.parse_args()
    if ENGINE_VERSION != "1.1.0":
        raise SystemExit(f"REFUSE tradesim {ENGINE_VERSION}; need 1.1.0 with EXEC-021")
    print(f"priority={raise_current_process(high=True)} demoted={demote_competitors()}", flush=True)
    print(f"tradesim={ENGINE_VERSION} lockbox={FORWARD_LOCKBOX_START} smoke={args.smoke}", flush=True)
    DB_DIR.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB_DIR / "rescore.sqlite")
    extra = {
        "ln3_llm2_running": False,
        "structure_units_running": False,
        "note": "ln3 had zero llm2 units. Structure packs are not live. Event-study-only ideas were not re-simulated.",
    }
    if args.phase in ("all", "live"):
        run_live(con, smoke=args.smoke)
        write_report(con, extra)
    if args.smoke:
        write_report(con, extra)
        print(f"SMOKE wrote {OUT / 'universe_latest.md'}", flush=True)
        return 0
    if args.phase in ("all", "research"):
        run_ema_settle(con)
        write_report(con, extra)
        run_dsr_research(con)
        write_report(con, extra)
        run_hunt_catalog(
            con,
            family="ml_lab_004",
            json_name="hunt_004_idea_catalog_latest.json",
            signals_fn=signals_from_ohlcv,
            cfg_path=_ROOT / "configs/preregister/ml_lab_hunt_004_idea_catalog.yaml",
        )
        write_report(con, extra)
        run_hunt_catalog(
            con,
            family="ml_lab_005",
            json_name="hunt_005_orb_structure_latest.json",
            signals_fn=signals_b,
            cfg_path=_ROOT / "configs/preregister/ml_lab_hunt_005_orb_structure.yaml",
        )
        write_report(con, extra)
        run_hunt_catalog(
            con,
            family="ml_lab_006",
            json_name="hunt_006_session_flow_latest.json",
            signals_fn=signals_c,
            cfg_path=_ROOT / "configs/preregister/ml_lab_hunt_006_session_flow.yaml",
        )
        write_report(con, extra)
        run_hunt_catalog(
            con,
            family="ml_lab_005b",
            json_name="hunt_005b_cvd_sparse_latest.json",
            signals_fn=signals_b5,
            cfg_path=_ROOT / "configs/preregister/ml_lab_hunt_005b_cvd_sparse.yaml",
        )
        write_report(con, extra)
        run_hunt_001(con)
        write_report(con, extra)
        run_hunt_002(con)
        write_report(con, extra)
        run_hunt_003(con)
        write_report(con, extra)
        run_edge_003(con)
        write_report(con, extra)
    payload = write_report(con, extra)
    append_ledger(f"EXEC021_RESCORE rows={payload['n_rows']} live={payload['n_live']}", tier=0)
    print(f"WROTE {OUT / 'universe_latest.md'} rows={payload['n_rows']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
