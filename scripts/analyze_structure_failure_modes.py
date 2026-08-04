"""Failure-mode measure for structure packs (multitrade + single-book).

Evidence: MEASURE_DIAGNOSTIC. Outer folds only; lockbox unused.
Compares ETH multitrade book-1 weakness against BTC/ETH/SOL single-book.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim,
    research_sim_hedge,
)

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.experiments.eth_multitrade_nested import (  # noqa: E402
    build_multitrade_signals,
    live_control_cfg,
    pf,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.labels.fwd_return import build_fwd_return_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    ROUND_TRIP_COST,
    TF_MS,
    touch_timeframe,
)
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.signals.singlebook_clarity import SingleBookArm, build_singlebook_signals  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, build_outer_folds, index_to_ms  # noqa: E402

TIMEFRAME = "1h"
SPACE = "structure_v1"
LABEL_HORIZON = 6
SL = 0.02
FWD_BARS = (1, 3, 6, 12)
GEN = "structure_v1_failure_modes_btc_eth_sol_001"

# Live single-book geometry (Xxobster7): clarity none, hold 6, tp 1%.
LIVE_SINGLE = SingleBookArm(clarity="none", horizon_bars=6, tp_pct=0.01, sl_pct=SL)
# Clarity settle arm for contrast (pack-ready, not live).
CLARITY_SINGLE = SingleBookArm(
    clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL
)

COMBOS = (
    {
        "key": "eth_multitrade_v1_1",
        "symbol": "ETHUSDT",
        "target": "direction",
        "mode": "multitrade",
        "arm": None,
    },
    {
        "key": "btc_live_single",
        "symbol": "BTCUSDT",
        "target": "fwd_return",
        "mode": "single",
        "arm": LIVE_SINGLE,
    },
    {
        "key": "eth_live_single",
        "symbol": "ETHUSDT",
        "target": "direction",
        "mode": "single",
        "arm": LIVE_SINGLE,
    },
    {
        "key": "sol_live_single",
        "symbol": "SOLUSDT",
        "target": "direction",
        "mode": "single",
        "arm": LIVE_SINGLE,
    },
    {
        "key": "btc_clarity_hold12",
        "symbol": "BTCUSDT",
        "target": "fwd_return",
        "mode": "single",
        "arm": CLARITY_SINGLE,
    },
    {
        "key": "sol_clarity_hold12",
        "symbol": "SOLUSDT",
        "target": "direction",
        "mode": "single",
        "arm": CLARITY_SINGLE,
    },
)


def _min_edge(target: str) -> float:
    return float(DIRECTION_BAND) if target_family(target) == "directional" else float(ROUND_TRIP_COST)


def _labels(ohlcv: pd.DataFrame, target: str) -> pd.Series:
    if target == "direction":
        return build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    if target == "fwd_return":
        return build_fwd_return_labels(ohlcv, horizon=LABEL_HORIZON)["fwd_return"]
    raise ValueError(target)


def _signed_fwd(close: np.ndarray, entry_i: int, side: int) -> dict[str, float]:
    out: dict[str, float] = {}
    px0 = float(close[entry_i]) if 0 <= entry_i < len(close) else float("nan")
    sign = float(side)
    for h in FWD_BARS:
        j = entry_i + int(h)
        if not np.isfinite(px0) or px0 <= 0 or j >= len(close):
            out[f"signed_fwd_{h}"] = float("nan")
            continue
        out[f"signed_fwd_{h}"] = sign * (float(close[j]) / px0 - 1.0)
    return out


def _bucket(rows: list[dict[str, Any]], key: str) -> dict[str, Any]:
    groups: dict[Any, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        groups[r[key]].append(r)
    out: dict[str, Any] = {}
    for k, grp in sorted(groups.items(), key=lambda x: str(x[0])):
        pnls = np.asarray([g["pnl"] for g in grp], dtype=float)
        w1 = np.asarray([g["signed_fwd_1"] for g in grp], dtype=float)
        out[str(k)] = {
            "n": int(len(grp)),
            "win_rate": float(np.mean([g["win"] for g in grp])),
            "profit_factor": pf(pnls),
            "frac_wrong_way_1h": float(np.mean(w1 < 0)),
            "frac_wrong_way_3h": float(
                np.mean(np.asarray([g["signed_fwd_3"] for g in grp], dtype=float) < 0)
            ),
            "exit_reasons": {
                str(reason): int(sum(1 for g in grp if g["exit_reason"] == reason))
                for reason in sorted({g["exit_reason"] for g in grp})
            },
        }
    return out


def _cluster_all_loss_frac(df: pd.DataFrame) -> dict[str, float]:
    cluster_n = 0
    cluster_loss = 0
    for _, g in df.sort_values(["side", "entry_ts_ms"]).groupby("side"):
        g = g.reset_index(drop=True)
        i = 0
        while i < len(g):
            j = i
            while (
                j + 1 < len(g)
                and int(g.loc[j + 1, "entry_ts_ms"]) - int(g.loc[j, "entry_ts_ms"])
                <= 6 * 3_600_000
            ):
                j += 1
            cluster = g.loc[i:j]
            if len(cluster) >= 3:
                cluster_n += 1
                if bool((cluster["pnl"] <= 0).all()):
                    cluster_loss += 1
            i = j + 1
    return {
        "n_clusters": float(cluster_n),
        "n_all_loss": float(cluster_loss),
        "frac_all_loss": float(cluster_loss / cluster_n) if cluster_n else float("nan"),
    }


def analyse_combo(combo: dict[str, Any]) -> dict[str, Any]:
    symbol = combo["symbol"]
    target = combo["target"]
    mode = combo["mode"]
    print(f"AUDIT {combo['key']} …", flush=True)

    ohlcv = load_ohlcv(symbol, TIMEFRAME)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TIMEFRAME)
    y = _labels(ohlcv, target)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    touch = load_ohlcv(symbol, touch_timeframe(TIMEFRAME, symbol))
    touch_tf = touch_timeframe(TIMEFRAME, symbol)
    funding = load_funding(symbol)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(symbol)
    family = target_family(target)
    min_edge = _min_edge(target)
    full_close = ohlcv["close"].to_numpy(dtype=float)
    full_ts = index_to_ms(ohlcv.index)
    ts_to_i = {int(t): i for i, t in enumerate(full_ts)}
    mt_cfg = live_control_cfg()

    rows: list[dict[str, Any]] = []
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        if mode == "multitrade":
            sigs, stats = build_multitrade_signals(oos_ts, side, mean, cfg=mt_cfg)
            hold = int(mt_cfg["hold_addon"])
            sim = research_sim_hedge(
                max_hold_bars=hold,
                decision_timeframe=TIMEFRAME,
                max_positions_per_side=7,
                max_positions_per_symbol=14,
            )
        else:
            arm: SingleBookArm = combo["arm"]
            sigs, stats = build_singlebook_signals(
                oos_ts, side, mean, arm=arm, min_edge=min_edge
            )
            hold = int(arm.horizon_bars)
            sim = research_sim(max_hold_bars=hold, decision_timeframe=TIMEFRAME)

        mean_by_ts = {int(oos_ts[i]): float(mean[i]) for i in range(len(oos_ts))}

        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, hold * 4)
        pos = int(ohlcv.index.searchsorted(oos0))
        window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
        end, start = window.index[-1], window.index[0]
        dec_ms = int(TF_MS[TIMEFRAME])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
        w_ts = index_to_ms(window.index)
        fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
        bundle = run_strategy_backtest(
            window,
            sigs,
            symbol=symbol,
            timeframe=TIMEFRAME,
            strategy_id=f"{combo['key']}-f{fold.fold_index}",
            touch_ohlcv=touch_win,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=sim,
            instrument=instrument,
            funding_ts_ms=funding_ts[fmask],
            funding_rate=funding_rt[fmask],
            strategy_meta={"name": combo["key"]},
            plot=False,
            print_headline=False,
            store_path=None,
        )
        for t in bundle.result.trades:
            ets = int(t.entry_ts_ms)
            s = int(getattr(t.side, "value", t.side))
            tag = str(getattr(t, "tag", "") or "")
            book = 1
            if mode == "multitrade" and "_b" in tag:
                try:
                    book = int(tag.rsplit("_b", 1)[-1])
                except ValueError:
                    book = 1
            entry_i = ts_to_i.get(ets, -1)
            fwds = _signed_fwd(full_close, entry_i, s) if entry_i >= 0 else {
                f"signed_fwd_{h}": float("nan") for h in FWD_BARS
            }
            pnl = float(getattr(t, "realized_pnl", 0) or 0)
            m = float(mean_by_ts.get(ets, float("nan")))
            rows.append(
                {
                    "fold": int(fold.fold_index),
                    "entry_ts_ms": ets,
                    "side": s,
                    "book_idx": book,
                    "abs_mean": abs(m) if np.isfinite(m) else float("nan"),
                    "pnl": pnl,
                    "win": bool(pnl > 0),
                    "exit_reason": str(getattr(t, "exit_reason", "") or "unknown"),
                    "signed_fwd_1": fwds["signed_fwd_1"],
                    "signed_fwd_3": fwds["signed_fwd_3"],
                    "signed_fwd_6": fwds["signed_fwd_6"],
                    "signed_fwd_12": fwds["signed_fwd_12"],
                    "n_signals_fold": int(stats.get("n_emitted", 0)),
                }
            )
        print(
            f"  fold {fold.fold_index}: trades={len(bundle.result.trades)} "
            f"signals={stats.get('n_emitted', 0)}",
            flush=True,
        )

    if not rows:
        return {"key": combo["key"], "error": "no_trades"}

    df = pd.DataFrame(rows)
    am = df["abs_mean"].to_numpy(dtype=float)
    finite = np.isfinite(am)
    q = np.nanquantile(am[finite], [1 / 3, 2 / 3]) if finite.any() else np.array([0.0, 0.0])
    df["strength_tercile"] = np.where(
        ~finite,
        "na",
        np.where(am <= q[0], "low", np.where(am <= q[1], "mid", "high")),
    )
    rowdicts = df.to_dict(orient="records")
    book1 = df[df["book_idx"] == 1] if mode == "multitrade" else df
    los = df[~df["win"]]
    return {
        "key": combo["key"],
        "symbol": symbol,
        "target": target,
        "mode": mode,
        "arm": None
        if combo["arm"] is None
        else {
            "clarity": combo["arm"].clarity,
            "horizon_bars": combo["arm"].horizon_bars,
            "tp_pct": combo["arm"].tp_pct,
            "sl_pct": combo["arm"].sl_pct,
        },
        "overall": {
            "n": int(len(df)),
            "win_rate": float(df["win"].mean()),
            "profit_factor": pf(df["pnl"].to_numpy()),
            "frac_wrong_way_1h": float((df["signed_fwd_1"] < 0).mean()),
            "frac_wrong_way_3h": float((df["signed_fwd_3"] < 0).mean()),
            "frac_exit_max_hold": float((df["exit_reason"] == "max_hold").mean()),
            "frac_exit_stop": float(
                df["exit_reason"].isin(["stop", "stop_entry_bar"]).mean()
            ),
        },
        "book1_or_all": {
            "n": int(len(book1)),
            "win_rate": float(book1["win"].mean()) if len(book1) else float("nan"),
            "profit_factor": pf(book1["pnl"].to_numpy()) if len(book1) else float("nan"),
            "frac_wrong_way_1h": float((book1["signed_fwd_1"] < 0).mean())
            if len(book1)
            else float("nan"),
        },
        "by_book_idx": _bucket(rowdicts, "book_idx") if mode == "multitrade" else None,
        "by_strength_tercile": _bucket(rowdicts, "strength_tercile"),
        "exit_reasons": {
            str(k): int(v) for k, v in df["exit_reason"].value_counts().to_dict().items()
        },
        "loser_exits": {
            str(k): int(v) for k, v in los["exit_reason"].value_counts().to_dict().items()
        },
        "same_side_clusters_ge3_within_6h": _cluster_all_loss_frac(df),
        "interpretation_note": (
            "same_side all-loss clusters are rare when frac_all_loss << 0.5; "
            "most multi-entry bursts are NOT everyone-wrong-together"
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Optional subset of combo keys",
    )
    args = ap.parse_args()
    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")

    combos = COMBOS
    if args.only:
        want = set(args.only)
        combos = tuple(c for c in COMBOS if c["key"] in want)
        if not combos:
            raise SystemExit(f"no combos matched {args.only}")

    results = [analyse_combo(c) for c in combos]

    # Cross-pack headline: is ETH mt book1 weaker than BTC/SOL single?
    cross: dict[str, Any] = {}
    by_key = {r["key"]: r for r in results if "error" not in r}
    if "eth_multitrade_v1_1" in by_key:
        mt_b1 = by_key["eth_multitrade_v1_1"]["book1_or_all"]
        cross["eth_mt_book1_wrong_1h"] = mt_b1["frac_wrong_way_1h"]
        cross["eth_mt_book1_pf"] = mt_b1["profit_factor"]
        for k in ("btc_live_single", "eth_live_single", "sol_live_single"):
            if k not in by_key:
                continue
            o = by_key[k]["overall"]
            cross[f"{k}_wrong_1h"] = o["frac_wrong_way_1h"]
            cross[f"{k}_pf"] = o["profit_factor"]
            cross[f"{k}_vs_mt_book1_wrong_delta"] = (
                float(o["frac_wrong_way_1h"]) - float(mt_b1["frac_wrong_way_1h"])
            )

    findings = []
    if cross:
        findings.append(
            "ETH multitrade book1 wrong@1h="
            f"{cross.get('eth_mt_book1_wrong_1h', float('nan')):.1%} "
            f"PF={cross.get('eth_mt_book1_pf', float('nan')):.2f}"
        )
        for k in ("btc_live_single", "eth_live_single", "sol_live_single"):
            if f"{k}_wrong_1h" in cross:
                findings.append(
                    f"{k} wrong@1h={cross[f'{k}_wrong_1h']:.1%} "
                    f"PF={cross[f'{k}_pf']:.2f} "
                    f"(delta vs mt book1 wrong="
                    f"{cross[f'{k}_vs_mt_book1_wrong_delta']:+.1%})"
                )
    for r in results:
        if "error" in r:
            continue
        cl = r["same_side_clusters_ge3_within_6h"]
        findings.append(
            f"{r['key']}: all-loss clusters "
            f"{int(cl['n_all_loss'])}/{int(cl['n_clusters'])} "
            f"({cl['frac_all_loss']:.1%} of clusters) — "
            "NOT the usual mode when this fraction is low"
        )

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": stamp,
            "evidence_class": "MEASURE_DIAGNOSTIC",
            "max_readiness": "RESEARCH_ONLY",
            "promotion": False,
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "conformance_passed": bool(conf.get("passed")),
            "findings": findings,
            "cross_pack": cross,
            "packs": results,
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "cluster_plain_english": (
                "Same-side clusters (≥3 entries within 6 hours) going entirely "
                "to loss are uncommon (~single-digit percent of such clusters on "
                "ETH multitrade). Most of the time a burst of same-side entries "
                "is NOT an everyone-wrong-together wipeout."
            ),
        }
    )
    out = ARTIFACTS / "reports" / f"{GEN}_latest.json"
    out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (ARTIFACTS / "reports" / f"{GEN}_{stamp}.json").write_text(
        out.read_text(encoding="utf-8"), encoding="utf-8"
    )
    print(json.dumps({"findings": findings, "cross_pack": cross}, indent=2))
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
