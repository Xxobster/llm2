"""Watch pivot LIVE units for N new 15m DECIDE events; run tip parity after each.

Usage:
  python scripts/watch_pivot_live_closes.py --closes 3
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

HOST = "94.156.189.76"
SOL_LOG = "/opt/llm2-pivot-sol-geo-p75-w4/logs/pivot_live.log"
ETH_LOG = "/opt/llm2-pivot-eth-p75-ctrl-atr-w4/logs/pivot_live.log"
DECIDE_RE = re.compile(r"DECIDE (\{.*\})")


def _ssh(cmd: str) -> str:
    return subprocess.check_output(["ssh", f"root@{HOST}", cmd], text=True, errors="replace")


def _tail_decides(log: str, n: int = 20) -> list[dict]:
    out = _ssh(f"grep ' DECIDE ' {log} | tail -n {n}")
    rows = []
    for line in out.splitlines():
        m = DECIDE_RE.search(line)
        if not m:
            continue
        try:
            payload = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        rows.append(payload)
    return rows


def _latest_bar(log: str) -> int | None:
    rows = _tail_decides(log, 5)
    if not rows:
        return None
    return int(rows[-1].get("bar_ts_ms") or 0) or None


def _run_parity() -> dict:
    env = dict(**{**dict(**__import__("os").environ), "PYTHONPATH": str(_ROOT)})
    proc = subprocess.run(
        [sys.executable, str(_ROOT / "scripts" / "ops_pivot_live_parity_once.py")],
        cwd=str(_ROOT),
        env=env,
        capture_output=True,
        text=True,
    )
    print(proc.stdout)
    if proc.returncode not in (0, 2):
        print(proc.stderr, file=sys.stderr)
    path = _ROOT / "artifacts" / "reports" / "ops_pivot_live_parity_latest.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}


def _check_fill_state() -> dict:
    py = r"""
import json, sqlite3, os, sys
sys.path[:0]=['/opt/llm2-pivot-sol-geo-p75-w4','/opt/llm2-structure']
os.environ['TRADING_SECRETS_ENV']='/root/.trading/secrets.env'
os.environ['PYTHONPATH']='/opt/llm2-pivot-sol-geo-p75-w4:/opt/llm2-structure:/opt/botsgeneral/packages/tradesim/src'
from llm2.live.micro_runner import _load_account_keys, _position_list
_load_account_keys('Xxobster7')
out={}
for root,sym in (
 ('/opt/llm2-pivot-sol-geo-p75-w4','SOLUSDT'),
 ('/opt/llm2-pivot-eth-p75-ctrl-atr-w4','ETHUSDT'),
):
 con=sqlite3.connect(root+'/state/pivot_live_state.sqlite')
 last=con.execute('SELECT bar_ts_ms,payload_json FROM pivot_decisions ORDER BY bar_ts_ms DESC LIMIT 1').fetchone()
 orders=con.execute('SELECT order_id,payload_json FROM pivot_orders ORDER BY created_utc DESC LIMIT 3').fetchall()
 working=con.execute(\"SELECT v FROM pivot_state WHERE k='working_order_id'\").fetchone()
 pos=_position_list(account='Xxobster7', symbol=sym)
 open_pos=[p for p in pos if float(p.get('size') or 0)>0]
 out[sym]={
  'last_bar': None if not last else last[0],
  'last_action': None if not last else json.loads(last[1]).get('action'),
  'working_order_id': None if not working else working[0],
  'recent_orders':[{'id':o[0],'payload':json.loads(o[1])} for o in orders],
  'open_positions':[{'side':p.get('side'),'size':p.get('size'),'leverage':p.get('leverage'),'tp':p.get('takeProfit'),'sl':p.get('stopLoss'),'tpslMode':p.get('tpslMode')} for p in open_pos],
 }
print(json.dumps(out))
"""
    # Prefer remote file to avoid shell quoting pain on Windows.
    return {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--closes", type=int, default=3)
    ap.add_argument("--poll-sec", type=int, default=30)
    args = ap.parse_args()

    base_sol = _latest_bar(SOL_LOG)
    base_eth = _latest_bar(ETH_LOG)
    print(
        json.dumps(
            {
                "start_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "base_sol_bar": base_sol,
                "base_eth_bar": base_eth,
                "target_closes": args.closes,
            },
            indent=2,
        )
    )
    seen = 0
    last_pair = (base_sol, base_eth)
    report: list[dict] = []
    while seen < args.closes:
        time.sleep(args.poll_sec)
        sol = _latest_bar(SOL_LOG)
        eth = _latest_bar(ETH_LOG)
        active = _ssh(
            "systemctl is-active llm2-pivot-sol-geo-p75-w4 llm2-pivot-eth-p75-ctrl-atr-w4"
        ).strip().splitlines()
        order_hits = _ssh(
            "grep -E 'ORDER_RESULT|ENTER_LIMIT|TPSL_|CANCEL|LIMIT_' "
            f"{SOL_LOG} {ETH_LOG} | tail -n 20 || true"
        )
        if (sol, eth) != last_pair and sol is not None and eth is not None:
            if sol != last_pair[0] or eth != last_pair[1]:
                # count when both advanced or either new decide beyond base
                if sol != base_sol or eth != base_eth:
                    if sol != last_pair[0] and eth != last_pair[1]:
                        seen += 1
                        last_pair = (sol, eth)
                        print(
                            f"\n=== close #{seen} sol_bar={sol} eth_bar={eth} "
                            f"units={active} ===",
                            flush=True,
                        )
                        sol_d = _tail_decides(SOL_LOG, 1)[-1]
                        eth_d = _tail_decides(ETH_LOG, 1)[-1]
                        print("SOL", json.dumps(sol_d)[:500], flush=True)
                        print("ETH", json.dumps(eth_d)[:500], flush=True)
                        if order_hits.strip():
                            print("ORDER_HITS\n", order_hits, flush=True)
                        parity = _run_parity()
                        row = {
                            "n": seen,
                            "sol": sol_d,
                            "eth": eth_d,
                            "parity_all_match": parity.get("all_match"),
                            "parity_rows": parity.get("rows"),
                            "units_active": active,
                            "order_hits": order_hits.strip().splitlines()[-10:],
                        }
                        report.append(row)
                        out = _ROOT / "artifacts" / "reports" / "watch_pivot_live_closes_latest.json"
                        out.write_text(
                            json.dumps(
                                {
                                    "updated_utc": datetime.now(timezone.utc).strftime(
                                        "%Y-%m-%dT%H:%M:%SZ"
                                    ),
                                    "closes_seen": seen,
                                    "report": report,
                                },
                                indent=2,
                            )
                            + "\n",
                            encoding="utf-8",
                        )
        else:
            print(
                f"{datetime.now(timezone.utc).strftime('%H:%M:%SZ')} waiting "
                f"seen={seen}/{args.closes} sol={sol} eth={eth} units={active}",
                flush=True,
            )
            if order_hits.strip():
                print(order_hits, flush=True)

    print(json.dumps({"done": True, "closes_seen": seen}, indent=2))
    return 0 if all(r.get("parity_all_match") for r in report) else 2


if __name__ == "__main__":
    raise SystemExit(main())
