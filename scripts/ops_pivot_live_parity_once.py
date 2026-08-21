"""One-shot tip parity: VPS pivot state tip vs local recompute on Binance REST tip.

Does not authorize or place orders. Run after each 15m close:
  python scripts/ops_pivot_live_parity_once.py
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from llm2.live.pivot_runner import load_pack, load_pivot_ohlcv, tip_decide
from llm2.paths import ARTIFACTS, ROOT

HOST = "94.156.189.76"
ARMS = (
    {
        "name": "sol",
        "pack": ARTIFACTS / "live_packs" / "pivot_sol_geo_tp1_sl1_p75_w4",
        "remote_state": "/opt/llm2-pivot-sol-geo-p75-w4/state/pivot_live_state.sqlite",
    },
    {
        "name": "eth",
        "pack": ARTIFACTS / "live_packs" / "pivot_eth_p75_ctrl_atr_w4",
        "remote_state": "/opt/llm2-pivot-eth-p75-ctrl-atr-w4/state/pivot_live_state.sqlite",
    },
)


def _remote_tip(state_path: str) -> dict:
    py = (
        "import sqlite3,json;"
        f"c=sqlite3.connect('{state_path}');"
        "r=c.execute('SELECT bar_ts_ms,payload_json FROM pivot_decisions "
        "ORDER BY bar_ts_ms DESC LIMIT 1').fetchone();"
        "print(json.dumps({'bar_ts_ms':r[0],'payload':json.loads(r[1])}) if r else '{}')"
    )
    out = subprocess.check_output(
        ["ssh", f"root@{HOST}", f"python3 -c {json.dumps(py)}"],
        text=True,
    )
    return json.loads(out.strip() or "{}")


def main() -> int:
    rows = []
    for arm in ARMS:
        live = _remote_tip(arm["remote_state"])
        strat, blob = load_pack(arm["pack"])
        ohlcv = load_pivot_ohlcv(str(strat["symbol"]), str(strat["timeframe"]))
        local = tip_decide(ohlcv=ohlcv, strategy=strat, blob=blob)
        live_p = (live.get("payload") or {}).get("p_any")
        local_p = local.get("p_any")
        live_bar = live.get("bar_ts_ms")
        local_bar = local.get("bar_ts_ms")
        match = (
            live_bar == local_bar
            and live_p is not None
            and local_p is not None
            and abs(float(live_p) - float(local_p)) < 1e-9
            and (live.get("payload") or {}).get("action") == local.get("action")
        )
        rows.append(
            {
                "arm": arm["name"],
                "match": match,
                "live_bar_ts_ms": live_bar,
                "local_bar_ts_ms": local_bar,
                "live_p_any": live_p,
                "local_p_any": local_p,
                "live_action": (live.get("payload") or {}).get("action"),
                "local_action": local.get("action"),
            }
        )
        print(json.dumps(rows[-1], indent=2))
    out = {
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "all_match": all(r["match"] for r in rows),
        "rows": rows,
    }
    path = ARTIFACTS / "reports" / "ops_pivot_live_parity_latest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("wrote", path, "all_match", out["all_match"])
    return 0 if out["all_match"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
