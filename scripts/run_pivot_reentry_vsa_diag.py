"""Pivot timing: VSA-proxy pack MAE + one-shot LIMIT re-entry after stop-loss.

Preregistered RESEARCH_ONLY arms (SOL 15m TP1/SL1 work=4, cal P75):
  1) baseline LIMIT
  2) baseline + at most one re-limit after SL (same side; limit refreshed toward
     decision close by train median miss, rest work=2)
  3) pack MAE: price_vol_mom vs level_focus vs vsa_proxy vs level_vsa

Leakage audit on packs before scoring. No market paths. Not promotion.
"""

from __future__ import annotations

import json
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

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

from tradesim import Side, research_instrument, research_margin, research_sizing  # noqa: E402
from tradesim import research_sim_limit_entry  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.features.packs import build_feature_frame  # noqa: E402
from llm2.pivot.strategy.level_economy import level_error_stats  # noqa: E402
from llm2.pivot.strategy.limit_placement import (  # noqa: E402
    estimate_miss_overshoot_bps,
    limit_price_from_return,
    pull_toward_market_lr,
)
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL = "SOLUSDT"
TF = "15m"
H = 4
TP = 0.01
SL = 0.01
WORK = 4
PACK_TRADE = "level_focus"
PACKS_MAE = ("price_vol_mom", "level_focus", "vsa_proxy", "level_vsa")
MAX_ROWS = 120_000


def _leakage(pack: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = load_ohlcv(SYMBOL, TF)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-8000:].copy()

        def _b(df, **_k):
            return build_feature_frame(df, pack=pack)

        rep = run_leakage_audit(
            ohlcv=ohlcv,
            build_features=_b,
            interval=TF,
            symbol=SYMBOL,
            timeframe=TF,
        )
        require_clean_audit(rep)
        return {"pack": pack, "status": "PASS", "summary": str(rep)[:300]}
    except Exception as exc:  # noqa: BLE001
        return {"pack": pack, "status": "FAIL", "error": str(exc)[:500]}


def _metrics(bundle) -> dict:
    m = bundle.metrics
    out = {
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "net_pnl": float(m.net_pnl),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
    }
    result = getattr(bundle, "result", None)
    trades = getattr(result, "trades", None) if result is not None else None
    if trades is not None and len(trades):
        holds = []
        reasons = []
        for t in trades:
            h = getattr(t, "hold_bars", None)
            if h is not None:
                holds.append(float(h))
            reasons.append(str(getattr(t, "exit_reason", "") or "").lower())
        if holds:
            out["entry_bar_exit_rate"] = float(np.mean(np.asarray(holds) <= 0))
        out["n_stop"] = int(sum("stop" in r for r in reasons))
        out["n_target"] = int(sum("target" in r or r == "tp" for r in reasons))
        out["n_max_hold"] = int(sum("hold" in r or "max_hold" in r for r in reasons))
    return out


def _bt(ohlcv, signals, *, tag: str, max_hold: int):
    if len(signals) < 10:
        return None, {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(TF, SYMBOL)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    touch = load_ohlcv(SYMBOL, touch_tf)
    touch = touch.loc[touch.index < lock]
    funding = load_funding(SYMBOL)
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
    lev = float(leverage_from_stop(SL))
    try:
        bundle = run_strategy_backtest(
            window,
            signals,
            symbol=SYMBOL,
            timeframe=TF,
            strategy_id=tag,
            touch_ohlcv=touch_win if len(touch_win) else None,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=TF),
            instrument=research_instrument(SYMBOL),
            funding_ts_ms=f_ts[fmask],
            funding_rate=f_rt[fmask],
            plot=False,
            print_headline=False,
            store_path=None,
        )
    except Exception as exc:  # noqa: BLE001
        return None, {"status": "BT_ERROR", "error": str(exc)[:400]}
    return bundle, {"status": "RAN", "metrics": _metrics(bundle), "n_signals": len(signals)}


