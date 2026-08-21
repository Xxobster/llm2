"""Work-bars grid + time-head adaptive cancel + rare/level model pass.

RESEARCH_ONLY. Default research pair:
  SOLUSDT  TP1/SL1 P75 ret  (pack level_vsa)
  ETHUSDT  TP1/SL1 P75 atr  (pack level_vsa)

Frozen before Profit Factor (PF) ranking:
  work_bars in {2,3,4,5,6} — report intent_N / fill% / intent expectancy first
  adaptive cancel = time_bucket_work_bars vs fixed work=4

Model pass (ETH/SOL): rare atr labels + level_strong + existing isotonic cal.
Promote only if PR-AUC lift and ECE both improve AND control PF >= 0.85 * baseline.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

from tradesim import Side, research_instrument, research_margin, research_sizing  # noqa: E402
from tradesim import research_sim_limit_entry  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.features.packs import build_feature_frame  # noqa: E402
from llm2.pivot.strategy.score_oos import gate_mask, limit_price_side, score_symbol_oos  # noqa: E402
from llm2.pivot.strategy.timing_gates import time_bucket_work_bars  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.pivot.train.multihead import expected_calibration_error  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

TF = "15m"
H = 4
TP = SL = 0.01
WORK_GRID = (2, 3, 4, 5, 6)
MAX_ROWS = 120_000
PAIR = (
    {"symbol": "ETHUSDT", "level_mode": "atr", "pack": "level_vsa", "atr_min": 2.0},
    {"symbol": "SOLUSDT", "level_mode": "ret", "pack": "level_vsa", "atr_min": 2.0},
)
MODEL_VARIANTS = (
    {
        "name": "baseline_level_vsa",
        "pack": "level_vsa",
        "atr_min": 2.0,
        "horizon_bars": 4,
    },
    {
        "name": "rare_level_strong",
        "pack": "level_strong",
        "atr_min": 2.0,
        "horizon_bars": 4,
    },
    {
        "name": "rare15_level_strong",
        "pack": "level_strong",
        "atr_min": 1.5,
        "horizon_bars": 3,
    },
)
PF_FLOOR = 0.85  # control PF must be >= this * baseline PF


def _leak(symbol: str, pack: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = load_ohlcv(symbol, TF)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-6000:].copy()

        def _b(df, **_k):
            return build_feature_frame(df, pack=pack)

        require_clean_audit(
            run_leakage_audit(
                ohlcv=ohlcv, build_features=_b, interval=TF, symbol=symbol, timeframe=TF
            )
        )
        return {"symbol": symbol, "pack": pack, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "pack": pack, "status": "FAIL", "error": str(exc)[:300]}


def _diagnostics(sc) -> dict:
    y = np.asarray(sc.y_any, dtype=float)
    p = np.asarray(sc.p_any, dtype=float)
    m = np.isfinite(y) & np.isfinite(p)
    y, p = y[m], p[m]
    br = float(np.mean(y)) if y.size else float("nan")
    if y.size >= 20 and len(np.unique(y)) >= 2:
        pr = float(average_precision_score(y, p))
        pr_br = br  # baserate PR-AUC equals prevalence for constant score
    else:
        pr, pr_br = float("nan"), float("nan")
    ece = expected_calibration_error(y, p) if y.size >= 20 else float("nan")
    # level errors
    yl = np.asarray(sc.y_level, dtype=float)
    pl = np.asarray(sc.level_ret, dtype=float)
    ml = np.isfinite(yl) & np.isfinite(pl)
    abs_e = np.abs(yl[ml] - pl[ml]) if ml.any() else np.array([])
    return {
        "n": int(y.size),
        "frac_any": float(np.mean(y)) if y.size else float("nan"),
        "pr_auc": pr,
        "pr_auc_baserate": float(pr_br),
        "pr_auc_lift": float(pr - pr_br) if np.isfinite(pr) and np.isfinite(pr_br) else float("nan"),
        "ece": float(ece),
        "level_mae": float(np.mean(abs_e)) if abs_e.size else float("nan"),
        "level_p90": float(np.percentile(abs_e, 90)) if abs_e.size else float("nan"),
        "ece_folds_mean_outer": float(
            np.nanmean([d.get("ece_outer_cal", np.nan) for d in (sc.ece_folds or [])])
        ),
    }


def _bt(symbol, tf, ohlcv, signals, *, sl, tag, max_hold):
    if len(signals) < 12:
        return {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(tf, symbol)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    touch = load_ohlcv(symbol, touch_tf)
    touch = touch.loc[touch.index < lock]
    funding = load_funding(symbol)
    funding = funding[funding.index < lock]
    f_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    f_rt = funding.to_numpy(dtype=float)
    bar_ms = index_to_ms(ohlcv.index)
    sig_ts = np.array([s.ts_ms for s in signals], dtype=np.int64)
    i0 = int(np.searchsorted(bar_ms, int(sig_ts.min()), side="left"))
    i1 = int(np.searchsorted(bar_ms, int(sig_ts.max()), side="right"))
    window = ohlcv.iloc[max(0, i0 - 80) : min(len(ohlcv), i1 + 80)]
    w_ts = index_to_ms(window.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[tf])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=tf,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(sl))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=tf),
        instrument=research_instrument(symbol),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=False,
        print_headline=False,
        store_path=None,
    )
    m = bundle.metrics
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    holds = [float(getattr(t, "hold_bars", 1)) for t in trades] if trades else []
    ebr = float(np.mean(np.asarray(holds) <= 0)) if holds else float("nan")
    return {
        "status": "RAN",
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(m.win_rate),
        "net_pnl": float(m.net_pnl),
        "expectancy": float(m.expectancy),
        "entry_bar_exit_rate": ebr,
    }


def _intents(sc, mask, *, work_per_row: np.ndarray | None, default_work: int):
    ts, is_short, lim = limit_price_side(sc, mask)
    idx = np.flatnonzero(mask)
    h_bars = int(getattr(sc, "horizon_bars", H) or H)
    max_hold = h_bars + 2
    out = []
    for j in range(len(ts)):
        wb = int(work_per_row[j]) if work_per_row is not None else int(default_work)
        out.append(
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if is_short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=SL,
                target_offset=TP,
                max_hold_bars=max_hold,
                work_bars=wb,
                meta={"row": int(idx[j])},
            )
        )
    return out, max_hold


def _fill_only(sc, mask, *, work: int | None = None, work_per_row=None) -> dict:
    intents, _ = _intents(sc, mask, work_per_row=work_per_row, default_work=work or 4)
    _, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=int(work or 4))
    return {
        "n_intent": int(mask.sum()),
        "fill_pct": float(fill["fill_rate"]),
        "n_path_fill": int(fill["n_filled_path"]),
        "work_bars_mean_used": float(fill["work_bars_mean_used"]),
        "fill_stats": fill,
    }


def _run_arm(symbol, sc, mask, *, tag: str, work: int | None = None, work_per_row=None):
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent}
    intents, max_hold = _intents(
        sc, mask, work_per_row=work_per_row, default_work=work or 4
    )
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=int(work or 4))
    fill_pct = float(fill["fill_rate"])
    print(
        f"  BT {tag} intent_N={n_intent} fill%={100*fill_pct:.1f} path={fill['n_filled_path']}",
        flush=True,
    )
    res = _bt(symbol, sc.timeframe, sc.ohlcv, sigs, sl=SL, tag=tag, max_hold=max_hold)
    out = {
        "tag": tag,
        "n_intent": n_intent,
        "fill_pct": fill_pct,
        "fill_stats": fill,
        **res,
    }
    if res.get("status") == "RAN":
        out["expectancy_intent_all"] = float(res["net_pnl"]) / n_intent
        print(
            f"    trade_N={res['n_trades']} PF={res['profit_factor']:.3f} "
            f"exp_intent={out['expectancy_intent_all']:.5f} ebr={res['entry_bar_exit_rate']}",
            flush=True,
        )
    return out


def _prefer_shorter(arms: list[dict]) -> dict:
    """Rank by fill% usable (>=15%) then higher intent expectancy; prefer shorter work on ties."""
    fixed = [a for a in arms if a.get("status") == "RAN" and a.get("work_bars") is not None]
    usable = [a for a in fixed if float(a.get("fill_pct") or 0) >= 0.15]
    pool = usable or fixed
    if not pool:
        return {"choice": None, "reason": "no_ran_arms"}
    # sort: expectancy_intent desc, then work_bars asc
    pool = sorted(
        pool,
        key=lambda a: (-float(a.get("expectancy_intent_all") or -1e9), int(a["work_bars"])),
    )
    best = pool[0]
    return {
        "choice": best["tag"],
        "work_bars": best["work_bars"],
        "fill_pct": best["fill_pct"],
        "expectancy_intent_all": best.get("expectancy_intent_all"),
        "profit_factor": best.get("profit_factor"),
        "rule": "among fill%>=15%, max expectancy_intent, tie -> shorter work",
    }


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"work/adaptive/model pass stamp={stamp}", flush=True)

    leak = []
    for cfg in PAIR:
        for pack in ("level_vsa", "level_strong"):
            leak.append(_leak(cfg["symbol"], pack))
    for x in leak:
        print(f"  leakage {x['symbol']} {x['pack']}: {x['status']}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        print("LEAKAGE FAIL", flush=True)
        return 2

    # ---- Phase 1: score default pair + freeze fill% grid (no PF yet) ----
    scored = {}
    fill_freeze = {}
    for cfg in PAIR:
        sym = cfg["symbol"]
        print(
            f"SCORE exec {sym} pack={cfg['pack']} level={cfg['level_mode']} …",
            flush=True,
        )
        sc = score_symbol_oos(
            sym,
            timeframe=TF,
            horizon_bars=H,
            feature_pack=cfg["pack"],
            max_rows=MAX_ROWS,
            level_mode=cfg["level_mode"],
            atr_min=float(cfg["atr_min"]),
        )
        mask = gate_mask(sc, mode="p75", tp=TP, sl=SL)
        scored[sym] = {"sc": sc, "mask": mask, "cfg": cfg}
        grid = {}
        for w in WORK_GRID:
            grid[f"w{w}"] = _fill_only(sc, mask, work=w)
            print(
                f"  FREEZE fill {sym} w{w}: intent={grid[f'w{w}']['n_intent']} "
                f"fill%={100*grid[f'w{w}']['fill_pct']:.1f}",
                flush=True,
            )
        # adaptive fill freeze
        wb_all = time_bucket_work_bars(sc.time_bars, horizon=H, default_work=4)
        wb_gate = wb_all[mask]
        grid["adaptive_time"] = _fill_only(sc, mask, work_per_row=wb_gate, work=4)
        print(
            f"  FREEZE fill {sym} adaptive: intent={grid['adaptive_time']['n_intent']} "
            f"fill%={100*grid['adaptive_time']['fill_pct']:.1f} "
            f"mean_work={grid['adaptive_time']['work_bars_mean_used']:.2f}",
            flush=True,
        )
        fill_freeze[sym] = grid

    freeze_path = out_dir / f"work_grid_fill_freeze_{stamp}.json"
    freeze_path.write_text(
        json.dumps(
            {
                "stamp": stamp,
                "note": "fill% frozen before any PF ranking",
                "work_grid": list(WORK_GRID),
                "fill_freeze": fill_freeze,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"WROTE {freeze_path}", flush=True)

    # ---- Phase 2: BT grid + adaptive (PF after freeze) ----
    exec_results = {}
    for sym, pack in scored.items():
        sc, mask = pack["sc"], pack["mask"]
        arms = []
        for w in WORK_GRID:
            a = _run_arm(sym, sc, mask, tag=f"{sym}_p75_w{w}", work=w)
            a["work_bars"] = w
            arms.append(a)
        wb_gate = time_bucket_work_bars(sc.time_bars, horizon=H, default_work=4)[mask]
        a_ad = _run_arm(
            sym, sc, mask, tag=f"{sym}_p75_adaptive_time", work=4, work_per_row=wb_gate
        )
        a_ad["work_bars"] = None
        a_ad["adaptive"] = True
        arms.append(a_ad)
        pref = _prefer_shorter(arms)
        # adaptive vs fixed w4
        w4 = next(x for x in arms if x.get("tag") == f"{sym}_p75_w4")
        cmp_ad = {
            "fixed_w4_pf": w4.get("profit_factor"),
            "fixed_w4_fill_pct": w4.get("fill_pct"),
            "fixed_w4_exp_intent": w4.get("expectancy_intent_all"),
            "adaptive_pf": a_ad.get("profit_factor"),
            "adaptive_fill_pct": a_ad.get("fill_pct"),
            "adaptive_exp_intent": a_ad.get("expectancy_intent_all"),
            "adaptive_beats_w4_exp_intent": (
                a_ad.get("status") == "RAN"
                and w4.get("status") == "RAN"
                and float(a_ad.get("expectancy_intent_all") or -1e9)
                > float(w4.get("expectancy_intent_all") or -1e9)
            ),
        }
        exec_results[sym] = {
            "level_mode": pack["cfg"]["level_mode"],
            "arms": arms,
            "prefer_shorter": pref,
            "adaptive_vs_w4": cmp_ad,
        }
        print(f"  prefer_shorter {sym}: {pref}", flush=True)
        print(f"  adaptive_vs_w4 {sym}: {cmp_ad}", flush=True)

    # ---- Phase 3: model pass ----
    model_pass = {}
    for cfg in PAIR:
        sym = cfg["symbol"]
        model_pass[sym] = {"variants": {}, "promotion": {}}
        base_pf = None
        base_lift = None
        base_ece = None
        for var in MODEL_VARIANTS:
            print(
                f"SCORE model {sym} {var['name']} pack={var['pack']} "
                f"atr_min={var['atr_min']} H={var['horizon_bars']} …",
                flush=True,
            )
            sc = score_symbol_oos(
                sym,
                timeframe=TF,
                horizon_bars=int(var["horizon_bars"]),
                feature_pack=var["pack"],
                max_rows=MAX_ROWS,
                level_mode=cfg["level_mode"],
                atr_min=float(var["atr_min"]),
            )
            diag = _diagnostics(sc)
            mask = gate_mask(sc, mode="p75", tp=TP, sl=SL)
            arm = _run_arm(sym, sc, mask, tag=f"{sym}_{var['name']}_p75_w4", work=4)
            block = {"diagnostics": diag, "control_p75_w4": arm}
            model_pass[sym]["variants"][var["name"]] = block
            print(
                f"    lift={diag['pr_auc_lift']:.4f} ece={diag['ece']:.4f} "
                f"level_p90={diag['level_p90']:.4f}",
                flush=True,
            )
            if var["name"] == "baseline_level_vsa" and arm.get("status") == "RAN":
                base_pf = float(arm["profit_factor"])
                base_lift = float(diag["pr_auc_lift"])
                base_ece = float(diag["ece"])
                model_pass[sym]["baseline"] = var["name"]

        # promotion vs baseline
        for name, block in model_pass[sym]["variants"].items():
            if name == "baseline_level_vsa":
                continue
            d = block["diagnostics"]
            arm = block["control_p75_w4"]
            pf = float(arm.get("profit_factor", float("nan"))) if arm.get("status") == "RAN" else float("nan")
            lift_ok = (
                np.isfinite(d["pr_auc_lift"])
                and base_lift is not None
                and d["pr_auc_lift"] > base_lift
            )
            ece_ok = (
                np.isfinite(d["ece"]) and base_ece is not None and d["ece"] < base_ece
            )
            pf_ok = (
                np.isfinite(pf)
                and base_pf is not None
                and pf >= PF_FLOOR * base_pf
            )
            model_pass[sym]["promotion"][name] = {
                "pr_auc_lift_improved": bool(lift_ok),
                "ece_improved": bool(ece_ok),
                "pf_not_collapsed": bool(pf_ok),
                "promote": bool(lift_ok and ece_ok and pf_ok),
                "base_pf": base_pf,
                "new_pf": pf,
                "base_lift": base_lift,
                "new_lift": d["pr_auc_lift"],
                "base_ece": base_ece,
                "new_ece": d["ece"],
                "level_p90": d["level_p90"],
                "rule": "lift>base AND ece<base AND pf>=0.85*base_pf",
            }
            print(f"  promote? {sym} {name}: {model_pass[sym]['promotion'][name]}", flush=True)

    report = {
        "generation_id": "pivot_work_adaptive_model_001",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "default_research_pair": [
            "SOLUSDT TP1/SL1 P75 ret w4",
            "ETHUSDT TP1/SL1 P75 atr w4",
        ],
        "pi_star_tight_diagnostic_only": True,
        "leakage": leak,
        "fill_freeze_path": str(freeze_path),
        "exec_work_grid": exec_results,
        "model_pass": model_pass,
        "policy": {
            "score_fill_and_intent_before_pf": True,
            "prefer_shorter_work_if_fill_usable": True,
            "level_p90_target": 0.01,
            "no_post_hoc_work_widen": True,
        },
    }
    path = out_dir / f"work_adaptive_model_{stamp}.json"
    latest = out_dir / "work_adaptive_model_latest.json"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    md = out_dir / f"work_adaptive_model_{stamp}.md"
    md.write_text(_md(report), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    try:
        print(_md(report), flush=True)
    except UnicodeEncodeError:
        pass
    return 0


def _md(r: dict) -> str:
    lines = [
        f"# Work grid + adaptive cancel + model pass (`{r['stamp']}`)",
        "",
        f"**{r['readiness_max']}**",
        "",
        "## Execution (ETH/SOL P75)",
    ]
    for sym, block in r["exec_work_grid"].items():
        lines.append(f"### {sym}")
        lines.append("| tag | work | intent_N | fill% | trade_N | exp_intent | PF | ebr% |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
        for a in block["arms"]:
            if a.get("status") != "RAN":
                lines.append(
                    f"| {a.get('tag')} | {a.get('work_bars')} | {a.get('n_intent')} | — | — | — | {a.get('status')} | — |"
                )
                continue
            lines.append(
                f"| {a['tag']} | {a.get('work_bars')} | {a['n_intent']} | "
                f"{100*float(a['fill_pct']):.1f}% | {a['n_trades']} | "
                f"{a.get('expectancy_intent_all', float('nan')):.5f} | "
                f"{a['profit_factor']:.3f} | {100*float(a.get('entry_bar_exit_rate', float('nan'))):.1f}% |"
            )
        lines.append(f"- prefer_shorter: `{block['prefer_shorter']}`")
        lines.append(f"- adaptive_vs_w4: `{block['adaptive_vs_w4']}`")
        lines.append("")
    lines.append("## Model pass promotion")
    for sym, block in r["model_pass"].items():
        lines.append(f"### {sym}")
        for name, v in block["variants"].items():
            d = v["diagnostics"]
            a = v["control_p75_w4"]
            pf = a.get("profit_factor") if a.get("status") == "RAN" else a.get("status")
            lines.append(
                f"- **{name}**: lift={d['pr_auc_lift']:.4f} ece={d['ece']:.4f} "
                f"level_p90={d['level_p90']:.4f} control_PF={pf}"
            )
        for name, p in block.get("promotion", {}).items():
            lines.append(f"- promote `{name}`: **{p['promote']}** ({p})")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
