"""Finplot + table: BTC/ETH/SOL 1h p80 TP1.5/SL1.5 (and full ebr-attack table).

RESEARCH_ONLY. ~4 months Finplot (max-bars default 3200 on 1h).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import Side, research_instrument, research_margin, research_sizing  # noqa: E402
from tradesim import research_sim_limit_entry  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.strategy.score_oos import gate_mask, limit_price_side, score_symbol_oos  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

TF, H, WORK = "1h", 2, 2
PACK = "level_vsa"
MAX_ROWS = 120_000
OUT = ARTIFACTS / "reports" / "pivot_forecast" / "finplot_arms"
SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
# geometries for the attack table (same as fleet 004)
GEOS = (
    ("tp1_sl1", 0.01, 0.01),
    ("tp15_sl15", 0.015, 0.015),
    ("tp2_sl2", 0.02, 0.02),
    ("tp2_sl15", 0.02, 0.015),
    ("atr15_eq", None, None),  # special: 1.5*ATR TP=SL
)


def _p80_mask(sc):
    base = gate_mask(sc, mode="p75", tp=0.01, sl=0.01)
    p = np.asarray(sc.p_any, dtype=float)
    idx = np.flatnonzero(base)
    cut = max(30, int(0.7 * idx.size)) if idx.size else 30
    thr_floor = float(np.nanmedian(sc.thr_any[idx[:cut]])) if idx.size else 0.35
    train_p = p[idx[:cut]] if idx.size else p
    train_p = train_p[np.isfinite(train_p)]
    thr_ceil = float(np.nanpercentile(train_p, 80)) if train_p.size else 0.5
    thr = thr_ceil if thr_ceil > thr_floor else thr_floor
    return base & np.isfinite(p) & (p >= thr), thr


def _bt(symbol, ohlcv, signals, *, tag: str, sl: float, store_path: str | None, print_h: bool):
    if len(signals) < 12:
        return None, {"status": "TOO_FEW", "n_signals": len(signals)}
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
    sl_use = max(
        float(sl),
        max((float(getattr(s, "stop_offset", sl) or sl) for s in signals), default=sl),
    )
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=TF,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(sl_use))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=H + 2, decision_timeframe=TF),
        instrument=research_instrument(symbol),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=False,
        print_headline=print_h,
        store_path=store_path,
    )
    m = bundle.metrics
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    holds = [float(getattr(t, "hold_bars", 1)) for t in trades] if trades else []
    ebr = float(np.mean(np.asarray(holds) <= 0)) if holds else float("nan")
    # period days from metrics or window
    period_days = float(getattr(m, "period_days", float("nan")))
    if not np.isfinite(period_days):
        try:
            period_days = float((window.index[-1] - window.index[0]).total_seconds() / 86400.0)
        except Exception:
            period_days = float("nan")
    n_tr = int(m.n_trades)
    tpm = float(n_tr / (period_days / 30.437)) if period_days and period_days > 0 else float("nan")
    return bundle, {
        "status": "RAN",
        "n_trades": n_tr,
        "profit_factor": float(m.profit_factor),
        "win_rate": float(m.win_rate),
        "net_pnl": float(m.net_pnl),
        "entry_bar_exit_rate": ebr,
        "period_days": period_days,
        "trades_per_month": tpm,
        "run_id": bundle.run_id,
    }


def _arm(symbol, sc, mask, *, tag, tp, sl, atr_mult=None, store=False, print_h=False):
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent}
    ts, is_short, lim = limit_price_side(sc, mask)
    idx = np.flatnonzero(mask)
    atr = np.asarray(sc.atr_frac, dtype=float)
    intents = []
    for j in range(len(ts)):
        if atr_mult is not None:
            a = float(atr[idx[j]]) if np.isfinite(atr[idx[j]]) else 0.015
            sl_j = float(np.clip(atr_mult * a, 0.008, 0.05))
            tp_j = sl_j
        else:
            sl_j, tp_j = float(sl), float(tp)
        intents.append(
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if is_short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=sl_j,
                target_offset=tp_j,
                max_hold_bars=H + 2,
                work_bars=WORK,
            )
        )
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=WORK)
    store_path = str(OUT / f"{tag}_store") if store else None
    print(
        f"  BT {tag} intent={n_intent} fill%={100*float(fill['fill_rate']):.1f}",
        flush=True,
    )
    bundle, res = _bt(
        symbol,
        sc.ohlcv,
        sigs,
        tag=tag,
        sl=float(sl if sl is not None else 0.015),
        store_path=store_path,
        print_h=print_h,
    )
    out = {
        "tag": tag,
        "n_intent": n_intent,
        "fill_pct": float(fill["fill_rate"]),
        "fill_stats": fill,
        **res,
    }
    if res.get("status") == "RAN":
        out["expectancy_intent_all"] = float(res["net_pnl"]) / n_intent
        print(
            f"    n={res['n_trades']} t/mo={res['trades_per_month']:.2f} "
            f"PF={res['profit_factor']:.3f} ebr={100*res['entry_bar_exit_rate']:.1f}% "
            f"exp_i={out['expectancy_intent_all']:.5f}",
            flush=True,
        )
    return out


def _promote_row(ebr: float, pf: float) -> str:
    if not np.isfinite(ebr):
        return "No"
    if ebr > 0.35:
        return "No"
    if ebr <= 0.25:
        return "Yes (ebr<=25%)"
    return "Yes (under 35%)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-bars", type=int, default=3200)
    ap.add_argument("--build-only", action="store_true")
    ap.add_argument("--no-plot", action="store_true")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    if not args.no_plot:
        os.environ.pop("TRADESIM_NO_PLOT", None)
    warnings.filterwarnings("ignore", category=Warning, module=r"finplot(\.|$)")

    report = {"generation_id": "fleet_1h_tp15_finplot", "symbols": {}, "finplot_runs": []}

    for sym in SYMBOLS:
        print(f"SCORE {sym} 1h …", flush=True)
        sc = score_symbol_oos(
            sym,
            timeframe=TF,
            horizon_bars=H,
            feature_pack=PACK,
            max_rows=MAX_ROWS,
            level_mode="ret",
            atr_min=1.0,
        )
        mask, thr = _p80_mask(sc)
        print(f"  p80 thr={thr:.4f} gated={int(mask.sum())}", flush=True)
        arms = []
        for name, tp, sl in GEOS:
            tag = f"{sym}_1h_p80_{name}_w2"
            if name == "atr15_eq":
                arms.append(
                    _arm(
                        sym,
                        sc,
                        mask,
                        tag=tag,
                        tp=0.015,
                        sl=0.015,
                        atr_mult=1.5,
                        store=False,
                    )
                )
            else:
                # store+headline only for tp15_sl15 (the finplot arm)
                is_plot = name == "tp15_sl15"
                arms.append(
                    _arm(
                        sym,
                        sc,
                        mask,
                        tag=tag,
                        tp=float(tp),
                        sl=float(sl),
                        store=is_plot,
                        print_h=is_plot,
                    )
                )
        # also atr>=SL filter (reject diagnostic)
        atr = np.asarray(sc.atr_frac, dtype=float)
        arms.append(
            _arm(
                sym,
                sc,
                mask & np.isfinite(atr) & (atr >= 0.01),
                tag=f"{sym}_1h_p80_filter_atr_ge_sl_w2",
                tp=0.01,
                sl=0.01,
                store=False,
            )
        )
        report["symbols"][sym] = {"p80_thr": thr, "arms": arms}

        # finplot tp15
        plot_arm = next(a for a in arms if "tp15_sl15" in a["tag"])
        if plot_arm.get("status") == "RAN" and not args.no_plot and not args.build_only:
            run_id = plot_arm["run_id"]
            db = str(OUT / f"{plot_arm['tag']}_store")
            report["finplot_runs"].append({"symbol": sym, "run_id": run_id, "db": db})
            print(f"PLOT {sym} {run_id}", flush=True)
            subprocess.Popen(
                [
                    sys.executable,
                    "-c",
                    (
                        "from tradesim.ensure_source import prefer_botsgeneral_tradesim;"
                        "prefer_botsgeneral_tradesim();"
                        "import warnings; warnings.filterwarnings('ignore', category=Warning, module=r'finplot(\\.|$)');"
                        "from tradesim.research.__main__ import main;"
                        f"raise SystemExit(main(['--db', r'{db}', 'plot', '--run-id', '{run_id}', "
                        f"'--max-bars', '{int(args.max_bars)}']))"
                    ),
                ],
                cwd=str(_ROOT),
            )

    # markdown summary
    lines = [
        "# 1h p80 entry-bar attack — BTC / ETH / SOL",
        "",
        "**RESEARCH_ONLY** — Finplot arm = tp1.5/sl1.5",
        "",
    ]
    for sym, block in report["symbols"].items():
        lines.append(f"## {sym}")
        lines.append("| Arm | ebr | PF | intent-exp | trades/mo | n | Promote? |")
        lines.append("|---|---:|---:|---:|---:|---:|---|")
        for a in block["arms"]:
            if a.get("status") != "RAN":
                lines.append(f"| {a.get('tag')} | — | — | — | — | — | {a.get('status')} |")
                continue
            short = a["tag"].replace(f"{sym}_1h_p80_", "").replace("_w2", "")
            ebr = float(a["entry_bar_exit_rate"])
            pf = float(a["profit_factor"])
            exp_i = float(a.get("expectancy_intent_all", float("nan")))
            tpm = float(a.get("trades_per_month", float("nan")))
            prom = _promote_row(ebr, pf)
            if "filter_atr" in short:
                prom = "No (selection artifact)" if ebr > 0.35 else prom
            lines.append(
                f"| {short} | {100*ebr:.1f}% | {pf:.2f} | {exp_i:.3f} | {tpm:.2f} | "
                f"{a['n_trades']} | {prom} |"
            )
        lines.append("")
    md = "\n".join(lines)
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    stamp_path = out_dir / "fleet_1h_tp15_table_latest.md"
    stamp_path.write_text(md, encoding="utf-8")
    (out_dir / "fleet_1h_tp15_table_latest.json").write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8"
    )
    print(md, flush=True)
    if report["finplot_runs"]:
        print(f"Launched {len(report['finplot_runs'])} Finplot processes (~4 months 1h).", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
