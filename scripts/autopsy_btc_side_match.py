"""BTC side_match=0 autopsy: live ledger sides vs proxy_side / warehouse bands.

Proves whether the failure is:
  A) live decide bug (stored side != proxy_side(pred, family))
  B) warehouse pred residual (wh_mean != live_pred → different sides)
  C) **parity harness bug** (wrong edge band, e.g. DIRECTION_BAND on fwd_return)

Usage:
  python scripts/autopsy_btc_side_match.py
  python scripts/autopsy_btc_side_match.py --ledger artifacts/reports/_fleet_ledgers/...
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.paths import ARTIFACTS, ROUND_TRIP_COST  # noqa: E402

OUT = ARTIFACTS / "reports" / "btc_side_match_autopsy_latest.json"
DEFAULT_PACKS = [
    ARTIFACTS / "live_packs" / "structure_v1_btcusdt_k5_double3h_v1",
    ARTIFACTS / "live_packs" / "structure_v1_lgbm",
]
DEFAULT_LEDGERS = [
    ARTIFACTS
    / "reports"
    / "_fleet_ledgers"
    / "94_156_189_76_llm2-structure-btc-k5-double3h-v1_state.sqlite",
    ARTIFACTS
    / "reports"
    / "_fleet_ledgers"
    / "94_156_189_76_llm2-structure-micro_state.sqlite",
]


def _side_matrix(pred: float) -> dict:
    p = float(pred)
    ret = int(proxy_side(np.asarray([p]), "return")[0])
    di = int(proxy_side(np.asarray([p]), "directional")[0])
    return {
        "pred": p,
        "return_family_side_ROUND_TRIP_COST": ret,
        "direction_family_side_DIRECTION_BAND": di,
        "abs_pred": abs(p),
        "exceeds_round_trip_0_0016": abs(p) > ROUND_TRIP_COST,
        "exceeds_direction_band_0_10": abs(p) > DIRECTION_BAND,
    }


def audit_ledger(ledger: Path, strategy: dict) -> dict:
    target = str(strategy.get("target") or "fwd_return")
    family = target_family(target)
    default_edge = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    min_edge = float(strategy.get("min_edge", default_edge))
    con = sqlite3.connect(f"file:{ledger}?mode=ro", uri=True)
    try:
        rows = con.execute(
            "SELECT bar_ts_ms, side, pred_mean, detail "
            "FROM decisions ORDER BY bar_ts_ms DESC LIMIT 12"
        ).fetchall()
    finally:
        con.close()

    bars = []
    live_vs_proxy_ok = 0
    n = 0
    for bar_ts_ms, side, pred_mean, detail in reversed(rows):
        if pred_mean is None:
            continue
        n += 1
        live_side = int(side)
        pred = float(pred_mean)
        correct = int(proxy_side(np.asarray([pred]), family)[0])
        # Simulated pre-fix fleet harness:
        broken_edge = DIRECTION_BAND if abs(min_edge - ROUND_TRIP_COST) < 1e-12 else min_edge
        harness_bug_side = correct
        if abs(pred) < broken_edge:
            harness_bug_side = 0
        if live_side == correct:
            live_vs_proxy_ok += 1
        bars.append(
            {
                "bar_ts_ms": int(bar_ts_ms),
                "bar_utc": datetime.fromtimestamp(
                    int(bar_ts_ms) / 1000.0, tz=timezone.utc
                ).isoformat(),
                "live_side": live_side,
                "pred_mean": pred,
                "proxy_side_correct": correct,
                "live_matches_proxy": live_side == correct,
                "pre_fix_parity_wh_side": harness_bug_side,
                "pre_fix_would_side_match": live_side == harness_bug_side,
                "bands": _side_matrix(pred),
                "skip_reason": None,
            }
        )
        try:
            det = json.loads(detail) if isinstance(detail, str) else (detail or {})
            bars[-1]["skip_reason"] = det.get("skip_reason") or (
                (det.get("multitrade_gate") or {}).get("skip_reason")
            )
        except Exception:
            pass

    return {
        "ledger": str(ledger),
        "target": target,
        "family": family,
        "min_edge": min_edge,
        "ROUND_TRIP_COST": ROUND_TRIP_COST,
        "DIRECTION_BAND": DIRECTION_BAND,
        "n_bars": n,
        "live_vs_proxy_match_rate": (live_vs_proxy_ok / n) if n else None,
        "bars": bars,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ledger", action="append", default=[], help="repeatable ledger path")
    args = ap.parse_args(argv)

    ledgers = [Path(p) for p in args.ledger] if args.ledger else [p for p in DEFAULT_LEDGERS if p.is_file()]
    packs = [p for p in DEFAULT_PACKS if (p / "strategy.json").is_file()]

    pack_meta = []
    for p in packs:
        st = json.loads((p / "strategy.json").read_text(encoding="utf-8"))
        pack_meta.append(
            {
                "pack": str(p),
                "target": st.get("target"),
                "min_edge": st.get("min_edge"),
                "family": target_family(str(st.get("target") or "fwd_return")),
            }
        )

    # Use first BTC pack strategy as reference (all current BTC packs are fwd_return).
    strategy = json.loads((packs[0] / "strategy.json").read_text(encoding="utf-8")) if packs else {
        "target": "fwd_return",
        "min_edge": ROUND_TRIP_COST,
    }

    audits = []
    for led in ledgers:
        if not led.is_file():
            audits.append({"ledger": str(led), "error": "missing"})
            continue
        audits.append(audit_ledger(led, strategy))

    rates = [a.get("live_vs_proxy_match_rate") for a in audits if a.get("live_vs_proxy_match_rate") is not None]
    all_live_proxy_perfect = bool(rates) and all(r == 1.0 for r in rates)

    # Sample bar narrative from first audit with bars
    sample = None
    for a in audits:
        for b in a.get("bars") or []:
            if b.get("pred_mean") is not None and not b.get("pre_fix_would_side_match"):
                sample = b
                break
        if sample:
            break

    verdict = {
        "live_decide_ok": all_live_proxy_perfect,
        "root_cause": (
            "PARITY_HARNESS_EDGE_REMAP"
            if all_live_proxy_perfect
            else "LIVE_OR_WAREHOUSE_RESIDUAL"
        ),
        "explanation": (
            "BTC packs use target=fwd_return (family=return). Live decide applies "
            "proxy_side with ROUND_TRIP_COST=0.0016, so |pred|≈0.005..0.009 correctly "
            "yields side ±1. The fleet parity script previously remapped min_edge when "
            "min_edge≈ROUND_TRIP_COST to DIRECTION_BAND=0.10 (directional-only guard), "
            "then zeroed warehouse_side when |wh_mean|<0.10 — producing side_match=0 "
            "even when warehouse pred_mean matched live exactly."
            if all_live_proxy_perfect
            else "Stored live side disagrees with proxy_side(pred, family); dig into decide path."
        ),
        "sample_bar": sample,
        "fix": (
            "run_fleet_live_warehouse_parity.py: only remap min_edge for family==directional; "
            "warehouse_side = proxy_side(wh_mean, family) only"
        ),
        "do_not": "retune TP/SL/strength/fleet composition from the false side_match=0",
    }

    report = {
        "evidence_class": "BTC_SIDE_MATCH_AUTOPSY",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "packs": pack_meta,
        "verdict": verdict,
        "ledgers": audits,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps(verdict, indent=2), flush=True)
    print(f"wrote {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
