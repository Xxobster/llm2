"""Freeze a structure_v1 LightGBM live pack for one symbol/target (CLI)."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import research_instrument  # noqa: E402
from tradesim.venue.bybit import fetch_risk_limit_tiers  # noqa: E402

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import (  # noqa: E402
    DEFAULT_LEVERAGE_HAIRCUT,
    DEFAULT_MARK_BUFFER,
    DEFAULT_MM_BUFFER,
    leverage_ceiling_from_stop,
    resolve_operational_leverage,
)
from llm2.hunt.runner import _labels_for_target, _make_model  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, DEFAULT_HORIZON, target_family  # noqa: E402
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.live.refresh_structure import refresh_symbol  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROUND_TRIP_COST  # noqa: E402
from llm2.research_policy import MIN_SIZE_EQUITY_CAVEAT  # noqa: E402
from llm2.validation.folds import OUTER_FOLD_RANGES, index_to_ms  # noqa: E402

SPACE = "structure_v1"
MODEL = "lgbm_regressor"
TP = 0.01
SL = 0.02


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", required=True)
    ap.add_argument("--target", choices=("fwd_return", "direction"), required=True)
    ap.add_argument("--timeframe", default="1h")
    ap.add_argument(
        "--pack-dir",
        type=Path,
        default=None,
        help="default artifacts/live_packs/structure_v1_{symbol}_{target}",
    )
    args = ap.parse_args(argv)

    symbol = args.symbol.upper()
    target = args.target
    timeframe = args.timeframe
    horizon = int(DEFAULT_HORIZON[target])
    family = target_family(target)
    min_edge = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    pack = args.pack_dir or (
        ARTIFACTS / "live_packs" / f"structure_v1_{symbol.lower()}_{target}"
    )
    pack.mkdir(parents=True, exist_ok=True)

    ohlcv = load_ohlcv(symbol, timeframe)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=timeframe)
    y = _labels_for_target(ohlcv, target, horizon, symbol)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    feature_cols = [c for c in aligned.columns if c != "y"]
    X = aligned[feature_cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)

    last_oos_start = pd.Timestamp(OUTER_FOLD_RANGES[-1][0], tz="UTC")
    train_mask = np.asarray(aligned.index < last_oos_start)
    if int(train_mask.sum()) < 500:
        raise RuntimeError("insufficient train rows for live pack freeze")

    model = _make_model(MODEL)
    model.fit(X[train_mask], yv[train_mask])
    model_path = pack / "model.joblib"
    joblib.dump(
        {
            "model": model,
            "feature_columns": feature_cols,
            "model_name": MODEL,
            "trained_until": str(last_oos_start),
            "n_train": int(train_mask.sum()),
            "symbol": symbol,
            "target": target,
        },
        model_path,
    )

    tiers = fetch_risk_limit_tiers(symbol)
    inst = research_instrument(symbol)
    tier_rows = [
        {
            "notional_floor": t.notional_floor,
            "mm_rate": t.mm_rate,
            "max_leverage": t.max_leverage,
            "deduction": t.deduction,
        }
        for t in tiers
    ]
    (pack / "risk_tiers.json").write_text(
        json.dumps(
            {
                "symbol": symbol,
                "source": "bybit_v5_market_risk-limit",
                "retrieved_utc": datetime.now(timezone.utc).isoformat(),
                "n_tiers": len(tier_rows),
                "tiers": tier_rows,
                "instrument": {
                    "tick_size": inst.tick_size,
                    "qty_step": inst.qty_step,
                    "min_qty": inst.min_qty,
                    "min_notional": inst.min_notional,
                    "max_leverage": inst.max_leverage,
                    "tiers_available": bool(getattr(inst, "tiers_available", False)),
                    "n_tiers_on_spec": len(getattr(inst, "maintenance_tiers", ()) or ()),
                    "source": getattr(inst, "source", None),
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    try:
        import urllib.request

        url = (
            "https://api.bybit.com/v5/market/tickers?"
            f"category=linear&symbol={symbol}"
        )
        with urllib.request.urlopen(url, timeout=20) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        row = (payload.get("result") or {}).get("list") or [{}]
        mark_meta = {
            "symbol": symbol,
            "mark_price": row[0].get("markPrice"),
            "last_price": row[0].get("lastPrice"),
            "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            "source": "bybit_v5_tickers",
        }
        (pack / "mark_snapshot.json").write_text(
            json.dumps(mark_meta, indent=2) + "\n", encoding="utf-8"
        )
    except Exception as exc:  # noqa: BLE001
        mark_meta = {"error": f"{type(exc).__name__}: {exc}"}

    lev_info = resolve_operational_leverage(SL)
    lev = float(lev_info["leverage"])
    strategy_id = f"structure_v1_lgbm_{symbol}_{timeframe}_{target}"
    strategy = {
        "strategy_id": strategy_id,
        "symbol": symbol,
        "timeframe": timeframe,
        "venue_product": "Bybit USDT perpetual",
        "feature_space": SPACE,
        "target": target,
        "horizon_bars": horizon,
        "model": MODEL,
        "tp_pct": TP,
        "sl_pct": SL,
        "min_edge": min_edge,
        "leverage": lev,
        "leverage_policy": {
            "method": "leverage_from_stop",
            "sl_pct": SL,
            "mm_buffer": DEFAULT_MM_BUFFER,
            "mark_buffer": DEFAULT_MARK_BUFFER,
            "haircut": DEFAULT_LEVERAGE_HAIRCUT,
            "ceiling_before_haircut": int(leverage_ceiling_from_stop(SL)),
            "note": "Lowest operational leverage with SL security margin (D-001).",
        },
        "sizing": "MIN_EXCHANGE",
        "position_mode": "HEDGE",
        "max_positions": 1,
        "fold_geometry": "v2",
        "trained_until_exclusive": str(last_oos_start),
        "lockbox_start": FORWARD_LOCKBOX_START,
        "feature_columns": feature_cols,
        "model_file": model_path.name,
        "mark_sample": mark_meta,
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
        "what_it_does": (
            f"On each closed {timeframe} {symbol} bar, load confirmed-swing structure_v1 "
            f"features. LightGBM regressor predicts target={target} (horizon {horizon}). "
            f"If |prediction| clears the gate (min_edge={min_edge}), open ONE min-qty "
            f"market position with TP=+{TP:.0%} and SL=-{SL:.0%}, max hold {horizon} bars. "
            "Otherwise flat. Separate bot from BTCUSDT; max one open book on this symbol."
        ),
    }
    (pack / "strategy.json").write_text(
        json.dumps(strategy, indent=2) + "\n", encoding="utf-8"
    )

    # Bootstrap feature slice via Bybit REST (does not depend on warehouse freshness).
    slice_db = pack / "indicators_live_slice.sqlite"
    if slice_db.exists():
        slice_db.unlink()
    rep = refresh_symbol(
        symbol=symbol,
        timeframes=("1h", "4h", "1w"),
        indicator_db=slice_db,
        limit=800,
    )
    (pack / "structure_refresh_bootstrap.json").write_text(
        json.dumps(rep, indent=2) + "\n", encoding="utf-8"
    )

    settle_path = ARTIFACTS / "reports" / "structure_v1_eth_sol_settle_20260803T161346Z.json"
    settle = {}
    if settle_path.is_file():
        raw = json.loads(settle_path.read_text(encoding="utf-8"))
        for row in raw.get("combos") or []:
            if row.get("symbol") == symbol and row.get("target") == target:
                settle = row
                break

    meta = {
        "strategy_id": strategy_id,
        "status": "FROZEN_LIVE_PACK",
        "readiness": "MICRO_LIVE_AUTHORIZED_PENDING_SERVICE",
        "deployable": True,
        "settlement_overall": settle.get("overall"),
        "settlement_tier": settle.get("tier"),
        "pooled_pf": settle.get("pooled_pf"),
        "fold_geometry": "v2",
        "tiers_n": len(tier_rows),
        "account_ref_expected": "Xxobster7",
        "vps_host_expected": "94.156.189.76",
        "frozen_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
    }
    (pack / "pack_meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    (pack / "README.md").write_text(
        f"# {strategy_id}\n\n"
        "Frozen model + Bybit risk-limit tiers + strategy JSON.\n"
        "Micro-live only (MIN_EXCHANGE). Requires live certificate AUTHORIZED.\n",
        encoding="utf-8",
    )

    fp = pack_fingerprint(pack)
    (pack / "pack_hash.txt").write_text((fp or "") + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "pack": str(pack),
                "fingerprint": fp,
                "symbol": symbol,
                "target": target,
                "min_edge": min_edge,
                "leverage": lev,
                "tiers": len(tier_rows),
                "refresh": rep,
            },
            indent=2,
            default=str,
        )
    )
    return 0 if fp and tier_rows else 1


if __name__ == "__main__":
    raise SystemExit(main())
