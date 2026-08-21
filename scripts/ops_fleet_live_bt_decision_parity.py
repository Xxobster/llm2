"""Fleet live↔BT / tip-identity parity for all active 94.x strategies+pairs.

Runs on the VPS (preferred) or via SSH wrappers from the workstation.

Arms covered:
  - LLM2 pivot SOL/ETH 15m (tip_decide recompute vs state ledger)
  - XGB BTC/ETH (audit claims + live state/events if present)
  - TSM VPA + TSM Chandelier (pack claims + state DB events vs freeze refs)

Does not authorize live. Writes:
  artifacts/reports/ops_fleet_live_bt_decision_parity_latest.json
  (or /tmp/... when --local-vps)

  python scripts/ops_fleet_live_bt_decision_parity.py --local-vps
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
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

HOST = "94.156.189.76"


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _run_pivot_local(n: int) -> dict[str, Any]:
    # Import after path setup; prefer VPS pack paths when present.
    from llm2.live.pivot_runner import (  # noqa: WPS433
        LIVE_OHLCV_BARS,
        load_pack,
        load_pivot_ohlcv,
        tip_decide,
    )
    from llm2.validation.folds import index_to_ms  # noqa: WPS433

    arms = (
        ("sol", Path("/opt/llm2-pivot-sol-geo-p75-w4")),
        ("eth", Path("/opt/llm2-pivot-eth-p75-ctrl-atr-w4")),
    )
    out: dict[str, Any] = {"family": "pivot_llm2", "arms": []}
    all_ok = True
    for name, root in arms:
        state = root / "state" / "pivot_live_state.sqlite"
        pack = root / "pack"
        if not state.is_file() or not pack.is_dir():
            out["arms"].append({"arm": name, "error": "missing_pack_or_state"})
            all_ok = False
            continue
        con = sqlite3.connect(str(state))
        rows = con.execute(
            "SELECT bar_ts_ms, payload_json FROM pivot_decisions "
            "ORDER BY bar_ts_ms DESC LIMIT ?",
            (int(n),),
        ).fetchall()
        strat, blob = load_pack(pack)
        # Only score bars that already persisted tip_ohlc (post-fix decisions).
        scored = []
        for bar_ts, payload in sorted(rows, key=lambda r: int(r[0])):
            live = json.loads(payload)
            if not live.get("tip_ohlc"):
                scored.append(
                    {
                        "bar_ts_ms": bar_ts,
                        "match": None,
                        "skipped": "pre_tip_ohlc_ledger",
                        "live_action": live.get("action"),
                        "live_p_any": live.get("p_any"),
                    }
                )
                continue
            # Forensic replay: use shared/REST history for the prefix, but bind
            # tip OHLC to the values persisted at decide time (exchange tip can
            # revise later; that must not fail tip_decide identity).
            ohlcv = load_pivot_ohlcv(
                str(strat["symbol"]), str(strat["timeframe"]), limit=LIVE_OHLCV_BARS + 50
            )
            ts = index_to_ms(ohlcv.index)
            frame = ohlcv.loc[ts <= int(bar_ts)].copy()
            if len(frame) > LIVE_OHLCV_BARS:
                frame = frame.iloc[-LIVE_OHLCV_BARS:].copy()
            tip = int(index_to_ms(frame.index)[-1])
            if tip != int(bar_ts):
                scored.append(
                    {
                        "bar_ts_ms": bar_ts,
                        "match": False,
                        "error": f"tip {tip} != {bar_ts}",
                    }
                )
                all_ok = False
                continue
            tip_l = live.get("tip_ohlc") or {}
            for col in ("open", "high", "low", "close", "volume"):
                if col in tip_l and col in frame.columns:
                    frame.iloc[-1, frame.columns.get_loc(col)] = float(tip_l[col])
            bt = tip_decide(ohlcv=frame, strategy=strat, blob=blob)
            diffs = {}
            ok = True
            for k in ("action", "p_any", "close", "limit_px", "side"):
                lv, bv = live.get(k), bt.get(k)
                if isinstance(lv, float) or isinstance(bv, float):
                    if abs(float(lv) - float(bv)) > (
                        max(abs(float(bv)) * 1e-8, 1e-8)
                        if k in ("close", "limit_px")
                        else 1e-9
                    ):
                        ok = False
                        diffs[k] = {"live": lv, "bt": bv}
                elif lv != bv:
                    ok = False
                    diffs[k] = {"live": lv, "bt": bv}
            tip_b = bt.get("tip_ohlc") or {}
            for k in ("open", "high", "low", "close"):
                if k in tip_l and k in tip_b:
                    if abs(float(tip_l[k]) - float(tip_b[k])) > max(
                        abs(float(tip_b[k])) * 1e-8, 1e-8
                    ):
                        ok = False
                        diffs[f"tip_ohlc.{k}"] = {
                            "live": tip_l[k],
                            "bt": tip_b[k],
                        }
            scored.append(
                {
                    "bar_ts_ms": bar_ts,
                    "match": ok,
                    "diffs": diffs,
                    "live_action": live.get("action"),
                    "live_p_any": live.get("p_any"),
                    "bt_p_any": bt.get("p_any"),
                }
            )
            if not ok:
                all_ok = False
        post = [r for r in scored if r.get("match") is not None]
        out["arms"].append(
            {
                "arm": name,
                "symbol": strat.get("symbol"),
                "n_ledger": len(rows),
                "n_post_fix": len(post),
                "n_match": sum(1 for r in post if r.get("match")),
                "rows": scored,
            }
        )
    out["all_match"] = all_ok and all(
        (a.get("n_post_fix", 0) == 0) or (a.get("n_match") == a.get("n_post_fix"))
        for a in out["arms"]
        if "error" not in a
    )
    out["status"] = "PASS" if out["all_match"] else "FAIL"
    return out


def _probe_xgb() -> dict[str, Any]:
    root = Path("/home/xgb")
    out: dict[str, Any] = {
        "family": "xgb",
        "pairs": [],
        "status": "UNKNOWN",
        "blockers": [],
    }
    if not root.is_dir():
        out["status"] = "MISSING_ROOT"
        out["blockers"].append("/home/xgb missing")
        return out
    audits = {
        "BTCUSDT": root / "models" / "btcusdt_first_touch_live_audit.json",
        "ETHUSDT": root / "models" / "ethusdt_first_touch_live_audit.json",
    }
    for sym, path in audits.items():
        row: dict[str, Any] = {"symbol": sym, "audit": str(path)}
        if not path.is_file():
            row["status"] = "MISSING_AUDIT"
            out["blockers"].append(f"missing {path}")
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
                "status": "PASS_AUDIT_ALLOWS_LIVE"
                if live_ready
                else "FAIL_LIVE_READY_FALSE",
            }
        )
        if not live_ready:
            out["blockers"].append(
                f"{sym}: audit live_ready=false / verdict={d.get('verdict')}"
            )
        # Look for a decision ledger
        ledgers = list(root.rglob("*decision*")) + list(root.rglob("*signal*sqlite*"))
        row["ledger_candidates"] = [str(p) for p in ledgers[:20]]
        if not any(p.suffix == ".sqlite" for p in ledgers):
            out["blockers"].append(f"{sym}: no decision sqlite ledger found")
            row["tip_identity"] = "UNAVAILABLE_NO_LEDGER"
        out["pairs"].append(row)
    # Process alive?
    try:
        ps = subprocess.check_output(
            ["bash", "-lc", "pgrep -af vps_run_asset_live || true"], text=True
        )
        out["processes"] = [ln for ln in ps.splitlines() if ln.strip()]
    except Exception as exc:  # noqa: BLE001
        out["processes_error"] = str(exc)
    out["status"] = "FAIL" if out["blockers"] else "PASS"
    out["parity_certifiable"] = False
    out["why"] = (
        "XGB audits explicitly mark live_ready=false; no bar-level tip ledger "
        "was found to prove live tip_decide ≡ freeze/BT path. Fee models differ "
        "BTC(maker) vs ETH(taker)."
    )
    return out


def _probe_tsm(label: str, root: Path, expected_pack: str | None = None) -> dict[str, Any]:
    out: dict[str, Any] = {
        "family": label,
        "root": str(root),
        "pairs": [],
        "blockers": [],
        "status": "UNKNOWN",
    }
    if not root.is_dir():
        out["status"] = "MISSING_ROOT"
        out["blockers"].append(f"{root} missing")
        return out
    # Prefer LIVE pack configs
    packs = sorted((root / "configs").glob("*.json")) if (root / "configs").is_dir() else []
    live_packs = [p for p in packs if "live" in p.name.lower() and "shadow" not in p.name.lower()]
    chosen = None
    for p in live_packs or packs:
        d = json.loads(p.read_text(encoding="utf-8"))
        if expected_pack and d.get("pack_id") != expected_pack and expected_pack not in p.name:
            continue
        chosen = (p, d)
        if d.get("mode") in ("LIVE", "live"):
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
    if str(pack.get("mode", "")).upper() not in ("LIVE",):
        out["blockers"].append(f"pack mode={pack.get('mode')} not LIVE")
    if "RESEARCH_ONLY" in str(pack.get("readiness_earned", "")) and "SHADOW_READY" not in str(
        pack.get("readiness_earned", "")
    ):
        out["blockers"].append(f"readiness_earned={pack.get('readiness_earned')}")
    # freeze file presence
    freeze = pack.get("freeze_ref")
    freeze_ok = False
    if freeze:
        # try relative to root and absolute
        cands = [
            Path(freeze),
            root / freeze,
            root / "artifacts" / Path(freeze).name,
            Path("/opt") / Path(freeze),
        ]
        for c in cands:
            if c.is_file():
                out["freeze_path_resolved"] = str(c)
                freeze_ok = True
                break
        if not freeze_ok:
            out["blockers"].append(f"freeze_ref missing on disk: {freeze}")
    # per-symbol state
    data = root / "data"
    for sym in pack.get("symbols") or []:
        row: dict[str, Any] = {"symbol": sym}
        # find state db
        cands = list(data.rglob(f"*{sym}*")) if data.is_dir() else []
        cands += list(data.rglob("*.sqlite")) if data.is_dir() else []
        db = None
        for c in cands:
            if c.suffix == ".sqlite" and (sym in c.name or "live" in c.name.lower()):
                db = c
                break
        if db is None:
            for c in cands:
                if c.suffix == ".sqlite":
                    db = c
                    break
        if db is None:
            row["status"] = "NO_STATE_DB"
            out["blockers"].append(f"{label}:{sym} no state db")
            out["pairs"].append(row)
            continue
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        tables = [
            r[0]
            for r in con.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        ]
        row["state_db"] = str(db)
        row["tables"] = tables
        # tip identity unavailable without a decide payload table
        decide_tables = [t for t in tables if "decision" in t.lower() or "signal" in t.lower()]
        if not decide_tables:
            row["tip_identity"] = "UNAVAILABLE_NO_DECISION_TABLE"
            out["blockers"].append(
                f"{label}:{sym} state has {tables} but no decision/signal table"
            )
            row["status"] = "FAIL_NO_LEDGER"
        else:
            row["tip_identity"] = "LEDGER_PRESENT_NOT_REPLAYED"
            row["status"] = "PARTIAL"
            out["blockers"].append(
                f"{label}:{sym} has {decide_tables} but no BT replay harness in LLM2"
            )
        out["pairs"].append(row)
        con.close()
    try:
        ps = subprocess.check_output(
            ["bash", "-lc", f"pgrep -af '{label}|tsm-|run_live_bot' || true"],
            text=True,
        )
        out["processes"] = [ln for ln in ps.splitlines() if ln.strip()][:20]
    except Exception as exc:  # noqa: BLE001
        out["processes_error"] = str(exc)
    out["parity_certifiable"] = False
    out["status"] = "FAIL" if out["blockers"] else "PASS"
    out["why"] = (
        "Pack/process inventory only. Bar-level live tip ≡ freeze/BT recompute "
        "is not certifiable from LLM2 without a shared decide ledger + candle tip hash."
    )
    return out


def _structure_stopped() -> dict[str, Any]:
    units = [
        "llm2-structure-micro",
        "llm2-structure-eth",
        "llm2-structure-sol",
        "llm2-structure-eth-k5-double3h-v1",
        "llm2-structure-btc-k5-double3h-v1",
        "llm2-structure-sol-k5-double3h-v1",
        "llm2-structure-eth-multitrade-v1_2",
    ]
    rows = []
    for u in units:
        try:
            st = subprocess.check_output(
                ["systemctl", "is-active", u], text=True, stderr=subprocess.STDOUT
            ).strip()
        except subprocess.CalledProcessError as exc:
            raw = exc.output or ""
            if isinstance(raw, bytes):
                raw = raw.decode(errors="replace")
            st = str(raw).strip() or "inactive"
        rows.append({"unit": u, "active": st})
    any_up = any(r["active"] == "active" for r in rows)
    return {
        "family": "structure_llm2",
        "status": "FAIL_STILL_RUNNING" if any_up else "PASS_STOPPED",
        "units": rows,
        "why": "CAUS-STRUCT-001 void — must remain stopped for trading",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--local-vps", action="store_true")
    ap.add_argument("--n", type=int, default=6)
    args = ap.parse_args()
    if not args.local_vps:
        # Delegate to VPS
        remote = (
            "cd /opt/llm2-pivot-sol-geo-p75-w4 && "
            "PYTHONPATH=/opt/llm2-pivot-sol-geo-p75-w4:/opt/llm2-structure:"
            "/opt/botsgeneral/packages/live_candles/src:"
            "/opt/botsgeneral/packages/tradesim/src "
            "SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db "
            f"./venv/bin/python /tmp/ops_fleet_live_bt_decision_parity.py "
            f"--local-vps --n {int(args.n)}"
        )
        subprocess.check_call(["scp", str(Path(__file__)), f"root@{HOST}:/tmp/ops_fleet_live_bt_decision_parity.py"])
        subprocess.check_call(["ssh", f"root@{HOST}", remote])
        subprocess.check_call(
            [
                "scp",
                f"root@{HOST}:/tmp/ops_fleet_live_bt_decision_parity_latest.json",
                str(_ROOT / "artifacts" / "reports" / "ops_fleet_live_bt_decision_parity_latest.json"),
            ]
        )
        print("synced artifacts/reports/ops_fleet_live_bt_decision_parity_latest.json")
        return 0

    report = {
        "created_utc": _now(),
        "host": HOST,
        "families": {},
    }
    report["families"]["structure_llm2"] = _structure_stopped()
    report["families"]["pivot_llm2"] = _run_pivot_local(args.n)
    report["families"]["xgb"] = _probe_xgb()
    report["families"]["tsm_vpa"] = _probe_tsm(
        "tsm_vpa", Path("/opt/tsm-vpa"), expected_pack="live_top4_stack2_rr15_v1"
    )
    report["families"]["tsm_chandelier"] = _probe_tsm(
        "tsm_chandelier", Path("/opt/tsm-chandelier")
    )
    # overall: pivot post-fix must pass; structure must be stopped; others reported
    pivot_ok = report["families"]["pivot_llm2"].get("status") == "PASS"
    struct_ok = report["families"]["structure_llm2"].get("status") == "PASS_STOPPED"
    report["overall"] = {
        "pivot_tip_identity": report["families"]["pivot_llm2"].get("status"),
        "structure_stopped": report["families"]["structure_llm2"].get("status"),
        "xgb_certifiable": report["families"]["xgb"].get("parity_certifiable"),
        "tsm_vpa_certifiable": report["families"]["tsm_vpa"].get("parity_certifiable"),
        "tsm_chandelier_certifiable": report["families"]["tsm_chandelier"].get(
            "parity_certifiable"
        ),
        "all_certifiable_live_eq_bt": bool(
            pivot_ok
            and struct_ok
            and report["families"]["xgb"].get("parity_certifiable")
            and report["families"]["tsm_vpa"].get("parity_certifiable")
            and report["families"]["tsm_chandelier"].get("parity_certifiable")
        ),
    }
    out = Path("/tmp/ops_fleet_live_bt_decision_parity_latest.json")
    out.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps(report["overall"], indent=2))
    print("wrote", out)
    return 0 if pivot_ok and struct_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
