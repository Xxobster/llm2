"""Deploy frozen structure_v1 micro-live pack to ln1 and start SHADOW systemd unit.

Requires AUTHORIZED certificate matching host/account. Does not enable LIVE orders
unless --live-orders is passed (still MIN_EXCHANGE).
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from llm2.live.certificate import (
    DEFAULT_CERT,
    PACK_DIR,
    pack_fingerprint,
    refuse_vps_deploy_without_live_certificate,
)
from llm2.paths import ROOT

REMOTE_ROOT = "/opt/llm2-structure"
HOST_ALIAS = "ln1"


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.check_call(cmd)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="94.156.189.76")
    ap.add_argument("--account", default="Xxobster7")
    ap.add_argument("--mode", choices=("SHADOW", "LIVE"), default="SHADOW")
    ap.add_argument("--live-orders", action="store_true")
    ap.add_argument("--ssh", default=HOST_ALIAS)
    args = ap.parse_args()

    cert = refuse_vps_deploy_without_live_certificate(host=args.host)
    if cert.account_ref and cert.account_ref.lower() != args.account.lower():
        raise SystemExit(
            f"account mismatch cert={cert.account_ref} requested={args.account}"
        )
    fp = pack_fingerprint(PACK_DIR)
    if not fp or fp != cert.pack_hash:
        raise SystemExit(f"pack hash mismatch cert={cert.pack_hash} pack={fp}")

    # remote dirs
    run(["ssh", args.ssh, f"mkdir -p {REMOTE_ROOT}/{{pack,state,logs,venv}}"])

    # sync pack + llm2 package + runner deps list
    run(
        [
            "scp",
            "-r",
            str(PACK_DIR),
            f"{args.ssh}:{REMOTE_ROOT}/pack_parent",
        ]
    )
    run(
        [
            "ssh",
            args.ssh,
            f"rm -rf {REMOTE_ROOT}/pack && mv {REMOTE_ROOT}/pack_parent/structure_v1_lgbm {REMOTE_ROOT}/pack && rm -rf {REMOTE_ROOT}/pack_parent",
        ]
    )
    run(
        [
            "scp",
            "-r",
            str(ROOT / "llm2"),
            str(ROOT / "configs" / "live" / "structure_v1_lgbm_certificate.yaml"),
            f"{args.ssh}:{REMOTE_ROOT}/",
        ]
    )

    # bootstrap venv + deps (lightgbm needed for model)
    bootstrap = f"""
set -e
cd {REMOTE_ROOT}
python3 -m venv venv
./venv/bin/pip install -U pip
./venv/bin/pip install lightgbm joblib pandas numpy pyyaml scikit-learn
# secrets: expect /root/.trading/secrets.env or copy from ops — do not echo
mkdir -p /root/.trading
test -f /root/.trading/secrets.env || test -f /home/xgb/.trading/secrets.env || true
"""
    run(["ssh", args.ssh, f"bash -lc {bootstrap!r}"])

    unit = f"""[Unit]
Description=LLM2 structure_v1 micro-live ({args.mode})
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory={REMOTE_ROOT}
Environment=PYTHONPATH={REMOTE_ROOT}
Environment=LLM2_INDICATORS_DB={REMOTE_ROOT}/pack/indicators_live_slice.sqlite
Environment=LLM2_STRUCTURE_SOURCE=binance
Environment=SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db
ExecStart={REMOTE_ROOT}/venv/bin/python -m llm2.live.micro_runner --pack {REMOTE_ROOT}/pack --state {REMOTE_ROOT}/state/micro_live_state.sqlite --mode {args.mode} {"--live-orders" if args.live_orders else ""} --account {args.account} --cert {REMOTE_ROOT}/structure_v1_lgbm_certificate.yaml
Restart=always
RestartSec=10
StandardOutput=append:{REMOTE_ROOT}/logs/micro_live.log
StandardError=append:{REMOTE_ROOT}/logs/micro_live.log

[Install]
WantedBy=multi-user.target
"""
    # write unit via ssh heredoc
    run(
        [
            "ssh",
            args.ssh,
            f"cat > /etc/systemd/system/llm2-structure-micro.service <<'EOF'\n{unit}\nEOF\n"
            f"systemctl daemon-reload && systemctl enable --now llm2-structure-micro.service && "
            f"systemctl --no-pager -l status llm2-structure-micro.service | head -30",
        ]
    )
    print("deployed", args.mode, "fp", fp[:16], flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"DEPLOY_FAIL: {exc}", file=sys.stderr)
        raise
