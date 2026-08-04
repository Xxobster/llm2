"""Tier-2 review: independent re-run, Finplot, gate table.

Run this, and only this, when the sweep reports a tier >= 2 candidate. It refuses to print
anything quotable unless the tradesim conformance stamp is green, and it re-runs the
candidate from its stored configuration rather than trusting the sweep's own numbers.

    python scripts/tier2_review.py --generation-id auto_017_ETHUSDT_4h_xs_rank_pivot_v1_ts

Nothing here authorises live trading. Under Trading Bot Research Standard v2.1 a passing
review earns SHADOW_READY at most, and operational leverage is set to the lowest value
that clears margin, never the highest the stop distance permits.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from llm2.backtest.conformance import run_conformance_check
from llm2.gates.v21 import format_gates_table
from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt
from llm2.registry.db import ResearchDB


def _candidate(db: ResearchDB, generation_id: str) -> dict:
    trials = [t for t in db.list_trials() if t.get("generation_id") == generation_id]
    if not trials:
        raise SystemExit(f"no trials recorded for generation {generation_id!r}")
    best = max(trials, key=lambda t: (t.get("tier") or 0, t.get("outer_pf") or -1))
    if (best.get("tier") or 0) < 2:
        raise SystemExit(
            f"best trial in {generation_id} is tier {best.get('tier')}; "
            "this protocol is for tier >= 2 only"
        )
    return best


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Tier-2 candidate review")
    ap.add_argument("--generation-id", required=True)
    ap.add_argument("--seed", type=int, default=1337, help="a seed the sweep did not use")
    ap.add_argument("--no-plot", action="store_true")
    args = ap.parse_args(argv)

    db = ResearchDB()
    cand = _candidate(db, args.generation_id)
    print("candidate:", json.dumps(cand, indent=2, default=str))

    print("\n--- conformance ---")
    conf = run_conformance_check(quiet=True)
    stamp = conf.get("stamp") or {}
    print(
        f"stamp: {stamp.get('satisfied_count')}/{stamp.get('required_count')} "
        f"green={conf.get('passed')} commit={stamp.get('engine_commit')}"
    )
    if not conf.get("passed"):
        print(
            "\nconformance is not green: no number below is quotable evidence "
            "(standard section 24.0). Fix the engine before reviewing the candidate.",
            file=sys.stderr,
        )
        return 1
    if stamp.get("engine_commit", "").startswith("UNKNOWN"):
        print(
            "\nNOTE: the engine tree is dirty, so this stamp cannot be attributed to a "
            "commit. Acceptable for research, not for a live-readiness claim.",
            file=sys.stderr,
        )

    print("\n--- independent re-run (fresh seed, tradesim-backed) ---")
    cfg = HuntConfig(
        generation_id=f"{args.generation_id}__review",
        symbol=cand["symbol"],
        timeframe=cand["timeframe"],
        target=cand["target"],
        feature_space=cand["feature_space"],
        horizon=DEFAULT_HORIZON[cand["target"]],
        max_trials=1,
        seed=args.seed,
        run_backtest=True,
        run_surrogate_challenge=True,
        models=[cand["model"]],
    )
    summary = run_nested_hunt(cfg)
    best = summary.get("best") or {}
    print(json.dumps({k: v for k, v in summary.items() if k != "best"}, indent=2, default=str))

    print("\n--- gate table ---")
    if best.get("gates"):
        print(format_gates_table(best["gates"]))

    reproduced = int(best.get("tier") or 0) >= 2
    print(
        f"\nsweep tier={cand.get('tier')} pf={cand.get('outer_pf')}  ->  "
        f"review tier={best.get('tier')} pf={best.get('pooled_pf')}"
    )
    if not reproduced:
        print(
            "\nThe candidate did not reproduce under an independent seed. It is a "
            "selection artefact, not an edge. Record it and move on."
        )
        return 2

    if not args.no_plot:
        print("\n--- finplot ---")
        print(
            "reproduced; re-run the winning fold with plot=True via "
            "llm2.backtest.run.run_strategy_backtest to render the Finplot chart"
        )

    print(
        "\nReproduced. Maximum earned readiness is SHADOW_READY. Live sizing, if it is "
        "ever discussed, uses the lowest operational leverage that clears margin."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
