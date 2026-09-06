"""Upload missing live_guards.py after the sizing deploy ImportError. Do not flatten."""

from __future__ import annotations

import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

from llm2.live.certificate import refuse_vps_deploy_without_live_certificate
from llm2.paths import ROOT
from llm2.registry.ledger import append_ledger

SSH = "ln2"
HOST = "212.73.150.178"
BTC_CERT = ROOT / "configs" / "live" / "btc_1h_quad_slope_follow_xxobster11_ln2_certificate.yaml"
SOL_CERT = ROOT / "configs" / "live" / "sol_1h_fvg_confluence_xxobster11_ln2_certificate.yaml"
LOCAL_GUARDS = ROOT / "llm2" / "ml_lab" / "live_guards.py"
REMOTE_GUARDS = (
    "/opt/llm2-structure/llm2/ml_lab/live_guards.py",
    "/opt/llm2-quad-btc-1h/llm2/ml_lab/live_guards.py",
    "/opt/llm2-fvg-sol-1h/llm2/ml_lab/live_guards.py",
)


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


def _snap() -> str:
    return subprocess.check_output(
        [
            "ssh",
            "-o", "BatchMode=yes", "-o", "ConnectTimeout=25", SSH,
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
    if "def refuse_venue_min_qty_fallback" not in LOCAL_GUARDS.read_text(encoding="utf-8"):
        raise SystemExit("local live_guards.py missing refuse_venue_min_qty_fallback")

    print("LAYOUT", _ssh_out(
        "echo BTC=$(readlink -f /opt/llm2-quad-btc-1h/llm2); "
        "echo SOL=$(readlink -f /opt/llm2-fvg-sol-1h/llm2); "
        "echo STR=$(readlink -f /opt/llm2-structure/llm2); "
        "ls -ld /opt/llm2-quad-btc-1h/llm2 /opt/llm2-fvg-sol-1h/llm2 /opt/llm2-structure/llm2; "
        "systemctl is-active llm2-quad-btc-1h.service llm2-fvg-sol-1h.service; "
        "systemctl show llm2-quad-btc-1h.service llm2-fvg-sol-1h.service -p ActiveState -p SubState -p NRestarts -p Result"
    ), flush=True)
    print("BEFORE", _snap(), flush=True)

    seen: set[str] = set()
    for remote in REMOTE_GUARDS:
        resolved = _ssh_out(f"readlink -f {remote} || echo {remote}").strip()
        if resolved in seen:
            print("skip duplicate", remote, "->", resolved, flush=True)
            continue
        seen.add(resolved)
        _ssh(f"mkdir -p {remote.rsplit('/', 1)[0]}")
        _scp(LOCAL_GUARDS, remote)
        print("uploaded", remote, flush=True)

    print("IMPORT", _ssh_out(
        "export PYTHONPATH=/opt/llm2-quad-btc-1h:/opt/llm2-structure:"
        "/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:"
        "/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src; "
        "/opt/llm2-quad-btc-1h/venv/bin/python -c "
        "\"from llm2.ml_lab.live_guards import refuse_venue_min_qty_fallback; "
        "from llm2.live.ema_stack_runner import load_pack; "
        "from pathlib import Path; "
        "b=load_pack(Path('/opt/llm2-quad-btc-1h/pack')); "
        "s=load_pack(Path('/opt/llm2-fvg-sol-1h/pack')); "
        "print('import_ok', b['idea'], b['sizing']['mode'], b['sizing'].get('qty_round'), "
        "s['idea'], s['sizing']['mode'])\""
    ), flush=True)

    print("restart SOL then BTC", flush=True)
    _ssh("systemctl restart llm2-fvg-sol-1h.service")
    time.sleep(4)
    _ssh("systemctl restart llm2-quad-btc-1h.service")
    time.sleep(10)
    print("ACTIVE", _ssh_out("systemctl is-active llm2-quad-btc-1h.service llm2-fvg-sol-1h.service"), flush=True)
    print("AFTER", _snap(), flush=True)
    print("BTC LOG", _ssh_out("tail -n 16 /opt/llm2-quad-btc-1h/logs/ema_live.log"), flush=True)
    print("SOL LOG", _ssh_out("tail -n 16 /opt/llm2-fvg-sol-1h/logs/ema_live.log"), flush=True)
    append_ledger(
        "FORMULA_LIVE_GUARDS_FIX refuse_venue_min_qty_fallback uploaded; "
        f"btc=RISK_FRACTION qty_round=nearest sol=MIN_EXCHANGE host={HOST} "
        f"account=Xxobster11 at={datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} "
        "RESEARCH_ONLY do_not_flatten",
        tier=2,
    )
    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
