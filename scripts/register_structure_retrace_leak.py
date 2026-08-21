"""Record CAUS-STRUCT-001 in the leakage registry.

``last_retrace_pct`` (and its higher-timeframe aliases) was published at the leg's
own confirmation time while its value is measured against the END of the following
opposite leg. Every model trained before the fix consumed a value the live bot could
not have, so the affected columns are recorded as remediated-with-retrain-required.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REGISTRY = Path(__file__).resolve().parents[1] / "artifacts" / "sqlite" / "leakage_registry.json"

FINDING = (
    "CAUS-STRUCT-001 PREFIX_INVARIANCE: retracement is measured against the end of "
    "the NEXT opposite leg but was published at this leg's confirmation time, so a "
    "later full-history recompute rewrote bar T. Live saw NaN (zero-filled) where "
    "research saw the back-filled value. Fixed in botsgeneral indicators compute.py "
    "(publish at successor leg known time); warehouse rebuilt; models trained before "
    "the fix must be retrained."
)
COLUMNS = ("last_retrace_pct", "last_retrace_pct_4h", "last_retrace_pct_1w")
SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")


def main() -> int:
    doc = json.loads(REGISTRY.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    cols = doc.setdefault("columns", {})
    for name in COLUMNS:
        entry = cols.get(name) or {}
        reasons = list(entry.get("reasons") or [])
        if FINDING not in reasons:
            reasons.append(FINDING)
        cols[name] = {
            "engine_note": "indicators.compute CAUS-STRUCT-001",
            "first_seen_utc": entry.get("first_seen_utc") or now,
            "last_seen_utc": now,
            "reasons": reasons,
            # Remediated in the builder; the block that remains is retraining.
            "status": "REMEDIATED_RETRAIN_REQUIRED",
            "symbol": ",".join(SYMBOLS),
            "timeframe": "1h,4h,15m",
        }
    doc["updated_at_utc"] = now
    REGISTRY.write_text(json.dumps(doc, indent=2, sort_keys=True), encoding="utf-8")
    print(f"registered {len(COLUMNS)} columns in {REGISTRY}")
    for name in COLUMNS:
        print(f"  {name}: {cols[name]['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
