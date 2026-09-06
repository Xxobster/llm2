"""Live deployment certificate — fail closed without explicit authorization.

Research charts, settle PASS, and SHADOW_READY_CANDIDATE do **not** authorize VPS deploy.
A time-limited certificate must exist, hash-match the frozen pack, and be user-authorized.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from llm2.paths import ROOT
from llm2.research_policy import MIN_SIZE_EQUITY_CAVEAT, PolicyError

CERT_DIR = ROOT / "configs" / "live"
DEFAULT_CERT = CERT_DIR / "structure_v1_lgbm_certificate.yaml"
PACK_DIR = ROOT / "artifacts" / "live_packs" / "structure_v1_lgbm"


@dataclass(frozen=True)
class LiveCertificate:
    strategy_id: str
    status: str
    authorized_by_user: bool
    vps_host: str | None
    account_ref: str | None
    pack_hash: str | None
    expires_utc: str | None
    path: Path

    four_proof_ok: bool = False
    four_proof_hashes: dict[str, str] | None = None

    @property
    def is_deployable(self) -> bool:
        if self.status != "AUTHORIZED":
            return False
        if not self.authorized_by_user:
            return False
        if not self.vps_host or not self.account_ref:
            return False
        if not self.pack_hash:
            return False
        if not self.four_proof_ok or not self.four_proof_hashes:
            return False
        if self.expires_utc:
            exp = datetime.fromisoformat(self.expires_utc.replace("Z", "+00:00"))
            if datetime.now(timezone.utc) > exp:
                return False
        return True


def load_certificate(path: Path = DEFAULT_CERT) -> LiveCertificate:
    if not path.is_file():
        raise PolicyError(
            f"live certificate missing at {path}. Research readiness is not a deploy "
            "certificate. Create and user-authorize a certificate before any VPS action."
        )
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    hashes = raw.get("four_proof_hashes") or {}
    return LiveCertificate(
        strategy_id=str(raw.get("strategy_id", "")),
        status=str(raw.get("status", "BLOCKED")),
        authorized_by_user=bool(raw.get("authorized_by_user", False)),
        vps_host=raw.get("vps_host"),
        account_ref=raw.get("account_ref"),
        pack_hash=raw.get("pack_hash"),
        expires_utc=raw.get("expires_utc"),
        path=path,
        four_proof_ok=bool(raw.get("four_proof_ok", False)),
        four_proof_hashes=dict(hashes) if isinstance(hashes, dict) else None,
    )


def refuse_vps_deploy_without_live_certificate(
    *,
    path: Path = DEFAULT_CERT,
    host: str | None = None,
    account: str | None = None,
) -> LiveCertificate:
    """Hard stop for VPS sync/restart/enable unless a valid certificate is present."""
    cert = load_certificate(path)
    if not cert.four_proof_ok or not cert.four_proof_hashes:
        raise PolicyError(
            f"VPS deploy REFUSED for {cert.strategy_id or path.name}: "
            "certificate missing four_proof_ok + four_proof_hashes. "
            "Shared leakage PASS alone is not deploy evidence (D-055/D-057)."
        )
    if not cert.is_deployable:
        raise PolicyError(
            f"VPS deploy REFUSED for {cert.strategy_id or path.name}: "
            f"status={cert.status!r} authorized_by_user={cert.authorized_by_user} "
            f"pack_hash={cert.pack_hash!r}. Settle PASS / Finplot / SHADOW_READY_CANDIDATE "
            "are research evidence only. Require a frozen live pack, funding+Mark parity, "
            "four-proof causality hashes, and explicit user authorization on the certificate."
            + (f" Requested host={host!r}." if host else "")
        )
    if host and cert.vps_host and host != cert.vps_host:
        raise PolicyError(
            f"VPS host mismatch: certificate allows {cert.vps_host!r}, requested {host!r}"
        )
    if account and cert.account_ref and account != cert.account_ref:
        raise PolicyError(
            f"VPS account mismatch: certificate allows {cert.account_ref!r}, requested {account!r}"
        )
    return cert


def pack_fingerprint(pack_dir: Path = PACK_DIR) -> str | None:
    """Hash pack artifacts (config + model + feature slice); None if incomplete."""
    if not pack_dir.is_dir():
        return None
    parts: list[bytes] = []
    # Case-fold sort so Windows (case-insensitive) and Linux produce the same digest.
    files = sorted(
        (p for p in pack_dir.rglob("*") if p.is_file()),
        key=lambda p: p.relative_to(pack_dir).as_posix().lower(),
    )
    for p in files:
        if p.suffix.lower() not in {
            ".json",
            ".yaml",
            ".yml",
            ".md",
            ".txt",
            ".joblib",
            ".sqlite",
            ".parquet",
        }:
            continue
        # Avoid circular hash / runtime state contaminating the freeze stamp.
        if p.name in {"pack_hash.txt", "PACK_HASH"}:
            continue
        # Live feature slice is refreshed hourly; model+strategy JSON are the freeze.
        if p.suffix.lower() == ".sqlite":
            continue
        parts.append(p.relative_to(pack_dir).as_posix().encode())
        parts.append(p.read_bytes())
    if not parts:
        return None
    return hashlib.sha256(b"\0".join(parts)).hexdigest()


def write_pack_scaffold(
    *,
    settlement: dict[str, Any],
    pack_dir: Path = PACK_DIR,
) -> Path:
    """Write a non-deployable research pack stub (no secrets, no AUTHORIZED flag)."""
    pack_dir.mkdir(parents=True, exist_ok=True)
    meta = {
        "strategy_id": "structure_v1_lgbm_BTCUSDT_1h",
        "status": "RESEARCH_PACK_ONLY",
        "readiness": "RESEARCH_ONLY",
        "deployable": False,
        "settlement_verdict": settlement.get("verdict"),
        "settlement_overall": settlement.get("overall"),
        "pooled_pf": settlement.get("pooled_pf"),
        "fold_geometry": "v2",
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
        "required_before_live": [
            "FOUR_PROOF_GATE_V1 (responsiveness + recompute_prefix + no_live_fill + layer_a)",
            "botsgeneral leakage PASS is necessary but NEVER sufficient for warehouse spaces",
            "structure knowable-when / confirmation-time tests PASS",
            "funding attached at actual settlements",
            "Mark/tier liquidation pack (not SIMPLIFIED)",
            "live certificate status=AUTHORIZED + authorized_by_user=true + four_proof_hashes",
            "explicit user deploy command naming host and account",
        ],
        "vps_deploy": "FORBIDDEN",
    }
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    (pack_dir / "README.md").write_text(
        "# structure_v1 LightGBM research pack\n\n"
        "**Not deployable.** This scaffold records settle evidence only.\n"
        "VPS deploy requires `configs/live/structure_v1_lgbm_certificate.yaml` with "
        "`status: AUTHORIZED` and `authorized_by_user: true`.\n",
        encoding="utf-8",
    )
    return pack_dir

