"""Inspect TSM-VPA state DB tables and recent decision/order rows."""
from __future__ import annotations

import sqlite3
from pathlib import Path

base = Path("/opt/tsm-vpa/data/live")
for p in sorted(base.glob("*.sqlite")):
    con = sqlite3.connect(p)
    tables = [
        r[0]
        for r in con.execute(
            "select name from sqlite_master where type='table'"
        ).fetchall()
    ]
    print("FILE", p.name, "tables=", tables)
    for t in tables:
        cols = [c[1] for c in con.execute(f"pragma table_info({t})").fetchall()]
        n = con.execute(f"select count(*) from {t}").fetchone()[0]
        print(f"  {t}: n={n} cols={cols[:30]}")
        if n == 0:
            continue
        try:
            rows = con.execute(f"select * from {t} order by rowid desc limit 3").fetchall()
            for row in rows:
                print("   ", row[:20])
        except Exception as exc:  # noqa: BLE001
            print("   err", exc)
