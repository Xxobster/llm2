"""Append-only research ledger."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from llm2.paths import ARTIFACTS

LEDGER_PATH = ARTIFACTS / "reports" / "RESEARCH_LEDGER.md"


def append_ledger(entry: str, *, tier: int = 0) -> None:
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    prefix = "ALERT" if tier >= 2 else "INFO"
    line = f"\n## [{prefix}] {ts} (tier {tier})\n\n{entry.strip()}\n"
    if not LEDGER_PATH.exists():
        LEDGER_PATH.write_text("# LLM2 Research Ledger\n", encoding="utf-8")
    with LEDGER_PATH.open("a", encoding="utf-8") as f:
        f.write(line)
