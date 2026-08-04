"""Concordance of live fleet signal / entry intent on outer out-of-sample only.

Window: OUTER fold-V2 range union [first_fold_start, FORWARD_LOCKBOX_START).
Does **not** touch the forward lockbox — no Finplot, no contamination flags.

Compares live packs as frozen for micro-live:
  BTC  structure_v1_lgbm (fwd_return)
  ETH  structure_v1_ethusdt_direction (single-book)
  SOL  structure_v1_solusdt_direction
  ETH  structure_v1_ethusdt_multitrade_v1_1 (concurrent K=7, mean_strength add-ons)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.live.multitrade import decide_entry_gate, parse_multitrade_config  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROUND_TRIP_COST, ROOT  # noqa: E402
from llm2.validation.folds import OUTER_FOLD_RANGES  # noqa: E402

SPACE = "structure_v1"
FLEET: list[dict[str, Any]] = [
    {
        "bot_id": "btc_fwd_single_v1",
        "service": "llm2-structure-micro",
        "account": "Xxobster7",
        "pack": ARTIFACTS / "live_packs" / "structure_v1_lgbm",
    },
    {
        "bot_id": "eth_direction_single_v1",
        "service": "llm2-structure-eth",
        "account": "Xxobster7",
        "pack": ARTIFACTS / "live_packs" / "structure_v1_ethusdt_direction",
    },
    {
        "bot_id": "sol_direction_single_v1",
        "service": "llm2-structure-sol",
        "account": "Xxobster7",
        "pack": ARTIFACTS / "live_packs" / "structure_v1_solusdt_direction",
    },
    {
        "bot_id": "eth_multitrade_v1_1",
        "service": "llm2-structure-eth-multitrade-v1_1",
        "account": "Xxobster8",
        "pack": ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_v1_1",
    },
]


def _default_edge(strategy: dict[str, Any]) -> float:
    family = target_family(str(strategy.get("target", "fwd_return")))
    default = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    edge = float(strategy.get("min_edge", default))
    if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
        edge = DIRECTION_BAND
    return edge


def predict_sides(
    *,
    pack_dir: Path,
    start: pd.Timestamp,
    end: pd.Timestamp,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Return DatetimeIndex frame with columns mean, side (gated intent if flat)."""
    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(pack_dir / "model.joblib")
    model = blob["model"]
    cols = list(blob["feature_columns"])
    symbol = str(strategy["symbol"]).upper()
    timeframe = str(strategy["timeframe"])
    family = target_family(str(strategy.get("target", "fwd_return")))
    edge = _default_edge(strategy)

    ohlcv = load_ohlcv(symbol, timeframe)
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    # Feature history + evaluate inside [start, end)
    feat_ohlcv = ohlcv.loc[ohlcv.index < end].copy()
    feats = build_space(feat_ohlcv, SPACE, symbol=symbol, timeframe=timeframe)
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    for c in feats.columns:
        if c.startswith("last_retrace_pct_"):
            feats[c] = feats[c].fillna(0.0)
    aligned = feats.dropna()
    mask = (aligned.index >= start) & (aligned.index < end)
    aligned = aligned.loc[mask]
    if len(aligned) < 100:
        raise RuntimeError(f"{symbol} insufficient bars in window ({len(aligned)})")

    pred = model.predict(aligned.to_numpy(dtype=float))
    mean = pred.mean if pred.mean is not None else np.zeros(len(aligned))
    mean = np.asarray(mean, dtype=float).reshape(-1)
    # Live gate: proxy_side then |mean| must clear edge (same as predictions_to_signals)
    side = proxy_side(mean, family).astype(np.int8)
    side = np.where(np.abs(mean) >= edge, side, 0).astype(np.int8)

    out = pd.DataFrame({"mean": mean, "side": side}, index=aligned.index)
    meta = {
        "symbol": symbol,
        "timeframe": timeframe,
        "target": strategy.get("target"),
        "family": family,
        "min_edge": edge,
        "pack": str(pack_dir.relative_to(ROOT)).replace("\\", "/"),
        "strategy_id": strategy.get("strategy_id"),
        "execution_mode": strategy.get("execution_mode"),
        "multitrade": parse_multitrade_config(strategy),
        "n_bars": int(len(out)),
        "n_fire": int((out["side"] != 0).sum()),
        "fire_rate": float((out["side"] != 0).mean()),
        "long_rate": float((out["side"] > 0).mean()),
        "short_rate": float((out["side"] < 0).mean()),
    }
    return out, meta


