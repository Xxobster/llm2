"""Settle structure_v1 on fold geometry V2 (through lockbox start) with full V2.1 gates.

Prereg: configs/preregister/structure_v1_fold_extension_001.yaml (D-033).
Does NOT authorize VPS deploy — writes a research pack scaffold + blocked certificate check.
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from llm2.gates.v21 import format_gates_table
from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt
from llm2.live.certificate import (
    refuse_vps_deploy_without_live_certificate,
    write_pack_scaffold,
)
from llm2.paths import ARTIFACTS, ROOT
from llm2.registry.ledger import append_ledger
from llm2.research_policy import PolicyError, stamp_min_size_equity_caveat
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, OUTER_FOLD_RANGES

GENERATION = "autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1"
SETTLEMENT_PATH = ARTIFACTS / "reports" / "structure_v1_tier2_settlement.json"
PREREG = ROOT / "configs" / "preregister" / "structure_v1_fold_extension_001.yaml"


def main() -> int:
    leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
    if leak.is_dir() and str(leak) not in sys.path:
        sys.path.insert(0, str(leak))

    # Explicitly refuse VPS as part of this settle path.
    try:
        refuse_vps_deploy_without_live_certificate(host="94.156.189.76")
    except PolicyError as exc:
        append_ledger(f"VPS_REFUSED_AS_EXPECTED: {exc}", tier=0)
        print(f"VPS deploy blocked (expected): {exc}")

    prereg_sha = hashlib.sha256(PREREG.read_text(encoding="utf-8").encode()).hexdigest()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    gid = f"{GENERATION}__settle_v2_{stamp[:8]}"
    append_ledger(
        f"STRUCTURE_TIER2_SETTLE_V2 start fold_geometry={FOLD_GEOMETRY_VERSION} "
        f"n_folds={len(OUTER_FOLD_RANGES)} prereg_sha={prereg_sha[:16]} run={gid}",
        tier=0,
    )

    cfg = HuntConfig(
        generation_id=gid,
        symbol="BTCUSDT",
        timeframe="1h",
        target="fwd_return",
        feature_space="structure_v1",
        horizon=DEFAULT_HORIZON["fwd_return"],
        max_trials=4,
        seed=20260803,
        run_backtest=True,
        run_surrogate_challenge=True,
        models=["hist_mean", "ridge", "lgbm_regressor", "lgbm_classifier"],
        tp_pct=0.01,
        sl_pct=0.02,
    )
    summary = run_nested_hunt(cfg)
    best = summary.get("best") or {}
    gates = best.get("gates") or {}
    overall = gates.get("overall", "UNKNOWN")
    tier = int(best.get("tier") or summary.get("best_tier") or 0)

    unbound = [
        k
        for k in (
            "stress_pnl",
            "stress_pf",
            "baseline_mdd",
            "stress_mdd",
            "margin_utilization",
        )
        if gates.get(k) == "UNKNOWN"
    ]
    settled = overall in ("PASS", "FAIL") and not unbound
    verdict = (
        "SHADOW_READY_CANDIDATE"
        if settled and overall == "PASS" and tier >= 2
        else ("SETTLED_FAIL" if settled and overall == "FAIL" else "UNSETTLED")
    )

    payload = {
        "base_generation": GENERATION,
        "settle_generation": gid,
        "stamped_utc": stamp,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES,
        "prereg_path": str(PREREG),
        "prereg_sha256_text": prereg_sha,
        "verdict": verdict,
        "settled": settled,
        "allow_resume_other_structure_combos": settled,
        "overall": overall,
        "tier": tier,
        "pooled_pf": best.get("pooled_pf"),
        "gates": gates,
        "readiness": "RESEARCH_ONLY",
        "shadow_ready_candidate": verdict == "SHADOW_READY_CANDIDATE",
        "vps_deploy": "FORBIDDEN_without_live_certificate",
        "abc_bounce": "UNDERPOWERED_HOLD_untouched",
        "leakage": "botsgeneral leakage + structure confirmation-time tests required",
        "note": (
            "Fold V2 closes Oct-2025→lockbox gap. Live/VPS still blocked. "
            "Use per-fold Finplot with trade cap for readable markers."
        ),
    }
    payload = stamp_min_size_equity_caveat(payload)
    SETTLEMENT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SETTLEMENT_PATH.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    SETTLEMENT_PATH.with_suffix(".md").write_text(
        f"# structure_v1 settle fold {FOLD_GEOMETRY_VERSION} ({stamp})\n\n"
        f"**Verdict:** `{verdict}` · overall=`{overall}` · tier={tier} · "
        f"pooled_pf={best.get('pooled_pf')}\n\n"
        f"VPS deploy: FORBIDDEN without live certificate.\n\n"
        f"{format_gates_table(gates)}\n",
        encoding="utf-8",
    )
    pack = write_pack_scaffold(settlement=payload)
    append_ledger(
        f"STRUCTURE_TIER2_SETTLE_V2 {verdict} overall={overall} tier={tier} "
        f"pf={best.get('pooled_pf')} pack={pack}",
        tier=tier if tier >= 2 else 0,
    )
    print(format_gates_table(gates))
    print(f"\nverdict={verdict} settled={settled} wrote {SETTLEMENT_PATH}")
    print(f"research pack scaffold: {pack} (not deployable)")
    if verdict == "SHADOW_READY_CANDIDATE":
        return 2
    if not settled:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
