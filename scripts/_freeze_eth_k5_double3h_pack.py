"""One-shot: freeze ETH k5_double3h pack JSON + hash + cert patch."""
from __future__ import annotations

import json
import re
from pathlib import Path

from llm2.live.certificate import load_certificate, pack_fingerprint
from llm2.live.multitrade import parse_multitrade_config

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / "artifacts/live_packs/structure_v1_ethusdt_multitrade_v1_1/strategy.json"
P = ROOT / "artifacts/live_packs/structure_v1_ethusdt_k5_double3h_v1"
CERT = ROOT / "configs/live/structure_v1_ethusdt_k5_double3h_v1_certificate.yaml"

parent = json.loads(PARENT.read_text(encoding="utf-8"))
strategy = {
    "strategy_id": "structure_v1_lgbm_ETHUSDT_1h_direction_k5_double3h_v1",
    "symbol": "ETHUSDT",
    "timeframe": "1h",
    "venue_product": "Bybit USDT perpetual",
    "feature_space": "structure_v1",
    "target": "direction",
    "horizon_bars": 12,
    "model": "lgbm_regressor",
    "tp_pct": 0.01,
    "sl_pct": 0.02,
    "min_edge": 0.1,
    "leverage": 18.0,
    "leverage_policy": {
        "method": "leverage_from_stop",
        "sl_pct": 0.02,
        "mm_buffer": 0.005,
        "mark_buffer": 0.002,
        "haircut": 0.5,
        "ceiling_before_haircut": 37,
        "note": "Lowest operational leverage with SL security margin (D-001).",
    },
    "sizing": "MIN_EXCHANGE",
    "position_mode": "HEDGE",
    "fold_geometry": "v2",
    "trained_until_exclusive": "2025-10-01 00:00:00+00:00",
    "lockbox_start": "2026-05-01",
    "feature_columns": parent["feature_columns"],
    "model_file": "model.joblib",
    "mark_sample": parent.get("mark_sample"),
    "min_size_equity_caveat": parent.get(
        "min_size_equity_caveat",
        "Wallet equity / maximum drawdown under research_sizing MIN_EXCHANGE "
        "(minimum exchange size) on a large wallet is not tradable-edge evidence.",
    ),
    "version_id": "eth_k5_double3h_v1",
    "version_lineage": {
        "parent_pack": "structure_v1_ethusdt_direction",
        "research_arm": "clarity=mean_strength|hold=12|tp=1%|K=5|size_double_within_bars=3",
        "grid_version": "cluster_size_double_k3_9",
        "note": (
            "Research k5_double3h: primary mean_strength on all entries; "
            "uniform TP1%/SL2%/hold12; qty 2x min when same-side entry gap <= 3h."
        ),
    },
    "execution_mode": "multitrade",
    "max_positions": 10,
    "max_positions_per_side": 5,
    "multitrade": {
        "version_id": "eth_k5_double3h_v1",
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
    },
    "what_it_does": (
        "K=5 concurrent books/side; mean_strength on every entry; all books "
        "TP+1% SL-2% hold12; size 2x min-exchange when same-side entry within "
        "3h of last. Research arm k5_double3h. MIN_EXCHANGE. Account Xxobster6."
    ),
}
P.mkdir(parents=True, exist_ok=True)
(P / "strategy.json").write_text(json.dumps(strategy, indent=2) + "\n", encoding="utf-8")
meta = {
    "version_id": "eth_k5_double3h_v1",
    "parent": "structure_v1_ethusdt_direction",
    "research_arm": "mean_strength|hold12|tp1pct|K=5|double3h",
    "frozen_utc": "2026-08-04T11:20:00Z",
    "account": "Xxobster6",
}
(P / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
(P / "README.md").write_text(
    "# ETHUSDT k=5 cluster size-double (3h)\n\n"
    "Research arm: mean_strength (all entries) + hold 12 + TP 1% + SL 2% + K=5 "
    "+ size double within 3 bars (1h).\n"
    "Frozen pack v1 for Xxobster6 micro-live. Do not overwrite in place.\n",
    encoding="utf-8",
)
fp = pack_fingerprint(P)
assert fp
(P / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
text = CERT.read_text(encoding="utf-8")
CERT.write_text(re.sub(r"pack_hash:.*", f"pack_hash: {fp}", text), encoding="utf-8")
c = load_certificate(CERT)
assert c.is_deployable and c.pack_hash == fp
mt = parse_multitrade_config(strategy)
assert mt and mt["size_double_within_bars"] == 3 and mt["uniform_books"]
print("OK hash", fp)
print(
    "gate",
    mt["clarity_scope"],
    mt["base_hold"],
    mt["max_positions_per_side"],
)
