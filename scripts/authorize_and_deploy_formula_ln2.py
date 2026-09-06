"""Deploy hunt-009 / hunt-012 formula packs to live-network-2.

User 2026-09-04: Bitcoin 1h slope-follow + Solana 1h Fair Value Gap confluence
on 212.73.150.178, free Xxobster, 5% equity stop-risk, Post-Only, adapt bots
start date, calculate leverage. Nested settle FAIL is acknowledged on the
certificate. Do not stop existing live units.
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

HOST = "212.73.150.178"
SSH = "ln2"
START = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
START_DATE = datetime.now(timezone.utc).strftime("%Y-%m-%d")

UNITS = (
    {
        "slug": "btc_1h_quad_slope_follow",
        "account": "Xxobster11",
        "remote": "/opt/llm2-quad-btc-1h",
        "unit": "llm2-quad-btc-1h",
        "bot_id": "llm2_quad_btc_1h",
        "symbol": "BTCUSDT",
        "pack": ARTIFACTS / "live_packs" / "btc_1h_quad_slope_follow",
        "cert": ROOT / "configs" / "live" / "btc_1h_quad_slope_follow_xxobster11_ln2_certificate.yaml",
        "pack_local": "D:/projects/LLM2/artifacts/live_packs/btc_1h_quad_slope_follow",
        "notes": (
            "BTC 1h quad_slope_follow Post-Only two-sided; 5% equity stop-risk; "
            "lev13 from 3% cap; RESEARCH_ONLY nested FAIL; skip if below venue min"
        ),
    },
    {
        "slug": "sol_1h_fvg_confluence",
        "account": "Xxobster11",
        "remote": "/opt/llm2-fvg-sol-1h",
        "unit": "llm2-fvg-sol-1h",
        "bot_id": "llm2_fvg_sol_1h",
        "symbol": "SOLUSDT",
        "pack": ARTIFACTS / "live_packs" / "sol_1h_fvg_confluence",
        "cert": ROOT / "configs" / "live" / "sol_1h_fvg_confluence_xxobster11_ln2_certificate.yaml",
        "pack_local": "D:/projects/LLM2/artifacts/live_packs/sol_1h_fvg_confluence",
        "notes": (
            "SOL 1h fvg_confluence Post-Only long-only; 5% equity stop-risk; "
            "lev13 from 3% cap; RESEARCH_ONLY nested FAIL; skip if below venue min"
        ),
    },
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


def _write_unit(cfg: dict) -> None:
    remote = cfg["remote"]
    unit = cfg["unit"]
    account = cfg["account"]
    unit_body = f"""[Unit]
Description=LLM2 {cfg['slug']} Post-Only 5pct stop-risk {account}
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory={remote}
Environment=PYTHONPATH={remote}:/opt/llm2-structure:/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src
Environment=SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db
Environment=TRADING_SECRETS_ENV=/root/.trading/secrets.env
Environment=TRADESIM_NO_PLOT=1
ExecStart={remote}/venv/bin/python -u -m llm2.live.ema_stack_runner --pack {remote}/pack --state {remote}/state/ema_live_state.sqlite --mode LIVE --live-orders --account {account} --cert {remote}/certificate.yaml --vps-host {HOST}
Restart=always
RestartSec=10
StandardOutput=append:{remote}/logs/ema_live.log
StandardError=append:{remote}/logs/ema_live.log

[Install]
WantedBy=multi-user.target
"""
    subprocess.check_call(
        ["ssh", "-o", "BatchMode=yes", SSH, f"cat > /etc/systemd/system/{unit}.service <<'EOF'\n{unit_body}\nEOF"]
    )


def _register_bots() -> None:
    units_json = json.dumps(
        [
            {
                "bot_id": u["bot_id"],
                "account": u["account"],
                "symbol": u["symbol"],
                "remote": u["remote"],
                "unit": u["unit"],
                "notes": u["notes"],
                "pack_local": u["pack_local"],
                "start": START,
                "start_date": START_DATE,
            }
            for u in UNITS
        ]
    )
    script = f"""
import json
from pathlib import Path
import yaml
units = json.loads({units_json!r})
p = Path("/opt/botsgeneral/config/bots_registry.yaml")
raw = yaml.safe_load(p.read_text()) or {{}}
bots = raw.setdefault("bots", {{}})
host = raw.setdefault("vps", {{}}).setdefault("212.73.150.178", {{}})
bl = list(host.get("bots") or [])
for u in units:
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
for u in units:
    sba[u["account"]] = u["start"]
    sbb[u["bot_id"]] = {{u["symbol"]: u["start"]}}
rp.write_text(yaml.safe_dump(rep, sort_keys=False))
print("report_since_by_account", sba)
"""
    print(_ssh_in("python3 -", script), flush=True)


def main() -> int:
    for cfg in UNITS:
        refuse_vps_deploy_without_live_certificate(path=cfg["cert"], host=HOST)
        stored = (cfg["pack"] / "pack_hash.txt").read_text(encoding="utf-8").strip()
        if stored not in cfg["cert"].read_text(encoding="utf-8"):
            raise SystemExit(f"pack_hash.txt {stored} missing from {cfg['cert'].name}")

    print("UPLOAD llm2 package …", flush=True)
    _tar_upload(ROOT / "llm2", "/opt/llm2-structure/llm2")

    for cfg in UNITS:
        remote = cfg["remote"]
        print(f"UPLOAD {cfg['slug']} …", flush=True)
        _ssh(f"mkdir -p {remote}/{{pack,state,logs}} && ln -sfn /opt/llm2-structure/venv {remote}/venv")
        _ssh(f"ln -sfn /opt/llm2-structure/llm2 {remote}/llm2")
        _tar_upload(cfg["pack"], f"{remote}/pack")
        subprocess.check_call(["scp", str(cfg["cert"]), f"{SSH}:{remote}/certificate.yaml"])
        _write_unit(cfg)
        _ssh(f"systemctl daemon-reload && systemctl enable --now {cfg['unit']}.service")

    _register_bots()
    time.sleep(4)

    for cfg in UNITS:
        active = _ssh_out(f"systemctl is-active {cfg['unit']}.service").strip()
        print(f"ACTIVE {cfg['unit']} {active}", flush=True)
        print(_ssh_out(f"tail -n 30 {cfg['remote']}/logs/ema_live.log"), flush=True)
        if active != "active":
            print(_ssh_out(f"journalctl -u {cfg['unit']} -n 80 --no-pager"), flush=True)
            raise SystemExit(f"{cfg['unit']} not active")
        print(f"ONCE smoke {cfg['unit']} …", flush=True)
        print(
            _ssh_out(
                f"cd {cfg['remote']} && PYTHONPATH={cfg['remote']}:/opt/llm2-structure:"
                "/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:"
                "/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src "
                f"{cfg['remote']}/venv/bin/python -m llm2.live.ema_stack_runner --pack {cfg['remote']}/pack "
                f"--state {cfg['remote']}/state/ema_live_state.sqlite --once"
            ),
            flush=True,
        )

    hashes = []
    for cfg in UNITS:
        fp = (cfg["pack"] / "pack_hash.txt").read_text(encoding="utf-8").strip()
        hashes.append(f"{cfg['slug']}@{cfg['account']} hash={fp[:16]}")
    append_ledger(
        f"FORMULA_LIVE_AUTH {' '.join(hashes)} host={HOST} start={START} "
        "risk_fraction=0.05 lev=13 four_proof_ok=true nested_settle=FAIL RESEARCH_ONLY",
        tier=2,
    )
    print("DONE", datetime.now(timezone.utc).isoformat(), "start", START, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
