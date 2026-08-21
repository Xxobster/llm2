"""Multi-bar pivot live decision vs identical tip_decide recompute (BT path).

Pulls last N decisions from VPS state DBs, rebuilds OHLCV tip via the same
live candle loader (Binance shared/REST), truncates to each decision bar, and
re-runs tip_decide with the pack on the VPS. Exact match required on action,
p_any, side, limit_px (within 1e-9 / 1 tick).

  python scripts/audit_pivot_live_bt_decision_parity.py
  # or on VPS:
  PYTHONPATH=/opt/llm2-pivot-sol-geo-p75-w4:/opt/llm2-structure:... \\
    python scripts/audit_pivot_live_bt_decision_parity.py --local-vps
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.live.pivot_runner import (  # noqa: E402
    LIVE_OHLCV_BARS,
    load_pack,
    load_pivot_ohlcv,
    tip_decide,
)
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

HOST = "94.156.189.76"
ARMS = (
    {
        "name": "sol",
        "remote_root": "/opt/llm2-pivot-sol-geo-p75-w4",
        "pack_local": ARTIFACTS / "live_packs" / "pivot_sol_geo_tp1_sl1_p75_w4",
    },
    {
        "name": "eth",
        "remote_root": "/opt/llm2-pivot-eth-p75-ctrl-atr-w4",
        "pack_local": ARTIFACTS / "live_packs" / "pivot_eth_p75_ctrl_atr_w4",
    },
)


def _ssh_decisions(remote_root: str, n: int) -> list[dict]:
    py = (
        "import sqlite3,json;"
        f"c=sqlite3.connect('{remote_root}/state/pivot_live_state.sqlite');"
        "rows=c.execute('SELECT bar_ts_ms,payload_json FROM pivot_decisions "
        f"ORDER BY bar_ts_ms DESC LIMIT {int(n)}').fetchall();"
        "print(json.dumps([{'bar_ts_ms':r[0],'payload':json.loads(r[1])} for r in rows]))"
    )
    out = subprocess.check_output(
        ["ssh", f"root@{HOST}", f"python3 -c {json.dumps(py)}"],
        text=True,
        timeout=120,
    )
    return json.loads(out.strip() or "[]")


def _local_vps_decisions(remote_root: str, n: int) -> list[dict]:
    con = sqlite3.connect(f"{remote_root}/state/pivot_live_state.sqlite")
    rows = con.execute(
        "SELECT bar_ts_ms, payload_json FROM pivot_decisions "
        "ORDER BY bar_ts_ms DESC LIMIT ?",
        (int(n),),
    ).fetchall()
    return [{"bar_ts_ms": r[0], "payload": json.loads(r[1])} for r in rows]


def _recompute_at_bar(
    pack_dir: Path, bar_ts_ms: int, tip_ohlc: dict | None = None
) -> dict:
    strat, blob = load_pack(pack_dir)
    ohlcv = load_pivot_ohlcv(
        str(strat["symbol"]), str(strat["timeframe"]), limit=LIVE_OHLCV_BARS + 50
    )
    ts = index_to_ms(ohlcv.index)
    mask = ts <= int(bar_ts_ms)
    if not np.any(mask):
        raise RuntimeError(f"no bars <= {bar_ts_ms}")
    frame = ohlcv.loc[mask].copy()
    if len(frame) > LIVE_OHLCV_BARS:
        frame = frame.iloc[-LIVE_OHLCV_BARS:].copy()
    tip = int(index_to_ms(frame.index)[-1])
    if tip != int(bar_ts_ms):
        raise RuntimeError(f"tip {tip} != want {bar_ts_ms} (missing closed bar)")
    # Bind tip to the candle values frozen in the live ledger (forensic identity).
    if tip_ohlc:
        for col in ("open", "high", "low", "close", "volume"):
            if col in tip_ohlc and col in frame.columns:
                frame.iloc[-1, frame.columns.get_loc(col)] = float(tip_ohlc[col])
    return tip_decide(ohlcv=frame, strategy=strat, blob=blob)


def _cmp(live: dict, bt: dict) -> dict:
    keys = ("action", "reason", "side", "p_any", "p_any_raw", "limit_px", "thr_any", "close")
    diffs = {}
    ok = True
    for k in keys:
        lv, bv = live.get(k), bt.get(k)
        if isinstance(lv, (int, float)) or isinstance(bv, (int, float)):
            if lv is None or bv is None:
                match = lv == bv
            elif not np.isfinite(float(lv)) or not np.isfinite(float(bv)):
                match = lv == bv
            else:
                # limit_px / close: loose relative; probs: 1e-9 abs
                if k in ("limit_px", "close"):
                    match = abs(float(lv) - float(bv)) <= max(
                        1e-8 * abs(float(bv)), 1e-8
                    )
                else:
                    match = abs(float(lv) - float(bv)) < 1e-9
        else:
            match = lv == bv
        if not match:
            ok = False
            diffs[k] = {"live": lv, "bt": bv}
    # Forensic: tip candle identity when live persisted tip_ohlc
    tip = live.get("tip_ohlc") or {}
    if tip and bt.get("tip_ohlc"):
        for k in ("open", "high", "low", "close"):
            if k not in tip or k not in bt["tip_ohlc"]:
                continue
            if abs(float(tip[k]) - float(bt["tip_ohlc"][k])) > max(
                abs(float(bt["tip_ohlc"][k])) * 1e-8, 1e-8
            ):
                ok = False
                diffs[f"tip_ohlc.{k}"] = {
                    "live": tip[k],
                    "bt": bt["tip_ohlc"][k],
                }
    return {"match": ok, "diffs": diffs}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=8)
    ap.add_argument(
        "--local-vps",
        action="store_true",
        help="Read state DBs on this host (run on VPS).",
    )
    args = ap.parse_args()

    report = {
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "n_requested": args.n,
        "arms": [],
        "all_match": True,
    }
    for arm in ARMS:
        if args.local_vps:
            lives = _local_vps_decisions(arm["remote_root"], args.n)
            pack = Path(arm["remote_root"]) / "pack"
        else:
            lives = _ssh_decisions(arm["remote_root"], args.n)
            pack = arm["pack_local"]
        rows = []
        for item in sorted(lives, key=lambda x: int(x["bar_ts_ms"])):
            bar = int(item["bar_ts_ms"])
            live = item["payload"]
            try:
                bt = _recompute_at_bar(pack, bar, tip_ohlc=live.get("tip_ohlc"))
                cmp = _cmp(live, bt)
            except Exception as exc:  # noqa: BLE001
                cmp = {"match": False, "diffs": {"error": str(exc)}, "bt": None}
                bt = {"error": str(exc)}
            rows.append(
                {
                    "bar_ts_ms": bar,
                    "match": cmp["match"],
                    "diffs": cmp.get("diffs"),
                    "live_action": live.get("action"),
                    "live_p_any": live.get("p_any"),
                    "bt_action": bt.get("action") if isinstance(bt, dict) else None,
                    "bt_p_any": bt.get("p_any") if isinstance(bt, dict) else None,
                }
            )
            if not cmp["match"]:
                report["all_match"] = False
            print(
                arm["name"],
                bar,
                "OK" if cmp["match"] else "DIFF",
                live.get("action"),
                live.get("p_any"),
                cmp.get("diffs") or "",
            )
        report["arms"].append(
            {
                "arm": arm["name"],
                "n": len(rows),
                "n_match": sum(1 for r in rows if r["match"]),
                "rows": rows,
            }
        )

    out = ARTIFACTS / "reports" / "audit_pivot_live_bt_decision_parity_latest.json"
    if args.local_vps:
        out = Path("/tmp/audit_pivot_live_bt_decision_parity_latest.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print("wrote", out, "all_match", report["all_match"])
    return 0 if report["all_match"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
