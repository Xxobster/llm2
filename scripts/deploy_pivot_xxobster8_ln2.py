"""Deploy ETH+SOL 15m 1%/1% pivot LIMIT bots to 212.73.150.178 / Xxobster8.

User chat authorization 2026-08-21: same frozen packs as Xxobster7.
Does not change the 94.156.189.76 / Xxobster7 units.
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.live.certificate import refuse_vps_deploy_without_live_certificate
from llm2.registry.ledger import append_ledger

HOST = "212.73.150.178"
SSH = "ln2"
ACCOUNT = "Xxobster8"
ARMS = (
    {
        "pack": _ROOT / "artifacts" / "live_packs" / "pivot_eth_p75_ctrl_atr_w4",
        "cert": _ROOT / "configs" / "live" / "pivot_eth_p75_ctrl_atr_w4_xxobster8_ln2_certificate.yaml",
        "remote": "/opt/llm2-pivot-eth-p75-ctrl-atr-w4",
        "unit": "llm2-pivot-eth-p75-ctrl-atr-w4",
        "symbol": "ETHUSDT",
    },
    {
        "pack": _ROOT / "artifacts" / "live_packs" / "pivot_sol_geo_tp1_sl1_p75_w4",
        "cert": _ROOT / "configs" / "live" / "pivot_sol_geo_tp1_sl1_p75_w4_xxobster8_ln2_certificate.yaml",
        "remote": "/opt/llm2-pivot-sol-geo-p75-w4",
        "unit": "llm2-pivot-sol-geo-p75-w4",
        "symbol": "SOLUSDT",
    },
)


def _run(cmd: list[str] | str, *, shell: bool = False) -> None:
    print("+", cmd if isinstance(cmd, str) else " ".join(cmd), flush=True)
    subprocess.check_call(cmd, shell=shell)


def _ssh(cmd: str) -> str:
    out = subprocess.check_output(["ssh", SSH, cmd], text=True)
    sys.stdout.write(out)
    return out


def _tar_upload(local_dir: Path, remote_dir: str) -> None:
    _ssh(f"mkdir -p {remote_dir}")
    cmd = (
        f'tar -C "{local_dir}" --exclude=__pycache__ --exclude=*.pyc '
        f"--exclude=*.sqlite-wal --exclude=*.sqlite-shm -cf - . "
        f"| ssh {SSH} \"tar -C {remote_dir} -xf -\""
    )
    _run(cmd, shell=True)


def _copy_xx8_from_ln1() -> None:
    subprocess.check_call(
        ["ssh", "ln1", 'grep -E "^Xxobster8_API_" /root/.trading/secrets.env > /tmp/xx8.env && chmod 600 /tmp/xx8.env']
    )
    tmp = Path(tempfile.gettempdir()) / "xx8.env"
    try:
        subprocess.check_call(["scp", "ln1:/tmp/xx8.env", str(tmp)])
        subprocess.check_call(["scp", str(tmp), f"{SSH}:/tmp/xx8.env"])
        _ssh(
            "mkdir -p /root/.trading && touch /root/.trading/secrets.env && "
            "chmod 600 /root/.trading/secrets.env && "
            'grep -v "^Xxobster8_API_" /root/.trading/secrets.env > /tmp/s.env || true && '
            "cat /tmp/xx8.env >> /tmp/s.env && mv /tmp/s.env /root/.trading/secrets.env && "
            "chmod 600 /root/.trading/secrets.env && rm -f /tmp/xx8.env && "
            'echo xx8_lines=$(grep -c "^Xxobster8_API_" /root/.trading/secrets.env)'
        )
    finally:
        if tmp.exists():
            tmp.unlink()
        subprocess.call(["ssh", "ln1", "rm -f /tmp/xx8.env"])


def _ensure_venv() -> None:
    have = subprocess.call(["ssh", SSH, "test -x /opt/llm2-structure/venv/bin/python"])
    if have == 0:
        print("venv already present", flush=True)
        return
    print("copy venv from ln1 …", flush=True)
    _ssh("mkdir -p /opt/llm2-structure")
    subprocess.check_call(
        ["ssh", "ln1", "tar -C /opt/llm2-structure -cf /tmp/llm2-venv.tar venv"]
    )
    tmp = Path(tempfile.gettempdir()) / "llm2-venv.tar"
    try:
        subprocess.check_call(["scp", "ln1:/tmp/llm2-venv.tar", str(tmp)])
        subprocess.check_call(["scp", str(tmp), f"{SSH}:/tmp/llm2-venv.tar"])
        _ssh("tar -C /opt/llm2-structure -xf /tmp/llm2-venv.tar && rm -f /tmp/llm2-venv.tar")
    finally:
        if tmp.exists():
            tmp.unlink()
        subprocess.call(["ssh", "ln1", "rm -f /tmp/llm2-venv.tar"])


def _unit_body(arm: dict) -> str:
    remote = arm["remote"]
    unit = arm["unit"]
    return f"""[Unit]
