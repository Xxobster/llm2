"""Fail-closed VPS deploy gate — research charts never deploy."""

from __future__ import annotations

import argparse
import sys

from llm2.live.certificate import refuse_vps_deploy_without_live_certificate
from llm2.research_policy import PolicyError


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="94.156.189.76")
    ap.add_argument("--account", default="xxobster7")
    args = ap.parse_args()
    try:
        cert = refuse_vps_deploy_without_live_certificate(host=args.host)
    except PolicyError as exc:
        print(f"REFUSED: {exc}")
        print(
            f"Requested account_ref={args.account!r}. "
            "Authorize configs/live/structure_v1_lgbm_certificate.yaml only after a "
            "frozen live pack with funding + Mark parity, then re-issue an explicit deploy command."
        )
        return 5
    print(f"certificate allows deploy: {cert}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
