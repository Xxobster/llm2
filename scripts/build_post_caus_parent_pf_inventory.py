"""Build post-CAUS parent Profit Factor inventory (one-shot helper)."""

from __future__ import annotations

import json
from pathlib import Path

from llm2.paths import ARTIFACTS

REPORTS = ARTIFACTS / "reports"


def _rows_from(path: Path) -> tuple[str, list[dict]]:
    r = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for h in r.get("rows") or []:
        gates = h.get("gates") or {}
        rows.append(
            {
                "symbol": h.get("symbol"),
                "target": h.get("target"),
                "timeframe": h.get("timeframe") or "1h",
                "pooled_pf": float(h.get("pooled_pf")),
                "overall": h.get("overall"),
                "feature_space": h.get("feature_space")
                or r.get("feature_space")
                or "structure_v1",
                "daily_mtm_sharpe": gates.get("daily_mtm_sharpe_value"),
            }
        )
    return str(r.get("generation_id")), rows


def main() -> int:
    parents: list[dict] = []
    for name in (
        "structure_v1_caus_retrain_001_latest.json",
        "structure_v1_causal_drop_retrace_001_latest.json",
    ):
        path = REPORTS / name
        gid, rows = _rows_from(path)
        for x in rows:
            parents.append({"parent_generation": gid, **x})

    nest = json.loads(
        (REPORTS / "structure_v1_forecast_filter_on_direction_001_latest.json").read_text(
            encoding="utf-8"
        )
    )
    nest_arms = []
    for s in nest.get("symbols") or []:
        for arm, blob in (s.get("arms") or {}).items():
            nest_arms.append(
                {
                    "symbol": s.get("symbol"),
                    "arm": arm,
                    "mean_fold_pf": blob.get("mean_fold_pf"),
                    "sum_net_pnl": blob.get("sum_net_pnl"),
                    "n_signals": blob.get("n_signals"),
                }
            )

    s1 = json.loads(
        (REPORTS / "structure_v1_next_retrace_forecast_001_latest.json").read_text(
            encoding="utf-8"
        )
    )
    stage2 = []
    for s in s1.get("stage2_trade_rule") or []:
        m = s.get("metrics") or {}
        stage2.append(
            {
                "symbol": s.get("symbol"),
                "status": s.get("status"),
                "profit_factor": m.get("profit_factor"),
            }
        )

    pfs = [p["pooled_pf"] for p in parents]
    nest_pfs = [float(a["mean_fold_pf"]) for a in nest_arms if a.get("mean_fold_pf") is not None]
    inv = {
        "inventory_id": "post_caus_parent_pf_inventory_001",
        "created_utc": "2026-08-08T00:00:00Z",
        "decision": "D-060",
        "question": (
            "Any post-CAUS-STRUCT-001 parent with causal outer Profit Factor (PF) "
            ">= 1.0 suitable for nesting filters?"
        ),
        "answer": "NO",
        "min_pooled_pf_observed": min(pfs) if pfs else None,
        "max_pooled_pf_observed": max(pfs) if pfs else None,
        "max_nest_mean_fold_pf": max(nest_pfs) if nest_pfs else None,
        "parents_hunt_rows": parents,
        "forecast_stage2_naive": stage2,
        "forecast_filter_nest_arms": nest_arms,
        "conclusion": (
            "No positive outer PF parent post-CAUS for structure_v1 / "
            "structure_v1_no_retrace direction@1h or fwd_return@1h. "
            "Nesting filters cannot create readyability. "
            "Shift research off structure_v1 direction@1h parent family for trading; "
            "forecast skill of next_retrace remains a separate non-promotable claim."
        ),
        "readiness_max": "RESEARCH_ONLY",
    }
    out = REPORTS / "post_caus_parent_pf_inventory_001.json"
    out.write_text(json.dumps(inv, indent=2), encoding="utf-8")
    print(json.dumps({k: inv[k] for k in ("answer", "min_pooled_pf_observed", "max_pooled_pf_observed", "max_nest_mean_fold_pf", "conclusion")}, indent=2))
    print(f"WROTE {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
