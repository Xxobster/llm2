"""Track-3 gate: engine conformance + structure leakage before any new model hunt.

Activates only if Track1/2 leave no pack-eligible winners (see settle/transfer reports).
Does not open the candidate hunt — only stamps readiness of engines.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import tradesim  # noqa: E402

# Prefer botsgeneral leakage onto sys.path (same pattern as tradesim).
_bg_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _bg_leak.is_dir() and str(_bg_leak) not in sys.path:
    sys.path.insert(0, str(_bg_leak))
try:
    from leakage.ensure_source import prefer_botsgeneral_leakage  # noqa: E402

    prefer_botsgeneral_leakage()
except Exception:  # noqa: BLE001
    pass

import leakage  # noqa: E402

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

GEN = "structure_v1_target_align_calibration_001"
REPORT = ARTIFACTS / "reports" / f"{GEN}_engine_gate_latest.json"
SETTLE = ARTIFACTS / "reports" / "structure_v1_clarity_hold12_outer_settle_001_latest.json"
TRANSFER = ARTIFACTS / "reports" / "structure_v1_btc_sol_cluster_double_transfer_001_latest.json"


def _track12_insufficient() -> tuple[bool, dict]:
    info: dict = {"settle": None, "transfer": None}
    n_eligible = 0
    if SETTLE.is_file():
        s = json.loads(SETTLE.read_text(encoding="utf-8"))
        info["settle"] = {
            "n_pack_eligible": (s.get("verdict") or {}).get("n_pack_eligible"),
            "n_pass_gates": (s.get("verdict") or {}).get("n_pass_gates"),
            "summary": s.get("summary"),
        }
        n_eligible += int((s.get("verdict") or {}).get("n_pack_eligible") or 0)
    if TRANSFER.is_file():
        t = json.loads(TRANSFER.read_text(encoding="utf-8"))
        info["transfer"] = t.get("verdict")
        cand = (t.get("verdict") or {}).get("settle_candidates") or []
        # transfer winners are RESEARCH_ONLY until settle — still "progress" if any
        info["transfer_n_k5"] = len(cand)
    # Insufficient for promotion if no pack-eligible settle and no transfer winner
    transfer_wins = int(info.get("transfer_n_k5") or 0)
    insufficient = n_eligible == 0 and transfer_wins == 0
    return insufficient, info


def _leakage_eth() -> dict:
    if "botsgeneral" not in str(leakage.__file__).lower():
        return {"passed": False, "error": "leakage not from botsgeneral", "file": leakage.__file__}
    from leakage.api import require_clean_audit, run_leakage_audit  # type: ignore

    ohlcv = load_ohlcv("ETHUSDT", "1h")
    lock_ms = int(__import__("pandas").Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    # Use a short recent window for speed but enough for prefix test
    ohlcv = ohlcv.tail(3000)

    def build_features(frame):
        return build_space(frame, "structure_v1", symbol="ETHUSDT", timeframe="1h")

    report = run_leakage_audit(ohlcv=ohlcv, build_features=build_features)
    try:
        require_clean_audit(report)
        passed = True
        err = None
    except Exception as exc:  # noqa: BLE001
        passed = False
        err = f"{type(exc).__name__}: {exc}"
    return {
        "passed": passed,
        "error": err,
        "file": leakage.__file__,
        "summary": getattr(report, "to_dict", lambda: str(report))(),
    }


def main() -> int:
    if "botsgeneral" not in str(tradesim.__file__).lower():
        raise SystemExit(f"tradesim not botsgeneral: {tradesim.__file__}")

    conf = run_conformance_check()
    insufficient, t12 = _track12_insufficient()
    leak: dict = {"skipped": True}
    activate_hunt = False
    note = ""
    if not insufficient:
        note = (
            "Tracks 1–2 produced pack-eligible or transfer winners; "
            "Track-3 hunt stays PREREG_ONLY (do not open candidate space)."
        )
    else:
        note = "Tracks 1–2 insufficient for promotion; engine gate required before hunt activation."
        try:
            leak = _leakage_eth()
        except Exception as exc:  # noqa: BLE001
            leak = {"passed": False, "error": f"{type(exc).__name__}: {exc}"}
        activate_hunt = bool(conf.get("passed") is not False and leak.get("passed"))

    payload = {
        "generation_id": GEN,
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "evidence_class": "ENGINE_GATE_PRE_HUNT",
        "track12": t12,
        "track12_insufficient_for_promotion": insufficient,
        "tradesim_file": tradesim.__file__,
        "leakage_file": leakage.__file__,
        "conformance": conf,
        "leakage": {
            k: v
            for k, v in leak.items()
            if k != "summary" or not isinstance(v, dict) or len(str(v)) < 5000
        },
        "activate_hunt": activate_hunt,
        "note": note,
        "max_readiness": "RESEARCH_ONLY",
        "no_live_deploy": True,
    }
    # shrink leakage summary if huge
    if isinstance(payload["leakage"].get("summary"), dict):
        payload["leakage"]["summary_keys"] = list(payload["leakage"]["summary"].keys())[:20]
        payload["leakage"].pop("summary", None)

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(json.dumps({k: payload[k] for k in (
        "track12_insufficient_for_promotion", "activate_hunt", "note",
        "conformance", "activate_hunt"
    ) if k in payload}, indent=2, default=str))
    print(f"conformance_passed={conf.get('passed')} leak={leak.get('passed')} wrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
