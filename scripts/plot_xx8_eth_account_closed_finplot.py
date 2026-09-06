#!/usr/bin/env python3
"""Finplot ALL Xxobster8 ETH closed trades (account PnL) vs structure backtest.

The bots report n=20 is Bybit closed-PnL on the account since 2026-07-09.
Those fills are ETH 1h structure multitrade (31 Jul–6 Aug), NOT the new 15m pivot.

  python -u scripts/plot_xx8_eth_account_closed_finplot.py \\
    --i-accept-lockbox-contamination --i-accept-finplot-lockbox --show
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
if "botsgeneral" not in __import__("tradesim").__file__.replace("\\", "/"):
    raise SystemExit("tradesim must load from botsgeneral")

from tradesim.research.plot import plot_backtest

from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest
from llm2.data.loader import load_ohlcv
from llm2.data.macro import load_funding
from llm2.evidence.lockbox_guard import add_lockbox_guard_args, require_lockbox_access
from llm2.experiments.eth_multitrade_nested import build_multitrade_signals
from llm2.features.registry import build_space
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family
from llm2.paths import ARTIFACTS, TF_MS
from llm2.validation.folds import index_to_ms
from tradesim import Side, Signal
from tradesim import research_instrument, research_margin, research_sim_hedge, research_sizing

CLOSED = ARTIFACTS / "reports" / "_xx8_eth_closed.json"
PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_v1_2"
BT_COLOR = "#2962ff"
LIVE_COLOR = "#ff9800"
PLOT_START = datetime(2026, 7, 30, tzinfo=timezone.utc)
PLOT_END = datetime(2026, 8, 8, tzinfo=timezone.utc)


def _closed_rows() -> list[dict]:
    blob = json.loads(CLOSED.read_text(encoding="utf-8"))
    rows = []
    for t in blob.get("trades") or []:
        if str(t.get("symbol") or "ETHUSDT").upper() != "ETHUSDT":
            continue
        e = int(t.get("createdTime") or 0)
        x = int(t.get("updatedTime") or 0)
        ep = float(t.get("avgEntryPrice") or 0)
        xp = float(t.get("avgExitPrice") or 0)
        if e <= 0 or x <= 0 or ep <= 0 or xp <= 0:
            continue
        rows.append(
            {
                "entry_ts": pd.Timestamp(e, unit="ms", tz="UTC"),
                "exit_ts": pd.Timestamp(x, unit="ms", tz="UTC"),
                "entry_px": ep,
                "exit_px": xp,
                "side": t.get("side"),
                "qty": t.get("qty"),
                "pnl": t.get("closedPnl"),
            }
        )
    return rows


def _bar_i(ts, index: pd.DatetimeIndex) -> int:
    t = pd.Timestamp(ts)
    if t.tzinfo is None:
        t = t.tz_localize("UTC")
    if index.tz is None:
        t = t.tz_localize(None)
    else:
        t = t.tz_convert(index.tz)
    loc = int(index.get_indexer([t], method="nearest")[0])
    return 0 if loc < 0 else loc


def _draw_span(fplt, ax, index: pd.DatetimeIndex, t0, p0, t1, p1, color: str, legend: str | None) -> None:
    """Draw entry→exit on Finplot using integer candle indices (not timestamps)."""
    n = len(index)
    i0 = min(_bar_i(t0, index), n - 1)
    i1 = min(_bar_i(t1, index), n - 1)
    if i1 <= i0:
        i1 = min(i0 + 1, n - 1)
    fplt.add_line((i0, float(p0)), (i1, float(p1)), color=color, width=2, ax=ax)
    fplt.plot([i0], [float(p0)], ax=ax, color=color, style="o", width=3, legend=legend)
    fplt.plot([i1], [float(p1)], ax=ax, color=color, style="x", width=3, legend=None)


def _structure_bt_trades() -> list:
    import joblib

    strategy = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    symbol = "ETHUSDT"
    timeframe = str(strategy.get("timeframe") or "1h")
    sl = float(strategy.get("sl_pct") or 0.02)
    hold = int(strategy.get("horizon_bars") or 6)
    mt = dict(strategy.get("multitrade") or {})
    lookback = int(mt.get("mean_lookback") or 168)
    k_side = int(mt.get("max_positions_per_side") or strategy.get("max_positions_per_side") or 7)
    max_hold_cap = int(mt.get("hold_addon") or hold)
    fam = target_family(str(strategy.get("target") or "direction"))
    min_edge = float(strategy.get("min_edge") or DIRECTION_BAND)
    cfg = {
        "max_positions_per_side": k_side,
        "clarity": str(mt.get("clarity") or "none"),
        "clarity_scope": str(mt.get("clarity_scope") or "addon"),
        "fib_ext": float(mt.get("fib_ext") or 0.0),
        "hold_addon": max_hold_cap,
        "base_hold": hold,
        "base_tp": float(mt.get("base_tp") or strategy.get("tp_pct") or 0.01),
        "base_sl": float(mt.get("base_sl") or sl),
        "mean_lookback": lookback,
        "uniform_books": bool(mt.get("uniform_books", False)),
        "bar_ms": int(TF_MS[timeframe]),
        "strength_quantile": float(mt.get("strength_quantile") or 0.5),
        "geometry": str(mt.get("geometry") or "bar_count"),
        "size_double_within_bars": int(mt.get("size_double_within_bars") or 0),
        "size_double_mult": float(mt.get("size_double_mult") or 2.0),
        "min_edge": min_edge,
        "skip_weak_short_book1": bool(mt.get("skip_weak_short_book1", True)),
    }
    blob = joblib.load(PACK / "model.joblib")
    model = blob["model"] if isinstance(blob, dict) and "model" in blob else blob
    cols = list((blob.get("feature_columns") if isinstance(blob, dict) else None) or strategy.get("feature_columns") or [])
    live_start_ms = int(PLOT_START.timestamp() * 1000)
    live_end_ms = int(PLOT_END.timestamp() * 1000)
    warm_start_ms = live_start_ms - (lookback + 400) * int(TF_MS[timeframe])
    ohlcv = load_ohlcv(symbol, timeframe)
    ohlcv = ohlcv.loc[
        (index_to_ms(ohlcv.index) >= warm_start_ms) & (index_to_ms(ohlcv.index) <= live_end_ms)
    ].copy()
    feats = build_space(ohlcv, "structure_v1", symbol=symbol, timeframe=timeframe, recent_only=False)
    aligned = feats.reindex(columns=cols)
    for c in aligned.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            aligned[c] = aligned[c].fillna(0.0)
    valid = aligned.dropna()
    pred = model.predict(valid.to_numpy(dtype=float))
    mean = np.asarray(pred.mean if hasattr(pred, "mean") else pred, dtype=float).reshape(-1)
    side = proxy_side(mean, fam)
    close_v = ohlcv["close"].reindex(valid.index).to_numpy(dtype=float)
    ts_v = index_to_ms(valid.index)
    emit_mask = (ts_v >= live_start_ms) & (ts_v <= live_end_ms)
    pre_mask = ts_v < live_start_ms
    seed_hist = [float(abs(m)) for m in mean[pre_mask] if np.isfinite(m)][-lookback:]
    occ_ts = index_to_ms(ohlcv.index)
    free_sigs, _ = build_multitrade_signals(
        ts_v[emit_mask],
        side[emit_mask],
        mean[emit_mask],
        cfg=cfg,
        close=close_v[emit_mask],
        seed_strength_hist=seed_hist,
        occupancy_bars={
            "ts_ms": occ_ts,
            "open": ohlcv["open"].to_numpy(dtype=float),
            "high": ohlcv["high"].to_numpy(dtype=float),
            "low": ohlcv["low"].to_numpy(dtype=float),
        },
    )
    try:
        t0 = int(ohlcv.index[0].timestamp() * 1000)
        t1 = int(ohlcv.index[-1].timestamp() * 1000) + int(TF_MS[timeframe]) + 60_000
        touch = load_ohlcv(symbol, "1m", start_ms=t0, end_ms=t1)
    except Exception:
        touch = pd.DataFrame()
    try:
        funding = load_funding(symbol)
        f_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
        f_rt = funding.to_numpy(dtype=float)
    except Exception:
        f_ts = np.asarray([], dtype=np.int64)
        f_rt = np.asarray([], dtype=float)
    w_ts = index_to_ms(ohlcv.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1])) if len(f_ts) else np.asarray([], dtype=bool)
    start, end = ohlcv.index[0], ohlcv.index[-1]
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[timeframe])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    bundle = run_strategy_backtest(
        ohlcv,
        free_sigs,
        symbol=symbol,
        timeframe=timeframe,
        strategy_id="xx8_eth_mt_v12_closed_window",
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe="1m",
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(sl))),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=max_hold_cap,
            decision_timeframe=timeframe,
            max_positions_per_side=max(1, k_side),
            max_positions_per_symbol=max(1, k_side * 2),
        ),
        instrument=research_instrument(symbol),
        funding_ts_ms=f_ts[fmask] if len(f_ts) else None,
        funding_rate=f_rt[fmask] if len(f_ts) else None,
        plot=False,
        print_headline=False,
        store_path=None,
    )
    return list(getattr(getattr(bundle, "result", None), "trades", None) or ())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    add_lockbox_guard_args(ap)
    ap.add_argument("--show", action="store_true")
    args = ap.parse_args(argv)
    live = _closed_rows()
    require_lockbox_access(
        experiment_id="plot_xx8_eth_account_closed_finplot",
        window_start=PLOT_START.date().isoformat(),
        window_end=PLOT_END.date().isoformat(),
        purpose="finplot_xx8_eth_account_closed_vs_structure_bt",
        symbols=["ETHUSDT"],
        accepted_contamination=bool(args.i_accept_lockbox_contamination),
        open_finplot=bool(args.show),
        accepted_finplot=bool(args.i_accept_finplot_lockbox),
        notes=f"n_live_closed={len(live)}",
    )
    ohlcv = load_ohlcv("ETHUSDT", "15m")
    ohlcv = ohlcv.loc[(ohlcv.index >= pd.Timestamp(PLOT_START)) & (ohlcv.index <= pd.Timestamp(PLOT_END))].copy()
    print(f"live_closed_eth={len(live)} 15m_bars={len(ohlcv)}", flush=True)
    bt_trades: list = []
    try:
        bt_trades = _structure_bt_trades()
        print(f"structure_v1_2_bt_trades={len(bt_trades)}", flush=True)
    except Exception as exc:
        print(f"structure_bt_failed {type(exc).__name__}: {exc}", flush=True)
    dummy = run_strategy_backtest(
        ohlcv,
        [],
        symbol="ETHUSDT",
        timeframe="15m",
        strategy_id="xx8_eth_closed_canvas",
        costs=research_costs_baseline(),
        margin=research_margin(leverage=18.0),
        sizing=research_sizing(),
        instrument=research_instrument("ETHUSDT"),
        plot=False,
        print_headline=False,
        store_path=None,
    )

    def on_axes(view) -> None:
        import finplot as fplt

        ax = view.ax_price
        index = view.bars_df.index
        first = True
        for t in bt_trades:
            _draw_span(
                fplt,
                ax,
                index,
                pd.Timestamp(int(t.entry_ts_ms), unit="ms", tz="UTC"),
                float(t.entry_price),
                pd.Timestamp(int(t.exit_ts_ms), unit="ms", tz="UTC"),
                float(t.exit_price),
                BT_COLOR,
                "backtest structure v1.2" if first else None,
            )
            first = False
        first = True
        for lf in live:
            _draw_span(
                fplt,
                ax,
                index,
                lf["entry_ts"],
                lf["entry_px"],
                lf["exit_ts"],
                lf["exit_px"],
                LIVE_COLOR,
                "live Bybit closed" if first else None,
            )
            first = False

    bars = ohlcv_to_bar_series(ohlcv, symbol="ETHUSDT", timeframe="15m")
    empty = replace(dummy.result, trades=())
    title = (
        f"ETHUSDT 15m Xxobster8 ACCOUNT closed  live={len(live)} (orange)  "
        f"structure v1.2 BT={len(bt_trades)} (blue)  2026-07-30→08-08  "
        "NOT the new 15m pivot"
    )
    plot_backtest(
        bars,
        empty,
        title=title,
        show=bool(args.show),
        show_metrics_window=False,
        strategy_meta={"name": "xx8_eth_account_closed", "account": "Xxobster8", "n_live": len(live)},
        on_axes=on_axes,
    )
    print(f"plotted live={len(live)} backtest={len(bt_trades)} show={bool(args.show)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
