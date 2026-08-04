"""Add llm2_structure candle demand to bots_registry.yaml on ln1."""
from __future__ import annotations

from pathlib import Path

import yaml

REG = Path("/opt/botsgeneral/config/bots_registry.yaml")
raw = yaml.safe_load(REG.read_text(encoding="utf-8")) or {}
vps = raw.setdefault("vps", {}).setdefault("94.156.189.76", {})
bots = list(vps.get("bots") or [])
if "llm2_structure" not in bots:
    bots.append("llm2_structure")
vps["bots"] = bots
raw.setdefault("bots", {})["llm2_structure"] = {
    "serve_candles": True,
    "exchange": "bybit",
    "account": "Xxobster7",
    "path": "/opt/llm2-structure",
    "parser": "none",
    "timeframe": "1h",
    "symbols": ["BTCUSDT"],
    "also_fetch_timeframes": ["4h", "1w"],
    "process_match": ["llm2.live.micro_runner"],
    "systemd_match": ["llm2-structure-micro"],
    "screen_match": ["llm2-structure"],
}
REG.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
print("registered llm2_structure ->", bots)
