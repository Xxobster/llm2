"""Finplot frozen single-book arm (mean_strength|hold12|tp1%) vs control.

Default trade overlay cap = 240 (= 2× lockbox usual 120).
Stitches fold-V2 outer OOS signals (same protocol as the transfer report), then
opens Finplot on the full pre-lockbox window.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

os.environ.pop("TRADESIM_NO_PLOT", None)

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim,
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
from llm2.paths import FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.signals.singlebook_clarity import SingleBookArm, build_singlebook_signals  # noqa: E402
from llm2.validation.folds import build_outer_folds, index_to_ms  # noqa: E402

TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
LABEL_HORIZON = 6
SL = 0.02
MIN_EDGE = DIRECTION_BAND
# 2× lockbox DEFAULT_TRADE_CAP (120)
DEFAULT_TRADE_CAP = 240
FROZEN = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)
CONTROL = SingleBookArm(clarity="none", horizon_bars=6, tp_pct=0.01, sl_pct=SL)

# Stitched PFs from gen-1 / transfer reports (title annotation only)
REF_PF = {
    ("ETHUSDT", "frozen"): 3.32,
    ("ETHUSDT", "control"): 1.99,
    ("BTCUSDT", "frozen"): 2.94,
    ("BTCUSDT", "control"): 1.90,
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


def _collect_signals(
    *,
    symbol: str,
    arm: SingleBookArm,
) -> tuple[pd.DataFrame, list, dict]:
    ohlcv = load_ohlcv(symbol, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    feature_cols = [c for c in aligned.columns if c != "y"]
    X = aligned[feature_cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    family = target_family(TARGET)

    all_signals = []
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        sigs, _stats = build_singlebook_signals(
            ts_ms[oos], side, mean, arm=arm, min_edge=MIN_EDGE
        )
        all_signals.extend(sigs)

    # Full OOS calendar window for chart
    oos0 = aligned.index[folds[0].oos_indices[0]]
    oos1 = aligned.index[folds[-1].oos_indices[-1]]
    pad = max(50, int(arm.horizon_bars) * 4)
    pos = int(ohlcv.index.searchsorted(oos0))
    pad_start = ohlcv.index[max(0, pos - pad)]
    window = ohlcv.loc[pad_start:oos1]
    meta = {
        "oos_start": str(oos0),
        "oos_end": str(oos1),
        "n_signals": len(all_signals),
        "n_folds": len(folds),
    }
    return window, all_signals, meta


def _run_and_plot(
    *,
    symbol: str,
    arm: SingleBookArm,
    arm_label: str,
    trade_cap: int,
    show: bool,
) -> dict:
    window, signals, meta = _collect_signals(symbol=symbol, arm=arm)
    touch_tf = touch_timeframe(TIMEFRAME, symbol)
    try:
        touch = load_ohlcv(symbol, touch_tf)
        end = window.index[-1]
        start = window.index[0]
        dec_ms = int(TF_MS[TIMEFRAME])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    except Exception:  # noqa: BLE001
        touch_win = None
        touch_tf = None

    funding = load_funding(symbol)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    lev = float(leverage_from_stop(SL))
    try:
        instrument = research_instrument(symbol)
    except Exception:  # noqa: BLE001
        instrument = None

    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=TIMEFRAME,
        strategy_id=f"frozen-arm-{symbol[:3].lower()}-{arm_label}",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim(max_hold_bars=arm.horizon_bars, decision_timeframe=TIMEFRAME),
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": f"{symbol} {arm.key}",
            "batch": "frozen_singlebook_finplot",
            "arm": arm.key,
        },
        plot=False,
        print_headline=True,
        store_path=None,
    )
    m = bundle.metrics
    pnls = [float(getattr(t, "realized_pnl", 0.0) or 0.0) for t in bundle.result.trades]
    stitch_pf = _pf(pnls)
    ref = REF_PF.get((symbol, arm_label))
    summary = {
        "symbol": symbol,
        "arm": arm.key,
        "arm_label": arm_label,
        "n_signals": meta["n_signals"],
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "stitched_pf_from_trades": stitch_pf,
        "ref_report_pf": ref,
        "net_pnl": float(m.net_pnl),
        "trade_cap": trade_cap,
        "oos": meta,
    }
    print(json.dumps(summary, indent=2), flush=True)

    if show:
        # Chart from first OOS bar (drop pure pad) for readability
        oos_start = pd.Timestamp(meta["oos_start"])
        if oos_start.tzinfo is None:
            oos_start = oos_start.tz_localize("UTC")
        plot_win = window.loc[window.index >= oos_start]
        bars = ohlcv_to_bar_series(plot_win, symbol=symbol, timeframe=TIMEFRAME)
        ctl_ref = REF_PF.get((symbol, "control"))
        frz_ref = REF_PF.get((symbol, "frozen"))
        if arm_label == "frozen" and frz_ref and ctl_ref:
            cmp = f"report frozen PF={frz_ref:.2f} vs control={ctl_ref:.2f} (Δ+{frz_ref-ctl_ref:.2f})"
        else:
            cmp = f"report PF≈{ref}" if ref else f"engine PF={m.profit_factor:.2f}"
        plot_backtest(
            bars,
            bundle.result,
            title=(
                f"{symbol} {TIMEFRAME} direction | {arm_label} {arm.key} | "
                f"[{meta['oos_start'][:10]} -> {meta['oos_end'][:10]}] "
                f"BT_PnL={m.net_pnl:.2f} PF={m.profit_factor:.2f} n={m.n_trades} | {cmp}"
            ),
            metrics=bundle.metrics,
            trade_style="boxes",
            max_zone_trades=trade_cap,
            strategy_meta={
                "name": f"{symbol} direction {arm.key}",
                "symbol": symbol,
                "timeframe": TIMEFRAME,
                "venue_product": "Bybit USDT perpetual",
                "backtest_net_pnl": float(m.net_pnl),
                "backtest_profit_factor": float(m.profit_factor),
                "backtest_n_trades": int(m.n_trades),
                "max_hold_bars": arm.horizon_bars,
                "tp_pct": arm.tp_pct,
                "sl_pct": arm.sl_pct,
                "clarity": arm.clarity,
                "note": (
                    f"Fold-V2 stitched OOS Finplot. Green/red boxes = hold win/loss. "
                    f"Showing last {trade_cap} trades (2× usual lockbox cap of 120)."
                ),
            },
            show=True,
        )
    return summary


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--symbols",
        default="ETHUSDT,BTCUSDT",
        help="comma-separated symbols",
    )
    ap.add_argument(
        "--arms",
        default="frozen,control",
        help="frozen and/or control (comma-separated)",
    )
    ap.add_argument("--trade-cap", type=int, default=DEFAULT_TRADE_CAP)
    ap.add_argument("--no-show", action="store_true")
    args = ap.parse_args()

    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not from botsgeneral")

    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    arm_names = [a.strip().lower() for a in args.arms.split(",") if a.strip()]
    arm_map = {"frozen": FROZEN, "control": CONTROL}

    rows = []
    for sym in symbols:
        for name in arm_names:
            if name not in arm_map:
                raise SystemExit(f"unknown arm {name}")
            print(f"\n=== {sym} {name} trade_cap={args.trade_cap} ===", flush=True)
            rows.append(
                _run_and_plot(
                    symbol=sym,
                    arm=arm_map[name],
                    arm_label=name,
                    trade_cap=int(args.trade_cap),
                    show=not args.no_show,
                )
            )
    print(json.dumps({"charts": len(rows), "trade_cap": args.trade_cap}, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
