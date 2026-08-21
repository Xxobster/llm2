"""Deploy ETH+SOL 15m 0.5%/0.5% pivot LIMIT bots to 212.73.150.178 / Xxobster9.

User chat authorization 2026-08-21: same models/gates as the 1%/1% control
packs, exits and leverage from a 0.5% stop. Does not change the Xxobster8
1%/1% units already running on this host.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.gates.evidence import leverage_ceiling_from_stop, leverage_from_stop
from llm2.live.certificate import pack_fingerprint, refuse_vps_deploy_without_live_certificate
from llm2.registry.ledger import append_ledger

HOST = "212.73.150.178"
SSH = "ln2"
ACCOUNT = "Xxobster9"
TP_SL = 0.005
EXPIRES_UTC = "2026-09-04T21:00:00Z"
CREATED_UTC = "2026-08-21T21:30:00Z"

ETH_SRC = _ROOT / "artifacts" / "live_packs" / "pivot_eth_p75_ctrl_atr_w4"
SOL_SRC = _ROOT / "artifacts" / "live_packs" / "pivot_sol_geo_tp1_sl1_p75_w4"
ETH_DST = _ROOT / "artifacts" / "live_packs" / "pivot_eth_p50_tp05_sl05_w4"
SOL_DST = _ROOT / "artifacts" / "live_packs" / "pivot_sol_p50_tp05_sl05_w4"
ETH_CERT = _ROOT / "configs" / "live" / "pivot_eth_p50_tp05_sl05_w4_xxobster9_ln2_certificate.yaml"
SOL_CERT = _ROOT / "configs" / "live" / "pivot_sol_p50_tp05_sl05_w4_xxobster9_ln2_certificate.yaml"

ARMS = (
    {
        "pack": ETH_DST,
        "cert": ETH_CERT,
        "remote": "/opt/llm2-pivot-eth-p50-tp05-sl05",
        "unit": "llm2-pivot-eth-p50-tp05-sl05",
        "symbol": "ETHUSDT",
    },
    {
        "pack": SOL_DST,
        "cert": SOL_CERT,
        "remote": "/opt/llm2-pivot-sol-p50-tp05-sl05",
        "unit": "llm2-pivot-sol-p50-tp05-sl05",
        "symbol": "SOLUSDT",
    },
)


def _run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.check_call(cmd)


def _ssh(cmd: str) -> str:
    out = subprocess.check_output(["ssh", SSH, cmd], text=True)
    sys.stdout.write(out)
    return out


def _clone_pack(src: Path, dst: Path, *, pack_name: str, arm_id: str, strategy_id: str) -> str:
    if not (src / "model.joblib").is_file():
        raise FileNotFoundError(f"missing model in {src}")
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    shutil.copy2(src / "model.joblib", dst / "model.joblib")
    shutil.copy2(src / "risk_tiers.json", dst / "risk_tiers.json")

    strategy = json.loads((src / "strategy.json").read_text(encoding="utf-8"))
    lev = float(leverage_from_stop(TP_SL))
    ceil = float(leverage_ceiling_from_stop(TP_SL))
    strategy["strategy_id"] = strategy_id
    strategy["arm_id"] = arm_id
    strategy["tp_pct"] = TP_SL
    strategy["sl_pct"] = TP_SL
    strategy["leverage"] = lev
    strategy["leverage_ceiling"] = ceil
    strategy["leverage_from_stop"] = {
        "sl_pct": TP_SL,
        "mm_buffer": 0.005,
        "mark_buffer": 0.002,
        "haircut": 0.5,
        "operational": lev,
    }
    strategy["readiness_max"] = "RESEARCH_ONLY"
    strategy["promotion_allowed"] = False
    (dst / "strategy.json").write_text(
        json.dumps(strategy, indent=2) + "\n", encoding="utf-8"
    )

    src_meta = json.loads((src / "pack_meta.json").read_text(encoding="utf-8"))
    four_proof = dict(src_meta.get("four_proof_hashes") or {})
    meta = {
        "pack_name": pack_name,
        "arm_id": arm_id,
        "status": "LIVE_ACTIVE",
        "readiness": "RESEARCH_ONLY",
        "deployable": True,
        "evidence": src_meta.get("evidence"),
        "frozen_utc": "2026-08-21T21:30:00Z",
        "parent_pack": src.name,
        "exit_override": {"tp_pct": TP_SL, "sl_pct": TP_SL, "leverage": lev},
        "note": (
            "Same model/features/gate as parent 1%/1% pack. Take-profit and "
            "stop-loss changed to 0.5%/0.5% by user live authorization. "
            "Research still LIVE_STOP: ~80% same-15-minute exits."
        ),
        "four_proof_ok": True,
        "four_proof_hashes": four_proof,
        "live": {
            "deployed": True,
            "account_ref": ACCOUNT,
            "service": f"llm2-pivot-{pack_name.replace('pivot_', '').replace('_w4', '')}",
            "vps_host": HOST,
        },
        "sklearn_runtime": src_meta.get("sklearn_runtime"),
        "sklearn_repacked_utc": src_meta.get("sklearn_repacked_utc"),
    }
    (dst / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    fp = pack_fingerprint(dst)
    if not fp:
        raise RuntimeError(f"pack_fingerprint failed for {dst}")
    meta["pack_hash"] = fp
    (dst / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    fp = pack_fingerprint(dst)
    if not fp:
        raise RuntimeError(f"pack_fingerprint failed after meta hash for {dst}")
    (dst / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    return fp


def _write_cert(
    path: Path,
    *,
    strategy_id: str,
    pack_rel: str,
    pack_hash: str,
    four_proof: dict,
    symbol: str,
) -> None:
    hashes = "\n".join(f"  {k}: {v}" for k, v in four_proof.items())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""strategy_id: {strategy_id}
status: AUTHORIZED
authorized_by_user: true
vps_host: '{HOST}'
account_ref: {ACCOUNT}
intended_vps_host: '{HOST}'
intended_account_ref: {ACCOUNT}
pack_path: {pack_rel}
pack_hash: {pack_hash}
expires_utc: '{EXPIRES_UTC}'
created_utc: '{CREATED_UTC}'
four_proof_ok: true
four_proof_hashes:
{hashes}
notes: >-
  User explicitly authorized 2026-08-21 (UTC+7) real-USDT MIN_EXCHANGE pivot
  LIMIT micro-live on {HOST} / {ACCOUNT} ({symbol} 15m 0.5%/0.5%). Same
  model and p75 gate as the 1%/1% parent pack. Leverage from stop 0.5% = 41x.
  Research readiness remains LIVE_STOP / RESEARCH_ONLY (high same-bar exit
  rate). This certificate is operational authorization only.
""",
        encoding="utf-8",
    )


