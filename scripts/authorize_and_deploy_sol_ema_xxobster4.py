"""Replace Xxobster4 diagonal bots with Solana 1h EMA stack on live-network-1.

User 2026-09-01: deploy Post-Only 5% equity stop-risk. Flatten leftover ETH DSR
exposure first (naked short, no stop). Do not start until four-proof certificate
is AUTHORIZED.
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.live.certificate import refuse_vps_deploy_without_live_certificate  # noqa: E402
from llm2.paths import ARTIFACTS, ROOT  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402

HOST = "94.156.189.76"
SSH = "ln1"
ACCOUNT = "Xxobster4"
PACK = ARTIFACTS / "live_packs" / "sol_1h_power_ema_stack_long"
CERT = ROOT / "configs" / "live" / "sol_1h_power_ema_stack_long_xxobster4_ln1_certificate.yaml"
REMOTE = "/opt/llm2-ema-sol-1h"
UNIT = "llm2-ema-sol-1h"
DSR_UNITS = ("llm2-dsr-eth-bu-1h", "llm2-dsr-sol-bu-1h")
START_DATE = "2026-09-01"


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


def _tar_upload(local_dir: Path, remote_dir: str) -> None:
    _ssh(f"mkdir -p {remote_dir}")
    _ssh(f"rm -rf {remote_dir}/*")
    cmd = (
        f"tar -C \"{local_dir}\" --exclude=__pycache__ --exclude=*.pyc "
        f"--exclude=*.sqlite-wal --exclude=*.sqlite-shm -cf - . "
        f"| ssh -o BatchMode=yes {SSH} \"tar -C {remote_dir} -xf -\""
    )
    subprocess.check_call(cmd, shell=True)


def _flatten_eth_orphan() -> None:
    """Close the leftover ETH short on Xxobster4 (no stop attached)."""
    py = r'''
import json, os
os.environ["TRADESIM_NO_PLOT"] = "1"
from llm2.live.micro_runner import _position_list, close_reduce_only, fetch_wallet_equity_usdt
print("equity", round(fetch_wallet_equity_usdt(account="Xxobster4"), 4))
for sym in ("ETHUSDT", "SOLUSDT"):
    rows = _position_list(account="Xxobster4", symbol=sym)
    for p in rows:
        size = float(p.get("size") or 0)
        side = str(p.get("side") or "")
        if size <= 0 or side not in ("Buy", "Sell"):
            continue
        side_i = 1 if side == "Buy" else -1
        resp = close_reduce_only(account="Xxobster4", symbol=sym, side=side_i, qty=size)
        print("FLATTEN", json.dumps({"symbol": sym, "side": side, "qty": size, "retCode": resp.get("retCode"), "retMsg": resp.get("retMsg")}))
    left = [p for p in _position_list(account="Xxobster4", symbol=sym) if float(p.get("size") or 0) > 0]
    print("LEFT", sym, json.dumps([{k: x.get(k) for k in ("side","size","stopLoss")} for x in left]))
'''
    env = (
        "export PYTHONPATH=/opt/llm2-dsr-eth-bu-1h:/opt/llm2-structure:"
        "/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:"
        "/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src; "
        "export TRADING_SECRETS_ENV=/root/.trading/secrets.env; export TRADESIM_NO_PLOT=1; "
        "python3 -"
    )
    print(_ssh_in(env, py), flush=True)


def _stop_dsr() -> None:
    units = " ".join(DSR_UNITS)
    _ssh(f"systemctl disable --now {units} || true")
    _ssh(f"systemctl is-active {units} || true")


def _register_bots() -> None:
    script = r'''
from pathlib import Path
import yaml
p = Path("/opt/botsgeneral/config/bots_registry.yaml")
raw = yaml.safe_load(p.read_text()) or {}
bots = raw.setdefault("bots", {})
for dead in ("llm2_dsr_eth_bu_1h", "llm2_dsr_sol_bu_1h"):
    bots.pop(dead, None)
bots["llm2_ema_sol_1h"] = {
    "serve_candles": True,
    "exchange": "binance",
    "account": "Xxobster4",
    "symbols": ["SOLUSDT"],
    "timeframe": "1h",
    "min_history_bars": 3000,
    "also_fetch_timeframes": ["1m"],
    "min_history_bars_by_tf": {"1h": 3000, "1m": 500},
    "path": "/opt/llm2-ema-sol-1h",
    "path_local": "D:/projects/LLM2",
    "local_pack_roots": ["D:/projects/LLM2/artifacts/live_packs/sol_1h_power_ema_stack_long"],
    "parser": "none",
    "process_match": ["--pack /opt/llm2-ema-sol-1h/pack", "ema_stack_runner"],
    "systemd_match": ["llm2-ema-sol-1h"],
    "screen_match": ["llm2-ema-sol-1h"],
    "start_date": "2026-09-01",
    "authorized_from_utc": "2026-09-01T00:00:00Z",
    "notes": "SOL 1h power_ema_stack_long Post-Only; 5% equity stop-risk floored to 0.1; lev13 from 3% cap; start 2026-09-01; RESEARCH_ONLY",
}
host = raw.setdefault("vps", {}).setdefault("94.156.189.76", {})
bl = [n for n in list(host.get("bots") or []) if n not in ("llm2_dsr_eth_bu_1h", "llm2_dsr_sol_bu_1h")]
if "llm2_ema_sol_1h" not in bl:
    bl.append("llm2_ema_sol_1h")
host["bots"] = bl
raw.pop("hosts", None)
p.write_text(yaml.safe_dump(raw, sort_keys=False))
print("registry_vps_bots", bl)
'''
    print(_ssh_in("python3 -", script), flush=True)


def _write_unit() -> None:
    unit_body = f"""[Unit]
