"""Compare live pack tip bar_features vs local research warehouse for soft mismatch audit."""
from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from llm2.paths import MARKET_DB  # noqa: E402 — ensure project path loads

HOST = "185.203.119.52"
UNIT = "llm2-structure-eth-15m-multitrade-wall-clock-p75-v1"
REMOTE_PACK = f"/opt/{UNIT}/pack/indicators_live_slice.sqlite"
LOCAL_IND = Path(r"D:\projectsdata\indicators\indicators.sqlite")


def main() -> int:
    bar_ts = int(sys.argv[1]) if len(sys.argv) > 1 else 1785945600000  # 16:00
    remote = r"""
import json, sqlite3, sys
ts = int(sys.argv[1])
con = sqlite3.connect(sys.argv[2])
cols = [r[1] for r in con.execute("PRAGMA table_info(bar_features)").fetchall()]
row = con.execute(
    f"SELECT {','.join(cols)} FROM bar_features "
    "WHERE symbol='ETHUSDT' AND timeframe='15m' AND source='binance' AND ts_ms=?",
    (ts,),
).fetchone()
print(json.dumps({"cols": cols, "row": list(row) if row else None}))
"""
    helper = Path(__import__("tempfile").gettempdir()) / "_pack_tip_row.py"
    helper.write_text(remote, encoding="utf-8", newline="\n")
    subprocess.check_call(["scp", "-o", "BatchMode=yes", str(helper), f"root@{HOST}:/tmp/_pack_tip_row.py"])
    raw = subprocess.check_output(
        [
            "ssh",
            "-o",
            "BatchMode=yes",
            f"root@{HOST}",
            f"sed -i 's/\\r$//' /tmp/_pack_tip_row.py; python3 /tmp/_pack_tip_row.py {bar_ts} {REMOTE_PACK}",
        ],
        text=True,
        encoding="utf-8",
    )
    lines = [ln for ln in raw.splitlines() if ln.strip().startswith("{")]
    pack = json.loads(lines[-1])
    if not pack.get("row"):
        print("PACK_ROW_MISSING", bar_ts)
        return 2
    pcols, prow = pack["cols"], pack["row"]
    pmap = dict(zip(pcols, prow))

    con = sqlite3.connect(f"file:{LOCAL_IND}?mode=ro", uri=True)
    cols = [r[1] for r in con.execute("PRAGMA table_info(bar_features)").fetchall()]
    use = [c for c in cols if c in pmap]
    row = con.execute(
        f"SELECT {','.join(use)} FROM bar_features "
        "WHERE symbol='ETHUSDT' AND timeframe='15m' AND source='binance' AND ts_ms=?",
        (bar_ts,),
    ).fetchone()
    con.close()
    if not row:
        print("RESEARCH_ROW_MISSING", bar_ts, "local", LOCAL_IND)
        return 3
    rmap = dict(zip(use, row))

    mism = []
    for c in use:
        a, b = pmap.get(c), rmap.get(c)
        if a is None and b is None:
            continue
        try:
            fa, fb = float(a), float(b)
            if abs(fa - fb) > 1e-9:
                mism.append((c, fa, fb, abs(fa - fb)))
        except (TypeError, ValueError):
            if a != b:
                mism.append((c, a, b, None))
    mism.sort(key=lambda x: (x[3] is None, -(x[3] or 0)))
    print("bar_ts_ms", bar_ts)
    print("n_common", len(use), "n_mismatch", len(mism))
    vol = [m for m in mism if "_vol" in m[0] or "vol" in m[0].lower()]
    htf = [m for m in mism if m[0].endswith("_1h") or m[0].endswith("_4h")]
    native = [m for m in mism if m not in vol and m not in htf]
    print("vol_mismatches", len(vol), "htf", len(htf), "native", len(native))
    for label, group in (("NATIVE", native[:15]), ("VOL", vol[:15]), ("HTF", htf[:15])):
        print(f"--- {label} ---")
        for c, a, b, d in group:
            print(f"  {c}: pack={a} research={b} abs={d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
