"""Run a preregistered vol-as-filter vs always-on control experiment."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from llm2.experiments.vol_filter import (
    PREREG_DIR,
    PREREG_PATH,
    run_vol_filter_experiment,
    run_vol_filter_tradesim,
)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Vol-as-filter vs always-on control")
    ap.add_argument(
        "--prereg",
        type=Path,
        default=PREREG_PATH,
        help=f"preregister yaml (default {PREREG_PATH.name}; also under {PREREG_DIR})",
    )
    ap.add_argument(
        "--no-tradesim",
        action="store_true",
        help="skip tradesim even if proxy filter beats control",
    )
    args = ap.parse_args(argv)

    proxy = run_vol_filter_experiment(prereg_path=args.prereg)
    print(json.dumps({"proxy": proxy}, indent=2, default=str))
    if not proxy.get("success"):
        print("proxy filter did not beat control — no tradesim escalation", flush=True)
        return 0
    if args.no_tradesim:
        print("proxy FILTER_BEATS_CONTROL — tradesim skipped by flag", flush=True)
        return 0
    print("proxy FILTER_BEATS_CONTROL — escalating to tradesim", flush=True)
    ts = run_vol_filter_tradesim(prereg_path=args.prereg)
    print(json.dumps({"tradesim": ts}, indent=2, default=str))
    return 0 if ts.get("status") == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
