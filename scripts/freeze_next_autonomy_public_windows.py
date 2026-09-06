"""Freeze unused public-formula windows so the autonomy hunt never idles.

RESEARCH_ONLY. Honors artifacts/autonomy/STOP.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.autonomy.auto_windows import (  # noqa: E402
    DEFAULT_BATCH,
    DEFAULT_MIN_REMAINING,
    ensure_queue_depth,
    remaining_count,
)


def main() -> int:
    stop = _ROOT / "artifacts" / "autonomy" / "STOP"
    p = argparse.ArgumentParser()
    p.add_argument("--ensure-remaining", type=int, default=DEFAULT_MIN_REMAINING)
    p.add_argument("--batch", type=int, default=DEFAULT_BATCH)
    args = p.parse_args()
    if stop.exists():
        print("STOP present — not freezing", flush=True)
        return 0
    before = remaining_count()
    added = ensure_queue_depth(min_remaining=int(args.ensure_remaining), batch=int(args.batch))
    after = remaining_count()
    if added:
        print(
            f"auto-froze n={len(added)} ids={added[0]}..{added[-1]} remaining {before}->{after}",
            flush=True,
        )
    else:
        print(f"queue remaining={after} (no freeze)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
