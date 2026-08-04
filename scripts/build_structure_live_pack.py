"""Freeze a deployable structure_v1 LightGBM pack: model + Mark/tier + meta.

Does not place orders. Writes under artifacts/live_packs/structure_v1_lgbm/.
"""

from __future__ import annotations

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
from llm2.hunt.runner import _labels_for_target, _make_model  # noqa: E402
from llm2.live.certificate import PACK_DIR, pack_fingerprint  # noqa: E402
from llm2.paths import FORWARD_LOCKBOX_START, ROUND_TRIP_COST  # noqa: E402
from llm2.research_policy import MIN_SIZE_EQUITY_CAVEAT  # noqa: E402
from llm2.validation.folds import OUTER_FOLD_RANGES, index_to_ms  # noqa: E402

SYMBOL = "BTCUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "fwd_return"
MODEL = "lgbm_regressor"
HORIZON = 6
TP = 0.01
SL = 0.02


def main() -> int:
    pack = PACK_DIR
    pack.mkdir(parents=True, exist_ok=True)

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = _labels_for_target(ohlcv, TARGET, HORIZON, SYMBOL)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    feature_cols = [c for c in aligned.columns if c != "y"]
    X = aligned[feature_cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)

    # Train on all bars before the last outer fold OOS start (frozen selection geometry).
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
        },
        model_path,
    )

    tiers = fetch_risk_limit_tiers(SYMBOL)
    inst = research_instrument(SYMBOL)
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
                "symbol": SYMBOL,
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

    # Mark snapshot via public ticker (full Mark history stays in the warehouse).
    try:
        import json as _json
        import urllib.request

        url = (
            "https://api.bybit.com/v5/market/tickers?"
            f"category=linear&symbol={SYMBOL}"
        )
        with urllib.request.urlopen(url, timeout=20) as resp:
            payload = _json.loads(resp.read().decode("utf-8"))
        row = (payload.get("result") or {}).get("list") or [{}]
        mark_meta = {
            "symbol": SYMBOL,
            "mark_price": row[0].get("markPrice"),
            "last_price": row[0].get("lastPrice"),
            "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            "source": "bybit_v5_tickers",
        }
        (pack / "mark_snapshot.json").write_text(
            _json.dumps(mark_meta, indent=2) + "\n", encoding="utf-8"
        )
    except Exception as exc:  # noqa: BLE001
        mark_meta = {"error": f"{type(exc).__name__}: {exc}"}

    from llm2.gates.evidence import (
        DEFAULT_LEVERAGE_HAIRCUT,
        DEFAULT_MARK_BUFFER,
        DEFAULT_MM_BUFFER,
        leverage_ceiling_from_stop,
        resolve_operational_leverage,
    )

    lev_info = resolve_operational_leverage(SL)
    lev = float(lev_info["leverage"])
    strategy = {
        "strategy_id": "structure_v1_lgbm_BTCUSDT_1h",
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "venue_product": "Bybit USDT perpetual",
        "feature_space": SPACE,
        "target": TARGET,
        "horizon_bars": HORIZON,
        "model": MODEL,
        "tp_pct": TP,
        "sl_pct": SL,
        "min_edge": ROUND_TRIP_COST,
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
        "position_mode": "ONE_WAY",
        "max_positions": 1,
        "fold_geometry": "v2",
        "trained_until_exclusive": str(last_oos_start),
        "lockbox_start": FORWARD_LOCKBOX_START,
        "feature_columns": feature_cols,
        "model_file": model_path.name,
        "mark_sample": mark_meta,
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
        "what_it_does": (
            "On each closed 1h BTCUSDT bar, load confirmed-swing structure_v1 features "
            "(warehouse + vol-normalised distances + completed higher-TF structure). "
            "LightGBM regressor predicts the next-6-bar log return. If |prediction| exceeds "
            "the round-trip cost hurdle (0.16%), open ONE min-qty market position in the "
            "sign of the prediction with TP=+1% and SL=-2%, max hold 6 bars. "
            "Otherwise flat. No concurrent books."
        ),
    }
    (pack / "strategy.json").write_text(
        json.dumps(strategy, indent=2) + "\n", encoding="utf-8"
    )

    settlement_path = Path("artifacts/reports/structure_v1_tier2_settlement.json")
    settlement = {}
    if settlement_path.is_file():
        settlement = json.loads(settlement_path.read_text(encoding="utf-8"))

    meta = {
        "strategy_id": strategy["strategy_id"],
        "status": "FROZEN_LIVE_PACK",
        "readiness": "MICRO_LIVE_CANDIDATE_PENDING_SHADOW",
        "deployable": True,
        "settlement_verdict": settlement.get("verdict"),
        "pooled_pf": settlement.get("pooled_pf"),
        "fold_geometry": "v2",
        "tiers_n": len(tier_rows),
        "liquidation_model": "MODELLED_WITH_TIERS" if tier_rows else "SIMPLIFIED",
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
        "account_ref_expected": "Xxobster7",
        "vps_host_expected": "94.156.189.76",
        "frozen_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
    }
    (pack / "pack_meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    (pack / "README.md").write_text(
        "# structure_v1 LightGBM live pack (BTCUSDT 1h)\n\n"
        "Frozen model + Bybit risk-limit tiers + strategy JSON.\n"
        "Micro-live only (MIN_EXCHANGE). Requires live certificate AUTHORIZED.\n",
        encoding="utf-8",
    )

    fp = pack_fingerprint(pack)
    print(json.dumps({"pack": str(pack), "fingerprint": fp, "tiers": len(tier_rows)}, indent=2))
    if not tier_rows:
        print("WARNING: no risk tiers — liquidation still SIMPLIFIED", file=sys.stderr)
        return 2
    if not fp:
        return 1
    (pack / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
