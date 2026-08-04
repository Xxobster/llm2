"""ETHUSDT structure_v1 lockbox: baseline (1 book) vs concurrent hedge (3 per side).

Each open trade keeps its own take-profit / stop-loss. Contaminated lockbox window —
quote settle outer-OOS for promotion, not these Finplot numbers.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
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
    research_sim_hedge,
)
from tradesim.research.plot import plot_backtest  # noqa: E402

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import (  # noqa: E402
    leverage_from_stop,
    peak_margin_utilization,
    research_costs_baseline,
)
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.models.base import Prediction  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROUND_TRIP_COST, TF_MS, touch_timeframe  # noqa: E402
from llm2.signals.translate import predictions_to_signals  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL = "ETHUSDT"
SPACE = "structure_v1"
HORIZON = 6
TP = 0.01
SL = 0.02
PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_direction"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
OUT = ARTIFACTS / "reports" / "structure_v1_eth_concurrent_lockbox.json"


def _json_default(obj: object) -> object:
    if isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
        return None
    raise TypeError(f"Object of type {type(obj)!r} is not JSON serializable")


def _peak_concurrent(trades: list, *, side: int | None = None) -> int:
    events: list[tuple[int, int]] = []
    for t in trades:
        s = int(getattr(t, "side", 0) or 0)
        if side is not None and s != side:
            continue
        entry = int(getattr(t, "entry_ts_ms", 0) or 0)
        exit_ = int(getattr(t, "exit_ts_ms", entry) or entry)
        events.append((entry, +1))
        events.append((exit_, -1))
    if not events:
        return 0
    events.sort(key=lambda x: (x[0], x[1]))
    cur = peak = 0
    for _, delta in events:
        cur += delta
        peak = max(peak, cur)
    return int(peak)


def _skip_counts(bundle) -> dict[str, int]:
    skips = getattr(bundle.result, "skips", None) or []
    out: dict[str, int] = {}
    for s in skips:
        reason = str(getattr(s, "reason", s))
        out[reason] = out.get(reason, 0) + 1
    return out


def _prepare(start: str):
    strategy = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(PACK / "model.joblib")
    model = blob["model"]
    cols = list(blob["feature_columns"])
    target = str(strategy["target"])
    timeframe = str(strategy["timeframe"])
    family = target_family(target)
    min_edge = float(
        strategy.get("min_edge")
        or (DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST)
    )

    ohlcv = load_ohlcv(SYMBOL, timeframe)
    start_ts = pd.Timestamp(start, tz="UTC")
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")

    feats = build_space(ohlcv.copy(), SPACE, symbol=SYMBOL, timeframe=timeframe)
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    for c in feats.columns:
        if c.startswith("last_retrace_pct_"):
            feats[c] = feats[c].fillna(0.0)
    aligned = feats.dropna()
    lock_mask = aligned.index >= start_ts
    if int(lock_mask.sum()) < 50:
        raise RuntimeError(f"insufficient lockbox bars after {start}")

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
    window = ohlcv.loc[:end_ts]
    window = window.loc[window.index >= (start_ts - pd.Timedelta(days=14))]

    touch_tf = touch_timeframe(timeframe, SYMBOL)
    touch = load_ohlcv(SYMBOL, touch_tf)
    dec_ms = int(TF_MS[timeframe])
    touch_end = end_ts + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[
        (touch.index >= (start_ts - pd.Timedelta(days=14))) & (touch.index <= touch_end)
    ]
    touch_ms = int(TF_MS[touch_tf])
    need = dec_ms // touch_ms
    last_dec = int(window["ts_ms"].iloc[-1])
    t_ts = touch_win["ts_ms"].to_numpy(dtype=np.int64)
    lo = int(np.searchsorted(t_ts, last_dec, side="left"))
    hi = int(np.searchsorted(t_ts, last_dec + dec_ms, side="left"))
    if hi - lo < need:
        window = window.iloc[:-1]
        end_ts = window.index[-1]
        touch_end = end_ts + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[
            (touch.index >= (start_ts - pd.Timedelta(days=14))) & (touch.index <= touch_end)
        ]

    funding = load_funding(SYMBOL)
    if funding.empty:
        raise RuntimeError("no funding — refusing concurrent lockbox without live cost")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))

    lev = leverage_from_stop(SL)
    try:
        instrument = research_instrument(SYMBOL)
    except Exception:  # noqa: BLE001
        instrument = None

    return {
        "target": target,
        "timeframe": timeframe,
        "min_edge": min_edge,
        "start_ts": start_ts,
        "end_ts": end_ts,
        "window": window,
        "signals": signals,
        "touch_win": touch_win,
        "touch_tf": touch_tf,
        "funding_ts": funding_ts[fmask],
        "funding_rt": funding_rt[fmask],
        "lev": lev,
        "instrument": instrument,
        "n_signals": len(signals),
    }


def _run_arm(ctx: dict, *, max_per_side: int, store: bool, label: str):
    if max_per_side <= 1:
        sim = research_sim(max_hold_bars=HORIZON, decision_timeframe=ctx["timeframe"])
        mode = "one_way_single"
    else:
        sim = research_sim_hedge(
            max_hold_bars=HORIZON,
            decision_timeframe=ctx["timeframe"],
            max_positions_per_side=int(max_per_side),
            max_positions_per_symbol=int(max_per_side) * 2,
        )
        mode = f"hedge_{max_per_side}_per_side"

    bundle = run_strategy_backtest(
        ctx["window"],
        ctx["signals"],
        symbol=SYMBOL,
        timeframe=ctx["timeframe"],
        strategy_id=f"llm2-structure_v1-ethusdt-direction-lockbox-{label}",
        touch_ohlcv=ctx["touch_win"],
        touch_timeframe=ctx["touch_tf"],
        costs=research_costs_baseline(),
        margin=research_margin(leverage=ctx["lev"]),
        sizing=research_sizing(),
        sim=sim,
        instrument=ctx["instrument"],
        funding_ts_ms=ctx["funding_ts"],
        funding_rate=ctx["funding_rt"],
        strategy_meta={
            "name": f"{SYMBOL} {ctx['timeframe']} {ctx['target']} {mode}",
            "symbol": SYMBOL,
            "timeframe": ctx["timeframe"],
            "batch": "structure_v1_eth_concurrent",
            "target": ctx["target"],
            "tp_pct": TP,
            "sl_pct": SL,
            "min_edge": ctx["min_edge"],
            "leverage": ctx["lev"],
            "position_mode": mode,
            "max_positions_per_side": max_per_side,
            "min_size_caveat": True,
            "lockbox_start": str(ctx["start_ts"].date()),
            "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
            "note": (
                "Each open trade has its own TP/SL bracket. TP/SL % frozen identical "
                f"({TP:.0%}/{SL:.0%}); concurrency changes stack risk / margin, not per-trade SL."
            ),
        },
        plot=False,
        print_headline=True,
        store_path=str(STORE) if store else None,
    )
    m = bundle.metrics
    start_ms = int(ctx["start_ts"].value // 1_000_000)
    trades = [
        t
        for t in bundle.result.trades
        if int(getattr(t, "entry_ts_ms", 0) or 0) >= start_ms
    ]
    peak_m = peak_margin_utilization(
        trades,
        equity=getattr(bundle.result, "equity", None),
        starting_equity=float(m.starting_equity),
    )
    summary = {
        "label": label,
        "mode": mode,
        "max_positions_per_side": int(max_per_side),
        "leverage": float(ctx["lev"]),
        "tp_pct": TP,
        "sl_pct": SL,
        "n_signals": int(ctx["n_signals"]),
        "n_trades": int(len(trades)),
        "n_trades_engine": int(m.n_trades),
        "n_longs": int(getattr(m, "n_longs", 0) or 0),
        "n_shorts": int(getattr(m, "n_shorts", 0) or 0),
        "net_pnl": float(m.net_pnl),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "total_slippage": float(getattr(m, "total_slippage", float("nan"))),
        "total_funding": float(getattr(m, "total_funding", float("nan"))),
        "max_drawdown": float(getattr(m, "max_drawdown", float("nan"))),
        "sharpe_daily_raw": float(getattr(m, "sharpe_daily_raw", float("nan"))),
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "peak_concurrent_all": _peak_concurrent(trades),
        "peak_concurrent_long": _peak_concurrent(trades, side=1),
        "peak_concurrent_short": _peak_concurrent(trades, side=-1),
        "peak_margin_utilization": float(peak_m),
        "skips": _skip_counts(bundle),
        "warnings": list(getattr(bundle.result, "warnings", []) or []),
        "run_id": getattr(bundle, "run_id", None),
        "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
    }
    return bundle, summary, trades


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=FORWARD_LOCKBOX_START)
    ap.add_argument("--max-per-side", type=int, default=3)
    ap.add_argument("--store", action="store_true", default=True)
    ap.add_argument("--no-show", action="store_true")
    ap.add_argument("--trade-cap", type=int, default=120)
    args = ap.parse_args(argv)

    if os.environ.get("TRADESIM_NO_PLOT") and not args.no_show:
        os.environ.pop("TRADESIM_NO_PLOT", None)

    stamp = run_conformance_check(quiet=True)
    if not stamp.get("passed"):
        print("tradesim conformance not green; refusing")
        return 1
    if not (PACK / "model.joblib").is_file():
        raise SystemExit(f"missing pack {PACK}")

    ctx = _prepare(args.start)
    print("\n=== BASELINE: one position at a time ===", flush=True)
    _, base_sum, _ = _run_arm(ctx, max_per_side=1, store=bool(args.store), label="baseline1")
    print(json.dumps(base_sum, indent=2), flush=True)

    print(f"\n=== CONCURRENT: hedge mode, {args.max_per_side} per side (separate TP/SL) ===", flush=True)
    bundle, conc_sum, _ = _run_arm(
        ctx,
        max_per_side=int(args.max_per_side),
        store=bool(args.store),
        label=f"hedge{args.max_per_side}",
    )
    print(json.dumps(conc_sum, indent=2), flush=True)

    delta = {
        "net_pnl_delta": conc_sum["net_pnl"] - base_sum["net_pnl"],
        "pf_delta": conc_sum["profit_factor"] - base_sum["profit_factor"],
        "n_trades_delta": conc_sum["n_trades"] - base_sum["n_trades"],
        "better_net_pnl": conc_sum["net_pnl"] > base_sum["net_pnl"],
        "better_pf": conc_sum["profit_factor"] > base_sum["profit_factor"],
    }
    payload = {
        "symbol": SYMBOL,
        "lockbox_start": args.start,
        "data_end": str(ctx["end_ts"]),
        "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
        "note": (
            "Contaminated May→now lockbox. Concurrent arm uses Bybit-style hedge mode with "
            f"max_positions_per_side={args.max_per_side}; each trade keeps its own TP/SL. "
            "TP/SL percentages are still frozen identical (1%/2%), so leverage_from_stop is "
            "unchanged at research time — live must still track stacked margin if concurrency "
            "is deployed, and per-position leverage if SL ever differs by trade."
        ),
        "baseline": base_sum,
        "concurrent": conc_sum,
        "delta": delta,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(payload, indent=2, allow_nan=False, default=_json_default) + "\n",
        encoding="utf-8",
    )
    print(f"\nwrote {OUT}", flush=True)
    print(json.dumps({"delta": delta}, indent=2), flush=True)

    if not args.no_show:
        start_ts = ctx["start_ts"]
        bars = ohlcv_to_bar_series(
            ctx["window"].loc[ctx["window"].index >= start_ts],
            symbol=SYMBOL,
            timeframe=ctx["timeframe"],
        )
        m = bundle.metrics
        plot_backtest(
            bars,
            bundle.result,
            title=(
                f"{SYMBOL} 1h | structure_v1 direction LOCKBOX concurrent "
                f"hedge×{args.max_per_side} "
                f"[{start_ts.date()} -> {ctx['end_ts'].date()}] "
                f"BT_PnL={m.net_pnl:.2f} PF={m.profit_factor:.2f} n={m.n_trades} "
                f"peakL={conc_sum['peak_concurrent_long']} peakS={conc_sum['peak_concurrent_short']}"
            ),
            metrics=bundle.metrics,
            trade_style="boxes",
            max_zone_trades=int(args.trade_cap),
            strategy_meta={
                "name": f"{SYMBOL} concurrent hedge×{args.max_per_side}",
                "symbol": SYMBOL,
                "timeframe": ctx["timeframe"],
                "venue_product": "Bybit USDT perpetual",
                "bots": ["llm2-structure-eth"],
                "backtest_net_pnl": float(m.net_pnl),
                "backtest_profit_factor": float(m.profit_factor),
                "backtest_n_trades": int(m.n_trades),
                "max_positions_per_side": int(args.max_per_side),
                "leverage": float(ctx["lev"]),
                "tp_pct": TP,
                "sl_pct": SL,
                "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
                "note": (
                    f"Hedge mode: up to {args.max_per_side} longs + {args.max_per_side} shorts, "
                    "each with own TP/SL. Green/red boxes = hold win/loss."
                ),
            },
            show=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
