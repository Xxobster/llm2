"""Chronological win/loss streak autopsy helpers (pre-lockbox diagnostics).

Does not train or promote strategies. Evidence class MEASURE_DIAGNOSTIC when used
by the fleet runner. Streak sort is by exit_ts_ms (then entry_ts_ms, trade_id).
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Iterable, Mapping, Sequence

import numpy as np
import pandas as pd

FWD_BARS = (1, 3, 6, 12)
DEFAULT_STREAK_N = 4


def _as_trade_frame(trades: Sequence[Mapping[str, Any]] | pd.DataFrame) -> pd.DataFrame:
    if isinstance(trades, pd.DataFrame):
        df = trades.copy()
    else:
        df = pd.DataFrame(list(trades))
    if df.empty:
        return df
    for col in ("exit_ts_ms", "entry_ts_ms", "pnl"):
        if col not in df.columns:
            raise ValueError(f"trades require column {col!r}")
    if "win" not in df.columns:
        df["win"] = df["pnl"].astype(float) > 0.0
    if "loss" not in df.columns:
        df["loss"] = df["pnl"].astype(float) < 0.0
    # flats (pnl==0) break both win and loss streaks
    df["outcome"] = np.where(
        df["pnl"].astype(float) > 0.0,
        1,
        np.where(df["pnl"].astype(float) < 0.0, -1, 0),
    )
    sort_cols = ["exit_ts_ms", "entry_ts_ms"]
    if "trade_id" in df.columns:
        sort_cols.append("trade_id")
    return df.sort_values(sort_cols).reset_index(drop=True)


def chronological_streaks(
    trades: Sequence[Mapping[str, Any]] | pd.DataFrame,
    *,
    min_streak: int = DEFAULT_STREAK_N,
    group_cols: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Compute consecutive win/loss stats ordered by closed-trade chronology.

    Parameters
    ----------
    min_streak
        Report individual streak events only when length >= this value.
    group_cols
        If set (e.g. ['side'] or ['book_idx']), compute streaks within groups
        then aggregate headline max across groups into ``by_group``.
    """
    df = _as_trade_frame(trades)
    if df.empty:
        return {
            "n_trades": 0,
            "max_loss_streak": 0,
            "max_win_streak": 0,
            "mean_loss_streak": float("nan"),
            "mean_win_streak": float("nan"),
            "p95_loss_streak": float("nan"),
            "p95_win_streak": float("nan"),
            "loss_streak_hist": {},
            "win_streak_hist": {},
            "loss_streaks_ge_n": [],
            "win_streaks_ge_n": [],
            "by_group": None,
            "min_streak": int(min_streak),
        }

    def _one(sub: pd.DataFrame) -> dict[str, Any]:
        outcomes = sub["outcome"].to_numpy(dtype=int)
        loss_lens: list[int] = []
        win_lens: list[int] = []
        loss_events: list[dict[str, Any]] = []
        win_events: list[dict[str, Any]] = []
        i = 0
        n = len(outcomes)
        while i < n:
            o = int(outcomes[i])
            if o == 0:
                i += 1
                continue
            j = i
            while j + 1 < n and int(outcomes[j + 1]) == o:
                j += 1
            length = j - i + 1
            start_row = sub.iloc[i]
            end_row = sub.iloc[j]
            event = {
                "length": int(length),
                "start_exit_ts_ms": int(start_row["exit_ts_ms"]),
                "end_exit_ts_ms": int(end_row["exit_ts_ms"]),
                "start_entry_ts_ms": int(start_row["entry_ts_ms"]),
                "end_entry_ts_ms": int(end_row["entry_ts_ms"]),
                "n_trades": int(length),
                "sum_pnl": float(sub.iloc[i : j + 1]["pnl"].astype(float).sum()),
            }
            if o < 0:
                loss_lens.append(length)
                if length >= int(min_streak):
                    loss_events.append(event)
            else:
                win_lens.append(length)
                if length >= int(min_streak):
                    win_events.append(event)
            i = j + 1

        def _stats(lens: list[int]) -> dict[str, Any]:
            if not lens:
                return {
                    "max": 0,
                    "mean": float("nan"),
                    "p95": float("nan"),
                    "hist": {},
                }
            arr = np.asarray(lens, dtype=float)
            hist = {str(int(k)): int(v) for k, v in sorted(Counter(lens).items())}
            return {
                "max": int(arr.max()),
                "mean": float(arr.mean()),
                "p95": float(np.quantile(arr, 0.95)),
                "hist": hist,
            }

        ls = _stats(loss_lens)
        ws = _stats(win_lens)
        return {
            "n_trades": int(len(sub)),
            "max_loss_streak": ls["max"],
            "max_win_streak": ws["max"],
            "mean_loss_streak": ls["mean"],
            "mean_win_streak": ws["mean"],
            "p95_loss_streak": ls["p95"],
            "p95_win_streak": ws["p95"],
            "loss_streak_hist": ls["hist"],
            "win_streak_hist": ws["hist"],
            "loss_streaks_ge_n": loss_events,
            "win_streaks_ge_n": win_events,
            "min_streak": int(min_streak),
        }

    overall = _one(df)
    overall["by_group"] = None
    if group_cols:
        present = [c for c in group_cols if c in df.columns]
        if present:
            by_g: dict[str, Any] = {}
            for key, g in df.groupby(list(present), dropna=False):
                label = key if not isinstance(key, tuple) else "|".join(str(x) for x in key)
                by_g[str(label)] = _one(g.reset_index(drop=True))
            overall["by_group"] = by_g
    return overall


