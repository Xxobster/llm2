"""Finplot + full metrics: ETH K=5 flat 1x vs double-within-3h.

Walk-forward fold V2 stitch (no lockbox). Trade overlay cap default = 600
(= 5x usual lockbox cap of 120).
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path
from typing import Any

os.environ.pop("TRADESIM_NO_PLOT", None)

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
    research_sizing_equity_leverage,
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
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    POST_MULTITRADE_FREEZE_START,
    ROUND_TRIP_COST,
    TF_MS,
    touch_timeframe,
)
from llm2.sizing_policy import (  # noqa: E402
    DEFAULT_EQUITY_FRACTION,
    labelled_money_metrics,
    peak_concurrent_margin_util,
)
from llm2.signals.cluster_concurrency import (  # noqa: E402
    build_cluster_concurrent_signals,
    build_cluster_size_signals,
)
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
BASE = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)
# 5x usual lockbox DEFAULT_TRADE_CAP (120)
DEFAULT_TRADE_CAP = 600
OUT = ARTIFACTS / "reports" / "structure_v1_eth_k5_flat_vs_double_metrics.json"


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
        "profit_factor_note": str(getattr(m, "profit_factor_note", "")),
        "win_rate": _finite(float(m.win_rate)),
        "win_rate_ci_low": _finite(float(getattr(m, "win_rate_ci_low", float("nan")))),
        "win_rate_ci_high": _finite(float(getattr(m, "win_rate_ci_high", float("nan")))),
        "long_win_rate": _finite(float(getattr(m, "long_win_rate", float("nan")))),
        "short_win_rate": _finite(float(getattr(m, "short_win_rate", float("nan")))),
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
        "max_drawdown_duration_days": _finite(
            float(getattr(m, "max_drawdown_duration_days", float("nan")))
        ),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "exposure": _finite(float(getattr(m, "exposure", float("nan")))),
        "sharpe_raw_periodic": _finite(float(getattr(sh, "raw_periodic", float("nan"))))
        if sh
        else None,
        "sharpe_annualised": _finite(float(getattr(sh, "annualised", float("nan"))))
        if sh
        else None,
        "sharpe_hac_raw": _finite(float(getattr(sh, "hac_raw", float("nan")))) if sh else None,
        "sharpe_hac_annualised": _finite(float(getattr(sh, "hac_annualised", float("nan"))))
        if sh
        else None,
        "sortino_annualised": _finite(float(getattr(m, "sortino_annualised", float("nan")))),
        "calmar": _finite(float(getattr(m, "calmar", float("nan")))),
        "sqn": _finite(float(getattr(m, "sqn", float("nan")))),
        "trades_per_month": _finite(float(getattr(m, "trades_per_month", float("nan")))),
        "span_days": _finite(float(getattr(m, "span_days", float("nan")))),
        "wallet_start": _finite(float(getattr(m, "starting_equity", float("nan")))),
        "wallet_end": _finite(float(getattr(m, "ending_equity", float("nan")))),
    }


def _collect(
    size_mode: str,
    instrument: Any,
    *,
    hard_end: pd.Timestamp,
) -> tuple[pd.DataFrame, list, dict[str, Any]]:
    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    end_ms = int(hard_end.value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < end_ms].copy()
    if ohlcv.empty:
        raise SystemExit(f"no bars before hard_end={hard_end}")
    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    close_all = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)
    feature_cols = [c for c in aligned.columns if c != "y"]
    X = aligned[feature_cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    family = target_family(TARGET)

    all_signals: list = []
    signal_stats_acc = {"n_emitted": 0, "n_size_1x": 0, "n_size_2x": 0, "n_addon": 0}
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        if size_mode == "flat_1x":
            sigs, stats = build_cluster_concurrent_signals(
                ts_ms[oos],
                side,
                mean,
                arm=BASE,
                min_edge=MIN_EDGE,
                max_per_side=K,
                cluster_bars=None,
            )
        else:
            sigs, stats = build_cluster_size_signals(
                ts_ms[oos],
                side,
                mean,
                close_all[oos],
                arm=BASE,
                min_edge=MIN_EDGE,
                max_per_side=K,
                instrument=instrument,
                size_double_within_bars=3,
            )
        all_signals.extend(sigs)
        signal_stats_acc["n_emitted"] += int(stats.get("n_emitted", 0))
        signal_stats_acc["n_size_1x"] += int(stats.get("n_size_1x", 0))
        signal_stats_acc["n_size_2x"] += int(stats.get("n_size_2x", 0))
        signal_stats_acc["n_addon"] += int(stats.get("n_addon", 0))

    oos0 = aligned.index[folds[0].oos_indices[0]]
    oos1 = aligned.index[folds[-1].oos_indices[-1]]
    pad = max(50, BASE.horizon_bars * 4)
    pos = int(ohlcv.index.searchsorted(oos0))
    pad_start = ohlcv.index[max(0, pos - pad)]
    window = ohlcv.loc[pad_start:oos1]
    meta = {
        "oos_start": str(oos0),
        "oos_end": str(oos1),
        "n_folds": len(folds),
        "signal_stats": signal_stats_acc,
        "n_signals": len(all_signals),
        "hard_end": str(hard_end),
    }
    return window, all_signals, meta


def _resolve_display_window(
    *,
    months: float | None,
    days: float | None,
    allow_lockbox: bool,
    allow_post_peek: bool,
) -> tuple[pd.Timestamp | None, pd.Timestamp, str]:
    """Return (plot_start_or_None, hard_end, evidence_class).

    Default hard end is FORWARD_LOCKBOX_START — display only of frozen OOS stays
    non-contaminating for promotion. Crossing into the lockbox is diagnostic-only
    and requires an explicit flag (and peeks that window).
    """
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    post = pd.Timestamp(POST_MULTITRADE_FREEZE_START, tz="UTC")
    hard_end = lock
    evidence = "OOS_SLICE_DISPLAY"
    if allow_lockbox:
        hard_end = post if not allow_post_peek else pd.Timestamp.now(tz="UTC")
        evidence = "LOCKBOX_DIAGNOSTIC_CONTAMINATED"
        if allow_post_peek and hard_end > post:
            evidence = "POST_FREEZE_FORWARD_OR_PEEK"
    if days is not None and days > 0:
        start = hard_end - pd.Timedelta(days=float(days))
        return start, hard_end, evidence
    if months is None or months <= 0:
        return None, hard_end, evidence
    start = hard_end - pd.DateOffset(months=float(months))
    return start, hard_end, evidence


def _clip_to_display(
    window: pd.DataFrame,
    signals: list,
    *,
    plot_start: pd.Timestamp | None,
    hard_end: pd.Timestamp,
    meta: dict[str, Any],
) -> tuple[pd.DataFrame, list, dict[str, Any]]:
    """Clip OHLC and signals to the display slice; pad left so hold/TP resolution works."""
    oos0 = pd.Timestamp(meta["oos_start"])
    if oos0.tzinfo is None:
        oos0 = oos0.tz_localize("UTC")
    oos1 = pd.Timestamp(meta["oos_end"])
    if oos1.tzinfo is None:
        oos1 = oos1.tz_localize("UTC")
    end = min(oos1, hard_end - pd.Timedelta(milliseconds=1))
    start = oos0 if plot_start is None else max(oos0, plot_start)
    if start >= end:
        raise SystemExit(f"empty display window: start={start} end={end}")

    # Drop signals outside the display window (entries only in slice).
    s0 = int(start.value // 1_000_000)
    s1 = int(end.value // 1_000_000)
    clipped_sigs = [s for s in signals if s0 <= int(s.ts_ms) <= s1]

    pad = max(50, BASE.horizon_bars * 4)
    pos = int(window.index.searchsorted(start))
    pad_start = window.index[max(0, pos - pad)]
    win = window.loc[(window.index >= pad_start) & (window.index <= end)].copy()
    meta = dict(meta)
    meta["display_start"] = str(start)
    meta["display_end"] = str(end)
    meta["n_signals_display"] = len(clipped_sigs)
    return win, clipped_sigs, meta


def _run_one(
    size_mode: str,
    *,
    trade_cap: int,
    show: bool,
    display_months: float | None,
    display_days: float | None,
    starting_equity: float,
    leverage: float | None,
    sizing_mode: str,
    equity_fraction: float,
    allow_lockbox: bool,
    allow_post_peek: bool,
) -> dict[str, Any]:
    instrument = research_instrument(SYMBOL)
    plot_start, hard_end, evidence = _resolve_display_window(
        months=display_months,
        days=display_days,
        allow_lockbox=allow_lockbox,
        allow_post_peek=allow_post_peek,
    )
    window, signals, meta = _collect(size_mode, instrument, hard_end=hard_end)
    window, signals, meta = _clip_to_display(
        window,
        signals,
        plot_start=plot_start,
        hard_end=hard_end,
        meta=meta,
    )
    meta["evidence_class"] = evidence
    if evidence.startswith("LOCKBOX") or evidence.startswith("POST_FREEZE"):
        print(
            f"EVIDENCE_CLASS={evidence} — display/metrics are diagnostic only; "
            "do not promote or retune on this slice.",
            flush=True,
        )
    else:
        print(
            f"EVIDENCE_CLASS={evidence} — frozen arm, pre-lockbox OOS slice only "
            f"(hard_end={hard_end.date()}); not a re-selection.",
            flush=True,
        )

    try:
        touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
        touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
        end = window.index[-1]
        start = window.index[0]
        dec_ms = int(TF_MS[TIMEFRAME])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    except Exception:  # noqa: BLE001
        touch_win = None
        touch_tf = None

    funding = load_funding(SYMBOL)
    funding = funding[funding.index < hard_end]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    lev = float(leverage) if leverage is not None else float(leverage_from_stop(SL))
    smode = str(sizing_mode).upper()
    if smode in ("EQUITY_LEVERAGE", "EQUITY_LEVERAGE_NOTIONAL", "N_EQ_X_LEV"):
        sizing = research_sizing_equity_leverage(
            equity_fraction=float(equity_fraction),
            compound=True,
        )
        sizing_label = "EQUITY_LEVERAGE_NOTIONAL"
    else:
        sizing = research_sizing()
        sizing_label = "MIN_EXCHANGE"

    label = f"{SYMBOL[:3].lower()}-k{K}-{size_mode}"
    if display_days:
        label = f"{label}-last{display_days:g}d"
    elif display_months:
        label = f"{label}-last{display_months:g}m"
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=label,
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=sizing,
        sim=research_sim_hedge(
            starting_equity=float(starting_equity),
            max_hold_bars=BASE.horizon_bars,
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=K,
            max_positions_per_symbol=K * 2,
        ),
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": label,
            "batch": "k5_flat_vs_double",
            "k": K,
            "evidence_class": evidence,
            "starting_equity_usdt": float(starting_equity),
            "sizing": sizing_label,
            "equity_fraction": float(equity_fraction) if sizing_label.startswith("EQUITY") else None,
            "notional_formula": (
                "equity*equity_fraction*leverage"
                if sizing_label.startswith("EQUITY")
                else "min_exchange"
            ),
        },
        plot=False,
        print_headline=True,
        store_path=None,
        starting_equity=float(starting_equity),
    )
    m = bundle.metrics
    metrics = _metrics_dict(m)
    money = labelled_money_metrics(m, starting_equity=float(starting_equity))
    peak = peak_concurrent_margin_util(
        bundle.result.trades,
        starting_equity=float(starting_equity),
        leverage=float(lev),
        compound=True,
    )
    metrics.update(money)
    metrics["peak_concurrent_margin"] = peak
    row = {
        "name": label,
        "k": K,
        "size_mode": size_mode,
        "base_arm": BASE.key,
        "leverage": lev,
        "starting_equity_usdt": float(starting_equity),
        "sizing": sizing_label,
        "equity_fraction": float(equity_fraction) if sizing_label.startswith("EQUITY") else None,
        "evidence_class": evidence,
        "oos": meta,
        "metrics": metrics,
        "money_labels": money,
        "peak_concurrent_margin": peak,
    }
    print(
        json.dumps(
            {
                "arm": size_mode,
                "evidence_class": evidence,
                "sizing": sizing_label,
                "equity_fraction": row["equity_fraction"],
                "leverage": lev,
                "money_labels": money,
                "peak_concurrent_margin": peak,
                "metrics": metrics,
            },
            indent=2,
        ),
        flush=True,
    )

    if show:
        disp_start = pd.Timestamp(meta.get("display_start") or meta["oos_start"])
        if disp_start.tzinfo is None:
            disp_start = disp_start.tz_localize("UTC")
        plot_win = window.loc[window.index >= disp_start]
        bars = ohlcv_to_bar_series(plot_win, symbol=SYMBOL, timeframe=TIMEFRAME)
        d0 = str(meta.get("display_start") or meta["oos_start"])[:10]
        d1 = str(meta.get("display_end") or meta["oos_end"])[:10]
        wr = money.get("wallet_return")
        roi = money.get("roi_on_invested_notional")
        title = (
            f"{SYMBOL} {TIMEFRAME} K={K} {size_mode} | {BASE.key} | {evidence} | "
            f"{sizing_label} N={equity_fraction:g} lev={lev:g} wallet={starting_equity:g} | "
            f"[{d0} -> {d1}] PF={m.profit_factor:.3f} "
            f"PnL={m.net_pnl:.2f} wallet%={(wr or float('nan')):.2%} "
            f"ROII={(roi or float('nan')):.2%} n={m.n_trades}"
        )
        plot_backtest(
            bars,
            bundle.result,
            title=title,
            metrics=bundle.metrics,
            trade_style="boxes",
            max_zone_trades=trade_cap,
            strategy_meta={
                "name": f"{SYMBOL} K={K} {size_mode}",
                "symbol": SYMBOL,
                "timeframe": TIMEFRAME,
                "k": K,
                "size_mode": size_mode,
                "evidence_class": evidence,
                "starting_equity_usdt": float(starting_equity),
                "sizing": sizing_label,
                "equity_fraction": float(equity_fraction),
                "wallet_return": money.get("wallet_return"),
                "roi_on_invested_notional": money.get("roi_on_invested_notional"),
                "peak_margin_utilisation": peak.get("peak_margin_utilisation"),
                "backtest_net_pnl": float(m.net_pnl),
                "backtest_profit_factor": float(m.profit_factor),
                "backtest_n_trades": int(m.n_trades),
                "note": (
                    f"Display slice {d0}→{d1}; {sizing_label}; "
                    f"notional=equity×{equity_fraction:g}×lev when equity mode. "
                    f"Class={evidence}."
                ),
            },
            show=True,
        )
    return row


def _compare(flat: dict[str, Any], dbl: dict[str, Any]) -> dict[str, Any]:
    fm, dm = flat["metrics"], dbl["metrics"]
    keys = sorted(set(fm) | set(dm))
    deltas = {}
    for k in keys:
        a, b = fm.get(k), dm.get(k)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if a is not None and b is not None:
                deltas[k] = b - a
    return {
        "flat_1x": flat,
        "double_within_3h": dbl,
        "delta_double_minus_flat": deltas,
        "headline": {
            "flat_pf": fm.get("profit_factor"),
            "double_pf": dm.get("profit_factor"),
            "delta_pf": deltas.get("profit_factor"),
            "flat_pnl": fm.get("net_pnl"),
            "double_pnl": dm.get("net_pnl"),
            "delta_pnl": deltas.get("net_pnl"),
            "flat_n": fm.get("n_trades"),
            "double_n": dm.get("n_trades"),
            "flat_wr": fm.get("win_rate"),
            "double_wr": dm.get("win_rate"),
            "flat_mdd_pct": fm.get("max_drawdown_pct"),
            "double_mdd_pct": dm.get("max_drawdown_pct"),
            "flat_fees": fm.get("total_fees"),
            "double_fees": dm.get("total_fees"),
            "flat_funding": fm.get("total_funding"),
            "double_funding": dm.get("total_funding"),
            "flat_sharpe_ann": fm.get("sharpe_annualized"),
            "double_sharpe_ann": dm.get("sharpe_annualized"),
        },
    }


def _print_full_table(comp: dict[str, Any]) -> None:
    fm = comp["flat_1x"]["metrics"]
    dm = comp["double_within_3h"]["metrics"]
    keys = [
        "n_trades",
        "n_longs",
        "n_shorts",
        "net_pnl",
        "gross_profit",
        "gross_loss",
        "profit_factor",
        "win_rate",
        "win_rate_ci_low",
        "win_rate_ci_high",
        "long_win_rate",
        "short_win_rate",
        "expectancy",
        "payoff_ratio",
        "avg_win",
        "avg_loss",
        "total_fees",
        "total_funding",
        "total_slippage",
        "max_drawdown",
        "max_drawdown_pct",
        "max_drawdown_duration_days",
        "sharpe_raw",
        "sharpe_annualized",
        "sortino",
        "n_liquidations",
        "entry_bar_exits",
        "exposure",
    ]
    print("\n" + "=" * 88, flush=True)
    print(
        f"{'metric':32} {'flat_1x':>16} {'double_3h':>16} {'delta(d-f)':>16}",
        flush=True,
    )
    print("-" * 88, flush=True)
    for k in keys:
        a, b = fm.get(k), dm.get(k)
        if isinstance(a, float) and isinstance(b, float):
            d = b - a
            if "rate" in k or "pct" in k or k in {"exposure", "sharpe_raw", "sharpe_annualized", "sortino"}:
                print(f"{k:32} {a:16.4f} {b:16.4f} {d:+16.4f}", flush=True)
            else:
                print(f"{k:32} {a:16.4f} {b:16.4f} {d:+16.4f}", flush=True)
        elif isinstance(a, int) and isinstance(b, int):
            print(f"{k:32} {a:16d} {b:16d} {b-a:+16d}", flush=True)
        else:
            print(f"{k:32} {a!s:>16} {b!s:>16}", flush=True)
    print("=" * 88, flush=True)
    # signal stats
    print("\nSignal emission stats:", flush=True)
    print(" flat:", comp["flat_1x"]["oos"]["signal_stats"], flush=True)
    print(" double:", comp["double_within_3h"]["oos"]["signal_stats"], flush=True)


def main() -> int:
    global SYMBOL, TARGET, MIN_EDGE, OUT
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--trade-cap", type=int, default=DEFAULT_TRADE_CAP)
    ap.add_argument("--no-show", action="store_true")
    ap.add_argument(
        "--symbol",
        default=SYMBOL,
        help="e.g. ETHUSDT / BTCUSDT / SOLUSDT (Track2 live pack parent)",
    )
    ap.add_argument(
        "--target",
        default=None,
        help="direction (default for ETH/SOL) or fwd_return (default for BTC)",
    )
    ap.add_argument(
        "--arms",
        default="flat_1x,double_within_3h",
        help="comma list: flat_1x and/or double_within_3h",
    )
    ap.add_argument(
        "--display-months",
        type=float,
        default=None,
        help=(
            "Zoom sim+Finplot to the last N months ending at the hard end "
            "(default hard end = FORWARD_LOCKBOX_START). Frozen arm only; "
            "does not re-select parameters."
        ),
    )
    ap.add_argument(
        "--display-days",
        type=float,
        default=None,
        help=(
            "Zoom sim+Finplot to the last N days ending at the hard end "
            "(default hard end = FORWARD_LOCKBOX_START). Overrides --display-months."
        ),
    )
    ap.add_argument(
        "--starting-equity",
        type=float,
        default=10_000.0,
        help="Sim wallet start in USDT (live-like micro: 100; research default 10000).",
    )
    ap.add_argument(
        "--leverage",
        type=float,
        default=None,
        help="Override leverage (default: leverage_from_stop(SL) with haircut, e.g. 18).",
    )
    ap.add_argument(
        "--sizing",
        default="equity_leverage",
        choices=("equity_leverage", "min_exchange"),
        help="equity_leverage: notional=equity×N×lev (default); min_exchange: venue min qty.",
    )
    ap.add_argument(
        "--equity-fraction",
        type=float,
        default=DEFAULT_EQUITY_FRACTION,
        help="N in notional=equity×N×leverage (default 0.01).",
    )
    ap.add_argument(
        "--allow-lockbox",
        action="store_true",
        help=(
            "Allow bars on/after FORWARD_LOCKBOX_START (diagnostic/contaminated). "
            "Default refuses so a plain --display-months stays pre-lockbox OOS."
        ),
    )
    ap.add_argument(
        "--allow-post-peek",
        action="store_true",
        help="With --allow-lockbox, extend hard end past POST_MULTITRADE_FREEZE_START to now.",
    )
    ap.add_argument(
        "--run-id",
        default=None,
        help=(
            "Reopen a stored tradesim run_id (no resim). Labels output REOPEN_ONLY — "
            "never freeze evidence from a fresh simulation when this flag is set."
        ),
    )
    ap.add_argument(
        "--from-pack",
        default=None,
        help=(
            "version_id registered in live_pack_versions; reopens primary tradesim "
            "run_id if evidence.tradesim_run_ids is set. Refuses freeze-evidence label."
        ),
    )
    args = ap.parse_args()
    if args.run_id or args.from_pack:
        from llm2.evidence.pack_registry import open_pack_run, primary_run_id

        if args.run_id and args.from_pack:
            raise SystemExit("use only one of --run-id / --from-pack")
        rid = args.run_id or primary_run_id(str(args.from_pack))
        if not rid:
            raise SystemExit(
                f"no tradesim run_id for --from-pack={args.from_pack!r}; "
                "pack evidence missing run ids — cannot open without resim "
                "(refuse freeze-evidence from a fresh plot)"
            )
        info = open_pack_run(
            version_id=str(args.from_pack) if args.from_pack else None,
            run_id=str(rid),
        )
        print(json.dumps({"mode": "REOPEN_ONLY", **info}, indent=2), flush=True)
        if not info.get("cli_ok") and not info.get("report_dir"):
            raise SystemExit(
                f"could not reopen run_id={rid}: {info.get('cli_detail')}"
            )
        print(
            "REOPEN_ONLY: chart/metrics from stored tradesim run — not a new simulation.",
            flush=True,
        )
        return 0
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not from botsgeneral")
    if args.allow_post_peek and not args.allow_lockbox:
        raise SystemExit("--allow-post-peek requires --allow-lockbox")
    if args.starting_equity <= 0:
        raise SystemExit("--starting-equity must be > 0")
    if args.leverage is not None and args.leverage <= 0:
        raise SystemExit("--leverage must be > 0")

    SYMBOL = str(args.symbol).upper()
    if args.target:
        TARGET = str(args.target).strip().lower()
    else:
        TARGET = "fwd_return" if SYMBOL.startswith("BTC") else "direction"
    MIN_EDGE = (
        float(DIRECTION_BAND)
        if target_family(TARGET) == "directional"
        else float(ROUND_TRIP_COST)
    )
    slice_tag = ""
    if args.display_days:
        slice_tag = f"_last{args.display_days:g}d"
    elif args.display_months:
        slice_tag = f"_last{args.display_months:g}m"
    equity_tag = f"_eq{args.starting_equity:g}"
    lev_tag = f"_lev{args.leverage:g}" if args.leverage is not None else ""
    size_tag = f"_sz{args.sizing}"
    if args.sizing.startswith("equity"):
        size_tag += f"_N{args.equity_fraction:g}"
    OUT = (
        ARTIFACTS
        / "reports"
        / (
            f"structure_v1_{SYMBOL.lower()}_k5_flat_vs_double"
            f"{slice_tag}{equity_tag}{lev_tag}{size_tag}_metrics.json"
        )
    )
    lev_note = f"{args.leverage:g}" if args.leverage is not None else "from_stop"
    print(
        f"CONFIG symbol={SYMBOL} target={TARGET} min_edge={MIN_EDGE} K={K} arm={BASE.key} "
        f"starting_equity={args.starting_equity:g} leverage={lev_note} "
        f"sizing={args.sizing} equity_fraction={args.equity_fraction:g}",
        flush=True,
    )

    arms = [a.strip() for a in args.arms.split(",") if a.strip()]
    rows = {}
    for mode in arms:
        print(
            f"\n=== running {SYMBOL} {mode} trade_cap={args.trade_cap} "
            f"display_days={args.display_days} display_months={args.display_months} "
            f"equity={args.starting_equity:g} leverage={lev_note} sizing={args.sizing} ===",
            flush=True,
        )
        rows[mode] = _run_one(
            mode,
            trade_cap=int(args.trade_cap),
            show=not args.no_show,
            display_months=args.display_months,
            display_days=args.display_days,
            starting_equity=float(args.starting_equity),
            leverage=float(args.leverage) if args.leverage is not None else None,
            sizing_mode=str(args.sizing),
            equity_fraction=float(args.equity_fraction),
            allow_lockbox=bool(args.allow_lockbox),
            allow_post_peek=bool(args.allow_post_peek),
        )

    if "flat_1x" in rows and "double_within_3h" in rows:
        comp = _compare(rows["flat_1x"], rows["double_within_3h"])
        _print_full_table(comp)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(comp, indent=2), encoding="utf-8")
        print(f"\nwrote full metrics -> {OUT}", flush=True)
    elif len(rows) == 1:
        only = next(iter(rows.values()))
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(only, indent=2), encoding="utf-8")
        print(f"\nwrote metrics -> {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
