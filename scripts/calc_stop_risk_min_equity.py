"""Min wallet so 5% equity stop-risk is still an exchange-legal Solana lot.

Does not deploy. Floors quantity to Bybit qty_step. Never rounds up past 5%.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from tradesim.contracts import InstrumentSpec  # noqa: E402
from tradesim.sizing import minimum_executable_qty  # noqa: E402

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.diagonal_sr.bar_series import make_bar_series  # noqa: E402
from llm2.edge_lab.sim_atr import atr_brackets  # noqa: E402
from llm2.ml_lab.idea_catalog import signals_from_ohlcv  # noqa: E402
from llm2.ml_lab.live_guards import SOL_EMA_SPEC  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.sizing_policy import (  # noqa: E402
    DEFAULT_STOP_RISK_FRACTION,
    min_equity_for_stop_risk,
    size_by_stop_risk,
)
from llm2.validation.folds import index_to_ms  # noqa: E402

OUT = ARTIFACTS / "reports" / "sizing"
BYBIT_TICKER = "https://api.bybit.com/v5/market/tickers?category=linear&symbol=SOLUSDT"
BYBIT_INST = (
    "https://api.bybit.com/v5/market/instruments-info?category=linear&symbol=SOLUSDT"
)
RISK_FRAC = DEFAULT_STOP_RISK_FRACTION
EMA_LEV = 13.0
AUTO013_LEV = 29.0
AUTO013_SL = 0.01
EXAMPLE_EQUITIES = (50.0, 100.0, 200.0, 500.0, 1000.0, 2000.0)


def _http_json(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": "llm2-sizing/1"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _ssh_json(host: str, url: str) -> dict[str, Any]:
    import subprocess

    proc = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=12", host, f"curl -sS --max-time 15 '{url}'"],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if proc.returncode != 0 or not (proc.stdout or "").strip():
        raise RuntimeError(f"ssh {host} curl failed rc={proc.returncode} {(proc.stderr or '')[:200]}")
    return json.loads(proc.stdout)


def _load_json(url: str) -> dict[str, Any]:
    try:
        return _http_json(url)
    except Exception:
        return _ssh_json("ln1", url)


def fetch_bybit_sol() -> dict[str, Any]:
    tick = _load_json(BYBIT_TICKER)
    inst = _load_json(BYBIT_INST)
    trow = (tick.get("result") or {}).get("list") or []
    irow = (inst.get("result") or {}).get("list") or []
    if not trow or not irow:
        raise RuntimeError("empty Bybit SOLUSDT public response")
    t = trow[0]
    i = irow[0]
    lot = i.get("lotSizeFilter") or {}
    return {
        "last": float(t["lastPrice"]),
        "mark": float(t["markPrice"]),
        "qty_step": float(lot.get("qtyStep") or 0.1),
        "min_qty": float(lot.get("minOrderQty") or 0.1),
        "max_qty": float(lot.get("maxOrderQty") or 96000.0),
        "min_notional": float(lot.get("minNotionalValue") or 5.0),
        "tick_size": float((i.get("priceFilter") or {}).get("tickSize") or 0.01),
        "max_leverage": float((i.get("leverageFilter") or {}).get("maxLeverage") or 100.0),
    }


def instrument_from_bybit(row: dict[str, Any]) -> InstrumentSpec:
    return InstrumentSpec(
        symbol="SOLUSDT",
        tick_size=float(row["tick_size"]),
        qty_step=float(row["qty_step"]),
        min_qty=float(row["min_qty"]),
        min_notional=float(row["min_notional"]),
        max_qty=float(row["max_qty"]),
        max_leverage=float(row["max_leverage"]),
    )


def _lock_ms() -> int:
    import pandas as pd

    return int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)


def ema_signal_sl_stats() -> dict[str, Any]:
    ohlcv = load_ohlcv("SOLUSDT", "1h")
    ts = index_to_ms(ohlcv.index)
    sc_all = make_bar_series("SOLUSDT", "1h", ohlcv)
    sig_all = signals_from_ohlcv(ohlcv, "1h")
    fire = sig_all["power_ema_stack_long"] != 0
    sl_all, _tp = atr_brackets(
        sc_all.atr_frac,
        k_sl=float(SOL_EMA_SPEC["k_sl"]),
        tp_ratio=float(SOL_EMA_SPEC["tp_ratio"]),
        sl_cap=float(SOL_EMA_SPEC["sl_cap"]),
    )
    pre = ts < _lock_ms()
    mask = fire & pre
    sl_sig = sl_all[mask]
    sl_sig = sl_sig[np.isfinite(sl_sig)]
    last_i = int(np.max(np.flatnonzero(np.isfinite(sc_all.atr_frac))))
    sl_now = float(sl_all[last_i])
    atr_now = float(sc_all.atr_frac[last_i])
    tip_ms = int(ts[last_i])
    return {
        "n_signal_bars_pre_lockbox": int(sl_sig.size),
        "sl_mean": float(np.mean(sl_sig)) if sl_sig.size else float("nan"),
        "sl_median": float(np.median(sl_sig)) if sl_sig.size else float("nan"),
        "sl_p10": float(np.quantile(sl_sig, 0.10)) if sl_sig.size else float("nan"),
        "sl_p90": float(np.quantile(sl_sig, 0.90)) if sl_sig.size else float("nan"),
        "sl_min": float(np.min(sl_sig)) if sl_sig.size else float("nan"),
        "sl_max": float(np.max(sl_sig)) if sl_sig.size else float("nan"),
        "frac_at_floor": float(np.mean(sl_sig <= 0.004 + 1e-12)) if sl_sig.size else float("nan"),
        "frac_at_cap": float(np.mean(sl_sig >= 0.030 - 1e-12)) if sl_sig.size else float("nan"),
        "sl_now_last_closed_1h": sl_now,
        "atr_frac_now": atr_now,
        "last_closed_1h_open_ms": tip_ms,
        "k_sl": float(SOL_EMA_SPEC["k_sl"]),
        "sl_floor": 0.004,
        "sl_cap": float(SOL_EMA_SPEC["sl_cap"]),
    }


def _try_wallet(account: str) -> dict[str, Any]:
    try:
        from llm2.live.micro_runner import fetch_wallet_equity_usdt

        eq = float(fetch_wallet_equity_usdt(account=account))
        return {"ok": True, "equity_usdt": eq}
    except Exception as exc:
        return {"ok": False, "error": type(exc).__name__}


def _book(
    *,
    name: str,
    account: str,
    sl_pct: float,
    sl_note: str,
    price: float,
    spec: InstrumentSpec,
    leverage: float,
    wallet: dict[str, Any],
) -> dict[str, Any]:
    min_q = float(minimum_executable_qty(spec, price))
    e_min = min_equity_for_stop_risk(
        price=price, sl_pct=sl_pct, instrument=spec, risk_fraction=RISK_FRAC
    )
    min_lot_risk = min_q * price * sl_pct
    examples = []
    for eq in EXAMPLE_EQUITIES:
        sized = size_by_stop_risk(
            equity=eq,
            price=price,
            sl_pct=sl_pct,
            instrument=spec,
            risk_fraction=RISK_FRAC,
            leverage=leverage,
        )
        examples.append({"equity_usdt": eq, **sized})
    live_size = None
    if wallet.get("ok"):
        live_size = size_by_stop_risk(
            equity=float(wallet["equity_usdt"]),
            price=price,
            sl_pct=sl_pct,
            instrument=spec,
            risk_fraction=RISK_FRAC,
            leverage=leverage,
        )
    return {
        "account": account,
        "name": name,
        "sl_pct": sl_pct,
        "sl_note": sl_note,
        "leverage": leverage,
        "min_executable_qty": min_q,
        "min_lot_stop_risk_usdt": min_lot_risk,
        "min_equity_usdt_for_5pct_risk": e_min,
        "meaning": (
            "Below this wallet, one Bybit-minimum Solana lot already risks more than "
            "5% if the stop hits. Skip the trade (do not round the lot up). "
            "At this wallet, qty = the minimum lot and stop-risk is 5%. "
            "Above it, qty is floored so stop-risk stays at or under 5%."
        ),
        "wallet": wallet,
        "size_at_current_wallet": live_size,
        "examples": examples,
    }


def main() -> None:
    venue = fetch_bybit_sol()
    spec = instrument_from_bybit(venue)
    price = float(venue["mark"])
    ema_sl = ema_signal_sl_stats()
    w4 = _try_wallet("Xxobster4")
    w10 = _try_wallet("Xxobster10")
    payload = {
        "stamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "do_not_deploy": True,
        "risk_fraction": RISK_FRAC,
        "rounding": "floor to qty_step; skip if below venue min; never round up past 5%",
        "venue": venue,
        "price_used": price,
        "price_field": "bybit_mark",
        "ema_sl_stats": ema_sl,
        "xxobster4_sol_1h_ema_stack": _book(
            name="SOLUSDT 1h power_ema_stack_long",
            account="Xxobster4",
            sl_pct=float(ema_sl["sl_mean"]),
            sl_note="mean stop on pre-lockbox Exponential Moving Average stack signal bars; clip(1.5*ATR%, 0.4%, 3%)",
            price=price,
            spec=spec,
            leverage=EMA_LEV,
            wallet=w4,
        ),
        "xxobster4_ema_at_sl_cap": _book(
            name="SOLUSDT 1h power_ema_stack_long (3% cap, widest stop)",
            account="Xxobster4",
            sl_pct=float(SOL_EMA_SPEC["sl_cap"]),
            sl_note="worst-case cap used for leverage; need the most equity to keep 5%",
            price=price,
            spec=spec,
            leverage=EMA_LEV,
            wallet=w4,
        ),
        "xxobster4_ema_sl_now": _book(
            name="SOLUSDT 1h power_ema_stack_long (last closed 1h stop)",
            account="Xxobster4",
            sl_pct=float(ema_sl["sl_now_last_closed_1h"]),
            sl_note="clip(1.5 * last closed 1h ATR%, 0.4%, 3%)",
            price=price,
            spec=spec,
            leverage=EMA_LEV,
            wallet=w4,
        ),
        "xxobster10_autonomy_013": _book(
            name="SOLUSDT 15m autonomy gen013 atr_rel_cross_up_h8",
            account="Xxobster10",
            sl_pct=AUTO013_SL,
            sl_note="frozen 1% stop",
            price=price,
            spec=spec,
            leverage=AUTO013_LEV,
            wallet=w10,
        ),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "stop_risk_5pct_xx4_xx10_latest.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2), flush=True)
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