def _primary_intents(scored):
    mask = gate_mask(scored, mode="p75", tp=TP, sl=SL)
    ts, is_short, lim = limit_price_side(scored, mask)
    intents = []
    for j in range(len(ts)):
        intents.append(
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if is_short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=SL,
                target_offset=TP,
                max_hold_bars=H + 2,
                work_bars=WORK,
                meta={"leg": "primary", "j": j},
            )
        )
    return intents, mask, ts, is_short, lim


def _train_miss_bps(scored, mask, work_bars=4) -> float:
    idx = np.flatnonzero(mask)
    if idx.size < 80:
        return 50.0
    cut = max(40, int(0.7 * idx.size))
    tr = idx[:cut]
    ts = scored.ts_ms[tr]
    close = scored.close[tr]
    short = scored.p_high[tr] >= 0.5
    lr = scored.level_ret[tr]
    lim = np.empty(len(tr))
    for j in range(len(tr)):
        x = float(lr[j]) if np.isfinite(lr[j]) else (0.005 if short[j] else -0.005)
        x = float(np.clip(x, -0.03, 0.03))
        lim[j] = limit_price_from_return(float(close[j]), x)
    bar_ts = index_to_ms(scored.ohlcv.index)
    high = scored.ohlcv["high"].to_numpy(dtype=float)
    low = scored.ohlcv["low"].to_numpy(dtype=float)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
    n = len(bar_ts)
    ext = np.full(len(tr), np.nan)
    touch = np.zeros(len(tr), dtype=bool)
    for j, t in enumerate(ts):
        i = pos.get(int(t))
        if i is None:
            continue
        i0, i1 = i + 1, min(n, i + 1 + work_bars)
        if i0 >= i1:
            continue
        if short[j]:
            ext[j] = float(np.max(high[i0:i1]))
            touch[j] = ext[j] >= lim[j]
        else:
            ext[j] = float(np.min(low[i0:i1]))
            touch[j] = ext[j] <= lim[j]
    med_m, med_o, net = estimate_miss_overshoot_bps(
        closes=close, limits=lim, is_short=short, touched=touch, window_ext=ext
    )
    return float(max(net, med_m * 0.5, 0.0))


