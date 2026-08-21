"""Authorize + stamp ETH K5 p75 pack for Xxobster3 live deploy.

Certificate stays under configs/live/ (not inside pack) so pack_hash is stable.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.evidence.pack_registry import (  # noqa: E402
    ensure_registry_schema,
    regenerate_versions_md,
    register_freeze,
    register_live,
)
from llm2.live.certificate import load_certificate, pack_fingerprint  # noqa: E402
from llm2.paths import ARTIFACTS, ROOT  # noqa: E402

DST = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_k5_double3h_p75_v1"
CERT = ROOT / "configs" / "live" / "structure_v1_ethusdt_k5_double3h_p75_v1_certificate.yaml"
VERSION_ID = "eth_k5_double3h_p75_v1"
SERVICE = "llm2-structure-eth-k5-double3h-p75-v1"
ACCOUNT = "Xxobster3"
HOST = "185.203.119.52"
GEN = "structure_v1_eth_k5_expectancy_strength_p75_001"
REPORT = ARTIFACTS / "reports" / f"{GEN}_latest.json"


def main() -> int:
    if not DST.is_dir():
        raise SystemExit(f"missing pack {DST}")
    if not (DST / "model.joblib").is_file():
        raise SystemExit("missing model.joblib")
    # Never keep certificate inside pack (breaks hash stability).
    for name in ("certificate.yaml", "pack_hash.txt"):
        p = DST / name
        if p.is_file():
            p.unlink()

    strat_path = DST / "strategy.json"
    strat = json.loads(strat_path.read_text(encoding="utf-8"))
    mt = dict(strat.get("multitrade") or {})
    mt["strength_quantile"] = 0.75
    mt["version_id"] = VERSION_ID
    strat["multitrade"] = mt
    strat["version_id"] = VERSION_ID
    strat["account"] = ACCOUNT
    strat["what_it_does"] = (
        "LIVE MICRO p75 strength arm on Xxobster3. K=5 books/side; mean_strength "
        "q=0.75 of 168-bar |mean|; TP+1% SL-2% hold12; size 2x min when same-side "
        "entry within 3h. MIN_EXCHANGE. Signal candles Binance; execution Bybit."
    )
    lineage = dict(strat.get("version_lineage") or {})
    lineage["live_auth"] = {
        "authorized_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "account": ACCOUNT,
        "vps_host": HOST,
        "service": SERVICE,
        "note": "User authorized ship 2026-08-05 chat",
    }
    strat["version_lineage"] = lineage
    strat_path.write_text(json.dumps(strat, indent=2) + "\n", encoding="utf-8")

    metrics: dict = {}
    if REPORT.is_file():
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        metrics = dict((report.get("candidate") or {}).get("stitched") or {})

    meta = {
        "version_id": VERSION_ID,
        "parent": "structure_v1_ethusdt_k5_double3h_v1",
        "research_arm": "mean_strength|hold12|tp1pct|K=5|double3h|q0.75",
        "frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "strategy_id": strat["strategy_id"],
        "status": "LIVE_ACTIVE",
        "readiness": "MICRO_LIVE_CANDIDATE",
        "live": {
            "deployed": True,
            "account_ref": ACCOUNT,
            "service": SERVICE,
            "vps_host": HOST,
        },
        "metrics": {
            "profit_factor": metrics.get("profit_factor"),
            "expectancy_return_units": metrics.get("expectancy_return_units"),
            "n_trades": metrics.get("n_trades"),
            "win_rate": metrics.get("win_rate"),
            "window": "outer_v2_hard_end_2026-05-01",
            "source_report": str(REPORT.relative_to(ROOT)).replace("\\", "/")
            if REPORT.is_file()
            else None,
        },
    }
    (DST / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (DST / "README.md").write_text(
        f"# {VERSION_ID}\n\n"
        "Live micro pack: eth_k5_double3h geometry with `strength_quantile=0.75`.\n"
        f"Account `{ACCOUNT}` on `{HOST}` · service `{SERVICE}`.\n"
        f"Evidence: `{GEN}` OUTER_TRANSFER_COMPARE.\n",
        encoding="utf-8",
    )

    # Registry rewrites pack_meta — seal fingerprint only after those writes.
    ensure_registry_schema()
    register_freeze(
        DST,
        evidence={
            "generation_id": GEN,
            "report_paths": [
                str(REPORT.relative_to(ROOT)).replace("\\", "/")
                if REPORT.is_file()
                else ""
            ],
        },
        metrics=meta.get("metrics") or {},
        status="LIVE_ACTIVE",
        readiness="MICRO_LIVE_CANDIDATE",
        require_run_id=False,
        ledger=True,
    )
    register_live(
        VERSION_ID,
        deployed=True,
        account_ref=ACCOUNT,
        service=SERVICE,
        certificate_path=str(CERT.relative_to(ROOT)).replace("\\", "/"),
    )
    regenerate_versions_md()

    for name in ("certificate.yaml", "pack_hash.txt"):
        p = DST / name
        if p.is_file():
            p.unlink()
    fp = pack_fingerprint(DST)
    if not fp:
        raise RuntimeError("pack_fingerprint failed")
    # pack_hash.txt is excluded from the fingerprint; do not rewrite pack_meta after this.
    (DST / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8", newline="\n")

    text = CERT.read_text(encoding="utf-8")
    CERT.write_text(
        re.sub(r"pack_hash:.*", f"pack_hash: {fp}", text),
        encoding="utf-8",
        newline="\n",
    )
    cert = load_certificate(CERT)
    if not cert.is_deployable or cert.pack_hash != fp:
        raise RuntimeError(f"certificate not deployable hash={cert.pack_hash} fp={fp}")
    if cert.vps_host != HOST or cert.account_ref != ACCOUNT:
        raise RuntimeError("certificate host/account mismatch")
    if pack_fingerprint(DST) != fp:
        raise RuntimeError("pack fingerprint drifted after seal")

    print(
        json.dumps(
            {
                "version_id": VERSION_ID,
                "pack_hash": fp,
                "account": ACCOUNT,
                "host": HOST,
                "service": SERVICE,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
