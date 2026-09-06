"""ML lab hunt 016 — oscillators and classic floor pivots. RESEARCH_ONLY."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from llm2.ml_lab.catalog_hunt_runner import run_catalog_hunt  # noqa: E402
from llm2.ml_lab.idea_catalog_m import (  # noqa: E402
    IDEA_IDS_M,
    build_features_for_guard,
    signals_m,
)
from llm2.paths import ARTIFACTS  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument("--skip-leakage", action="store_true")
    ap.add_argument("--skip-tradesim", action="store_true")
    args = ap.parse_args()
    return run_catalog_hunt(
        prereg=_ROOT / "configs" / "preregister" / "ml_lab_hunt_016_osc_pivot.yaml",
        db_dir=ARTIFACTS / "sqlite" / "ml_lab_hunt_016_osc_pivot",
        out_stem="hunt_016_osc_pivot",
        title="ML lab hunt 016 (oscillators and classic floor pivots)",
        idea_ids=IDEA_IDS_M,
        signals_fn=signals_m,
        leak_builder=build_features_for_guard,
        ledger_name="ML_LAB_HUNT_016",
        skip_leakage=args.skip_leakage,
        skip_tradesim=args.skip_tradesim,
        report_only=args.report_only,
    )


if __name__ == "__main__":
    raise SystemExit(main())