def annotate_trades_with_preds(
    trades: Sequence[Mapping[str, Any]] | pd.DataFrame,
    *,
    pred_ts_ms: np.ndarray,
    pred_mean: np.ndarray,
    pred_side: np.ndarray | None = None,
) -> pd.DataFrame:
    """Left-join pred_mean (and optional side) onto trades by entry_ts_ms."""
    df = _as_trade_frame(trades)
    if df.empty:
        return df
    pts = np.asarray(pred_ts_ms, dtype=np.int64)
    pmean = np.asarray(pred_mean, dtype=float)
    mean_map = {int(t): float(m) for t, m in zip(pts, pmean)}
    df["pred_mean"] = df["entry_ts_ms"].map(lambda t: mean_map.get(int(t), float("nan")))
    df["abs_mean"] = df["pred_mean"].abs()
    if pred_side is not None:
        pside = np.asarray(pred_side, dtype=int)
        side_map = {int(t): int(s) for t, s in zip(pts, pside)}
        df["pred_side"] = df["entry_ts_ms"].map(lambda t: side_map.get(int(t), 0))
    return df


def signed_forward_returns(
    close: np.ndarray,
    ts_ms: np.ndarray,
    *,
    entry_ts_ms: int,
    side: int,
    horizons: Sequence[int] = FWD_BARS,
) -> dict[str, float]:
    """Signed close→close returns after entry (positive = favorable)."""
    ts = np.asarray(ts_ms, dtype=np.int64)
    c = np.asarray(close, dtype=float)
    out: dict[str, float] = {}
    idx = int(np.searchsorted(ts, int(entry_ts_ms)))
    if idx >= len(c) or int(ts[idx]) != int(entry_ts_ms):
        # nearest left if exact missing
        if idx > 0 and (idx >= len(ts) or int(ts[idx]) > int(entry_ts_ms)):
            idx -= 1
        if idx < 0 or idx >= len(c):
            return {f"signed_fwd_{h}": float("nan") for h in horizons}
    px0 = float(c[idx])
    sign = float(side)
    for h in horizons:
        j = idx + int(h)
        if not np.isfinite(px0) or px0 <= 0 or j >= len(c):
            out[f"signed_fwd_{h}"] = float("nan")
        else:
            out[f"signed_fwd_{h}"] = sign * (float(c[j]) / px0 - 1.0)
    return out


def strength_tercile_labels(abs_mean: np.ndarray) -> np.ndarray:
    am = np.asarray(abs_mean, dtype=float)
    finite = np.isfinite(am)
    labels = np.full(len(am), "na", dtype=object)
    if not finite.any():
        return labels
    q = np.nanquantile(am[finite], [1.0 / 3.0, 2.0 / 3.0])
    labels[finite] = np.where(
        am[finite] <= q[0],
        "low",
        np.where(am[finite] <= q[1], "mid", "high"),
    )
    return labels


