"""ETHUSDT switch-book × plain TP-offset ablation (no Fibonacci storytelling).

Prereg: configs/preregister/structure_v1_eth_switch_tp_ablation_001.yaml
Contaminated lockbox diagnostic only. Does not change live packs.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import Side, Signal  # noqa: E402

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402

# Reuse prepare / sim helpers from the prior concurrent hunt.
_FIB = _ROOT / "scripts" / "hunt_eth_concurrent_fib_clarity.py"
_spec = importlib.util.spec_from_file_location("eth_fib_hunt", _FIB)
assert _spec and _spec.loader
fib = importlib.util.module_from_spec(_spec)
sys.modules["eth_fib_hunt"] = fib  # required for @dataclass under importlib
_spec.loader.exec_module(fib)

GENERATION = "structure_v1_eth_switch_tp_ablation_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GENERATION}.yaml"
REPORT_DIR = ARTIFACTS / "reports"
GRID_VERSION = "switch_tp_001"

CLARITY = ("none", "mean_strength")
SWITCH_BOOKS = (2, 3, 4, 5)  # first 1-based book index using addon TP
ADDON_TP = (0.015, 0.02, 0.02618)
HOLD_ADDON = (12, 18)
K_VALUES = (6, 7, 8)
PEAK_CAP = 12
N_TRADES_MIN = 200


def build_signals(
    ctx: Any,
    *,
    clarity: str,
    switch_book: int | None,
    addon_tp: float | None,
    hold_addon: int | None,
    max_per_side: int,
) -> tuple[list[Signal], dict[str, int]]:
    """Books with index < switch_book (or all if switch_book is None) use base TP/hold."""
    open_long: list = []
    open_short: list = []
    strength_hist: list[float] = []
    stats = {
        "n_candidates": 0,
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_cap": 0,
        "n_addon": 0,
        "n_wide_tp": 0,
    }
    out: list[Signal] = []
    high, low, close = ctx.high, ctx.low, ctx.close
    n_bars = len(close)
    cap = fib.resolve_k(max_per_side)

    for cand in ctx.candidates:
        stats["n_candidates"] += 1
        bar_i = cand.bar_i
        if bar_i < 0 or bar_i >= n_bars:
            continue
        open_long = fib._prune_open(open_long, bar_i)
        open_short = fib._prune_open(open_short, bar_i)
        side = int(cand.side)
        books = open_long if side > 0 else open_short
        n_open = len(books)
        is_addon = n_open >= 1

        if is_addon and clarity == "mean_strength":
            recent = strength_hist[-fib.MEAN_LOOKBACK :] if strength_hist else []
            if not fib._mean_strength_ok(cand, recent):
                stats["n_skipped_clarity"] += 1
                strength_hist.append(abs(float(cand.mean)))
                continue

        if n_open >= cap:
            stats["n_skipped_cap"] += 1
            strength_hist.append(abs(float(cand.mean)))
            continue

        book_idx = n_open + 1
        if is_addon:
            stats["n_addon"] += 1

        use_wide = (
            switch_book is not None
            and addon_tp is not None
            and hold_addon is not None
            and book_idx >= int(switch_book)
        )
        if use_wide:
            tp = float(addon_tp)
            hold = int(hold_addon)
            stats["n_wide_tp"] += 1
        else:
            tp = float(fib.BASE_TP)
            hold = int(fib.BASE_HOLD)

        if bar_i + 1 < n_bars:
            entry_bar = bar_i + 1
            entry_px = float(ctx.open[entry_bar])
        else:
            entry_bar = bar_i
            entry_px = float(close[bar_i])

        exit_bar = fib._estimate_exit_bar(
            side=side,
            entry_bar=entry_bar,
            entry_price=entry_px,
            tp=tp,
            sl=fib.BASE_SL,
            hold=hold,
            high=high,
            low=low,
        )
        book = fib.OpenBook(
            side=side,
            entry_bar=entry_bar,
            entry_price=entry_px,
            tp=tp,
            sl=fib.BASE_SL,
            hold=hold,
            exit_bar=exit_bar,
        )
        if side > 0:
            open_long.append(book)
        else:
            open_short.append(book)

        out.append(
            Signal(
                ts_ms=int(cand.ts_ms),
                side=Side.LONG if side > 0 else Side.SHORT,
                stop_offset=fib.BASE_SL,
                target_offset=tp,
                max_hold_bars=hold,
                tag=f"b{book_idx}_tp{tp:.4f}_h{hold}",
                meta={
                    "book_idx": book_idx,
                    "clarity": clarity,
                    "switch_book": switch_book,
                    "addon_tp": addon_tp,
                    "tp_offset": tp,
                },
            )
        )
        stats["n_emitted"] += 1
        strength_hist.append(abs(float(cand.mean)))
    return out, stats


def arm_label(
    *,
    clarity: str,
    switch_book: int | None,
    addon_tp: float | None,
    hold: int | None,
    k: int,
) -> str:
    if switch_book is None:
        return f"control|clarity={clarity}|tp=0.01|hold=6|K={k}"
    return (
        f"clarity={clarity}|switch={switch_book}|tp={addon_tp}|hold={hold}|K={k}"
    )


def build_arms() -> list[dict[str, Any]]:
    arms: list[dict[str, Any]] = []
    # Controls: all books +1% / hold 6
    for clarity in CLARITY:
        for k in K_VALUES:
            arms.append(
                {
                    "kind": "control",
                    "clarity": clarity,
                    "switch_book": None,
                    "addon_tp": None,
                    "hold": None,
                    "k": int(k),
                }
            )
    # Grid
    for clarity in CLARITY:
        for s in SWITCH_BOOKS:
            for tp in ADDON_TP:
                for hold in HOLD_ADDON:
                    for k in K_VALUES:
                        arms.append(
                            {
                                "kind": "grid",
                                "clarity": clarity,
                                "switch_book": int(s),
                                "addon_tp": float(tp),
                                "hold": int(hold),
                                "k": int(k),
                            }
                        )
    return arms


def rank_report(trials: list[dict[str, Any]]) -> dict[str, Any]:
    rows = []
    for t in trials:
        pnl = float(t.get("net_pnl") or float("nan"))
        pf = float(t.get("profit_factor") or float("nan"))
        mdd = abs(float(t.get("max_drawdown") or 0.0))
        peak = float(t.get("peak_concurrent_all") or 0.0)
        n = float(t.get("n_trades") or 0.0)
        if not np.isfinite(pnl) or not np.isfinite(pf):
            continue
        if n < N_TRADES_MIN or peak > PEAK_CAP:
            continue
        rows.append(
            {
                **{k: t.get(k) for k in (
                    "label", "kind", "clarity", "switch_book", "addon_tp",
                    "hold", "k", "n_trades", "net_pnl", "profit_factor",
                    "win_rate", "max_drawdown", "peak_concurrent_all",
                )},
                "pnl_over_mdd": pnl / max(mdd, 1e-9),
            }
        )
    if not rows:
        return {"eligible": [], "live_reference": None, "verdict": "NO_ELIGIBLE"}

    df = pd.DataFrame(rows)
    df["r_pf"] = df["profit_factor"].rank(pct=True)
    df["r_pnl"] = df["net_pnl"].rank(pct=True)
    df["r_calmar"] = df["pnl_over_mdd"].rank(pct=True)
    df["balance"] = 0.40 * df["r_pf"] + 0.30 * df["r_pnl"] + 0.30 * df["r_calmar"]
    df = df.sort_values(
        ["balance", "profit_factor", "peak_concurrent_all"],
        ascending=[False, False, True],
    )

    live_mask = (
        (df["clarity"] == "mean_strength")
        & (df["switch_book"] == 3)
        & np.isclose(df["addon_tp"].astype(float), 0.02618)
        & (df["hold"] == 12)
        & (df["k"] == 7)
    )
    live = df.loc[live_mask].iloc[0].to_dict() if live_mask.any() else None
    best = df.iloc[0].to_dict()
    best_ms = df[df["clarity"] == "mean_strength"]
    best_ms_row = best_ms.iloc[0].to_dict() if len(best_ms) else None

    verdict = "KEEP_LIVE_eth_multitrade_v1_1"
    reason = "no mean_strength arm cleared the live_v1_2 gate"
    gate_pass_row = None
    if live is not None and len(best_ms):
        # Prereg: any mean_strength arm may pass if it beats live on ALL gates.
        dom = best_ms[
            (best_ms["balance"] > float(live["balance"]))
            & (best_ms["profit_factor"] >= float(live["profit_factor"]))
            & (best_ms["peak_concurrent_all"] <= PEAK_CAP)
        ].sort_values(["balance", "profit_factor"], ascending=False)
        if len(dom):
            gate_pass_row = dom.iloc[0].to_dict()
            if gate_pass_row["label"] == live["label"]:
                reason = "live reference already satisfies the gate as top dual-beat arm"
            else:
                verdict = "CANDIDATE_LIVE_v1_2_LOCKBOX_ONLY"
                reason = (
                    f"{gate_pass_row['label']} beats live on balance+PF "
                    f"with peak<={PEAK_CAP} (contaminated lockbox — not promotion)"
                )
        elif best_ms_row is not None:
            reason = (
                f"best-balance mean_strength={best_ms_row['label']} "
                f"bal={best_ms_row['balance']:.3f} pf={best_ms_row['profit_factor']:.3f} "
                f"vs live bal={live['balance']:.3f} pf={live['profit_factor']:.3f} "
                f"(no arm beats live on BOTH)"
            )

    def _clean(d: dict[str, Any] | None) -> dict[str, Any] | None:
        if d is None:
            return None
        out = {}
        for k, v in d.items():
            if isinstance(v, (np.floating, float)):
                out[k] = float(v)
            elif isinstance(v, (np.integer, int)):
                out[k] = int(v)
            else:
                out[k] = v
        return out

    return {
        "n_eligible": int(len(df)),
        "peak_cap": PEAK_CAP,
        "n_trades_min": N_TRADES_MIN,
        "live_reference": _clean(live),
        "best_overall_eligible": _clean(best),
        "best_mean_strength_eligible": _clean(best_ms_row),
        "best_gate_pass_mean_strength": _clean(gate_pass_row),
        "top10": [_clean(r) for r in df.head(10).to_dict(orient="records")],
        "verdict": verdict,
        "reason": reason,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=FORWARD_LOCKBOX_START)
    ap.add_argument("--store", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="debug: first N arms only")
    from llm2.evidence.lockbox_guard import add_lockbox_guard_args, require_lockbox_access
    from llm2.research_policy import PolicyError

    add_lockbox_guard_args(ap)
    args = ap.parse_args()

    try:
        require_lockbox_access(
            experiment_id=GENERATION,
            window_start=str(args.start),
            purpose="multi_arm_lockbox_grid",
            symbols=["ETHUSDT"],
            accepted_contamination=bool(args.i_accept_lockbox_contamination),
            open_finplot=False,
            notes="scripts/hunt_eth_switch_tp_ablation.py",
        )
    except PolicyError as exc:
        print(f"REFUSED: {exc}", flush=True)
        return 2

    conf = run_conformance_check()
    if not conf.get("passed"):
        print("CONFORMANCE_FAIL", conf, flush=True)
        return 2

    if not PREREG.is_file():
        raise SystemExit(f"prereg missing: {PREREG}")

    print(f"PREPARE lockbox start={args.start}", flush=True)
    ctx = fib.prepare(str(args.start))
    arms = build_arms()
    if args.limit and args.limit > 0:
        arms = arms[: int(args.limit)]
    print(f"ARMS n={len(arms)} generation={GENERATION}", flush=True)

    trials: list[dict[str, Any]] = []
    t0 = time.time()
    for i, arm in enumerate(arms, 1):
        label = arm_label(
            clarity=arm["clarity"],
            switch_book=arm["switch_book"],
            addon_tp=arm["addon_tp"],
            hold=arm["hold"],
            k=arm["k"],
        )
        signals, stats = build_signals(
            ctx,
            clarity=arm["clarity"],
            switch_book=arm["switch_book"],
            addon_tp=arm["addon_tp"],
            hold_addon=arm["hold"],
            max_per_side=int(arm["k"]),
        )
        row = fib.run_one(
            ctx,
            signals=signals,
            max_per_side=int(arm["k"]),
            label=label,
            store=bool(args.store),
            meta_extra={
                "batch": GENERATION,
                "grid_version": GRID_VERSION,
                "prereg": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
                **arm,
                "build_stats": stats,
            },
        )
        row.update(arm)
        row["build_stats"] = stats
        trials.append(row)
        print(
            f"[{i}/{len(arms)}] {label} n={row['n_trades']} "
            f"pnl={row['net_pnl']:.2f} pf={row['profit_factor']:.3f} "
            f"peak={row['peak_concurrent_all']}",
            flush=True,
        )

    ranking = rank_report(trials)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    try:
        from llm2.evidence.peek_log import append_peek
        from llm2.research_policy import classify_evidence_for_window

        pe_cls = classify_evidence_for_window(
            window_start=str(args.start),
            window_end=str(ctx.end_ts.date()) if hasattr(ctx.end_ts, "date") else str(ctx.end_ts),
            experiment_family="multitrade_knob",
        )
        append_peek(
            experiment_id=GENERATION,
            window_start=str(args.start),
            window_end=str(getattr(ctx.end_ts, "date", lambda: ctx.end_ts)()),
            purpose="multi_arm_lockbox_grid",
            arms=f"{len(arms)} arms switch×tp×hold×K",
            n_arms=len(arms),
            evidence_class=pe_cls,
            notes=f"verdict={ranking.get('verdict')}",
        )
    except Exception as exc:  # noqa: BLE001
        print(f"PEEK_LOG_WARN {type(exc).__name__}: {exc}", flush=True)
    out = {
        "generation_id": GENERATION,
        "grid_version": GRID_VERSION,
        "prereg": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
        "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
        "lockbox_start": str(args.start),
        "data_end": str(ctx.end_ts),
        "n_arms": len(arms),
        "elapsed_sec": round(time.time() - t0, 1),
        "engine": "botsgeneral_tradesim",
        "note": (
            "Plain TP-offset schedule ablation (switch_book × addon_tp). "
            "No Fibonacci claim. Contaminated lockbox — not a promotion gate."
        ),
        "ranking": ranking,
        "trials": trials,
    }
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORT_DIR / f"{GENERATION}_{stamp}.json"
    latest = REPORT_DIR / f"{GENERATION}_latest.json"
    text = json.dumps(out, indent=2, default=str)
    path.write_text(text + "\n", encoding="utf-8")
    latest.write_text(text + "\n", encoding="utf-8")

    print("\n=== RANKING VERDICT ===", flush=True)
    print("verdict:", ranking.get("verdict"), flush=True)
    print("reason:", ranking.get("reason"), flush=True)
    print("live_reference:", ranking.get("live_reference"), flush=True)
    print("best_mean_strength:", ranking.get("best_mean_strength_eligible"), flush=True)
    print("wrote", path, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
