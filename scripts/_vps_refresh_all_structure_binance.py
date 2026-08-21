"""Refresh every LLM2 pack slice on the host from Binance (1h/4h/1w).

Replaces the previous version, which was failing on every run:

* ``limit=1500`` is below the ``MIN_STRUCTURE_HISTORY_BARS`` guard (5000 on 1h,
  2000 on 4h), so the refresh raised ``structure_history_too_short`` and no pack
  slice was ever updated by the timer. Full history is what the backtest uses, so
  the limit must be ``None``.
* The unit list was hard-coded and had drifted: the k5 units were never refreshed
  at all. Units are now discovered from ``/opt``.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, "/opt/llm2-structure")
sys.path.insert(0, "/opt/botsgeneral/packages/live_candles/src")
sys.path.insert(0, "/opt/botsgeneral/packages/indicators/src")

from llm2.live.refresh_structure import refresh_symbol  # noqa: E402

OPT = Path("/opt")


def discover() -> list[tuple[str, Path]]:
    """(symbol, slice_db) for every unit that has a pack on this host."""
    out: list[tuple[str, Path]] = []
    for pack in sorted(OPT.glob("llm2-structure*/pack/strategy.json")):
        try:
            strategy = json.loads(pack.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"SKIP unreadable {pack}: {exc}")
            continue
        symbol = str(strategy.get("symbol") or "").upper()
        if not symbol:
            print(f"SKIP no symbol in {pack}")
            continue
        out.append((symbol, pack.parent / "indicators_live_slice.sqlite"))
    return out


def main() -> int:
    targets = discover()
    print(f"units discovered: {len(targets)}")
    rc = 0
    for symbol, db in targets:
        if not db.parent.is_dir():
            print(f"SKIP missing {db}")
            continue
        rep = refresh_symbol(
            symbol=symbol,
            timeframes=("1h", "4h", "1w"),
            indicator_db=db,
            limit=None,
            source="binance",
        )
        bad = [s for s in rep["series"] if s.get("error")]
        if bad:
            rc = 1
        print(
            ("FAIL" if bad else "OK"),
            symbol,
            db,
            json.dumps(rep["series"], default=str),
            flush=True,
        )
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
