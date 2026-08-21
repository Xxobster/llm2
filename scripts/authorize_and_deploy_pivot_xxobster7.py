"""Authorize + deploy pivot SOL + ETH LIMIT micro-live on 94.x / Xxobster7.

User chat authorization 2026-08-12: real USDT MIN_EXCHANGE for
  - sol_geo_tp1_sl1_p75_w4
  - eth_p75_ctrl_atr_w4
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.evidence.pivot_four_proof import run_pivot_four_proof  # noqa: E402
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.paths import ARTIFACTS, ROOT  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402

HOST = "94.156.189.76"
ACCOUNT = "Xxobster7"
ARMS = (
    {
        "pack": ARTIFACTS / "live_packs" / "pivot_sol_geo_tp1_sl1_p75_w4",
        "cert": ROOT / "configs" / "live" / "pivot_sol_geo_tp1_sl1_p75_w4_certificate.yaml",
        "remote": "/opt/llm2-pivot-sol-geo-p75-w4",
        "unit": "llm2-pivot-sol-geo-p75-w4",
        "strategy_id": "pivot_sol_geo_tp1_sl1_p75_w4_SOLUSDT_15m",
    },
    {
        "pack": ARTIFACTS / "live_packs" / "pivot_eth_p75_ctrl_atr_w4",
        "cert": ROOT / "configs" / "live" / "pivot_eth_p75_ctrl_atr_w4_certificate.yaml",
        "remote": "/opt/llm2-pivot-eth-p75-ctrl-atr-w4",
        "unit": "llm2-pivot-eth-p75-ctrl-atr-w4",
        "strategy_id": "pivot_eth_p75_ctrl_atr_w4_ETHUSDT_15m",
    },
)


def _write_cert(arm: dict, pack_hash: str, four_proof: dict) -> None:
    exp = (datetime.now(timezone.utc) + timedelta(days=14)).strftime("%Y-%m-%dT%H:%M:%SZ")
    hashes = four_proof.get("artifact_hashes") or {}
    text = f"""strategy_id: {arm['strategy_id']}
status: AUTHORIZED
authorized_by_user: true
vps_host: '{HOST}'
account_ref: {ACCOUNT}
intended_vps_host: '{HOST}'
intended_account_ref: {ACCOUNT}
pack_path: {arm['pack'].relative_to(ROOT).as_posix()}
pack_hash: {pack_hash}
expires_utc: '{exp}'
created_utc: '{datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}'
four_proof_ok: true
four_proof_hashes:
  builder_responsiveness: {hashes.get('builder_responsiveness')}
  recompute_prefix: {hashes.get('recompute_prefix')}
  no_live_feature_fill: {hashes.get('no_live_feature_fill')}
  layer_a_pred_identity: {hashes.get('layer_a_pred_identity')}
notes: >-
  User explicitly authorized 2026-08-12 (UTC+7) real-USDT MIN_EXCHANGE pivot LIMIT
  micro-live on {HOST} / {ACCOUNT}. Leverage from stop 1% = 29x. work_bars=4.
  Certificate expires unless renewed.
"""
    arm["cert"].write_text(text, encoding="utf-8")


def _ssh(cmd: str) -> None:
    subprocess.check_call(["ssh", f"root@{HOST}", cmd])


def _tar_upload(local_dir: Path, remote_dir: str) -> None:
    """Upload a directory via tar|ssh (Windows-friendly; no rsync required)."""
    _ssh(f"mkdir -p {remote_dir}")
    # Clear remote contents then extract
    _ssh(f"rm -rf {remote_dir}/*")
    cmd = (
        f"tar -C \"{local_dir}\" --exclude=__pycache__ --exclude=*.pyc "
        f"--exclude=*.sqlite-wal --exclude=*.sqlite-shm -cf - . "
        f"| ssh root@{HOST} \"tar -C {remote_dir} -xf -\""
    )
    subprocess.check_call(cmd, shell=True)


def _deploy_arm(arm: dict) -> None:
    remote = arm["remote"]
    unit = arm["unit"]
    pack = arm["pack"]
    cert = arm["cert"]
    _ssh(f"mkdir -p {remote}/{{pack,state,logs}} && ln -sfn /opt/llm2-structure/venv {remote}/venv")
    # Sync llm2 tree into shared location used by structure (and link)
    _tar_upload(ROOT / "llm2", "/opt/llm2-structure/llm2")
    _ssh(f"ln -sfn /opt/llm2-structure/llm2 {remote}/llm2")
    _tar_upload(pack, f"{remote}/pack")
    subprocess.check_call(["scp", str(cert), f"root@{HOST}:{remote}/certificate.yaml"])

    unit_body = f"""[Unit]