Description=LLM2 SOL 1h EMA stack Post-Only 5pct stop-risk Xxobster4
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
        ["ssh", "-o", "BatchMode=yes", SSH, f"cat > /etc/systemd/system/{UNIT}.service <<'EOF'\n{unit_body}\nEOF"]
    )


def main() -> int:
    refuse_vps_deploy_without_live_certificate(path=CERT, host=HOST)
    stored = (PACK / "pack_hash.txt").read_text(encoding="utf-8").strip()
    cert_text = CERT.read_text(encoding="utf-8")
    if stored not in cert_text:
        raise SystemExit(f"pack_hash.txt {stored} missing from certificate")
    fp = stored

    print("FLATTEN leftover Xxobster4 exposure …", flush=True)
    _flatten_eth_orphan()

    print("STOP DSR units …", flush=True)
    _stop_dsr()

    print("UPLOAD pack + llm2 …", flush=True)
    _ssh(f"mkdir -p {REMOTE}/{{pack,state,logs}} && ln -sfn /opt/llm2-structure/venv {REMOTE}/venv")
    _tar_upload(ROOT / "llm2", "/opt/llm2-structure/llm2")
    _ssh(f"ln -sfn /opt/llm2-structure/llm2 {REMOTE}/llm2")
    _tar_upload(PACK, f"{REMOTE}/pack")
    subprocess.check_call(["scp", str(CERT), f"{SSH}:{REMOTE}/certificate.yaml"])

    print("SYSTEMD enable …", flush=True)
    _write_unit()
    _ssh(f"systemctl daemon-reload && systemctl enable --now {UNIT}.service")
    _register_bots()

    import time

    time.sleep(3)
    active = _ssh_out(f"systemctl is-active {UNIT}.service").strip()
    print("ACTIVE", active, flush=True)
    print(_ssh_out(f"tail -n 40 {REMOTE}/logs/ema_live.log"), flush=True)
    if active != "active":
        print(_ssh_out(f"journalctl -u {UNIT} -n 80 --no-pager"), flush=True)
        raise SystemExit(f"{UNIT} not active")

    print("ONCE smoke …", flush=True)
    print(
        _ssh_out(
            f"cd {REMOTE} && PYTHONPATH={REMOTE}:/opt/llm2-structure:"
            "/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:"
            "/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src "
            f"{REMOTE}/venv/bin/python -m llm2.live.ema_stack_runner --pack {REMOTE}/pack "
            f"--state {REMOTE}/state/ema_live_state.sqlite --once"
        ),
        flush=True,
    )

    append_ledger(
        f"EMA_STACK_LIVE_AUTH arm={PACK.name} account={ACCOUNT} host={HOST} "
        f"hash={fp[:16]} start={START_DATE} risk_fraction=0.05 lev=13 four_proof_ok=true "
        f"replaced DSR eth+sol; flattened leftover ETH short before stop",
        tier=2,
    )
    print("DONE", datetime.now(timezone.utc).isoformat(), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
