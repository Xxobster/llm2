# Tier-2 Review Protocol

No GATE_CANDIDATE has cleared Frozen Gates B–E yet.

When a trial reaches tier >= 2, automatically:
1. Re-run the exact config with tradesim (store_path enabled)
2. Open finplot via tradesim-research open --run-id ...
3. Print format_gates_table(...) with evidence
4. ALERT the operator — do not deploy

Current best: `structure_v1_tier2_settlement.json` — lgbm_regressor settle PF≈1.84 tier=3
overall PASS (stress/MDD/margin PASS; PBO UNAVAILABLE). Verdict SHADOW_READY_CANDIDATE;
readiness still RESEARCH_ONLY / LIVE_STOP. Do not deploy.
