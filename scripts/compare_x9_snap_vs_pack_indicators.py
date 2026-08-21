"""Pull pack indicators rows for decision bars and compare to live feature_snapshot raw cols."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from llm2.paths import ARTIFACTS  # noqa: E402

HOST = "185.203.119.52"
OUT = ARTIFACTS / "reports" / "x9_live_snap_vs_pack_indicators_latest.json"

REMOTE = r'''
import json, sqlite3
from pathlib import Path
ledger = Path("/opt/llm2-structure-eth-multitrade-p75-v1/state/micro_live_state.sqlite")
ind = Path("/opt/llm2-structure-eth-multitrade-p75-v1/pack/indicators_live_slice.sqlite")
con_l = sqlite3.connect(f"file:{ledger}?mode=ro", uri=True)
decs = con_l.execute("SELECT bar_ts_ms, pred_mean, detail FROM decisions ORDER BY bar_ts_ms").fetchall()
con_l.close()
con = sqlite3.connect(f"file:{ind}?mode=ro", uri=True)
names = [r[1] for r in con.execute("PRAGMA table_info(bar_features)").fetchall()]
n1h = con.execute("SELECT COUNT(*) FROM bar_features WHERE source='binance' AND timeframe='1h'").fetchone()[0]
out = {"pack_1h_n": n1h, "bars": []}
for ts, pm, detail in decs:
    det = json.loads(detail) if detail else {}
    snap = (det.get("feature_snapshot") or {}).get("values") or {}
    row = con.execute(
        "SELECT * FROM bar_features WHERE source=? AND timeframe=? AND ts_ms=?",
        ("binance", "1h", int(ts)),
    ).fetchone()
    if not row:
        out["bars"].append({"ts_ms": ts, "error": "pack_row_missing"})
        continue
    d = dict(zip(names, row))
    common = [c for c in snap if c in d]
    mism = []
    for c in common:
        try:
            a = float(snap[c]); b = float(d[c]) if d[c] is not None else float("nan")
            if abs(a-b) > 1e-9:
                mism.append({"col": c, "snap": a, "pack": b, "abs": abs(a-b)})
        except Exception:
            if snap[c] != d[c]:
                mism.append({"col": c, "snap": snap[c], "pack": d[c]})
    mism.sort(key=lambda x: float(x.get("abs") or 0), reverse=True)
    out["bars"].append({
        "ts_ms": int(ts),
        "pred_mean": pm,
        "pack_close": d.get("close"),
        "n_common": len(common),
        "n_mismatch": len(mism),
        "identical": len(mism) == 0,
        "top": mism[:12],
    })
con.close()
print(json.dumps(out))
'''


def main() -> int:
    helper = ARTIFACTS / "reports" / "_x9_remote_pack_snap.py"
    helper.write_text(REMOTE, encoding="utf-8", newline="\n")
    subprocess.check_call(
        ["scp", "-o", "BatchMode=yes", str(helper), f"root@{HOST}:/tmp/_x9_remote_pack_snap.py"]
    )
    raw = subprocess.check_output(
        [
            "ssh",
            "-o",
            "BatchMode=yes",
            f"root@{HOST}",
            "sed -i 's/\\r$//' /tmp/_x9_remote_pack_snap.py; "
            "/opt/llm2-structure-eth-multitrade-p75-v1/venv/bin/python /tmp/_x9_remote_pack_snap.py",
        ],
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    line = [ln for ln in raw.splitlines() if ln.strip().startswith("{")][-1]
    payload = json.loads(line)
    payload["note"] = (
        "Snap vs pack indicators: should be near-exact if decide used pack tip after structure refresh."
    )
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print("pack_1h_n", payload.get("pack_1h_n"))
    for b in payload.get("bars") or []:
        print(
            b.get("ts_ms"),
            "id",
            b.get("identical"),
            "mis",
            b.get("n_mismatch"),
            "pred",
            b.get("pred_mean"),
            "top",
            [t["col"] for t in (b.get("top") or [])[:5]],
        )
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
