"""EXEC-021 retest: resting limit + 1-minute fill clock + maker fees.

The illegal clock treated a limit as filled at the decision-bar open, so
take-profit/stop could fire on 1-minute bars *before* the path touched the
limit. tradesim 1.1.0 fills at the first 1-minute touch, then arms exits.

Scores this project's live units and quoted research names. Window is
pre-lockbox (2026-05-01) for nested / live-geometry arms. Hunt 004–006 inner
screens stay before 2022-01-01 and are labelled INNER (not a live vote).

Does not deploy. Does not retune stops. Does not rescore ~1500 autonomy gens.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import threading
from datetime import datetime, timezone
from functools import partial
from pathlib import Path
from typing import Any, Callable

import numpy as np
import yaml

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

import tradesim  # noqa: E402

from llm2.confluence.sim_arms import (  # noqa: E402
    arm_done,
    jsonable,
    load_arms,
    open_checkpoint,
    run_limit_arm,
    save_arm,
)
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.diagonal_sr.bar_series import make_bar_series  # noqa: E402
from llm2.diagonal_sr.events import MARKET_ENTRY_EVENTS  # noqa: E402
from llm2.edge_lab.sim_atr import run_atr_bracket_arm  # noqa: E402
from llm2.gates.evidence import research_maker_first_costs  # noqa: E402
from llm2.ml_lab.idea_catalog import signals_from_ohlcv  # noqa: E402
from llm2.ml_lab.idea_catalog_b import signals_b  # noqa: E402
from llm2.ml_lab.idea_catalog_c import signals_c  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402
from scripts.run_diagonal_sr_nested_settle_001 import (  # noqa: E402
    MAX_HOLD as DSR_HOLD,
    WORK as DSR_WORK,
    _Ctx as DsrCtx,
    _limit_atr,
    _side,
)
from scripts.run_edge_lab_hunt_001 import _screen_end_ms  # noqa: E402
from scripts.run_ml_lab_nested_settle_004_ema_stack import Ctx as EmaCtx  # noqa: E402

_HUNT = importlib.util.spec_from_file_location(
    "hunt002_exec021", _ROOT / "scripts" / "run_confluence_autonomous_hunt_002.py"
)
_hunt002 = importlib.util.module_from_spec(_HUNT)
assert _HUNT.loader is not None
_HUNT.loader.exec_module(_hunt002)

OUT = ARTIFACTS / "reports" / "exec021"
DB = ARTIFACTS / "sqlite" / "exec021_maker_limit_retest" / "retest.sqlite"
DSR_YAML = _ROOT / "configs" / "preregister" / "diagonal_sr_nested_settle_001.yaml"
COSTS = research_maker_first_costs()

LIVE_DSR_KEYS = {
    ("ETHUSDT", "1h", "bounce_upper"): {
        "host": "ln1",
        "account": "Xxobster4",
        "unit": "llm2-dsr-eth-bu-1h",
    },
    ("SOLUSDT", "1h", "bounce_upper"): {
        "host": "ln1",
        "account": "Xxobster4",
        "unit": "llm2-dsr-sol-bu-1h",
    },
}

PIVOT_LIVE = (
    {
        "id": "live_pivot_eth_15m_1pct",
        "live": True,
        "host": "ln1+ln2",
        "account": "Xxobster7/8",
        "unit": "llm2-pivot-eth-p75-ctrl-atr-w4",
        "symbol": "ETHUSDT",
        "timeframe": "15m",
        "tp": 0.01,
        "sl": 0.01,
        "note": "1%/1% geometry of the live pivot (p75 is an extra filter)",
    },
    {
        "id": "live_pivot_sol_15m_1pct",
        "live": True,
        "host": "ln1+ln2",
        "account": "Xxobster7/8",
        "unit": "llm2-pivot-sol-geo-p75-w4",
        "symbol": "SOLUSDT",
        "timeframe": "15m",
        "tp": 0.01,
        "sl": 0.01,
        "note": "1%/1% geometry of the live pivot (p75 is an extra filter)",
    },
    {
        "id": "live_pivot_eth_15m_050",
        "live": True,
        "host": "ln2",
        "account": "Xxobster9",
        "unit": "llm2-pivot-eth-p50-tp05-sl05",
        "symbol": "ETHUSDT",
        "timeframe": "15m",
        "tp": 0.005,
        "sl": 0.005,
        "note": "0.5%/0.5% live; historically high entry-bar exits",
    },
    {
        "id": "live_pivot_sol_15m_050",
        "live": True,
        "host": "ln2",
        "account": "Xxobster9",
        "unit": "llm2-pivot-sol-p50-tp05-sl05",
        "symbol": "SOLUSDT",
        "timeframe": "15m",
        "tp": 0.005,
        "sl": 0.005,
        "note": "0.5%/0.5% live; historically high entry-bar exits",
    },
)

PIVOT_RESEARCH = (
    {
        "id": "pivot_btc_15m_1pct",
        "live": False,
        "symbol": "BTCUSDT",
        "timeframe": "15m",
        "tp": 0.01,
        "sl": 0.01,
        "note": "same 1%/1% control geometry, not a live unit",
    },
)

EMA_NESTED = (
    {
        "id": "sol_1h_power_ema_stack_long",
        "live": False,
        "symbol": "SOLUSDT",
        "timeframe": "1h",
        "idea": "power_ema_stack_long",
        "window": "pre_lockbox_oos",
    },
    {
        "id": "btc_4h_power_ema_stack_long",
        "live": False,
        "symbol": "BTCUSDT",
        "timeframe": "4h",
        "idea": "power_ema_stack_long",
        "window": "pre_lockbox_oos",
    },
)

HUNT004_INNER = (
    {"symbol": "SOLUSDT", "timeframe": "4h", "idea": "power_ema_stack_long"},
    {"symbol": "ETHUSDT", "timeframe": "4h", "idea": "power_ema_stack_long"},
    {"symbol": "SOLUSDT", "timeframe": "4h", "idea": "mix_turtle_hurst"},
    {"symbol": "ETHUSDT", "timeframe": "15m", "idea": "power_vol_expand"},
    {"symbol": "ETHUSDT", "timeframe": "1h", "idea": "power_ema_stack_long"},
    {"symbol": "SOLUSDT", "timeframe": "1h", "idea": "mix_turtle_hurst"},
    {"symbol": "BTCUSDT", "timeframe": "4h", "idea": "surf_linreg_channel"},
)

HUNT005_INNER = (
    {"symbol": "SOLUSDT", "timeframe": "1h", "idea": "wick_reject_follow"},
    {"symbol": "SOLUSDT", "timeframe": "4h", "idea": "cvd_slope"},
    {"symbol": "ETHUSDT", "timeframe": "4h", "idea": "cvd_slope"},
    {"symbol": "SOLUSDT", "timeframe": "15m", "idea": "wick_reject_follow"},
)

HUNT006_INNER = (
    {"symbol": "SOLUSDT", "timeframe": "4h", "idea": "outside_bar_follow"},
    {"symbol": "SOLUSDT", "timeframe": "4h", "idea": "close_streak_fade"},
    {"symbol": "SOLUSDT", "timeframe": "1h", "idea": "close_streak_fade"},
    {"symbol": "BTCUSDT", "timeframe": "4h", "idea": "macd_hist_cross"},
    {"symbol": "SOLUSDT", "timeframe": "1h", "idea": "utc_vwap_reclaim"},
    {"symbol": "ETHUSDT", "timeframe": "4h", "idea": "close_streak_follow"},
)

ATR_WORK = {"15m": 4, "1h": 3, "4h": 2}
ATR_HOLD = {"15m": 24, "1h": 16, "4h": 8}

AUTONOMY_LIVE = (
    {
        "id": "live_autonomy_376_sol_sma540",
        "live": True,
        "host": "ln2",
        "account": "Xxobster2",
        "unit": "llm2-autonomy-376-sol-sma540",
        "gen": "376",
        "symbol": "SOLUSDT",
        "timeframe": "15m",
        "event": "sma540_below_at_h",
        "horizon": 4,
        "work": 5,
    },
    {
        "id": "live_autonomy_705_eth_ema1320",
        "live": True,
        "host": "ln2",
        "account": "Xxobster2",
        "unit": "llm2-autonomy-705-eth-ema1320",
        "gen": "705",
        "symbol": "ETHUSDT",
        "timeframe": "15m",
        "event": "ema1320_below_at_h",
        "horizon": 4,
        "work": 4,
    },
    {
        "id": "live_autonomy_013_sol_atrrel",
        "live": True,
        "host": "ln2",
        "account": "Xxobster10",
        "unit": "llm2-autonomy-013-sol-atrrel",
        "gen": "013",
        "symbol": "SOLUSDT",
        "timeframe": "15m",
        "event": "atr_rel_cross_up_1",
        "horizon": 8,
        "work": 5,
    },
)

_DSR_CTX: dict[tuple[str, str, str], Any] = {}
_PIVOT_CTX: dict[str, Any] = {}
_EMA_CTX: dict[tuple[str, str], Any] = {}
_AUTO_CTX: dict[str, Any] = {}


def require_engine() -> dict[str, str]:
    path = str(tradesim.__file__)
    if "botsgeneral" not in path.lower():
        raise SystemExit(f"tradesim not botsgeneral: {path}")
    if str(tradesim.__version__) != "1.1.0":
        raise SystemExit(f"need tradesim 1.1.0, got {tradesim.__version__}")
    return {"tradesim_file": path, "tradesim_version": str(tradesim.__version__)}


def fmt(v: Any, nd: int = 3) -> str:
    try:
        x = float(v)
    except (TypeError, ValueError):
        return ""
    if not np.isfinite(x):
        return ""
    return f"{x:.{nd}f}"


def min_live_vote(row: dict[str, Any]) -> str:
    """Minimum-size Post-Only test vote. Not a Shadow-Ready stamp. Not a deploy."""
    if row.get("status") != "RAN":
        return "no"
    if row.get("window") == "inner_pre_2022":
        return "no_inner_only"
    try:
        n = int(row.get("n_trades") or 0)
        pf = float(row.get("profit_factor"))
        ebr = float(row.get("entry_bar_exit_rate"))
        tpm = float(row.get("trades_per_month"))
    except (TypeError, ValueError):
        return "no"
    if n < 50 or not np.isfinite(pf) or pf < 1.20:
        return "no"
    if not np.isfinite(ebr) or ebr > 0.25:
        return "no_entry_bar_noise"
    if not np.isfinite(tpm) or tpm < 2.0 or tpm > 40.0:
        return "no"
    return "yes_min_size_limit_only"


def _slim(sim: dict[str, Any]) -> dict[str, Any]:
    keep = (
        "status",
        "n_intent",
        "n_trades",
        "trades_per_month",
        "profit_factor",
        "win_rate",
        "entry_bar_exit_rate",
        "fill_pct",
        "sharpe_annualised",
        "sharpe_hac_annualised",
        "net_pnl",
        "expectancy",
        "total_fees",
        "n_liquidations",
        "touch_timeframe",
        "touch_resolved_rate",
        "ambiguous_rate",
        "avg_hold_bars",
        "span_days",
        "error",
    )
    return {k: sim.get(k) for k in keep}


def _heartbeat(label: str) -> threading.Event:
    stop = threading.Event()

    def _run() -> None:
        n = 0
        while not stop.wait(60):
            n += 1
            print(f"  ... still {label} {n}m", flush=True)

    threading.Thread(target=_run, daemon=True).start()
    return stop


def _dsr_specs() -> list[dict[str, Any]]:
    cfg = yaml.safe_load(DSR_YAML.read_text(encoding="utf-8"))
    out: list[dict[str, Any]] = []
    for spec in cfg["survivors"]:
        key = (spec["symbol"], spec["timeframe"], spec["event"])
        live_meta = LIVE_DSR_KEYS.get(key)
        sid = (
            f"{'live_dsr' if live_meta else 'dsr'}_"
            f"{spec['symbol'][:3].lower()}_{spec['event']}_{spec['timeframe']}"
        )
        row = {
            **spec,
            "id": sid,
            "live": bool(live_meta),
            "window": "pre_lockbox_oos",
        }
        if live_meta:
            row.update(live_meta)
        out.append(row)
    return out


def _dsr(spec: dict[str, Any]) -> dict[str, Any]:
    key = (spec["symbol"], spec["timeframe"], spec["generation"])
    if key not in _DSR_CTX:
        print(f"  DSR context {key}", flush=True)
        _DSR_CTX[key] = DsrCtx(*key)
    ctx = _DSR_CTX[key]
    occ = ctx.pack.occurrence[spec["event"]].to_numpy(dtype=float) >= 0.5
    side = _side(spec["event"], len(ctx.ohlcv))
    mask = ctx.oos_union & occ & (side != 0)
    is_short = (side < 0)[np.flatnonzero(mask)]
    if spec["event"] in MARKET_ENTRY_EVENTS:
        from llm2.confluence.sim_arms import run_market_arm

        return run_market_arm(
            spec["symbol"],
            ctx.sc,
            mask,
            is_short,
            tag=spec["id"],
            max_hold=DSR_HOLD[spec["timeframe"]],
            tp=float(spec["tp"]),
            sl=float(spec["sl"]),
            costs=COSTS,
        )
    lim = _limit_atr(ctx.sc, mask, is_short)
    return run_limit_arm(
        spec["symbol"],
        ctx.sc,
        mask,
        is_short,
        lim,
        tag=spec["id"],
        work=DSR_WORK[spec["timeframe"]],
        max_hold=DSR_HOLD[spec["timeframe"]],
        tp=float(spec["tp"]),
        sl=float(spec["sl"]),
        costs=COSTS,
    )


def _pivot(spec: dict[str, Any]) -> dict[str, Any]:
    from llm2.pivot.strategy.score_oos import limit_price_side

    symbol = spec["symbol"]
    if symbol not in _PIVOT_CTX:
        print(f"  pivot context {symbol}", flush=True)
        _PIVOT_CTX[symbol] = _hunt002._Ctx(symbol, "15m", 120_000)
    ctx = _PIVOT_CTX[symbol]
    mask = ctx.ctrl_mask & ctx.in_test
    if ctx.level_override is not None:
        old = ctx.sc.level_ret
        ctx.sc.level_ret = ctx.level_override
        _, is_s, lim = limit_price_side(ctx.sc, mask)
        ctx.sc.level_ret = old
    else:
        _, is_s, lim = limit_price_side(ctx.sc, mask)
    return run_limit_arm(
        spec["symbol"],
        ctx.sc,
        mask,
        is_s,
        lim,
        tag=spec["id"],
        work=ctx.work_ctrl,
        max_hold=6,
        tp=float(spec["tp"]),
        sl=float(spec["sl"]),
        costs=COSTS,
    )


def _ema(spec: dict[str, Any]) -> dict[str, Any]:
    key = (spec["symbol"], spec["timeframe"])
    if key not in _EMA_CTX:
        print(f"  EMA context {key}", flush=True)
        _EMA_CTX[key] = EmaCtx(*key)
    ctx = _EMA_CTX[key]
    sig = ctx.sig[spec["idea"]]
    mask = (sig != 0) & ctx.oos_union
    is_short = sig[np.flatnonzero(mask)] < 0
    tf = spec["timeframe"]
    return run_atr_bracket_arm(
        spec["symbol"],
        ctx.sc,
        mask,
        is_short,
        tag=spec["id"],
        market=False,
        work=ATR_WORK[tf],
        max_hold=ATR_HOLD[tf],
        k_sl=1.5,
        tp_ratio=1.5,
        sl_cap=0.030,
        costs=COSTS,
    )


def _inner_atr(spec: dict[str, Any], *, catalog: str) -> dict[str, Any]:
    raw = load_ohlcv(spec["symbol"], spec["timeframe"])
    ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
    sc = make_bar_series(spec["symbol"], spec["timeframe"], ohlcv)
    tf = spec["timeframe"]
    if catalog == "a":
        other = "ETHUSDT" if spec["symbol"] == "BTCUSDT" else "BTCUSDT"
        o2 = load_ohlcv(other, tf)
        o2 = o2.loc[index_to_ms(o2.index) < _screen_end_ms()]
        aligned = o2["close"].reindex(ohlcv.index).ffill()
        sigs = signals_from_ohlcv(ohlcv, tf, other_close=aligned.to_numpy(dtype=float))
    elif catalog == "b":
        sigs = signals_b(ohlcv, tf)
    else:
        sigs = signals_c(ohlcv, tf)
    sig = sigs[spec["idea"]]
    mask = sig != 0
    is_short = sig[np.flatnonzero(mask)] < 0
    return run_atr_bracket_arm(
        spec["symbol"],
        sc,
        mask,
        is_short,
        tag=spec["id"],
        market=False,
        work=ATR_WORK[tf],
        max_hold=ATR_HOLD[tf],
        k_sl=1.5,
        tp_ratio=1.5,
        sl_cap=0.030,
        costs=COSTS,
    )


def _autonomy(spec: dict[str, Any]) -> dict[str, Any]:
    from llm2.pivot.strategy.ev import net_bracket_magnitudes
    from scripts.run_autonomy_public_indicator_hunt import (
        _Ctx,
        _map_to_sc,
        _pivot_side_lim,
    )

    gen = spec["gen"]
    if gen not in _AUTO_CTX:
        db_dir = ARTIFACTS / "sqlite" / f"autonomy_gen_{gen}"
        cache = db_dir / "cache"
        db_dir.mkdir(parents=True, exist_ok=True)
        print(f"  autonomy context gen={gen} {spec['symbol']}", flush=True)
        _AUTO_CTX[gen] = _Ctx(spec["symbol"], "15m", 120_000, gen, db_dir, cache)
    ctx = _AUTO_CTX[gen]
    mag = net_bracket_magnitudes(0.01, 0.01)
    p_te = ctx.head(int(spec["horizon"]), spec["event"])
    p_sc = _map_to_sc(ctx.sc, ctx.test_df.index, p_te)
    gated = np.isfinite(p_sc) & (p_sc >= float(mag.pi_star)) & ctx.in_test
    mask = gated & ctx.ctrl_mask
    is_s, lim = _pivot_side_lim(ctx, mask)
    return run_limit_arm(
        spec["symbol"],
        ctx.sc,
        mask,
        is_s,
        lim,
        tag=spec["id"],
        work=int(spec["work"]),
        max_hold=6,
        tp=0.01,
        sl=0.01,
        costs=COSTS,
    )


def write_report(con, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    for r in rows:
        r["min_live_test"] = min_live_vote(r)
    live = [r for r in rows if r.get("live")]
    research = [r for r in rows if not r.get("live")]
    yes = [r for r in rows if r.get("min_live_test") == "yes_min_size_limit_only"]
    payload = {
        "generation_id": "exec021_maker_limit_retest",
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "engine": extra,
        "n_rows": len(rows),
        "n_live": len(live),
        "n_research": len(research),
        "n_min_live_yes": len(yes),
        "min_live_yes_ids": [r.get("id") for r in yes],
        "live": live,
        "research": research,
        "all": rows,
        "scope_note": (
            "Live = currently authorized LLM2 units on ln1/ln2 "
            "(pivot, diagonal support/resistance, autonomy 376/705/013). "
            "Not Extreme Gradient Boosting / Time-Series Momentum / Crypthor. "
            "Not ~1500 other autonomy gens."
        ),
    }
    (OUT / "exec021_maker_limit_retest_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )

    def live_line(r: dict) -> str:
        return (
            f"| `{r.get('id')}` | {r.get('unit') or ''} | {r.get('n_trades')} | "
            f"{fmt(r.get('trades_per_month'))} | {fmt(r.get('profit_factor'))} | "
            f"{fmt(r.get('win_rate'))} | {fmt(r.get('entry_bar_exit_rate'))} | "
            f"{fmt(r.get('fill_pct'))} | {fmt(r.get('sharpe_annualised'))} | "
            f"{r.get('min_live_test')} |"
        )

    md = [
        "# EXEC-021 maker-limit retest",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Engine tradesim {extra.get('tradesim_version')}.",
        "Resting limit, first 1-minute touch is the fill, maker 0.02% on resting legs.",
        "Take-profit/stop armed only after that fill. Not a Shadow-Ready stamp. Not a deploy.",
        "",
        f"Min-size Post-Only vote (not already live): **{len([r for r in yes if not r.get('live')])}** research names. "
        f"Already-live names that still pass the same bar: **{len([r for r in yes if r.get('live')])}**.",
        "",
        "## Live (this project, currently authorized units)",
        "",
        "| Id | Unit | n | /mo | PF | WR | ebr | fill | Sharpe | min-live? |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in live:
        md.append(live_line(r))
    md += [
        "",
        "## Research / not currently live",
        "",
        "| Id | n | /mo | PF | WR | ebr | fill | Sharpe | min-live? |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in research:
        md.append(
            f"| `{r.get('id')}` | {r.get('n_trades')} | {fmt(r.get('trades_per_month'))} | "
            f"{fmt(r.get('profit_factor'))} | {fmt(r.get('win_rate'))} | "
            f"{fmt(r.get('entry_bar_exit_rate'))} | {fmt(r.get('fill_pct'))} | "
            f"{fmt(r.get('sharpe_annualised'))} | {r.get('min_live_test')} |"
        )
    (OUT / "exec021_maker_limit_retest_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return payload


def _jobs() -> list[tuple[str, dict[str, Any], Callable[[dict[str, Any]], dict[str, Any]]]]:
    jobs: list[tuple[str, dict[str, Any], Callable[[dict[str, Any]], dict[str, Any]]]] = []
    for spec in _dsr_specs():
        jobs.append(("dsr", spec, _dsr))
    for spec in (*PIVOT_LIVE, *PIVOT_RESEARCH):
        jobs.append(("pivot", spec, _pivot))
    for spec in EMA_NESTED:
        jobs.append(("ema", spec, _ema))
    for spec in HUNT004_INNER:
        s = {
            **spec,
            "id": f"inner004_{spec['symbol']}_{spec['timeframe']}_{spec['idea']}",
            "live": False,
            "window": "inner_pre_2022",
        }
        jobs.append(("h4", s, partial(_inner_atr, catalog="a")))
    for spec in HUNT005_INNER:
        s = {
            **spec,
            "id": f"inner005_{spec['symbol']}_{spec['timeframe']}_{spec['idea']}",
            "live": False,
            "window": "inner_pre_2022",
        }
        jobs.append(("h5", s, partial(_inner_atr, catalog="b")))
    for spec in HUNT006_INNER:
        s = {
            **spec,
            "id": f"inner006_{spec['symbol']}_{spec['timeframe']}_{spec['idea']}",
            "live": False,
            "window": "inner_pre_2022",
        }
        jobs.append(("h6", s, partial(_inner_atr, catalog="c")))
    for spec in AUTONOMY_LIVE:
        jobs.append(("auto", spec, _autonomy))
    return jobs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    args = ap.parse_args()
    extra = require_engine()
    print(f"engine {extra}", flush=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    extra["stamp"] = stamp
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB)
    if args.report_only:
        write_report(con, extra)
        print(f"WROTE {OUT / 'exec021_maker_limit_retest_latest.md'}", flush=True)
        return 0

    jobs = _jobs()
    print(f"planned_arms={len(jobs)}", flush=True)
    for i, (kind, spec, fn) in enumerate(jobs, start=1):
        aid = spec["id"]
        if arm_done(con, aid):
            print(f"[{i}/{len(jobs)}] skip {aid}", flush=True)
            continue
        print(f"[{i}/{len(jobs)}] === {kind} {aid} ===", flush=True)
        beat = _heartbeat(aid)
        try:
            sim = fn(spec)
        except Exception as exc:  # noqa: BLE001
            sim = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
            print(f"  ERROR {exc}", flush=True)
        finally:
            beat.set()
        payload = {
            **spec,
            **_slim(sim),
            "kind": kind,
            "window": spec.get("window", "pre_lockbox_oos"),
        }
        save_arm(con, aid, spec, payload)
        print(
            f"  {payload.get('status')} n={payload.get('n_trades')} "
            f"tpm={fmt(payload.get('trades_per_month'))} PF={fmt(payload.get('profit_factor'))} "
            f"ebr={fmt(payload.get('entry_bar_exit_rate'))}",
            flush=True,
        )
        write_report(con, extra)

    write_report(con, extra)
    print(f"WROTE {OUT / 'exec021_maker_limit_retest_latest.md'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
