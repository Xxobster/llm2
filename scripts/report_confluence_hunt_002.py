"""Rebuild the hunt-002 leaderboard from the checkpoint SQLite file."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.confluence.sim_arms import open_checkpoint
from llm2.paths import ARTIFACTS

# Reuse writer from the hunt module without rerunning the grid.
import scripts.run_confluence_autonomous_hunt_002 as hunt


def main() -> int:
    db = ARTIFACTS / "sqlite" / "confluence_autonomous_hunt_002" / "hunt.sqlite"
    if not db.exists():
        raise SystemExit(f"missing {db}")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    con = open_checkpoint(db)
    hunt._write_leaderboard(con, stamp, {"rebuilt": True})
    print(f"WROTE {ARTIFACTS / 'reports' / 'confluence' / 'autonomous_hunt_002_latest.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
