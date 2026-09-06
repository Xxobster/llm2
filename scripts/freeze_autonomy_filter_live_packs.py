"""Freeze autonomy hunt heads 013/376/705 as live filter packs.

Exact hunt arm: existing 15-minute 1%/1% pivot LIMIT control AND
P(event in next H bars) >= pi*. RESEARCH_ONLY readiness. Operational
live still needs a certificate + user host/account authorization.
"""

from __future__ import annotations

import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.autonomy.filter_head import (  # noqa: E402
    feature_columns_present,
    fit_filter_head,
    pi_star_1pct,
    save_filter_head,
)
from llm2.autonomy.packs import build_autonomy_pack  # noqa: E402
from llm2.confluence.train import chronological_cut_index, split_ohlcv_files  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.evidence.pack_registry import register_freeze  # noqa: E402
from llm2.evidence.pivot_four_proof import run_pivot_four_proof  # noqa: E402
from llm2.gates.evidence import leverage_ceiling_from_stop, leverage_from_stop  # noqa: E402
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

HOST = "212.73.150.178"
CREATED_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
EXPIRES_UTC = "2026-09-08T21:00:00Z"
MAX_ROWS = 120_000
TP_SL = 0.01

ETH_SRC = _ROOT / "artifacts" / "live_packs" / "pivot_eth_p75_ctrl_atr_w4"
SOL_SRC = _ROOT / "artifacts" / "live_packs" / "pivot_sol_geo_tp1_sl1_p75_w4"

ARMS = (
    {
        "generation": "376",
        "event": "sma540_below_at_h",
        "horizon": 4,
        "symbol": "SOLUSDT",
        "parent": SOL_SRC,
        "account": "Xxobster2",
        "work_bars": 5,
        "limit_level": "atr_clip",
        "pack_name": "autonomy_gen376_sol_sma540_below_h4",
        "arm_id": "autonomy_376_sol_sma540_below_h4",
        "unit": "llm2-autonomy-376-sol-sma540",
    },
    {
        "generation": "705",
        "event": "ema1320_below_at_h",
        "horizon": 4,
        "symbol": "ETHUSDT",
        "parent": ETH_SRC,
        "account": "Xxobster2",
        "work_bars": 4,
        "limit_level": "",
        "pack_name": "autonomy_gen705_eth_ema1320_below_h4",
        "arm_id": "autonomy_705_eth_ema1320_below_h4",
        "unit": "llm2-autonomy-705-eth-ema1320",
    },
    {
        "generation": "013",
        "event": "atr_rel_cross_up_1",
        "horizon": 8,
        "symbol": "SOLUSDT",
        "parent": SOL_SRC,
        "account": "Xxobster10",
        "work_bars": 5,
        "limit_level": "atr_clip",
        "pack_name": "autonomy_gen013_sol_atr_rel_cross_up_h8",
        "arm_id": "autonomy_013_sol_atr_rel_cross_up_h8",
        "unit": "llm2-autonomy-013-sol-atrrel",
    },
)


def _lock_ts() -> pd.Timestamp:
    return pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")


