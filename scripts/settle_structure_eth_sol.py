"""Full-gate settle for ETH/SOL structure_v1 tier-2 proxy screens (fold geometry V2)."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

from llm2.gates.v21 import format_gates_table
from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt
from llm2.paths import ARTIFACTS
from llm2.registry.ledger import append_ledger
from llm2.research_policy import stamp_min_size_equity_caveat
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, OUTER_FOLD_RANGES

# Proxy tier≥2 from structure_v1_hunt_20260803T160026Z — settle once, no retune.
COMBOS = (
    ("ETHUSDT", "1h", "fwd_return"),
    ("ETHUSDT", "1h", "direction"),
    ("SOLUSDT", "1h", "fwd_return"),
    ("SOLUSDT", "1h", "direction"),
)


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = ARTIFACTS / "reports" / f"structure_v1_eth_sol_settle_{stamp}.json"
    rows = []
    best_overall = None
    for i, (sym, tf, tgt) in enumerate(COMBOS):
        gid = f"settle_struct2_{i:02d}_{sym}_{tf}_{tgt}_{stamp[:8]}"
        append_ledger(
            f"STRUCTURE_ETH_SOL_SETTLE start {gid} fold={FOLD_GEOMETRY_VERSION}",
            tier=0,
        )
        cfg = HuntConfig(
            generation_id=gid,
            symbol=sym,
            timeframe=tf,
            target=tgt,
            feature_space="structure_v1",
            horizon=DEFAULT_HORIZON[tgt],
            max_trials=4,
            seed=20260803 + i,
            run_backtest=True,
            run_surrogate_challenge=True,
            models=["hist_mean", "ridge", "lgbm_regressor", "lgbm_classifier"],
            tp_pct=0.01,
            sl_pct=0.02,
        )
        summary = run_nested_hunt(cfg)
        best = summary.get("best") or {}
        gates = best.get("gates") or {}
        row = {
            "symbol": sym,
            "timeframe": tf,
            "target": tgt,
            "generation_id": gid,
            "tier": best.get("tier") or summary.get("best_tier"),
            "pooled_pf": best.get("pooled_pf"),
            "pooled_trades": best.get("pooled_trades"),
            "overall": gates.get("overall"),
            "gates": gates,
            "model": best.get("model"),
        }
        rows.append(row)
        print(
            f"{sym} {tf} {tgt}: tier={row['tier']} pf={row['pooled_pf']} "
            f"overall={row['overall']}",
            flush=True,
        )
        print(format_gates_table(gates), flush=True)
        if row["overall"] == "PASS" and (
            best_overall is None
            or float(row["pooled_pf"] or 0) > float(best_overall.get("pooled_pf") or 0)
        ):
            best_overall = row

    payload = stamp_min_size_equity_caveat(
        {
            "stamped_utc": stamp,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "readiness": "RESEARCH_ONLY",
            "vps_deploy": "FORBIDDEN_without_separate_live_pack_and_auth",
            "combos": rows,
            "best_pass": best_overall,
            "note": (
                "ETH/SOL settles are research evidence only. Do not deploy on Xxobster7 "
                "without a frozen pack + certificate naming that symbol."
            ),
        }
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    print(f"wrote {out_path}", flush=True)
    append_ledger(
        f"STRUCTURE_ETH_SOL_SETTLE done best_pass={bool(best_overall)} path={out_path}",
        tier=2 if best_overall else 0,
    )
    return 0 if best_overall else 2


if __name__ == "__main__":
    raise SystemExit(main())
