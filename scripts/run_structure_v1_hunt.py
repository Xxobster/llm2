"""Bounded hunt outside ABC continuation — warehouse structure_v1 feature space.

ABC equal-leg / bounce families are closed or UNDERPOWERED_HOLD. This screen uses the
audited confirmed-swing structure features on directional / return targets only.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ensure botsgeneral leakage is importable before the hunt guard loads.
_leak_src = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak_src.is_dir() and str(_leak_src) not in sys.path:
    sys.path.insert(0, str(_leak_src))

from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt
from llm2.registry.db import ResearchDB
from llm2.registry.ledger import append_ledger
SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT")
TIMEFRAMES = ("1h", "4h")
TARGETS = ("fwd_return", "direction")
SPACE = "structure_v1"
GATE_REVISION = "struct2"


def main() -> int:
    # ABC continuation / bounce are closed or UNDERPOWERED_HOLD — this arm stays outside.
    append_ledger(
        "STRUCTURE_V1_HUNT: ABC continuation CLOSED (D-030); bounce UNDERPOWERED_HOLD "
        "(D-031); hunting audited structure_v1 only; video rules not evidence",
        tier=0,
    )

    from llm2.paths import ARTIFACTS

    settlement = ARTIFACTS / "reports" / "structure_v1_tier2_settlement.json"
    if settlement.is_file():
        import json

        st = json.loads(settlement.read_text(encoding="utf-8"))
        if not st.get("allow_resume_other_structure_combos"):
            print(
                f"HOLD: structure Tier-2 not settled ({st.get('verdict')}). "
                "Run scripts/settle_structure_tier2.py first.",
                flush=True,
            )
            return 5
    else:
        print(
            "HOLD: no structure_v1_tier2_settlement.json — settle autostruct1_00 first "
            "(scripts/settle_structure_tier2.py).",
            flush=True,
        )
        return 5

    db = ResearchDB()
    combos = [
        (sym, tf, tgt)
        for sym in SYMBOLS
        for tf in TIMEFRAMES
        for tgt in TARGETS
    ]
    # Skip the already-settled first combo; resume the other 7.
    combos = [c for c in combos if not (c[0] == "BTCUSDT" and c[1] == "1h" and c[2] == "fwd_return")]
    append_ledger(
        f"STRUCTURE_V1_HUNT start n={len(combos)} space={SPACE} rev={GATE_REVISION}",
        tier=0,
    )
    results = []
    best_tier = 0
    for i, (sym, tf, tgt) in enumerate(combos):
        gid = f"auto{GATE_REVISION}_{i:02d}_{sym}_{tf}_{tgt}_{SPACE}"
        trials = db.list_trials(gid)
        if any(t.get("status") == "completed" for t in trials):
            print(f"[{i+1}/{len(combos)}] {gid} SKIP", flush=True)
            continue
        cfg = HuntConfig(
            generation_id=gid,
            symbol=sym,
            timeframe=tf,
            target=tgt,
            feature_space=SPACE,
            horizon=DEFAULT_HORIZON[tgt],
            max_trials=4,
            run_backtest=False,  # proxy screen only; full gates via settle_structure_tier2
            run_surrogate_challenge=True,
            models=["hist_mean", "ridge", "lgbm_regressor", "lgbm_classifier"],
        )
        summary = run_nested_hunt(cfg)
        tier = int(summary.get("best_tier") or 0)
        best_tier = max(best_tier, tier)
        print(
            f"[{i+1}/{len(combos)}] {gid} tier={tier} "
            f"pred={summary.get('predictability_passed')}",
            flush=True,
        )
        results.append({"generation_id": gid, **{k: summary.get(k) for k in (
            "best_tier", "predictability_passed", "status", "best"
        )}})
        # Proxy Tier ≥ 2 is a screen signal only — do not halt or claim readiness.
        # The settled BTCUSDT 1h fwd_return candidate already owns the full-gate path.
        if tier >= 2 and summary.get("predictability_passed"):
            append_ledger(
                f"SCREEN_CANDIDATE structure_v1 {gid} proxy_tier={tier} "
                "(not a full-gate alert; stress/MDD unbound on proxy path)",
                tier=1,
            )

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = {
        "study_id": "structure_v1_hunt_001",
        "readiness": "RESEARCH_ONLY",
        "best_tier": best_tier,
        "results": results,
        "stamped_utc": stamp,
        "note": "Outside ABC continuation; video rules are not evidence (ABC_RULES_TESTED.md)",
    }
    from llm2.paths import ARTIFACTS

    path = ARTIFACTS / "reports" / f"structure_v1_hunt_{stamp}.json"
    path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    append_ledger(
        f"STRUCTURE_V1_HUNT complete best_tier={best_tier} report={path.name}",
        tier=best_tier,
    )
    print(f"wrote {path} best_tier={best_tier}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
