"""Symmetric K sweep (longs and shorts both allowed up to K/side) — outer OOS only.

Frozen arm = live eth_multitrade_v1_1:
  clarity=mean_strength, fib_ext=1.618 (book3+ TP 2.618%), hold_addon=12, SL=2%.

Window: [2022-01-01, FORWARD_LOCKBOX_START) exclusive end — no lockbox multi-arm peep.
K = 1..36 (symmetric cap per side). Hedge mode always allows long + short together.

Evidence class: OUTER_OOS_K_SWEEP_DIAGNOSTIC. Picking best K on this full stitch is
selection bias; do not treat the argmax as live authorization without nested
inner/outer protocol. MIN_EXCHANGE dust sizing inflates dollar PnL with K.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

# Reuse engine from concurrent hunt (prepare + build_tiered_signals + run_one)
sys.path.insert(0, str(_ROOT / "scripts"))
from hunt_eth_concurrent_fib_clarity import (  # noqa: E402
    BASE_HOLD,
    PACK,
    SYMBOL,
    build_tiered_signals,
    prepare,
    run_one,
)

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.validation.folds import OUTER_FOLD_RANGES  # noqa: E402

# Live v1.1 freeze
CLARITY = "mean_strength"
FIB_EXT = 1.618
HOLD_ADDON = 12
GENERATION = "structure_v1_eth_multitrade_k_sweep_001"


def prepare_outer_oos(*, start: str, end_exclusive: str):
    """Like prepare() but candidates and window stop before end_exclusive."""
    end_ts = pd.Timestamp(end_exclusive, tz="UTC")
    ctx = prepare(start)
    # Trim candidates and bars at/after lockbox
    mask = ctx.window.index < end_ts
    if not bool(mask.any()):
        raise RuntimeError("empty window after end cut")
    # Rebuild context lists relative to trimmed window
    new_window = ctx.window.loc[mask].copy()
    start_ts = pd.Timestamp(start, tz="UTC")
    # Keep only candidates whose bar_i still in window
    # Remap: bar timestamps on old window
    old_ts = ctx.ts_ms
    new_ts = (
        new_window["ts_ms"].to_numpy(dtype=np.int64)
        if "ts_ms" in new_window.columns
        else (new_window.index.asi8 // 1_000_000).astype(np.int64)
    )
    new_index = {int(t): i for i, t in enumerate(new_ts.tolist())}

    from hunt_eth_concurrent_fib_clarity import Candidate, Ctx

    new_cands = []
    for c in ctx.candidates:
        if int(c.ts_ms) >= int(end_ts.value // 1_000_000):
            continue
        bi = new_index.get(int(c.ts_ms))
        if bi is None:
            j = int(np.searchsorted(new_ts, int(c.ts_ms), side="right") - 1)
            if j < 0:
                continue
            bi = j
        if bi >= len(new_ts):
            continue
        new_cands.append(
            Candidate(bar_i=int(bi), ts_ms=int(c.ts_ms), side=int(c.side), mean=float(c.mean))
        )
    new_cands.sort(key=lambda x: x.ts_ms)

    high = new_window["high"].to_numpy(dtype=float)
    low = new_window["low"].to_numpy(dtype=float)
    close = new_window["close"].to_numpy(dtype=float)
    open_ = new_window["open"].to_numpy(dtype=float)
    rng = (high - low) / np.maximum(close, 1e-12)
    s = pd.Series(rng)
    range_6 = s.rolling(6, min_periods=1).mean().to_numpy(dtype=float)
    range_med48 = (
        s.rolling(6, min_periods=1)
        .mean()
        .shift(1)
        .rolling(48, min_periods=1)
        .median()
        .to_numpy(dtype=float)
    )
    # funding already in ctx — re-mask
    fmask = (ctx.funding_ts >= int(new_ts[0])) & (ctx.funding_ts <= int(new_ts[-1]))
    touch_win = ctx.touch_win
    if touch_win is not None and len(touch_win):
        touch_win = touch_win.loc[touch_win.index < end_ts]

    return Ctx(
        target=ctx.target,
        timeframe=ctx.timeframe,
        min_edge=ctx.min_edge,
        start_ts=start_ts,
        end_ts=new_window.index[-1],
        window=new_window,
        touch_win=touch_win,
        touch_tf=ctx.touch_tf,
        funding_ts=ctx.funding_ts[fmask],
        funding_rt=ctx.funding_rt[fmask],
        lev=ctx.lev,
        instrument=ctx.instrument,
        candidates=new_cands,
        open=open_,
        high=high,
        low=low,
        close=close,
        ts_ms=new_ts,
        range_6=range_6,
        range_med48=range_med48,
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=f"{GENERATION}: K=1..max outer-OOS")
    ap.add_argument("--start", default=OUTER_FOLD_RANGES[0][0])
    ap.add_argument("--end", default=FORWARD_LOCKBOX_START, help="exclusive")
    ap.add_argument("--k-min", type=int, default=1)
    ap.add_argument("--k-max", type=int, default=36)
    ap.add_argument(
        "--k-grid",
        default="",
        help=(
            "Comma list of K values (overrides min/max denseness). "
            "Example for sparse upper range: 1,3,5,7,9,12,18,24,30,36"
        ),
    )
    ap.add_argument("--store", action="store_true")
    args = ap.parse_args(argv)

    end = pd.Timestamp(args.end, tz="UTC")
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    if end > lock:
        print(
            f"REFUSED: --end {end} enters lockbox (>{lock}). Use end<={FORWARD_LOCKBOX_START}.",
            flush=True,
        )
        return 2

    conf = run_conformance_check(quiet=True)
    if not conf.get("passed"):
        print("CONFORMANCE_FAIL", conf, flush=True)
        return 2
    if not (PACK / "model.joblib").is_file():
        raise SystemExit(f"missing pack {PACK}")

    if str(args.k_grid).strip():
        k_list = sorted({int(x.strip()) for x in str(args.k_grid).split(",") if x.strip()})
    else:
        k_list = list(range(int(args.k_min), int(args.k_max) + 1))
    if not k_list or min(k_list) < 1:
        raise SystemExit("K values must be positive integers")

    print(
        f"{GENERATION} arm={CLARITY}|fib={FIB_EXT}|hold={HOLD_ADDON} "
        f"K_grid={k_list} window=[{args.start},{args.end})",
        flush=True,
    )
    t0 = time.time()
    print("prepare outer OOS context …", flush=True)
    ctx = prepare_outer_oos(start=str(args.start), end_exclusive=str(args.end))
    print(
        f"candidates={len(ctx.candidates)} bars={len(ctx.window)} "
        f"{ctx.window.index[0]} -> {ctx.end_ts}",
        flush=True,
    )

    rows: list[dict[str, Any]] = []
    for i, k in enumerate(k_list, 1):
        sigs, stats = build_tiered_signals(
            ctx,
            clarity=CLARITY,  # type: ignore[arg-type]
            fib_ext=float(FIB_EXT),
            hold_addon=int(HOLD_ADDON),
            max_per_side=int(k),
            uniform_baseline=False,
        )
        label = f"v1_1|mean_strength|fib1.618|hold12|K={k}"
        row = run_one(
            ctx,
            signals=sigs,
            max_per_side=int(k),
            label=label,
            store=bool(args.store),
            meta_extra={
                "batch": GENERATION,
                "clarity": CLARITY,
                "fib_ext": FIB_EXT,
                "hold_addon": HOLD_ADDON,
                "k": k,
                "evidence_class": "OUTER_OOS_K_SWEEP_DIAGNOSTIC",
                "build_stats": stats,
            },
        )
        row["k"] = k
        row["clarity"] = CLARITY
        row["fib_ext"] = FIB_EXT
        row["hold_addon"] = HOLD_ADDON
        row["build_stats"] = stats
        rows.append(row)
        print(
            f"[{i}/{len(k_list)}] K={k:2d} n={row['n_trades']:>5} "
            f"pnl={row['net_pnl']:>10.2f} pf={row['profit_factor']:.3f} "
            f"peakL={row.get('peak_concurrent_long')} peakS={row.get('peak_concurrent_short')} "
            f"cap_skip={stats.get('n_skipped_cap', 0)}",
            flush=True,
        )

    # Rank diagnostics (not promotion)
    by_pnl = sorted(rows, key=lambda r: float(r.get("net_pnl") or -1e18), reverse=True)
    by_pf = sorted(
        rows,
        key=lambda r: (float(r.get("profit_factor") or 0.0), float(r.get("net_pnl") or 0.0)),
        reverse=True,
    )

    # Plateau: smallest K within 2% of best PnL and PF not worse than max_pf * 0.98
    best_pnl = float(by_pnl[0]["net_pnl"])
    best_pf_row = by_pf[0]
    plateau_pnl = [
        r
        for r in rows
        if float(r["net_pnl"]) >= 0.98 * best_pnl
    ]
    preferred = min(plateau_pnl, key=lambda r: int(r["k"])) if plateau_pnl else by_pnl[0]

    # Marginal gain: first K where ΔPnL(K) - ΔPnL(K-1) < 0.5% of best
    marginal = []
    for j in range(1, len(rows)):
        d = float(rows[j]["net_pnl"]) - float(rows[j - 1]["net_pnl"])
        marginal.append(
            {
                "k": int(rows[j]["k"]),
                "delta_pnl": d,
                "delta_pf": float(rows[j]["profit_factor"]) - float(rows[j - 1]["profit_factor"]),
            }
        )
    # Knee: largest K where cumulative PnL still rises ≥1% over prev
    knee_k = int(rows[0]["k"])
    for j in range(1, len(rows)):
        if float(rows[j]["net_pnl"]) > float(rows[j - 1]["net_pnl"]) * 1.01:
            knee_k = int(rows[j]["k"])
        # keep going while still improving by 0.5%
        if float(rows[j]["net_pnl"]) >= float(rows[j - 1]["net_pnl"]) + 0.01 * abs(best_pnl):
            knee_k = int(rows[j]["k"])

    # Cap saturation: skips from cap
    sat_k = next(
        (int(r["k"]) for r in rows if int((r.get("build_stats") or {}).get("n_skipped_cap") or 0) == 0),
        int(rows[-1]["k"]),
    )
    # When cap stop mattering: n_skipped_cap drops and stays flat
    for r in rows:
        sk = int((r.get("build_stats") or {}).get("n_skipped_cap") or 0)
        if sk == 0:
            sat_k = int(r["k"])
            break

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    payload = {
        "generation_id": GENERATION,
        "evidence_class": "OUTER_OOS_K_SWEEP_DIAGNOSTIC",
        "lockbox": "not_used",
        "window_start_inclusive": str(args.start),
        "window_end_exclusive": str(args.end),
        "data_end": str(ctx.end_ts),
        "frozen_arm": {
            "clarity": CLARITY,
            "fib_ext": FIB_EXT,
            "hold_addon": HOLD_ADDON,
            "sl_pct": 0.02,
            "base_tp": 0.01,
            "note": "matches eth_multitrade_v1_1 knobs; only K varies",
        },
        "k_range": [min(k_list), max(k_list)],
        "k_grid": k_list,
        "elapsed_sec": time.time() - t0,
        "min_size_equity_caveat": True,
        "note": (
            "Symmetric K/side (longs and shorts each up to K). Both sides may be open "
            "at once (hedge). Best K on this full outer stitch is diagnostic / "
            "selection-contaminated for that choice; live stayed at K=7 until re-protocol. "
            "MIN_EXCHANGE makes higher K print larger USDT PnL almost mechanically."
        ),
        "selection": {
            "best_net_pnl": {
                "k": int(by_pnl[0]["k"]),
                "net_pnl": by_pnl[0]["net_pnl"],
                "profit_factor": by_pnl[0]["profit_factor"],
                "n_trades": by_pnl[0]["n_trades"],
                "peak_concurrent_long": by_pnl[0].get("peak_concurrent_long"),
                "peak_concurrent_short": by_pnl[0].get("peak_concurrent_short"),
            },
            "best_profit_factor": {
                "k": int(best_pf_row["k"]),
                "net_pnl": best_pf_row["net_pnl"],
                "profit_factor": best_pf_row["profit_factor"],
                "n_trades": best_pf_row["n_trades"],
            },
            "smallest_k_within_2pct_best_pnl": {
                "k": int(preferred["k"]),
                "net_pnl": preferred["net_pnl"],
                "profit_factor": preferred["profit_factor"],
            },
            "k_where_cap_skips_hit_zero": sat_k,
            "knee_k_marginal_usd": knee_k,
            "live_frozen_k": 7,
        },
        "marginal_deltas": marginal,
        "trials": [
            {
                "k": r["k"],
                "n_trades": r["n_trades"],
                "n_longs": r.get("n_longs"),
                "n_shorts": r.get("n_shorts"),
                "net_pnl": r["net_pnl"],
                "profit_factor": r["profit_factor"],
                "win_rate": r.get("win_rate"),
                "total_fees": r.get("total_fees"),
                "peak_concurrent_long": r.get("peak_concurrent_long"),
                "peak_concurrent_short": r.get("peak_concurrent_short"),
                "peak_concurrent_all": r.get("peak_concurrent_all"),
                "entry_bar_exit_rate": r.get("entry_bar_exit_rate"),
                "n_skipped_cap": (r.get("build_stats") or {}).get("n_skipped_cap"),
                "n_skipped_clarity": (r.get("build_stats") or {}).get("n_skipped_clarity"),
                "n_signals": r.get("n_signals"),
            }
            for r in rows
        ],
        "stamped_utc": stamp,
    }

    out = ARTIFACTS / "reports" / f"{GENERATION}_{stamp}.json"
    latest = ARTIFACTS / "reports" / f"{GENERATION}_latest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, default=str) + "\n"
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")

    sel = payload["selection"]
    print("\n=== SELECTION (outer OOS diagnostic — not live auth) ===", flush=True)
    print(
        f"best net PnL   : K={sel['best_net_pnl']['k']} "
        f"pnl={sel['best_net_pnl']['net_pnl']:.2f} pf={sel['best_net_pnl']['profit_factor']:.3f} "
        f"peakL/S={sel['best_net_pnl']['peak_concurrent_long']}/"
        f"{sel['best_net_pnl']['peak_concurrent_short']}",
        flush=True,
    )
    print(
        f"best PF        : K={sel['best_profit_factor']['k']} "
        f"pnl={sel['best_profit_factor']['net_pnl']:.2f} pf={sel['best_profit_factor']['profit_factor']:.3f}",
        flush=True,
    )
    print(
        f"smallest K ~2% of best PnL: K={sel['smallest_k_within_2pct_best_pnl']['k']}",
        flush=True,
    )
    print(f"K where cap skips → 0: {sel['k_where_cap_skips_hit_zero']}", flush=True)
    print(f"live frozen K: {sel['live_frozen_k']}", flush=True)
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
