"""Register BTC+SOL k5 double3h (Xxobster10) and set go-live dates on VPS."""
from __future__ import annotations

from pathlib import Path

import yaml

HOST = "94.156.189.76"
ACCOUNT = "Xxobster10"
TODAY = "2026-08-04"
REG = Path("/opt/botsgeneral/config/bots_registry.yaml")
REPORT = Path("/etc/botsgeneral/report.yaml")

BOTS = (
    {
        "name": "llm2_structure_btc_k5_double3h",
        "path": "/opt/llm2-structure-btc-k5-double3h-v1",
        "unit": "llm2-structure-btc-k5-double3h-v1",
        "symbols": ["BTCUSDT"],
        "notes": "Track2 k5_double3h BTC; Xxobster10; distinct from llm2_structure",
    },
    {
        "name": "llm2_structure_sol_k5_double3h",
        "path": "/opt/llm2-structure-sol-k5-double3h-v1",
        "unit": "llm2-structure-sol-k5-double3h-v1",
        "symbols": ["SOLUSDT"],
        "notes": "Track2 k5_double3h SOL; Xxobster10; distinct from llm2_structure_sol",
    },
)


def main() -> None:
    raw = yaml.safe_load(REG.read_text(encoding="utf-8")) or {}
    vps = raw.setdefault("vps", {}).setdefault(HOST, {})
    fleet = list(vps.get("bots") or [])
    bots = raw.setdefault("bots", {})
    for b in BOTS:
        if b["name"] not in fleet:
            fleet.append(b["name"])
        bots[b["name"]] = {
            "serve_candles": True,
            "exchange": "bybit",
            "account": ACCOUNT,
            "path": b["path"],
            "parser": "none",
            "timeframe": "1h",
            "symbols": b["symbols"],
            "also_fetch_timeframes": ["4h", "1w"],
            "process_match": [f"--pack {b['path']}/pack"],
            "systemd_match": [b["unit"]],
            "screen_match": [b["unit"]],
            "notes": b["notes"],
        }
    vps["bots"] = fleet
    REG.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")

    rep = yaml.safe_load(REPORT.read_text(encoding="utf-8")) if REPORT.is_file() else {}
    if not isinstance(rep, dict):
        rep = {}
    by_bot = rep.setdefault("since_by_bot", {})
    if not isinstance(by_bot, dict):
        by_bot = {}
        rep["since_by_bot"] = by_bot
    for b in BOTS:
        by_bot[b["name"]] = {b["symbols"][0]: TODAY}
    by_acct = rep.setdefault("since_by_account", {})
    if not isinstance(by_acct, dict):
        by_acct = {}
        rep["since_by_account"] = by_acct
    by_acct[ACCOUNT] = TODAY
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(yaml.safe_dump(rep, sort_keys=False), encoding="utf-8")
    print("registered", [b["name"] for b in BOTS], "account", ACCOUNT, "since", TODAY)


if __name__ == "__main__":
    main()
