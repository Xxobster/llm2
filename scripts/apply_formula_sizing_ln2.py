"""Push sizing-only pack+runner changes to ln2. Restart both formula units.

Bitcoin is in a 0.001 long: restart the unit so the next entry uses 5% nearest-step
size. Do not flatten. Solana is flat: venue-minimum lot going forward.
"""

from __future__ import annotations

import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

from llm2.live.certificate import refuse_vps_deploy_without_live_certificate
from llm2.paths import ARTIFACTS, ROOT
from llm2.registry.ledger import append_ledger

SSH = "ln2"
HOST = "212.73.150.178"
BTC_CERT = ROOT / "configs" / "live" / "btc_1h_quad_slope_follow_xxobster11_ln2_certificate.yaml"
SOL_CERT = ROOT / "configs" / "live" / "sol_1h_fvg_confluence_xxobster11_ln2_certificate.yaml"


def _ssh(cmd: str) -> None:
    subprocess.check_call(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=25", SSH, cmd])


def _ssh_out(cmd: str) -> str:
    return subprocess.check_output(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=25", SSH, cmd],
        text=True,
    )


def _scp(local: Path, remote: str) -> None:
    subprocess.check_call(
        ["scp", "-o", "BatchMode=yes", "-o", "ConnectTimeout=25", str(local), f"{SSH}:{remote}"]
    )


def _tar_pack(local: Path, remote: str) -> None:
    _ssh(f"mkdir -p {remote}")
    cmd = (
        f'tar -C "{local}" --exclude=__pycache__ -cf - . '
        f'| ssh -o BatchMode=yes -o ConnectTimeout=25 {SSH} "tar -C {remote} -xf -"'
    )
    subprocess.check_call(cmd, shell=True)


def _snap() -> str:
    return subprocess.check_output(
        [
            "ssh",
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=25",
            SSH,
            "export TRADING_SECRETS_ENV=/root/.trading/secrets.env "
            "PYTHONPATH=/opt/llm2-quad-btc-1h:/opt/llm2-structure:"
            "/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:"
            "/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src; "
            "/opt/llm2-quad-btc-1h/venv/bin/python -",
        ],
        input="""
from llm2.live.micro_runner import fetch_wallet_equity_usdt, _position_list, _list_open_orders, _list_stop_orders

def snap(a, s):
    eq = fetch_wallet_equity_usdt(account=a)
    pos = [(p.get("side"), float(p.get("size") or 0), p.get("avgPrice")) for p in _position_list(account=a, symbol=s) if float(p.get("size") or 0) > 0]
    n = sl = 0
    for o in list(_list_open_orders(account=a, symbol=s)) + list(_list_stop_orders(account=a, symbol=s)):
        if str(o.get("orderStatus") or "") in ("Filled", "Cancelled", "Deactivated"):
            continue
        n += 1
        if str(o.get("reduceOnly")).lower() in ("true", "1"):
            sl += 1
    print(a, s, "eq", round(eq, 4), "pos", pos, "working", n, "reduce_only", sl)

snap("Xxobster11", "BTCUSDT")
snap("Xxobster11", "SOLUSDT")
""",
        text=True,
    )


def main() -> int:
    refuse_vps_deploy_without_live_certificate(path=BTC_CERT, host=HOST, account="Xxobster11")
    refuse_vps_deploy_without_live_certificate(path=SOL_CERT, host=HOST, account="Xxobster11")
    btc_hash = (ARTIFACTS / "live_packs" / "btc_1h_quad_slope_follow" / "pack_hash.txt").read_text().strip()
    sol_hash = (ARTIFACTS / "live_packs" / "sol_1h_fvg_confluence" / "pack_hash.txt").read_text().strip()
    if btc_hash not in BTC_CERT.read_text(encoding="utf-8"):
        raise SystemExit("BTC pack_hash missing from certificate")
    if sol_hash not in SOL_CERT.read_text(encoding="utf-8"):
        raise SystemExit("SOL pack_hash missing from certificate")

    print("BEFORE", _snap(), flush=True)
    for rel in (
        "llm2/sizing_policy.py",
        "llm2/live/micro_runner.py",
        "llm2/live/ema_stack_runner.py",
    ):
        _scp(ROOT / rel, f"/opt/llm2-structure/{rel}")
        print("uploaded", rel, flush=True)

    _tar_pack(ARTIFACTS / "live_packs" / "btc_1h_quad_slope_follow", "/opt/llm2-quad-btc-1h/pack")
    _tar_pack(ARTIFACTS / "live_packs" / "sol_1h_fvg_confluence", "/opt/llm2-fvg-sol-1h/pack")
    _scp(BTC_CERT, "/opt/llm2-quad-btc-1h/certificate.yaml")
    _scp(SOL_CERT, "/opt/llm2-fvg-sol-1h/certificate.yaml")

    print("restart SOL then BTC", flush=True)
    _ssh("systemctl restart llm2-fvg-sol-1h.service")
    time.sleep(4)
    _ssh("systemctl restart llm2-quad-btc-1h.service")
    time.sleep(8)
    print("ACTIVE", _ssh_out("systemctl is-active llm2-quad-btc-1h.service llm2-fvg-sol-1h.service"))
    print("PACK SIZING", _ssh_out("python3 -c \"import json; b=json.load(open('/opt/llm2-quad-btc-1h/pack/strategy.json')); s=json.load(open('/opt/llm2-fvg-sol-1h/pack/strategy.json')); print('btc', b['sizing']); print('sol', s['sizing'])\""))
    print("AFTER", _snap(), flush=True)
    print("BTC LOG", _ssh_out("tail -n 8 /opt/llm2-quad-btc-1h/logs/ema_live.log"), flush=True)
    print("SOL LOG", _ssh_out("tail -n 8 /opt/llm2-fvg-sol-1h/logs/ema_live.log"), flush=True)
    append_ledger(
        f"FORMULA_SIZING_LIVE btc=RISK_FRACTION qty_round=nearest hash={btc_hash[:16]} "
        f"sol=MIN_EXCHANGE hash={sol_hash[:16]} host={HOST} account=Xxobster11 "
        f"at={datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} RESEARCH_ONLY",
        tier=2,
    )
    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
