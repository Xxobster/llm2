"""Diagnostic: why ETH multitrade signals fail — especially under stack depth.

Evidence class: MEASURE_DIAGNOSTIC (outer folds only; lockbox unused).
Frozen arm = live eth_multitrade_v1_1 knobs. Does NOT retune or promote.

Questions answered:
  1) Win rate / profit factor by book index (stack position at entry)
  2) Same metrics by concurrent open books on that side at entry
  3) Signed forward return after entry (did price move with the signal?)
  4) Exit-reason mix by book / stack
  5) |mean| strength vs outcome within stack buckets
  6) Cluster losses: consecutive same-side add-ons that all lose
"""

from __future__ import annotations

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
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.live.multitrade import (  # noqa: E402
    MEAN_LOOKBACK,
    book_tp_hold,
    mean_strength_ok,
    parse_multitrade_config,
)
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    build_outer_folds,
    index_to_ms,
)

MIN_EDGE = DIRECTION_BAND


def build_multitrade_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    mean: np.ndarray,
    *,
    cfg: dict[str, Any],
) -> tuple[list[Signal], dict[str, Any]]:
    """Recreate live multitrade gate (addon clarity, fib book tiers)."""
    cap = int(cfg["max_positions_per_side"])
    clarity = str(cfg.get("clarity", "none"))
    scope = str(cfg.get("clarity_scope", "addon"))
    lookback = int(cfg.get("mean_lookback", MEAN_LOOKBACK))
    bar_ms = int(cfg.get("bar_ms", 3_600_000))
    open_exit: dict[int, list[int]] = {1: [], -1: []}
    strength_hist: list[float] = []
    out: list[Signal] = []
    stats = {
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_cap": 0,
        "n_primary": 0,
        "n_addon": 0,
    }
    for i in range(len(ts_ms)):
        s = int(side[i])
        m = float(mean[i])
        if s == 0 or not np.isfinite(m) or abs(m) < MIN_EDGE:
            continue
        ts = int(ts_ms[i])
        open_exit[s] = [e for e in open_exit[s] if int(e) > ts]
        n_open = len(open_exit[s])
        is_addon = n_open >= 1
        abs_m = abs(m)
        recent = strength_hist[-lookback:] if strength_hist else []
        apply_clarity = clarity == "mean_strength" and (
            scope == "all" or (scope == "addon" and is_addon)
        )
        if apply_clarity and not mean_strength_ok(abs_m, recent):
            stats["n_skipped_clarity"] += 1
            strength_hist.append(abs_m)
            continue
        if n_open >= cap:
            stats["n_skipped_cap"] += 1
            strength_hist.append(abs_m)
            continue
        book_idx = n_open + 1
        tp, hold = book_tp_hold(
            book_idx,
            fib_ext=float(cfg["fib_ext"]),
            hold_addon=int(cfg["hold_addon"]),
            base_tp=float(cfg["base_tp"]),
            base_hold=int(cfg["base_hold"]),
            uniform_books=bool(cfg.get("uniform_books", False)),
        )
        if book_idx == 1:
            stats["n_primary"] += 1
        else:
            stats["n_addon"] += 1
        out.append(
            Signal(
                ts_ms=ts,
                side=Side.LONG if s > 0 else Side.SHORT,
                stop_offset=float(cfg["base_sl"]),
                target_offset=float(tp),
                max_hold_bars=int(hold),
                tag=f"k{cap}_b{book_idx}",
                meta={"book_idx": book_idx, "tp_pct": tp, "hold": hold},
            )
        )
        open_exit[s].append(ts + int(hold) * bar_ms)
        strength_hist.append(abs_m)
        stats["n_emitted"] += 1
    return out, stats

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
LABEL_HORIZON = 6
K = 7
SL = 0.02
GEN = "structure_v1_eth_multitrade_failure_modes_001"
PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_v1_1"
FWD_BARS = (1, 3, 6, 12)


