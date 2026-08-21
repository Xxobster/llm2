"""Full pivot strategy research stack (RESEARCH_ONLY).

Preregistered before outer path re-use (generation pivot_strategy_stack_001):
1) Level-economy suite on walk-forward OOS scores
2) Favorable geometry LIMIT arms (TP>=SL families) + asymmetric SL
3) Working-time cancel (multi-bar rest via materialize)
4) Composed gates: cal p75, π*, π* + level band
5) Intent-all vs fill-path trade counts (no structure-direction nest)

Does NOT promote readiness. Pre-lockbox Binance 15m.
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
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
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.strategy.ev import net_bracket_magnitudes  # noqa: E402
from llm2.pivot.strategy.level_economy import (  # noqa: E402
    level_error_stats,
    touch_diagnostics,
)
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    ScoredOOS,
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TF = "15m"
H_BARS = 4
ATR_MIN = 2.0
MAX_ROWS = 120_000
GENERATION = "pivot_strategy_stack_001"


@dataclass(frozen=True)
class Arm:
    """Preregistered executable arm — do not reorder by OOS performance after view."""

    id: str
    tp: float
    sl: float | None  # None → asymmetric from train level P90
    work_bars: int
    max_hold_bars: int
    gate: str  # p75 | pi_star | pi_star_level
    entry: str  # limit_work | market
    note: str = ""


# Fixed preregistered set (geometry + time + gate + market control).
ARMS: tuple[Arm, ...] = (
    Arm("geo_tp2_sl1_p75_w4", 0.02, 0.01, 4, 6, "p75", "limit_work", "2:1 favorable"),
    Arm("geo_tp3_sl1p5_p75_w4", 0.03, 0.015, 4, 6, "p75", "limit_work", "2:1 favorable"),
    Arm("geo_tp3_sl2_p75_w4", 0.03, 0.02, 4, 6, "p75", "limit_work", "1.5:1 favorable"),
    Arm("geo_tp2_sl2_p75_w4", 0.02, 0.02, 4, 6, "p75", "limit_work", "1:1 reference"),
    Arm("geo_tp1_sl1_p75_w4", 0.01, 0.01, 4, 6, "p75", "limit_work", "flat prior diag"),
    Arm("asym_tp2_sl_p90_p75_w4", 0.02, None, 4, 6, "p75", "limit_work", "SL=clip(1.25*train P90,0.75%,2%)"),
    Arm("geo_tp2_sl1_pi_w4", 0.02, 0.01, 4, 6, "pi_star", "limit_work", "EV π* gate"),
    Arm("geo_tp2_sl1_pi_lvl_w4", 0.02, 0.01, 4, 6, "pi_star_level", "limit_work", "π*+level band"),
    # Time limit sensitivity on main favorable geometry
    Arm("geo_tp2_sl1_p75_w2", 0.02, 0.01, 2, 4, "p75", "limit_work", "work=2 cancel"),
    Arm("geo_tp2_sl1_p75_w6", 0.02, 0.01, 6, 8, "p75", "limit_work", "work=6 cancel"),
    Arm("geo_tp2_sl1_p75_w8", 0.02, 0.01, 8, 10, "p75", "limit_work", "work=8 cancel"),
    # Market control (should lose per prior diag)
    Arm("mkt_tp2_sl1_p75", 0.02, 0.01, 0, 6, "p75", "market", "market control 2:1"),
)


def _metrics(bundle) -> dict:
    m = bundle.metrics
    return {
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "net_pnl": float(m.net_pnl),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
    }


def _bt(symbol: str, ohlcv: pd.DataFrame, signals: list[Signal], *, sl: float, tag: str):
    if len(signals) < 15:
        return {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(TF, symbol)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    from llm2.data.loader import load_ohlcv

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
    try:
        bundle = run_strategy_backtest(
            window,
            signals,
            symbol=symbol,
            timeframe=TF,
            strategy_id=f"pivot_stack_{symbol.lower()}_{tag}",
            touch_ohlcv=touch_win if len(touch_win) else None,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_limit_entry(
                max_hold_bars=max(int(s.max_hold_bars or 6) for s in signals),
                decision_timeframe=TF,
            ),
            instrument=research_instrument(symbol),
            funding_ts_ms=f_ts[fmask],
            funding_rate=f_rt[fmask],
            plot=False,
            print_headline=False,
            store_path=None,
        )
    except Exception as exc:  # noqa: BLE001
        return {
            "status": "BT_ERROR",
            "error": str(exc)[:400],
            "n_signals": len(signals),
        }
    return {"status": "RAN", "metrics": _metrics(bundle), "n_signals": len(signals)}


def _resolve_sl(arm: Arm, scored: ScoredOOS, mask: np.ndarray) -> float:
    if arm.sl is not None:
        return float(arm.sl)
    # Asymmetric: median train P90 among gated rows, clipped
    p90 = scored.level_p90_train[mask]
    p90 = p90[np.isfinite(p90)]
    raw = float(np.median(p90) * 1.25) if p90.size else 0.012
    return float(np.clip(raw, 0.0075, 0.02))


def _run_arm(scored: ScoredOOS, arm: Arm) -> dict:
    br = net_bracket_magnitudes(
        arm.tp, arm.sl if arm.sl is not None else 0.01
    )  # provisional π* for gate if fixed; asym uses 1% proxy in π until resolved
    # For asym gate we recompute after sl resolve using full mask with provisional sl
    pi = br.pi_star
    mask = gate_mask(
        scored, mode=arm.gate, tp=arm.tp, sl=arm.sl or 0.01, pi_star=pi
    )
    if not mask.any():
        return {
            "arm": arm.id,
            "status": "NO_SIGNALS",
            "n_intent": 0,
            **asdict(arm),
        }
    sl = _resolve_sl(arm, scored, mask)
    if arm.sl is None:
        # re-gate with actual π* for asym SL
        br = net_bracket_magnitudes(arm.tp, sl)
        pi = br.pi_star
        if arm.gate != "p75":
            mask = gate_mask(
                scored, mode=arm.gate, tp=arm.tp, sl=sl, pi_star=pi
            )
    if not mask.any():
        return {
            "arm": arm.id,
            "status": "NO_SIGNALS",
            "n_intent": 0,
            "tp": arm.tp,
            "sl": sl,
            "pi_star": pi,
        }

    ts, is_short, lim = limit_price_side(scored, mask)
    n_intent = int(len(ts))
    out: dict = {
        "arm": arm.id,
        "tp": arm.tp,
        "sl": sl,
        "work_bars": arm.work_bars,
        "max_hold_bars": arm.max_hold_bars,
        "gate": arm.gate,
        "entry": arm.entry,
        "note": arm.note,
        "pi_star": pi,
        "mu_plus": br.mu_plus,
        "mu_minus": br.mu_minus,
        "n_intent": n_intent,
    }

    if arm.entry == "market":
        sigs: list[Signal] = []
        for j in range(n_intent):
            sigs.append(
                Signal(
                    ts_ms=int(ts[j]),
                    side=Side.SHORT if is_short[j] else Side.LONG,
                    stop_offset=float(sl),
                    target_offset=float(arm.tp),
                    max_hold_bars=int(arm.max_hold_bars),
                    tag="pivot_stack_mkt",
                )
            )
        out["fill_stats"] = {
            "n_intent": n_intent,
            "n_filled_path": n_intent,
            "fill_rate": 1.0,
        }
        print(
            f"  BT {arm.id} mkt n_intent={n_intent} sl={sl:.4f} …",
            flush=True,
        )
        res = _bt(scored.symbol, scored.ohlcv, sigs, sl=sl, tag=arm.id)
        out.update(res)
        print(f"    {_short(res)}", flush=True)
        return out

    # Working multi-bar limit
    intents: list[LimitIntent] = []
    for j in range(n_intent):
        intents.append(
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if is_short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=float(sl),
                target_offset=float(arm.tp),
                max_hold_bars=int(arm.max_hold_bars),
                meta={"p_gate": arm.gate},
            )
        )
    sigs, fill_stats = materialize_working_limits(
        scored.ohlcv, intents, work_bars=int(arm.work_bars)
    )
    out["fill_stats"] = fill_stats
    print(
        f"  BT {arm.id} limit work={arm.work_bars} intent={n_intent} "
        f"path_fill={fill_stats['n_filled_path']} sl={sl:.4f} …",
        flush=True,
    )
    res = _bt(scored.symbol, scored.ohlcv, sigs, sl=sl, tag=arm.id)
    out.update(res)
    # Intent-all expectancy: net_pnl / n_intent (fill-or-skip)
    if res.get("status") == "RAN" and n_intent > 0:
        out["expectancy_intent_all"] = float(res["metrics"]["net_pnl"]) / n_intent
        out["expectancy_fill_only"] = float(res["metrics"]["expectancy"])
    print(f"    {_short(res)}", flush=True)
    return out


def _short(res: dict) -> str:
    if res.get("status") != "RAN":
        return str(res.get("error") or res.get("status"))
    m = res["metrics"]
    return (
        f"n={m['n_trades']} PF={m['profit_factor']:.3f} "
        f"WR={m['win_rate']:.3f} pnl={m['net_pnl']:.2f}"
    )


def _level_block(scored: ScoredOOS) -> dict:
    # Event-conditioned level errors
    m_ev = np.isfinite(scored.y_level) & np.isfinite(scored.level_ret)
    lev = level_error_stats(
        y_level_ret=scored.y_level[m_ev],
        pred_level_ret=scored.level_ret[m_ev],
        atr_frac=scored.atr_frac[m_ev],
    )
    # High-confidence decisions (p75 gate) for touch diag
    mask = gate_mask(scored, mode="p75", tp=0.02, sl=0.01)
    if mask.any():
        ts, is_short, lim = limit_price_side(scored, mask)
        # true side on events among gated
        idx = np.flatnonzero(mask)
        y_high = scored.y_high[idx]
        touch = touch_diagnostics(
            ohlcv=scored.ohlcv,
            decision_ts_ms=ts,
            limit_prices=lim,
            is_short=is_short,
            work_bars=H_BARS,
            true_side_high=y_high,
        )
    else:
        touch = {"n": 0}
    # Outer ECE average
    eces = [f["ece_outer_cal"] for f in scored.ece_folds if np.isfinite(f["ece_outer_cal"])]
    return {
        "level_error_events": lev,
        "touch_p75_work4": touch,
        "mean_outer_ece_any": float(np.mean(eces)) if eces else float("nan"),
        "frac_any_label": scored.frac_any,
        "n_scored": scored.n_rows,
    }


def run_symbol(symbol: str) -> dict:
    print(f"SCORE {symbol} …", flush=True)
    scored = score_symbol_oos(
        symbol,
        timeframe=TF,
        horizon_bars=H_BARS,
        atr_min=ATR_MIN,
        max_rows=MAX_ROWS,
    )
    level = _level_block(scored)
    print(
        f"  level MAE%={level['level_error_events'].get('mae_pct')} "
        f"touch={level['touch_p75_work4'].get('touch_rate')} "
        f"ECE={level['mean_outer_ece_any']}",
        flush=True,
    )
    arm_rows = []
    for arm in ARMS:
        arm_rows.append(_run_arm(scored, arm))
    return {
        "symbol": symbol,
        "level_economy": level,
        "arms": arm_rows,
        "ece_folds": scored.ece_folds,
    }


def _md(report: dict) -> str:
    lines = [
        f"# Pivot strategy stack (`{report['stamp']}`)",
        "",
        f"Generation: `{report['generation_id']}` | **{report['readiness_max']}**",
        "",
        "Preregistered arms (not post-hoc selected).",
        "",
    ]
    for sym in report["symbols"]:
        lines.append(f"## {sym['symbol']}")
        le = sym["level_economy"]
        lev = le["level_error_events"]
        t = le["touch_p75_work4"]
        lines.append("")
        lines.append("### Level economy (OOS)")
        lines.append(
            f"- MAE level %: {lev.get('mae_pct')} | P90: {lev.get('p90_abs_pct')} | "
            f"corr: {lev.get('corr')} | MAE/ATR: {lev.get('mae_atr')}"
        )
        lines.append(
            f"- Touch rate (p75, work=4): {t.get('touch_rate')} | "
            f"wrong-side: {t.get('wrong_side_touch_rate')} | "
            f"side acc on events: {t.get('side_accuracy_on_events')}"
        )
        lines.append(f"- Mean outer ECE (any): {le.get('mean_outer_ece_any')}")
        lines.append("")
        lines.append("### Arms (LIMIT work unless market)")
        lines.append(
            "| arm | TP | SL | work | gate | n_intent | fill% | n_tr | WR | PF | "
            "exp_fill | exp_intent | pnl |"
        )
        lines.append("|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for a in sym["arms"]:
            fs = a.get("fill_stats") or {}
            fill = fs.get("fill_rate", float("nan"))
            if a.get("status") != "RAN":
                lines.append(
                    f"| {a.get('arm')} | {a.get('tp')} | {a.get('sl')} | "
                    f"{a.get('work_bars')} | {a.get('gate')} | {a.get('n_intent')} | "
                    f"— | — | — | {a.get('status')} | — | — | — |"
                )
                continue
            m = a["metrics"]
            lines.append(
                f"| {a['arm']} | {100*a['tp']:.1f}% | {100*a['sl']:.2f}% | "
                f"{a['work_bars']} | {a['gate']} | {a['n_intent']} | "
                f"{100*fill:.1f}% | {m['n_trades']} | {m['win_rate']:.3f} | "
                f"{m['profit_factor']:.3f} | {m['expectancy']:.4f} | "
                f"{a.get('expectancy_intent_all', float('nan')):.5f} | "
                f"{m['net_pnl']:.2f} |"
            )
        lines.append("")
    lines.append(
        "Notes: fill% is path-touch within work_bars (intent); n_tr is engine-filled "
        "trades after sim rules. RESEARCH_ONLY — not V2.1 promotion."
    )
    return "\n".join(lines)


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(f"PIVOT_STRATEGY_STACK start {stamp}", tier=0)
    print(f"pivot strategy stack {GENERATION} stamp={stamp}", flush=True)
    # document π* geometry table once
    pi_table = {
        f"tp{int(100*tp)}_sl{int(100*sl)}": net_bracket_magnitudes(tp, sl)._asdict()
        for tp, sl in ((0.02, 0.01), (0.03, 0.015), (0.03, 0.02), (0.02, 0.02), (0.01, 0.01))
    }
    rows = [run_symbol(s) for s in SYMBOLS]
    report = {
        "generation_id": GENERATION,
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "source": "binance",
        "lockbox_start": FORWARD_LOCKBOX_START,
        "setup": {
            "timeframe": TF,
            "horizon_bars": H_BARS,
            "atr_min": ATR_MIN,
            "working_limit": "multi_bar first-touch materialize into tradesim LIMIT",
            "no_structure_direction_nest": True,
            "d060_closed": True,
        },
        "preregistered_arms": [asdict(a) for a in ARMS],
        "break_even_table_maker_entry_taker_exit": pi_table,
        "symbols": rows,
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"strategy_stack_{stamp}.json"
    latest = out_dir / "strategy_stack_latest.json"
    md_path = out_dir / f"strategy_stack_{stamp}.md"
    text = json.dumps(report, indent=2, default=str)
    path.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    md = _md(report)
    md_path.write_text(md, encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    print(f"WROTE {md_path}", flush=True)
    try:
        print(md, flush=True)
    except UnicodeEncodeError:
        print("(markdown summary on disk; console encoding limited)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
