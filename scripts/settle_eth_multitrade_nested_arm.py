"""Run a frozen eth_multitrade nested arm vs live control (outer folds only).

Usage:
  python scripts/settle_eth_multitrade_nested_arm.py --generation primary_clarity_all
  python scripts/settle_eth_multitrade_nested_arm.py --generation shorter_hold
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.experiments.eth_multitrade_nested import (  # noqa: E402
    live_control_cfg,
    stitch_arm,
)
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, OUTER_FOLD_RANGES  # noqa: E402

GENS = {
    "primary_clarity_all": {
        "generation_id": "structure_v1_eth_multitrade_primary_clarity_all_001",
        "evidence_class": "OUTER_TRANSFER_COMPARE",
        "promotion_allowed_if_pass": False,
        "candidate_overrides": {"clarity_scope": "all"},
        "success_needs_pf_beat": True,
    },
    "shorter_hold": {
        "generation_id": "structure_v1_eth_multitrade_shorter_hold_001",
        "evidence_class": "OUTER_COMPARE_CONTAMINATED",
        "promotion_allowed_if_pass": False,
        "candidate_overrides": {"base_hold": 4, "hold_addon": 8},
        "success_needs_pf_beat": False,  # diagnostic only
    },
}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--generation", required=True, choices=sorted(GENS))
    args = ap.parse_args()
    spec = GENS[args.generation]
    gen_id = spec["generation_id"]
    prereg = _ROOT / "configs" / "preregister" / f"{gen_id}.yaml"
    if not prereg.is_file():
        raise SystemExit(f"missing preregister {prereg}")
    prereg_sha = _sha(prereg)

    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")

    control_cfg = live_control_cfg()
    cand_cfg = dict(control_cfg)
    cand_cfg.update(spec["candidate_overrides"])

    print(f"[{gen_id}] control stitch …", flush=True)
    control = stitch_arm(control_cfg, label=f"{gen_id}_control")
    print(
        f"  control PF={control['stitched']['profit_factor']:.3f} "
        f"n={control['stitched']['n_trades']} "
        f"book1_wrong1h={control['book1_wrong_way_1h']:.1%}",
        flush=True,
    )
    print(f"[{gen_id}] candidate stitch …", flush=True)
    candidate = stitch_arm(cand_cfg, label=f"{gen_id}_candidate")
    print(
        f"  candidate PF={candidate['stitched']['profit_factor']:.3f} "
        f"n={candidate['stitched']['n_trades']} "
        f"book1_wrong1h={candidate['book1_wrong_way_1h']:.1%}",
        flush=True,
    )

    c_pf = float(candidate["stitched"]["profit_factor"])
    o_pf = float(control["stitched"]["profit_factor"])
    beat = bool(np_isfinite(c_pf) and np_isfinite(o_pf) and c_pf > o_pf)
    no_liq = int(candidate["stitched"]["n_liquidations"]) == 0
    pf_ok = bool(np_isfinite(c_pf) and c_pf >= 1.20)
    passed = bool(beat and pf_ok and no_liq) if spec["success_needs_pf_beat"] else False

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": gen_id,
            "created_utc": stamp,
            "preregister_path": str(prereg.relative_to(_ROOT)).replace("\\", "/"),
            "preregister_sha256": prereg_sha,
            "evidence_class": spec["evidence_class"],
            "max_readiness": "RESEARCH_ONLY",
            "promotion_allowed": False,
            "live_deploy": "FORBIDDEN",
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "conformance_passed": bool(conf.get("passed")),
            "leakage_recheck_ref": (
                "artifacts/reports/structure_v1_leakage_recheck_20260804T144240Z.json"
            ),
            "control": control,
            "candidate": candidate,
            "compare": {
                "candidate_pf": c_pf,
                "control_pf": o_pf,
                "pf_delta": c_pf - o_pf if np_isfinite(c_pf) and np_isfinite(o_pf) else None,
                "candidate_beats_control": beat,
                "candidate_pf_ge_1_20": pf_ok,
                "candidate_no_liquidation": no_liq,
                "book1_wrong_way_1h_control": control["book1_wrong_way_1h"],
                "book1_wrong_way_1h_candidate": candidate["book1_wrong_way_1h"],
                "passed_success_criteria": passed,
            },
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "note": (
                "Nested one-arm vs live control. Not a live pack swap. "
                "shorter_hold is OUTER_COMPARE_CONTAMINATED (failure_modes peek)."
            ),
        }
    )

    out_dir = ARTIFACTS / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    latest = out_dir / f"{gen_id}_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (out_dir / f"{gen_id}_{stamp}.json").write_text(
        latest.read_text(encoding="utf-8"), encoding="utf-8"
    )

    # Annotate prereg status
    text = prereg.read_text(encoding="utf-8")
    if "status: FROZEN" in text:
        text = text.replace(
            "status: FROZEN",
            f"status: OOS_COMPARE_COMPLETE\nsettled_utc: \"{stamp}\"\n"
            f"preregister_sha256_at_run: {prereg_sha}",
            1,
        )
        prereg.write_text(text, encoding="utf-8")

    print(json.dumps(report["compare"], indent=2))
    print(f"wrote {latest}")
    return 0


def np_isfinite(x: float) -> bool:
    import math

    return math.isfinite(float(x))


if __name__ == "__main__":
    raise SystemExit(main())
