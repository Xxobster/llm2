"""Sequential research batch: hunt 009, hunt 010, answer-A EXEC-021."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    os.chdir(_ROOT)
    jobs = [
        "scripts/run_ml_lab_hunt_009_causal_math.py",
        "scripts/run_ml_lab_hunt_010_contaminated_tune.py",
        "scripts/run_ml_lab_hunt_011_more_formulas.py",
    ]
    rc = 0
    for job in jobs:
        print(f"=== BATCH {job} ===", flush=True)
        r = subprocess.run([sys.executable, "-u", str(_ROOT / job)], cwd=str(_ROOT))
        print(f"=== BATCH {job} rc={r.returncode} ===", flush=True)
        if r.returncode != 0:
            rc = r.returncode
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
