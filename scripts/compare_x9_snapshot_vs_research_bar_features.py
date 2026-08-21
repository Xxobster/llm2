"""Compare live feature_snapshot vs research indicators.sqlite raw structure columns.

For bars where warehouse rebuild (build_space) diverges, check whether the *stored*
warehouse bar_features row still differs from live — pure storage parity.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from llm2.paths import ARTIFACTS  # noqa: E402

LEDGER = ARTIFACTS / "reports" / "_x9_micro_live_state.sqlite"
IND = Path(r"D:\projectsdata\indicators\indicators.sqlite")
BUNDLE = ARTIFACTS / "reports" / "x9_live_full_parity_bundle_latest.json"
OUT = ARTIFACTS / "reports" / "x9_snapshot_vs_research_bar_features_latest.json"
# columns that live uses in model and that exist as warehouse bar_features fields
# (engineered vol columns may not be raw)


def main() -> int:
    con_l = sqlite3.connect(f"file:{LEDGER}?mode=ro", uri=True)
    decisions = con_l.execute(
        "SELECT bar_ts_ms, pred_mean, detail FROM decisions ORDER BY bar_ts_ms"
    ).fetchall()
    con_l.close()

    con = sqlite3.connect(f"file:{IND}?mode=ro", uri=True)
    names = [r[1] for r in con.execute("PRAGMA table_info(bar_features)").fetchall()]
    rows_out = []
    for ts, pm, detail in decisions:
        det = json.loads(detail) if detail else {}
        snap = (det.get("feature_snapshot") or {}).get("values") or {}
        if not snap:
            rows_out.append({"bar_ts_ms": ts, "note": "no_snapshot"})
            continue
        common = [c for c in snap if c in names]
        if not common:
            rows_out.append({"bar_ts_ms": ts, "note": "no_common_cols_in_warehouse_table"})
            continue
        row = con.execute(
            f"SELECT {','.join(common)} FROM bar_features "
            "WHERE symbol='ETHUSDT' AND timeframe='1h' AND source='binance' AND ts_ms=?",
            (int(ts),),
        ).fetchone()
        if not row:
            rows_out.append({"bar_ts_ms": ts, "note": "warehouse_row_missing"})
            continue
        wh = dict(zip(common, row))
        mism = []
        for c in common:
            try:
                a = float(snap[c])
                b = float(wh[c]) if wh[c] is not None else float("nan")
                if not (np.isfinite(a) and np.isfinite(b)):
                    if snap[c] != wh[c]:
                        mism.append({"col": c, "live": snap[c], "research": wh[c]})
                    continue
                d = abs(a - b)
                if d > 1e-9:
                    mism.append({"col": c, "live": a, "research": b, "abs": d})
            except (TypeError, ValueError):
                if snap[c] != wh[c]:
                    mism.append({"col": c, "live": snap[c], "research": wh[c]})
        mism.sort(key=lambda x: float(x.get("abs") or 0), reverse=True)
        rows_out.append(
            {
                "bar_ts_ms": int(ts),
                "bar_utc": datetime.fromtimestamp(int(ts) / 1000, tz=timezone.utc).isoformat(),
                "live_pred_mean": pm,
                "n_common": len(common),
                "n_mismatch": len(mism),
                "max_abs": max((float(m["abs"]) for m in mism if "abs" in m), default=0.0),
                "identical": len(mism) == 0,
                "top_mismatches": mism[:15],
            }
        )
    con.close()

    report = {
        "evidence_class": "LIVE_SNAPSHOT_VS_RESEARCH_BAR_FEATURES",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "note": (
            "Only columns present in both feature_snapshot and research bar_features. "
            "Vol-scaled / derived pack features may be absent in warehouse table."
        ),
        "rows": rows_out,
        "n_identical": sum(1 for r in rows_out if r.get("identical")),
        "n_with_snap": sum(1 for r in rows_out if r.get("n_common") is not None),
    }
    OUT.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("n_identical", "n_with_snap", "note")}, indent=2))
    for r in rows_out:
        if r.get("identical") is True:
            print("OK", r["bar_utc"], "n_common", r["n_common"])
        elif r.get("identical") is False:
            print(
                "DIFF",
                r["bar_utc"],
                "mis",
                r["n_mismatch"],
                "max_abs",
                r["max_abs"],
                "top",
                [m["col"] for m in r["top_mismatches"][:5]],
            )
        else:
            print("META", r)
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
