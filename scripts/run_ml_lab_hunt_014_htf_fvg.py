"""ML lab hunt 014 — higher-timeframe Fair Value Gap + new formulas. RESEARCH_ONLY."""

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
from llm2.ml_lab.idea_catalog_k import (  # noqa: E402
    IDEA_IDS_K,
    build_features_for_guard,
    signals_k,
)
from llm2.paths import ARTIFACTS  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument("--skip-leakage", action="store_true")
    ap.add_argument("--skip-tradesim", action="store_true")
    args = ap.parse_args()
    return run_catalog_hunt(
        prereg=_ROOT / "configs" / "preregister" / "ml_lab_hunt_014_htf_fvg.yaml",
        db_dir=ARTIFACTS / "sqlite" / "ml_lab_hunt_014_htf_fvg",
        out_stem="hunt_014_htf_fvg",
        title="ML lab hunt 014 (higher-timeframe Fair Value Gap + new formulas)",
        idea_ids=IDEA_IDS_K,
        signals_fn=signals_k,
        leak_builder=build_features_for_guard,
        ledger_name="ML_LAB_HUNT_014",
        skip_leakage=args.skip_leakage,
        skip_tradesim=args.skip_tradesim,
        report_only=args.report_only,
    )


if __name__ == "__main__":
    raise SystemExit(main())
