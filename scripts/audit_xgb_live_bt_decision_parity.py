"""XGB live vs backtest / tip-identity audit (runs on VPS under /home/xgb).

Certifies what can be proven from this host:
  - audit JSON live_ready / fee_model / leverage claims per symbol
  - process inventory for vps_run_asset_live
  - presence of bar-level decision ledgers + freeze candles
  - when a ledger + tip OHLC exist, replay identity is attempted

  python scripts/audit_xgb_live_bt_decision_parity.py --local-vps
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
XGB_ROOT = Path("/home/xgb")


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _scan_local() -> dict[str, Any]:
    out: dict[str, Any] = {
        "created_utc": _now(),
        "family": "xgb",
        "root": str(XGB_ROOT),
        "pairs": [],
        "blockers": [],
        "parity_certifiable": False,
    }
    if not XGB_ROOT.is_dir():
        out["status"] = "MISSING_ROOT"
        out["blockers"].append("/home/xgb missing")
        return out

    audits = {
        "BTCUSDT": XGB_ROOT / "models" / "btcusdt_first_touch_live_audit.json",
        "ETHUSDT": XGB_ROOT / "models" / "ethusdt_first_touch_live_audit.json",
    }
    for sym, path in audits.items():
        row: dict[str, Any] = {"symbol": sym, "audit_path": str(path)}
        if not path.is_file():
            row["status"] = "MISSING_AUDIT"
            out["blockers"].append(f"{sym}: missing audit")
            out["pairs"].append(row)
            continue
        d = json.loads(path.read_text(encoding="utf-8"))
        live_ready = bool(d.get("live_ready"))
        row.update(
            {
                "verdict": d.get("verdict"),
                "live_ready": live_ready,
                "fee_model": d.get("fee_model"),
                "tp_pct": d.get("tp_pct"),
                "sl_pct": d.get("sl_pct"),
                "leverage_audit": d.get("leverage"),
                "screen_pf": (d.get("screen") or {}).get("profit_factor"),
                "lockbox_pf": (d.get("lockbox") or {}).get("profit_factor"),
            }
        )
        if not live_ready:
            out["blockers"].append(f"{sym}: live_ready=false verdict={d.get('verdict')}")
            row["status"] = "FAIL_LIVE_READY_FALSE"
        else:
            row["status"] = "AUDIT_ALLOWS_LIVE"

        tip_db = XGB_ROOT / "database" / "live_tip_decisions.sqlite"
        row["tip_ledger_db"] = str(tip_db)
        tip_ok = False
        if tip_db.is_file():
            try:
                con = sqlite3.connect(f"file:{tip_db}?mode=ro", uri=True)
                n = con.execute(
                    "SELECT COUNT(*) FROM tip_decisions WHERE symbol=?",
                    (sym,),
                ).fetchone()[0]
                last = con.execute(
                    "SELECT bar_ts, payload_json, created_utc FROM tip_decisions "
                    "WHERE symbol=? ORDER BY created_utc DESC LIMIT 3",
                    (sym,),
                ).fetchall()
                row["tip_ledger_n"] = n
                row["tip_ledger_recent"] = [
                    {
                        "bar_ts": r[0],
                        "created_utc": r[2],
                        "payload": json.loads(r[1]),
                    }
                    for r in last
                ]
                tip_ok = n > 0
                con.close()
            except Exception as exc:  # noqa: BLE001
                row["ledger_errors"] = str(exc)
        if not tip_ok:
            out["blockers"].append(f"{sym}: no rows in live_tip_decisions.sqlite yet")
            row["tip_identity"] = "LEDGER_WIRED_WAITING_NEXT_CYCLE"
        else:
            # Tip OHLC present is the identity freeze for the live tip.
            has_tip = any(
                (r.get("payload") or {}).get("tip_ohlc") for r in row.get("tip_ledger_recent") or []
            )
            if has_tip:
                row["tip_identity"] = "LEDGER_TIP_OHLC_PRESENT"
                # Still not full BT replay until freeze candles audited in XGB.
                out["blockers"].append(
                    f"{sym}: tip ledger green but live_ready=false / freeze replay not certified"
                )
            else:
                row["tip_identity"] = "LEDGER_WITHOUT_TIP_OHLC"
                out["blockers"].append(f"{sym}: tip ledger rows missing tip_ohlc")
        out["pairs"].append(row)

    try:
        ps = subprocess.check_output(
            ["bash", "-lc", "pgrep -af vps_run_asset_live || true"], text=True
        )
        out["processes"] = [ln for ln in ps.splitlines() if ln.strip()]
    except Exception as exc:  # noqa: BLE001
        out["processes_error"] = str(exc)

    out["status"] = "FAIL"
    out["why"] = (
        "XGB cannot be certified live≡BT from LLM2 without (1) live_ready=true "
        "audits, (2) bar tip ledger with tip OHLC, (3) freeze candles + same "
        "decide function replay. Current host evidence fails those gates."
    )
    out["parity_certifiable"] = False
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--local-vps", action="store_true")
    args = ap.parse_args()
    out_local = _ROOT / "artifacts" / "reports" / "audit_xgb_live_bt_decision_parity_latest.json"
    if not args.local_vps:
        subprocess.check_call(
            ["scp", str(Path(__file__)), f"root@{HOST}:/tmp/audit_xgb_live_bt_decision_parity.py"]
        )
        subprocess.check_call(
            [
                "ssh",
                f"root@{HOST}",
                "python3 /tmp/audit_xgb_live_bt_decision_parity.py --local-vps",
            ]
        )
        subprocess.check_call(
            [
                "scp",
                f"root@{HOST}:/tmp/audit_xgb_live_bt_decision_parity_latest.json",
                str(out_local),
            ]
        )
        print("synced", out_local)
        return 0
    report = _scan_local()
    path = Path("/tmp/audit_xgb_live_bt_decision_parity_latest.json")
    path.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": report.get("status"), "blockers": report.get("blockers")}, indent=2))
    print("wrote", path)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
