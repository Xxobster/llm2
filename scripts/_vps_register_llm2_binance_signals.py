"""Point all LLM2 live bots at Binance candle collection (signal parity).

Account stays Xxobster* for Bybit PnL / keys. exchange=binance drives shared_candles.
"""
from __future__ import annotations

from pathlib import Path

import yaml

REG = Path("/opt/botsgeneral/config/bots_registry.yaml")
raw = yaml.safe_load(REG.read_text(encoding="utf-8")) or {}
bots = raw.setdefault("bots", {})

updates = {
    "llm2_structure": {
        "exchange": "binance",
        "account": "Xxobster7",
        "path": "/opt/llm2-structure",
        "symbols": ["BTCUSDT"],
        "systemd_match": ["llm2-structure-micro"],
        "process_match": ["--pack /opt/llm2-structure/pack"],
        "screen_match": ["llm2-structure-micro"],
    },
    "llm2_structure_eth": {
        "exchange": "binance",
        "account": "Xxobster7",
        "path": "/opt/llm2-structure-eth",
        "symbols": ["ETHUSDT"],
        "systemd_match": ["llm2-structure-eth"],
        "process_match": ["--pack /opt/llm2-structure-eth/pack"],
        "screen_match": ["llm2-structure-eth"],
    },
    "llm2_structure_sol": {
        "exchange": "binance",
        "account": "Xxobster7",
        "path": "/opt/llm2-structure-sol",
        "symbols": ["SOLUSDT"],
        "systemd_match": ["llm2-structure-sol"],
        "process_match": ["--pack /opt/llm2-structure-sol/pack"],
        "screen_match": ["llm2-structure-sol"],
    },
    "llm2_structure_eth_multitrade": {
        "exchange": "binance",
        "account": "Xxobster8",
        "path": "/opt/llm2-structure-eth-multitrade-v1_1",
        "symbols": ["ETHUSDT"],
        "systemd_match": ["llm2-structure-eth-multitrade-v1_1"],
        "process_match": ["--pack /opt/llm2-structure-eth-multitrade-v1_1/pack"],
        "screen_match": ["llm2-structure-eth-multitrade-v1_1"],
    },
}

vps = raw.setdefault("vps", {}).setdefault("94.156.189.76", {})
fleet = list(vps.get("bots") or [])
for name, cfg in updates.items():
    if name not in fleet:
        fleet.append(name)
    bots[name] = {
        "serve_candles": True,
        "exchange": cfg["exchange"],
        "account": cfg["account"],
        "path": cfg["path"],
        "parser": "none",
        "timeframe": "1h",
        "symbols": cfg["symbols"],
        "also_fetch_timeframes": ["4h", "1w"],
        "process_match": cfg["process_match"],
        "systemd_match": cfg["systemd_match"],
        "screen_match": cfg["screen_match"],
        "notes": "signal=binance USD-M; execution=bybit",
    }
vps["bots"] = fleet
REG.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
print("updated llm2 bots -> exchange=binance; fleet=", fleet)
