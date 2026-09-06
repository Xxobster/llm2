"""Deploy autonomy filter bots 376/705/013 to 212.73.150.178.

Xxobster2: gen 376 SOL + gen 705 ETH
Xxobster10: gen 013 SOL

Does not restart existing Xxobster8/9 pivot units.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.live.certificate import pack_fingerprint, refuse_vps_deploy_without_live_certificate
from llm2.registry.ledger import append_ledger

HOST = "212.73.150.178"
SSH = "ln2"
SSH_LN1 = "ln1"

ARMS = (
    {
        "pack": _ROOT / "artifacts" / "live_packs" / "autonomy_gen376_sol_sma540_below_h4",
        "cert": _ROOT / "configs" / "live" / "autonomy_gen376_sol_sma540_below_h4_xxobster2_ln2_certificate.yaml",
        "remote": "/opt/llm2-autonomy-376-sol-sma540",
        "unit": "llm2-autonomy-376-sol-sma540",
        "account": "Xxobster2",
        "symbol": "SOLUSDT",
        "bot_key": "llm2_autonomy_376_sol",
    },
    {
        "pack": _ROOT / "artifacts" / "live_packs" / "autonomy_gen705_eth_ema1320_below_h4",
        "cert": _ROOT / "configs" / "live" / "autonomy_gen705_eth_ema1320_below_h4_xxobster2_ln2_certificate.yaml",
        "remote": "/opt/llm2-autonomy-705-eth-ema1320",
        "unit": "llm2-autonomy-705-eth-ema1320",
        "account": "Xxobster2",
        "symbol": "ETHUSDT",
        "bot_key": "llm2_autonomy_705_eth",
    },
    {
        "pack": _ROOT / "artifacts" / "live_packs" / "autonomy_gen013_sol_atr_rel_cross_up_h8",
        "cert": _ROOT / "configs" / "live" / "autonomy_gen013_sol_atr_rel_cross_up_h8_xxobster10_ln2_certificate.yaml",
        "remote": "/opt/llm2-autonomy-013-sol-atrrel",
        "unit": "llm2-autonomy-013-sol-atrrel",
        "account": "Xxobster10",
        "symbol": "SOLUSDT",
        "bot_key": "llm2_autonomy_013_sol",
    },
)

CODE_FILES = (
    "llm2/live/pivot_runner.py",
    "llm2/live/micro_runner.py",
    "llm2/sizing_policy.py",
    "llm2/autonomy/filter_head.py",
    "llm2/autonomy/__init__.py",
    "llm2/autonomy/policy.py",
    "llm2/autonomy/packs.py",
    "llm2/autonomy/public_formulas.py",
    "llm2/confluence/events.py",
    "llm2/diagnostics/events.py",
    "llm2/evidence/pivot_four_proof.py",
)


def _run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.check_call(cmd)


def _ssh(host: str, cmd: str) -> str:
    out = subprocess.check_output(["ssh", host, cmd], text=True)
    sys.stdout.write(out)
    return out


def _unit_body(arm: dict) -> str:
    remote = arm["remote"]
    unit = arm["unit"]
    account = arm["account"]
    return f"""[Unit]
Description=LLM2 autonomy filter {unit} LIVE MIN_EXCHANGE {account}
After=network-online.target botsgeneral-collector@212.73.150.178.service
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory={remote}
Environment=PYTHONPATH={remote}:/opt/llm2-structure:/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src
Environment=SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db
Environment=TRADING_SECRETS_ENV=/root/.trading/secrets.env
Environment=TRADESIM_NO_PLOT=1
ExecStart={remote}/venv/bin/python -m llm2.live.pivot_runner --pack {remote}/pack --state {remote}/state/pivot_live_state.sqlite --mode LIVE --live-orders --account {account} --cert {remote}/certificate.yaml --vps-host {HOST}
Restart=always
RestartSec=10
StandardOutput=append:{remote}/logs/pivot_live.log
StandardError=append:{remote}/logs/pivot_live.log

[Install]
WantedBy=multi-user.target
"""


def _copy_keys() -> None:
    """Copy Xxobster2 + Xxobster10 key *names* into ln2 secrets.env. Never print values."""
    extract = r"""
from pathlib import Path
import json
import re
out = Path("/tmp/xx2_xx10.env")
lines = []
sec = Path("/root/.trading/secrets.env")
if sec.is_file():
    for line in sec.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("Xxobster10_API_"):
            lines.append(line)