def multitrade_primary_fire(
    df: pd.DataFrame,
    mt_cfg: dict[str, Any] | None,
) -> pd.Series:
    """Simulate whether multitrade would open *an* entry this bar (any book).

    Uses full path: position book counts + clarity (add-ons only for v1.1).
    Holding time simplified to base_hold for position decay (not TP/SL path) —
    enough for concurrent *intent* vs single-book primary fire.
    """
    if mt_cfg is None:
        return (df["side"] != 0).astype(np.int8)

    sides = df["side"].to_numpy(dtype=int)
    means = df["mean"].to_numpy(dtype=float)
    n = len(sides)
    max_hold = int(mt_cfg["base_hold"])  # exit approx for occupancy
    hold_addon = int(mt_cfg["hold_addon"])
    opens_long: list[int] = []  # exit_bar exclusive indices
    opens_short: list[int] = []
    hist: list[float] = []
    fire = np.zeros(n, dtype=np.int8)

    for i in range(n):
        opens_long = [e for e in opens_long if e > i]
        opens_short = [e for e in opens_short if e > i]
        s = int(sides[i])
        if s == 0:
            continue
        n_open = len(opens_long) if s > 0 else len(opens_short)
        gate = decide_entry_gate(
            side=s,
            pred_mean=float(means[i]),
            n_open_same_side=n_open,
            strength_hist=hist,
            cfg=mt_cfg,
        )
        if gate.get("append_strength") or gate.get("allow"):
            hist.append(abs(float(means[i])))
            if len(hist) > int(mt_cfg["mean_lookback"]) * 4:
                hist = hist[-int(mt_cfg["mean_lookback"]) * 4 :]
        if not gate.get("allow"):
            continue
        fire[i] = 1
        hold = int(gate.get("max_hold_bars", max_hold))
        exit_i = i + max(1, hold)
        if s > 0:
            opens_long.append(exit_i)
        else:
            opens_short.append(exit_i)
    return pd.Series(fire, index=df.index, name="mt_entry")


def single_book_path_fire(df: pd.DataFrame, max_hold: int = 6) -> pd.Series:
    """Single-book: fire only when flat (vectorized-friendly loop, O(n))."""
    sides = df["side"].to_numpy(dtype=int)
    n = len(sides)
    fire = np.zeros(n, dtype=np.int8)
    busy_until = -1
    for i in range(n):
        if i < busy_until:
            continue
        if sides[i] == 0:
            continue
        fire[i] = 1
        busy_until = i + max_hold
    return pd.Series(fire, index=df.index, name="sb_entry")


