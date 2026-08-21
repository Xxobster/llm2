"""Freeze tip-scoring packs for pivot LIMIT arms (SOL geo_tp1 / ETH p75_ctrl_atr).

Trains final LightGBM heads on all pre-lockbox rows (minus a calibration slice),
persists calibrators + p75 threshold + level_mode. RESEARCH → tip pack only.
Does NOT authorize live orders by itself.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import lightgbm as lgb
import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import research_instrument  # noqa: E402
from tradesim.venue.bybit import fetch_risk_limit_tiers  # noqa: E402

from llm2.gates.evidence import (  # noqa: E402
    DEFAULT_LEVERAGE_HAIRCUT,
    DEFAULT_MARK_BUFFER,
    DEFAULT_MM_BUFFER,
    leverage_ceiling_from_stop,
    leverage_from_stop,
)
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.pivot.strategy.score_oos import _atr_frac, default_label_cfg  # noqa: E402
from llm2.pivot.train.calibration import apply_calibrator, fit_binary_calibrator  # noqa: E402
from llm2.pivot.train.multihead import _fit_predict_binary  # noqa: E402
from llm2.pivot.train.samples import build_samples  # noqa: E402
from llm2.pivot.train.walk_forward import ModelSpec  # noqa: E402
from llm2.research_policy import MIN_SIZE_EQUITY_CAVEAT  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

ARMS = {
    "sol_geo_tp1_sl1_p75_w4": {
        "symbol": "SOLUSDT",
        "level_mode": "ret",
        "gate": "p75",
        "feature_pack": "level_vsa",
        "tp_pct": 0.01,
        "sl_pct": 0.01,
        "work_bars": 4,
        "horizon_bars": 4,
        "timeframe": "15m",
    },
    "eth_p75_ctrl_atr_w4": {
        "symbol": "ETHUSDT",
        "level_mode": "atr",
        "gate": "p75",
        "feature_pack": "level_vsa",
        "tp_pct": 0.01,
        "sl_pct": 0.01,
        "work_bars": 4,
        "horizon_bars": 4,
        "timeframe": "15m",
    },
}


def _lgbm_cls() -> ModelSpec:
    return ModelSpec(
        "lgbm_m",
        lambda: lgb.LGBMClassifier(
            n_estimators=200,
            num_leaves=31,
            learning_rate=0.05,
            class_weight="balanced",
            verbosity=-1,
            random_state=20260812,
        ),
    )


def freeze_arm(arm_id: str, *, max_rows: int = 120_000) -> Path:
    cfg = dict(ARMS[arm_id])
    symbol = cfg["symbol"]
    timeframe = cfg["timeframe"]
    horizon = int(cfg["horizon_bars"])
    level_mode = str(cfg["level_mode"])
    pack_name = f"pivot_{arm_id}"
    pack = ARTIFACTS / "live_packs" / pack_name
    pack.mkdir(parents=True, exist_ok=True)

    label_cfg = default_label_cfg(timeframe=timeframe, atr_min=2.0)
    ms = _lgbm_cls()
    samp = build_samples(
        symbol=symbol,
        timeframe=timeframe,
        feature_pack=cfg["feature_pack"],
        label_cfg=label_cfg,
        horizon_bars=horizon,
        max_rows=max_rows,
    )
    X = samp["X"]
    y_any = samp["y_any"]
    y_high = samp["y_high_given"]
    y_level = samp["y_level_ret"]
    ts = samp["ts_ms"]
    feature_columns = list(samp["feature_names"])
    ohlcv = load_ohlcv(symbol, timeframe)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    atr_map = dict(
        zip(index_to_ms(ohlcv.index).tolist(), _atr_frac(ohlcv).tolist())
    )
    atrs = np.array([atr_map.get(int(t), np.nan) for t in ts], dtype=float)
    n = len(X)
    if n < 2000:
        raise RuntimeError(f"{arm_id}: only {n} rows — refuse freeze")

    # Tip freeze: train on all but last 15% (cal slice inside train); no lockbox peep.
    cut = int(n * 0.85)
    cal0 = int(cut * 0.8)
    tr_fit = np.arange(0, cal0)
    tr_cal = np.arange(cal0, cut)
    # Keep a held tip slice unused for train (parity / smoke); models use [0, cut).
    tr_all = np.arange(0, cut)

    p_cal_raw = _fit_predict_binary(
        X[tr_fit], y_any[tr_fit], X[tr_cal], model_spec=ms, is_baserate=False
    )
    cal_any = fit_binary_calibrator(y_any[tr_cal], p_cal_raw, method="isotonic")
    p_cal_cal = apply_calibrator(cal_any, p_cal_raw)
    thr_any = max(float(np.nanpercentile(p_cal_cal, 75)), 0.35)

    any_model = ms.builder()
    any_model.fit(X[tr_all], y_any[tr_all])

    high_model = None
    cal_high = None
    tr_ev = tr_all[y_high[tr_all] >= 0]
    if tr_ev.size >= 80:
        high_model = ms.builder()
        high_model.fit(X[tr_ev], y_high[tr_ev])
        tr_cal_ev = tr_cal[y_high[tr_cal] >= 0]
        if tr_cal_ev.size >= 40:
            p_hg_cal_raw = _fit_predict_binary(
                X[tr_ev], y_high[tr_ev], X[tr_cal_ev], model_spec=ms, is_baserate=False
            )
            cal_high = fit_binary_calibrator(
                y_high[tr_cal_ev], p_hg_cal_raw, method="isotonic"
            )

    y_lv = y_level.copy()
    if level_mode == "atr":
        with np.errstate(divide="ignore", invalid="ignore"):
            y_lv = np.where(np.isfinite(atrs) & (atrs > 1e-8), y_level / atrs, np.nan)
    tr_lv = tr_all[np.isfinite(y_lv[tr_all])]
    level_model = None
    if tr_lv.size >= 50:
        level_model = lgb.LGBMRegressor(
            n_estimators=200,
            num_leaves=31,
            learning_rate=0.05,
            verbosity=-1,
            random_state=20260812,
        )
        level_model.fit(X[tr_lv], y_lv[tr_lv])

    sl = float(cfg["sl_pct"])
    lev = float(leverage_from_stop(sl))
    lev_ceil = float(leverage_ceiling_from_stop(sl))

    blob = {
        "arm_id": arm_id,
        "symbol": symbol,
        "timeframe": timeframe,
        "feature_pack": cfg["feature_pack"],
        "feature_columns": feature_columns,
        "level_mode": level_mode,
        "gate": cfg["gate"],
        "thr_any": thr_any,
        "tp_pct": float(cfg["tp_pct"]),
        "sl_pct": sl,
        "work_bars": int(cfg["work_bars"]),
        "horizon_bars": horizon,
        "max_hold_bars": horizon + 2,
        "leverage": lev,
        "any_model": any_model,
        "cal_any": cal_any,
        "high_model": high_model,
        "cal_high": cal_high,
        "level_model": level_model,
        "n_train": int(tr_all.size),
        "n_cal": int(tr_cal.size),
        "trained_until_lockbox": FORWARD_LOCKBOX_START,
        "frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "readiness_max": "RESEARCH_ONLY",
        "note": "Tip freeze for pivot LIMIT micro-live. Not V2.1 SHADOW_READY.",
    }
    joblib.dump(blob, pack / "model.joblib")

    try:
        tiers = fetch_risk_limit_tiers(symbol)
    except Exception as exc:  # noqa: BLE001
        tiers = {"error": str(exc)}
    (pack / "risk_tiers.json").write_text(
        json.dumps(tiers, indent=2, default=str), encoding="utf-8"
    )

    strategy = {
        "strategy_id": f"pivot_{arm_id}_{symbol}_{timeframe}",
        "arm_id": arm_id,
        "symbol": symbol,
        "timeframe": timeframe,
        "feature_pack": cfg["feature_pack"],
        "level_mode": level_mode,
        "gate": cfg["gate"],
        "tp_pct": float(cfg["tp_pct"]),
        "sl_pct": sl,
        "work_bars": int(cfg["work_bars"]),
        "horizon_bars": horizon,
        "max_hold_bars": horizon + 2,
        "entry": "limit_work",
        "signal_source": "binance",
        "execution_venue": "bybit",
        "sizing": {"mode": "MIN_EXCHANGE"},
        "leverage": lev,
        "leverage_ceiling": lev_ceil,
        "leverage_from_stop": {
            "sl_pct": sl,
            "mm_buffer": DEFAULT_MM_BUFFER,
            "mark_buffer": DEFAULT_MARK_BUFFER,
            "haircut": DEFAULT_LEVERAGE_HAIRCUT,
            "operational": lev,
        },
        "thr_any": thr_any,
        "instrument": research_instrument(symbol).__dict__
        if hasattr(research_instrument(symbol), "__dict__")
        else str(research_instrument(symbol)),
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
        "readiness_max": "RESEARCH_ONLY",
        "promotion_allowed": False,
        "frozen_utc": blob["frozen_utc"],
    }
    (pack / "strategy.json").write_text(
        json.dumps(strategy, indent=2, default=str), encoding="utf-8"
    )
    (pack / "pack_meta.json").write_text(
        json.dumps(
            {
                "pack_name": pack_name,
                "arm_id": arm_id,
                "status": "FROZEN_TIP",
                "readiness": "RESEARCH_ONLY",
                "deployable": False,
                "evidence": {
                    "four_proof_ok": False,
                    "note": "Attach four_proof / tip-identity before certificate AUTHORIZED",
                },
                "frozen_utc": blob["frozen_utc"],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    fp = pack_fingerprint(pack)
    meta = json.loads((pack / "pack_meta.json").read_text(encoding="utf-8"))
    meta["pack_hash"] = fp
    (pack / "pack_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(
        f"FROZE {arm_id} -> {pack} lev={lev} thr_any={thr_any:.4f} "
        f"n_train={tr_all.size} hash={fp}",
        flush=True,
    )
    return pack


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--arms",
        nargs="+",
        default=list(ARMS),
        choices=list(ARMS),
        help="Which arms to freeze",
    )
    ap.add_argument("--max-rows", type=int, default=120_000)
    args = ap.parse_args()
    for arm in args.arms:
        freeze_arm(arm, max_rows=args.max_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