Description=LLM2 pivot LIMIT {unit} LIVE MIN_EXCHANGE Xxobster8
After=network-online.target botsgeneral-collector@212.73.150.178.service
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory={remote}
Environment=PYTHONPATH={remote}:/opt/llm2-structure:/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src
Environment=SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db
Environment=TRADING_SECRETS_ENV=/root/.trading/secrets.env
Environment=TRADESIM_NO_PLOT=1
ExecStart={remote}/venv/bin/python -m llm2.live.pivot_runner --pack {remote}/pack --state {remote}/state/pivot_live_state.sqlite --mode LIVE --live-orders --account {ACCOUNT} --cert {remote}/certificate.yaml --vps-host {HOST}
Restart=always
RestartSec=10
StandardOutput=append:{remote}/logs/pivot_live.log
StandardError=append:{remote}/logs/pivot_live.log

[Install]
WantedBy=multi-user.target
"""


def _deploy_arm(arm: dict) -> None:
    remote = arm["remote"]
    unit = arm["unit"]
    _ssh(f"mkdir -p {remote}/{{pack,state,logs}} && ln -sfn /opt/llm2-structure/venv {remote}/venv")
    _ssh("ln -sfn /opt/llm2-structure/llm2 " + remote + "/llm2")
    _tar_upload(arm["pack"], f"{remote}/pack")
    subprocess.check_call(["scp", str(arm["cert"]), f"{SSH}:{remote}/certificate.yaml"])
    body = _unit_body(arm)
    subprocess.check_call(["ssh", SSH, f"cat > /etc/systemd/system/{unit}.service <<'EOF'\n{body}\nEOF"])


def _patch_registry() -> None:
    script = r"""
from pathlib import Path
import yaml
p = Path("/opt/botsgeneral/config/bots_registry.yaml")
r = yaml.safe_load(p.read_text()) or {}
host = r.setdefault("vps", {}).setdefault("212.73.150.178", {})
bots = list(host.get("bots") or [])
if "llm2" not in bots:
    bots.append("llm2")
host["bots"] = bots
llm2 = r.setdefault("bots", {}).setdefault("llm2", {})
also = set(llm2.get("also_fetch_timeframes") or [])
also.add("1m")
llm2["also_fetch_timeframes"] = sorted(also)
llm2["timeframe"] = "15m"
acc = llm2.get("account")
if isinstance(acc, list):
    if "Xxobster8" not in acc:
        acc.append("Xxobster8")
    llm2["account"] = acc
elif acc:
    llm2["account"] = [acc, "Xxobster8"] if acc != "Xxobster8" else ["Xxobster8"]
else:
    llm2["account"] = ["Xxobster8"]
by_tf = dict(llm2.get("min_history_bars_by_tf") or {})
by_tf.setdefault("15m", 3000)
by_tf.setdefault("1m", 500)
llm2["min_history_bars_by_tf"] = by_tf
p.write_text(yaml.safe_dump(r, sort_keys=False))
print("vps212", host)
print("llm2 also", llm2.get("also_fetch_timeframes"), "account", llm2.get("account"))
"""
    subprocess.check_call(["ssh", SSH, "python3 - <<'PY'\n" + script + "\nPY"])


def main() -> int:
    for arm in ARMS:
        refuse_vps_deploy_without_live_certificate(path=arm["cert"], host=HOST)
        print("cert_ok", arm["cert"].name, flush=True)

    _copy_xx8_from_ln1()
    _ensure_venv()
    _tar_upload(_ROOT / "llm2", "/opt/llm2-structure/llm2")
    _patch_registry()
    print("restart collector …", flush=True)
    _ssh(
        "systemctl restart botsgeneral-collector@212.73.150.178 && "
        "sleep 3 && systemctl is-active botsgeneral-collector@212.73.150.178"
    )

    for arm in ARMS:
        print("DEPLOY", arm["unit"], flush=True)
        _deploy_arm(arm)

    units = " ".join(a["unit"] + ".service" for a in ARMS)
    _ssh(
        f"systemctl daemon-reload && systemctl enable --now {units} && "
        f"sleep 4 && systemctl is-active {units}"
    )
    for arm in ARMS:
        _ssh(f"tail -n 25 {arm['remote']}/logs/pivot_live.log || true")
    append_ledger(
        f"PIVOT_LIVE_AUTH ETH+SOL 15m 1pct/1pct account={ACCOUNT} host={HOST} "
        "packs=eth_p75_ctrl_atr_w4,sol_geo_tp1_sl1_p75_w4",
        tier=2,
    )
    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
