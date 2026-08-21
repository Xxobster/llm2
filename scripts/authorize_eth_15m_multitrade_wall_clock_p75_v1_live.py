"""Authorize + stamp ETH 15m wall-clock p75 pack for Xxobster11 live deploy.

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

DST = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1"
CERT = (
    ROOT
    / "configs"
    / "live"
    / "structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1_certificate.yaml"
)
VERSION_ID = "eth_15m_multitrade_wall_clock_p75_v1"
STRATEGY_ID = "structure_v1_lgbm_ETHUSDT_15m_direction_multitrade_wall_clock_p75_v1"
SERVICE = "llm2-structure-eth-15m-multitrade-wall-clock-p75-v1"
ACCOUNT = "Xxobster11"
HOST = "185.203.119.52"
GEN = "structure_v1_eth_15m_multitrade_geometry_001"
REPORT = ARTIFACTS / "reports" / f"{GEN}_latest.json"


def main() -> int:
    if not DST.is_dir():
        raise SystemExit(f"missing pack {DST}")
    if not (DST / "model.joblib").is_file():
        raise SystemExit("missing model.joblib")
    for name in ("certificate.yaml", "pack_hash.txt"):
        p = DST / name
        if p.is_file():
            p.unlink()

    strat_path = DST / "strategy.json"
    strat = json.loads(strat_path.read_text(encoding="utf-8"))
    strat["account"] = ACCOUNT
    strat["strategy_id"] = STRATEGY_ID
    strat["version_id"] = VERSION_ID
    strat["what_it_does"] = (
        "LIVE MICRO ETH 15m multitrade wall-clock p75 on Xxobster11. "
        "K=7/side; mean_strength q=0.75 of 672-bar |mean|; base hold 24 / addon 48; "
        "TP1%/SL2%; fib 1.618 books 3+; touch 1m. MIN_EXCHANGE. "
        "Signal candles Binance via botsgeneral shared collector; execution Bybit."
    )
    lineage = dict(strat.get("version_lineage") or {})
    lineage["parent_pack"] = "structure_v1_ethusdt_multitrade_p75_v1"
    lineage["research_arm"] = (
        "15m|wall_clock|K=7|fib1.618|base_hold24|addon48|lookback672|"
        "label24|strength_q=0.75|touch1m"
    )
    lineage["generation_id"] = GEN
    lineage["evidence_class"] = "OUTER_TRANSFER_COMPARE"
    lineage["live_auth"] = {
        "authorized_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "account": ACCOUNT,
        "vps_host": HOST,
        "service": SERVICE,
        "note": "User authorized deploy 2026-08-05 chat: Xxobster11 / 185.203.119.52",
    }
    lineage.pop("note", None)
    strat["version_lineage"] = lineage
    strat_path.write_text(json.dumps(strat, indent=2) + "\n", encoding="utf-8")

    metrics: dict = {}
    if REPORT.is_file():
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        best = (report.get("arms") or {}).get("wall_clock_q75") or {}
        metrics = dict(best.get("stitched") or {})

    meta = {
        "version_id": VERSION_ID,
        "parent": "structure_v1_ethusdt_multitrade_p75_v1",
        "research_arm": lineage["research_arm"],
        "frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "strategy_id": STRATEGY_ID,
        "status": "LIVE_ACTIVE",
        "readiness": "MICRO_LIVE_CANDIDATE",
        "timeframe": "15m",
        "touch_timeframe": "1m",
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
        "Live micro pack: ETHUSDT 15m multitrade wall-clock p75.\n"
        f"Account `{ACCOUNT}` on `{HOST}` · service `{SERVICE}`.\n"
        f"Evidence: `{GEN}` OUTER_TRANSFER_COMPARE.\n"
        "Candles: botsgeneral shared `shared_candles.db` (Binance signal).\n",
        encoding="utf-8",
    )

    # Empty slice DB so unit env path exists; first decide builds full history.
    slice_db = DST / "indicators_live_slice.sqlite"
    if not slice_db.is_file():
        import sqlite3

        sqlite3.connect(slice_db).close()

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
