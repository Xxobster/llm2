"""Print open BTCUSDT positions + TP/SL for Xxobster7 (run on ln1)."""
from __future__ import annotations

import hashlib
import hmac
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path


def _load() -> tuple[str, str]:
    env: dict[str, str] = {}
    for line in Path("/root/.trading/secrets.env").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env["Xxobster7_API_KEY"], env["Xxobster7_API_SECRET"]


def signed_get(path: str, params: dict, key: str, secret: str) -> dict:
    q = urllib.parse.urlencode(params)
    ts = str(int(time.time() * 1000))
    recv = "60000"
    sign = hmac.new(
        secret.encode(), f"{ts}{key}{recv}{q}".encode(), hashlib.sha256
    ).hexdigest()
    req = urllib.request.Request(
        f"https://api.bybit.com{path}?{q}",
        headers={
            "X-BAPI-API-KEY": key,
            "X-BAPI-TIMESTAMP": ts,
            "X-BAPI-RECV-WINDOW": recv,
            "X-BAPI-SIGN": sign,
        },
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())


def main() -> None:
    key, secret = _load()
    pos = signed_get(
        "/v5/position/list",
        {"category": "linear", "symbol": "BTCUSDT"},
        key,
        secret,
    )
    out = []
    for p in (pos.get("result") or {}).get("list") or []:
        if float(p.get("size") or 0) == 0:
            continue
        out.append(
            {
                k: p.get(k)
                for k in (
                    "symbol",
                    "side",
                    "size",
                    "avgPrice",
                    "takeProfit",
                    "stopLoss",
                    "tpTriggerBy",
                    "slTriggerBy",
                    "positionIdx",
                    "leverage",
                    "unrealisedPnl",
                    "liqPrice",
                )
            }
        )
    print(
        json.dumps(
            {"retCode": pos.get("retCode"), "retMsg": pos.get("retMsg"), "open": out},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
