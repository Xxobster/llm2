"""Register ETH k5 double3h (Xxobster6) in bots_registry.yaml on VPS."""
from __future__ import annotations

from pathlib import Path

import yaml

REG = Path("/opt/botsgeneral/config/bots_registry.yaml")
NAME = "llm2_structure_eth_k5_double3h"
ACCOUNT = "Xxobster6"
PATH = "/opt/llm2-structure-eth-k5-double3h-v1"
UNIT = "llm2-structure-eth-k5-double3h-v1"
HOST = "94.156.189.76"

raw = yaml.safe_load(REG.read_text(encoding="utf-8")) or {}
vps = raw.setdefault("vps", {}).setdefault(HOST, {})
fleet = list(vps.get("bots") or [])
if NAME not in fleet:
    fleet.append(NAME)
vps["bots"] = fleet

bots = raw.setdefault("bots", {})
bots[NAME] = {
    "serve_candles": True,
    "exchange": "bybit",
    "account": ACCOUNT,
    "path": PATH,
    "parser": "none",
    "timeframe": "1h",
    "symbols": ["ETHUSDT"],
    "also_fetch_timeframes": ["4h", "1w"],
    "process_match": [f"--pack {PATH}/pack"],
    "systemd_match": [UNIT],
    "screen_match": [UNIT],
    "notes": (
        "k5_double3h mean_strength|hold12|tp1%|K=5|size×2 within 3h; "
        "distinct from llm2_structure_eth and eth_multitrade"
    ),
}
REG.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
print("registered", NAME, "account=", ACCOUNT, "fleet=", fleet)