def pairwise(frames: dict[str, pd.Series]) -> list[dict[str, Any]]:
    ids = list(frames.keys())
    rows: list[dict[str, Any]] = []
    for i, a in enumerate(ids):
        for b in ids[i + 1 :]:
            idx = frames[a].index.intersection(frames[b].index)
            xa = frames[a].reindex(idx).fillna(0).astype(int).to_numpy()
            yb = frames[b].reindex(idx).fillna(0).astype(int).to_numpy()
            n = len(idx)
            fa = xa != 0
            fb = yb != 0
            both = fa & fb
            long_a = xa > 0
            long_b = yb > 0
            short_a = xa < 0
            short_b = yb < 0
            both_long = long_a & long_b
            both_short = short_a & short_b
            a_long_b_short = long_a & short_b
            a_short_b_long = short_a & long_b
            same_dir = both_long | both_short
            opp_dir = a_long_b_short | a_short_b_long
            p_a = float(fa.mean()) if n else 0.0
            p_b = float(fb.mean()) if n else 0.0
            p_both = float(both.mean()) if n else 0.0
            p_long_a = float(long_a.mean()) if n else 0.0
            p_long_b = float(long_b.mean()) if n else 0.0
            p_short_a = float(short_a.mean()) if n else 0.0
            p_short_b = float(short_b.mean()) if n else 0.0
            p_both_long = float(both_long.mean()) if n else 0.0
            p_both_short = float(both_short.mean()) if n else 0.0
            p_opp = float(opp_dir.mean()) if n else 0.0
            indep = p_a * p_b
            indep_long = p_long_a * p_long_b
            indep_short = p_short_a * p_short_b
            indep_opp = p_long_a * p_short_b + p_short_a * p_long_b
            rows.append(
                {
                    "a": a,
                    "b": b,
                    "n_bars": n,
                    "rate_a": p_a,
                    "rate_b": p_b,
                    "rate_long_a": p_long_a,
                    "rate_long_b": p_long_b,
                    "rate_short_a": p_short_a,
                    "rate_short_b": p_short_b,
                    "rate_both_fire": p_both,
                    "rate_both_long": p_both_long,
                    "rate_both_short": p_both_short,
                    "rate_opposite": p_opp,
                    "rate_a_long_b_short": float(a_long_b_short.mean()) if n else 0.0,
                    "rate_a_short_b_long": float(a_short_b_long.mean()) if n else 0.0,
                    "rate_expected_independent": indep,
                    "lift_vs_independent": (p_both / indep) if indep > 0 else None,
                    "lift_both_long_vs_independent": (p_both_long / indep_long)
                    if indep_long > 0
                    else None,
                    "lift_both_short_vs_independent": (p_both_short / indep_short)
                    if indep_short > 0
                    else None,
                    "lift_opposite_vs_independent": (p_opp / indep_opp) if indep_opp > 0 else None,
                    "n_both": int(both.sum()),
                    "n_both_long": int(both_long.sum()),
                    "n_both_short": int(both_short.sum()),
                    "n_same_direction": int(same_dir.sum()),
                    "n_opposite_direction": int(opp_dir.sum()),
                    "p_same_dir_given_both": float(same_dir.sum() / both.sum())
                    if both.sum()
                    else None,
                    "p_both_long_given_both": float(both_long.sum() / both.sum())
                    if both.sum()
                    else None,
                    "p_both_short_given_both": float(both_short.sum() / both.sum())
                    if both.sum()
                    else None,
                    "p_opposite_given_both": float(opp_dir.sum() / both.sum())
                    if both.sum()
                    else None,
                    "phi_corr_any_fire": float(
                        np.corrcoef(fa.astype(float), fb.astype(float))[0, 1]
                    )
                    if n > 10
                    else None,
                    "phi_corr_long": float(
                        np.corrcoef(long_a.astype(float), long_b.astype(float))[0, 1]
                    )
                    if n > 10
                    else None,
                    "phi_corr_short": float(
                        np.corrcoef(short_a.astype(float), short_b.astype(float))[0, 1]
                    )
                    if n > 10
                    else None,
                    # keep old key for back-compat readers
                    "phi_corr": float(np.corrcoef(fa.astype(float), fb.astype(float))[0, 1])
                    if n > 10
                    else None,
                }
            )
    return rows


