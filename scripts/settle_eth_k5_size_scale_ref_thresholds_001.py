#!/usr/bin/env python3
"""Full metrics table: size-scale refs + min_edge thresholds on ETH K5.

Prereg: configs/preregister/structure_v1_eth_k5_size_scale_ref_thresholds_001.yaml

MEASURE_DIAGNOSTIC / RESEARCH_ONLY — multi-threshold comparison for design.
Do **not** promote a ref picked after viewing this table (outer multi-arm peep).

Also records size-lift frequency next to each size-scale arm.

Run::

  python scripts/settle_eth_k5_size_scale_ref_thresholds_001.py
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np
import pandas as pd
import yaml

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_hedge,
)

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.signals.cluster_concurrency import build_cluster_size_signals  # noqa: E402
from llm2.signals.singlebook_clarity import SingleBookArm  # noqa: E402
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    build_outer_folds,
    index_to_ms,
)

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
LABEL_HORIZON = 6
K = 5
SL = 0.02
GEN = "structure_v1_eth_k5_size_scale_ref_thresholds_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN}.yaml"
ARM = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)
STRENGTH_Q = 0.5
SIZE_DOUBLE = 3

# Months across outer stitch ~ 2022-01 → 2026-05 exclusive ≈ 52 months
OUTER_MONTHS_APPROX = (
    (pd.Timestamp("2026-05-01", tz="UTC") - pd.Timestamp("2022-01-01", tz="UTC")).days
    / 30.4375
)


def _finite(x: Any) -> Any:
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    if isinstance(x, (np.floating,)):
        v = float(x)
        return None if not math.isfinite(v) else v
    if isinstance(x, (np.integer,)):
        return int(x)
    return x


def _pf(pnls: list[float]) -> float:
    a = np.asarray(pnls, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return float("nan")
    gp = float(a[a > 0].sum())
    gl = float((-a[a < 0]).sum())
    if gl <= 0:
        return float("inf") if gp > 0 else float("nan")
    return gp / gl


def _metrics_from_bundle(bundle: Any) -> dict[str, Any]:
    m = bundle.metrics
    sh = getattr(m, "sharpe", None)
    return {
        "n_trades": int(m.n_trades),
        "net_pnl": _finite(float(m.net_pnl)),
        "profit_factor": _finite(float(m.profit_factor)),
        "win_rate": _finite(float(m.win_rate)),
        "expectancy": _finite(float(getattr(m, "expectancy", float("nan")))),
        "expectancy_return_units": _finite(
            float(getattr(m, "expectancy_return_units", float("nan")))
        ),
        "total_fees": _finite(float(getattr(m, "total_fees", float("nan")))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "max_drawdown": _finite(float(getattr(m, "max_drawdown", float("nan")))),
        "payoff_ratio": _finite(float(getattr(m, "payoff_ratio", float("nan")))),
        "avg_win": _finite(float(getattr(m, "avg_win", float("nan")))),
        "avg_loss": _finite(float(getattr(m, "avg_loss", float("nan")))),
        "sharpe_annualised": _finite(
            float(getattr(sh, "annualised", getattr(sh, "annualized", float("nan"))))
        )
        if sh is not None
        else None,
    }


def _stitched(
    fold_rows: list[dict],
    all_pnls: list[float],
    all_fees: float,
    n_liq: int,
    extra: dict | None = None,
) -> dict[str, Any]:
    wins = sum(1 for p in all_pnls if p > 0)
    losses = sum(1 for p in all_pnls if p < 0)
    exp_num = exp_den = exp_usdt = 0.0
    mdd = None
    for fr in fold_rows:
        n = float(fr.get("n_trades") or 0)
        if n > 0 and fr.get("expectancy_return_units") is not None:
            exp_num += float(fr["expectancy_return_units"]) * n
            exp_den += n
        if n > 0 and fr.get("expectancy") is not None:
            exp_usdt += float(fr["expectancy"]) * n
        md = fr.get("max_drawdown")
        if md is not None:
            mdd = md if mdd is None else max(float(mdd), float(md))
    n_tr = len(all_pnls)
    out = {
        "n_trades": n_tr,
        "trades_per_month": float(n_tr / OUTER_MONTHS_APPROX) if n_tr else 0.0,
        "avg_trades_per_fold": float(n_tr / len(fold_rows)) if fold_rows else 0.0,
        "n_folds": len(fold_rows),
        "net_pnl": float(np.nansum(all_pnls)),
        "profit_factor": _pf(all_pnls),
        "win_rate": float(wins / n_tr) if n_tr else float("nan"),
        "n_wins": wins,
        "n_losses": losses,
        "expectancy": (exp_usdt / exp_den) if exp_den else float("nan"),
        "expectancy_return_units": (exp_num / exp_den) if exp_den else float("nan"),
        "total_fees": all_fees,
        "n_liquidations": int(n_liq),
        "max_drawdown_worst_fold": _finite(mdd),
        "frac_folds_pf_gt_1": float(
            np.mean([float(r.get("profit_factor") or 0) > 1 for r in fold_rows])
        )
        if fold_rows
        else float("nan"),
        "avg_net_pnl_per_trade": float(np.nansum(all_pnls) / n_tr) if n_tr else float("nan"),
    }
    if extra:
        out.update(extra)
    return out


def run_bt(
    *,
    window,
    sigs,
    label: str,
    fold_index: int,
    touch_win,
    touch_tf: str,
    funding_ts,
    funding_rt,
    fmask,
    instrument,
    lev: float,
    meta: dict,
):
    return run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=f"{label}-f{fold_index}",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=int(ARM.horizon_bars),
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=K,
            max_positions_per_symbol=K * 2,
        ),
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={"name": label, "generation_id": GEN, **meta},
        plot=False,
        print_headline=False,
        store_path=None,
    )


def size_freq(abs_means: list[float], ref: float) -> dict[str, Any]:
    a = np.asarray(abs_means, dtype=float)
    if a.size == 0:
        return {"n": 0}
    lift = a >= float(ref)
    cap = a >= 2.0 * float(ref)
    prop = lift & ~cap
    floor = ~lift
    return {
        "n": int(a.size),
        "ref": float(ref),
        "pct_size_lift_met": float(lift.mean()),
        "pct_size_lift_not_met_floor": float(floor.mean()),
        "pct_cap_2x": float(cap.mean()),
        "pct_proportional_band": float(prop.mean()),
        "mean_abs_mean": float(a.mean()),
        "p50_abs_mean": float(np.median(a)),
        "p90_abs_mean": float(np.quantile(a, 0.90)),
    }


def main() -> int:
    t0 = time.perf_counter()
    if not PREREG.is_file():
        print(f"MISSING {PREREG}", file=sys.stderr)
        return 2
    prereg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    size_refs = [float(x) for x in prereg["size_scale_refs"]]
    edge_ladder = [float(x) for x in prereg["min_edge_ladder"]]

    conf = run_conformance_check()
    conf_ok = bool(conf.get("passed") if isinstance(conf, dict) else conf)
    print(f"conformance_ok={conf_ok}", flush=True)

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(SYMBOL)
    family = target_family(TARGET)
    close_full = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)

    # Arm registry
    arms: list[dict[str, Any]] = [
        {
            "label": "control_time_double",
            "kind": "control",
            "min_edge": float(DIRECTION_BAND),
            "size_scale": False,
            "size_ref": None,
        }
    ]
    for ref in size_refs:
        arms.append(
            {
                "label": f"size_ref_{ref:.2f}",
                "kind": "size_scale",
                "min_edge": float(DIRECTION_BAND),
                "size_scale": True,
                "size_ref": float(ref),
            }
        )
    for e in edge_ladder:
        arms.append(
            {
                "label": f"min_edge_{e:.2f}",
                "kind": "min_edge",
                "min_edge": float(e),
                "size_scale": False,
                "size_ref": None,
            }
        )

    # Accumulators per arm
    state: dict[str, dict[str, Any]] = {
        a["label"]: {
            "cfg": a,
            "fold_rows": [],
            "pnls": [],
            "fees": 0.0,
            "n_liq": 0,
            "emitted_abs": [],
            "mean_size_mult_w": 0.0,
            "mean_size_mult_n": 0.0,
        }
        for a in arms
    }

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        print(f"=== fold {fold.fold_index} train/predict shared ===", flush=True)
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        close_oos = close_full[oos]

        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, int(ARM.horizon_bars) * 4)
        pos = int(ohlcv.index.searchsorted(oos0))
        window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
        end, start = window.index[-1], window.index[0]
        dec_ms = int(TF_MS[TIMEFRAME])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
        w_ts = index_to_ms(window.index)
        fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))

        for arm in arms:
            lab = arm["label"]
            sigs, stats = build_cluster_size_signals(
                oos_ts,
                side,
                mean,
                close_oos,
                arm=ARM,
                min_edge=float(arm["min_edge"]),
                max_per_side=K,
                instrument=instrument,
                size_double_within_bars=SIZE_DOUBLE,
                strength_quantile=STRENGTH_Q,
                size_scale_by_abs_mean=bool(arm["size_scale"]),
                size_scale_ref=float(arm["size_ref"] or 0.5),
                size_scale_factor_min=1.0,
                size_scale_factor_max=2.0,
            )
            st = state[lab]
            for s in sigs:
                st["emitted_abs"].append(float(s.meta.get("abs_mean") or 0.0))
            if stats.get("n_emitted") and stats.get("mean_size_mult") is not None:
                n_e = float(stats["n_emitted"])
                st["mean_size_mult_w"] += float(stats["mean_size_mult"]) * n_e
                st["mean_size_mult_n"] += n_e

            bundle = run_bt(
                window=window,
                sigs=sigs,
                label=lab,
                fold_index=int(fold.fold_index),
                touch_win=touch_win,
                touch_tf=touch_tf,
                funding_ts=funding_ts,
                funding_rt=funding_rt,
                fmask=fmask,
                instrument=instrument,
                lev=lev,
                meta={
                    "kind": arm["kind"],
                    "min_edge": arm["min_edge"],
                    "size_ref": arm["size_ref"],
                },
            )
            mdict = _metrics_from_bundle(bundle)
            pnls = [
                float(getattr(t, "realized_pnl", 0) or 0) for t in bundle.result.trades
            ]
            st["pnls"].extend(pnls)
            st["fees"] += float(mdict.get("total_fees") or 0.0)
            st["n_liq"] += int(mdict.get("n_liquidations") or 0)
            st["fold_rows"].append({"fold_index": int(fold.fold_index), **mdict})
            print(
                f"  {lab} f{fold.fold_index}: n={mdict['n_trades']} "
                f"pnl={mdict['net_pnl']} pf={mdict['profit_factor']} "
                f"wr={mdict['win_rate']}",
                flush=True,
            )

    control = state["control_time_double"]
    control_st = _stitched(
        control["fold_rows"], control["pnls"], control["fees"], control["n_liq"]
    )

    size_rows: list[dict] = []
    edge_rows: list[dict] = []
    all_arm_rows: list[dict] = []

    for arm in arms:
        lab = arm["label"]
        st = state[lab]
        mean_sm = (
            st["mean_size_mult_w"] / st["mean_size_mult_n"]
            if st["mean_size_mult_n"] > 0
            else None
        )
        freq = None
        if arm["kind"] == "size_scale" and arm["size_ref"] is not None:
            freq = size_freq(st["emitted_abs"], float(arm["size_ref"]))
        elif arm["kind"] == "control":
            # still report abs dist vs ref=0.5 for comparison
            freq = size_freq(st["emitted_abs"], 0.5)
            freq["note"] = "freq versus ref=0.5 even though size-scale off"

        stitched = _stitched(
            st["fold_rows"],
            st["pnls"],
            st["fees"],
            st["n_liq"],
            extra={
                "mean_size_mult": _finite(mean_sm),
                "size_lift_freq": freq,
            },
        )
        row = {
            "label": lab,
            "kind": arm["kind"],
            "min_edge": arm["min_edge"],
            "size_scale_ref": arm["size_ref"],
            **stitched,
            "delta_net_pnl_vs_control": (
                None
                if lab == "control_time_double"
                else float(stitched["net_pnl"] or 0)
                - float(control_st["net_pnl"] or 0)
            ),
            "delta_pf_vs_control": (
                None
                if lab == "control_time_double"
                or stitched.get("profit_factor") is None
                or control_st.get("profit_factor") is None
                else float(stitched["profit_factor"]) - float(control_st["profit_factor"])
            ),
            "delta_n_trades_vs_control": (
                None
                if lab == "control_time_double"
                else int(stitched["n_trades"]) - int(control_st["n_trades"])
            ),
            "folds": st["fold_rows"],
        }
        all_arm_rows.append(row)
        if arm["kind"] in ("control", "size_scale"):
            size_rows.append(row)
        if arm["kind"] in ("control", "min_edge"):
            edge_rows.append(row)

        print(
            f"SUMMARY {lab}: n={stitched['n_trades']} "
            f"tpm={stitched['trades_per_month']:.1f} "
            f"pnl={stitched['net_pnl']:.2f} PF={stitched['profit_factor']} "
            f"WR={stitched['win_rate']} E[r]={stitched['expectancy_return_units']} "
            f"mean_x={mean_sm}",
            flush=True,
        )

    # Compact markdown table strings
    def md_size(rows: list[dict]) -> str:
        lines = [
            "| arm | ref | n_trades | trades/mo | mean_x | pct_lift_met | net_pnl | PF | WR | E[r] | d_pnl | liq |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for r in rows:
            ref = r.get("size_scale_ref")
            ref_s = f"{ref:.2f}" if ref is not None else "—"
            freq = r.get("size_lift_freq") or {}
            lift = freq.get("pct_size_lift_met")
            lift_s = f"{100*lift:.1f}%" if lift is not None else "—"
            dlt = r.get("delta_net_pnl_vs_control")
            dlt_s = f"{dlt:+.1f}" if dlt is not None else "—"
            lines.append(
                f"| {r['label']} | {ref_s} | {r['n_trades']} | "
                f"{r['trades_per_month']:.1f} | "
                f"{(r.get('mean_size_mult') or 0):.3f} | {lift_s} | "
                f"{r['net_pnl']:.1f} | {r['profit_factor']:.3f} | "
                f"{100*float(r['win_rate'] or 0):.1f}% | "
                f"{100*float(r['expectancy_return_units'] or 0):.3f}% | "
                f"{dlt_s} | {r['n_liquidations']} |"
            )
        return "\n".join(lines)

    def md_edge(rows: list[dict]) -> str:
        lines = [
            "| arm | min_edge | n_trades | trades/mo | net_pnl | PF | WR | E[r] | fees | liq | d_n | d_pnl |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for r in rows:
            dlt = r.get("delta_net_pnl_vs_control")
            dn = r.get("delta_n_trades_vs_control")
            lines.append(
                f"| {r['label']} | {r['min_edge']:.2f} | {r['n_trades']} | "
                f"{r['trades_per_month']:.1f} | {r['net_pnl']:.1f} | "
                f"{r['profit_factor']:.3f} | {100*float(r['win_rate'] or 0):.1f}% | "
                f"{100*float(r['expectancy_return_units'] or 0):.3f}% | "
                f"{float(r['total_fees'] or 0):.1f} | {r['n_liquidations']} | "
                f"{dn if dn is not None else '—'} | "
                f"{(f'{dlt:+.1f}' if dlt is not None else '—')} |"
            )
        return "\n".join(lines)

    # CSV-friendly flat cells
    csv_cells = []
    for r in all_arm_rows:
        freq = r.get("size_lift_freq") or {}
        csv_cells.append(
            {
                "label": r["label"],
                "kind": r["kind"],
                "min_edge": r["min_edge"],
                "size_scale_ref": r.get("size_scale_ref"),
                "n_trades": r["n_trades"],
                "trades_per_month": r["trades_per_month"],
                "avg_trades_per_fold": r["avg_trades_per_fold"],
                "net_pnl": r["net_pnl"],
                "profit_factor": r["profit_factor"],
                "win_rate": r["win_rate"],
                "expectancy": r["expectancy"],
                "expectancy_return_units": r["expectancy_return_units"],
                "total_fees": r["total_fees"],
                "n_liquidations": r["n_liquidations"],
                "max_drawdown_worst_fold": r.get("max_drawdown_worst_fold"),
                "mean_size_mult": r.get("mean_size_mult"),
                "pct_size_lift_met": freq.get("pct_size_lift_met"),
                "pct_size_lift_not_met_floor": freq.get("pct_size_lift_not_met_floor"),
                "pct_cap_2x": freq.get("pct_cap_2x"),
                "delta_net_pnl_vs_control": r.get("delta_net_pnl_vs_control"),
                "delta_pf_vs_control": r.get("delta_pf_vs_control"),
                "frac_folds_pf_gt_1": r.get("frac_folds_pf_gt_1"),
            }
        )

    out = {
        "generation_id": GEN,
        "gate_name": "ETH K5 size-scale ref + min_edge thresholds full metrics",
        "evidence_class": "MEASURE_DIAGNOSTIC",
        "maximum_earned_readiness": "RESEARCH_ONLY",
        "promotion_allowed": False,
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "note": (
            "Multi-threshold outer stitch. Ranking is exploratory — do not promote "
            "a ref or min_edge chosen after viewing. Companion to size/TP scale design "
            "and structure_v1_eth_k5_pred_mean_strength_met_freq_001."
        ),
        "prereg_sha256": hashlib.sha256(PREREG.read_bytes()).hexdigest(),
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES,
        "outer_months_approx": OUTER_MONTHS_APPROX,
        "hard_end_exclusive": str(FORWARD_LOCKBOX_START),
        "lockbox_used": False,
        "conformance_ok": conf_ok,
        "control": control_st,
        "size_scale_table": size_rows,
        "min_edge_table": edge_rows,
        "all_arms": all_arm_rows,
        "markdown_size_scale": md_size(size_rows),
        "markdown_min_edge": md_edge(edge_rows),
        "flat_cells": csv_cells,
        "related_frequency_report": "structure_v1_eth_k5_pred_mean_strength_met_freq_001_latest.json",
        "elapsed_sec": time.perf_counter() - t0,
    }
    stamp_min_size_equity_caveat(out)

    reports = ARTIFACTS / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stamp = out["created_utc"]
    latest = reports / f"{GEN}_latest.json"
    path = reports / f"{GEN}_{stamp}.json"
    blob = json.dumps(out, indent=2, default=str)
    latest.write_text(blob, encoding="utf-8")
    path.write_text(blob, encoding="utf-8")

    # CSV
    try:
        pd.DataFrame(csv_cells).to_csv(
            reports / f"{GEN}_all_cells.csv", index=False
        )
    except Exception as e:
        print(f"csv_write_failed: {e}", flush=True)

    md_path = reports / f"{GEN}_TABLE.md"
    md_path.write_text(
        f"# {GEN}\n\n"
        f"**Evidence class:** MEASURE_DIAGNOSTIC — not for promotion.\n\n"
        f"## Size-scale refs (time double on, min_edge=0.10)\n\n"
        f"{out['markdown_size_scale']}\n\n"
        f"## min_edge ladder (time double on, no size-scale)\n\n"
        f"{out['markdown_min_edge']}\n\n"
        f"Frequency companion: `structure_v1_eth_k5_pred_mean_strength_met_freq_001_latest.json`\n",
        encoding="utf-8",
    )

    print("\n==== SIZE-SCALE REFS ====", flush=True)
    print(out["markdown_size_scale"].encode("ascii", "replace").decode("ascii"), flush=True)
    print("\n==== MIN_EDGE LADDER ====", flush=True)
    print(out["markdown_min_edge"].encode("ascii", "replace").decode("ascii"), flush=True)
    print(f"WROTE {latest}", flush=True)
    print(f"WROTE {md_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