js = Path("/home/xgb/config/api_keys.json")
if js.is_file():
    raw = json.loads(js.read_text(encoding="utf-8"))
    # common shapes: {Xxobster2: {key,secret}} or {api_key, api_secret}
    def grab(d, *names):
        for n in names:
            if n in d and d[n]:
                return str(d[n])
        return ""
    key = secret = ""
    if isinstance(raw, dict):
        block = raw.get("xxobster2") or raw.get("Xxobster2") or raw
        if isinstance(block, dict):
            key = grab(block, "api_key", "API_KEY", "key", "Xxobster2_API_KEY")
            secret = grab(block, "api_secret", "API_SECRET", "secret", "Xxobster2_API_SECRET")
        if (not key or not secret) and "accounts" in raw:
            acc = raw["accounts"]
            block = acc.get("Xxobster2") if isinstance(acc, dict) else None
            if isinstance(block, dict):
                key = grab(block, "api_key", "API_KEY", "key")
                secret = grab(block, "api_secret", "API_SECRET", "secret")
    if key and secret:
        lines.append("Xxobster2_API_KEY=" + key)
        lines.append("Xxobster2_API_SECRET=" + secret)
    else:
        raise SystemExit("xx2_keys_not_found")
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
out.chmod(0o600)
print("wrote_names", [re.split("=", ln, 1)[0] for ln in lines])
"""
    subprocess.check_call(["ssh", SSH_LN1, "python3 - <<'PY'\n" + extract + "\nPY"])
    tmp = Path(tempfile.gettempdir()) / "xx2_xx10.env"
    try:
        _run(["scp", f"{SSH_LN1}:/tmp/xx2_xx10.env", str(tmp)])
        _run(["scp", str(tmp), f"{SSH}:/tmp/xx2_xx10.env"])
        _ssh(
            SSH,
            "mkdir -p /root/.trading && touch /root/.trading/secrets.env && "
            "chmod 600 /root/.trading/secrets.env && "
            'grep -vE "^Xxobster2_API_|^Xxobster10_API_" /root/.trading/secrets.env > /tmp/s.env || true && '
            "cat /tmp/xx2_xx10.env >> /tmp/s.env && mv /tmp/s.env /root/.trading/secrets.env && "
            "chmod 600 /root/.trading/secrets.env && rm -f /tmp/xx2_xx10.env && "
            'echo xx2=$(grep -c "^Xxobster2_API_" /root/.trading/secrets.env) '
            'xx10=$(grep -c "^Xxobster10_API_" /root/.trading/secrets.env)',
        )
    finally:
        if tmp.exists():
            tmp.unlink()
        subprocess.call(["ssh", SSH_LN1, "rm -f /tmp/xx2_xx10.env"])


def _sync_code() -> None:
    _ssh(SSH, "mkdir -p /opt/llm2-structure/llm2/live /opt/llm2-structure/llm2/autonomy /opt/llm2-structure/llm2/evidence")
    for rel in CODE_FILES:
        local = _ROOT / rel
        if not local.is_file():
            raise FileNotFoundError(local)
        _run(["scp", str(local), f"{SSH}:/opt/llm2-structure/{rel}"])
    _ssh(SSH, "rm -rf /opt/llm2-structure/llm2/live/__pycache__ /opt/llm2-structure/llm2/autonomy/__pycache__")


def _scp_pack(local_dir: Path, remote_dir: str) -> None:
    _ssh(SSH, f"mkdir -p {remote_dir}")
    tmp = Path(tempfile.gettempdir()) / f"{local_dir.name}.tar"
    try:
        _run(["tar", "-C", str(local_dir), "--exclude=__pycache__", "-cf", str(tmp), "."])
        _run(["scp", str(tmp), f"{SSH}:/tmp/{tmp.name}"])
        _ssh(SSH, f"tar -C {remote_dir} -xf /tmp/{tmp.name} && rm -f /tmp/{tmp.name}")
    finally:
        if tmp.exists():
            tmp.unlink()


def _deploy_arm(arm: dict) -> None:
    remote = arm["remote"]
    unit = arm["unit"]
    _ssh(SSH, f"mkdir -p {remote}/{{pack,state,logs}} && ln -sfn /opt/llm2-structure/venv {remote}/venv")
    _ssh(SSH, f"ln -sfn /opt/llm2-structure/llm2 {remote}/llm2")
    _scp_pack(arm["pack"], f"{remote}/pack")
    _run(["scp", str(arm["cert"]), f"{SSH}:{remote}/certificate.yaml"])
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
for name in ("llm2_autonomy_376_sol", "llm2_autonomy_705_eth", "llm2_autonomy_013_sol"):
    if name not in bots:
        bots.append(name)
host["bots"] = bots
spec = {
    "llm2_autonomy_376_sol": {
        "serve_candles": True,
        "exchange": "bybit",
        "account": "Xxobster2",
        "path": "/opt/llm2-autonomy-376-sol-sma540",
        "parser": "none",
        "timeframe": "15m",
        "symbols": ["SOLUSDT"],
        "process_match": ["llm2.live.pivot_runner", "autonomy-376"],
        "systemd_match": ["llm2-autonomy-376-sol-sma540"],
        "notes": "SOL 15m autonomy gen376 sma540_below H4 filter on pivot control",
    },
    "llm2_autonomy_705_eth": {
        "serve_candles": True,
        "exchange": "bybit",
        "account": "Xxobster2",
        "path": "/opt/llm2-autonomy-705-eth-ema1320",
        "parser": "none",
        "timeframe": "15m",
        "symbols": ["ETHUSDT"],
        "process_match": ["llm2.live.pivot_runner", "autonomy-705"],
        "systemd_match": ["llm2-autonomy-705-eth-ema1320"],
        "notes": "ETH 15m autonomy gen705 ema1320_below H4 filter on pivot control",
    },
    "llm2_autonomy_013_sol": {
        "serve_candles": True,
        "exchange": "bybit",
        "account": "Xxobster10",
        "path": "/opt/llm2-autonomy-013-sol-atrrel",
        "parser": "none",
        "timeframe": "15m",
        "symbols": ["SOLUSDT"],
        "process_match": ["llm2.live.pivot_runner", "autonomy-013"],
        "systemd_match": ["llm2-autonomy-013-sol-atrrel"],
        "notes": "SOL 15m autonomy gen013 atr_rel_cross_up_1 H8 filter on pivot control",
    },
}
bots_map = r.setdefault("bots", {})
bots_map.update(spec)
llm2 = bots_map.setdefault("llm2", {})
# Generic llm2 is pivot Xxobster8/9 only. Autonomy 376/705/013 have their own keys.
acc = llm2.get("account")
pivot_only = ["Xxobster8", "Xxobster9"]
if isinstance(acc, list):
    llm2["account"] = [n for n in acc if n in pivot_only] or list(pivot_only)
    for name in pivot_only:
        if name not in llm2["account"]:
            llm2["account"].append(name)
elif acc and acc in pivot_only:
    llm2["account"] = [acc] + [n for n in pivot_only if n != acc]
else:
    llm2["account"] = list(pivot_only)
p.write_text(yaml.safe_dump(r, sort_keys=False), encoding="utf-8")
print("host_bots", host.get("bots"))
print("llm2_accounts", llm2.get("account"))
"""
    subprocess.check_call(["ssh", SSH, "python3 - <<'PY'\n" + script + "\nPY"])


