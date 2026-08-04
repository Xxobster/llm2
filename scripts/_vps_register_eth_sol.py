"""Register complete llm2 BTC/ETH/SOL entries in bots_registry.yaml on ln1."""
from __future__ import annotations

from pathlib import Path

import yaml

REG = Path("/opt/botsgeneral/config/bots_registry.yaml")
raw = yaml.safe_load(REG.read_text(encoding="utf-8")) or {}
vps = raw.setdefault("vps", {}).setdefault("94.156.189.76", {})
fleet = list(vps.get("bots") or [])
for name in ("llm2_structure", "llm2_structure_eth", "llm2_structure_sol"):
    if name not in fleet:
        fleet.append(name)
vps["bots"] = fleet
bots = raw.setdefault("bots", {})
bots["llm2_structure"] = {
    "serve_candles": True,
    "exchange": "bybit",
    "account": "Xxobster7",
    "path": "/opt/llm2-structure",
    "parser": "none",
    "timeframe": "1h",
    "symbols": ["BTCUSDT"],
    "also_fetch_timeframes": ["4h", "1w"],
    "process_match": ["--pack /opt/llm2-structure/pack"],
    "systemd_match": ["llm2-structure-micro"],
    "screen_match": ["llm2-structure-micro"],
}
bots["llm2_structure_eth"] = {
    "serve_candles": True,
    "exchange": "bybit",
    "account": "Xxobster7",
    "path": "/opt/llm2-structure-eth",
    "parser": "none",
    "timeframe": "1h",
    "symbols": ["ETHUSDT"],
    "also_fetch_timeframes": ["4h", "1w"],
    "process_match": ["--pack /opt/llm2-structure-eth/pack"],
    "systemd_match": ["llm2-structure-eth"],
    "screen_match": ["llm2-structure-eth"],
}
bots["llm2_structure_sol"] = {
    "serve_candles": True,
    "exchange": "bybit",
    "account": "Xxobster7",
    "path": "/opt/llm2-structure-sol",
    "parser": "none",
    "timeframe": "1h",
    "symbols": ["SOLUSDT"],
    "also_fetch_timeframes": ["4h", "1w"],
    "process_match": ["--pack /opt/llm2-structure-sol/pack"],
    "systemd_match": ["llm2-structure-sol"],
    "screen_match": ["llm2-structure-sol"],
}
REG.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
print("registered", fleet)
