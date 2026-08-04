"""Hard leakage + confirmation-time recheck for structure_v1 on expansion symbols."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

import pandas as pd

from llm2.data.indicators import SWING_RIGHT, indicators_db_path, load_bar_features, timeframe_ms
from llm2.data.loader import load_ohlcv
from llm2.features.guard import run_audit_for_space
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START
from llm2.registry.ledger import append_ledger

SYMBOLS = (
    "BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "VETUSDT",
    "ADAUSDT", "DOGEUSDT", "AVAXUSDT", "LINKUSDT", "DOTUSDT", "TRXUSDT", "XLMUSDT",
)
TIMEFRAMES = ("1h", "4h")


def _swings(symbol: str, timeframe: str, source: str = "binance") -> pd.DataFrame:
    import sqlite3

    db = indicators_db_path()
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        return pd.read_sql(
            "SELECT kind, pivot_i, confirm_i, pivot_ts_ms, confirm_ts_ms, price FROM swings "
            "WHERE symbol=? AND timeframe=? AND source=? ORDER BY swing_id",
            conn,
            params=(symbol, timeframe, source),
        )
    finally:
        conn.close()


def confirmation_audit(symbol: str, timeframe: str) -> dict:
    sw = _swings(symbol, timeframe)
    if len(sw) < 50:
        return {"symbol": symbol, "timeframe": timeframe, "ok": False, "error": f"insufficient swings n={len(sw)}"}
    lag_ok = bool((sw["confirm_i"] - sw["pivot_i"] == SWING_RIGHT).all())
    step = timeframe_ms(timeframe)
    ts_ok = bool((sw["confirm_ts_ms"] - sw["pivot_ts_ms"] == SWING_RIGHT * step).all())
    bf = load_bar_features(symbol, timeframe)
    early_cites = {}
    unknown_pivots = {}
    for kind, ts_col in (("high", "last_sh_ts_ms"), ("low", "last_sl_ts_ms")):
        if ts_col not in bf.columns:
            early_cites[kind] = -1
            unknown_pivots[kind] = -1
            continue
        confirm_of_pivot = sw[sw.kind == kind].set_index("pivot_ts_ms")["confirm_ts_ms"]
        cited = bf.dropna(subset=[ts_col])
        confirm = cited[ts_col].astype("int64").map(confirm_of_pivot)
        unknown_pivots[kind] = int(confirm.isna().sum())
        early_cites[kind] = int((confirm > cited["ts_ms"]).sum()) if confirm.notna().any() else 0
    ok = lag_ok and ts_ok and all(v == 0 for v in early_cites.values()) and all(v == 0 for v in unknown_pivots.values())
    return {
        "symbol": symbol, "timeframe": timeframe, "ok": ok, "n_swings": int(len(sw)),
        "confirm_lag_bars_ok": lag_ok, "confirm_lag_ts_ok": ts_ok,
        "early_cites": early_cites, "unknown_pivots": unknown_pivots,
    }


def leakage_audit(symbol: str, timeframe: str) -> dict:
    ohlcv = load_ohlcv(symbol, timeframe)
    ohlcv = ohlcv.loc[ohlcv.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")].copy()
    audit = run_audit_for_space(ohlcv.tail(8000), interval=timeframe, space="structure_v1", symbol=symbol, cuts=3)
    return {
        "symbol": symbol, "timeframe": timeframe, "ok": bool(audit.get("passed")),
        "price_type": ohlcv.attrs.get("price_type"), "n_bars": int(len(ohlcv)),
        "leakage_potential": audit.get("leakage_potential"),
        "report_text": (audit.get("report_text") or "")[:2000],
    }


def main() -> int:
    from leakage.ensure_source import prefer_botsgeneral_leakage
    import leakage

    prefer_botsgeneral_leakage()
    if "botsgeneral" not in str(getattr(leakage, "__file__", "")):
        print(f"REFUSE: leakage not botsgeneral ({leakage.__file__})")
        return 3

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rows = []
    hard_fail = False
    for sym in SYMBOLS:
        for tf in TIMEFRAMES:
            print(f"AUDIT {sym} {tf} ...", flush=True)
            try:
                conf = confirmation_audit(sym, tf)
            except Exception as exc:
                conf = {"symbol": sym, "timeframe": tf, "ok": False, "error": str(exc)}
            try:
                leak = leakage_audit(sym, tf)
            except Exception as exc:
                leak = {"symbol": sym, "timeframe": tf, "ok": False, "error": str(exc)}
            ok = bool(conf.get("ok")) and bool(leak.get("ok"))
            hard_fail = hard_fail or (not ok)
            rows.append({"confirmation": conf, "leakage": leak, "ok": ok})
            print(f"  conf={conf.get('ok')} leak={leak.get('ok')} early={conf.get('early_cites')} err={conf.get('error') or leak.get('error')}", flush=True)

    payload = {
        "stamped_utc": stamp, "space": "structure_v1", "leakage_engine": str(leakage.__file__),
        "readiness": "RESEARCH_ONLY", "overall_ok": not hard_fail,
        "n_cases": len(rows), "n_pass": sum(1 for r in rows if r["ok"]), "n_fail": sum(1 for r in rows if not r["ok"]),
        "cases": rows,
        "note": "Warehouse confirmation-time + botsgeneral leakage. Do not train on FAIL cases.",
    }
    out = ARTIFACTS / "reports" / f"structure_v1_leakage_recheck_{stamp}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    append_ledger(f"STRUCTURE_LEAKAGE_RECHECK overall_ok={not hard_fail} pass={payload['n_pass']}/{payload['n_cases']} path={out.name}", tier=0)
    print(f"wrote {out} overall_ok={not hard_fail}", flush=True)
    return 0 if not hard_fail else 2


if __name__ == "__main__":
    raise SystemExit(main())
