"""Set bots report since-dates for k5 double3h go-live (today)."""
from __future__ import annotations

from pathlib import Path

import yaml

REPORT = Path("/etc/botsgeneral/report.yaml")
# Session context: go-live date (UTC calendar day for PnL window).
TODAY = "2026-08-04"
BOT = "llm2_structure_eth_k5_double3h"
ACCOUNT = "Xxobster6"

raw = yaml.safe_load(REPORT.read_text(encoding="utf-8")) if REPORT.is_file() else {}
if not isinstance(raw, dict):
    raw = {}

by_bot = raw.setdefault("since_by_bot", {})
if not isinstance(by_bot, dict):
    by_bot = {}
    raw["since_by_bot"] = by_bot
by_bot[BOT] = {"ETHUSDT": TODAY}

by_acct = raw.setdefault("since_by_account", {})
if not isinstance(by_acct, dict):
    by_acct = {}
    raw["since_by_account"] = by_acct
# User: set account date to today for this Xxobster6 micro deploy.
by_acct[ACCOUNT] = TODAY

REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
print("report.yaml updated since_by_bot", BOT, TODAY, "since_by_account", ACCOUNT, TODAY)
