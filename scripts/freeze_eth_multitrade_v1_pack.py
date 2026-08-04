"""Freeze ETHUSDT multitrade v1 pack (distinct from single-book direction).

Arm: clarity=mean_strength | fib_ext=1.618 | hold_addon=12 | K=6
Parent model: structure_v1_ethusdt_direction (same LightGBM weights).
Does not modify the single-book pack or Xxobster7 certificates.
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from llm2.live.certificate import pack_fingerprint
from llm2.live.multitrade import extended_tp_offset
from llm2.paths import ARTIFACTS, ROOT

PARENT = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_direction"
DEST = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_v1"
VERSION_ID = "eth_multitrade_v1"
STRATEGY_ID = "structure_v1_lgbm_ETHUSDT_1h_direction_multitrade_v1"


def main() -> int:
    if not PARENT.is_dir():
        raise SystemExit(f"parent pack missing: {PARENT}")
    DEST.mkdir(parents=True, exist_ok=True)
    for name in (
        "model.joblib",
        "risk_tiers.json",
        "indicators_live_slice.sqlite",
        "mark_snapshot.json",
        "structure_refresh_bootstrap.json",
    ):
        src = PARENT / name
        if src.is_file():
            shutil.copy2(src, DEST / name)

    parent_strat = json.loads((PARENT / "strategy.json").read_text(encoding="utf-8"))
    fib = 1.618
    tp3 = extended_tp_offset(fib)
    strategy = {
        **{k: v for k, v in parent_strat.items() if k not in {"what_it_does", "max_positions"}},
        "strategy_id": STRATEGY_ID,
        "version_id": VERSION_ID,
        "version_lineage": {
            "parent_pack": "structure_v1_ethusdt_direction",
            "parent_strategy_id": parent_strat.get("strategy_id"),
            "diff": "multitrade concurrent books vs single-book; fib-extended TP on book 3+",
            "research_arm": "clarity=mean_strength|fib_ext=1.618|hold=12|K=6",
            "grid_version": "v2_ext",
        },
        "execution_mode": "multitrade",
        "max_positions": 12,
        "max_positions_per_side": 6,
        "position_mode": "HEDGE",
        "multitrade": {
            "version_id": VERSION_ID,
            "max_positions_per_side": 6,
            "clarity": "mean_strength",
            "fib_ext": fib,
            "hold_addon": 12,
            "base_tp": 0.01,
            "base_sl": 0.02,
            "base_hold": 6,
            "mean_lookback": 168,
            "book3plus_tp_pct": tp3,
        },
        "what_it_does": (
            "MULTITRADE v1 (not single-book). On each closed 1h ETHUSDT bar, structure_v1 "
            "LightGBM direction gate (±0.10). Up to 6 concurrent min-qty books per side "
            "(hedge). Book 1–2: TP +1%, SL −2%, max-hold 6. Book 3+: TP +2.618% "
            f"(fib_ext={fib} on usual TP), SL −2%, max-hold 12. Add-ons require "
            "mean_strength (|pred| ≥ median of prior 168 signal |means|). Partial TP/SL "
            "per fill. Distinct from structure_v1_ethusdt_direction single-book live."
        ),
    }
    (DEST / "strategy.json").write_text(
        json.dumps(strategy, indent=2) + "\n", encoding="utf-8"
    )
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    meta = {
        "strategy_id": STRATEGY_ID,
        "version_id": VERSION_ID,
        "status": "FROZEN_LIVE_PACK",
        "readiness": "MICRO_LIVE_CANDIDATE_LOCKBOX_ONLY",
        "deployable": True,
        "evidence_class": "LOCKBOX_CONTAMINATED + outer-OOS hedge×3 proxy",
        "execution_mode": "multitrade",
        "account_ref_expected": "Xxobster8",
        "vps_host_expected": "94.156.189.76",
        "parent_pack": str(PARENT.relative_to(ROOT)).replace("\\", "/"),
        "frozen_utc": stamp,
        "rollback": {
            "this_pack": "artifacts/live_packs/structure_v1_ethusdt_multitrade_v1",
            "single_book_unchanged": "artifacts/live_packs/structure_v1_ethusdt_direction",
            "git_tag": f"live/{VERSION_ID}",
            "stop_service": "llm2-structure-eth-multitrade-v1",
        },
        "min_size_equity_caveat": parent_strat.get("min_size_equity_caveat"),
    }
    (DEST / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (DEST / "README.md").write_text(
        f"# {STRATEGY_ID}\n\n"
        f"**Version:** `{VERSION_ID}` — MULTITRADE (up to 6 books/side).\n\n"
        "Not the single-book ETH bot on Xxobster7 (`structure_v1_ethusdt_direction`).\n"
        "Rollback: stop `llm2-structure-eth-multitrade-v1`; single-book services untouched.\n"
        "See `artifacts/live_packs/VERSIONS.md`.\n",
        encoding="utf-8",
    )
    fp = pack_fingerprint(DEST)
    (DEST / "pack_hash.txt").write_text((fp or "") + "\n", encoding="utf-8")
    print(f"FROZE {DEST}")
    print(f"pack_hash={fp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
