"""Freeze BTCUSDT + SOLUSDT k5_double3h packs (Track2 arm) for Xxobster10."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from llm2.live.certificate import pack_fingerprint

ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "artifacts" / "live_packs"
CERTS = ROOT / "configs" / "live"

SPECS = (
    {
        "parent": "structure_v1_lgbm",
        "dst": "structure_v1_btcusdt_k5_double3h_v1",
        "symbol": "BTCUSDT",
        "target": "fwd_return",
        "min_edge": 0.0016,
        "version_id": "btc_k5_double3h_v1",
        "strategy_id": "structure_v1_lgbm_BTCUSDT_1h_fwd_return_k5_double3h_v1",
    },
    {
        "parent": "structure_v1_solusdt_direction",
        "dst": "structure_v1_solusdt_k5_double3h_v1",
        "symbol": "SOLUSDT",
        "target": "direction",
        "min_edge": 0.1,
        "version_id": "sol_k5_double3h_v1",
        "strategy_id": "structure_v1_lgbm_SOLUSDT_1h_direction_k5_double3h_v1",
    },
)

MULTITRADE = {
    "max_positions_per_side": 5,
    "clarity": "mean_strength",
    "clarity_scope": "all",
    "fib_ext": 0.0,
    "hold_addon": 12,
    "base_tp": 0.01,
    "base_sl": 0.02,
    "base_hold": 12,
    "mean_lookback": 168,
    "size_double_within_bars": 3,
    "size_double_mult": 2.0,
    "uniform_books": True,
    "bar_ms": 3_600_000,
}


def freeze_one(spec: dict) -> str:
    parent = PACKS / spec["parent"]
    dst = PACKS / spec["dst"]
    if not parent.is_dir():
        raise SystemExit(f"missing parent {parent}")
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(parent, dst)
    strat_path = dst / "strategy.json"
    s = json.loads(strat_path.read_text(encoding="utf-8"))
    s["strategy_id"] = spec["strategy_id"]
    s["symbol"] = spec["symbol"]
    s["target"] = spec["target"]
    s["horizon_bars"] = 12
    s["tp_pct"] = 0.01
    s["sl_pct"] = 0.02
    s["min_edge"] = float(spec["min_edge"])
    s["leverage"] = 18.0
    s.setdefault(
        "leverage_policy",
        {
            "method": "leverage_from_stop",
            "sl_pct": 0.02,
            "mm_buffer": 0.005,
            "mark_buffer": 0.002,
            "haircut": 0.5,
            "ceiling_before_haircut": 37,
        },
    )
    s["sizing"] = "MIN_EXCHANGE"
    s["position_mode"] = "HEDGE"
    s["version_id"] = spec["version_id"]
    s["version_lineage"] = {
        "parent_pack": spec["parent"],
        "research_arm": "mean_strength|hold12|tp1pct|K=5|double3h",
        "transfer_generation": "structure_v1_btc_sol_cluster_double_transfer_001",
        "note": "Track2 transfer arm; RESEARCH_TRANSFER_MICRO on Xxobster10.",
    }
    s["execution_mode"] = "multitrade"
    s["max_positions"] = 10
    s["max_positions_per_side"] = 5
    mt = dict(MULTITRADE)
    mt["version_id"] = spec["version_id"]
    s["multitrade"] = mt
    s["what_it_does"] = (
        f"K=5 concurrent books/side on {spec['symbol']}; mean_strength on every entry; "
        "all books TP+1% SL-2% hold12; size 2x min-exchange when same-side entry within "
        "3h of last. Account Xxobster10. MIN_EXCHANGE."
    )
    strat_path.write_text(json.dumps(s, indent=2) + "\n", encoding="utf-8")
    (dst / "README.md").write_text(
        f"# {spec['dst']}\n\nTrack2 k5_double3h for {spec['symbol']}. "
        "Do not overwrite in place.\n",
        encoding="utf-8",
    )
    (dst / "pack_meta.json").write_text(
        json.dumps(
            {
                "version_id": spec["version_id"],
                "parent": spec["parent"],
                "account": "Xxobster10",
                "frozen_utc": "2026-08-04T14:40:00Z",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    fp = pack_fingerprint(dst)
    assert fp
    (dst / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")

    cert = CERTS / f"{spec['dst']}_certificate.yaml"
    body = f"""strategy_id: {spec['strategy_id']}
version_id: {spec['version_id']}
status: AUTHORIZED
authorized_by_user: true
vps_host: 94.156.189.76
account_ref: Xxobster10
intended_vps_host: 94.156.189.76
intended_account_ref: Xxobster10
pack_path: artifacts/live_packs/{spec['dst']}
pack_hash: {fp}
expires_utc: '2026-08-18T00:00:00Z'
created_utc: '2026-08-04T14:40:00Z'
execution_mode: multitrade
notes: >-
  User authorized 2026-08-04 to deploy Track2 k5_double3h for {spec['symbol']}
  on Xxobster10 / 94.156.189.76 (shared with BTC+SOL k5 units). MIN_EXCHANGE.
  RESEARCH_TRANSFER_MICRO — not full V2.1 hedge settle. Distinct from Xxobster7
  single-book. Expires 2026-08-18 unless renewed.
"""
    cert.write_text(body, encoding="utf-8")
    print(spec["symbol"], "hash", fp, "->", dst)
    return fp


def main() -> int:
    for spec in SPECS:
        freeze_one(spec)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
