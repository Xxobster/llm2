"""CLI: log a research peek or seed known multitrade peeks."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.evidence.peek_log import (  # noqa: E402
    append_peek,
    default_peek_log_path,
    read_peeks,
    seed_known_multitrade_peeks,
)
from llm2.paths import FORWARD_LOCKBOX_START, POST_MULTITRADE_FREEZE_START  # noqa: E402
from llm2.research_policy import (  # noqa: E402
    PolicyError,
    classify_evidence_for_window,
    refuse_copy_as_pristine_holdout,
    refuse_lockbox_multitrade_knob_as_promotion,
)


def main() -> int:
    ap = argparse.ArgumentParser(description="Research peek log (contamination is explicit)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("seed", help="Seed D-035/D-036 known peeks (idempotent)")
    s.add_argument("--force", action="store_true")

    a = sub.add_parser("append", help="Append one peek")
    a.add_argument("--experiment-id", required=True)
    a.add_argument("--window-start", default=FORWARD_LOCKBOX_START)
    a.add_argument("--window-end", required=True)
    a.add_argument("--purpose", required=True)
    a.add_argument("--arms", default="")
    a.add_argument("--n-arms", type=int, default=None)
    a.add_argument("--notes", default="")
    a.add_argument(
        "--evidence-class",
        default=None,
        help="default: auto-classify from window",
    )

    l = sub.add_parser("list", help="Print peeks")
    l.add_argument("--last", type=int, default=20)

    c = sub.add_parser("check-promote", help="Refuse if claim is lockbox multitrade promotion")
    c.add_argument("--claim", required=True)
    c.add_argument("--evidence-class", default="LOCKBOX_OPENED_CONTAMINATED")
    c.add_argument("--window-start", default=FORWARD_LOCKBOX_START)
    c.add_argument("--window-end", default=POST_MULTITRADE_FREEZE_START)
    c.add_argument(
        "--claimed-copy-pristine",
        action="store_true",
        help="also trigger copy-as-pristine refusal",
    )

    args = ap.parse_args()
    if args.cmd == "seed":
        n = seed_known_multitrade_peeks(force=bool(args.force))
        print(f"seeded={n} log={default_peek_log_path()}")
        print(f"POST_MULTITRADE_FREEZE_START={POST_MULTITRADE_FREEZE_START}")
        return 0
    if args.cmd == "append":
        ec = args.evidence_class or classify_evidence_for_window(
            window_start=args.window_start,
            window_end=args.window_end,
        )
        rec = append_peek(
            experiment_id=args.experiment_id,
            window_start=args.window_start,
            window_end=args.window_end,
            purpose=args.purpose,
            arms=args.arms or None,
            n_arms=args.n_arms,
            notes=args.notes,
            evidence_class=ec,
        )
        print(json.dumps(rec, indent=2))
        return 0
    if args.cmd == "list":
        peeks = read_peeks()
        for r in peeks[-int(args.last) :]:
            print(
                f"{r.get('ts_utc')} | {r.get('experiment_id')} | "
                f"{r.get('window_start')}→{r.get('window_end')} | {r.get('purpose')} | "
                f"{r.get('evidence_class')}"
            )
        print(f"n={len(peeks)} log={default_peek_log_path()}")
        return 0
    if args.cmd == "check-promote":
        try:
            if args.claimed_copy_pristine:
                refuse_copy_as_pristine_holdout(
                    claimed_pristine=True, same_calendar_window=True
                )
            refuse_lockbox_multitrade_knob_as_promotion(
                claim=args.claim,
                evidence_class=args.evidence_class,
                window_start=args.window_start,
                window_end=args.window_end,
            )
        except PolicyError as exc:
            print(f"REFUSED: {exc}")
            return 2
        print("OK (not a contaminated multitrade promotion claim under given stamps)")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