def _reentry_intents(bundle, *, pull_bps: float, work_bars: int = 2):
    """After each stop exit, one new LIMIT: same side, limit pulled toward market."""
    out = []
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    for t in trades:
        reason = str(getattr(t, "exit_reason", "") or "").lower()
        if "stop" not in reason:
            continue
        side = Side.SHORT if int(getattr(t, "side", 0)) < 0 else Side.LONG
        entry = float(getattr(t, "entry_price", float("nan")))
        exit_px = float(getattr(t, "exit_price", float("nan")))
        exit_ts = int(getattr(t, "exit_ts_ms", 0))
        if not (np.isfinite(entry) and entry > 0 and exit_ts > 0):
            continue
        # Pull original entry limit toward market by train miss (compensate slight miss).
        is_short = side == Side.SHORT
        # express entry as return vs exit close proxy: use entry as limit anchor
        # New limit: between stop exit and original entry (favor fillability).
        if is_short:
            # short was filled high then stopped up further; re-rest slightly below prior entry
            lr_raw = 0.0  # relative to exit — rebuild absolute
            lim = entry * (1.0 - pull_bps / 1e4)
            # keep limit above exit if possible (still a short rest above market)
            lim = max(lim, exit_px * 1.0015) if np.isfinite(exit_px) else lim
        else:
            lim = entry * (1.0 + pull_bps / 1e4)
            lim = min(lim, exit_px * 0.9985) if np.isfinite(exit_px) else lim
        out.append(
            LimitIntent(
                decision_ts_ms=exit_ts,
                side=side,
                limit_price=float(lim),
                stop_offset=SL,
                target_offset=TP,
                max_hold_bars=H + 2,
                work_bars=work_bars,
                meta={"leg": "reentry_after_sl", "parent_entry": entry},
            )
        )
    return out


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(f"PIVOT_REENTRY_VSA start {stamp}", tier=0)
    print(f"pivot reentry/vsa diag stamp={stamp}", flush=True)

    leak = [_leakage(p) for p in PACKS_MAE]
    for x in leak:
        print(f"  leakage {x['pack']}: {x['status']}", flush=True)
        if x["status"] != "PASS":
            print(f"    {x.get('error','')[:200]}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        print("LEAKAGE FAIL — abort trade arms", flush=True)
        out = {"stamp": stamp, "leakage": leak, "readiness_max": "RESEARCH_ONLY"}
        path = ARTIFACTS / "reports" / "pivot_forecast" / f"reentry_vsa_{stamp}.json"
        path.write_text(json.dumps(out, indent=2), encoding="utf-8")
        return 2

    mae_rows = {}
    for pack in PACKS_MAE:
        print(f"SCORE MAE pack={pack} …", flush=True)
        sc = score_symbol_oos(
            SYMBOL,
            timeframe=TF,
            horizon_bars=H,
            atr_min=2.0,
            feature_pack=pack,
            max_rows=MAX_ROWS,
        )
        m = np.isfinite(sc.y_level) & np.isfinite(sc.level_ret)
        mae_rows[pack] = level_error_stats(
            y_level_ret=sc.y_level[m],
            pred_level_ret=sc.level_ret[m],
            atr_frac=sc.atr_frac[m],
        )
        print(
            f"  MAE={mae_rows[pack]['mae_pct']:.4f} P90={mae_rows[pack]['p90_abs_pct']:.4f} "
            f"corr={mae_rows[pack]['corr']:.3f}",
            flush=True,
        )

    print(f"SCORE trade pack={PACK_TRADE} …", flush=True)
    scored = score_symbol_oos(
        SYMBOL,
        timeframe=TF,
        horizon_bars=H,
        atr_min=2.0,
        feature_pack=PACK_TRADE,
        max_rows=MAX_ROWS,
    )
    intents, mask, ts, is_short, lim = _primary_intents(scored)
    pull = _train_miss_bps(scored, mask)
    print(f"  n_intent={len(intents)} train_pull_bps~={pull:.1f}", flush=True)

    sigs1, fill1 = materialize_working_limits(scored.ohlcv, intents, work_bars=WORK)
    print(f"BT baseline path_fill={fill1['n_filled_path']} …", flush=True)
    b1, r1 = _bt(scored.ohlcv, sigs1, tag="sol_pivot_base_w4", max_hold=H + 2)
    if r1.get("status") == "RAN":
        r1["expectancy_intent_all"] = r1["metrics"]["net_pnl"] / max(len(intents), 1)
        r1["fill_stats"] = fill1
        print(
            f"  PF={r1['metrics']['profit_factor']:.3f} n={r1['metrics']['n_trades']} "
            f"WR={r1['metrics']['win_rate']:.3f} ebr={r1['metrics'].get('entry_bar_exit_rate')} "
            f"stops={r1['metrics'].get('n_stop')}",
            flush=True,
        )

    # Re-entry arm: primary + one limit after each SL
    re_intents = _reentry_intents(b1, pull_bps=pull, work_bars=2) if b1 is not None else []
    print(f"BT reentry n_re_intents={len(re_intents)} …", flush=True)
    sigs_re, fill_re = materialize_working_limits(
        scored.ohlcv, re_intents, work_bars=2
    )
    # Combine: primary signals + reentry signals (one sim)
    combined = list(sigs1) + list(sigs_re)
    combined.sort(key=lambda s: s.ts_ms)
    b2, r2 = _bt(scored.ohlcv, combined, tag="sol_pivot_reentry_sl", max_hold=H + 2)
    if r2.get("status") == "RAN":
        # intent-all uses primary intents only (reentry is contingent)
        r2["expectancy_intent_all"] = r2["metrics"]["net_pnl"] / max(len(intents), 1)
        r2["fill_stats_primary"] = fill1
        r2["fill_stats_reentry"] = fill_re
        r2["n_reentry_intents"] = len(re_intents)
        print(
            f"  PF={r2['metrics']['profit_factor']:.3f} n={r2['metrics']['n_trades']} "
            f"WR={r2['metrics']['win_rate']:.3f} ebr={r2['metrics'].get('entry_bar_exit_rate')} "
            f"stops={r2['metrics'].get('n_stop')}",
            flush=True,
        )

    # Reentry-only economics (second pass on reentry signals alone)
    b3, r3 = _bt(scored.ohlcv, sigs_re, tag="sol_pivot_reentry_only", max_hold=H + 2)
    if r3.get("status") == "RAN":
        r3["fill_stats"] = fill_re
        print(
            f"  reentry-only PF={r3['metrics']['profit_factor']:.3f} "
            f"n={r3['metrics']['n_trades']} WR={r3['metrics']['win_rate']:.3f}",
            flush=True,
        )

    report = {
        "generation_id": "pivot_reentry_vsa_001",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "symbol": SYMBOL,
        "setup": {
            "tf": TF,
            "tp": TP,
            "sl": SL,
            "work": WORK,
            "pack_trade": PACK_TRADE,
            "reentry": "one LIMIT after SL; work=2; limit pulled by train miss bps",
        },
        "leakage": leak,
        "level_mae_by_pack": mae_rows,
        "baseline": r1,
        "baseline_plus_reentry": r2,
        "reentry_leg_only": r3,
        "advice": {
            "vsa": (
                "VSA proxies can help *timing confidence* (effort vs result, climax shape) "
                "but rarely fix level MAE alone. Use as a gate on when to rest, not as magic."
            ),
            "reentry": (
                "Re-limit after SL is a second bet on side accuracy. It helps only if the "
                "first stop was a level miss, not a wrong thesis. Always report reentry-only PF."
            ),
            "other_timing": [
                "time-to-touch model / time buckets (already)",
                "realized vol regime (only rest in medium vol)",
                "session / funding window filters",
                "order-book / trade imbalance if venue data is causal and live-available",
                "multi-TF confirm: 1h side agrees with 15m rest",
            ],
        },
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"reentry_vsa_{stamp}.json"
    latest = out_dir / "reentry_vsa_latest.json"
    md = out_dir / f"reentry_vsa_{stamp}.md"
    text = json.dumps(report, indent=2, default=str)
    path.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    md.write_text(_md(report), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    try:
        print(_md(report), flush=True)
    except UnicodeEncodeError:
        print("(markdown on disk)", flush=True)
    return 0


def _md(r: dict) -> str:
    lines = [
        f"# Pivot reentry + VSA (`{r['stamp']}`)",
        "",
        f"**{r['readiness_max']}** — {r['symbol']}",
        "",
        "## Leakage",
    ]
    for x in r["leakage"]:
        lines.append(f"- {x['pack']}: **{x['status']}**")
    lines.append("")
    lines.append("## Level MAE by pack")
    lines.append("| pack | MAE | P90 | corr | MAE/ATR |")
    lines.append("|---|---:|---:|---:|---:|")
    for k, v in r["level_mae_by_pack"].items():
        lines.append(
            f"| {k} | {v.get('mae_pct')} | {v.get('p90_abs_pct')} | "
            f"{v.get('corr')} | {v.get('mae_atr')} |"
        )
    lines.append("")
    lines.append("## Trade arms (LIMIT)")
    lines.append("| arm | n_sig | n_tr | WR | PF | exp_fill | exp_intent | entry_bar% | pnl | stops |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for name, key in (
        ("baseline", "baseline"),
        ("baseline+reentry", "baseline_plus_reentry"),
        ("reentry-only", "reentry_leg_only"),
    ):
        a = r.get(key) or {}
        if a.get("status") != "RAN":
            lines.append(f"| {name} | — | — | — | {a.get('status')} | — | — | — | — | — |")
            continue
        m = a["metrics"]
        lines.append(
            f"| {name} | {a.get('n_signals')} | {m['n_trades']} | {m['win_rate']:.3f} | "
            f"{m['profit_factor']:.3f} | {m['expectancy']:.4f} | "
            f"{a.get('expectancy_intent_all', float('nan')):.5f} | "
            f"{100*float(m.get('entry_bar_exit_rate', float('nan'))):.1f}% | "
            f"{m['net_pnl']:.2f} | {m.get('n_stop')} |"
        )
    lines.append("")
    lines.append("### Other timing ideas")
    for t in r["advice"]["other_timing"]:
        lines.append(f"- {t}")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
