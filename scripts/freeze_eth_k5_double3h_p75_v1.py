"""Freeze RESEARCH_ONLY ETH K5 double pack with strength_quantile=p75.

Copies model/risk artifacts from live eth_k5_double3h_v1 (same LightGBM /
structure_v1). Only execution knobs + registry differ. No live deploy.
"""

from __future__ import annotations

import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.evidence.pack_registry import (  # noqa: E402
    ensure_registry_schema,
    regenerate_versions_md,
    register_freeze,
)
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.paths import ARTIFACTS, ROOT  # noqa: E402

PARENT = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_k5_double3h_v1"
DST = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_k5_double3h_p75_v1"
VERSION_ID = "eth_k5_double3h_p75_v1"
GEN = "structure_v1_eth_k5_expectancy_strength_p75_001"
REPORT = ARTIFACTS / "reports" / f"{GEN}_latest.json"


def main() -> int:
    if not PARENT.is_dir():
        raise SystemExit(f"missing parent pack {PARENT}")
    if not REPORT.is_file():
        raise SystemExit(f"missing p75 settle report {REPORT}")
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    cand = (report.get("candidate") or {}).get("stitched") or {}
    compare = report.get("compare") or {}
    if not compare.get("passed_success_criteria"):
        print(
            "WARNING: report passed_success_criteria is not true; "
            "still freezing RESEARCH_ONLY pack from prior OUTER_TRANSFER_COMPARE",
            flush=True,
        )

    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(PARENT, DST)

    # Research pack: never ship a live certificate / bind service.
    for name in ("certificate.yaml",):
        p = DST / name
        if p.is_file():
            p.unlink()
    cert_live = ROOT / "configs" / "live" / f"{DST.name}_certificate.yaml"
    # Do not create a certificate — deploy remains forbidden.

    strat_path = DST / "strategy.json"
    strat = json.loads(strat_path.read_text(encoding="utf-8"))
    strat["strategy_id"] = (
        "structure_v1_lgbm_ETHUSDT_1h_direction_k5_double3h_p75_v1"
    )
    strat["version_id"] = VERSION_ID
    strat["version_lineage"] = {
        "parent_pack": "structure_v1_ethusdt_k5_double3h_v1",
        "replaces": None,
        "research_arm": (
            "clarity=mean_strength|hold=12|tp=1%|K=5|double3h|strength_q=0.75"
        ),
        "generation_id": GEN,
        "evidence_class": "OUTER_TRANSFER_COMPARE",
        "note": (
            "Same geometry as eth_k5_double3h_v1 with strength_quantile=0.75. "
            "RESEARCH_ONLY; live deploy FORBIDDEN without certificate + user auth."
        ),
    }
    mt = dict(strat.get("multitrade") or {})
    mt["version_id"] = VERSION_ID
    mt["strength_quantile"] = 0.75
    strat["multitrade"] = mt
    strat["what_it_does"] = (
        "RESEARCH_ONLY p75 strength arm. K=5 books/side; mean_strength on every "
        "entry at q=0.75 of 168-bar |mean| history; TP+1% SL-2% hold12; size 2x "
        "min when same-side entry within 3h. Not live."
    )
    # Strip live account language
    strat.pop("account", None)
    strat_path.write_text(json.dumps(strat, indent=2) + "\n", encoding="utf-8")

    meta = {
        "version_id": VERSION_ID,
        "parent": "structure_v1_ethusdt_k5_double3h_v1",
        "parent_pack": "structure_v1_ethusdt_k5_double3h_v1",
        "research_arm": "mean_strength|hold12|tp1pct|K=5|double3h|q0.75",
        "frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "strategy_id": strat["strategy_id"],
        "status": "FROZEN_RESEARCH_ONLY",
        "readiness": "RESEARCH_ONLY",
        "live": {
            "deployed": False,
            "account_ref": None,
            "service": None,
            "note": "live_deploy FORBIDDEN until certificate + explicit user auth",
        },
        "metrics": {
            "profit_factor": cand.get("profit_factor"),
            "expectancy_return_units": cand.get("expectancy_return_units"),
            "n_trades": cand.get("n_trades"),
            "win_rate": cand.get("win_rate"),
            "window": "outer_v2_hard_end_2026-05-01",
            "source_report": str(REPORT.relative_to(ROOT)).replace("\\", "/"),
        },
        "evidence": {
            "report_paths": [str(REPORT.relative_to(ROOT)).replace("\\", "/")],
            "generation_id": GEN,
            "tradesim_run_ids": list(
                (report.get("candidate") or {}).get("tradesim_run_ids") or []
            ),
        },
    }
    (DST / "pack_meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    (DST / "README.md").write_text(
        f"# {VERSION_ID}\n\n"
        "Frozen RESEARCH_ONLY pack: eth_k5_double3h geometry with "
        "`strength_quantile=0.75`.\n\n"
        f"Evidence: `{GEN}` OUTER_TRANSFER_COMPARE "
        f"(expectancy_return_units beat control).\n\n"
        "**Live deploy FORBIDDEN** without new certificate + explicit user auth.\n",
        encoding="utf-8",
    )

    fp = pack_fingerprint(DST)
    if not fp:
        raise RuntimeError("pack_fingerprint failed")
    (DST / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    meta["pack_hash"] = fp
    (DST / "pack_meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )

    ensure_registry_schema()
    register_freeze(
        DST,
        evidence=meta["evidence"],
        metrics=meta["metrics"],
        status="FROZEN_RESEARCH_ONLY",
        readiness="RESEARCH_ONLY",
        require_run_id=False,
        ledger=True,
    )
    regenerate_versions_md()
    print(
        json.dumps(
            {
                "pack": str(DST.relative_to(ROOT)).replace("\\", "/"),
                "version_id": VERSION_ID,
                "pack_hash": fp,
                "metrics": meta["metrics"],
                "live_deploy": "FORBIDDEN",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
