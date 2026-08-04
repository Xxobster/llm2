"""Export a slim indicators SQLite for VPS micro-live (BTCUSDT structure only)."""

from __future__ import annotations

import sqlite3
from pathlib import Path

SRC = Path(r"D:\projectsdata\indicators\indicators.sqlite")
DST = Path(r"D:\projects\LLM2\artifacts\live_packs\structure_v1_lgbm\indicators_live_slice.sqlite")
SYMBOLS = ("BTCUSDT",)
TIMEFRAMES = ("1h", "4h", "1w")


def main() -> int:
    DST.parent.mkdir(parents=True, exist_ok=True)
    if DST.exists():
        DST.unlink()
    src = sqlite3.connect(SRC)
    dst = sqlite3.connect(DST)
    for row in src.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    ):
        if row[0]:
            dst.execute(row[0])
    dst.commit()

    syms = ",".join(f"'{s}'" for s in SYMBOLS)
    tfs = ",".join(f"'{t}'" for t in TIMEFRAMES)
    where = f"symbol IN ({syms}) AND timeframe IN ({tfs})"

    for table in ("series", "bar_features", "swings", "structure_events", "legs", "levels"):
        try:
            cols = [d[0] for d in src.execute(f"SELECT * FROM {table} LIMIT 0").description]
        except sqlite3.OperationalError as exc:
            print(table, "skip", exc)
            continue
        if "symbol" in cols and "timeframe" in cols:
            rows = src.execute(f"SELECT * FROM {table} WHERE {where}").fetchall()
        else:
            rows = []
        if rows:
            dst.executemany(
                f"INSERT INTO {table} ({','.join(cols)}) VALUES ({','.join('?' for _ in cols)})",
                rows,
            )
        print(table, len(rows))

    try:
        meta = src.execute("SELECT * FROM meta").fetchall()
        cols = [d[0] for d in src.execute("SELECT * FROM meta LIMIT 0").description]
        if meta:
            dst.executemany(
                f"INSERT INTO meta ({','.join(cols)}) VALUES ({','.join('?' for _ in cols)})",
                meta,
            )
    except sqlite3.OperationalError:
        pass

    dst.commit()
    src.close()
    dst.close()
    mb = DST.stat().st_size / (1024 * 1024)
    print(f"wrote {DST} ({mb:.1f} MiB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
