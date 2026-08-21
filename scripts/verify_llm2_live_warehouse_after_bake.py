"""Tip + tip50 parity: VPS shared closed vs research market_ohlcv (+ optional indicators)."""
from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"d:\projects\LLM2\artifacts\reports")
WH = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
IND = Path(r"D:\projectsdata\indicators\indicators.sqlite")
TF_MS = {"1h": 3_600_000, "4h": 14_400_000, "1w": 604_800_000}


def _resolve_pt(con: sqlite3.Connection, symbol: str, timeframe: str) -> str:
    rows = con.execute(
        "SELECT price_type, COUNT(*) AS n FROM market_ohlcv "
        "WHERE symbol=? AND timeframe=? AND source='binance' "
        "AND (is_complete=1 OR is_complete IS NULL) GROUP BY price_type ORDER BY n DESC",
        (symbol, timeframe),
    ).fetchall()
    avail = {str(r[0]): int(r[1]) for r in rows}
    syn = [(p, avail[p]) for p in ("last_price", "last") if avail.get(p, 0) > 0]
    if not syn:
        raise RuntimeError(f"no last series for {symbol} {timeframe}")
    return max(syn, key=lambda x: x[1])[0]


def warehouse_closed(symbol: str, timeframe: str, *, tip_n: int = 50) -> dict:
    now = int(time.time() * 1000)
    step = TF_MS[timeframe]
    con = sqlite3.connect(f"file:{WH}?mode=ro", uri=True)
    try:
        pt = _resolve_pt(con, symbol, timeframe)
        rows = con.execute(
            "SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv "
            "WHERE symbol=? AND timeframe=? AND source='binance' AND price_type=? "
            "AND (is_complete=1 OR is_complete IS NULL) ORDER BY ts_ms",
            (symbol, timeframe, pt),
        ).fetchall()
    finally:
        con.close()
    closed = [r for r in rows if int(r[0]) + step <= now]
    if not closed:
        return {"error": "no_closed", "price_type": pt}
    tip = closed[-1]
    tip50 = closed[-tip_n:]
    blob = "".join(f"{r[0]}|{r[1]}|{r[2]}|{r[3]}|{r[4]}\n" for r in tip50).encode()
    return {
        "price_type": pt,
        "n_closed": len(closed),
        "tip_ts_ms": int(tip[0]),
        "tip_utc": datetime.fromtimestamp(tip[0] / 1000, tz=timezone.utc).isoformat(),
        "tip_ohlc": [float(tip[1]), float(tip[2]), float(tip[3]), float(tip[4])],
        "tip_volume": float(tip[5]),
        "tip50_ohlc_sha256": hashlib.sha256(blob).hexdigest(),
    }


