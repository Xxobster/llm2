"""Report (optional Finplot) frozen structure_v1 packs on the forward lockbox.

Uses the live pack model.joblib (train cut matches deploy).

**Sealed by default (D-038):** evaluating bars on/after FORWARD_LOCKBOX_START
requires ``--i-accept-lockbox-contamination``. Interactive Finplot additionally
requires ``--i-accept-finplot-lockbox`` and ``--show``. Every authorized open
appends the peek log. Prefer outer-fold settle for quotable evidence.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

# Default sealed: no interactive Finplot until dual accept.
os.environ.setdefault("TRADESIM_NO_PLOT", "1")

_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

import joblib
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

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.models.base import Prediction  # noqa: E402
from llm2.evidence.lockbox_guard import (  # noqa: E402
    add_lockbox_guard_args,
    require_lockbox_access,
    seal_finplot_unless_authorized,
)
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROUND_TRIP_COST, touch_timeframe  # noqa: E402
from llm2.research_policy import PolicyError  # noqa: E402
from llm2.signals.translate import predictions_to_signals  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SPACE = "structure_v1"
HORIZON = 6
TP = 0.01
SL = 0.02
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
DEFAULT_TRADE_CAP = 120

PACKS = {
    "ETHUSDT": ARTIFACTS / "live_packs" / "structure_v1_ethusdt_direction",
    "SOLUSDT": ARTIFACTS / "live_packs" / "structure_v1_solusdt_direction",
    "LINKUSDT": ARTIFACTS / "live_packs" / "structure_v1_linkusdt_direction",
    "VETUSDT": ARTIFACTS / "live_packs" / "structure_v1_vetusdt_direction",
    "ADAUSDT": ARTIFACTS / "live_packs" / "structure_v1_adausdt_direction",
}


def _run_one(
    *,
    symbol: str,
    pack_dir: Path,
    start: str,
    trade_cap: int,
    store: bool,
    show: bool,
) -> dict:
    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(pack_dir / "model.joblib")
    model = blob["model"]
    cols = list(blob["feature_columns"])
    target = str(strategy["target"])
    timeframe = str(strategy["timeframe"])
    family = target_family(target)
    min_edge = float(strategy.get("min_edge") or (
        DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    ))

    ohlcv = load_ohlcv(symbol, timeframe)
    start_ts = pd.Timestamp(start, tz="UTC")
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    # Need lookback before lockbox for features / holds; sim window starts at start_ts.
    feat_ohlcv = ohlcv.copy()
    feats = build_space(feat_ohlcv, SPACE, symbol=symbol, timeframe=timeframe)
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    for c in feats.columns:
        if c.startswith("last_retrace_pct_"):
            feats[c] = feats[c].fillna(0.0)
    aligned = feats.dropna()
    lock_mask = aligned.index >= start_ts
    if int(lock_mask.sum()) < 50:
        raise RuntimeError(
            f"{symbol}: insufficient lockbox bars after {start} "
            f"(have {int(lock_mask.sum())}, data ends {ohlcv.index.max()})"
        )

    X = aligned.loc[lock_mask].to_numpy(dtype=float)
    ts_idx = aligned.index[lock_mask]
    ts_ms = index_to_ms(ts_idx)
    pred = model.predict(X)
    mean = pred.mean if pred.mean is not None else np.zeros(len(ts_idx))
    mean = np.asarray(mean, dtype=float).reshape(-1)
    side = proxy_side(mean, family)
    signals = predictions_to_signals(
        ts_ms,
        Prediction(side=side, mean=mean),
        tp_pct=TP,
        sl_pct=SL,
        min_edge=min_edge,
    )

    end_ts = ts_idx[-1]
    # Pad history so entry-bar / funding resolution has context.
    window = ohlcv.loc[:end_ts]
    window = window.loc[window.index >= (start_ts - pd.Timedelta(days=14))]
    touch_tf = touch_timeframe(timeframe, symbol)
    try:
        from llm2.paths import TF_MS

        dec_ms = int(TF_MS[timeframe])
        touch = load_ohlcv(symbol, touch_tf)
        # Touch must cover through the *end* of the last decision bar, not its open.
        # Slicing touch to end_ts alone leaves the final hour with only the :00 1m child.
        touch_end = end_ts + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[:touch_end]
        touch_win = touch_win.loc[touch_win.index >= (start_ts - pd.Timedelta(days=14))]
        # Drop a trailing decision bar still forming (incomplete touch children).
        touch_ms = int(TF_MS[touch_tf])
        need = dec_ms // touch_ms
        last_dec = int(window["ts_ms"].iloc[-1]) if "ts_ms" in window.columns else int(
            window.index[-1].value // 1_000_000
        )
        t_ts = (
            touch_win["ts_ms"].to_numpy(dtype=np.int64)
            if "ts_ms" in touch_win.columns
            else (touch_win.index.asi8 // 1_000_000).astype(np.int64)
        )
        lo = int(np.searchsorted(t_ts, last_dec, side="left"))
        hi = int(np.searchsorted(t_ts, last_dec + dec_ms, side="left"))
        if hi - lo < need:
            window = window.iloc[:-1]
            end_ts = window.index[-1]
            touch_end = end_ts + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
            touch_win = touch.loc[
                (touch.index >= (start_ts - pd.Timedelta(days=14))) & (touch.index <= touch_end)
            ]
    except Exception:  # noqa: BLE001
        touch_win = None
        touch_tf = None

    funding = load_funding(symbol)
    if funding.empty:
        raise RuntimeError(f"{symbol}: no funding — refusing lockbox plot without live cost")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))

    lev = leverage_from_stop(SL)
    try:
        instrument = research_instrument(symbol)
    except Exception:  # noqa: BLE001
        instrument = None

    bot = f"llm2-structure-{symbol[:3].lower()}"
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=timeframe,
        strategy_id=f"llm2-structure_v1-{symbol.lower()}-{target}-lockbox",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim(max_hold_bars=HORIZON, decision_timeframe=timeframe),
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": f"{symbol} {timeframe} {target}",
            "symbol": symbol,
            "timeframe": timeframe,
            "batch": "structure_v1_lockbox_open",
            "target": target,
            "tp_pct": TP,
            "sl_pct": SL,
            "min_edge": min_edge,
            "leverage": lev,
            "min_size_caveat": True,
            "lockbox_start": start,
            "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
        },
        plot=False,
        print_headline=True,
        store_path=str(STORE) if store else None,
    )
    m = bundle.metrics
    # Restrict reported trades to those entering on/after lockbox start.
    start_ms = int(start_ts.value // 1_000_000)
    trades = [
        t
        for t in bundle.result.trades
        if int(getattr(t, "entry_ts_ms", 0) or 0) >= start_ms
    ]
    summary = {
        "symbol": symbol,
        "target": target,
        "pack": str(pack_dir),
        "lockbox_start": start,
        "data_end": str(end_ts),
        "n_signals": int(len(signals)),
        "n_trades": int(len(trades)),
        "n_trades_engine": int(m.n_trades),
        "net_pnl": float(m.net_pnl),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "total_funding": float(getattr(m, "total_funding", float("nan"))),
        "n_longs": int(getattr(m, "n_longs", 0) or 0),
        "n_shorts": int(getattr(m, "n_shorts", 0) or 0),
        "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
    }
    print(json.dumps(summary, indent=2), flush=True)

    if show:
        bars = ohlcv_to_bar_series(window.loc[window.index >= start_ts], symbol=symbol, timeframe=timeframe)
        # Re-slice result trades visually: plot_backtest uses bundle.result; pass full result
        # but title states lockbox window. Boxes still drawn for trades in window.
        plot_backtest(
            bars,
            bundle.result,
            title=(
                f"{symbol} {timeframe} | structure_v1 {target} LOCKBOX "
                f"[{start_ts.date()} -> {end_ts.date()}] "
                f"BT_PnL={m.net_pnl:.2f} PF={m.profit_factor:.2f} n={m.n_trades} "
                f"L/S={summary['n_longs']}/{summary['n_shorts']}"
            ),
            metrics=bundle.metrics,
            trade_style="boxes",
            max_zone_trades=trade_cap,
            strategy_meta={
                "name": f"{symbol} {timeframe} structure_v1 {target}",
                "symbol": symbol,
                "timeframe": timeframe,
                "venue_product": "Bybit USDT perpetual",
                "bots": [bot],
                "backtest_net_pnl": float(m.net_pnl),
                "backtest_profit_factor": float(m.profit_factor),
                "backtest_n_trades": int(m.n_trades),
                "n_longs": summary["n_longs"],
                "n_shorts": summary["n_shorts"],
                "max_hold_bars": HORIZON,
                "tp_pct": TP,
                "sl_pct": SL,
                "min_edge": min_edge,
                "leverage": lev,
                "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
                "note": (
                    f"Forward lockbox after research freeze. Both long and short. "
                    f"Green/red boxes = hold win/loss. Showing last {trade_cap} trades."
                ),
            },
            show=True,
        )
    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Forward lockbox report for frozen packs. Sealed unless "
            "--i-accept-lockbox-contamination; Finplot needs --show + --i-accept-finplot-lockbox."
        )
    )
    ap.add_argument("--symbols", default="ETHUSDT,SOLUSDT")
    ap.add_argument("--start", default=FORWARD_LOCKBOX_START)
    ap.add_argument("--trade-cap", type=int, default=DEFAULT_TRADE_CAP)
    ap.add_argument("--store", action="store_true", default=True)
    ap.add_argument(
        "--show",
        action="store_true",
        help="Open Finplot (requires dual contamination accepts).",
    )
    ap.add_argument(
        "--no-show",
        action="store_true",
        help="Deprecated alias: Finplot is off by default.",
    )
    add_lockbox_guard_args(ap)
    args = ap.parse_args(argv)

    syms = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    open_finplot = bool(args.show) and not bool(args.no_show)
    try:
        require_lockbox_access(
            experiment_id="structure_v1_lockbox_plot",
            window_start=str(args.start),
            purpose="finplot_lockbox_open" if open_finplot else "lockbox_report_only",
            symbols=syms,
            accepted_contamination=bool(args.i_accept_lockbox_contamination),
            open_finplot=open_finplot,
            accepted_finplot=bool(args.i_accept_finplot_lockbox),
            notes="scripts/plot_structure_lockbox.py",
        )
    except PolicyError as exc:
        print(f"REFUSED: {exc}", flush=True)
        return 2

    show = seal_finplot_unless_authorized(
        open_finplot=open_finplot,
        accepted_finplot=bool(args.i_accept_finplot_lockbox),
    )
    stamp = run_conformance_check(quiet=True)
    if not stamp.get("passed"):
        print("tradesim conformance not green; refusing lockbox plot")
        return 1

    rows = []
    for sym in syms:
        pack = PACKS.get(sym)
        if pack is None or not (pack / "model.joblib").is_file():
            raise SystemExit(f"missing frozen pack for {sym}: {pack}")
        rows.append(
            _run_one(
                symbol=sym,
                pack_dir=pack,
                start=args.start,
                trade_cap=int(args.trade_cap),
                store=bool(args.store),
                show=show,
            )
        )

    tag = "_".join(s.lower().replace("usdt", "") for s in syms[:4]) or "lockbox"
    out = ARTIFACTS / "reports" / f"structure_v1_lockbox_{tag}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "lockbox_start": args.start,
        "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
        "finplot": show,
        "note": (
            "Authorized lockbox access for "
            + ", ".join(syms)
            + ("; Finplot ON" if show else "; report-only").strip()
            + ". Contaminated for first-look claims; quote settle outer-OOS for promotion."
        ),
        "results": rows,
    }
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
