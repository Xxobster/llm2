"""Register ETH multitrade v1.2 (Xxobster8) in bots_registry.yaml on VPS."""
from __future__ import annotations

from pathlib import Path

import yaml

REG = Path("/opt/botsgeneral/config/bots_registry.yaml")
NAME = "llm2_structure_eth_multitrade"
ACCOUNT = "Xxobster8"
PATH = "/opt/llm2-structure-eth-multitrade-v1_2"
UNIT = "llm2-structure-eth-multitrade-v1_2"
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
        "multitrade v1.2 mean_strength|clarity_scope=all|fib1.618|hold12|K=7; "
        "replaces v1.1 addon-scope; distinct from llm2_structure_eth"
    ),
}
REG.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
print("registered", NAME, "account=", ACCOUNT, "path=", PATH, "fleet=", fleet)
