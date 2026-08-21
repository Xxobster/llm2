"""Sanity for 0.5%/0.5% pivot packs cloned from the 1%/1% parents."""

from __future__ import annotations

import json

from llm2.gates.evidence import leverage_from_stop
from llm2.live.certificate import pack_fingerprint, refuse_vps_deploy_without_live_certificate

from scripts.deploy_pivot_xxobster9_ln2_tp05 import (
    ETH_CERT,
    ETH_DST,
    HOST,
    SOL_CERT,
    SOL_DST,
    TP_SL,
    build_local_packs,
)


def test_leverage_from_half_percent_stop() -> None:
    assert leverage_from_stop(0.005) == 41.0


def test_build_tp05_packs_and_certs() -> None:
    build_local_packs()
    eth = json.loads((ETH_DST / "strategy.json").read_text(encoding="utf-8"))
    sol = json.loads((SOL_DST / "strategy.json").read_text(encoding="utf-8"))
    assert eth["tp_pct"] == TP_SL
    assert eth["sl_pct"] == TP_SL
    assert eth["leverage"] == 41.0
    assert sol["tp_pct"] == TP_SL
    assert sol["sl_pct"] == TP_SL
    assert sol["leverage"] == 41.0
    assert eth["thr_any"] == 0.35
    assert sol["thr_any"] == 0.35
    eth_fp = pack_fingerprint(ETH_DST)
    sol_fp = pack_fingerprint(SOL_DST)
    assert eth_fp and eth_fp in ETH_CERT.read_text(encoding="utf-8")
    assert sol_fp and sol_fp in SOL_CERT.read_text(encoding="utf-8")
    refuse_vps_deploy_without_live_certificate(path=ETH_CERT, host=HOST)
    refuse_vps_deploy_without_live_certificate(path=SOL_CERT, host=HOST)