def main() -> int:
    for arm in ARMS:
        if not (arm["pack"] / "filter_head.joblib").is_file():
            raise SystemExit(f"missing freeze {arm['pack']}")
        if not arm["cert"].is_file():
            raise SystemExit(f"missing cert {arm['cert']}")
        refuse_vps_deploy_without_live_certificate(path=arm["cert"], host=HOST)
        fp = pack_fingerprint(arm["pack"])
        if fp is None or fp not in arm["cert"].read_text(encoding="utf-8"):
            raise SystemExit(f"cert/pack hash mismatch {arm['unit']}")
        print("cert_ok", arm["unit"], flush=True)

    _copy_keys()
    _sync_code()
    _patch_registry()
    for arm in ARMS:
        print("DEPLOY", arm["unit"], flush=True)
        _deploy_arm(arm)

    units = " ".join(a["unit"] + ".service" for a in ARMS)
    _ssh(
        SSH,
        f"systemctl daemon-reload && systemctl enable --now {units} && "
        f"sleep 8 && systemctl is-active {units}",
    )
    print("KEEP_EXISTING", flush=True)
    _ssh(
        SSH,
        "systemctl is-active llm2-pivot-eth-p75-ctrl-atr-w4 llm2-pivot-sol-geo-p75-w4 "
        "llm2-pivot-eth-p50-tp05-sl05 llm2-pivot-sol-p50-tp05-sl05 "
        "llm2-autonomy-376-sol-sma540 llm2-autonomy-705-eth-ema1320 llm2-autonomy-013-sol-atrrel",
    )
    for arm in ARMS:
        _ssh(SSH, f"tail -n 25 {arm['remote']}/logs/pivot_live.log || true")
    append_ledger(
        "AUTONOMY_FILTER_LIVE_AUTH 376 SOL + 705 ETH on Xxobster2; 013 SOL on Xxobster10; "
        f"host={HOST} MIN_EXCHANGE 1pct/1pct 29x "
        "(research remains LIVE_STOP; user operational authorize)",
        tier=2,
    )
    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
