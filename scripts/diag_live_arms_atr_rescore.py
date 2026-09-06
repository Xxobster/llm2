"""Diagnostic: how much of the two LIVE arms' edge survives a wider stop?

This is **not** a search for a better bracket and it must not be used to pick one.
It answers one question, and reports it whatever the answer is.

Hunt 002 established across 10,269 arms that a stop tight enough to be hit inside
the entry candle inflates profit factor, and that widening it drives profit factor
toward 1.0 monotonically. Both live diagonal S/R arms show that signature in their
own frozen evidence: profit factor correlates with entry-bar exit rate at +0.771
Spearman across their six outer folds, and the Solana arm's pooled entry-bar rate
of 0.469 breaches its own preregistered 0.35 cap.

So: re-score the *same* events, on the *same* outer out-of-sample folds, with the
*same* limit entry prices, changing only the bracket from fixed 1.5% / 1.0% to a
stop scaled by Average True Range. Reward-to-risk is held at 1.5 throughout, so
the geometry that made the live pack attractive is unchanged and the only moving
part is how far the stop sits from entry.

Read the result this way: if profit factor holds up as the entry-bar exit rate
falls below 0.25, the live edge is real. If profit factor decays toward 1.0 as the
entry-bar rate falls, the live edge was the artifact.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from llm2.diagonal_sr.events import MARKET_ENTRY_EVENTS  # noqa: E402
from llm2.edge_lab.sim_atr import run_atr_bracket_arm  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402

sys.path.insert(0, str(_ROOT / "scripts"))
from run_diagonal_sr_nested_settle_001 import _Ctx, _side  # noqa: E402

# The two arms live on Xxobster4 right now.
LIVE_ARMS = [
    {"symbol": "ETHUSDT", "timeframe": "1h", "generation": "A", "event": "bounce_upper",
     "live_tp": 0.015, "live_sl": 0.01, "live_pf": 1.3524, "live_ebr": 0.2604},
    {"symbol": "SOLUSDT", "timeframe": "1h", "generation": "A", "event": "bounce_upper",
     "live_tp": 0.015, "live_sl": 0.01, "live_pf": 1.9651, "live_ebr": 0.4694},
]
K_SL_GRID = [1.0, 1.5, 2.0, 2.5, 3.0]
TP_RATIO = 1.5  # identical reward-to-risk to the live pack (1.5% against 1.0%)
WORK = {"1h": 3}
MAX_HOLD = {"1h": 8}
OUT = ARTIFACTS / "reports" / "diagonal_sr"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--per-fold", action="store_true", help="also score each outer fold")
    args = ap.parse_args()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    results = []

    for arm in LIVE_ARMS:
        key = (arm["symbol"], arm["timeframe"], arm["generation"])
        print(f"\n=== context {key} ===", flush=True)
        ctx = _Ctx(*key)
        event = arm["event"]
        occ = ctx.pack.occurrence[event].to_numpy(dtype=float) >= 0.5
        side = _side(event, len(ctx.ohlcv))
        base = occ & (side != 0)
        market = event in MARKET_ENTRY_EVENTS

        print(f"  outer folds={len(ctx.folds)} oos_bars={int(ctx.oos_union.sum())} "
              f"event_bars_in_oos={int((base & ctx.oos_union).sum())}", flush=True)
        print(f"\n  LIVE PACK (fixed tp{arm['live_tp']} sl{arm['live_sl']}): "
              f"PF={arm['live_pf']:.3f} entry_bar_rate={arm['live_ebr']:.3f}")
        print(f"\n  {'k_sl':>5} {'stop%':>7} {'n':>5} {'PF':>7} {'Sharpe':>8} {'HAC':>7} "
              f"{'ebr':>6} {'hold':>6} {'WR':>6} {'fill':>6}")

        for k_sl in K_SL_GRID:
            mask = base & ctx.oos_union
            is_short = (side < 0)[np.flatnonzero(mask)]
            tag = f"{arm['symbol']}|1h|{event}|atr_ksl{k_sl}|r{TP_RATIO}|stitched"
            try:
                r = run_atr_bracket_arm(
                    arm["symbol"], ctx.sc, mask, is_short,
                    tag=tag, market=market,
                    work=WORK[arm["timeframe"]], max_hold=MAX_HOLD[arm["timeframe"]],
                    k_sl=k_sl, tp_ratio=TP_RATIO,
                )
            except Exception as exc:  # noqa: BLE001
                print(f"  {k_sl:>5} ERROR {exc}", flush=True)
                continue
            if str(r.get("status")) != "RAN":
                print(f"  {k_sl:>5} {r.get('status')}", flush=True)
                continue

            def g(k, d=float("nan")):
                try:
                    return float(r.get(k))
                except (TypeError, ValueError):
                    return d

            print(
                f"  {k_sl:>5} {g('sl_pct_mean') * 100:>6.2f}% {int(g('n_trades')):>5} "
                f"{g('profit_factor'):>7.3f} {g('sharpe_annualised'):>8.2f} "
                f"{g('sharpe_hac_annualised'):>7.2f} {g('entry_bar_exit_rate'):>6.3f} "
                f"{g('avg_hold_bars'):>6.2f} {g('win_rate'):>6.3f} {g('fill_pct'):>6.2f}",
                flush=True,
            )
            r.update({**{k: v for k, v in arm.items()}, "k_sl": k_sl, "tp_ratio": TP_RATIO,
                      "kind": "stitched"})
            results.append(r)

        if args.per_fold:
            for k_sl in (1.5, 2.0):
                print(f"\n  per-fold at k_sl={k_sl}:")
                for fo in ctx.folds:
                    w = (ctx.sc.ts_ms >= fo.oos_start_ms) & (ctx.sc.ts_ms < fo.oos_end_ms)
                    mask = base & w
                    is_short = (side < 0)[np.flatnonzero(mask)]
                    try:
                        r = run_atr_bracket_arm(
                            arm["symbol"], ctx.sc, mask, is_short,
                            tag=f"{tag}|fold{fo.fold_index}", market=market,
                            work=WORK["1h"], max_hold=MAX_HOLD["1h"],
                            k_sl=k_sl, tp_ratio=TP_RATIO,
                        )
                    except Exception as exc:  # noqa: BLE001
                        print(f"    fold{fo.fold_index} ERROR {exc}")
                        continue
                    if str(r.get("status")) != "RAN":
                        print(f"    fold{fo.fold_index} {r.get('status')}")
                        continue
                    print(f"    fold{fo.fold_index} n={int(r['n_trades']):4d} "
                          f"PF={float(r['profit_factor']):6.3f} "
                          f"ebr={float(r['entry_bar_exit_rate']):.3f}")
                    r.update({**arm, "k_sl": k_sl, "tp_ratio": TP_RATIO,
                              "kind": "fold", "fold_index": fo.fold_index})
                    results.append(r)

        del ctx

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "live_arms_atr_rescore_latest.json"
    path.write_text(
        json.dumps(
            {
                "diagnostic_id": "diagonal_sr_live_arms_atr_rescore",
                "stamp": stamp,
                "purpose": "measure how much live-arm profit factor survives a stop "
                           "wide enough to escape single-bar noise",
                "not_a_selection": True,
                "readiness_effect": "can only invalidate, never promote",
                "tp_ratio_held_constant": TP_RATIO,
                "k_sl_grid": K_SL_GRID,
                "rows": results,
            },
            default=str,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"\nWROTE {path} rows={len(results)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
