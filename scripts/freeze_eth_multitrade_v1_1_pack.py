"""Freeze ETHUSDT multitrade v1.1 — replaces v1 on Xxobster8 (K=7).

Arm: clarity=mean_strength | fib_ext=1.618 | hold_addon=12 | K=7
Does not overwrite structure_v1_ethusdt_multitrade_v1 (K=6 rollback pack).
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
DEST = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_v1_1"
VERSION_ID = "eth_multitrade_v1_1"
STRATEGY_ID = "structure_v1_lgbm_ETHUSDT_1h_direction_multitrade_v1_1"
K = 7
FIB = 1.618
HOLD_ADDON = 12


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
    tp3 = extended_tp_offset(FIB)
    strategy = {
        **{k: v for k, v in parent_strat.items() if k not in {"what_it_does", "max_positions"}},
        "strategy_id": STRATEGY_ID,
        "version_id": VERSION_ID,
        "version_lineage": {
            "parent_pack": "structure_v1_ethusdt_direction",
            "replaces": "structure_v1_ethusdt_multitrade_v1",
            "diff": "K=7 (was K=6); same mean_strength / fib 1.618 / hold 12",
            "research_arm": f"clarity=mean_strength|fib_ext={FIB}|hold={HOLD_ADDON}|K={K}",
            "grid_version": "v2_ext",
        },
        "execution_mode": "multitrade",
        "max_positions": int(K) * 2,
        "max_positions_per_side": int(K),
        "position_mode": "HEDGE",
        "multitrade": {
            "version_id": VERSION_ID,
            "max_positions_per_side": int(K),
            "clarity": "mean_strength",
            "fib_ext": FIB,
            "hold_addon": HOLD_ADDON,
            "base_tp": 0.01,
            "base_sl": 0.02,
            "base_hold": 6,
            "mean_lookback": 168,
            "book3plus_tp_pct": tp3,
        },
        "what_it_does": (
            f"MULTITRADE v1.1 (not single-book). Up to {K} concurrent min-qty books "
            "per side. Book 1–2: TP +1%, SL −2%, max-hold 6. Book 3+: TP +2.618% "
            f"(fib_ext={FIB}), SL −2%, max-hold {HOLD_ADDON}. Clarity mean_strength. "
            "Replaces eth_multitrade_v1 (K=6) on Xxobster8."
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
        "execution_mode": "multitrade",
        "account_ref_expected": "Xxobster8",
        "vps_host_expected": "94.156.189.76",
        "replaces_version": "eth_multitrade_v1",
        "frozen_utc": stamp,
        "rollback": {
            "this_pack": "artifacts/live_packs/structure_v1_ethusdt_multitrade_v1_1",
            "previous_pack": "artifacts/live_packs/structure_v1_ethusdt_multitrade_v1",
            "stop_service": "llm2-structure-eth-multitrade-v1_1",
            "restore_previous_service": "llm2-structure-eth-multitrade-v1",
        },
    }
    (DEST / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (DEST / "README.md").write_text(
        f"# {STRATEGY_ID}\n\n"
        f"**Version:** `{VERSION_ID}` — MULTITRADE K={K}/side "
        f"(mean_strength | fib {FIB} | hold {HOLD_ADDON}).\n\n"
        "Replaces `eth_multitrade_v1` (K=6) on Xxobster8. Prior pack kept for rollback.\n",
        encoding="utf-8",
    )
    fp = pack_fingerprint(DEST)
    (DEST / "pack_hash.txt").write_text((fp or "") + "\n", encoding="utf-8")
    print(f"FROZE {DEST}")
    print(f"pack_hash={fp}")
    print(f"K={K}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
