#!/usr/bin/env python3
"""Finplot Ether Xxobster8 live vs backtest trades (two colors).

Backtest = blue. Live = orange. Lockbox window; both accept flags required.

  python -u scripts/plot_xx8_eth_live_vs_bt_finplot.py --i-accept-lockbox-contamination --i-accept-finplot-lockbox --show
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

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
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline
from llm2.live.pivot_runner import load_pack
from llm2.paths import ARTIFACTS, TF_MS
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits
from llm2.validation.folds import index_to_ms
from tradesim import Side
from tradesim import research_margin, research_sim_limit_entry, research_sizing
from tradesim.contracts import InstrumentSpec

DUMP = ARTIFACTS / "reports" / "_ln2_xx89_pivot_live.json"
PACK = ARTIFACTS / "live_packs" / "pivot_eth_p75_ctrl_atr_w4"
PLOT_START = datetime(2026, 8, 18, tzinfo=timezone.utc)
SINCE = datetime(2026, 8, 21, tzinfo=timezone.utc)  # Xxobster8 live start (fills only)
SINCE_MS = int(SINCE.timestamp() * 1000)
BT_COLOR = "#2962ff"
LIVE_COLOR = "#ff9800"


def _payloads() -> list[dict]:
    dump = json.loads(DUMP.read_text(encoding="utf-8"))
    rows = ((dump.get("arms") or {}).get("xx8_eth") or {}).get("pivot_decisions") or []
    out = []
    for r in rows:
        p = json.loads(r["payload_json"]) if isinstance(r.get("payload_json"), str) else r
        if int(p.get("bar_ts_ms") or 0) >= SINCE_MS:
            out.append(p)
    return out


def _live_fills(decs: list[dict]) -> list[dict]:
    fills = []
    for p in decs:
        orr = p.get("order_result") or {}
        if p.get("action") != "ENTER_LIMIT" or not orr.get("filled"):
            continue
        fills.append(
            {
                "entry_ts": pd.Timestamp(int(orr.get("entry_bar_ms") or p["bar_ts_ms"]), unit="ms", tz="UTC"),
                "exit_ts": pd.Timestamp(int(orr.get("max_hold_deadline_ms") or 0), unit="ms", tz="UTC")
                if orr.get("max_hold_deadline_ms")
                else None,
                "entry_px": float(orr.get("avg_price") or p["limit_px"]),
                "exit_px": None,
                "side": p.get("side"),
            }
        )
    # fill ledger exits if present
    dump = json.loads(DUMP.read_text(encoding="utf-8"))
    for row in ((dump.get("arms") or {}).get("xx8_eth") or {}).get("pivot_fills") or []:
        payload = json.loads(row["payload_json"]) if isinstance(row.get("payload_json"), str) else row
        fills.append(
            {
                "entry_ts": pd.Timestamp(int(payload.get("entry_bar_ms") or payload.get("bar_ts_ms") or 0), unit="ms", tz="UTC"),
                "exit_ts": pd.Timestamp(row.get("created_utc")) if row.get("event") in {"max_hold_flatten", "exchange_flat"} else None,
                "entry_px": float(payload.get("avg_price") or 0) or None,
                "exit_px": None,
                "side": payload.get("side"),
                "event": row.get("event"),
            }
        )
    return fills


def _instrument(strat: dict) -> InstrumentSpec:
    inst = strat.get("instrument") or {}
    return InstrumentSpec(
        symbol=str(strat["symbol"]),
        tick_size=float(inst.get("tick_size") or 0.01),
        qty_step=float(inst.get("qty_step") or 0.01),
        min_qty=float(inst.get("min_qty") or 0.01),
        min_notional=float(inst.get("min_notional") or 5.0),
        max_qty=float(inst.get("max_qty") or 1e9),
        max_leverage=float(inst.get("max_leverage") or 100.0),
        maintenance_rate=float(inst.get("maintenance_rate") or 0.005),
        source="pack_strategy_json",
    )


def _draw_span(fplt, ax, t0, p0, t1, p1, color: str, legend: str | None) -> None:
    idx = pd.DatetimeIndex([t0, t1])
    fplt.plot(idx, [p0, p1], ax=ax, color=color, width=3, legend=legend)
    fplt.plot([t0], [p0], ax=ax, color=color, style="o", width=3, legend=None)
    fplt.plot([t1], [p1], ax=ax, color=color, style="x", width=3, legend=None)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    add_lockbox_guard_args(ap)
    ap.add_argument("--show", action="store_true")
    args = ap.parse_args(argv)
    require_lockbox_access(
        experiment_id="plot_xx8_eth_live_vs_bt_finplot",
        window_start=PLOT_START.date().isoformat(),
        window_end=datetime.now(timezone.utc).date().isoformat(),
        purpose="finplot_live_vs_bt_xx8_eth",
        symbols=["ETHUSDT"],
        accepted_contamination=bool(args.i_accept_lockbox_contamination),
        open_finplot=bool(args.show),
        accepted_finplot=bool(args.i_accept_finplot_lockbox),
    )
    strat, blob = load_pack(PACK)
    ohlcv_all = load_ohlcv("ETHUSDT", "15m", price_type="last")
    ohlcv = ohlcv_all.loc[ohlcv_all.index >= pd.Timestamp(PLOT_START)].copy()
    decs = _payloads()
    intents = []
    for p in decs:
        if p.get("action") != "ENTER_LIMIT":
            continue
        intents.append(
            LimitIntent(
                decision_ts_ms=int(p["bar_ts_ms"]),
                side=Side.SHORT if p.get("side") == "Sell" else Side.LONG,
                limit_price=float(p["limit_px"]),
                stop_offset=float(strat["sl_pct"]),
                target_offset=float(strat["tp_pct"]),
                max_hold_bars=int(strat["max_hold_bars"]),
                work_bars=int(strat["work_bars"]),
            )
        )
    # Also score-window: if no live ENTER, materialize from local replay of live bars only
    if not intents:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "audit_pivot_ln1", ROOT / "scripts" / "audit_llm2_pivot_live_vs_bt.py"
        )
        assert spec and spec.loader
        audit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(audit)
        scored = audit._score_all(ohlcv_all, strat, blob)
        scored = scored.loc[scored["ts_ms"].astype("int64") >= int(PLOT_START.timestamp() * 1000)]
        for rec in scored.itertuples():
            if rec.action != "ENTER_LIMIT":
                continue
            intents.append(
                LimitIntent(
                    decision_ts_ms=int(rec.ts_ms),
                    side=Side.SHORT if bool(rec.is_short) else Side.LONG,
                    limit_price=float(rec.limit_px),
                    stop_offset=float(strat["sl_pct"]),
                    target_offset=float(strat["tp_pct"]),
                    max_hold_bars=int(strat["max_hold_bars"]),
                    work_bars=int(strat["work_bars"]),
                )
            )
    sigs, _stats = materialize_working_limits(ohlcv, intents, work_bars=int(strat["work_bars"]))
    touch = load_ohlcv("ETHUSDT", "1m", price_type="last")
    try:
        funding = load_funding("ETHUSDT")
        f_ts = (funding.index.asi8 // 1_000_000).astype("int64")
        f_rt = funding.to_numpy(dtype=float)
    except Exception:
        import numpy as np

        f_ts = np.asarray([], dtype="int64")
        f_rt = np.asarray([], dtype=float)
    start, end = ohlcv.index[0], ohlcv.index[-1]
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS["15m"])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    import numpy as np

    fmask = (f_ts >= int(index_to_ms(ohlcv.index)[0])) & (f_ts <= int(index_to_ms(ohlcv.index)[-1])) if len(f_ts) else np.asarray([], dtype=bool)
    bundle = run_strategy_backtest(
        ohlcv,
        sigs,
        symbol="ETHUSDT",
        timeframe="15m",
        strategy_id="xx8_eth_live_window",
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe="1m",
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(float(strat["sl_pct"])))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=int(strat["max_hold_bars"]), decision_timeframe="15m"),
        instrument=_instrument(strat),
        funding_ts_ms=f_ts[fmask] if len(f_ts) else None,
        funding_rate=f_rt[fmask] if len(f_ts) else None,
        plot=False,
        print_headline=True,
        store_path=None,
    )
    live_fills = _live_fills(decs)
    bt_trades = list(getattr(getattr(bundle, "result", None), "trades", None) or ())

    def on_axes(view) -> None:
        import finplot as fplt

        ax = view.ax_price
        first_bt = True
        for t in bt_trades:
            e = pd.Timestamp(int(t.entry_ts_ms), unit="ms", tz="UTC")
            x = pd.Timestamp(int(t.exit_ts_ms), unit="ms", tz="UTC")
            _draw_span(fplt, ax, e, float(t.entry_price), x, float(t.exit_price), BT_COLOR, "backtest" if first_bt else None)
            first_bt = False
        first_live = True
        for lf in live_fills:
            if lf.get("entry_px") is None:
                continue
            t1 = lf.get("exit_ts") or lf["entry_ts"]
            p1 = lf.get("exit_px") or lf["entry_px"]
            _draw_span(fplt, ax, lf["entry_ts"], lf["entry_px"], t1, p1, LIVE_COLOR, "live" if first_live else None)
            first_live = False

    bars = ohlcv_to_bar_series(ohlcv, symbol="ETHUSDT", timeframe="15m")
    empty = replace(bundle.result, trades=())
    n_bt = len(bt_trades)
    n_live = len(live_fills)
    title = (
        f"ETHUSDT 15m Xxobster8 1%/1%  live={n_live} (orange)  backtest={n_bt} (blue)  "
        f"plot {PLOT_START.date().isoformat()}+ live-since {SINCE.date().isoformat()}  LOCKBOX_OPENED_CONTAMINATED"
    )
    plot_backtest(
        bars,
        empty,
        title=title,
        show=bool(args.show),
        show_metrics_window=True,
        metrics=bundle.metrics,
        strategy_meta={"name": "xx8_eth_live_vs_bt", "account": "Xxobster8"},
        on_axes=on_axes,
    )
    print(f"plotted live={n_live} backtest={n_bt} show={bool(args.show)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
