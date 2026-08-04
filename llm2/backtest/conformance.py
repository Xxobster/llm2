"""Tradesim conformance wrapper — run before quoting any backtest numbers."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

TRADESIM_ROOT = Path(r"C:\projects\botsgeneral\packages\tradesim")
TRADESIM_TESTS = TRADESIM_ROOT / "tests"


def run_conformance_check(*, quiet: bool = True) -> dict[str, Any]:
    """Run tradesim-conformance in a subprocess and adopt its stamp in this process."""
    try:
        from tradesim.conformance.stamp import ConformanceStamp, record_stamp
    except Exception as exc:  # noqa: BLE001
        return {"status": "unknown", "error": f"stamp import failed: {exc}", "passed": False}

    report_path = Path(tempfile.mkdtemp(prefix="llm2_conf_")) / "report.json"
    cmd = [
        sys.executable,
        "-m",
        "tradesim.conformance.checker",
        "--engine",
        "tradesim",
        "--tests",
        str(TRADESIM_TESTS),
        "--json",
        str(report_path),
        "--quiet",
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=1800,
            check=False,
            # The checker spawns a nested pytest over throwaway suites in the system temp
            # directory. Run it from the package root so pytest can express those files
            # relative to a rootdir on the same drive.
            cwd=str(TRADESIM_ROOT),
        )
    except Exception as exc:  # noqa: BLE001
        return {"status": "error", "error": str(exc), "passed": False}

    stamp_dict: dict[str, Any] | None = None
    if report_path.exists():
        try:
            stamp_dict = json.loads(report_path.read_text(encoding="utf-8"))["stamp"]
        except Exception:  # noqa: BLE001
            stamp_dict = None

    passed = False
    if stamp_dict is not None:
        fields = set(ConformanceStamp.__dataclass_fields__)
        stamp = ConformanceStamp(
            **{k: (tuple(v) if k == "unsatisfied" else v)
               for k, v in stamp_dict.items() if k in fields}
        )
        # record_stamp is process-local, so the subprocess verdict has to be replayed here
        # for assert_quotable and for simulations launched afterwards.
        record_stamp(stamp)
        passed = stamp.is_green

    out = {
        "status": "ok" if proc.returncode == 0 else "fail",
        "returncode": proc.returncode,
        "passed": passed,
        "stamp": stamp_dict,
    }
    if not quiet:
        out["stdout"] = proc.stdout[-4000:]
        out["stderr"] = proc.stderr[-2000:]
    return out


def ensure_green_stamp() -> dict[str, Any]:
    """Fail closed unless conformance is green in this process after checker run."""
    result = run_conformance_check(quiet=True)
    if not result.get("passed"):
        raise RuntimeError(f"tradesim conformance not green: {result}")
    return result
