"""Hourly research tip bake for structure symbols (BTC/ETH/SOL).

Pulls tip Open-High-Low-Close-Volume into market_ohlcv.sqlite, then extends
botsgeneral indicators bar_features for 1h/4h/1w so warehouse parity does not
lag the live shared candle store by a closed bar.

Usage:
  python scripts/bake_research_ohlcv_tip.py
  python scripts/bake_research_ohlcv_tip.py --symbols BTCUSDT,ETHUSDT,SOLUSDT
  python scripts/bake_research_ohlcv_tip.py --skip-candles   # indicators only

Windows Task Scheduler / cron (suggested):
  every hour at :03 after the bar close — local research machine only.
  Does not touch VPS live services.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from llm2.paths import ARTIFACTS  # noqa: E402

OUT = ARTIFACTS / "reports" / "research_ohlcv_tip_bake_latest.json"
DEFAULT_SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TFS = ("1h", "4h", "1w")
IND_SRC = r"C:\projects\botsgeneral\packages\indicators\src"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--symbols", default=",".join(DEFAULT_SYMBOLS))
    ap.add_argument("--skip-candles", action="store_true")
    ap.add_argument("--source", default="binance")
    args = ap.parse_args(argv)

    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    report: dict = {
        "evidence_class": "RESEARCH_OHLCV_TIP_BAKE",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "symbols": symbols,
        "timeframes": list(TFS),
        "steps": [],
    }

    sys.path.insert(0, IND_SRC)
    if not args.skip_candles:
        try:
            from indicators.candles import refresh_candles

            # Full refresh is safe: incremental skip is implemented inside.
            print(f"refresh_candles symbols={symbols} tfs={list(TFS)}", flush=True)
            refresh_candles(symbols=symbols, timeframes=list(TFS))
            report["steps"].append({"step": "refresh_candles", "ok": True})
        except Exception as exc:  # noqa: BLE001
            report["steps"].append(
                {"step": "refresh_candles", "ok": False, "error": f"{type(exc).__name__}: {exc}"}
            )
            print(f"refresh_candles failed: {exc}", flush=True)

    try:
        from indicators.update import update_series
    except Exception as exc:  # noqa: BLE001
        report["error"] = f"indicators import failed: {exc}"
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(report["error"], flush=True)
        return 2

    for sym in symbols:
        for tf in TFS:
            try:
                r = update_series(sym, tf, source=str(args.source))
                row = {
                    "step": "update_series",
                    "symbol": sym,
                    "timeframe": tf,
                    "n_bars": r.n_bars,
                    "error": r.error or None,
                    "ok": not bool(r.error),
                }
            except Exception as exc:  # noqa: BLE001
                row = {
                    "step": "update_series",
                    "symbol": sym,
                    "timeframe": tf,
                    "ok": False,
                    "error": f"{type(exc).__name__}: {exc}",
                }
            report["steps"].append(row)
            print(
                f"{sym} {tf}: n={row.get('n_bars')} err={row.get('error')}",
                flush=True,
            )

    fails = sum(1 for s in report["steps"] if not s.get("ok", True))
    report["n_fail"] = fails
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print(f"wrote {OUT} (fails={fails})", flush=True)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
