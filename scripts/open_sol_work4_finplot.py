"""Open SOL work4 TP1/SL1 Finplot without drowning in full-history finplot warnings.

The saved run has ~99k 15m bars + 798 trades. Full-period Finplot fragments a
huge DataFrame and spams PerformanceWarning; clip to a trade-aware window.
"""

from __future__ import annotations

import argparse
import os
import sys
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

DEFAULT_DB = (
    _ROOT
    / "artifacts"
    / "reports"
    / "pivot_forecast"
    / "finplot_diag_20260810T154701Z"
    / "SOL_work4_tp1_sl1_report"
)
RUN_ID = "SOL_work4_tp1_sl1-97d5a6060d"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-bars", type=int, default=4000, help="0 = full (slow/noisy)")
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = ap.parse_args()

    os.environ.pop("TRADESIM_NO_PLOT", None)

    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()

    # Finplot inserts many columns on large frames; warnings are noise, not the bug.
    warnings.filterwarnings(
        "ignore",
        category=Warning,
        module=r"finplot(\.|$)",
    )
    try:
        import pandas as pd

        warnings.filterwarnings(
            "ignore",
            category=pd.errors.PerformanceWarning,
        )
    except Exception:
        pass

    from tradesim.research.__main__ import main as research_main

    db = str(args.db.resolve())
    if not Path(db).is_file():
        print(f"missing store: {db}", file=sys.stderr)
        return 2
    print(
        f"Opening {RUN_ID}\n  db={db}\n  max_bars={args.max_bars} "
        f"(full run is ~99k bars / 798 trades — clip keeps Finplot usable)",
        flush=True,
    )
    return research_main(
        [
            "--db",
            db,
            "plot",
            "--run-id",
            RUN_ID,
            "--max-bars",
            str(int(args.max_bars)),
        ]
    )


if __name__ == "__main__":
    raise SystemExit(main())