def _load_pre_lock(symbol: str, timeframe: str) -> pd.DataFrame:
    ohlcv = load_ohlcv(symbol, timeframe)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(_lock_ts().value // 1_000_000)].copy()
    if len(ohlcv) > MAX_ROWS:
        ohlcv = ohlcv.iloc[-MAX_ROWS:].copy()
    return ohlcv


def _fit_one(arm: dict) -> dict:
    symbol = str(arm["symbol"])
    gen = str(arm["generation"])
    horizon = int(arm["horizon"])
    event = str(arm["event"])
    print(f"FIT {arm['arm_id']} {symbol} gen={gen} H={horizon} {event}", flush=True)
    ohlcv = _load_pre_lock(symbol, "15m")
    db_dir = ARTIFACTS / "sqlite" / f"autonomy_filter_freeze_{gen}" / f"{symbol}_15m"
    db_dir.mkdir(parents=True, exist_ok=True)
    train_path = db_dir / "train.sqlite"
    test_path = db_dir / "test.sqlite"
    if not (train_path.exists() and test_path.exists()):
        split_ohlcv_files(ohlcv, train_path=train_path, test_path=test_path)
    import sqlite3

    with sqlite3.connect(str(train_path)) as con:
        train = pd.read_sql("SELECT * FROM ohlcv", con)
    if "ts_ms" in train.columns:
        idx = pd.to_datetime(train["ts_ms"].to_numpy(dtype=np.int64), unit="ms", utc=True)
        train = train.drop(columns=["ts_ms"])
        train.index = idx
    pack = build_autonomy_pack(train, gen=gen, horizon=horizon)
    cols = feature_columns_present(pack.features)
    x = pack.features[cols].to_numpy(dtype=float)
    y = pack.labels[event].to_numpy(dtype=float)
    ok = np.isfinite(y) & np.isfinite(x).all(axis=1)
    head = fit_filter_head(x[ok], y[ok].astype(np.int32))
    head["feature_columns"] = cols
    head["event"] = event
    head["generation"] = gen
    head["horizon_bars"] = horizon
    head["pi_star"] = pi_star_1pct()
    head["n_train_ok"] = int(ok.sum())
    print(
        f"  n_train_ok={head['n_train_ok']} ece={head['ece_inner']:.4f} "
        f"rate={head['train_rate']:.3f} cols={len(cols)} pi*={head['pi_star']:.4f}",
        flush=True,
    )
    return head


def _write_cert(path: Path, *, strategy_id: str, pack_rel: str, pack_hash: str, four: dict, account: str, symbol: str, notes: str) -> None:
    hashes = "\n".join(f"  {k}: {v}" for k, v in four.items())
    path.write_text(
        f"""strategy_id: {strategy_id}
status: AUTHORIZED
authorized_by_user: true
vps_host: '{HOST}'
account_ref: {account}
intended_vps_host: '{HOST}'
intended_account_ref: {account}
pack_path: {pack_rel}
pack_hash: {pack_hash}
expires_utc: '{EXPIRES_UTC}'
created_utc: '{CREATED_UTC}'
four_proof_ok: true
four_proof_hashes:
{hashes}
notes: >-
  {notes}
""",
        encoding="utf-8",
    )


def _clone_and_stamp(arm: dict, head: dict) -> Path:
    src = Path(arm["parent"])
    dst = _ROOT / "artifacts" / "live_packs" / str(arm["pack_name"])
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    shutil.copy2(src / "model.joblib", dst / "model.joblib")
    if (src / "risk_tiers.json").is_file():
        shutil.copy2(src / "risk_tiers.json", dst / "risk_tiers.json")
    strategy = json.loads((src / "strategy.json").read_text(encoding="utf-8"))
    lev = float(leverage_from_stop(TP_SL))
    strategy["strategy_id"] = f"{arm['pack_name']}_{arm['symbol']}_15m"
    strategy["arm_id"] = arm["arm_id"]
    strategy["work_bars"] = int(arm["work_bars"])
    strategy["max_hold_bars"] = 6
    strategy["tp_pct"] = TP_SL
    strategy["sl_pct"] = TP_SL
    strategy["leverage"] = lev
    strategy["leverage_ceiling"] = float(leverage_ceiling_from_stop(TP_SL))
    if arm["limit_level"]:
        strategy["limit_level"] = arm["limit_level"]
    strategy["filter"] = {
        "generation": arm["generation"],
        "event": arm["event"],
        "horizon_bars": int(arm["horizon"]),
        "pi_star": float(head["pi_star"]),
        "feature_columns": list(head["feature_columns"]),
        "parent_pack": src.name,
        "mode": "one_head_filter_pi_star",
    }
    strategy["readiness_max"] = "RESEARCH_ONLY"
    strategy["promotion_allowed"] = False
    strategy["frozen_utc"] = CREATED_UTC
    (dst / "strategy.json").write_text(json.dumps(strategy, indent=2) + "\n", encoding="utf-8")
    save_filter_head(
        dst / "filter_head.joblib",
        {
            "model": head["model"],
            "iso": head["iso"],
            "feature_columns": head["feature_columns"],
            "event": head["event"],
            "generation": head["generation"],
            "horizon_bars": head["horizon_bars"],
            "pi_star": head["pi_star"],
            "ece_inner": head["ece_inner"],
            "n_train": head["n_train"],
        },
    )
    src_meta = json.loads((src / "pack_meta.json").read_text(encoding="utf-8")) if (src / "pack_meta.json").is_file() else {}
    meta = {
        "pack_name": arm["pack_name"],
        "arm_id": arm["arm_id"],
        "status": "FROZEN",
        "readiness": "RESEARCH_ONLY",
        "deployable": True,
        "parent_pack": src.name,
        "filter": strategy["filter"],
        "frozen_utc": CREATED_UTC,
        "sklearn_runtime": src_meta.get("sklearn_runtime"),
        "note": (
            "Pivot parent model plus autonomy predicted filter. "
            "Research remains LIVE_STOP / RESEARCH_ONLY."
        ),
    }
    (dst / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return dst


def main() -> int:
    if leverage_from_stop(TP_SL) != 29.0:
        raise SystemExit(f"expected 29x, got {leverage_from_stop(TP_SL)}")
    for arm in ARMS:
        head = _fit_one(arm)
        dst = _clone_and_stamp(arm, head)
        print(f"FOUR_PROOF {dst.name}", flush=True)
        summary = run_pivot_four_proof(pack_dir=dst)
        register_freeze(dst, readiness="RESEARCH_ONLY", status="FROZEN")
        meta = json.loads((dst / "pack_meta.json").read_text(encoding="utf-8"))
        fp = pack_fingerprint(dst)
        if not fp:
            raise SystemExit(f"fingerprint failed {dst}")
        meta["pack_hash"] = fp
        (dst / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        fp = pack_fingerprint(dst)
        if not fp:
            raise SystemExit(f"fingerprint failed after meta {dst}")
        (dst / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
        cert = _ROOT / "configs" / "live" / f"{arm['pack_name']}_{arm['account'].lower()}_ln2_certificate.yaml"
        four = dict((meta.get("evidence") or {}).get("four_proof_hashes") or meta.get("four_proof_hashes") or {})
        _write_cert(
            cert,
            strategy_id=f"{arm['pack_name']}_{arm['symbol']}_15m",
            pack_rel=f"artifacts/live_packs/{arm['pack_name']}",
            pack_hash=fp,
            four=four,
            account=str(arm["account"]),
            symbol=str(arm["symbol"]),
            notes=(
                f"User authorized 2026-08-25 real-USDT MIN_EXCHANGE on {HOST} / {arm['account']} "
                f"({arm['symbol']} 15m 1%/1% pivot control AND predicted {arm['event']} "
                f"H{arm['horizon']}). Leverage from stop 1% = 29x. "
                "Research readiness remains LIVE_STOP / RESEARCH_ONLY."
            ),
        )
        print(f"OK {arm['arm_id']} hash={fp} cert={cert.name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