def research_indicator_tip(symbol: str, timeframe: str = "1h") -> dict | None:
    if not IND.is_file():
        return None
    con = sqlite3.connect(f"file:{IND}?mode=ro", uri=True)
    try:
        cols = [r[1] for r in con.execute("PRAGMA table_info(bar_features)").fetchall()]
        prefer = [c for c in ("ts_ms", "bos", "choch", "last_retrace", "atr", "close") if c in cols]
        if "ts_ms" not in prefer:
            prefer = ["ts_ms"]
        row = con.execute(
            "SELECT COUNT(*), MAX(ts_ms) FROM bar_features "
            "WHERE symbol=? AND timeframe=? AND source='binance'",
            (symbol, timeframe),
        ).fetchone()
        if not row or not row[1]:
            return {"n": 0}
        tip = con.execute(
            f"SELECT {', '.join(prefer)} FROM bar_features "
            "WHERE symbol=? AND timeframe=? AND source='binance' AND ts_ms=?",
            (symbol, timeframe, row[1]),
        ).fetchone()
        return {"n": int(row[0]), "max_ts": int(row[1]), "tip": dict(zip(prefer, tip)) if tip else None}
    finally:
        con.close()


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> int:
    t1 = _load_json(ROOT / "shared_tip_ln1.json")
    t3 = _load_json(ROOT / "shared_tip_ln3.json")
    u1 = _load_json(ROOT / "units_ln1.json")
    u3 = _load_json(ROOT / "units_ln3.json")

    out: dict = {
        "evidence_class": "LLM2_LIVE_VS_WAREHOUSE_AFTER_BAKE",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "series": {},
        "units": {},
    }
    blockers: list[str] = []

    for key, meta in t3["series"].items():
        sym, tf = key.split(":")
        wh = warehouse_closed(sym, tf)
        ln1 = t1["series"].get(key, {})
        row = {
            "ln3": {
                "tip_ohlc": meta.get("tip_ohlc"),
                "tip_ts_ms": meta.get("tip_ts_ms"),
                "tip50": meta.get("tip50_ohlc_sha256"),
                "n_closed": meta.get("n_closed"),
            },
            "ln1": {
                "tip_ohlc": ln1.get("tip_ohlc"),
                "tip_ts_ms": ln1.get("tip_ts_ms"),
                "tip50": ln1.get("tip50_ohlc_sha256"),
            },
            "warehouse": wh,
            "ln1_eq_ln3": ln1.get("tip_ohlc") == meta.get("tip_ohlc")
            and ln1.get("tip50_ohlc_sha256") == meta.get("tip50_ohlc_sha256"),
            "ln3_eq_warehouse_ohlc": (
                not wh.get("error")
                and meta.get("tip_ohlc") == wh.get("tip_ohlc")
                and meta.get("tip_ts_ms") == wh.get("tip_ts_ms")
            ),
            "ln3_eq_warehouse_tip50": (
                not wh.get("error")
                and meta.get("tip50_ohlc_sha256") == wh.get("tip50_ohlc_sha256")
            ),
        }
        if tf == "1h":
            row["research_indicators"] = research_indicator_tip(sym, "1h")
        out["series"][key] = row
        if not row["ln1_eq_ln3"]:
            blockers.append(f"LN1_LN3:{key}")
        if not row["ln3_eq_warehouse_ohlc"]:
            blockers.append(f"TIP_OHLC:{key}")
        if not row["ln3_eq_warehouse_tip50"]:
            blockers.append(f"TIP50:{key}")

    for host, urep in (("ln1", u1), ("ln3", u3)):
        rows = []
        for unit in urep["units"]:
            bfs = unit.get("bar_features_binance") or []
            depth_ok = all(x.get("depth_ok_1h", True) for x in bfs)
            bad = int(unit.get("recent_bad_log_n") or 0)
            # tip ts vs shared closed tip for matching symbol 1h
            tip_align = []
            for bf in bfs:
                if bf.get("tf") != "1h":
                    continue
                sk = f"{bf['symbol']}:1h"
                shared_ts = t3["series"].get(sk, {}).get("tip_ts_ms")
                pack_ts = bf.get("max_ts")
                tip_align.append(
                    {
                        "symbol": bf["symbol"],
                        "pack_max_ts": pack_ts,
                        "shared_closed_tip_ts": shared_ts,
                        "pack_at_or_before_shared": (
                            pack_ts is not None
                            and shared_ts is not None
                            and int(pack_ts) <= int(shared_ts)
                        ),
                        "n": bf.get("n"),
                    }
                )
            ok = (
                unit.get("active") == "active"
                and depth_ok
                and bad == 0
                and all(x["pack_at_or_before_shared"] for x in tip_align)
            )
            rows.append(
                {
                    "unit": unit["unit"],
                    "active": unit.get("active"),
                    "source": unit.get("source"),
                    "depth_ok": depth_ok,
                    "recent_bad_log_n": bad,
                    "tip_align": tip_align,
                    "ok": ok,
                }
            )
            if not ok:
                blockers.append(f"BOT:{unit['unit']}")
        out["units"][host] = rows

    out["principal_blocker"] = blockers[0] if blockers else None
    out["blockers"] = blockers
    out["all_ok"] = not blockers
    # Note on indicators identity
    out["notes"] = [
        "Candle identity gate: closed-bar OHLC tip + tip50 hash vs market_ohlcv.",
        "Live packs still compute/store structure in indicators_live_slice; "
        "exact feature identity also needs same compute_structure code + full history left edge.",
        "Pack bar_features tip may lag shared closed tip by 0–1 bars until next decide refresh.",
    ]
    path = ROOT / "llm2_live_warehouse_parity_after_bake.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "all_ok": out["all_ok"],
        "principal_blocker": out["principal_blocker"],
        "blockers": blockers,
        "series_summary": {
            k: {
                "ln1_eq_ln3": v["ln1_eq_ln3"],
                "tip_ohlc": v["ln3_eq_warehouse_ohlc"],
                "tip50": v["ln3_eq_warehouse_tip50"],
                "wh_tip": v["warehouse"].get("tip_ohlc"),
                "ln3_tip": v["ln3"]["tip_ohlc"],
            }
            for k, v in out["series"].items()
        },
        "bots_ok": {
            host: all(u["ok"] for u in rows) for host, rows in out["units"].items()
        },
    }, indent=2))
    return 0 if out["all_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
