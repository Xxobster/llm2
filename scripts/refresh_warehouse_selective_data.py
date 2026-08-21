"""Incremental warehouse refresh before Phase B feature trains.

Refreshes funding and attempt research_candles download for crypto OHLCV.
Never overwrites evidence DBs. Logs what was refreshed / skipped.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.paths import ARTIFACTS, MARKET_DB, MARKET_OI_DB, PROJECTSDATA  # noqa: E402

FUNDING_DB = PROJECTSDATA / "candles" / "binance_funding.sqlite"
REPORT = ARTIFACTS / "reports" / "warehouse_refresh_selective_data_latest.json"


def _try_cmd(args: list[str], timeout: int = 600) -> dict:
    t0 = time.perf_counter()
    try:
        r = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(_ROOT),
        )
        return {
            "cmd": args,
            "returncode": r.returncode,
            "stdout_tail": (r.stdout or "")[-2000:],
            "stderr_tail": (r.stderr or "")[-2000:],
            "elapsed_sec": round(time.perf_counter() - t0, 1),
        }
    except FileNotFoundError as exc:
        return {"cmd": args, "error": f"FileNotFoundError: {exc}"}
    except subprocess.TimeoutExpired:
        return {"cmd": args, "error": "timeout", "timeout_sec": timeout}


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log: dict = {
        "created_utc": stamp,
        "purpose": "warehouse_refresh_before_selective_data_phase_b",
        "paths": {
            "market_ohlcv": str(MARKET_DB),
            "funding": str(FUNDING_DB),
            "market_oi": str(MARKET_OI_DB),
        },
        "pre_sizes_bytes": {
            "market_ohlcv": MARKET_DB.stat().st_size if MARKET_DB.is_file() else None,
            "funding": FUNDING_DB.stat().st_size if FUNDING_DB.is_file() else None,
            "market_oi": MARKET_OI_DB.stat().st_size if MARKET_OI_DB.is_file() else None,
        },
        "steps": [],
    }

    # Ensure C:\projects\botsgeneral is importable (not always on site-packages).
    botsgeneral_root = Path(r"C:\projects\botsgeneral")
    env = dict(**{k: v for k, v in __import__("os").environ.items()})
    prior = env.get("PYTHONPATH", "")
    extra = str(botsgeneral_root)
    env["PYTHONPATH"] = extra + (f";{prior}" if prior else "")

    for only in (["BTCUSDT", "ETHUSDT", "SOLUSDT"], ["funding"]):
        cmd = [
            sys.executable,
            "-m",
            "botsgeneral.research_candles.download_all",
            "--only",
            *only,
        ]
        print("RUN", " ".join(cmd), flush=True)
        t0 = time.perf_counter()
        try:
            r = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=900,
                cwd=str(botsgeneral_root),
                env=env,
            )
            res = {
                "cmd": cmd,
                "returncode": r.returncode,
                "stdout_tail": (r.stdout or "")[-2000:],
                "stderr_tail": (r.stderr or "")[-2000:],
                "elapsed_sec": round(time.perf_counter() - t0, 1),
            }
        except Exception as exc:  # noqa: BLE001
            res = {"cmd": cmd, "error": f"{type(exc).__name__}: {exc}"}
        log["steps"].append(res)
        if res.get("returncode") not in (0, None) or res.get("error"):
            print(f"  soft-fail: {res.get('error') or res.get('returncode')}", flush=True)

    log["post_sizes_bytes"] = {
        "market_ohlcv": MARKET_DB.stat().st_size if MARKET_DB.is_file() else None,
        "funding": FUNDING_DB.stat().st_size if FUNDING_DB.is_file() else None,
        "market_oi": MARKET_OI_DB.stat().st_size if MARKET_OI_DB.is_file() else None,
    }
    try:
        import sqlite3

        if FUNDING_DB.is_file():
            c = sqlite3.connect(f"file:{FUNDING_DB}?mode=ro", uri=True)
            mx = c.execute(
                "SELECT MAX(funding_time_ms) FROM funding_rate WHERE symbol='ETHUSDT'"
            ).fetchone()[0]
            c.close()
            log["funding_eth_max_ts_ms"] = mx
            if mx:
                log["funding_eth_max_utc"] = datetime.fromtimestamp(
                    mx / 1000.0, tz=timezone.utc
                ).isoformat()
    except Exception as exc:  # noqa: BLE001
        log["funding_probe_error"] = str(exc)

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(log, indent=2, default=str), encoding="utf-8")
    print(json.dumps({"wrote": str(REPORT), "n_steps": len(log["steps"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
