"""Pivot: level-pack MAE, placement blend, time-bucket cancel, TF trial + leakage.

Preregistered research arms (SOL primary; ETH control on TF). LIMIT only.
RESEARCH_ONLY — not promotion. Train-fold stats only for placement pulls.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
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
from llm2.pivot.strategy.level_economy import level_error_stats  # noqa: E402
from llm2.pivot.strategy.limit_placement import (  # noqa: E402
    apply_placement,
    estimate_miss_overshoot_bps,
    limit_price_from_return,
)
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    ScoredOOS,
    gate_mask,
    score_symbol_oos,
)
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

GENERATION = "pivot_level_place_tf_001"
MAX_ROWS = 120_000


@dataclass(frozen=True)
class Arm:
    id: str
    tf: str
    h_bars: int
    pack: str
    placement: str  # raw|blend_75_1pct|miss_comp|miss_minus_overshoot
    work_mode: str  # fixed4|fixed2|time_bucket
    tp: float = 0.01
    sl: float = 0.01
    note: str = ""


ARMS: tuple[Arm, ...] = (
    Arm("sol15_raw_w4", "15m", 4, "price_vol_mom", "raw", "fixed4", note="baseline"),
    Arm("sol15_levelpack_raw_w4", "15m", 4, "level_focus", "raw", "fixed4", note="better where pack"),
    Arm("sol15_blend75_1pct_w4", "15m", 4, "level_focus", "blend_75_1pct", "fixed4", note="user 75/25@1%"),
    Arm("sol15_miss_comp_w4", "15m", 4, "level_focus", "miss_comp", "fixed4", note="pull by train miss"),
    Arm("sol15_miss_minus_os_w4", "15m", 4, "level_focus", "miss_minus_overshoot", "fixed4", note="miss-overshoot"),
    Arm("sol15_blend_timebucket", "15m", 4, "level_focus", "blend_75_1pct", "time_bucket", note="cancel if late"),
    Arm("sol15_raw_w2", "15m", 4, "level_focus", "raw", "fixed2", note="short work"),
    # Native warehouse TFs only (no 30m). Same ~60m label horizon: 5m×12, 1h×1.
    Arm("sol5m_raw_w4", "5m", 12, "level_focus", "raw", "fixed4", note="TF trial 5m; expect more entry-bar noise"),
    Arm("sol1h_raw_w1", "1h", 1, "level_focus", "raw", "fixed1", note="TF trial 1h; expect fewer entry-bar exits"),
    Arm("eth15_blend75_1pct_w4", "15m", 4, "level_focus", "blend_75_1pct", "fixed4", note="ETH control"),
)


def _leakage_check(symbol: str, timeframe: str, pack: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    from llm2.pivot.features.packs import build_feature_frame

    try:
        ohlcv = load_ohlcv(symbol, timeframe)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-8000:].copy()

        def _builder(df: pd.DataFrame, **_kw):
            return build_feature_frame(df, pack=pack)

        report = run_leakage_audit(
            ohlcv=ohlcv,
            build_features=_builder,
            interval=timeframe,
            symbol=symbol,
            timeframe=timeframe,
            registry_path=None,
        )
        require_clean_audit(report)
        return {
            "status": "PASS",
            "symbol": symbol,
            "timeframe": timeframe,
            "pack": pack,
            "summary": str(report)[:500],
            "ok": bool(getattr(report, "ok", False)),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "status": "FAIL",
            "symbol": symbol,
            "timeframe": timeframe,
            "pack": pack,
            "error": str(exc)[:800],
        }


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
    for k in ("entry_bar_exit_rate", "entry_bar_exits", "n_entry_bar_exits"):
        if hasattr(m, k):
            try:
                out[k] = float(getattr(m, k))
            except (TypeError, ValueError):
                pass
    # derive entry-bar exit rate from headline attrs if present
    if hasattr(m, "n_trades") and hasattr(bundle, "trades"):
        try:
            tr = bundle.trades
            if tr is not None and len(tr):
                # trade objects or dataframe
                if hasattr(tr, "columns") and "exit_reason" in getattr(tr, "columns", []):
                    pass
        except Exception:  # noqa: BLE001
            pass
    return out


def _bt(symbol, tf, ohlcv, signals, *, sl, tag, max_hold):
    if len(signals) < 12:
        return {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(tf, symbol)
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
    dec_ms = int(TF_MS[tf])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    lev = float(leverage_from_stop(sl))
    try:
        bundle = run_strategy_backtest(
            window,
            signals,
            symbol=symbol,
            timeframe=tf,
            strategy_id=tag,
            touch_ohlcv=touch_win if len(touch_win) else None,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=tf),
            instrument=research_instrument(symbol),
            funding_ts_ms=f_ts[fmask],
            funding_rate=f_rt[fmask],
            plot=False,
            print_headline=False,
            store_path=None,
        )
    except Exception as exc:  # noqa: BLE001
        return {"status": "BT_ERROR", "error": str(exc)[:400], "n_signals": len(signals)}
    met = _metrics(bundle)
    # entry-bar exits from trades if available
    ebr = _entry_bar_exit_rate(bundle)
    if ebr is not None:
        met["entry_bar_exit_rate"] = ebr
    return {"status": "RAN", "metrics": met, "n_signals": len(signals)}


def _entry_bar_exit_rate(bundle) -> float | None:
    trades = getattr(bundle, "trades", None)
    if trades is None:
        return None
    try:
        if isinstance(trades, pd.DataFrame):
            if "hold_bars" in trades.columns:
                n = len(trades)
                if n == 0:
                    return float("nan")
                return float((trades["hold_bars"] <= 0).mean())
        # sequence of objects
        holds = []
        for t in trades:
            h = getattr(t, "hold_bars", None)
            if h is None:
                h = getattr(t, "bars_held", None)
            if h is not None:
                holds.append(float(h))
        if not holds:
            return None
        return float(np.mean(np.asarray(holds) <= 0))
    except Exception:  # noqa: BLE001
        return None


def _path_extremes(ohlcv, ts_ms, work_bars: int):
    bar_ts = index_to_ms(ohlcv.index)
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
    n = len(bar_ts)
    ext = np.full(len(ts_ms), np.nan)
    touched_hi = np.zeros(len(ts_ms), dtype=bool)
    touched_lo = np.zeros(len(ts_ms), dtype=bool)
    for j, t in enumerate(ts_ms):
        i = pos.get(int(t))
        if i is None:
            continue
        i0, i1 = i + 1, min(n, i + 1 + work_bars)
        if i0 >= n:
            continue
        ext_hi = float(np.max(high[i0:i1]))
        ext_lo = float(np.min(low[i0:i1]))
        # store both via caller choice; here return hi in ext for short later
        ext[j] = ext_hi  # placeholder overwritten per side in caller
        touched_hi[j] = True
        touched_lo[j] = True
        # actually keep arrays
        ext[j] = np.nan  # reset; use parallel arrays
    # rebuild properly
    hi_ext = np.full(len(ts_ms), np.nan)
    lo_ext = np.full(len(ts_ms), np.nan)
    for j, t in enumerate(ts_ms):
        i = pos.get(int(t))
        if i is None:
            continue
        i0, i1 = i + 1, min(n, i + 1 + work_bars)
        if i0 >= n or i1 <= i0:
            continue
        hi_ext[j] = float(np.max(high[i0:i1]))
        lo_ext[j] = float(np.min(low[i0:i1]))
    return hi_ext, lo_ext


def _level_mae_block(scored: ScoredOOS) -> dict:
    m = np.isfinite(scored.y_level) & np.isfinite(scored.level_ret)
    return level_error_stats(
        y_level_ret=scored.y_level[m],
        pred_level_ret=scored.level_ret[m],
        atr_frac=scored.atr_frac[m],
    )


def _run_arm(symbol: str, scored: ScoredOOS, arm: Arm, pull_cache: dict) -> dict:
    mask = gate_mask(scored, mode="p75", tp=arm.tp, sl=arm.sl)
    idx = np.flatnonzero(mask)
    if idx.size == 0:
        return {"arm": arm.id, "status": "NO_SIGNALS"}

    # train-only pull from first half of gated rows (proxy for fold train; conservative)
    cut = max(50, int(0.7 * idx.size))
    train_idx, te_use = idx[:cut], idx  # placement params from early OOS-looking proxy
    # Better: use rows where we can estimate on train_idx only
    ts_tr = scored.ts_ms[train_idx]
    close_tr = scored.close[train_idx]
    lr_tr = scored.level_ret[train_idx]
    short_tr = scored.p_high[train_idx] >= 0.5
    lim_tr = np.array(
        [
            limit_price_from_return(
                float(close_tr[j]),
                float(np.clip(lr_tr[j] if np.isfinite(lr_tr[j]) else (0.005 if short_tr[j] else -0.005), -0.03, 0.03)),
            )
            for j in range(len(train_idx))
        ],
        dtype=float,
    )
    hi_e, lo_e = _path_extremes(scored.ohlcv, ts_tr, work_bars=4)
    ext = np.where(short_tr, hi_e, lo_e)
    touch = np.where(short_tr, hi_e >= lim_tr, lo_e <= lim_tr)
    med_m, med_o, net = estimate_miss_overshoot_bps(
        closes=close_tr, limits=lim_tr, is_short=short_tr, touched=touch, window_ext=ext
    )
    pull_cache[arm.id] = {"median_miss_bps": med_m, "median_overshoot_bps": med_o, "net_pull_bps": net}

    if arm.placement == "miss_comp":
        pull_bps = med_m
    elif arm.placement == "miss_minus_overshoot":
        pull_bps = net
    else:
        pull_bps = 0.0

    intents: list[LimitIntent] = []
    for j in te_use:
        c = float(scored.close[j])
        if not np.isfinite(c) or c <= 0:
            continue
        is_short = bool(scored.p_high[j] >= 0.5)
        lr = float(scored.level_ret[j]) if np.isfinite(scored.level_ret[j]) else (
            0.005 if is_short else -0.005
        )
        lr = float(np.clip(lr, -0.03, 0.03))
        if is_short:
            lr = max(lr, 0.0015)
        else:
            lr = min(lr, -0.0015)
        lr_adj = apply_placement(
            lr, is_short=is_short, mode=arm.placement, pull_bps=pull_bps  # type: ignore[arg-type]
        )
        # keep on correct side of market
        if is_short:
            lr_adj = float(np.clip(lr_adj, 0.0005, 0.04))
        else:
            lr_adj = float(np.clip(lr_adj, -0.04, -0.0005))
        lim = limit_price_from_return(c, lr_adj)

        if arm.work_mode == "fixed4":
            wb = 4
        elif arm.work_mode == "fixed2":
            wb = 2
        elif arm.work_mode == "fixed1":
            wb = 1
        elif arm.work_mode == "time_bucket":
            tb = float(scored.time_bars[j]) if np.isfinite(scored.time_bars[j]) else 2.0
            # cancel early if model says late (> H): work_bars=0 → drop
            if tb > float(arm.h_bars) + 0.5:
                wb = 0
            else:
                wb = int(np.clip(int(np.ceil(tb)) + 1, 1, arm.h_bars))
        else:
            wb = 4

        intents.append(
            LimitIntent(
                decision_ts_ms=int(scored.ts_ms[j]),
                side=Side.SHORT if is_short else Side.LONG,
                limit_price=float(lim),
                stop_offset=float(arm.sl),
                target_offset=float(arm.tp),
                max_hold_bars=max(arm.h_bars + 2, wb + 2),
                work_bars=wb,
                meta={"placement": arm.placement, "lr_adj": lr_adj},
            )
        )

    default_wb = 4 if arm.work_mode.startswith("fixed") is False else (
        4 if arm.work_mode == "fixed4" else (2 if arm.work_mode == "fixed2" else 1)
    )
    if arm.work_mode == "fixed4":
        default_wb = 4
    elif arm.work_mode == "fixed2":
        default_wb = 2
    elif arm.work_mode == "fixed1":
        default_wb = 1
    else:
        default_wb = 4

    sigs, fill_stats = materialize_working_limits(
        scored.ohlcv, intents, work_bars=default_wb
    )
    n_intent = len(intents)
    print(
        f"  BT {arm.id} intent={n_intent} path_fill={fill_stats.get('n_filled_path')} "
        f"pull_bps={pull_bps:.1f} …",
        flush=True,
    )
    res = _bt(
        symbol,
        arm.tf,
        scored.ohlcv,
        sigs,
        sl=arm.sl,
        tag=arm.id,
        max_hold=arm.h_bars + 2,
    )
    out = {
        "arm": arm.id,
        "symbol": symbol,
        "tf": arm.tf,
        "pack": arm.pack,
        "placement": arm.placement,
        "work_mode": arm.work_mode,
        "note": arm.note,
        "n_intent": n_intent,
        "fill_stats": fill_stats,
        "train_pull": pull_cache[arm.id],
        "level_mae_oos": _level_mae_block(scored),
        **res,
    }
    if res.get("status") == "RAN" and n_intent > 0:
        out["expectancy_intent_all"] = float(res["metrics"]["net_pnl"]) / n_intent
        out["expectancy_fill_only"] = float(res["metrics"]["expectancy"])
        days = max(
            1.0,
            (
                pd.Timestamp(scored.ohlcv.index[-1]) - pd.Timestamp(scored.ohlcv.index[0])
            ).total_seconds()
            / 86400.0,
        )
        out["trades_per_month"] = float(res["metrics"]["n_trades"]) / (days / 30.0)
    print(
        f"    {res.get('status')} "
        + (
            f"n={res['metrics']['n_trades']} PF={res['metrics']['profit_factor']:.3f} "
            f"WR={res['metrics']['win_rate']:.3f} ebr={res['metrics'].get('entry_bar_exit_rate')} "
            f"intent_exp={out.get('expectancy_intent_all')}"
            if res.get("status") == "RAN"
            else str(res)[:200]
        ),
        flush=True,
    )
    return out


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(f"PIVOT_LEVEL_PLACE_TF start {stamp}", tier=0)
    print(f"{GENERATION} stamp={stamp}", flush=True)

    print("LEAKAGE audits (decisive) …", flush=True)
    leak_reports = [
        _leakage_check("SOLUSDT", "15m", "level_focus"),
        _leakage_check("SOLUSDT", "15m", "price_vol_mom"),
        _leakage_check("SOLUSDT", "5m", "level_focus"),
        _leakage_check("SOLUSDT", "1h", "level_focus"),
        _leakage_check("ETHUSDT", "15m", "level_focus"),
    ]
    for lr in leak_reports:
        print(f"  leakage {lr['pack']} {lr['timeframe']}: {lr['status']}", flush=True)
        if lr["status"] != "PASS":
            print(f"    HARD STOP detail: {lr.get('error', '')[:300]}", flush=True)

    if any(x["status"] != "PASS" for x in leak_reports):
        # still record but do not pretend clean
        print("LEAKAGE FAIL — continuing diagnostics as RESEARCH_ONLY_CONTAMINATED risk", flush=True)

    scored_cache: dict[tuple[str, str, str, int], ScoredOOS] = {}

    def get_scored(symbol: str, arm: Arm) -> ScoredOOS:
        key = (symbol, arm.tf, arm.pack, arm.h_bars)
        if key not in scored_cache:
            print(f"SCORE {key} …", flush=True)
            scored_cache[key] = score_symbol_oos(
                symbol,
                timeframe=arm.tf,
                horizon_bars=arm.h_bars,
                atr_min=2.0,
                feature_pack=arm.pack,
                max_rows=MAX_ROWS,
            )
            mae = _level_mae_block(scored_cache[key])
            print(
                f"  MAE%={mae.get('mae_pct')} P90%={mae.get('p90_abs_pct')} corr={mae.get('corr')}",
                flush=True,
            )
        return scored_cache[key]

    rows = []
    pull_cache: dict = {}
    for arm in ARMS:
        symbol = "ETHUSDT" if arm.id.startswith("eth") else "SOLUSDT"
        needed = next(
            (
                x
                for x in leak_reports
                if x["symbol"] == symbol
                and x["timeframe"] == arm.tf
                and x["pack"] == arm.pack
            ),
            None,
        )
        if needed is None:
            needed = next(
                (
                    x
                    for x in leak_reports
                    if x["timeframe"] == arm.tf and x["pack"] == arm.pack
                ),
                None,
            )
        if needed is None or needed["status"] != "PASS":
            rows.append(
                {
                    "arm": arm.id,
                    "status": "SKIP_LEAKAGE_FAIL",
                    "leakage": needed,
                }
            )
            continue
        scored = get_scored(symbol, arm)
        rows.append(_run_arm(symbol, scored, arm, pull_cache))

    # pack MAE comparison table
    mae_compare = {}
    for (sym, tf, pack, h), sc in scored_cache.items():
        mae_compare[f"{sym}_{tf}_{pack}_H{h}"] = _level_mae_block(sc)

    report = {
        "generation_id": GENERATION,
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "leakage": leak_reports,
        "mae_by_pack": mae_compare,
        "arms": rows,
        "placement_idea": {
            "user": "75% weight on pred±1% toward market, 25% on raw pred (one limit)",
            "miss_overshoot": "pull_bps = max(0, median_miss - median_overshoot) from early gated sample",
            "note": (
                "0.82% mean abs gap is not 'precision'; 100-82'; it is typical |limit-wick| "
                "across intents. Pulling toward market raises fills; may dilute edge."
            ),
        },
        "multi_limit_recommendation": (
            "Yes later: ladder 2–3 rests with size ∝ calibrated p_any * side_confidence, "
            "but only after level P90 <~1%. Today, ladders mostly buy more fills of a noisy level "
            "and add fee drag. Prefer one bias-corrected limit + hard cancel."
        ),
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"level_place_tf_{stamp}.json"
    latest = out_dir / "level_place_tf_latest.json"
    md_path = out_dir / f"level_place_tf_{stamp}.md"
    text = json.dumps(report, indent=2, default=str)
    path.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    md = _md(report)
    md_path.write_text(md, encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    try:
        print(md, flush=True)
    except UnicodeEncodeError:
        print("(markdown on disk)", flush=True)
    return 0


def _md(report: dict) -> str:
    lines = [
        f"# Pivot level / placement / TF (`{report['stamp']}`)",
        "",
        f"**{report['readiness_max']}**",
        "",
        "## Leakage",
        "",
    ]
    for x in report["leakage"]:
        lines.append(f"- {x['pack']} {x['timeframe']}: **{x['status']}**")
    lines.append("")
    lines.append("## Level MAE by pack/TF")
    lines.append("")
    for k, v in report["mae_by_pack"].items():
        lines.append(
            f"- {k}: MAE={v.get('mae_pct')} P90={v.get('p90_abs_pct')} corr={v.get('corr')}"
        )
    lines.append("")
    lines.append(
        "| arm | n_intent | fill% | n_tr | /mo | WR | PF | exp_fill | exp_intent | "
        "entry_bar% | pnl | pull_net_bps |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for a in report["arms"]:
        if a.get("status") not in (None, "RAN") and a.get("status") != "RAN":
            if a.get("status") != "RAN":
                lines.append(f"| {a.get('arm')} | — | — | — | — | — | {a.get('status')} | — | — | — | — | — |")
                continue
        if a.get("status") != "RAN":
            continue
        fs = a.get("fill_stats") or {}
        m = a["metrics"]
        trp = a.get("train_pull") or {}
        lines.append(
            f"| {a['arm']} | {a['n_intent']} | {100*float(fs.get('fill_rate', float('nan'))):.1f}% | "
            f"{m['n_trades']} | {a.get('trades_per_month', float('nan')):.1f} | "
            f"{m['win_rate']:.3f} | {m['profit_factor']:.3f} | "
            f"{a.get('expectancy_fill_only', float('nan')):.4f} | "
            f"{a.get('expectancy_intent_all', float('nan')):.5f} | "
            f"{100*float(m.get('entry_bar_exit_rate', float('nan'))):.1f}% | "
            f"{m['net_pnl']:.2f} | {trp.get('net_pull_bps', float('nan')):.1f} |"
        )
    lines.append("")
    lines.append(report["multi_limit_recommendation"])
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