def build_local_packs() -> None:
    eth_src_meta = json.loads((ETH_SRC / "pack_meta.json").read_text(encoding="utf-8"))
    sol_src_meta = json.loads((SOL_SRC / "pack_meta.json").read_text(encoding="utf-8"))
    eth_fp = _clone_pack(
        ETH_SRC,
        ETH_DST,
        pack_name="pivot_eth_p50_tp05_sl05_w4",
        arm_id="eth_p50_tp05_sl05_w4",
        strategy_id="pivot_eth_p50_tp05_sl05_w4_ETHUSDT_15m",
    )
    sol_fp = _clone_pack(
        SOL_SRC,
        SOL_DST,
        pack_name="pivot_sol_p50_tp05_sl05_w4",
        arm_id="sol_p50_tp05_sl05_w4",
        strategy_id="pivot_sol_p50_tp05_sl05_w4_SOLUSDT_15m",
    )
    _write_cert(
        ETH_CERT,
        strategy_id="pivot_eth_p50_tp05_sl05_w4_ETHUSDT_15m",
        pack_rel="artifacts/live_packs/pivot_eth_p50_tp05_sl05_w4",
        pack_hash=eth_fp,
        four_proof=dict(eth_src_meta["four_proof_hashes"]),
        symbol="ETHUSDT",
    )
    _write_cert(
        SOL_CERT,
        strategy_id="pivot_sol_p50_tp05_sl05_w4_SOLUSDT_15m",
        pack_rel="artifacts/live_packs/pivot_sol_p50_tp05_sl05_w4",
        pack_hash=sol_fp,
        four_proof=dict(sol_src_meta["four_proof_hashes"]),
        symbol="SOLUSDT",
    )
    print("eth_fp", eth_fp, flush=True)
    print("sol_fp", sol_fp, flush=True)


def _scp_tar(local_dir: Path, remote_dir: str) -> None:
    _ssh(f"mkdir -p {remote_dir}")
    tmp = Path(tempfile.gettempdir()) / f"{local_dir.name}.tar"
    try:
        _run(
            [
                "tar",
                "-C",
                str(local_dir),
                "--exclude=__pycache__",
                "--exclude=*.pyc",
                "-cf",
                str(tmp),
                ".",
            ]
        )
        _run(["scp", str(tmp), f"{SSH}:/tmp/{tmp.name}"])
        _ssh(f"tar -C {remote_dir} -xf /tmp/{tmp.name} && rm -f /tmp/{tmp.name}")
    finally:
        if tmp.exists():
            tmp.unlink()


