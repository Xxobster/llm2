"""Move llm2-fvg-sol-1h from Xxobster3 onto Xxobster11 on live-network-2.

User 2026-09-04: share Xxobster11 for Bitcoin 1h quad_slope_follow and Solana
1h Fair Value Gap confluence. Do not restart the Bitcoin unit (open 0.001
long + stop). Solana on Xxobster3 is flat.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.live.certificate import refuse_vps_deploy_without_live_certificate  # noqa: E402
from llm2.paths import ROOT  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402

HOST = "212.73.150.178"
SSH = "ln2"
REMOTE = "/opt/llm2-fvg-sol-1h"
UNIT = "llm2-fvg-sol-1h"
BOT_ID = "llm2_fvg_sol_1h"
ACCOUNT = "Xxobster11"
OLD_ACCOUNT = "Xxobster3"
BTC_UNIT = "llm2-quad-btc-1h"
CERT = ROOT / "configs" / "live" / "sol_1h_fvg_confluence_xxobster11_ln2_certificate.yaml"
PACK_HASH = ROOT / "artifacts" / "live_packs" / "sol_1h_fvg_confluence" / "pack_hash.txt"


def _ssh(cmd: str) -> None:
    subprocess.check_call(["ssh", "-o", "BatchMode=yes", SSH, cmd])


def _ssh_out(cmd: str) -> str:
    return subprocess.check_output(["ssh", "-o", "BatchMode=yes", SSH, cmd], text=True)


def _ssh_in(cmd: str, script: str) -> str:
    return subprocess.check_output(
        ["ssh", "-o", "BatchMode=yes", SSH, cmd],
        input=script,
        text=True,
    )


def _write_sol_unit() -> None:
    unit_body = f"""[Unit]
Description=LLM2 sol_1h_fvg_confluence Post-Only 5pct stop-risk {ACCOUNT}
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory={REMOTE}
Environment=PYTHONPATH={REMOTE}:/opt/llm2-structure:/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src
Environment=SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db
Environment=TRADING_SECRETS_ENV=/root/.trading/secrets.env
Environment=TRADESIM_NO_PLOT=1
ExecStart={REMOTE}/venv/bin/python -u -m llm2.live.ema_stack_runner --pack {REMOTE}/pack --state {REMOTE}/state/ema_live_state.sqlite --mode LIVE --live-orders --account {ACCOUNT} --cert {REMOTE}/certificate.yaml --vps-host {HOST}
Restart=always
RestartSec=10
StandardOutput=append:{REMOTE}/logs/ema_live.log
StandardError=append:{REMOTE}/logs/ema_live.log

[Install]
WantedBy=multi-user.target
"""
    subprocess.check_call(
        [
            "ssh",
            "-o",
            "BatchMode=yes",
            SSH,
            f"cat > /etc/systemd/system/{UNIT}.service <<'EOF'\n{unit_body}\nEOF",
        ]
    )


def _register_bots() -> None:
    script = f"""
from pathlib import Path
import yaml
p = Path("/opt/botsgeneral/config/bots_registry.yaml")
raw = yaml.safe_load(p.read_text()) or {{}}
bots = raw.setdefault("bots", {{}})
row = dict(bots.get({BOT_ID!r}) or {{}})
row["account"] = {ACCOUNT!r}
row["notes"] = (
    "SOL 1h fvg_confluence Post-Only long-only; 5% equity stop-risk; "
    "lev13 from 3% cap; shared Xxobster11 with BTC quad_slope; "
    "RESEARCH_ONLY nested FAIL; skip if below venue min"
)
bots[{BOT_ID!r}] = row
p.write_text(yaml.safe_dump(raw, sort_keys=False))
print("bot_account", bots[{BOT_ID!r}].get("account"))
rp = Path("/etc/botsgeneral/report.yaml")
rep = yaml.safe_load(rp.read_text()) or {{}}
print("since_by_bot", (rep.get("since_by_bot") or {{}}).get({BOT_ID!r}))
"""
    print(_ssh_in("python3 -", script), flush=True)


def _exchange_snap() -> str:
    return _ssh_out(
        """
export TRADING_SECRETS_ENV=/root/.trading/secrets.env
export PYTHONPATH=/opt/llm2-fvg-sol-1h:/opt/llm2-structure:/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src
/opt/llm2-fvg-sol-1h/venv/bin/python - <<'PY'
from llm2.live.micro_runner import fetch_wallet_equity_usdt, _position_list, _list_open_orders, _list_stop_orders

