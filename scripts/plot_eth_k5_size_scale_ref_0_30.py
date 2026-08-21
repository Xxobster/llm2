#!/usr/bin/env python3
"""Research display: ETH K5 size-scale ref=0.30 — metrics + Finplot.

MEASURE_DIAGNOSTIC / RESEARCH_ONLY. Hard end = FORWARD_LOCKBOX_START (no lockbox).
Does **not** promote or authorize live. Size formula:

  size_mult = time_mult × clip(|pred_mean| / 0.30, 1.0, 2.0)
  time_mult = 2 if same-side entry within 3h else 1

Examples::

  python scripts/plot_eth_k5_size_scale_ref_0_30.py --show --display-months 12
  python scripts/plot_eth_k5_size_scale_ref_0_30.py --metrics-only
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sim_hedge,
    research_sizing,
)
from tradesim.research.plot import plot_backtest  # noqa: E402

from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest  # noqa: E402
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
from llm2.validation.folds import build_outer_folds, index_to_ms  # noqa: E402

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
K = 5
LABEL_HORIZON = 6
SL = 0.02
MIN_EDGE = DIRECTION_BAND
SIZE_REF = 0.30
GEN = "structure_v1_eth_k5_size_scale_ref_0_30_display_001"
ARM = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)
DEFAULT_TRADE_CAP = 600


def _finite(x: Any) -> Any:
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    if isinstance(x, (np.floating,)):
        v = float(x)
        return None if not math.isfinite(v) else v
    if isinstance(x, (np.integer,)):
        return int(x)
    return x


def _metrics_dict(m: Any) -> dict[str, Any]:
    sh = getattr(m, "sharpe", None)
    return {
        "n_trades": int(m.n_trades),
        "n_longs": int(getattr(m, "n_longs", 0) or 0),
        "n_shorts": int(getattr(m, "n_shorts", 0) or 0),
        "net_pnl": _finite(float(m.net_pnl)),
        "gross_profit": _finite(float(getattr(m, "gross_profit", float("nan")))),
        "gross_loss": _finite(float(getattr(m, "gross_loss", float("nan")))),
        "profit_factor": _finite(float(m.profit_factor)),
        "win_rate": _finite(float(m.win_rate)),
        "expectancy": _finite(float(getattr(m, "expectancy", float("nan")))),
        "expectancy_return_units": _finite(
            float(getattr(m, "expectancy_return_units", float("nan")))
        ),
        "payoff_ratio": _finite(float(getattr(m, "payoff_ratio", float("nan")))),
        "avg_win": _finite(float(getattr(m, "avg_win", float("nan")))),
        "avg_loss": _finite(float(getattr(m, "avg_loss", float("nan")))),
        "total_fees": _finite(float(getattr(m, "total_fees", float("nan")))),
        "total_funding": _finite(float(getattr(m, "total_funding", float("nan")))),
        "total_slippage": _finite(float(getattr(m, "total_slippage", float("nan")))),
        "max_drawdown": _finite(float(getattr(m, "max_drawdown", float("nan")))),
        "max_drawdown_pct": _finite(float(getattr(m, "max_drawdown_pct", float("nan")))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "exposure": _finite(float(getattr(m, "exposure", float("nan")))),
        "sharpe_annualised": _finite(
            float(getattr(sh, "annualised", getattr(sh, "annualized", float("nan"))))
        )
        if sh is not None
        else None,
        "trades_per_month": _finite(float(getattr(m, "trades_per_month", float("nan")))),
        "span_days": _finite(float(getattr(m, "span_days", float("nan")))),
    }


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


def collect_signals(
    *,
    size_scale: bool,
    size_ref: float = SIZE_REF,
) -> tuple[pd.DataFrame, list, dict[str, Any], list[dict], dict[str, Any]]:
    """Outer-fold signals + full OOS window (hard end lockbox). Fold-level metrics."""
    hard_end = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    end_ms = int(hard_end.value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < end_ms].copy()
    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    close_all = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    family = target_family(TARGET)
    instrument = research_instrument(SYMBOL)
    lev = float(leverage_from_stop(SL))
    touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < hard_end]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)

    all_signals: list = []
    fold_rows: list[dict] = []
    all_pnls: list[float] = []
    abs_means: list[float] = []
    size_mults: list[float] = []
    strength_mults: list[float] = []
    total_fees = 0.0
    n_liq = 0

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        sigs, stats = build_cluster_size_signals(
            ts_ms[oos],
            side,
            mean,
            close_all[oos],
            arm=ARM,
            min_edge=MIN_EDGE,
            max_per_side=K,
            instrument=instrument,
            size_double_within_bars=3,
            strength_quantile=0.5,
            size_scale_by_abs_mean=bool(size_scale),
            size_scale_ref=float(size_ref),
            size_scale_factor_min=1.0,
            size_scale_factor_max=2.0,
        )
        all_signals.extend(sigs)
        for s in sigs:
            abs_means.append(float(s.meta.get("abs_mean") or 0.0))
            size_mults.append(float(s.meta.get("size_mult") or 1.0))
            strength_mults.append(float(s.meta.get("strength_size_mult") or 1.0))

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
        label = f"{'ctrl' if not size_scale else f'ref{size_ref}'}-f{fold.fold_index}"
        bundle = run_strategy_backtest(
            window,
            sigs,
            symbol=SYMBOL,
            timeframe=TIMEFRAME,
            strategy_id=label,
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
            strategy_meta={
                "name": label,
                "generation_id": GEN,
                "size_scale_ref": size_ref if size_scale else None,
            },
            plot=False,
            print_headline=False,
            store_path=None,
        )
        md = _metrics_dict(bundle.metrics)
        pnls = [float(getattr(t, "realized_pnl", 0) or 0) for t in bundle.result.trades]
        all_pnls.extend(pnls)
        total_fees += float(md.get("total_fees") or 0.0)
        n_liq += int(md.get("n_liquidations") or 0)
        fold_rows.append({"fold_index": int(fold.fold_index), **md, "n_signals": len(sigs)})
        print(
            f"  fold {fold.fold_index}: n={md['n_trades']} pnl={md['net_pnl']} "
            f"PF={md['profit_factor']} WR={md['win_rate']}",
            flush=True,
        )

    wins = sum(1 for p in all_pnls if p > 0)
    exp_num = exp_den = 0.0
    for fr in fold_rows:
        n = float(fr.get("n_trades") or 0)
        if n > 0 and fr.get("expectancy_return_units") is not None:
            exp_num += float(fr["expectancy_return_units"]) * n
            exp_den += n
    am = np.asarray(abs_means, dtype=float)
    sm = np.asarray(size_mults, dtype=float)
    stm = np.asarray(strength_mults, dtype=float)
    stitched = {
        "n_trades": len(all_pnls),
        "net_pnl": float(np.nansum(all_pnls)),
        "profit_factor": _pf(all_pnls),
        "win_rate": float(wins / len(all_pnls)) if all_pnls else float("nan"),
        "expectancy_return_units": (exp_num / exp_den) if exp_den else float("nan"),
        "total_fees": total_fees,
        "n_liquidations": n_liq,
        "mean_size_mult": float(sm.mean()) if sm.size else None,
        "mean_strength_mult": float(stm.mean()) if stm.size else None,
        "pct_size_lift_met": float((am >= float(size_ref)).mean()) if am.size else None,
        "pct_strength_cap_2x": float((stm >= 2.0 - 1e-12).mean()) if stm.size else None,
        "pct_strength_floor_1x": float((stm <= 1.0 + 1e-12).mean()) if stm.size else None,
    }

    oos0 = aligned.index[folds[0].oos_indices[0]]
    oos1 = aligned.index[folds[-1].oos_indices[-1]]
    pad = max(50, ARM.horizon_bars * 4)
    pos = int(ohlcv.index.searchsorted(oos0))
    window_full = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
    meta = {
        "oos_start": str(oos0),
        "oos_end": str(oos1),
        "n_folds": len(folds),
        "hard_end": str(hard_end),
        "n_signals": len(all_signals),
        "size_scale": bool(size_scale),
        "size_ref": float(size_ref) if size_scale else None,
    }
    return window_full, all_signals, meta, fold_rows, stitched


def display_slice(
    window: pd.DataFrame,
    signals: list,
    meta: dict,
    *,
    months: float | None,
) -> tuple[pd.DataFrame, list, dict]:
    hard_end = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    oos0 = pd.Timestamp(meta["oos_start"])
    if oos0.tzinfo is None:
        oos0 = oos0.tz_localize("UTC")
    oos1 = pd.Timestamp(meta["oos_end"])
    if oos1.tzinfo is None:
        oos1 = oos1.tz_localize("UTC")
    end = min(oos1, hard_end - pd.Timedelta(milliseconds=1))
    if months and months > 0:
        start = max(oos0, hard_end - pd.DateOffset(months=float(months)))
    else:
        start = oos0
    s0 = int(start.value // 1_000_000)
    s1 = int(end.value // 1_000_000)
    clipped = [s for s in signals if s0 <= int(s.ts_ms) <= s1]
    pad = max(50, ARM.horizon_bars * 4)
    pos = int(window.index.searchsorted(start))
    pad_start = window.index[max(0, pos - pad)]
    win = window.loc[(window.index >= pad_start) & (window.index <= end)].copy()
    meta2 = dict(meta)
    meta2["display_start"] = str(start)
    meta2["display_end"] = str(end)
    meta2["n_signals_display"] = len(clipped)
    return win, clipped, meta2


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", action="store_true", help="Open Finplot for ref=0.30 display slice")
    ap.add_argument("--metrics-only", action="store_true", help="Skip Finplot even if --show")
    ap.add_argument(
        "--display-months",
        type=float,
        default=12.0,
        help="Finplot + slice metrics window ending at lockbox (default 12). 0 = full OOS.",
    )
    ap.add_argument("--trade-cap", type=int, default=DEFAULT_TRADE_CAP)
    ap.add_argument("--skip-control", action="store_true", help="Only run ref=0.30 arm")
    args = ap.parse_args(argv)

    show = bool(args.show) and not bool(args.metrics_only)
    if show:
        os.environ.pop("TRADESIM_NO_PLOT", None)
    else:
        os.environ.setdefault("TRADESIM_NO_PLOT", "1")

    months = None if args.display_months <= 0 else float(args.display_months)
    out: dict[str, Any] = {
        "generation_id": GEN,
        "evidence_class": "MEASURE_DIAGNOSTIC",
        "maximum_earned_readiness": "RESEARCH_ONLY",
        "promotion_allowed": False,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "size_scale_ref": SIZE_REF,
        "formula": (
            "size_mult = time_mult × clip(|pred_mean|/0.30, 1, 2); "
            "time_mult = 2 if same-side within 3h else 1"
        ),
        "hard_end_exclusive": str(FORWARD_LOCKBOX_START),
        "lockbox_used": False,
        "note": (
            "Research display only. Same multi-threshold family as "
            "structure_v1_eth_k5_size_scale_ref_thresholds_001 — single mild-ref "
            "view requested by user; not a live freeze."
        ),
    }

    arms_report = {}
    if not args.skip_control:
        print("=== control (time double, no size-scale) ===", flush=True)
        _, _, _, folds_c, st_c = collect_signals(size_scale=False)  # type: ignore[misc]
        arms_report["control_time_double"] = {
            "stitched": st_c,
            "folds": folds_c,
        }
        print(f"CONTROL stitch: {json.dumps(st_c, default=str)}", flush=True)

    print(f"=== size-scale ref={SIZE_REF} ===", flush=True)
    window, signals, meta, folds_r, st_r = collect_signals(  # type: ignore[misc]
        size_scale=True, size_ref=SIZE_REF
    )
    arms_report["size_ref_0_30"] = {"stitched": st_r, "folds": folds_r}
    print(f"REF0.30 stitch: {json.dumps(st_r, default=str)}", flush=True)

    if "control_time_double" in arms_report:
        c = arms_report["control_time_double"]["stitched"]
        out["compare_vs_control"] = {
            "delta_net_pnl": float(st_r["net_pnl"]) - float(c["net_pnl"]),
            "delta_pf": float(st_r["profit_factor"]) - float(c["profit_factor"]),
            "delta_fees": float(st_r["total_fees"]) - float(c["total_fees"]),
            "same_n_trades": int(st_r["n_trades"]) == int(c["n_trades"]),
            "same_wr": abs(float(st_r["win_rate"]) - float(c["win_rate"])) < 1e-12,
            "same_expectancy_return_units": abs(
                float(st_r["expectancy_return_units"]) - float(c["expectancy_return_units"])
            )
            < 1e-15,
        }

    # Display-slice BT for Finplot (optional months tail of OOS)
    win_d, sigs_d, meta_d = display_slice(window, signals, meta, months=months)
    instrument = research_instrument(SYMBOL)
    lev = float(leverage_from_stop(SL))
    hard_end = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    end, start = win_d.index[-1], win_d.index[0]
    dec_ms = int(TF_MS[TIMEFRAME])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < hard_end]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(win_d.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    slice_label = f"eth-k5-size_ref_{SIZE_REF}"
    if months:
        slice_label += f"-last{months:g}m"
    bundle = run_strategy_backtest(
        win_d,
        sigs_d,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=slice_label,
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
        strategy_meta={
            "name": slice_label,
            "generation_id": GEN,
            "size_scale_ref": SIZE_REF,
            "evidence_class": "OOS_SLICE_DISPLAY",
        },
        plot=False,
        print_headline=True,
        store_path=None,
    )
    slice_metrics = _metrics_dict(bundle.metrics)
    out["arms"] = arms_report
    out["display_slice"] = {
        "months": months,
        "meta": meta_d,
        "metrics": slice_metrics,
        "evidence_class": "OOS_SLICE_DISPLAY",
    }
    stamp_min_size_equity_caveat(out)

    reports = ARTIFACTS / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    latest = reports / f"{GEN}_latest.json"
    path = reports / f"{GEN}_{stamp}.json"
    latest.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"WROTE {latest}", flush=True)

    # human summary
    print("\n==== FULL OUTER STITCH (pre-lockbox) ====", flush=True)
    print(
        f"ref={SIZE_REF} n={st_r['n_trades']} net_pnl={st_r['net_pnl']:.2f} "
        f"PF={st_r['profit_factor']:.3f} WR={100*st_r['win_rate']:.1f}% "
        f"E[r]={100*st_r['expectancy_return_units']:.3f}% fees={st_r['total_fees']:.1f} "
        f"mean_x={st_r['mean_size_mult']:.3f} lift_met={100*(st_r['pct_size_lift_met'] or 0):.1f}% "
        f"cap2x={100*(st_r['pct_strength_cap_2x'] or 0):.1f}% liq={st_r['n_liquidations']}",
        flush=True,
    )
    if out.get("compare_vs_control"):
        print(f"vs control: {json.dumps(out['compare_vs_control'])}", flush=True)
    print(
        f"display slice metrics ({meta_d.get('display_start')} -> {meta_d.get('display_end')}): "
        f"n={slice_metrics['n_trades']} pnl={slice_metrics['net_pnl']} "
        f"PF={slice_metrics['profit_factor']} WR={slice_metrics['win_rate']}",
        flush=True,
    )

    if show:
        d0 = str(meta_d.get("display_start") or "")[:10]
        d1 = str(meta_d.get("display_end") or "")[:10]
        disp_start = pd.Timestamp(meta_d["display_start"])
        if disp_start.tzinfo is None:
            disp_start = disp_start.tz_localize("UTC")
        plot_win = win_d.loc[win_d.index >= disp_start]
        bars = ohlcv_to_bar_series(plot_win, symbol=SYMBOL, timeframe=TIMEFRAME)
        m = bundle.metrics
        title = (
            f"{SYMBOL} {TIMEFRAME} K={K} size_ref={SIZE_REF} | RESEARCH_ONLY | "
            f"[{d0} -> {d1}] PF={m.profit_factor:.3f} PnL={m.net_pnl:.2f} n={m.n_trades} "
            f"| not a live freeze"
        )
        plot_backtest(
            bars,
            bundle.result,
            title=title,
            metrics=bundle.metrics,
            trade_style="boxes",
            max_zone_trades=int(args.trade_cap),
            strategy_meta={
                "name": f"{SYMBOL} K={K} size_ref={SIZE_REF}",
                "symbol": SYMBOL,
                "timeframe": TIMEFRAME,
                "size_scale_ref": SIZE_REF,
                "evidence_class": "OOS_SLICE_DISPLAY",
                "maximum_earned_readiness": "RESEARCH_ONLY",
                "promotion_allowed": False,
            },
            show=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
