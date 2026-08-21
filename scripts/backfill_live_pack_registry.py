"""Backfill live_pack_versions from on-disk packs and regenerate VERSIONS.md."""

from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.evidence.pack_registry import backfill_all_packs, list_versions  # noqa: E402


def main() -> int:
    registered = backfill_all_packs(write_versions_md=True)
    print(json.dumps({"n": len(registered), "versions": [m["version_id"] for m in registered]}, indent=2))
    print(f"registry_rows={len(list_versions())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
