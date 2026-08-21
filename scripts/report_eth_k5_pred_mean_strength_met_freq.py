#!/usr/bin/env python3
"""Frequency of |pred_mean| strength: met vs not-met gate buckets (ETH K5 path).

Outer folds only (pre-lockbox). RESEARCH diagnostic — does not promote.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import research_instrument

from llm2.data.loader import load_ohlcv
from llm2.features.registry import build_space
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family
from llm2.labels.direction import build_direction_labels
from llm2.live.multitrade import mean_strength_ok, scale_size_mult_by_abs_mean
from llm2.models.boosting import LGBMRegressorPredictor
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START
from llm2.signals.cluster_concurrency import build_cluster_size_signals
from llm2.signals.singlebook_clarity import SingleBookArm
from llm2.validation.folds import build_outer_folds, index_to_ms

SYMBOL = "ETHUSDT"
TF = "1h"
SPACE = "structure_v1"
TARGET = "direction"
HORIZON = 6
K = 5
SL = 0.02
MIN_EDGE = DIRECTION_BAND  # 0.10
REF = 0.5
ARM = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)


def main() -> int:
    ohlcv = load_ohlcv(SYMBOL, TF)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TF)
    y = build_direction_labels(ohlcv, horizon=HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=HORIZON, embargo_bars=HORIZON)
    close_full = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)
    family = target_family(TARGET)
    instrument = research_instrument(SYMBOL)

    # Per OOS bar arrays
    abs_all = []
    side_all = []
    edge_met = []
    clarity_met = []  # among edge-met, using same rolling median history as builder
    # richer buckets only after side assigned
    abs_edge = []  # |m| for |m|>=edge
    abs_trade = []  # emitted signals' |m|
    abs_edge_fail_clarity = []

    n_side_nonzero = 0
    n_bars = 0

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        # live-style: zero side when |mean|<edge is already in proxy_side for directional
        oos_ts = ts_ms[oos]
        close_oos = close_full[oos]
        strength_hist: list[float] = []
        n_bars += len(oos)

        for i in range(len(oos)):
            m = float(mean[i])
            s = int(side[i])
            am = abs(m)
            abs_all.append(am)
            side_all.append(s)
            if s != 0:
                n_side_nonzero += 1
            em = np.isfinite(m) and am >= float(MIN_EDGE) and s != 0
            edge_met.append(bool(em))
            if not em:
                clarity_met.append(False)
                continue
            abs_edge.append(am)
            recent = strength_hist[-168:] if strength_hist else []
            ok = mean_strength_ok(am, recent, strength_quantile=0.5)
            clarity_met.append(bool(ok))
            if ok:
                abs_trade.append(am)
            else:
                abs_edge_fail_clarity.append(am)
            strength_hist.append(am)

        # also run full signal builder for size_mult distribution on emitted
        sigs, stats = build_cluster_size_signals(
            oos_ts,
            side,
            mean,
            close_oos,
            arm=ARM,
            min_edge=MIN_EDGE,
            max_per_side=K,
            instrument=instrument,
            size_double_within_bars=3,
            strength_quantile=0.5,
            size_scale_by_abs_mean=True,
            size_scale_ref=REF,
            size_scale_factor_min=1.0,
            size_scale_factor_max=2.0,
        )
        if fold.fold_index == 0:
            first_stats = stats
            emitted_mult = [float(s.meta["size_mult"]) for s in sigs]
            emitted_str = [float(s.meta.get("strength_size_mult") or 1) for s in sigs]
            emitted_abs = [float(s.meta.get("abs_mean") or 0) for s in sigs]
        else:
            emitted_mult.extend(float(s.meta["size_mult"]) for s in sigs)
            emitted_str.extend(float(s.meta.get("strength_size_mult") or 1) for s in sigs)
            emitted_abs.extend(float(s.meta.get("abs_mean") or 0) for s in sigs)

    abs_all = np.asarray(abs_all, dtype=float)
    edge_met_a = np.asarray(edge_met, dtype=bool)
    clarity_met_a = np.asarray(clarity_met, dtype=bool)
    abs_edge = np.asarray(abs_edge, dtype=float)
    abs_trade = np.asarray(abs_trade, dtype=float)
    abs_edge_fail_clarity = np.asarray(abs_edge_fail_clarity, dtype=float)
    emitted_abs = np.asarray(emitted_abs, dtype=float)
    emitted_str = np.asarray(emitted_str, dtype=float)

    def pct(n, d):
        return float(n) / float(d) if d else float("nan")

    # Strength-scale bins on edge-met bars (could have traded if clarity ok)
    # floor: factor pinned to 1 (|m|/0.5 < 1 i.e. |m| < 0.5)
    # prop: 0.5 <= |m| < 1.0
    # cap: |m| >= 1.0
    def scale_bins(arr):
        if arr.size == 0:
            return {"n": 0}
        floor = arr < REF
        prop = (arr >= REF) & (arr < 2 * REF)
        cap = arr >= 2 * REF
        return {
            "n": int(arr.size),
            "floor_below_ref": {
                "rule": f"|pred_mean| < {REF} → strength_mult=1 (floor)",
                "n": int(floor.sum()),
                "pct": pct(floor.sum(), arr.size),
            },
            "proportional": {
                "rule": f"{REF} <= |pred_mean| < {2*REF} → mult in (1,2)",
                "n": int(prop.sum()),
                "pct": pct(prop.sum(), arr.size),
            },
            "cap_2x": {
                "rule": f"|pred_mean| >= {2*REF} → strength_mult=2 (cap)",
                "n": int(cap.sum()),
                "pct": pct(cap.sum(), arr.size),
            },
            "stronger_than_ref_met": {
                "rule": f"|pred_mean| >= {REF} (strength scale actually lifts size)",
                "n": int((arr >= REF).sum()),
                "pct": pct((arr >= REF).sum(), arr.size),
            },
            "stronger_than_ref_not_met": {
                "rule": f"|pred_mean| < {REF} (no strength uplift; floor)",
                "n": int((arr < REF).sum()),
                "pct": pct((arr < REF).sum(), arr.size),
            },
            "quantiles_abs_mean": {
                "p10": float(np.quantile(arr, 0.10)),
                "p25": float(np.quantile(arr, 0.25)),
                "p50": float(np.quantile(arr, 0.50)),
                "p75": float(np.quantile(arr, 0.75)),
                "p90": float(np.quantile(arr, 0.90)),
                "p95": float(np.quantile(arr, 0.95)),
            },
        }

    # Edge gate fine bins 0.1,0.2,...,0.9
    edges = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    edge_ladder = []
    base_n = abs_edge.size
    for e in edges:
        met = int((abs_edge >= e).sum()) if base_n else 0
        edge_ladder.append(
            {
                "threshold": e,
                "n_edge_met_abs_ge": met,
                "pct_of_edge_ge_01": pct(met, base_n),
                "n_not_met": int(base_n - met),
                "pct_not_met": pct(base_n - met, base_n),
            }
        )

    # Clarity: stronger signals that fail median (interesting)
    fail_strong = (
        abs_edge_fail_clarity[abs_edge_fail_clarity >= REF]
        if abs_edge_fail_clarity.size
        else np.array([])
    )
    fail_weak = (
        abs_edge_fail_clarity[abs_edge_fail_clarity < REF]
        if abs_edge_fail_clarity.size
        else np.array([])
    )

    out = {
        "evidence_class": "MEASURE_DIAGNOSTIC",
        "maximum_earned_readiness": "RESEARCH_ONLY",
        "gate_name": "ETH K5 |pred_mean| strength met / not-met frequencies",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "symbol": SYMBOL,
        "timeframe": TF,
        "geometry": "k5 double3h path + mean_strength median clarity",
        "definitions": {
            "edge_met": f"|pred_mean| >= {MIN_EDGE} and directional side != 0 (live min_edge)",
            "clarity_met": "among edge_met: |m| >= median of prior 168 strength history",
            "strength_scale_lift_met": f"|pred_mean| >= {REF} → strength_mult > 1",
            "strength_scale_lift_not_met": f"{MIN_EDGE} <= |pred_mean| < {REF} → strength_mult stays floor 1",
            "trade_emitted": "edge + clarity + concurrent K=5 slot available",
        },
        "population": {
            "n_oos_bars": int(n_bars),
            "n_side_nonzero_raw": int(n_side_nonzero),
            "n_edge_met": int(edge_met_a.sum()),
            "pct_oos_bars_edge_met": pct(edge_met_a.sum(), n_bars),
            "n_clarity_met_among_edge": int(
                sum(1 for e, c in zip(edge_met, clarity_met) if e and c)
            ),
            "n_edge_met_clarity_fail": int(abs_edge_fail_clarity.size),
            "pct_clarity_pass_given_edge": pct(
                sum(1 for e, c in zip(edge_met, clarity_met) if e and c),
                edge_met_a.sum(),
            ),
            "pct_clarity_fail_given_edge": pct(
                abs_edge_fail_clarity.size, edge_met_a.sum()
            ),
            "n_signals_emitted_with_size_scale": int(emitted_abs.size),
        },
        "among_edge_met_abs_mean_strength": scale_bins(abs_edge),
        "among_clarity_passed_would_trade_pre_cap": scale_bins(abs_trade),
        "among_emitted_actual_trades": scale_bins(emitted_abs),
        "edge_threshold_ladder_among_edge_ge_01": edge_ladder,
        "clarity_fails_but_edge_met": {
            "n": int(abs_edge_fail_clarity.size),
            "n_strong_abs_ge_ref": int(fail_strong.size),
            "pct_of_clarity_fails_that_are_strong": pct(
                fail_strong.size, abs_edge_fail_clarity.size
            ),
            "n_weak_abs_lt_ref": int(fail_weak.size),
            "mean_abs_when_fail": float(abs_edge_fail_clarity.mean())
            if abs_edge_fail_clarity.size
            else None,
            "mean_abs_when_pass": float(abs_trade.mean()) if abs_trade.size else None,
            "note": (
                "Strong but not met = |pred| high but rolling median clarity blocked "
                "entry (history stricter than raw strength)."
            ),
        },
        "emitted_strength_mult_summary": {
            "mean": float(emitted_str.mean()) if emitted_str.size else None,
            "pct_exactly_1": pct((np.abs(emitted_str - 1.0) < 1e-12).sum(), emitted_str.size)
            if emitted_str.size
            else None,
            "pct_strictly_gt_1": pct((emitted_str > 1.0 + 1e-12).sum(), emitted_str.size)
            if emitted_str.size
            else None,
            "pct_exactly_2": pct((np.abs(emitted_str - 2.0) < 1e-12).sum(), emitted_str.size)
            if emitted_str.size
            else None,
        },
        "headline": {},
    }

    # Headlines for user
    e = out["among_edge_met_abs_mean_strength"]
    t = out["among_clarity_passed_would_trade_pre_cap"]
    em = out["among_emitted_actual_trades"]
    out["headline"] = {
        "of_edge_met_pct_strong_enough_for_size_lift": e.get("stronger_than_ref_met", {}).get(
            "pct"
        ),
        "of_edge_met_pct_too_weak_for_size_lift": e.get("stronger_than_ref_not_met", {}).get(
            "pct"
        ),
        "of_clarity_passed_pct_strong_size_lift": t.get("stronger_than_ref_met", {}).get("pct"),
        "of_clarity_passed_pct_size_floor": t.get("stronger_than_ref_not_met", {}).get("pct"),
        "of_emitted_trades_pct_strong_size_lift": em.get("stronger_than_ref_met", {}).get("pct"),
        "of_emitted_trades_pct_size_floor": em.get("stronger_than_ref_not_met", {}).get("pct"),
        "pct_edge_met_that_fail_clarity": out["population"]["pct_clarity_fail_given_edge"],
        "pct_clarity_fails_that_were_strong_ge_ref": out["clarity_fails_but_edge_met"][
            "pct_of_clarity_fails_that_are_strong"
        ],
    }

    reports = ARTIFACTS / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stem = "structure_v1_eth_k5_pred_mean_strength_met_freq_001"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    latest = reports / f"{stem}_latest.json"
    path = reports / f"{stem}_{stamp}.json"
    blob = json.dumps(out, indent=2, default=str)
    latest.write_text(blob, encoding="utf-8")
    path.write_text(blob, encoding="utf-8")

    h = out["headline"]
    print("=== |pred_mean| strength MET / NOT MET (ETH K5 OOS stitch) ===")
    print(f"OOS bars: {out['population']['n_oos_bars']}")
    print(
        f"Edge met (|m|>={MIN_EDGE}): {out['population']['n_edge_met']} "
        f"({100*out['population']['pct_oos_bars_edge_met']:.1f}% of bars)"
    )
    print(
        f"Clarity pass | edge: {100*out['population']['pct_clarity_pass_given_edge']:.1f}%  "
        f"Clarity FAIL | edge: {100*out['population']['pct_clarity_fail_given_edge']:.1f}%"
    )
    print()
    print("--- Among EDGE-MET bars (could trade if clarity + slot) ---")
    print(
        f"SIZE LIFT MET  (|m|>={REF}): {100*h['of_edge_met_pct_strong_enough_for_size_lift']:.1f}%"
    )
    print(
        f"SIZE LIFT NOT  ({MIN_EDGE}<=|m|<{REF}): {100*h['of_edge_met_pct_too_weak_for_size_lift']:.1f}%"
    )
    print(
        f"  floor/prop/cap: "
        f"{100*e['floor_below_ref']['pct']:.1f}% / "
        f"{100*e['proportional']['pct']:.1f}% / "
        f"{100*e['cap_2x']['pct']:.1f}%"
    )
    print()
    print("--- Among CLARITY-PASSED (pre K-slot) ---")
    print(
        f"SIZE LIFT MET: {100*h['of_clarity_passed_pct_strong_size_lift']:.1f}%  "
        f"FLOOR: {100*h['of_clarity_passed_pct_size_floor']:.1f}%"
    )
    print()
    print("--- Among EMITTED trades (K=5 + size-scale on) ---")
    print(
        f"SIZE LIFT MET: {100*h['of_emitted_trades_pct_strong_size_lift']:.1f}%  "
        f"FLOOR: {100*h['of_emitted_trades_pct_size_floor']:.1f}%"
    )
    print(
        f"strength_mult==1: {100*out['emitted_strength_mult_summary']['pct_exactly_1']:.1f}%  "
        f">1: {100*out['emitted_strength_mult_summary']['pct_strictly_gt_1']:.1f}%  "
        f"==2: {100*out['emitted_strength_mult_summary']['pct_exactly_2']:.1f}%"
    )
    print()
    print("--- Clarity FAIL but edge met (strong signal not traded) ---")
    print(
        f"n clarity fails: {out['clarity_fails_but_edge_met']['n']}  "
        f"of which strong |m|>={REF}: "
        f"{out['clarity_fails_but_edge_met']['n_strong_abs_ge_ref']} "
        f"({100*out['clarity_fails_but_edge_met']['pct_of_clarity_fails_that_are_strong']:.1f}%)"
    )
    print(f"WROTE {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
