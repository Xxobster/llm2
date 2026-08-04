"""Fold geometry for the pulse-continuation preregistration — a sample-size calculation.

This script deliberately computes **no performance number of any kind**. It counts events.
Choosing fold boundaries after seeing how the strategy performed in each candidate geometry
would be selection on out-of-sample, which voids the result; choosing them from event counts
alone is the ordinary power calculation that should precede any experiment.

The frozen V2.1 profile needs at least five eligible outer folds with at least ten resolved
trades each, and fifty pooled out-of-sample trades. The preregistration flagged that roughly
26 up-pulses per year would not fill that with the existing nine-month folds. This measures
whether that is true and, if so, what geometry does fill it.

Output is written to the preregistration as a frozen block with a hash.
"""

from __future__ import annotations

import hashlib
import json

import pandas as pd

from llm2.data.loader import load_ohlcv
from llm2.diagnostics.events import detect_pulses
from llm2.validation.folds import OUTER_FOLD_RANGES

SYMBOL, TIMEFRAME = "BTCUSDT", "1h"
TRAIN_END = "2026-05-01"          # forward lockbox start; nothing after this is touched
MIN_TRADES_PER_FOLD = 10
MIN_POOLED_TRADES = 50
MIN_FOLDS = 5

# Candidate geometries, all anchored on the same start so none of them is tuned to a
# particular market episode. Only the out-of-sample span length varies.
CANDIDATE_MONTHS = [9, 12, 15, 18, 24]
OOS_START = pd.Timestamp("2021-01-01", tz="UTC")
OOS_END = pd.Timestamp(TRAIN_END, tz="UTC")


def build_ranges(months: int) -> list[tuple[pd.Timestamp, pd.Timestamp]]:
    out, cur = [], OOS_START
    while cur < OOS_END:
        nxt = min(cur + pd.DateOffset(months=months), OOS_END)
        if (nxt - cur).days >= months * 25:
            out.append((cur, nxt))
        cur = nxt
    return out


HOLD_BARS = 96  # frozen in the preregistration


def sequential_trades(events: pd.DataFrame, hold_bars: int) -> pd.DataFrame:
    """Events that actually become trades under one-position-at-a-time.

    This is the difference between a *signal* count and a *trade* count, and it is where
    the sample size is really decided. The pulse detector enforces a 24-bar minimum gap
    while the entry rule holds for 96 bars, so up to four signals can fire inside a single
    open position. A live bot on a single symbol takes the first and ignores the rest.

    Counting signals instead of trades would have overstated the fold sample size roughly
    fourfold and produced folds that silently fail the ten-trade floor at run time, after
    the out-of-sample window had already been opened.
    """
    kept, busy_until = [], -(10**9)
    for bar, ts in zip(events["bar"].to_numpy(), events["timestamp"]):
        if bar >= busy_until:
            kept.append((int(bar), ts))
            busy_until = int(bar) + hold_bars
    return pd.DataFrame(kept, columns=["bar", "timestamp"])


def main() -> int:
    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    ohlcv = ohlcv[ohlcv.index < OOS_END]
    pulses = detect_pulses(ohlcv)
    up = pulses[pulses["direction"] > 0].copy()
    up["timestamp"] = pd.to_datetime(up["timestamp"], utc=True)

    trades = sequential_trades(up, HOLD_BARS)
    print(f"up-pulse signals {len(up)} -> sequential trades {len(trades)} "
          f"at a {HOLD_BARS}-bar hold ({100 * len(trades) / max(1, len(up)):.0f}% survive overlap)")
    up = trades

    print(f"{SYMBOL} {TIMEFRAME}: {len(ohlcv):,} bars to {TRAIN_END}")
    print(f"pulses total {len(pulses)}, up-pulses {len(up)}")
    span_years = (ohlcv.index[-1] - ohlcv.index[0]).days / 365.25
    print(f"span {span_years:.2f} years -> {len(up) / span_years:.1f} up-pulses per year\n")

    print("=== existing geometry (llm2.validation.folds.OUTER_FOLD_RANGES) ===")
    existing = [
        (pd.Timestamp(a, tz="UTC"), pd.Timestamp(b, tz="UTC")) for a, b in OUTER_FOLD_RANGES
    ]
    counts = [int(((up["timestamp"] >= a) & (up["timestamp"] < b)).sum()) for a, b in existing]
    for (a, b), c in zip(existing, counts):
        flag = "OK" if c >= MIN_TRADES_PER_FOLD else "UNDER"
        print(f"  {a.date()} .. {b.date()}  events={c:3d}  {flag}")
    print(f"  folds={len(counts)} pooled={sum(counts)} "
          f"under_floor={sum(1 for c in counts if c < MIN_TRADES_PER_FOLD)}\n")

    print("=== candidate geometries ===")
    results = []
    for months in CANDIDATE_MONTHS:
        ranges = build_ranges(months)
        c = [int(((up["timestamp"] >= a) & (up["timestamp"] < b)).sum()) for a, b in ranges]
        under = sum(1 for x in c if x < MIN_TRADES_PER_FOLD)
        ok = (
            len(c) >= MIN_FOLDS
            and under == 0
            and sum(c) >= MIN_POOLED_TRADES
        )
        results.append(
            {
                "oos_months": months,
                "n_folds": len(c),
                "pooled_events": sum(c),
                "min_fold_events": min(c) if c else 0,
                "folds_under_floor": under,
                "satisfies_v21": ok,
                "ranges": [(str(a.date()), str(b.date())) for a, b in ranges],
                "per_fold": c,
            }
        )
        print(f"  {months:2d} months: folds={len(c)} pooled={sum(c):3d} "
              f"min_fold={min(c) if c else 0:3d} under={under} "
              f"{'SATISFIES V2.1' if ok else 'insufficient'}")
        print(f"             per-fold {c}")

    eligible = [r for r in results if r["satisfies_v21"]]
    if not eligible:
        print("\nNO GEOMETRY SATISFIES THE FROZEN GATES.")
        print("The honest conclusion is that this hypothesis cannot be evaluated at the")
        print("required evidence level on this much data, not that the gates should move.")
        chosen = None
    else:
        # Shortest out-of-sample span that clears the floor: more folds is more evidence,
        # and a longer span than necessary buys nothing while hiding regime variation.
        chosen = min(eligible, key=lambda r: r["oos_months"])
        print(f"\nCHOSEN: {chosen['oos_months']}-month folds, {chosen['n_folds']} folds, "
              f"{chosen['pooled_events']} pooled up-pulses, min fold {chosen['min_fold_events']}")

    block = {
        "designed_utc": pd.Timestamp.utcnow().isoformat(),
        "basis": "event counts only; no performance statistic was computed",
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "train_end": TRAIN_END,
        "up_pulses_total": int(len(up)),
        "up_pulses_per_year": round(len(up) / span_years, 2),
        "floor_trades_per_fold": MIN_TRADES_PER_FOLD,
        "floor_pooled_trades": MIN_POOLED_TRADES,
        "floor_folds": MIN_FOLDS,
        "existing_geometry_per_fold": counts,
        "candidates": [{k: v for k, v in r.items() if k != "ranges"} for r in results],
        "chosen": chosen,
    }
    payload = json.dumps(block, sort_keys=True, default=str)
    block["design_hash"] = hashlib.sha256(payload.encode()).hexdigest()[:16]

    out = "artifacts/reports/pulse_fold_design.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(block, fh, indent=2, default=str)
    print(f"\ndesign hash {block['design_hash']} -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
