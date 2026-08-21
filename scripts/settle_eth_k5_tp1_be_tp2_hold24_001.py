"""Frozen outer-OOS settle: ETH K5 control vs TP1/BE/TP2 fixed hold-24.

RESEARCH_ONLY. Uses the shared botsgeneral tradesim engine. The 24-bar timer
starts at entry; this is not a post-TP1 extension/reset.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from llm2.evidence.pack_registry import ensure_registry_schema, register_compare_report
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START
from llm2.research_policy import stamp_min_size_equity_caveat
from llm2.signals.singlebook_clarity import SingleBookArm
from llm2.signals.tp_ladder import attach_tp1_be_tp2_hold24

# Reuse the canonical, already-settled ETH K5 outer-fold construction and
# tradesim invocation; only the frozen Signal exit geometry changes.
import scripts.settle_eth_k5_ev_calibrated_pi_star_001 as base

GEN = "structure_v1_eth_k5_tp1_be_tp2_hold24_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN}.yaml"
CONTROL_LABEL = f"{GEN}_control_hold12"
CANDIDATE_LABEL = f"{GEN}_tp1_be_tp2_hold24"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _finite(value):
    if value is None:
        return None
    try:
        value = float(value)
    except (TypeError, ValueError):
        return value
    return value if math.isfinite(value) else None


def _stitch_control() -> dict:
    base.ARM = SingleBookArm(
        clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=0.02
    )
    base.GEN = GEN
    return base.stitch_arm(use_calibration=False, label=CONTROL_LABEL)


def _stitch_ladder() -> dict:
    base.ARM = SingleBookArm(
        clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=0.02
    )
    base.GEN = GEN
    original = base.build_cluster_size_signals

    def _ladder_builder(*args, **kwargs):
        signals, stats = original(*args, **kwargs)
        return attach_tp1_be_tp2_hold24(signals), stats

    base.build_cluster_size_signals = _ladder_builder
    try:
        return base.stitch_arm(use_calibration=False, label=CANDIDATE_LABEL)
    finally:
        base.build_cluster_size_signals = original


def main() -> int:
    if not PREREG.is_file():
        raise SystemExit(f"missing preregistration: {PREREG}")
    prereg_sha = _sha(PREREG)
    t0 = time.perf_counter()

    conf = base.run_conformance_check()
    if not conf.get("passed"):
        raise RuntimeError("tradesim conformance failed")
    import tradesim

    if "botsgeneral" not in str(tradesim.__file__).lower():
        raise RuntimeError("refuse non-botsgeneral tradesim")
    ensure_registry_schema()

    print(f"[{GEN}] control hold12 …", flush=True)
    control = _stitch_control()
    print(
        f"  control n={control['stitched']['n_trades']} "
        f"PF={control['stitched']['profit_factor']} "
        f"exp_ru={control['stitched']['expectancy_return_units']}",
        flush=True,
    )
    print(f"[{GEN}] TP1/BE/TP2 fixed hold24 …", flush=True)
    candidate = _stitch_ladder()
    print(
        f"  candidate n={candidate['stitched']['n_trades']} "
        f"PF={candidate['stitched']['profit_factor']} "
        f"exp_ru={candidate['stitched']['expectancy_return_units']}",
        flush=True,
    )

    c = control["stitched"]
    k = candidate["stitched"]
    c_exp, k_exp = _finite(c["expectancy_return_units"]), _finite(
        k["expectancy_return_units"]
    )
    c_pf, k_pf = _finite(c["profit_factor"]), _finite(k["profit_factor"])
    beat = c_exp is not None and k_exp is not None and k_exp > c_exp
    pf_ok = k_pf is not None and k_pf >= 1.20
    no_liq = int(k["n_liquidations"]) == 0
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": stamp,
            "preregister_path": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
            "preregister_sha256": prereg_sha,
            "evidence_class": "OUTER_TRANSFER_COMPARE",
            "max_readiness": "RESEARCH_ONLY",
            "promotion_allowed": False,
            "live_deploy": "FORBIDDEN",
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "primary_metric": "expectancy_return_units",
            "conformance": conf,
            "geometry": {
                "control": "single TP=1%, SL=2%, hold=12",
                "candidate": (
                    "50% TP1=1%, BE after TP1 (effective next bar), "
                    "50% TP2=2%, initial SL=2%, fixed hold=24 from entry"
                ),
                "post_tp1_hold_reset_supported": False,
            },
            "control": control,
            "candidate": candidate,
            "compare": {
                "control_expectancy_return_units": c_exp,
                "candidate_expectancy_return_units": k_exp,
                "exp_ru_delta": None if c_exp is None or k_exp is None else k_exp - c_exp,
                "control_pf": c_pf,
                "candidate_pf": k_pf,
                "candidate_beats_control_exp_ru": beat,
                "candidate_pf_ge_1_20": pf_ok,
                "candidate_no_liquidation": no_liq,
                "passed_success_criteria": bool(beat and pf_ok and no_liq),
            },
            "elapsed_sec": round(time.perf_counter() - t0, 1),
        }
    )
    out = ARTIFACTS / "reports"
    out.mkdir(parents=True, exist_ok=True)
    latest = out / f"{GEN}_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (out / f"{GEN}_{stamp}.json").write_text(latest.read_text(encoding="utf-8"), encoding="utf-8")

    text = PREREG.read_text(encoding="utf-8")
    PREREG.write_text(
        text.replace(
            "status: FROZEN",
            f"status: OOS_COMPARE_COMPLETE\nsettled_utc: \"{stamp}\"\npreregister_sha256_at_run: {prereg_sha}",
            1,
        ),
        encoding="utf-8",
    )
    register_compare_report(
        GEN,
        report_path=latest,
        control_metrics=c,
        candidate_metrics=k,
        # This research-only overlay must not mutate/refresh the live control pack.
        # That pack predates FOUR_PROOF metadata, so attaching evidence would
        # correctly fail closed in register_freeze.
        control_version_id=None,
        candidate_version_id=None,
    )
    print(f"WROTE {latest}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