def realized_vol_tercile(
    close: np.ndarray,
    ts_ms: np.ndarray,
    entry_ts_ms: np.ndarray,
    *,
    lookback: int = 24,
) -> np.ndarray:
    """Causal 24h-ish realized vol tercile at entry (uses past returns only)."""
    c = np.asarray(close, dtype=float)
    ts = np.asarray(ts_ms, dtype=np.int64)
    rets = np.zeros(len(c), dtype=float)
    rets[1:] = np.diff(np.log(np.clip(c, 1e-12, None)))
    # rolling std of past `lookback` returns ending at i-1
    vol = np.full(len(c), np.nan, dtype=float)
    if len(c) > lookback + 1:
        # vectorized rolling of past window
        window = lookback
        cum = np.cumsum(np.insert(rets**2, 0, 0.0))
        # sum of squares of rets[i-window:i] = cum[i] - cum[i-window]
        for i in range(window, len(c)):
            ss = cum[i] - cum[i - window]
            vol[i] = float(np.sqrt(ss / window))
    ts_to_i = {int(t): i for i, t in enumerate(ts)}
    out = np.full(len(entry_ts_ms), "na", dtype=object)
    vals = []
    idxs = []
    for j, ets in enumerate(np.asarray(entry_ts_ms, dtype=np.int64)):
        i = ts_to_i.get(int(ets))
        if i is None or not np.isfinite(vol[i]):
            continue
        vals.append(float(vol[i]))
        idxs.append(j)
    if not vals:
        return out
    arr = np.asarray(vals, dtype=float)
    q = np.quantile(arr, [1.0 / 3.0, 2.0 / 3.0])
    for j, v in zip(idxs, vals):
        if v <= q[0]:
            out[j] = "low"
        elif v <= q[1]:
            out[j] = "mid"
        else:
            out[j] = "high"
    return out


def recent_hit_rate_causal(
    trades: Sequence[Mapping[str, Any]] | pd.DataFrame,
    *,
    lookback_trades: int = 10,
) -> pd.Series:
    """Hit rate of prior closed trades only (strictly previous in exit order)."""
    df = _as_trade_frame(trades)
    if df.empty:
        return pd.Series(dtype=float)
    wins = df["win"].astype(float).to_numpy()
    out = np.full(len(df), np.nan, dtype=float)
    lb = max(1, int(lookback_trades))
    for i in range(len(df)):
        if i == 0:
            continue
        start = max(0, i - lb)
        out[i] = float(np.mean(wins[start:i]))
    return pd.Series(out, index=df.index, name="recent_hit_rate")


def regime_snapshot(row: Mapping[str, Any]) -> dict[str, Any]:
    """Compact regime keys for similarity mining."""
    hour = None
    if "entry_ts_ms" in row and row["entry_ts_ms"] is not None:
        hour = int(pd.Timestamp(int(row["entry_ts_ms"]), unit="ms", tz="UTC").hour)
    return {
        "side": int(row.get("side", 0) or 0),
        "book_idx": int(row.get("book_idx", 1) or 1),
        "strength_tercile": str(row.get("strength_tercile", "na")),
        "vol_tercile": str(row.get("vol_tercile", "na")),
        "hour_utc": hour,
        "exit_reason_family": _exit_family(str(row.get("exit_reason", "") or "")),
        "wrong_way_1h": bool(row.get("signed_fwd_1", 0) is not None and float(row.get("signed_fwd_1", 0) or 0) < 0)
        if row.get("signed_fwd_1") is not None and np.isfinite(float(row.get("signed_fwd_1", float("nan"))))
        else None,
        "funding_sign": int(row.get("funding_sign", 0) or 0),
    }


def _exit_family(reason: str) -> str:
    r = (reason or "").lower()
    if "stop" in r:
        return "stop"
    if "target" in r or r.startswith("tp"):
        return "target"
    if "hold" in r:
        return "max_hold"
    if "liq" in r:
        return "liquidation"
    return "other"


