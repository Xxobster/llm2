"""Pivot LIMIT execution/model improve stack (preregistered pivot_exec_improve_001).

RESEARCH_ONLY. Rank by intent expectancy. Keep w4 default; SOL w5 sibling frozen.
Drop time-head adaptive cancel. Trial adverse-path cancel. Calibration-first
(isotonic vs Platt by inner ECE). Level placement: q50 + ATR-clip + mid ATR band.

Promote a sibling only if ECE not worse vs control AND intent expectancy improves.
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
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    _atr_frac,
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.pivot.train.multihead import expected_calibration_error  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

TF, H, TP, SL = "15m", 4, 0.01, 0.01
MAX_ROWS = 120_000
PACK = "level_vsa"


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


def _diag(sc) -> dict:
    y = np.asarray(sc.y_any, dtype=float)
    p = np.asarray(sc.p_any, dtype=float)
    m = np.isfinite(y) & np.isfinite(p)
    y, p = y[m], p[m]
    br = float(np.mean(y)) if y.size else float("nan")
    pr = float(average_precision_score(y, p)) if y.size >= 20 and len(np.unique(y)) >= 2 else float("nan")
    ece = expected_calibration_error(y, p) if y.size >= 20 else float("nan")
    yl, pl = np.asarray(sc.y_level, dtype=float), np.asarray(sc.level_ret, dtype=float)
    ml = np.isfinite(yl) & np.isfinite(pl)
    ae = np.abs(yl[ml] - pl[ml]) if ml.any() else np.array([])
    cal_methods = [d.get("cal_method") for d in (sc.ece_folds or [])]
    return {
        "frac_any": br,
        "pr_auc": pr,
        "pr_auc_lift": float(pr - br) if np.isfinite(pr) else float("nan"),
        "ece": float(ece),
        "level_mae": float(np.mean(ae)) if ae.size else float("nan"),
        "level_p90": float(np.percentile(ae, 90)) if ae.size else float("nan"),
        "cal_methods": cal_methods,
        "ece_outer_mean": float(
            np.nanmean([d.get("ece_outer_cal", np.nan) for d in (sc.ece_folds or [])])
        ),
    }


def _bt(symbol, ohlcv, signals, *, tag: str, max_hold: int):
    if len(signals) < 12:
        return {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(TF, symbol)
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
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[TF])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=TF,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(SL))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=TF),
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
    sharpe = float("nan")
    for attr in ("sharpe_daily_raw", "sharpe_raw", "sharpe"):
        val = getattr(m, attr, None)
        if val is None:
            continue
        if hasattr(val, "daily_raw"):
            try:
                sharpe = float(val.daily_raw)
                break
            except (TypeError, ValueError):
                pass
        try:
            sharpe = float(val)
            break
        except (TypeError, ValueError):
            continue
    return {
        "status": "RAN",
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(m.win_rate),
        "net_pnl": float(m.net_pnl),
        "expectancy": float(m.expectancy),
        "entry_bar_exit_rate": ebr,
        "sharpe_daily_raw": sharpe,
    }


def _atr_clip_level(sc, lo: float = 0.8, hi: float = 1.5) -> np.ndarray:
    lr = np.asarray(sc.level_ret, dtype=float).copy()
    atr = np.asarray(sc.atr_frac, dtype=float)
    mag = np.abs(lr)
    lo_b = lo * atr
    hi_b = hi * atr
    mag2 = np.clip(mag, lo_b, hi_b)
    # preserve NaNs
    out = np.sign(lr) * mag2
    out[~np.isfinite(lr) | ~np.isfinite(atr)] = np.nan
    return out


def _run(
    symbol,
    sc,
    mask,
    *,
    tag: str,
    work: int,
    level_override=None,
    adverse_mode=None,
    adverse_pct=0.005,
    adverse_atr_mult=1.0,
):
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent}
    if level_override is not None:
        old = sc.level_ret
        sc.level_ret = level_override
        ts, is_short, lim = limit_price_side(sc, mask)
        sc.level_ret = old
    else:
        ts, is_short, lim = limit_price_side(sc, mask)
    h = int(getattr(sc, "horizon_bars", H) or H)
    max_hold = h + 2
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[j]),
            side=Side.SHORT if is_short[j] else Side.LONG,
            limit_price=float(lim[j]),
            stop_offset=SL,
            target_offset=TP,
            max_hold_bars=max_hold,
            work_bars=work,
        )
        for j in range(len(ts))
    ]
    atr_bars = _atr_frac(sc.ohlcv)
    sigs, fill = materialize_working_limits(
        sc.ohlcv,
        intents,
        work_bars=work,
        adverse_mode=adverse_mode,
        adverse_pct=adverse_pct,
        adverse_atr_mult=adverse_atr_mult,
        atr_frac=atr_bars,
    )
    fill_pct = float(fill["fill_rate"])
    print(
        f"  BT {tag} intent={n_intent} fill%={100*fill_pct:.1f} "
        f"adv={fill.get('n_adverse_cancel', 0)} path={fill['n_filled_path']}",
        flush=True,
    )
    res = _bt(symbol, sc.ohlcv, sigs, tag=tag, max_hold=max_hold)
    out = {"tag": tag, "n_intent": n_intent, "fill_pct": fill_pct, "fill_stats": fill, **res}
    if res.get("status") == "RAN":
        out["expectancy_intent_all"] = float(res["net_pnl"]) / n_intent
        print(
            f"    n={res['n_trades']} PF={res['profit_factor']:.3f} WR={res['win_rate']:.3f} "
            f"pnl={res['net_pnl']:.2f} exp_i={out['expectancy_intent_all']:.5f} "
            f"sharpe={res.get('sharpe_daily_raw')} ebr={res['entry_bar_exit_rate']}",
            flush=True,
        )
    return out


def _rank(arms: list[dict]) -> list[dict]:
    ran = [a for a in arms if a.get("status") == "RAN"]
    ran = sorted(
        ran,
        key=lambda a: (
            -float(a.get("expectancy_intent_all") or -1e9),
            -float(a.get("profit_factor") or -1e9),
            -float(a.get("n_trades") or 0),
        ),
    )
    return [
        {
            "rank": i + 1,
            "tag": a["tag"],
            "expectancy_intent_all": a.get("expectancy_intent_all"),
            "profit_factor": a.get("profit_factor"),
            "n_trades": a.get("n_trades"),
            "fill_pct": a.get("fill_pct"),
            "win_rate": a.get("win_rate"),
            "net_pnl": a.get("net_pnl"),
            "sharpe_daily_raw": a.get("sharpe_daily_raw"),
        }
        for i, a in enumerate(ran)
    ]


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"exec improve stack stamp={stamp}", flush=True)

    leak = [_leak("ETHUSDT", PACK), _leak("SOLUSDT", PACK)]
    for x in leak:
        print(f"  leakage {x['symbol']}: {x['status']}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        return 2

    # Freeze arm list before PF
    frozen_arms = [
        "ETH_ctrl_w4",
        "ETH_adverse_pct_50bps",
        "ETH_adverse_atr_1x",
        "ETH_adverse_atr_0p5x",
        "ETH_level_q50_w4",
        "ETH_level_atr_clip_w4",
        "ETH_mid_atr_band_w4",
        "SOL_ctrl_w4",
        "SOL_sibling_w5",
        "SOL_adverse_pct_50bps",
        "SOL_adverse_atr_1x",
        "SOL_adverse_atr_0p5x",
        "SOL_level_q50_w4",
        "SOL_level_atr_clip_w4",
        "SOL_mid_atr_band_w4",
    ]
    freeze_path = out_dir / f"exec_improve_arms_freeze_{stamp}.json"
    freeze_path.write_text(
        json.dumps(
            {
                "stamp": stamp,
                "preregister": "configs/preregister/pivot_exec_improve_001.yaml",
                "ranking": "expectancy_intent_all",
                "frozen_arms_before_pf": frozen_arms,
                "dropped": ["time_head_adaptive_cancel"],
                "sol_w5_sibling_frozen": True,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"WROTE freeze {freeze_path}", flush=True)

    report = {
        "generation_id": "pivot_exec_improve_001",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "freeze_path": str(freeze_path),
        "leakage": leak,
        "symbols": {},
    }

    for sym, level_mode in (("ETHUSDT", "atr"), ("SOLUSDT", "ret")):
        print(f"SCORE {sym} level={level_mode} calib-first …", flush=True)
        sc = score_symbol_oos(
            sym,
            timeframe=TF,
            horizon_bars=H,
            feature_pack=PACK,
            max_rows=MAX_ROWS,
            level_mode=level_mode,
            atr_min=2.0,
        )
        # also q50 scoring for placement arm
        print(f"SCORE {sym} level=q50 …", flush=True)
        sc_q = score_symbol_oos(
            sym,
            timeframe=TF,
            horizon_bars=H,
            feature_pack=PACK,
            max_rows=MAX_ROWS,
            level_mode="q50",
            atr_min=2.0,
        )
        diag = _diag(sc)
        diag_q = _diag(sc_q)
        print(
            f"  diag lift={diag['pr_auc_lift']:.4f} ece={diag['ece']:.4f} "
            f"p90={diag['level_p90']:.4f} cal={diag['cal_methods']}",
            flush=True,
        )

        base = gate_mask(sc, mode="p75", tp=TP, sl=SL)
        abs_lr = np.abs(sc.level_ret)
        atr = sc.atr_frac
        mid = (
            base
            & np.isfinite(abs_lr)
            & np.isfinite(atr)
            & (abs_lr >= 0.8 * atr)
            & (abs_lr <= 1.5 * atr)
        )
        clip_lvl = _atr_clip_level(sc)
        prefix = "ETH" if sym == "ETHUSDT" else "SOL"
        arms = [
            _run(sym, sc, base, tag=f"{prefix}_ctrl_w4", work=4),
        ]
        if sym == "SOLUSDT":
            arms.append(_run(sym, sc, base, tag="SOL_sibling_w5", work=5))
        arms.extend(
            [
                _run(
                    sym,
                    sc,
                    base,
                    tag=f"{prefix}_adverse_pct_50bps",
                    work=4,
                    adverse_mode="pct",
                    adverse_pct=0.005,
                ),
                _run(
                    sym,
                    sc,
                    base,
                    tag=f"{prefix}_adverse_atr_1x",
                    work=4,
                    adverse_mode="atr",
                    adverse_atr_mult=1.0,
                ),
                _run(
                    sym,
                    sc,
                    base,
                    tag=f"{prefix}_adverse_atr_0p5x",
                    work=4,
                    adverse_mode="atr",
                    adverse_atr_mult=0.5,
                ),
                _run(sym, sc_q, gate_mask(sc_q, mode="p75", tp=TP, sl=SL), tag=f"{prefix}_level_q50_w4", work=4),
                _run(
                    sym,
                    sc,
                    base,
                    tag=f"{prefix}_level_atr_clip_w4",
                    work=4,
                    level_override=clip_lvl,
                ),
                _run(sym, sc, mid, tag=f"{prefix}_mid_atr_band_w4", work=4),
            ]
        )
        ranking = _rank(arms)
        ctrl = next(a for a in arms if a["tag"] == f"{prefix}_ctrl_w4")
        # promote siblings vs ctrl
        promotions = {}
        for a in arms:
            if a["tag"] == ctrl["tag"] or a.get("status") != "RAN" or ctrl.get("status") != "RAN":
                continue
            ece_ok = True  # same score object for most; q50 compared separately
            if "q50" in a["tag"]:
                ece_ok = float(diag_q["ece"]) <= float(diag["ece"]) * 1.02 + 1e-9
            exp_ok = float(a.get("expectancy_intent_all") or -1e9) > float(
                ctrl.get("expectancy_intent_all") or -1e9
            )
            pf_ok = float(a.get("profit_factor") or 0) >= 0.85 * float(ctrl.get("profit_factor") or 1)
            promotions[a["tag"]] = {
                "intent_exp_improved": bool(exp_ok),
                "pf_not_collapsed": bool(pf_ok),
                "ece_ok": bool(ece_ok),
                "promote": bool(exp_ok and pf_ok and ece_ok),
            }
        report["symbols"][sym] = {
            "level_mode": level_mode,
            "diagnostics": diag,
            "diagnostics_q50": diag_q,
            "arms": arms,
            "ranking_by_intent_expectancy": ranking,
            "promotions_vs_ctrl_w4": promotions,
        }
        print(f"  RANK {sym}: {ranking[:3]}", flush=True)
        print(f"  PROMOTE {sym}: {promotions}", flush=True)

    path = out_dir / f"exec_improve_{stamp}.json"
    latest = out_dir / "exec_improve_latest.json"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    md = out_dir / f"exec_improve_{stamp}.md"
    md.write_text(_md(report), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    try:
        print(_md(report), flush=True)
    except UnicodeEncodeError:
        pass
    return 0


def _md(r: dict) -> str:
    lines = [
        f"# Exec improve (`{r['stamp']}`)",
        "",
        f"**{r['readiness_max']}** — ranked by intent expectancy",
        "",
    ]
    for sym, block in r["symbols"].items():
        d = block["diagnostics"]
        lines.append(f"## {sym}")
        lines.append(
            f"lift={d['pr_auc_lift']:.4f} ece={d['ece']:.4f} level_p90={d['level_p90']:.4f} "
            f"cal={d['cal_methods']}"
        )
        lines.append("")
        lines.append("| rank | tag | intent_exp | PF | WR | n | fill% | pnl | sharpe |")
        lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|")
        for row in block["ranking_by_intent_expectancy"]:
            lines.append(
                f"| {row['rank']} | {row['tag']} | {row['expectancy_intent_all']:.5f} | "
                f"{row['profit_factor']:.3f} | {row['win_rate']:.3f} | {row['n_trades']} | "
                f"{100*float(row['fill_pct']):.1f}% | {row['net_pnl']:.2f} | {row['sharpe_daily_raw']} |"
            )
        lines.append("")
        for k, v in block["promotions_vs_ctrl_w4"].items():
            lines.append(f"- promote `{k}`: **{v['promote']}** `{v}`")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