def _pf(pnls: np.ndarray) -> float:
    a = np.asarray(pnls, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return float("nan")
    gp = float(a[a > 0].sum())
    gl = float((-a[a < 0]).sum())
    if gl <= 0:
        return float("inf") if gp > 0 else float("nan")
    return gp / gl


def _bucket_summary(rows: list[dict[str, Any]], key: str) -> dict[str, Any]:
    groups: dict[Any, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        groups[r[key]].append(r)
    out: dict[str, Any] = {}
    for k, grp in sorted(groups.items(), key=lambda x: (str(type(x[0])), x[0])):
        pnls = np.asarray([g["pnl"] for g in grp], dtype=float)
        wins = pnls > 0
        adverse1 = np.asarray([g["signed_fwd_1"] for g in grp], dtype=float)
        adverse3 = np.asarray([g["signed_fwd_3"] for g in grp], dtype=float)
        out[str(k)] = {
            "n": int(len(grp)),
            "win_rate": float(np.mean(wins)) if len(grp) else float("nan"),
            "profit_factor": _pf(pnls),
            "mean_pnl": float(np.mean(pnls)) if len(grp) else float("nan"),
            "frac_wrong_way_1h": float(np.mean(adverse1 < 0)) if len(grp) else float("nan"),
            "frac_wrong_way_3h": float(np.mean(adverse3 < 0)) if len(grp) else float("nan"),
            "mean_signed_fwd_1h": float(np.nanmean(adverse1)) if len(grp) else float("nan"),
            "mean_signed_fwd_3h": float(np.nanmean(adverse3)) if len(grp) else float("nan"),
            "mean_abs_mean": float(np.nanmean([g["abs_mean"] for g in grp])),
            "exit_reasons": {
                str(reason): int(sum(1 for g in grp if g["exit_reason"] == reason))
                for reason in sorted({g["exit_reason"] for g in grp})
            },
        }
    return out


def _signed_fwd(
    close: np.ndarray, entry_i: int, side: int, horizons: tuple[int, ...]
) -> dict[str, float]:
    """Return side-signed close-to-close forward returns (positive = with signal)."""
    n = int(close.size)
    out: dict[str, float] = {}
    px0 = float(close[entry_i])
    if not np.isfinite(px0) or px0 <= 0:
        for h in horizons:
            out[f"signed_fwd_{h}"] = float("nan")
        return out
    sign = float(side)
    for h in horizons:
        j = entry_i + int(h)
        if j >= n:
            out[f"signed_fwd_{h}"] = float("nan")
            continue
        px1 = float(close[j])
        out[f"signed_fwd_{h}"] = sign * (px1 / px0 - 1.0)
    return out


def _realized_vol(close: np.ndarray, i: int, lookback: int = 24) -> float:
    if i < 2:
        return float("nan")
    a = close[max(0, i - lookback) : i + 1]
    if a.size < 3:
        return float("nan")
    r = np.diff(np.log(np.asarray(a, dtype=float)))
    r = r[np.isfinite(r)]
    if r.size < 2:
        return float("nan")
    return float(np.std(r) * np.sqrt(24.0))


def main() -> int:
    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")

    pack_strat = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    cfg = parse_multitrade_config(pack_strat)
    if not cfg:
        raise SystemExit("pack is not multitrade")
    cfg["max_positions_per_side"] = K
    cfg["fib_ext"] = float((pack_strat.get("multitrade") or {}).get("fib_ext", 1.618))
    cfg["hold_addon"] = int((pack_strat.get("multitrade") or {}).get("hold_addon", 12))
    cfg["base_hold"] = int((pack_strat.get("multitrade") or {}).get("base_hold", 6))
    cfg["base_tp"] = 0.01
    cfg["base_sl"] = 0.02
    cfg["clarity"] = "mean_strength"
    cfg["clarity_scope"] = str(
        (pack_strat.get("multitrade") or {}).get("clarity_scope") or "addon"
    )
    cfg["uniform_books"] = False

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
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

    # Full-series close indexed by decision bar for forward returns
    full_close = ohlcv["close"].to_numpy(dtype=float)
    full_ts = index_to_ms(ohlcv.index)
    ts_to_i = {int(t): i for i, t in enumerate(full_ts)}

    trade_rows: list[dict[str, Any]] = []
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        sigs, stats = build_multitrade_signals(oos_ts, side, mean, cfg=cfg)
        # Map signal timestamp → book / mean for join onto closed trades
        sig_meta = {
            int(s.ts_ms): {
                "book_idx": int((s.meta or {}).get("book_idx", 0) or 0),
                "tag": str(getattr(s, "tag", "") or ""),
                "tp": float(s.target_offset),
                "hold": int(s.max_hold_bars or 0),
            }
            for s in sigs
        }
        mean_by_ts = {int(oos_ts[i]): float(mean[i]) for i in range(len(oos_ts))}
        side_by_ts = {int(oos_ts[i]): int(side[i]) for i in range(len(oos_ts))}

        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, int(cfg["hold_addon"]) * 4)
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
            symbol=SYMBOL,
            timeframe=TIMEFRAME,
            strategy_id=f"mt-fail-f{fold.fold_index}",
            touch_ohlcv=touch_win,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_hedge(
                max_hold_bars=int(cfg["hold_addon"]),
                decision_timeframe=TIMEFRAME,
                max_positions_per_side=K,
                max_positions_per_symbol=K * 2,
            ),
            instrument=instrument,
            funding_ts_ms=funding_ts[fmask],
            funding_rate=funding_rt[fmask],
            strategy_meta={"name": GEN, "k": K},
            plot=False,
            print_headline=False,
            store_path=None,
        )

        # Reconstruct concurrent open counts chronologically from closed trades
        # (entry_ts → exit_ts). Approximate stack depth at each entry.
        trades = list(bundle.result.trades)
        events: list[tuple[int, int, int]] = []  # (ts, +1/-1 open, side)
        for t in trades:
            s = int(getattr(t.side, "value", t.side))
            events.append((int(t.entry_ts_ms), +1, s))
            events.append((int(t.exit_ts_ms), -1, s))
        events.sort(key=lambda e: (e[0], -e[1]))  # opens before closes at same ts
        open_l = 0
        open_s = 0
        # Precompute open count just before each entry
        open_at_entry: dict[tuple[int, int], int] = {}
        open_opp_at_entry: dict[tuple[int, int], int] = {}
        for ts, delta, s in events:
            if delta > 0:
                same = open_l if s > 0 else open_s
                opp = open_s if s > 0 else open_l
                open_at_entry[(ts, s)] = int(same)
                open_opp_at_entry[(ts, s)] = int(opp)
            if s > 0:
                open_l += delta
            else:
                open_s += delta

        for t in trades:
            s = int(getattr(t.side, "value", t.side))
            ets = int(t.entry_ts_ms)
            meta = sig_meta.get(ets, {})
            book = int(meta.get("book_idx") or 0)
            if book <= 0:
                # Fall back to reconstructed open count + 1
                book = int(open_at_entry.get((ets, s), 0)) + 1
            m = float(mean_by_ts.get(ets, float("nan")))
            entry_i = ts_to_i.get(ets)
            fwds = (
                _signed_fwd(full_close, entry_i, s, FWD_BARS)
                if entry_i is not None
                else {f"signed_fwd_{h}": float("nan") for h in FWD_BARS}
            )
            pnl = float(getattr(t, "realized_pnl", 0.0) or 0.0)
            reason = str(getattr(t, "exit_reason", "") or "unknown")
            hour = int(pd.Timestamp(ets, unit="ms", tz="UTC").hour)
            vol = (
                _realized_vol(full_close, entry_i)
                if entry_i is not None
                else float("nan")
            )
            row = {
                "fold": int(fold.fold_index),
                "entry_ts_ms": ets,
                "side": int(s),
                "book_idx": int(book),
                "stack_same_before": int(open_at_entry.get((ets, s), max(0, book - 1))),
                "stack_opp_before": int(open_opp_at_entry.get((ets, s), 0)),
                "abs_mean": abs(m) if np.isfinite(m) else float("nan"),
                "pred_mean": m,
                "pnl": pnl,
                "win": bool(pnl > 0),
                "exit_reason": reason,
                "entry_price": float(getattr(t, "entry_price", float("nan"))),
                "exit_price": float(getattr(t, "exit_price", float("nan"))),
                "hour_utc": hour,
                "realized_vol_24h": vol,
                "is_addon": bool(book >= 2),
                "signed_fwd_1": fwds.get("signed_fwd_1", float("nan")),
                "signed_fwd_3": fwds.get("signed_fwd_3", float("nan")),
                "signed_fwd_6": fwds.get("signed_fwd_6", float("nan")),
                "signed_fwd_12": fwds.get("signed_fwd_12", float("nan")),
                "signal_stats_fold": stats,
            }
            trade_rows.append(row)
        print(
            f"fold {fold.fold_index}: trades={len(trades)} signals={stats['n_emitted']} "
            f"clarity_skip={stats['n_skipped_clarity']} cap_skip={stats['n_skipped_cap']}",
            flush=True,
        )

    if not trade_rows:
        raise SystemExit("no trades — cannot analyse")

    df = pd.DataFrame(trade_rows)
    # Strength terciles within sample (diagnostic only)
    am = df["abs_mean"].to_numpy(dtype=float)
    finite = np.isfinite(am)
    q = np.nanquantile(am[finite], [1 / 3, 2 / 3]) if finite.any() else np.array([0.0, 0.0])
    df["strength_tercile"] = np.where(
        ~finite,
        "na",
        np.where(am <= q[0], "low", np.where(am <= q[1], "mid", "high")),
    )
    vol = df["realized_vol_24h"].to_numpy(dtype=float)
    vf = np.isfinite(vol)
    vq = np.nanquantile(vol[vf], [1 / 3, 2 / 3]) if vf.any() else np.array([0.0, 0.0])
    df["vol_tercile"] = np.where(
        ~vf,
        "na",
        np.where(vol <= vq[0], "low", np.where(vol <= vq[1], "mid", "high")),
    )

    rows = df.to_dict(orient="records")

    # Cluster: runs of same-side add-on entries within 6h that all lose
    cluster_loss = 0
    cluster_n = 0
    df_s = df.sort_values(["side", "entry_ts_ms"])
    for side_v, g in df_s.groupby("side"):
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

    # Conditional: if stack already ≥3 and next add-on — how often wrong-way?
    deep = df[df["stack_same_before"] >= 3]
    shallow = df[df["stack_same_before"] <= 1]

    # Short-specific wrong-way (user asked about sells that don't go down)
    shorts = df[df["side"] < 0]
    longs = df[df["side"] > 0]

    summary = {
        "overall": {
            "n": int(len(df)),
            "win_rate": float(df["win"].mean()),
            "profit_factor": _pf(df["pnl"].to_numpy()),
            "frac_wrong_way_1h": float((df["signed_fwd_1"] < 0).mean()),
            "frac_wrong_way_3h": float((df["signed_fwd_3"] < 0).mean()),
            "frac_wrong_way_6h": float((df["signed_fwd_6"] < 0).mean()),
            "mean_signed_fwd_1h": float(df["signed_fwd_1"].mean()),
            "mean_signed_fwd_3h": float(df["signed_fwd_3"].mean()),
        },
        "by_book_idx": _bucket_summary(rows, "book_idx"),
        "by_stack_same_before": _bucket_summary(rows, "stack_same_before"),
        "by_side": _bucket_summary(rows, "side"),
        "by_strength_tercile": _bucket_summary(rows, "strength_tercile"),
        "by_vol_tercile": _bucket_summary(rows, "vol_tercile"),
        "by_is_addon": _bucket_summary(rows, "is_addon"),
        "exit_reasons_overall": {
            str(k): int(v) for k, v in df["exit_reason"].value_counts().to_dict().items()
        },
        "deep_stack_ge3_vs_shallow_le1": {
            "deep_n": int(len(deep)),
            "deep_wr": float(deep["win"].mean()) if len(deep) else float("nan"),
            "deep_pf": _pf(deep["pnl"].to_numpy()) if len(deep) else float("nan"),
            "deep_wrong_1h": float((deep["signed_fwd_1"] < 0).mean()) if len(deep) else float("nan"),
            "shallow_n": int(len(shallow)),
            "shallow_wr": float(shallow["win"].mean()) if len(shallow) else float("nan"),
            "shallow_pf": _pf(shallow["pnl"].to_numpy()) if len(shallow) else float("nan"),
            "shallow_wrong_1h": float((shallow["signed_fwd_1"] < 0).mean())
            if len(shallow)
            else float("nan"),
        },
        "shorts_vs_longs": {
            "short_n": int(len(shorts)),
            "short_wr": float(shorts["win"].mean()) if len(shorts) else float("nan"),
            "short_pf": _pf(shorts["pnl"].to_numpy()) if len(shorts) else float("nan"),
            "short_wrong_1h": float((shorts["signed_fwd_1"] < 0).mean())
            if len(shorts)
            else float("nan"),
            "short_wrong_3h": float((shorts["signed_fwd_3"] < 0).mean())
            if len(shorts)
            else float("nan"),
            "long_n": int(len(longs)),
            "long_wr": float(longs["win"].mean()) if len(longs) else float("nan"),
            "long_pf": _pf(longs["pnl"].to_numpy()) if len(longs) else float("nan"),
            "long_wrong_1h": float((longs["signed_fwd_1"] < 0).mean())
            if len(longs)
            else float("nan"),
            "long_wrong_3h": float((longs["signed_fwd_3"] < 0).mean())
            if len(longs)
            else float("nan"),
        },
        "same_side_clusters_ge3_within_6h": {
            "n_clusters": int(cluster_n),
            "n_all_loss_clusters": int(cluster_loss),
            "frac_all_loss": float(cluster_loss / cluster_n) if cluster_n else float("nan"),
        },
        # Interaction: deep stack × low strength
        "interaction_deep_x_strength": {
            f"stack>={3}_strength={st}": {
                "n": int(len(sub)),
                "win_rate": float(sub["win"].mean()) if len(sub) else float("nan"),
                "profit_factor": _pf(sub["pnl"].to_numpy()) if len(sub) else float("nan"),
                "frac_wrong_way_1h": float((sub["signed_fwd_1"] < 0).mean())
                if len(sub)
                else float("nan"),
            }
            for st in ("low", "mid", "high")
            for sub in [df[(df["stack_same_before"] >= 3) & (df["strength_tercile"] == st)]]
        },
    }

    # Headline findings (auto-generated, diagnostic)
    findings: list[str] = []
    b1 = summary["by_book_idx"].get("1", {})
    b_deep = summary["by_book_idx"].get("5") or summary["by_book_idx"].get("6") or {}
    if b1 and b_deep and b1.get("n", 0) >= 30 and b_deep.get("n", 0) >= 20:
        findings.append(
            f"Book1 WR={b1.get('win_rate', float('nan')):.1%} PF={b1.get('profit_factor', float('nan')):.2f} "
            f"vs deep-book WR={b_deep.get('win_rate', float('nan')):.1%} "
            f"PF={b_deep.get('profit_factor', float('nan')):.2f}"
        )
    ds = summary["deep_stack_ge3_vs_shallow_le1"]
    findings.append(
        f"Shallow stack(≤1) wrong-way@1h={ds['shallow_wrong_1h']:.1%} WR={ds['shallow_wr']:.1%} "
        f"| Deep stack(≥3) wrong-way@1h={ds['deep_wrong_1h']:.1%} WR={ds['deep_wr']:.1%}"
    )
    sl = summary["shorts_vs_longs"]
    findings.append(
        f"Shorts wrong-way@1h={sl['short_wrong_1h']:.1%} @3h={sl['short_wrong_3h']:.1%} "
        f"WR={sl['short_wr']:.1%} PF={sl['short_pf']:.2f} | "
        f"Longs wrong-way@1h={sl['long_wrong_1h']:.1%} WR={sl['long_wr']:.1%} PF={sl['long_pf']:.2f}"
    )
    cl = summary["same_side_clusters_ge3_within_6h"]
    findings.append(
        f"Same-side clusters (≥3 entries within 6h): {cl['n_all_loss_clusters']}/{cl['n_clusters']} "
        f"({cl['frac_all_loss']:.1%}) are all-loss clusters"
    )

    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
            "evidence_class": "MEASURE_DIAGNOSTIC",
            "max_readiness": "RESEARCH_ONLY",
            "promotion": False,
            "symbol": SYMBOL,
            "timeframe": TIMEFRAME,
            "pack": str(PACK.relative_to(_ROOT)),
            "geometry": {
                "k": K,
                "clarity": cfg["clarity"],
                "clarity_scope": cfg["clarity_scope"],
                "fib_ext": cfg["fib_ext"],
                "hold_addon": cfg["hold_addon"],
                "base_hold": cfg["base_hold"],
            },
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "conformance_passed": bool(conf.get("passed")),
            "leakage_recheck_ref": "artifacts/reports/structure_v1_leakage_recheck_20260804T144240Z.json",
            "definitions": {
                "wrong_way_Nh": (
                    "side-signed close-to-close return over N hours after the decision bar; "
                    "negative means price moved against the signal (short but price up, or long but price down)"
                ),
                "stack_same_before": "number of same-side open books already open at entry timestamp",
                "book_idx": "1-based stack position assigned by the live multitrade gate",
            },
            "findings": findings,
            "summary": summary,
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "note": (
                "Diagnostic only. Do not promote filters discovered here without a "
                "pre-registered nested settle. MIN_EXCHANGE dust caveat applies to PnL/PF."
            ),
        }
    )

    out_dir = ARTIFACTS / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = report["created_utc"]
    latest = out_dir / f"{GEN}_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (out_dir / f"{GEN}_{stamp}.json").write_text(latest.read_text(encoding="utf-8"), encoding="utf-8")

    # Compact trade table for follow-up (parquet if available, else csv)
    trades_path = out_dir / f"{GEN}_trades_{stamp}.csv"
    df.drop(columns=["signal_stats_fold"], errors="ignore").to_csv(trades_path, index=False)
    report["trades_csv"] = str(trades_path.relative_to(_ROOT))
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")

    print(json.dumps({"findings": findings, "overall": summary["overall"]}, indent=2))
    print(f"wrote {latest}")
    print(f"trades {trades_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