def _copy_xx9_from_ln1() -> None:
    subprocess.check_call(
        [
            "ssh",
            "ln1",
            'grep -E "^Xxobster9_API_" /root/.trading/secrets.env > /tmp/xx9.env && chmod 600 /tmp/xx9.env',
        ]
    )
    tmp = Path(tempfile.gettempdir()) / "xx9.env"
    try:
        _run(["scp", "ln1:/tmp/xx9.env", str(tmp)])
        _run(["scp", str(tmp), f"{SSH}:/tmp/xx9.env"])
        _ssh(
            "mkdir -p /root/.trading && touch /root/.trading/secrets.env && "
            "chmod 600 /root/.trading/secrets.env && "
            'grep -v "^Xxobster9_API_" /root/.trading/secrets.env > /tmp/s.env || true && '
            "cat /tmp/xx9.env >> /tmp/s.env && mv /tmp/s.env /root/.trading/secrets.env && "
            "chmod 600 /root/.trading/secrets.env && rm -f /tmp/xx9.env && "
            'echo xx9_lines=$(grep -c "^Xxobster9_API_" /root/.trading/secrets.env)'
        )
    finally:
        if tmp.exists():
            tmp.unlink()
        subprocess.call(["ssh", "ln1", "rm -f /tmp/xx9.env"])


def _unit_body(arm: dict) -> str:
    remote = arm["remote"]
    unit = arm["unit"]
    return f"""[Unit]
Description=LLM2 pivot LIMIT {unit} LIVE MIN_EXCHANGE Xxobster9 0.5pct
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
    _scp_tar(arm["pack"], f"{remote}/pack")
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
if "llm2" not in bots:
    bots.append("llm2")
host["bots"] = bots
llm2 = r.setdefault("bots", {}).setdefault("llm2", {})
also = set(llm2.get("also_fetch_timeframes") or [])
also.add("1m")
llm2["also_fetch_timeframes"] = sorted(also)
llm2["timeframe"] = "15m"
acc = llm2.get("account")
wanted = ["Xxobster7", "Xxobster8", "Xxobster9"]
if isinstance(acc, list):
    for name in wanted:
        if name not in acc:
            acc.append(name)
    llm2["account"] = acc
elif acc:
    llm2["account"] = [acc] + [n for n in wanted if n != acc]
else:
    llm2["account"] = ["Xxobster8", "Xxobster9"]
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
    if leverage_from_stop(TP_SL) != 41.0:
        raise SystemExit(f"expected operational leverage 41, got {leverage_from_stop(TP_SL)}")
    build_local_packs()
    for arm in ARMS:
        refuse_vps_deploy_without_live_certificate(path=arm["cert"], host=HOST)
        fp = pack_fingerprint(arm["pack"])
        raw = arm["cert"].read_text(encoding="utf-8")
        if fp is None or fp not in raw:
            raise SystemExit(f"cert/pack hash mismatch for {arm['unit']}")
        print("cert_ok", arm["cert"].name, flush=True)

    _copy_xx9_from_ln1()
    _patch_registry()

    for arm in ARMS:
        print("DEPLOY", arm["unit"], flush=True)
        _deploy_arm(arm)

    units = " ".join(a["unit"] + ".service" for a in ARMS)
    _ssh(
        f"systemctl daemon-reload && systemctl enable --now {units} && "
        f"sleep 6 && systemctl is-active {units}"
    )
    print("KEEP_XX8", flush=True)
    _ssh(
        "systemctl is-active llm2-pivot-eth-p75-ctrl-atr-w4 llm2-pivot-sol-geo-p75-w4; "
        "systemctl show -p ActiveState -p NRestarts "
        "llm2-pivot-eth-p50-tp05-sl05 llm2-pivot-sol-p50-tp05-sl05 "
        "llm2-pivot-eth-p75-ctrl-atr-w4 llm2-pivot-sol-geo-p75-w4"
    )
    for arm in ARMS:
        _ssh(f"tail -n 30 {arm['remote']}/logs/pivot_live.log || true")
    append_ledger(
        f"PIVOT_LIVE_AUTH ETH+SOL 15m 0.5pct/0.5pct account={ACCOUNT} host={HOST} "
        "packs=eth_p50_tp05_sl05_w4,sol_p50_tp05_sl05_w4 "
        "(research remains LIVE_STOP; user operational authorize)",
        tier=2,
    )
    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