def _bucket_key(snap: Mapping[str, Any]) -> str:
    return (
        f"str={snap.get('strength_tercile')}"
        f"|vol={snap.get('vol_tercile')}"
        f"|side={snap.get('side')}"
        f"|book={snap.get('book_idx')}"
        f"|ex={snap.get('exit_reason_family')}"
        f"|ww1={snap.get('wrong_way_1h')}"
    )


def miscalibration_summary(df: pd.DataFrame, *, min_edge: float) -> dict[str, Any]:
    """High conviction losers + wrong-way rates (signal said 'go' but price adverse)."""
    if df.empty:
        return {"n": 0}
    am = df["abs_mean"].to_numpy(dtype=float) if "abs_mean" in df.columns else np.full(len(df), np.nan)
    gated = np.isfinite(am) & (am >= float(min_edge))
    losers = ~df["win"].to_numpy(dtype=bool)
    high = df["strength_tercile"].astype(str).eq("high") if "strength_tercile" in df.columns else pd.Series(False, index=df.index)
    ww1 = (
        df["signed_fwd_1"].to_numpy(dtype=float) < 0
        if "signed_fwd_1" in df.columns
        else np.zeros(len(df), dtype=bool)
    )
    stop = df["exit_reason"].astype(str).str.contains("stop", case=False, na=False) if "exit_reason" in df.columns else pd.Series(False, index=df.index)
    high_losers = high.to_numpy() & losers
    return {
        "n": int(len(df)),
        "frac_gated_go": float(np.mean(gated)) if len(df) else float("nan"),
        "frac_loss": float(np.mean(losers)),
        "frac_high_strength": float(high.mean()) if len(df) else float("nan"),
        "frac_high_strength_and_loss": float(np.mean(high_losers)),
        "frac_high_strength_loss_wrong_way_1h": float(
            np.mean(high_losers & ww1) / max(1, int(high_losers.sum()))
        )
        if high_losers.any()
        else float("nan"),
        "frac_high_strength_loss_stop": float(
            np.mean(high_losers & stop.to_numpy()) / max(1, int(high_losers.sum()))
        )
        if high_losers.any()
        else float("nan"),
        "frac_wrong_way_1h": float(np.mean(ww1)),
        "n_high_strength_losers": int(high_losers.sum()),
    }


