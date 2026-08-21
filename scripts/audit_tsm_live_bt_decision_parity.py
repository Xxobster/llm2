"""TSM VPA + Chandelier live vs BT / tip-identity audit (VPS /opt/tsm-*).

  python scripts/audit_tsm_live_bt_decision_parity.py --local-vps
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
HOST = "94.156.189.76"

FAMILIES = (
    {
        "name": "tsm_vpa",
        "root": Path("/opt/tsm-vpa"),
        "expected_pack": "live_top4_stack2_rr15_v1",
    },
    {
        "name": "tsm_chandelier",
        "root": Path("/opt/tsm-chandelier"),
        "expected_pack": None,
    },
)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _probe(name: str, root: Path, expected_pack: str | None) -> dict[str, Any]:
    out: dict[str, Any] = {
        "family": name,
        "root": str(root),
        "pairs": [],
        "blockers": [],
        "parity_certifiable": False,
    }
    if not root.is_dir():
        out["status"] = "MISSING_ROOT"
        out["blockers"].append(f"{root} missing")
        return out

    cfg_dir = root / "configs"
    packs = sorted(cfg_dir.glob("*.json")) if cfg_dir.is_dir() else []
    live_packs = [
        p
        for p in packs
        if "live" in p.name.lower() and "shadow" not in p.name.lower()
    ]
    chosen = None
    for p in live_packs or packs:
        d = json.loads(p.read_text(encoding="utf-8"))
        if expected_pack and expected_pack not in (
            d.get("pack_id"),
            p.stem,
            p.name,
        ):
            if expected_pack not in p.name and d.get("pack_id") != expected_pack:
                continue
        chosen = (p, d)
        if str(d.get("mode", "")).upper() == "LIVE":
            break
    if chosen is None and packs:
        p = live_packs[0] if live_packs else packs[0]
        chosen = (p, json.loads(p.read_text(encoding="utf-8")))
    if chosen is None:
        out["status"] = "MISSING_PACK"
        out["blockers"].append("no configs/*.json")
        return out

    path, pack = chosen
    out["pack_path"] = str(path)
    out["pack_id"] = pack.get("pack_id")
    out["mode"] = pack.get("mode")
    out["readiness_earned"] = pack.get("readiness_earned")
    out["strategy"] = pack.get("strategy")
    out["symbols"] = pack.get("symbols")
    out["timeframe"] = pack.get("timeframe")
    out["candles_exchange"] = pack.get("candles_exchange")
    out["freeze_ref"] = pack.get("freeze_ref")
    out["evidence_contamination"] = pack.get("evidence_contamination")

    if str(pack.get("mode", "")).upper() != "LIVE":
        out["blockers"].append(f"pack mode={pack.get('mode')} not LIVE")

    freeze = pack.get("freeze_ref")
    freeze_ok = False
    if freeze:
        for c in (
            Path(freeze),
            root / freeze,
            root / "artifacts" / Path(freeze).name,
            Path("/opt") / Path(freeze),
        ):
            if c.is_file():
                out["freeze_path_resolved"] = str(c)
                freeze_ok = True
                break
        if not freeze_ok:
            out["blockers"].append(f"freeze_ref missing on disk: {freeze}")
    else:
        out["blockers"].append("pack has no freeze_ref")

    data = root / "data"
    shared_dbs = []
    if data.is_dir():
        shared_dbs = sorted(
            p
            for p in data.rglob("*.sqlite")
            if "live" in p.name.lower() or "state" in p.name.lower()
        )
    for sym in pack.get("symbols") or []:
        row: dict[str, Any] = {"symbol": sym}
        dbs = list(data.rglob("*.sqlite")) if data.is_dir() else []
        prefer = [d for d in dbs if sym in d.name] + [
            d for d in shared_dbs if d not in [x for x in dbs if sym in d.name]
        ]
        tip_n = 0
        tip_recent: list[tuple] = []
        used_db = None
        for db in prefer or dbs:
            try:
                con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
                tables = [
                    r[0]
                    for r in con.execute(
                        "SELECT name FROM sqlite_master WHERE type='table'"
                    ).fetchall()
                ]
                if "events" not in tables:
                    con.close()
                    continue
                n = con.execute(
                    "SELECT COUNT(*) FROM events WHERE symbol=? AND kind='tip_decide'",
                    (sym,),
                ).fetchone()[0]
                recent = con.execute(
                    "SELECT ts_utc, detail_json FROM events "
                    "WHERE symbol=? AND kind='tip_decide' ORDER BY id DESC LIMIT 3",
                    (sym,),
                ).fetchall()
                con.close()
                if n > tip_n:
                    tip_n, tip_recent, used_db = n, recent, db
                    row["tables"] = tables
            except Exception as exc:  # noqa: BLE001
                row.setdefault("db_errors", []).append({"db": str(db), "err": str(exc)})
        if used_db is None and not dbs:
            row["status"] = "NO_STATE_DB"
            out["blockers"].append(f"{name}:{sym} no state db")
            out["pairs"].append(row)
            continue
        row["state_db"] = str(used_db) if used_db else (str(dbs[0]) if dbs else None)
        row["tip_decide_n"] = tip_n
        row["tip_decide_recent"] = [
            {"ts_utc": r[0], "detail": json.loads(r[1])} for r in tip_recent
        ]
        if tip_n <= 0:
            row["tip_identity"] = "LEDGER_WIRED_WAITING_NEXT_CYCLE"
            row["status"] = "FAIL_NO_TIP_DECIDE_YET"
            out["blockers"].append(
                f"{name}:{sym} tip_decide events not written yet (waiting next closed bar)"
            )
        else:
            has_tip = any(
                (r.get("detail") or {}).get("tip_ohlc") for r in row["tip_decide_recent"]
            )
            if has_tip:
                row["tip_identity"] = "LEDGER_TIP_OHLC_PRESENT"
                row["status"] = "PARTIAL"
                out["blockers"].append(
                    f"{name}:{sym} tip_decide ledger green but freeze/BT replay not certified"
                )
            else:
                row["tip_identity"] = "LEDGER_WITHOUT_TIP_OHLC"
                row["status"] = "FAIL"
                out["blockers"].append(f"{name}:{sym} tip_decide missing tip_ohlc")
        out["pairs"].append(row)

    try:
        ps = subprocess.check_output(
            ["bash", "-lc", f"pgrep -af '{name}|tsm-|run_live_bot' || true"],
            text=True,
        )
        out["processes"] = [ln for ln in ps.splitlines() if ln.strip()][:30]
    except Exception as exc:  # noqa: BLE001
        out["processes_error"] = str(exc)

    out["status"] = "FAIL"
    out["why"] = (
        "TSM tip identity requires freeze candles + decide ledger with tip OHLC "
        "and a shared replay path. Pack/process inventory alone is not live≡BT."
    )
    return out


def _scan_local() -> dict[str, Any]:
    report: dict[str, Any] = {
        "created_utc": _now(),
        "families": {},
        "blockers": [],
        "parity_certifiable": False,
    }
    for fam in FAMILIES:
        row = _probe(fam["name"], fam["root"], fam["expected_pack"])
        report["families"][fam["name"]] = row
        report["blockers"].extend(row.get("blockers") or [])
    report["status"] = "FAIL" if report["blockers"] else "PASS"
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--local-vps", action="store_true")
    args = ap.parse_args()
    out_local = (
        _ROOT / "artifacts" / "reports" / "audit_tsm_live_bt_decision_parity_latest.json"
    )
    if not args.local_vps:
        subprocess.check_call(
            ["scp", str(Path(__file__)), f"root@{HOST}:/tmp/audit_tsm_live_bt_decision_parity.py"]
        )
        subprocess.check_call(
            [
                "ssh",
                f"root@{HOST}",
                "python3 /tmp/audit_tsm_live_bt_decision_parity.py --local-vps",
            ]
        )
        subprocess.check_call(
            [
                "scp",
                f"root@{HOST}:/tmp/audit_tsm_live_bt_decision_parity_latest.json",
                str(out_local),
            ]
        )
        print("synced", out_local)
        return 0
    report = _scan_local()
    path = Path("/tmp/audit_tsm_live_bt_decision_parity_latest.json")
    path.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": report.get("status"),
                "blockers": report.get("blockers")[:20],
                "n_blockers": len(report.get("blockers") or []),
            },
            indent=2,
        )
    )
    print("wrote", path)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
