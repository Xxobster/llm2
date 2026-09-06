from __future__ import annotations

import json
from pathlib import Path

CLOSED = Path("artifacts/reports/_xx8_eth_closed.json")


def test_xx8_eth_closed_json_has_twenty_round_trips() -> None:
    blob = json.loads(CLOSED.read_text(encoding="utf-8"))
    assert blob.get("n") == 20
    rows = blob.get("trades") or []
    assert len(rows) == 20
    assert all(float(r["avgEntryPrice"]) > 0 and float(r["avgExitPrice"]) > 0 for r in rows)
    assert all(int(r["createdTime"]) > 0 and int(r["updatedTime"]) > 0 for r in rows)
    first = min(int(r["createdTime"]) for r in rows)
    last = max(int(r["updatedTime"]) for r in rows)
    assert first >= 1_751_000_000_000  # 2025-07+
    assert last < 1_800_000_000_000  # before 2027