def snap(account, symbol):
    eq = fetch_wallet_equity_usdt(account=account)
    pos = []
    for p in _position_list(account=account, symbol=symbol):
        sz = float(p.get("size") or 0)
        if sz <= 0:
            continue
        pos.append((p.get("side"), sz, p.get("avgPrice")))
    n_ord = 0
    n_sl = 0
    for o in list(_list_open_orders(account=account, symbol=symbol)) + list(_list_stop_orders(account=account, symbol=symbol)):
        if str(o.get("orderStatus") or "") in {"Filled", "Cancelled", "Deactivated"}:
            continue
        n_ord += 1
        if str(o.get("reduceOnly")).lower() in {"true", "1"}:
            n_sl += 1
    print(account, symbol, "eq", round(eq, 4), "pos", pos, "working_or_stops", n_ord, "reduce_only", n_sl)

for acc, sym in [
    ("Xxobster11", "BTCUSDT"),
    ("Xxobster11", "SOLUSDT"),
    ("Xxobster3", "SOLUSDT"),
]:
    snap(acc, sym)
PY
"""
    )


def main() -> int:
    refuse_vps_deploy_without_live_certificate(
        path=CERT, host=HOST, account=ACCOUNT
    )
    stored = PACK_HASH.read_text(encoding="utf-8").strip()
    if stored not in CERT.read_text(encoding="utf-8"):
        raise SystemExit(f"pack_hash.txt {stored} missing from {CERT.name}")

    btc_before = _ssh_out(f"systemctl is-active {BTC_UNIT}.service").strip()
    if btc_before != "active":
        raise SystemExit(f"{BTC_UNIT} is {btc_before}; refusing to move Solana")
    print("BEFORE", _exchange_snap(), flush=True)

    print("UPLOAD llm2 package (Bitcoin process stays running) …", flush=True)
    subprocess.check_call(
        f'tar -C "{ROOT / "llm2"}" --exclude=__pycache__ --exclude=*.pyc -cf - . '
        f'| ssh -o BatchMode=yes {SSH} "tar -C /opt/llm2-structure/llm2 -xf -"',
        shell=True,
    )
    subprocess.check_call(["scp", str(CERT), f"{SSH}:{REMOTE}/certificate.yaml"])
    _write_sol_unit()
    _register_bots()

    print(f"STOP {UNIT} (Bitcoin unit untouched) …", flush=True)
    _ssh(f"systemctl stop {UNIT}.service")
    _ssh("systemctl daemon-reload")
    _ssh(f"systemctl enable --now {UNIT}.service")
    time.sleep(5)

    sol_active = _ssh_out(f"systemctl is-active {UNIT}.service").strip()
    btc_after = _ssh_out(f"systemctl is-active {BTC_UNIT}.service").strip()
    print(f"ACTIVE {UNIT}={sol_active} {BTC_UNIT}={btc_after}", flush=True)
    if sol_active != "active":
        print(_ssh_out(f"journalctl -u {UNIT} -n 80 --no-pager"), flush=True)
        raise SystemExit(f"{UNIT} not active")
    if btc_after != "active":
        raise SystemExit(f"{BTC_UNIT} left {btc_after}")

    acct_line = _ssh_out(f"grep ExecStart /etc/systemd/system/{UNIT}.service").strip()
    if f"--account {ACCOUNT}" not in acct_line:
        raise SystemExit(f"systemd account not {ACCOUNT}: {acct_line}")
    if OLD_ACCOUNT in acct_line:
        raise SystemExit(f"systemd still names {OLD_ACCOUNT}")

    print("AFTER", _exchange_snap(), flush=True)
    print(_ssh_out(f"tail -n 20 {REMOTE}/logs/ema_live.log"), flush=True)

    append_ledger(
        f"FORMULA_LIVE_MOVE sol_1h_fvg_confluence {OLD_ACCOUNT}->{ACCOUNT} "
        f"unit={UNIT} host={HOST} pack_hash={stored[:16]} "
        "btc_unit_untouched=llm2-quad-btc-1h RESEARCH_ONLY nested_settle=FAIL",
        tier=2,
    )
    print("DONE", datetime.now(timezone.utc).isoformat(), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
