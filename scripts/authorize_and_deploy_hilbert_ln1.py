"""Deploy Solana 1-hour Hilbert always-fade to live-network-1.

User 2026-09-04: free Xxobster on 94.156.189.76, same operational pattern as
Solana Fair Value Gap (Post-Only, 5% equity stop-risk, floor to 0.1, skip below
min, leverage 13x). Nested subset PASS is not Shadow-Ready. Do not stop
existing live units (EMA stack, pivots, chandelier, TSM-VPA).
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
from llm2.paths import ARTIFACTS, ROOT  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402

HOST = "94.156.189.76"
SSH = "ln1"
ACCOUNT = "Xxobster3"
SLUG = "sol_1h_hilbert_amp_fade"
REMOTE = "/opt/llm2-hilbert-sol-1h"
UNIT = "llm2-hilbert-sol-1h"
BOT_ID = "llm2_hilbert_sol_1h"
PACK = ARTIFACTS / "live_packs" / SLUG
CERT = ROOT / "configs" / "live" / "sol_1h_hilbert_amp_fade_xxobster3_ln1_certificate.yaml"
PACK_LOCAL = "D:/projects/LLM2/artifacts/live_packs/sol_1h_hilbert_amp_fade"
NOTES = (
    "SOL 1h hilbert_amp_fade Post-Only two-sided; 5% equity stop-risk floored to 0.1; "
    "lev13 from 3% cap; RESEARCH_ONLY nested subset PASS; skip if below venue min"
)


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


def _write_unit() -> None:
    unit_body = f"""[Unit]
Description=LLM2 {SLUG} Post-Only 5pct stop-risk {ACCOUNT}
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


def _register_bots(*, start: str, start_date: str) -> None:
    payload = json.dumps(
        {
            "bot_id": BOT_ID,
            "account": ACCOUNT,
            "symbol": "SOLUSDT",
            "remote": REMOTE,
            "unit": UNIT,
            "notes": NOTES,
            "pack_local": PACK_LOCAL,
            "start": start,
            "start_date": start_date,
        }
    )
    script = f"""
import json
from pathlib import Path
import yaml
u = json.loads({payload!r})
p = Path("/opt/botsgeneral/config/bots_registry.yaml")
raw = yaml.safe_load(p.read_text()) or {{}}
bots = raw.setdefault("bots", {{}})
host = raw.setdefault("vps", {{}}).setdefault("94.156.189.76", {{}})
bl = list(host.get("bots") or [])
bots[u["bot_id"]] = {{
    "serve_candles": True,
    "exchange": "binance",
    "account": u["account"],
    "symbols": [u["symbol"]],
    "timeframe": "1h",
    "min_history_bars": 3000,
    "also_fetch_timeframes": ["1m"],
    "min_history_bars_by_tf": {{"1h": 3000, "1m": 500}},
    "path": u["remote"],
    "path_local": "D:/projects/LLM2",
    "local_pack_roots": [u["pack_local"]],
    "parser": "none",
    "process_match": [f"--pack {{u['remote']}}/pack", "ema_stack_runner"],
    "systemd_match": [u["unit"]],
    "screen_match": [u["unit"]],
    "start_date": u["start_date"],
    "authorized_from_utc": u["start"],
    "notes": u["notes"],
}}
if u["bot_id"] not in bl:
    bl.append(u["bot_id"])
host["bots"] = bl
raw.pop("hosts", None)
p.write_text(yaml.safe_dump(raw, sort_keys=False))
print("registry_vps_bots", bl)

rp = Path("/etc/botsgeneral/report.yaml")
rep = yaml.safe_load(rp.read_text()) or {{}}
sba = rep.setdefault("since_by_account", {{}})
sbb = rep.setdefault("since_by_bot", {{}})
sba[u["account"]] = u["start"]
sbb[u["bot_id"]] = {{u["symbol"]: u["start"]}}
rp.write_text(yaml.safe_dump(rep, sort_keys=False))
print("report_since_by_account", sba.get(u["account"]))
print("report_since_by_bot", sbb.get(u["bot_id"]))
"""
    print(_ssh_in("python3 -", script), flush=True)


def main() -> int:
    start = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    start_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    refuse_vps_deploy_without_live_certificate(path=CERT, host=HOST)
    stored = (PACK / "pack_hash.txt").read_text(encoding="utf-8").strip()
    if stored not in CERT.read_text(encoding="utf-8"):
        raise SystemExit(f"pack_hash.txt {stored} missing from {CERT.name}")

    print("UPLOAD llm2 package …", flush=True)
    _tar_upload(ROOT / "llm2", "/opt/llm2-structure/llm2")

    print(f"UPLOAD {SLUG} …", flush=True)
    _ssh(f"mkdir -p {REMOTE}/{{pack,state,logs}} && ln -sfn /opt/llm2-structure/venv {REMOTE}/venv")
    _ssh(f"ln -sfn /opt/llm2-structure/llm2 {REMOTE}/llm2")
    _tar_upload(PACK, f"{REMOTE}/pack")
    subprocess.check_call(["scp", str(CERT), f"{SSH}:{REMOTE}/certificate.yaml"])
    _write_unit()
    _ssh(f"systemctl daemon-reload && systemctl enable --now {UNIT}.service")

    _register_bots(start=start, start_date=start_date)
    time.sleep(4)

    active = _ssh_out(f"systemctl is-active {UNIT}.service").strip()
    print(f"ACTIVE {UNIT} {active}", flush=True)
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

    nrest = _ssh_out(
        f"systemctl show {UNIT}.service -p NRestarts -p ActiveState -p SubState --no-pager"
    )
    print(nrest, flush=True)

    fp = (PACK / "pack_hash.txt").read_text(encoding="utf-8").strip()
    append_ledger(
        f"FORMULA_LIVE_AUTH {SLUG}@{ACCOUNT} hash={fp[:16]} host={HOST} start={start} "
        "risk_fraction=0.05 lev=13 four_proof_ok=true nested_settle=PASS RESEARCH_ONLY",
        tier=2,
    )
    print("DONE", datetime.now(timezone.utc).isoformat(), "start", start, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
