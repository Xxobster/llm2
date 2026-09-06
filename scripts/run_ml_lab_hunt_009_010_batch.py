"""Run hunt 009 (new formulas) then hunt 010 (contaminated tunes). Never deploys."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from scripts.run_ml_lab_hunt_009_formulas import main as main_009
from scripts.run_ml_lab_hunt_010_contaminated_tune import main as main_010
from scripts.run_ml_lab_hunt_011_more_formulas import main as main_011


def main() -> int:
    print("=== batch hunt 009 formulas ===", flush=True)
    rc = main_009()
    if rc != 0:
        print(f"hunt 009 exited {rc} — still running hunt 010", flush=True)
    print("=== batch hunt 010 contaminated tune ===", flush=True)
    rc2 = main_010()
    print("=== batch hunt 011 more formulas ===", flush=True)
    rc3 = main_011()
    if rc != 0:
        return rc
    if rc2 != 0:
        return rc2
    return rc3


if __name__ == "__main__":
    raise SystemExit(main())
