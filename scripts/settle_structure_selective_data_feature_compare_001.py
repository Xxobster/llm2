"""Nested outer-fold compare: structure_v1 vs structure_v1+oi / +news.

Single-book CostHurdle geometry for fair feature-space isolation.
Hard end < lockbox. Primary: expectancy_return_units.
Negative result is a valid research success.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    Side,
    Signal,
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_hedge,
)

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.features.guard import run_audit_for_space  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    build_outer_folds,
    index_to_ms,
)

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
TARGET = "direction"
LABEL_HORIZON = 6
SL = 0.02
TP = 0.01
HOLD = 6
MIN_EDGE = DIRECTION_BAND
GEN = "structure_v1_selective_data_feature_compare_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN}.yaml"
CONTROL_SPACE = "structure_v1"
CANDIDATE_SPACES = ("structure_oi_v1", "structure_news_v1")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _pf(pnls: list[float]) -> float:
    a = np.asarray(pnls, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return float("nan")
    gp = float(a[a > 0].sum())
    gl = float((-a[a < 0]).sum())
    if gl <= 0:
        return float("inf") if gp > 0 else float("nan")
    return gp / gl


def stitch_space(space: str, *, label: str) -> dict[str, Any]:
    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, space, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(SYMBOL)
    family = target_family(TARGET)

    all_pnls: list[float] = []
    all_trades: list[Any] = []
    fold_rows: list[dict[str, Any]] = []
    n_liq = 0

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        sigs: list[Signal] = []
        for i in range(len(oos)):
            s = int(side[i])
            m = float(mean[i])
            if s == 0 or not np.isfinite(m) or abs(m) < MIN_EDGE:
                continue
            sigs.append(
                Signal(
                    ts_ms=int(oos_ts[i]),
                    side=Side.LONG if s > 0 else Side.SHORT,
                    stop_offset=SL,
                    target_offset=TP,
                    max_hold_bars=HOLD,
                    tag=f"{space}_single",
                )
            )
        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, HOLD * 4)
        pos = int(ohlcv.index.searchsorted(oos0))
        window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
        end, start = window.index[-1], window.index[0]
        dec_ms = int(TF_MS[TIMEFRAME])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(
            milliseconds=1
        )
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
        w_ts = index_to_ms(window.index)
        fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
        bundle = run_strategy_backtest(
            window,
            sigs,
            symbol=SYMBOL,
            timeframe=TIMEFRAME,
            strategy_id=f"{label}-f{fold.fold_index}",
            touch_ohlcv=touch_win,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_hedge(
                max_hold_bars=HOLD,
                decision_timeframe=TIMEFRAME,
                max_positions_per_side=1,
                max_positions_per_symbol=1,
            ),
            instrument=instrument,
            funding_ts_ms=funding_ts[fmask],
            funding_rate=funding_rt[fmask],
            strategy_meta={"name": label, "feature_space": space},
            plot=False,
            print_headline=False,
            store_path=None,
        )
        m = bundle.metrics
        trades = list(bundle.result.trades)
        pnls = [float(getattr(t, "realized_pnl", 0) or 0) for t in trades]
        all_pnls.extend(pnls)
        all_trades.extend(trades)
        n_liq += int(getattr(m, "n_liquidations", 0) or 0)
        fold_rows.append(
            {
                "fold_index": int(fold.fold_index),
                "n_trades": int(m.n_trades),
                "net_pnl": float(m.net_pnl),
                "profit_factor": float(m.profit_factor),
                "win_rate": float(getattr(m, "win_rate", float("nan"))),
                "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
            }
        )
        print(
            f"  {label} fold {fold.fold_index}: n={m.n_trades} pf={m.profit_factor}",
            flush=True,
        )

    wins = sum(1 for p in all_pnls if p > 0)
    exp_ru = (
        float(
            np.nanmean(
                [float(getattr(t, "return_units", float("nan"))) for t in all_trades]
            )
        )
        if all_trades
        else float("nan")
    )
    return {
        "label": label,
        "feature_space": space,
        "n_features": int(len(cols)),
        "folds": fold_rows,
        "stitched": {
            "n_trades": len(all_pnls),
            "net_pnl": float(np.nansum(all_pnls)),
            "profit_factor": _pf(all_pnls),
            "win_rate": float(wins / len(all_pnls)) if all_pnls else float("nan"),
            "expectancy_return_units": exp_ru,
            "n_liquidations": int(n_liq),
        },
        "leverage": lev,
    }


def main() -> int:
    if not PREREG.is_file():
        raise SystemExit(f"missing prereg {PREREG}")
    prereg_sha = _sha(PREREG)
    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")

    ohlcv_probe = load_ohlcv(SYMBOL, TIMEFRAME).iloc[-4000:]
    leakage_reports: dict[str, Any] = {}
    for space in (CONTROL_SPACE, *CANDIDATE_SPACES):
        print(f"[{GEN}] leakage {space} …", flush=True)
        try:
            rep = run_audit_for_space(
                ohlcv_probe, interval=TIMEFRAME, space=space, symbol=SYMBOL, cuts=2
            )
            leakage_reports[space] = {
                "passed": bool(rep.get("passed")),
                "leakage_potential": list(rep.get("leakage_potential") or [])[:20],
            }
            if not leakage_reports[space]["passed"]:
                print(f"  LEAKAGE FAIL {space}", flush=True)
                if space == CONTROL_SPACE:
                    raise RuntimeError(f"leakage hard-fail for {space}")
        except Exception as exc:  # noqa: BLE001
            leakage_reports[space] = {
                "passed": False,
                "error": f"{type(exc).__name__}: {exc}",
            }
            print(f"  leakage ERROR {space}: {exc}", flush=True)
            if space == CONTROL_SPACE:
                raise

    print(f"[{GEN}] control {CONTROL_SPACE} …", flush=True)
    control = stitch_space(CONTROL_SPACE, label=f"{GEN}_control")
    candidates: dict[str, Any] = {}
    compares: dict[str, Any] = {}
    for space in CANDIDATE_SPACES:
        if not leakage_reports.get(space, {}).get("passed", False):
            print(f"[{GEN}] SKIP {space} (leakage fail)", flush=True)
            candidates[space] = {"skipped": True, "leakage": leakage_reports.get(space)}
            compares[space] = {
                "skipped": True,
                "passed_success_criteria": False,
                "reason": "leakage_or_build_fail",
            }
            continue
        print(f"[{GEN}] candidate {space} …", flush=True)
        cand = stitch_space(space, label=f"{GEN}_{space}")
        candidates[space] = cand
        c_exp = control["stitched"].get("expectancy_return_units")
        k_exp = cand["stitched"].get("expectancy_return_units")
        c_pf = control["stitched"]["profit_factor"]
        k_pf = cand["stitched"]["profit_factor"]
        beat_exp = (
            c_exp is not None
            and k_exp is not None
            and math.isfinite(float(c_exp))
            and math.isfinite(float(k_exp))
            and float(k_exp) > float(c_exp)
        )
        pf_ok = math.isfinite(float(k_pf)) and float(k_pf) >= 1.20
        no_liq = int(cand["stitched"]["n_liquidations"]) == 0
        compares[space] = {
            "control_expectancy_return_units": c_exp,
            "candidate_expectancy_return_units": k_exp,
            "exp_ru_delta": (
                float(k_exp) - float(c_exp)
                if c_exp is not None
                and k_exp is not None
                and math.isfinite(float(c_exp))
                and math.isfinite(float(k_exp))
                else None
            ),
            "control_pf": c_pf,
            "candidate_pf": k_pf,
            "control_net_pnl": control["stitched"]["net_pnl"],
            "candidate_net_pnl": cand["stitched"]["net_pnl"],
            "control_win_rate": control["stitched"].get("win_rate"),
            "candidate_win_rate": cand["stitched"].get("win_rate"),
            "candidate_beats_control_exp_ru": beat_exp,
            "candidate_pf_ge_1_20": pf_ok,
            "candidate_no_liquidation": no_liq,
            "passed_success_criteria": bool(beat_exp and pf_ok and no_liq),
        }

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    any_pass = any(
        (compares.get(s) or {}).get("passed_success_criteria") for s in CANDIDATE_SPACES
    )
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": stamp,
            "preregister_path": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
            "preregister_sha256": prereg_sha,
            "evidence_class": "OUTER_TRANSFER_COMPARE",
            "max_readiness": "RESEARCH_ONLY",
            "promotion_allowed": False,
            "live_deploy": "FORBIDDEN",
            "primary_metric": "expectancy_return_units",
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "conformance_passed": bool(conf.get("passed")),
            "leakage": leakage_reports,
            "control": control,
            "candidates": candidates,
            "compare": compares,
            "any_candidate_passed": any_pass,
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "note": (
                "Single-book CostHurdle geometry for fair feature-space compare; "
                "not the live K5/multitrade layout. Negative result is valid success."
            ),
        }
    )
    out = ARTIFACTS / "reports"
    out.mkdir(parents=True, exist_ok=True)
    latest = out / f"{GEN}_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (out / f"{GEN}_{stamp}.json").write_text(
        latest.read_text(encoding="utf-8"), encoding="utf-8"
    )
    text = PREREG.read_text(encoding="utf-8")
    if "status: FROZEN" in text:
        PREREG.write_text(
            text.replace(
                "status: FROZEN",
                f"status: OOS_COMPARE_COMPLETE\nsettled_utc: \"{stamp}\"\n"
                f"preregister_sha256_at_run: {prereg_sha}",
                1,
            ),
            encoding="utf-8",
        )
    print(json.dumps({"compare": compares, "any_pass": any_pass}, indent=2, default=str))
    print(f"wrote {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
