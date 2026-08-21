"""Refresh ETH candles tip, build 15m structure warehouse, run leakage audit."""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
_IND_SRC = Path(r"C:\projects\botsgeneral\packages\indicators\src")
_LEAK_SRC = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _IND_SRC.is_dir() and str(_IND_SRC) not in sys.path:
    sys.path.insert(0, str(_IND_SRC))
if _LEAK_SRC.is_dir() and str(_LEAK_SRC) not in sys.path:
    sys.path.insert(0, str(_LEAK_SRC))

from indicators.ensure_source import prefer_botsgeneral_indicators

prefer_botsgeneral_indicators()

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

import leakage

if "botsgeneral" not in str(leakage.__file__).lower():
    raise SystemExit(f"leakage not botsgeneral: {leakage.__file__}")

from indicators import update_series  # noqa: E402
from indicators.candles import refresh_candles  # noqa: E402

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.guard import run_audit_for_space  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402

SYMBOL = "ETHUSDT"
OUT = ARTIFACTS / "reports" / "structure_v1_eth_15m_warehouse_audit_latest.json"


def _try_refresh() -> dict:
    """Best-effort tip refresh for ETH 1m/15m/1h/4h."""
    info: dict = {"refresh": []}
    t0 = time.perf_counter()
    try:
        n = refresh_candles(
            symbols=[SYMBOL],
            timeframes=["1m", "15m", "1h", "4h"],
            price_types=("last",),
        )
        info["refresh"].append(
            {"ok": True, "n": n, "sec": round(time.perf_counter() - t0, 1)}
        )
    except Exception as e:  # noqa: BLE001
        info["refresh"].append(
            {
                "ok": False,
                "error": f"{type(e).__name__}:{e}",
                "sec": round(time.perf_counter() - t0, 1),
            }
        )
    return info


def main() -> int:
    t0 = time.perf_counter()
    report: dict = {
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "symbol": SYMBOL,
        "indicators_file": str(__import__("indicators").__file__),
        "leakage_file": str(leakage.__file__),
    }
    report.update(_try_refresh())

    print("[1/3] update_series ETHUSDT 15m …", flush=True)
    t1 = time.perf_counter()
    res15 = update_series(SYMBOL, "15m", source="binance")
    print(
        f"  15m n_bars={res15.n_bars} n_swings={res15.n_swings} "
        f"err={res15.error!r} sec={time.perf_counter()-t1:.1f}",
        flush=True,
    )
    report["update_15m"] = {
        "n_bars": res15.n_bars,
        "n_swings": res15.n_swings,
        "counts": res15.counts,
        "error": res15.error,
        "sec": round(time.perf_counter() - t1, 1),
    }
    if res15.error or res15.n_bars < 1000:
        raise SystemExit(f"15m structure build failed: {res15}")

    # Tip-refresh HTF used by structure_v1 join
    for tf in ("1h", "4h"):
        print(f"[1b] update_series ETHUSDT {tf} tip …", flush=True)
        r = update_series(SYMBOL, tf, source="binance")
        report[f"update_{tf}"] = {
            "n_bars": r.n_bars,
            "n_swings": r.n_swings,
            "error": r.error,
        }
        print(f"  {tf} n_bars={r.n_bars} err={r.error!r}", flush=True)

    print("[2/3] load OHLCV 15m for leakage …", flush=True)
    ohlcv = load_ohlcv(SYMBOL, "15m")
    # Audit on a recent dense slice for speed; still prefix-invariance on structure_v1 path
    if len(ohlcv) > 8000:
        ohlcv_audit = ohlcv.iloc[-8000:].copy()
    else:
        ohlcv_audit = ohlcv
    print(f"  ohlcv n={len(ohlcv)} audit_n={len(ohlcv_audit)}", flush=True)

    print("[3/3] leakage audit structure_v1 @ 15m …", flush=True)
    audit = run_audit_for_space(
        ohlcv_audit,
        interval="15m",
        space="structure_v1",
        symbol=SYMBOL,
        cuts=3,
    )
    report["leakage"] = {
        "passed": audit.get("passed"),
        "ok": audit.get("ok"),
        "leakage_potential": audit.get("leakage_potential"),
        "report_text": audit.get("report_text"),
        "audit_bars": len(ohlcv_audit),
    }
    print(audit.get("report_text") or "", flush=True)
    if not audit.get("passed"):
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
        raise SystemExit("LEAKAGE FAIL — refuse train")

    report["elapsed_sec"] = round(time.perf_counter() - t0, 1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"OK wrote {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