def loss_streak_start_contexts(
    df: pd.DataFrame,
    streak_events: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Regime at the first trade of each loss streak ≥ N."""
    if df.empty or not streak_events:
        return []
    # map start_exit_ts + start_entry to row
    out: list[dict[str, Any]] = []
    for ev in streak_events:
        mask = (df["exit_ts_ms"] == int(ev["start_exit_ts_ms"])) & (
            df["entry_ts_ms"] == int(ev["start_entry_ts_ms"])
        )
        if not mask.any():
            continue
        row = df.loc[mask].iloc[0].to_dict()
        snap = regime_snapshot(row)
        out.append({**ev, "regime": snap, "bucket": _bucket_key(snap)})
    return out


def baseline_bucket_rates(df: pd.DataFrame) -> dict[str, dict[str, float]]:
    """Per-bucket entry share and loss rate for baseline comparison."""
    if df.empty:
        return {}
    snaps = [regime_snapshot(r) for r in df.to_dict(orient="records")]
    buckets = [_bucket_key(s) for s in snaps]
    losses = (~df["win"].astype(bool)).to_numpy()
    n = len(df)
    counts: dict[str, list[bool]] = defaultdict(list)
    for b, loss in zip(buckets, losses):
        counts[b].append(bool(loss))
    out: dict[str, dict[str, float]] = {}
    for b, flags in counts.items():
        out[b] = {
            "n": float(len(flags)),
            "share": float(len(flags) / n),
            "loss_rate": float(np.mean(flags)),
        }
    return out


def pack_dossier(
    *,
    version_id: str,
    symbol: str,
    geometry: Mapping[str, Any],
    trades_df: pd.DataFrame,
    streaks: Mapping[str, Any],
    miscal: Mapping[str, Any],
    min_streak: int = DEFAULT_STREAK_N,
) -> dict[str, Any]:
    """Per-pack structured autopsy for LLM / human review."""
    df = trades_df.copy() if not trades_df.empty else trades_df
    pain = 0.0
    if streaks:
        max_loss = float(streaks.get("max_loss_streak") or 0)
        n_ge = float(len(streaks.get("loss_streaks_ge_n") or []))
        high_loss = float(miscal.get("frac_high_strength_and_loss") or 0)
        pain = max_loss * 1.0 + n_ge * 0.5 + high_loss * 20.0
    starts = loss_streak_start_contexts(df, list(streaks.get("loss_streaks_ge_n") or []))
    base = baseline_bucket_rates(df) if not df.empty else {}
    # elevate buckets that appear often at streak starts
    start_counts = Counter(s["bucket"] for s in starts)
    elevated = []
    for b, cnt in start_counts.most_common(20):
        br = base.get(b, {})
        expected = float(br.get("share", 0.0)) * max(1.0, float(len(starts)))
        elevated.append(
            {
                "bucket": b,
                "n_streak_starts": int(cnt),
                "baseline_share": float(br.get("share", float("nan"))),
                "baseline_loss_rate": float(br.get("loss_rate", float("nan"))),
                "lift_vs_share": float(cnt / expected) if expected > 0 else float("nan"),
            }
        )
    return {
        "version_id": version_id,
        "symbol": symbol,
        "geometry": dict(geometry),
        "pain_score": float(pain),
        "streaks": dict(streaks),
        "miscalibration": dict(miscal),
        "loss_streak_start_contexts": starts[:50],
        "elevated_loss_streak_buckets": elevated[:15],
        "baseline_bucket_rates_top": sorted(
            ({"bucket": k, **v} for k, v in base.items()),
            key=lambda x: -float(x.get("n") or 0),
        )[:15],
        "min_streak": int(min_streak),
        "n_trades": int(len(df)),
    }


def cross_pack_similarity(
    dossiers: Sequence[Mapping[str, Any]],
    *,
    min_packs: int = 2,
    min_starts: int = 2,
) -> list[dict[str, Any]]:
    """Buckets co-occurring in loss-streak starts across ≥min_packs packs."""
    pack_buckets: dict[str, set[str]] = defaultdict(set)
    pack_counts: dict[str, Counter] = defaultdict(Counter)
    for d in dossiers:
        vid = str(d.get("version_id") or "")
        for row in d.get("elevated_loss_streak_buckets") or []:
            b = str(row.get("bucket") or "")
            n = int(row.get("n_streak_starts") or 0)
            if not b or n < min_starts:
                continue
            pack_buckets[b].add(vid)
            pack_counts[b][vid] = n
    out: list[dict[str, Any]] = []
    for b, packs in pack_buckets.items():
        if len(packs) < int(min_packs):
            continue
        out.append(
            {
                "bucket": b,
                "n_packs": int(len(packs)),
                "packs": sorted(packs),
                "starts_by_pack": dict(pack_counts[b]),
                "total_starts": int(sum(pack_counts[b].values())),
            }
        )
    out.sort(key=lambda r: (-int(r["n_packs"]), -int(r["total_starts"])))
    return out


def rank_packs_by_pain(dossiers: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    rows = [
        {
            "version_id": d.get("version_id"),
            "symbol": d.get("symbol"),
            "pain_score": float(d.get("pain_score") or 0.0),
            "max_loss_streak": int((d.get("streaks") or {}).get("max_loss_streak") or 0),
            "n_loss_streaks_ge_n": int(len((d.get("streaks") or {}).get("loss_streaks_ge_n") or [])),
            "n_trades": int(d.get("n_trades") or 0),
            "geometry": d.get("geometry"),
        }
        for d in dossiers
        if int(d.get("n_trades") or 0) > 0
    ]
    rows.sort(key=lambda r: (-float(r["pain_score"]), -int(r["max_loss_streak"])))
    return rows


def offline_llm_proposals(fleet_summary: Mapping[str, Any]) -> dict[str, Any]:
    """Deterministic analyst template when Ollama is unavailable.

    Proposes ≤5 frozen testable gate arms — never OOS-tuned.
    """
    pain = list(fleet_summary.get("pain_rank") or [])
    top = pain[0] if pain else {}
    shared = list(fleet_summary.get("cross_pack_loss_streak_buckets") or [])[:5]
    vid = str(top.get("version_id") or "unknown")
    geom = top.get("geometry") or {}
    proposals = [
        {
            "id": 1,
            "type": "execution_gate",
            "name": "loss_streak_cooloff_3",
            "control_version_id": vid,
            "candidate_knobs": {
                "cooloff_after_consecutive_losses": 3,
                "cooloff_scope": "all_sides_pooled",
            },
            "rationale": (
                "Pause new entries after 3 closed consecutive losses (causal: only "
                "trades with exit before decision). Cuts churn during loss runs "
                f"that hurt {vid}."
            ),
            "economic": "Avoid stacking books while the model is in a temporary failure mode.",
            "forbidden": ["tune N on outer OOS", "use lockbox", "size up after wins"],
        },
        {
            "id": 2,
            "type": "execution_gate",
            "name": "strength_quantile_p75",
            "control_version_id": vid,
            "candidate_knobs": {"strength_quantile": 0.75},
            "rationale": (
                "Raise mean_strength threshold to 75th percentile of lookback |mean|; "
                "prior p75 transfer on ETH K5 increased expectancy_return_units."
            ),
            "economic": "Trade only higher-conviction signals to raise edge per unit.",
            "forbidden": ["combine with cooloff in same generation"],
        },
        {
            "id": 3,
            "type": "execution_gate",
            "name": "skip_high_vol_low_strength",
            "control_version_id": vid,
            "candidate_knobs": {
                "skip_vol_tercile": "high",
                "require_strength_tercile": ["mid", "high"],
            },
            "rationale": (
                "Shared elevated buckets often pair high vol with weak signal; "
                f"shared_examples={ [s.get('bucket') for s in shared[:2]] }."
            ),
            "economic": "Avoid noisy high-vol entries with low absolute model score.",
            "forbidden": ["fit vol cutoffs on outer OOS"],
        },
        {
            "id": 4,
            "type": "execution_gate",
            "name": "book1_extra_strength",
            "control_version_id": vid,
            "candidate_knobs": {
                "clarity_scope": "all",
                "book1_strength_quantile": 0.75,
                "addon_strength_quantile": 0.5,
            },
            "rationale": "Historically book1 is noisier; require stronger |mean| only on primary.",
            "economic": "Improve first-entry quality without starving add-ons.",
            "forbidden": ["grid many quantiles on outer"],
        },
        {
            "id": 5,
            "type": "feature_retrain_later",
            "name": "causal_recent_hit_rate_feature",
            "control_version_id": vid,
            "candidate_knobs": {
                "new_feature": "recent_hit_rate_10",
                "fit_window": "train_only",
            },
            "rationale": (
                "Only if gate arms fail: add causal rolling hit-rate of prior closed "
                "trades as a LightGBM feature (train-fold fit only)."
            ),
            "economic": "Let the model learn temporary cold spells without OOS labels.",
            "forbidden": ["label future losses", "weight by outer-fold outcomes"],
        },
    ]
    return {
        "promotion_blocked": True,
        "source": "offline_template",
        "primary_control": top,
        "geometry_hint": geom,
        "proposals": proposals,
        "note": (
            "LLM analyst template. Does not retrain Live packs. "
            "Pick ONE arm, preregister, outer transfer settle only."
        ),
    }


def build_analyst_prompt(fleet_summary: Mapping[str, Any], max_chars: int = 12_000) -> str:
    pain = fleet_summary.get("pain_rank") or []
    shared = fleet_summary.get("cross_pack_loss_streak_buckets") or []
    body = {
        "task": (
            "Propose at most 5 TESTABLE execution-gate or train-only feature arms "
            "to reduce consecutive realized losses across structure_v1 packs. "
            "Do not use outer OOS or lockbox to tune. Do not change size after wins."
        ),
        "pain_rank_top5": pain[:5],
        "cross_pack_buckets_top8": shared[:8],
        "constraints": [
            "structure_v1 packs are LightGBM not language models",
            "promotion_blocked until nested outer transfer settle",
            "one candidate per generation",
        ],
    }
    text = json_dumps_safe(body)
    return text[: int(max_chars)]


def json_dumps_safe(obj: Any) -> str:
    import json

    return json.dumps(obj, indent=2, default=str)
