"""Day-long tip-identity watcher for all active 94.x arms (pivot + inventory).

Polls every poll_min minutes, runs fleet parity, appends a sitrep JSONL, and
refuses to treat research Profit Factor (PF) as live edge while tip identity
is not green for the watch window.

  python scripts/watch_fleet_tip_identity_day.py --hours 24 --poll-min 15
  python scripts/watch_fleet_tip_identity_day.py --hours 1 --poll-min 5 --once
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
HOST = "94.156.189.76"
REPORT_DIR = _ROOT / "artifacts" / "reports"
JSONL = REPORT_DIR / "fleet_tip_identity_day.jsonl"
LATEST = REPORT_DIR / "fleet_tip_identity_sitrep_latest.json"


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _run_fleet(n: int) -> dict:
    proc = subprocess.run(
        [
            sys.executable,
            str(_ROOT / "scripts" / "ops_fleet_live_bt_decision_parity.py"),
            "--n",
            str(int(n)),
        ],
        cwd=str(_ROOT),
        capture_output=True,
        text=True,
    )
    print(proc.stdout)
    if proc.returncode not in (0, 2):
        print(proc.stderr, file=sys.stderr)
    path = REPORT_DIR / "ops_fleet_live_bt_decision_parity_latest.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"error": "fleet_report_missing", "stdout": proc.stdout[-2000:], "rc": proc.returncode}


def _summarize(fleet: dict) -> dict:
    fam = fleet.get("families") or {}
    pivot = fam.get("pivot_llm2") or {}
    overall = fleet.get("overall") or {}
    pivot_green = pivot.get("status") == "PASS"
    struct_ok = (fam.get("structure_llm2") or {}).get("status") == "PASS_STOPPED"
    return {
        "created_utc": _now(),
        "pivot_tip_identity": pivot.get("status"),
        "pivot_all_match": pivot.get("all_match"),
        "structure_stopped": (fam.get("structure_llm2") or {}).get("status"),
        "xgb_status": (fam.get("xgb") or {}).get("status"),
        "xgb_certifiable": (fam.get("xgb") or {}).get("parity_certifiable"),
        "tsm_vpa_status": (fam.get("tsm_vpa") or {}).get("status"),
        "tsm_chandelier_status": (fam.get("tsm_chandelier") or {}).get("status"),
        "all_certifiable_live_eq_bt": overall.get("all_certifiable_live_eq_bt"),
        "judge_research_pf_allowed": bool(pivot_green and struct_ok),
        "note": (
            "Do not judge pivot edge from research stack PF until tip identity "
            "stays green for a full calendar day of this watcher."
            if not pivot_green
            else "Pivot tip identity PASS on this sample; keep watching for full day."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=24.0)
    ap.add_argument("--poll-min", type=float, default=15.0)
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--once", action="store_true")
    args = ap.parse_args()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    deadline = time.time() + float(args.hours) * 3600.0
    greens = 0
    polls = 0
    while True:
        polls += 1
        fleet = _run_fleet(args.n)
        sitrep = _summarize(fleet)
        sitrep["poll"] = polls
        sitrep["host"] = HOST
        with JSONL.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(sitrep, default=str) + "\n")
        # cumulative day status
        if sitrep.get("pivot_tip_identity") == "PASS" and sitrep.get(
            "structure_stopped"
        ) == "PASS_STOPPED":
            greens += 1
        day = {
            **sitrep,
            "polls": polls,
            "green_polls": greens,
            "green_ratio": (greens / polls) if polls else 0.0,
            "full_day_green": bool(
                polls >= max(1, int((args.hours * 60) / max(args.poll_min, 1)) - 1)
                and greens == polls
            ),
            "jsonl": str(JSONL),
        }
        LATEST.write_text(json.dumps(day, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(day, indent=2))
        if args.once or time.time() >= deadline:
            break
        time.sleep(max(30.0, float(args.poll_min) * 60.0))
    return 0 if greens == polls and polls > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
