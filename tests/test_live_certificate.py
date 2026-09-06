"""Live certificate fail-closed gates."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from llm2.live.certificate import (
    pack_fingerprint,
    refuse_vps_deploy_without_live_certificate,
)
from llm2.research_policy import PolicyError


def test_vps_deploy_refused_without_authorized_certificate(tmp_path: Path):
    blocked = tmp_path / "blocked.yaml"
    blocked.write_text(
        yaml.safe_dump(
            {
                "strategy_id": "test",
                "status": "BLOCKED",
                "authorized_by_user": False,
                "vps_host": None,
                "account_ref": None,
                "pack_hash": None,
            }
        ),
        encoding="utf-8",
    )
    with pytest.raises(PolicyError, match="VPS deploy REFUSED"):
        refuse_vps_deploy_without_live_certificate(path=blocked, host="94.156.189.76")


def test_vps_deploy_refused_on_account_mismatch(tmp_path: Path):
    cert = tmp_path / "ok.yaml"
    cert.write_text(
        yaml.safe_dump(
            {
                "strategy_id": "test",
                "status": "AUTHORIZED",
                "authorized_by_user": True,
                "vps_host": "212.73.150.178",
                "account_ref": "Xxobster11",
                "pack_hash": "a" * 64,
                "expires_utc": "2099-01-01T00:00:00Z",
                "four_proof_ok": True,
                "four_proof_hashes": {
                    "builder_responsiveness": "b" * 64,
                    "recompute_prefix": "c" * 64,
                    "no_live_feature_fill": "d" * 64,
                    "layer_a_pred_identity": "e" * 64,
                },
            }
        ),
        encoding="utf-8",
    )
    refuse_vps_deploy_without_live_certificate(
        path=cert, host="212.73.150.178", account="Xxobster11"
    )
    with pytest.raises(PolicyError, match="account mismatch"):
        refuse_vps_deploy_without_live_certificate(
            path=cert, host="212.73.150.178", account="Xxobster3"
        )


def test_authorized_certificate_matches_pack_when_present():
    # Live cert may be AUTHORIZED after user deploy command; still require hash shape.
    from llm2.live.certificate import DEFAULT_CERT, load_certificate

    if not DEFAULT_CERT.is_file():
        pytest.skip("no certificate file")
    cert = load_certificate()
    if cert.status != "AUTHORIZED":
        pytest.skip("certificate not authorized in this workspace")
    assert cert.authorized_by_user is True
    assert cert.vps_host == "94.156.189.76"
    assert cert.account_ref
    assert cert.pack_hash and len(cert.pack_hash) == 64
