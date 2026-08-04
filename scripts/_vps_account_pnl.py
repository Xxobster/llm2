"""Run on ln1: print one account's botsgeneral.pnl JSON (no secrets)."""
from __future__ import annotations

import json
import sys

sys.path.insert(0, "/opt/botsgeneral")
from botsgeneral.pnl import build_pnl  # noqa: E402

acc = (sys.argv[1] if len(sys.argv) > 1 else "Xxobster7").lower()
rep = build_pnl()
row = next(
    (a for a in rep.get("accounts") or [] if str(a.get("account", "")).lower() == acc),
    {"error": "account missing", "account": acc},
)
print(json.dumps(row, default=str))
