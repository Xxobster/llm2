"""Pivot limit: level-vs-wick diagnostics + full metrics + Finplot (pre-lockbox).

Arms:
  1) SOLUSDT next-bar LIMIT TP1%/SL2%  (original diag~347 fills)
  2) ETHUSDT multi-bar work=4 LIMIT TP1%/SL1%  (stack geo)
  3) SOLUSDT multi-bar work=4 LIMIT TP1%/SL1%  (stack geo)

RESEARCH_ONLY. Outer OOS stitched path only; not a promotion.
Finplot: set --show (and dual lockbox flags only if window hits lockbox; this run is cut).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    Side,
    Signal,
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_limit_entry,
)
from tradesim.contracts import EntryOrder  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

TF = "15m"
H_BARS = 4
ATR_MIN = 2.0
MAX_ROWS = 120_000


def _stat(a: np.ndarray) -> dict:
    a = np.asarray(a, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return {
            "n": 0,
            "mean": float("nan"),
            "median": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
            "p10": float("nan"),
            "p90": float("nan"),
            "std": float("nan"),
        }
    return {
        "n": int(a.size),
        "mean": float(np.mean(a)),
        "median": float(np.median(a)),
        "min": float(np.min(a)),
        "max": float(np.max(a)),
        "p10": float(np.percentile(a, 10)),
        "p90": float(np.percentile(a, 90)),
        "std": float(np.std(a)),
    }


def wick_level_report(
    ohlcv: pd.DataFrame,
    *,
    decision_ts_ms: np.ndarray,
    limit_prices: np.ndarray,
    is_short: np.ndarray,
    y_level_ret: np.ndarray | None,
    close: np.ndarray,
    work_bars: int,
) -> dict:
    """Compare predicted limit vs path wicks and vs true pivot return (when known).

    definitions (as fraction of decision close):
    - signed_to_extremum: for SHORT, (window_max_high - limit)/close
                          for LONG,  (limit - window_min_low)/close
      >0 means path traded through the limit (touch possible / went further)
      <0 means extreme never reached the limit (miss fill)
    - abs_to_extremum: absolute of that gap
    - pred_vs_true_level: |pred_level_ret - true_level_ret| when true event exists
    """
    bar_ts = index_to_ms(ohlcv.index)
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    n_bars = len(bar_ts)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}

    signed = []
    abs_gap = []
    touch = []
    miss_bps = []  # how far short of limit when no touch (bps of price)
    overshoot_bps = []  # how far beyond limit when touch
    vs_true = []
    wrong_sign_true = 0
    n_true = 0

    for j in range(len(decision_ts_ms)):
        i_dec = pos.get(int(decision_ts_ms[j]))
        if i_dec is None:
            continue
        i0 = i_dec + 1
        i1 = min(n_bars, i0 + int(work_bars))
        if i0 >= n_bars:
            continue
        lim = float(limit_prices[j])
        c = float(close[j])
        if not np.isfinite(lim) or lim <= 0 or not np.isfinite(c) or c <= 0:
            continue
        wh = float(np.max(high[i0:i1])) if i1 > i0 else float("nan")
        wl = float(np.min(low[i0:i1])) if i1 > i0 else float("nan")
        if is_short[j]:
            # rest above: gap = how much high sits relative to limit
            s = (wh - lim) / c
            t = wh >= lim
            if t:
                overshoot_bps.append(10000.0 * (wh - lim) / c)
            else:
                miss_bps.append(10000.0 * (lim - wh) / c)
        else:
            s = (lim - wl) / c
            t = wl <= lim
            if t:
                overshoot_bps.append(10000.0 * (lim - wl) / c)
            else:
                miss_bps.append(10000.0 * (wl - lim) / c)
        signed.append(s)
        abs_gap.append(abs(s))
        touch.append(float(t))

        if y_level_ret is not None and np.isfinite(y_level_ret[j]):
            n_true += 1
            pred_lr = lim / c - 1.0
            true_lr = float(y_level_ret[j])
            vs_true.append(abs(pred_lr - true_lr))
            # wrong side of decision: pred high (short) but true was low, etc.
            if is_short[j] and true_lr < 0:
                wrong_sign_true += 1
            if (not is_short[j]) and true_lr > 0:
                wrong_sign_true += 1

    touch_arr = np.asarray(touch, dtype=float)
    return {
        "work_bars": int(work_bars),
        "n_decisions": int(len(signed)),
        "touch_rate": float(np.mean(touch_arr)) if touch_arr.size else float("nan"),
        "signed_gap_to_extremum_frac": _stat(np.asarray(signed)),
        "abs_gap_to_extremum_frac": _stat(np.asarray(abs_gap)),
        "miss_distance_bps_when_no_touch": _stat(np.asarray(miss_bps)),
        "overshoot_bps_when_touch": _stat(np.asarray(overshoot_bps)),
        "abs_pred_vs_true_level_frac": _stat(np.asarray(vs_true)),
        "frac_wrong_side_among_true_events": (
            float(wrong_sign_true / n_true) if n_true else float("nan")
        ),
        "n_true_events_in_set": n_true,
        "pct_abs_gap_gt_50bps": float(np.mean(np.asarray(abs_gap) > 0.005))
        if abs_gap
        else float("nan"),
        "pct_abs_gap_gt_100bps": float(np.mean(np.asarray(abs_gap) > 0.01))
        if abs_gap
        else float("nan"),
        "pct_abs_gap_gt_200bps": float(np.mean(np.asarray(abs_gap) > 0.02))
        if abs_gap
        else float("nan"),
        "legend": {
            "signed_gap": (
                "SHORT: (window_max_high - limit)/close; LONG: (limit - window_min_low)/close. "
                "Positive => wick went to/through the rest price."
            ),
            "bps": "1 basis point = 0.01% of price",
        },
    }


def _full_metrics(bundle) -> dict:
    m = bundle.metrics
    keys = [
        "n_trades",
        "profit_factor",
        "net_pnl",
        "win_rate",
        "expectancy",
        "n_liquidations",
        "gross_profit",
        "gross_loss",
        "avg_win",
        "avg_loss",
        "payoff",
        "max_drawdown",
        "sharpe",
        "sortino",
        "exposure",
        "fees",
        "funding_pnl",
        "slippage",
        "trades_per_day",
    ]
    out = {}
    for k in keys:
        if hasattr(m, k):
            try:
                out[k] = float(getattr(m, k)) if not isinstance(getattr(m, k), int) else int(
                    getattr(m, k)
                )
            except (TypeError, ValueError):
                out[k] = getattr(m, k)
    # catch-all public attrs that look numeric
    for k in dir(m):
        if k.startswith("_"):
            continue
        if k in out:
            continue
        try:
            v = getattr(m, k)
        except Exception:  # noqa: BLE001
            continue
        if isinstance(v, (int, float, np.floating, np.integer)) and not isinstance(v, bool):
            out[k] = float(v) if not isinstance(v, (int, np.integer)) else int(v)
    return out


def _bt(symbol, ohlcv, signals, *, sl, tag, max_hold, plot, store_path):
    if len(signals) < 10:
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
    pad = 80
    window = ohlcv.iloc[max(0, i0 - pad) : min(len(ohlcv), i1 + pad)]
    w_ts = index_to_ms(window.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    dec_ms = int(TF_MS[TF])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    lev = float(leverage_from_stop(sl))
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=TF,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(
            max_hold_bars=max_hold, decision_timeframe=TF
        ),
        instrument=research_instrument(symbol),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=plot,
        print_headline=True,
        store_path=store_path,
    )
    return bundle, {
        "status": "RAN",
        "n_signals": len(signals),
        "metrics": _full_metrics(bundle),
    }


def _gated(scored):
    mask = gate_mask(scored, mode="p75", tp=0.01, sl=0.01)
    ts, is_short, lim = limit_price_side(scored, mask)
    idx = np.flatnonzero(mask)
    return mask, ts, is_short, lim, idx


def run_arm(
    scored,
    *,
    arm_id: str,
    tp: float,
    sl: float,
    mode: str,
    work_bars: int,
    max_hold: int,
    plot: bool,
    out_dir: Path,
):
    mask, ts, is_short, lim, idx = _gated(scored)
    close = scored.close[idx]
    y_lv = scored.y_level[idx]
    wick = wick_level_report(
        scored.ohlcv,
        decision_ts_ms=ts,
        limit_prices=lim,
        is_short=is_short,
        y_level_ret=y_lv,
        close=close,
        work_bars=work_bars if mode == "work" else 1,
    )
    if mode == "next_bar":
        sigs = []
        for j in range(len(ts)):
            sigs.append(
                Signal(
                    ts_ms=int(ts[j]),
                    side=Side.SHORT if is_short[j] else Side.LONG,
                    stop_offset=float(sl),
                    target_offset=float(tp),
                    max_hold_bars=int(max_hold),
                    entry_order=EntryOrder.LIMIT,
                    limit_price=float(lim[j]),
                    tag=arm_id,
                )
            )
        fill_stats = {
            "mode": "next_bar_tradesim_native",
            "n_intent": len(sigs),
            "note": "tradesim fills only if next bar touches; ~12-20% fill historically",
        }
    else:
        intents = [
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if is_short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=float(sl),
                target_offset=float(tp),
                max_hold_bars=int(max_hold),
            )
            for j in range(len(ts))
        ]
        sigs, fill_stats = materialize_working_limits(
            scored.ohlcv, intents, work_bars=work_bars
        )
        fill_stats = dict(fill_stats)
        fill_stats["mode"] = "multi_bar_work"
    store = str(out_dir / f"{arm_id}_report")
    print(
        f"\n=== {arm_id} {scored.symbol} TP={tp} SL={sl} mode={mode} "
        f"n_intent={len(ts)} n_path_sigs={len(sigs)} plot={plot} ===",
        flush=True,
    )
    _, res = _bt(
        scored.symbol,
        scored.ohlcv,
        sigs,
        sl=sl,
        tag=arm_id,
        max_hold=max_hold,
        plot=plot,
        store_path=store,
    )
    return {
        "arm_id": arm_id,
        "symbol": scored.symbol,
        "tp": tp,
        "sl": sl,
        "mode": mode,
        "work_bars": work_bars,
        "n_intent": int(len(ts)),
        "fill_stats": fill_stats,
        "wick_vs_level": wick,
        "backtest": res,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--show",
        action="store_true",
        help="Open Finplot windows (blocks until closed). Default: report-only.",
    )
    args = ap.parse_args()
    if args.show:
        os.environ.pop("TRADESIM_NO_PLOT", None)
    else:
        os.environ["TRADESIM_NO_PLOT"] = "1"

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "pivot_forecast" / f"finplot_diag_{stamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Scoring SOLUSDT…", flush=True)
    sol = score_symbol_oos(
        "SOLUSDT", timeframe=TF, horizon_bars=H_BARS, atr_min=ATR_MIN, max_rows=MAX_ROWS
    )
    print("Scoring ETHUSDT…", flush=True)
    eth = score_symbol_oos(
        "ETHUSDT", timeframe=TF, horizon_bars=H_BARS, atr_min=ATR_MIN, max_rows=MAX_ROWS
    )

    arms = [
        run_arm(
            sol,
            arm_id="SOL_nextbar_tp1_sl2",
            tp=0.01,
            sl=0.02,
            mode="next_bar",
            work_bars=1,
            max_hold=6,
            plot=bool(args.show),
            out_dir=out_dir,
        ),
        run_arm(
            eth,
            arm_id="ETH_work4_tp1_sl1",
            tp=0.01,
            sl=0.01,
            mode="work",
            work_bars=4,
            max_hold=6,
            plot=bool(args.show),
            out_dir=out_dir,
        ),
        run_arm(
            sol,
            arm_id="SOL_work4_tp1_sl1",
            tp=0.01,
            sl=0.01,
            mode="work",
            work_bars=4,
            max_hold=6,
            plot=bool(args.show),
            out_dir=out_dir,
        ),
    ]

    report = {
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "arms": arms,
        "arms_table_from_stack_reminder": (
            "See strategy_stack_latest.md for full multi-arm counts"
        ),
    }
    path = out_dir / "summary.json"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    md = _markdown(report)
    (out_dir / "summary.md").write_text(md, encoding="utf-8")
    latest = ARTIFACTS / "reports" / "pivot_forecast" / "finplot_diag_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"\nWROTE {path}", flush=True)
    try:
        print(md, flush=True)
    except UnicodeEncodeError:
        print("(summary on disk)", flush=True)
    return 0


def _fmt_stat(s: dict, pct: bool = False) -> str:
    if not s or s.get("n", 0) == 0:
        return "n/a"
    scale = 100.0 if pct else 1.0
    unit = "%" if pct else ""

    def f(x):
        return f"{scale * float(x):.3f}{unit}"

    return (
        f"n={s['n']} mean={f(s['mean'])} med={f(s['median'])} "
        f"min={f(s['min'])} max={f(s['max'])} p90={f(s['p90'])}"
    )


def _markdown(report: dict) -> str:
    lines = [
        f"# Pivot finplot / wick / metrics (`{report['stamp']}`)",
        "",
        f"**{report['readiness_max']}**",
        "",
    ]
    for a in report["arms"]:
        lines.append(f"## {a['arm_id']}")
        lines.append("")
        m = (a.get("backtest") or {}).get("metrics") or {}
        lines.append(
            f"- mode={a['mode']} TP={100*a['tp']:.0f}% SL={100*a['sl']:.0f}% "
            f"intent={a['n_intent']} path_fill~{a.get('fill_stats', {}).get('n_filled_path', 'n/a')}"
        )
        if m:
            lines.append(
                f"- trades={m.get('n_trades')} WR={m.get('win_rate')} "
                f"PF={m.get('profit_factor')} pnl={m.get('net_pnl')} "
                f"exp={m.get('expectancy')} liq={m.get('n_liquidations')}"
            )
        w = a["wick_vs_level"]
        lines.append(f"- touch_rate @ work={w['work_bars']}: {w.get('touch_rate')}")
        lines.append(
            f"- abs gap pred→extremum (frac): {_fmt_stat(w['abs_gap_to_extremum_frac'], pct=True)}"
        )
        lines.append(
            f"- miss when no touch (bps): {_fmt_stat(w['miss_distance_bps_when_no_touch'])}"
        )
        lines.append(
            f"- overshoot when touch (bps): {_fmt_stat(w['overshoot_bps_when_touch'])}"
        )
        lines.append(
            f"- |pred vs true level| (frac, events): "
            f"{_fmt_stat(w['abs_pred_vs_true_level_frac'], pct=True)}"
        )
        lines.append(
            f"- wrong side among true events: {w.get('frac_wrong_side_among_true_events')}"
        )
        lines.append(
            f"- share |gap|>50/100/200 bps: "
            f"{w.get('pct_abs_gap_gt_50bps')}/{w.get('pct_abs_gap_gt_100bps')}/"
            f"{w.get('pct_abs_gap_gt_200bps')}"
        )
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