def direction_fleet_summary(side_mat: pd.DataFrame) -> dict[str, Any]:
    """Per-bar long/short stack on Xxobster7 (columns = bot_id, values = -1/0/1)."""
    long = (side_mat > 0).astype(int)
    short = (side_mat < 0).astype(int)
    n_long = long.sum(axis=1)
    n_short = short.sum(axis=1)
    n = len(side_mat)
    both_sides_same_bar = (n_long > 0) & (n_short > 0)

    def _hist(s: pd.Series) -> dict[str, int]:
        return {str(k): int(v) for k, v in zip(*np.unique(s.to_numpy(), return_counts=True))}

    # All three same direction
    all_long = float((n_long == side_mat.shape[1]).mean()) if n else 0.0
    all_short = float((n_short == side_mat.shape[1]).mean()) if n else 0.0
    return {
        "n_bars": n,
        "n_bots": int(side_mat.shape[1]),
        "pct_bars_any_long": float((n_long > 0).mean()) if n else 0.0,
        "pct_bars_any_short": float((n_short > 0).mean()) if n else 0.0,
        "pct_bars_long_and_short_mixed": float(both_sides_same_bar.mean()) if n else 0.0,
        "pct_bars_all_long": all_long,
        "pct_bars_all_short": all_short,
        "pct_bars_ge2_long": float((n_long >= 2).mean()) if n else 0.0,
        "pct_bars_ge2_short": float((n_short >= 2).mean()) if n else 0.0,
        "mean_concurrent_longs": float(n_long.mean()) if n else 0.0,
        "mean_concurrent_shorts": float(n_short.mean()) if n else 0.0,
        "long_count_histogram": _hist(n_long),
        "short_count_histogram": _hist(n_short),
        "note": (
            "Mixed long+short same bar = netting opportunity across symbols "
            "(hedge mode); not the same as one bot flip-flopping."
        ),
    }