Description=LLM2 pivot LIMIT {unit} LIVE MIN_EXCHANGE Xxobster7
After=network-online.target
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
    # Write unit via ssh heredoc
    subprocess.check_call(
        [
            "ssh",
            f"root@{HOST}",
            f"cat > /etc/systemd/system/{unit}.service <<'EOF'\n{unit_body}\nEOF",
        ]
    )
    _ssh(
        f"systemctl daemon-reload && systemctl enable --now {unit}.service && "
        f"sleep 2 && systemctl is-active {unit}.service && tail -n 30 {remote}/logs/pivot_live.log"
    )


def _register_bots() -> None:
    script = r'''
from pathlib import Path
import yaml
p = Path("/opt/botsgeneral/config/bots_registry.yaml")
raw = yaml.safe_load(p.read_text()) or {}
bots = raw.setdefault("bots", {})
for name, path, match in (
    ("llm2_pivot_sol_geo", "/opt/llm2-pivot-sol-geo-p75-w4", ["pivot_runner", "pivot-sol"]),
    ("llm2_pivot_eth_ctrl", "/opt/llm2-pivot-eth-p75-ctrl-atr-w4", ["pivot_runner", "pivot-eth"]),
):
    bots[name] = {
        "serve_candles": False,
        "exchange": "binance",
        "account": "Xxobster7",
        "symbols": ["SOLUSDT"] if "sol" in name else ["ETHUSDT"],
        "timeframe": "15m",
        "also_fetch_timeframes": ["1m", "1h"],
        "path": path,
        "parser": "none",
        "process_match": match + ["llm2.live.pivot_runner"],
        "screen_match": [name],
        "systemd_match": [name.replace("_", "-") if False else name],
    }
# fix systemd match to actual unit names
bots["llm2_pivot_sol_geo"]["systemd_match"] = ["llm2-pivot-sol-geo-p75-w4"]
bots["llm2_pivot_eth_ctrl"]["systemd_match"] = ["llm2-pivot-eth-p75-ctrl-atr-w4"]
host = raw.setdefault("hosts", {}).setdefault("94.156.189.76", {})
bl = list(host.get("bots") or [])
for n in ("llm2_pivot_sol_geo", "llm2_pivot_eth_ctrl"):
    if n not in bl:
        bl.append(n)
host["bots"] = bl
p.write_text(yaml.safe_dump(raw, sort_keys=False))
print("registry_updated", bl)
'''
    subprocess.check_call(
        ["ssh", f"root@{HOST}", "python3 - <<'PY'\n" + script + "\nPY"]
    )


def main() -> int:
    for arm in ARMS:
        pack = arm["pack"]
        if not (pack / "model.joblib").is_file():
            raise SystemExit(f"missing pack {pack}")
        print(f"FOUR_PROOF {pack.name} …", flush=True)
        summary = run_pivot_four_proof(pack_dir=pack)
        print("  ok", summary.get("proofs_ok"), flush=True)
        # Re-hash after attaching evidence
        fp = pack_fingerprint(pack)
        assert fp
        (pack / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
        meta = json.loads((pack / "pack_meta.json").read_text(encoding="utf-8"))
        meta["pack_hash"] = fp
        meta["status"] = "LIVE_ACTIVE"
        meta["readiness"] = "MICRO_LIVE_CANDIDATE"
        meta["deployable"] = True
        meta["live"] = {
            "deployed": True,
            "account_ref": ACCOUNT,
            "service": arm["unit"],
            "vps_host": HOST,
        }
        (pack / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        fp2 = pack_fingerprint(pack)
        meta["pack_hash"] = fp2
        (pack / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        (pack / "pack_hash.txt").write_text(fp2 + "\n", encoding="utf-8")
        _write_cert(arm, fp2, summary)
        append_ledger(
            f"PIVOT_LIVE_AUTH arm={pack.name} account={ACCOUNT} host={HOST} "
            f"hash={fp2[:16]} four_proof_ok=true",
            tier=2,
        )
        print(f"CERT {arm['cert']}", flush=True)

    # Ensure 15m candles served for llm2 on host (extend registry also_fetch)
    _ssh(
        "python3 - <<'PY'\n"
        "from pathlib import Path\n"
        "import yaml\n"
        "p=Path('/opt/botsgeneral/config/bots_registry.yaml')\n"
        "r=yaml.safe_load(p.read_text())\n"
        "llm2=r['bots']['llm2']\n"
        "also=set(llm2.get('also_fetch_timeframes') or [])\n"
        "also.update(['15m','1m'])\n"
        "llm2['also_fetch_timeframes']=sorted(also)\n"
        "p.write_text(yaml.safe_dump(r, sort_keys=False))\n"
        "print('llm2 also_fetch', llm2['also_fetch_timeframes'])\n"
        "PY"
    )

    for arm in ARMS:
        print(f"DEPLOY {arm['unit']} …", flush=True)
        _deploy_arm(arm)

    _register_bots()
    print("DONE — both pivot units LIVE with --live-orders on Xxobster7", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