def fleet_histogram(fire_bool: pd.DataFrame) -> dict[str, Any]:
    """fire_bool: columns bot_id, 0/1 per bar aligned."""
    counts = fire_bool.sum(axis=1).to_numpy(dtype=int)
    n = len(counts)
    hist = {str(k): int(v) for k, v in zip(*np.unique(counts, return_counts=True))}
    return {
        "n_bars": n,
        "n_bots": int(fire_bool.shape[1]),
        "pct_bars_zero_fires": float((counts == 0).mean()) if n else 0.0,
        "pct_bars_exactly_one": float((counts == 1).mean()) if n else 0.0,
        "pct_bars_two_or_more": float((counts >= 2).mean()) if n else 0.0,
        "pct_bars_all_three_xxobster7": None,  # filled by caller if 3 cols
        "mean_concurrent_bots": float(counts.mean()) if n else 0.0,
        "max_concurrent_bots": int(counts.max()) if n else 0,
        "count_histogram": hist,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Live fleet concordance (outer OOS only)")
    ap.add_argument(
        "--start",
        default=OUTER_FOLD_RANGES[0][0],
        help="inclusive UTC start (default first outer fold)",
    )
    ap.add_argument(
        "--end",
        default=FORWARD_LOCKBOX_START,
        help="exclusive UTC end (default lockbox start — never past)",
    )
    ap.add_argument(
        "--allow-lockbox",
        action="store_true",
        help="forbid by default: refuse end > FORWARD_LOCKBOX_START without this + contamination",
    )
    args = ap.parse_args(argv)

    start = pd.Timestamp(args.start, tz="UTC")
    end = pd.Timestamp(args.end, tz="UTC")
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    if end > lock and not args.allow_lockbox:
        print(
            f"REFUSED: window end {end} extends into/after lockbox {lock}. "
            "Concordance uses outer OOS only (end <= FORWARD_LOCKBOX_START).",
            flush=True,
        )
        return 2
    if end > lock:
        # Double gate if someone passes --allow-lockbox
        from llm2.evidence.lockbox_guard import require_lockbox_access
        from llm2.research_policy import PolicyError

        try:
            require_lockbox_access(
                experiment_id="live_fleet_concordance",
                window_start=str(start.date()) if start < lock else FORWARD_LOCKBOX_START,
                window_end=str(end),
                purpose="live_fleet_concordance",
                accepted_contamination=True,
                open_finplot=False,
                notes="--allow-lockbox only",
            )
        except PolicyError as exc:
            print(f"REFUSED: {exc}", flush=True)
            return 2

    print(f"window [{start}, {end}) exclusive end · outer-OOS · no Finplot", flush=True)

    series_side: dict[str, pd.Series] = {}
    series_path: dict[str, pd.Series] = {}
    metas: list[dict[str, Any]] = []

    for bot in FLEET:
        pack = Path(bot["pack"])
        if not (pack / "model.joblib").is_file():
            print(f"SKIP missing pack {pack}", flush=True)
            continue
        print(f"predict {bot['bot_id']} …", flush=True)
        df, meta = predict_sides(pack_dir=pack, start=start, end=end)
        meta = {**bot, **meta}
        metas.append(meta)
        series_side[bot["bot_id"]] = df["side"]
        mt = meta.get("multitrade")
        if mt:
            series_path[bot["bot_id"]] = multitrade_primary_fire(df, mt)
        else:
            series_path[bot["bot_id"]] = single_book_path_fire(df, max_hold=6)
        print(
            f"  {meta['symbol']} fire_rate={meta['fire_rate']:.4f} "
            f"path_rate={float(series_path[bot['bot_id']].mean()):.4f} n={meta['n_bars']}",
            flush=True,
        )

    # Align outer fleet (signal intent as abs side)
    xx7 = [m["bot_id"] for m in metas if m.get("account") == "Xxobster7"]
    common = None
    for bid in xx7:
        common = series_side[bid].index if common is None else common.intersection(series_side[bid].index)
    assert common is not None

    fire_bool = pd.DataFrame(
        {bid: (series_side[bid].reindex(common).fillna(0).astype(int) != 0).astype(int) for bid in xx7},
        index=common,
    )
    hist = fleet_histogram(fire_bool)
    if len(xx7) == 3:
        hist["pct_bars_all_three_xxobster7"] = float(fire_bool.all(axis=1).mean())

    # Same-bar side sign matrix (for direction agreement among fires)
    side_mat = pd.DataFrame(
        {bid: series_side[bid].reindex(common).fillna(0).astype(int) for bid in xx7},
        index=common,
    )

    pair_signal = pairwise({bid: series_side[bid] for bid in series_side})
    pair_path = pairwise({bid: series_path[bid] for bid in series_path})

    # Path entries also carry sign from signal side on that bar
    path_signed: dict[str, pd.Series] = {}
    for bid, side in series_side.items():
        if bid not in series_path:
            continue
        idx = side.index.intersection(series_path[bid].index)
        s = side.reindex(idx).fillna(0).astype(int)
        p = series_path[bid].reindex(idx).fillna(0).astype(int)
        path_signed[bid] = (s * p).astype(int)  # entry side or 0
    pair_path_signed = pairwise(path_signed) if path_signed else []

    dir_summary = direction_fleet_summary(side_mat)

    # ETH single vs multi: signal identity + path
    eth_s = "eth_direction_single_v1"
    eth_m = "eth_multitrade_v1_1"
    eth_cmp: dict[str, Any] = {}
    if eth_s in series_side and eth_m in series_side:
        idx = series_side[eth_s].index.intersection(series_side[eth_m].index)
        sa = series_side[eth_s].reindex(idx).fillna(0).astype(int)
        sm = series_side[eth_m].reindex(idx).fillna(0).astype(int)
        pa = series_path[eth_s].reindex(idx).fillna(0).astype(int)
        pm = series_path[eth_m].reindex(idx).fillna(0).astype(int)
        both = (sa != 0) & (sm != 0)
        eth_cmp = {
            "n_bars": int(len(idx)),
            "signal_sides_identical_rate": float((sa == sm).mean()),
            "signal_both_fire_rate": float(both.mean()),
            "signal_both_long_rate": float(((sa > 0) & (sm > 0)).mean()),
            "signal_both_short_rate": float(((sa < 0) & (sm < 0)).mean()),
            "signal_disagreement_rate": float((sa != sm).mean()),
            "path_both_enter_rate": float(((pa == 1) & (pm == 1)).mean()),
            "path_single_only_rate": float(((pa == 1) & (pm == 0)).mean()),
            "path_multitrade_only_rate": float(((pa == 0) & (pm == 1)).mean()),
            "path_neither_rate": float(((pa == 0) & (pm == 0)).mean()),
            "note": (
                "Same structure_v1 direction targets → raw sides nearly identical. "
                "Path differs: single-book busy skips vs multitrade stacking/clarity."
            ),
        }

    # Peak capital: # of Xxobster7 bots that want entry same bar (signal) + multi separate account
    n_xx7 = fire_bool.sum(axis=1)
    peak_counts = {str(k): int(v) for k, v in zip(*np.unique(n_xx7.to_numpy(), return_counts=True))}

    # Sample same-bar multi-fire timestamps (first 15)
    multi_idx = fire_bool.index[fire_bool.sum(axis=1) >= 2][:15]
    samples = []
    for ts in multi_idx:
        samples.append(
            {
                "ts_utc": str(ts),
                **{bid: int(side_mat.loc[ts, bid]) for bid in xx7},
            }
        )

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    payload = {
        "generation_id": "live_fleet_concordance_001",
        "stamped_utc": stamp,
        "evidence_class": "OUTER_OOS_DIAGNOSTIC",
        "lockbox": "not_used",
        "window_start_inclusive": str(start),
        "window_end_exclusive": str(end),
        "note": (
            "Gated live sides (decide_once parity). Path fires use simplified max-hold occupancy "
            "(not full TP/SL) for concurrence only. Quote promotion from settle still."
        ),
        "bots": metas,
        "xxobster7_signal_histogram": hist,
        "xxobster7_long_short_stack": dir_summary,
        "xxobster7_concurrent_count_histogram": peak_counts,
        "pairwise_signal_intent": pair_signal,
        "pairwise_path_entry": pair_path,
        "pairwise_path_entry_signed": pair_path_signed,
        "eth_single_vs_multitrade": eth_cmp,
        "sample_multi_bot_bars": samples,
    }

    # Human summary lines
    verdict_bits = []
    p2 = hist.get("pct_bars_two_or_more", 0)
    verdict_bits.append(
        f"Xxobster7: on {p2*100:.2f}% of outer-OOS bars ≥2 bots share a gated signal; "
        f"all three together on {(hist.get('pct_bars_all_three_xxobster7') or 0)*100:.3f}%."
    )
    verdict_bits.append(
        f"Long/short stack: ≥2 longs {dir_summary['pct_bars_ge2_long']*100:.2f}% bars, "
        f"≥2 shorts {dir_summary['pct_bars_ge2_short']*100:.2f}%, "
        f"all-long {dir_summary['pct_bars_all_long']*100:.2f}%, "
        f"all-short {dir_summary['pct_bars_all_short']*100:.2f}%, "
        f"mixed long+short same bar {dir_summary['pct_bars_long_and_short_mixed']*100:.2f}%."
    )
    for r in pair_signal:
        if r["a"] in xx7 and r["b"] in xx7:
            lb = r.get("lift_both_long_vs_independent")
            ls = r.get("lift_both_short_vs_independent")
            same = r.get("p_same_dir_given_both")
            opp = r.get("p_opposite_given_both")
            lb_s = f"{lb:.3f}" if lb is not None else "n/a"
            ls_s = f"{ls:.3f}" if ls is not None else "n/a"
            same_s = f"{100.0 * same:.1f}" if same is not None else "n/a"
            opp_s = f"{100.0 * opp:.1f}" if opp is not None else "n/a"
            verdict_bits.append(
                f"  {r['a']} × {r['b']}: both_long={r['rate_both_long']*100:.2f}% "
                f"(lift {lb_s}), both_short={r['rate_both_short']*100:.2f}% "
                f"(lift {ls_s}), opposite={r['rate_opposite']*100:.2f}% "
                f"| given both fire: same={same_s}% opp={opp_s}%"
            )
    if eth_cmp:
        verdict_bits.append(
            f"ETH single vs multitrade: signal sides identical {eth_cmp['signal_sides_identical_rate']*100:.2f}% of bars; "
            f"path both-enter {eth_cmp['path_both_enter_rate']*100:.2f}%, multitrade-only {eth_cmp['path_multitrade_only_rate']*100:.2f}%."
        )
    payload["verdict_text"] = verdict_bits

    out = ARTIFACTS / "reports" / f"live_fleet_concordance_{stamp}.json"
    latest = ARTIFACTS / "reports" / "live_fleet_concordance_latest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, default=str) + "\n"
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    print("\n".join(verdict_bits), flush=True)
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
