"""ETHUSDT structure_v1 lockbox concurrent grid: Fibonacci *extension* of usual TP + longer hold.

Contaminated lockbox diagnostic only (May 2026 → data end). Not a promotion gate.

Book 1–2 (same side): usual bracket TP +1% (=BASE_TP), SL −2%, max-hold 6.
Book 3+ same side:
  Take-profit price = usual_TP + fib * (usual_TP − entry)
  → target_offset fraction = BASE_TP * (1 + fib)
  fib tested: {0.233, 0.377, 0.618, 1.618}  (hard ceiling fib=1.618 → offset = 2.618%)
  hold: {12, 18} bars; SL stays 2%.

K per side: {3..9} plus unlimited (no cap).
Clarity: none | mean_strength | range_chop | favor_confirm.
Anchors: one-way single; hedge×3 uniform (all books 1%/hold6).

Engine: botsgeneral tradesim all-taker + 0.05% entry slip + funding + min-exchange + lev 18×.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import joblib
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
    research_sim,
    research_sim_hedge,
)

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import (  # noqa: E402
    leverage_from_stop,
    peak_margin_utilization,
    research_costs_baseline,
)
from llm2.hunt.targets import DIRECTION_BAND, target_family  # noqa: E402
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    ROUND_TRIP_COST,
    TF_MS,
    touch_timeframe,
)
from llm2.signals.rules import direction_gate  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL = "ETHUSDT"
SPACE = "structure_v1"
BASE_TP = 0.01
BASE_SL = 0.02
BASE_HOLD = 6
# Fibonacci *extensions* of (usual_TP − entry), not absolute return targets.
# max fib = 1.618 → TP_price = usual_TP + 1.618*(usual_TP−entry) → offset = 2.618%.
FIB_EXT = (0.233, 0.377, 0.618, 1.618)
FIB_EXT_MAX = 1.618
HOLD_MULTS = (2, 3)  # 12, 18
# 0 means unlimited concurrent books per side
K_VALUES = (3, 4, 5, 6, 7, 8, 9, 0)
UNLIMITED_K = 1_000_000
CLARITY = ("none", "mean_strength", "range_chop", "favor_confirm")
MEAN_LOOKBACK = 168  # 7d on 1h
RANGE_WIN = 6
RANGE_MEDIAN_WIN = 48
FAVOR_FRAC = 0.5

PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_direction"
REPORT_DIR = ARTIFACTS / "reports"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
GRID_VERSION = "v2_ext"  # TP = BASE*(1+fib); includes K unlimited

ClarityName = Literal["none", "mean_strength", "range_chop", "favor_confirm"]


def resolve_k(k: int) -> int:
    """Map grid K; 0 → unlimited."""
    return UNLIMITED_K if int(k) <= 0 else int(k)


def k_label(k: int) -> str:
    return "unlimited" if int(k) <= 0 else str(int(k))


def extended_tp_offset(fib_ext: float) -> float:
    """Usual TP + fib*(usual_TP − entry) as a return fraction of entry.

    long: TP_price = E*(1+BASE_TP); extended = TP + fib*(TP-E) = E*(1 + BASE_TP*(1+fib)).
    Cap fib at FIB_EXT_MAX (1.618).
    """
    fib = min(max(float(fib_ext), 0.0), FIB_EXT_MAX)
    return float(BASE_TP * (1.0 + fib))


@dataclass
class OpenBook:
    side: int
    entry_bar: int
    entry_price: float
    tp: float
    sl: float
    hold: int
    exit_bar: int  # inclusive last bar index in ohlcv window


@dataclass
class Candidate:
    bar_i: int  # index into window close series
    ts_ms: int
    side: int
    mean: float


@dataclass
class Ctx:
    target: str
    timeframe: str
    min_edge: float
    start_ts: pd.Timestamp
    end_ts: pd.Timestamp
    window: pd.DataFrame
    touch_win: pd.DataFrame | None
    touch_tf: str | None
    funding_ts: np.ndarray
    funding_rt: np.ndarray
    lev: float
    instrument: Any
    candidates: list[Candidate]
    open: np.ndarray
    high: np.ndarray
    low: np.ndarray
    close: np.ndarray
    ts_ms: np.ndarray
    range_6: np.ndarray
    range_med48: np.ndarray
    abs_mean_by_bar: dict[int, float] = field(default_factory=dict)


def _json_default(obj: object) -> object:
    if isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
        return None
    if isinstance(obj, (np.floating,)):
        v = float(obj)
        if np.isnan(v) or np.isinf(v):
            return None
        return v
    if isinstance(obj, (np.integer,)):
        return int(obj)
    raise TypeError(f"Object of type {type(obj)!r} is not JSON serializable")


def _peak_concurrent(trades: list, *, side: int | None = None) -> int:
    events: list[tuple[int, int]] = []
    for t in trades:
        s = int(getattr(t, "side", 0) or 0)
        if side is not None and s != side:
            continue
        entry = int(getattr(t, "entry_ts_ms", 0) or 0)
        exit_ = int(getattr(t, "exit_ts_ms", entry) or entry)
        events.append((entry, +1))
        events.append((exit_, -1))
    if not events:
        return 0
    events.sort(key=lambda x: (x[0], x[1]))
    cur = peak = 0
    for _, delta in events:
        cur += delta
        peak = max(peak, cur)
    return int(peak)


def _skip_counts(bundle) -> dict[str, int]:
    out: dict[str, int] = {}
    for s in getattr(bundle.result, "skips", None) or []:
        reason = str(getattr(s, "reason", s))
        out[reason] = out.get(reason, 0) + 1
    return out


def _estimate_exit_bar(
    *,
    side: int,
    entry_bar: int,
    entry_price: float,
    tp: float,
    sl: float,
    hold: int,
    high: np.ndarray,
    low: np.ndarray,
) -> int:
    """Adverse same-bar convention on 1h OHLC; assignment heuristic only."""
    n = len(high)
    last = min(n - 1, entry_bar + int(hold))
    if side > 0:
        tp_px = entry_price * (1.0 + tp)
        sl_px = entry_price * (1.0 - sl)
        for j in range(entry_bar, last + 1):
            hit_sl = low[j] <= sl_px
            hit_tp = high[j] >= tp_px
            if hit_sl and hit_tp:
                return j  # adverse: SL first
            if hit_sl:
                return j
            if hit_tp:
                return j
        return last
    tp_px = entry_price * (1.0 - tp)
    sl_px = entry_price * (1.0 + sl)
    for j in range(entry_bar, last + 1):
        hit_sl = high[j] >= sl_px
        hit_tp = low[j] <= tp_px
        if hit_sl and hit_tp:
            return j
        if hit_sl:
            return j
        if hit_tp:
            return j
    return last


def _prune_open(books: list[OpenBook], bar_i: int) -> list[OpenBook]:
    return [b for b in books if b.exit_bar >= bar_i]


def _mean_strength_ok(
    cand: Candidate,
    past_abs: list[float],
) -> bool:
    if not past_abs:
        return True
    thr = float(np.median(np.asarray(past_abs, dtype=float)))
    return abs(float(cand.mean)) >= thr


def build_tiered_signals(
    ctx: Ctx,
    *,
    clarity: ClarityName,
    fib_ext: float | None,
    hold_addon: int | None,
    max_per_side: int,
    uniform_baseline: bool,
) -> tuple[list[Signal], dict[str, int]]:
    """Causal walk: assign book index, TP/hold; filter add-ons by clarity.

    ``uniform_baseline``: every book uses BASE_TP / BASE_HOLD (hedge×3 anchor).
    ``fib_ext``: Fibonacci extension of (usual_TP − entry) for book index >= 3.
    """
    open_long: list[OpenBook] = []
    open_short: list[OpenBook] = []
    past_abs: list[float] = []
    # ring for mean lookback of non-zero signal strengths
    strength_hist: list[float] = []

    stats = {
        "n_candidates": 0,
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_cap": 0,
        "n_addon": 0,
        "n_book3plus": 0,
        "tp_offsets_book3plus": [],
    }
    out: list[Signal] = []
    high, low, close = ctx.high, ctx.low, ctx.close
    n_bars = len(close)
    cap = resolve_k(max_per_side) if max_per_side > 0 else UNLIMITED_K
    # callers may pass resolved unlimited already
    if max_per_side >= UNLIMITED_K // 10:
        cap = int(max_per_side)

    for cand in ctx.candidates:
        stats["n_candidates"] += 1
        bar_i = cand.bar_i
        if bar_i < 0 or bar_i >= n_bars:
            continue

        open_long = _prune_open(open_long, bar_i)
        open_short = _prune_open(open_short, bar_i)

        side = int(cand.side)
        books = open_long if side > 0 else open_short
        n_open = len(books)
        is_addon = n_open >= 1

        # Clarity only blocks add-ons
        if is_addon and clarity != "none":
            ok = True
            if clarity == "mean_strength":
                recent = strength_hist[-MEAN_LOOKBACK:] if strength_hist else []
                ok = _mean_strength_ok(cand, recent)
            elif clarity == "range_chop":
                r6 = float(ctx.range_6[bar_i])
                med = float(ctx.range_med48[bar_i])
                if np.isfinite(r6) and np.isfinite(med) and med > 0:
                    ok = r6 >= med
                else:
                    ok = True
            elif clarity == "favor_confirm":
                oldest = books[0]
                mark = float(ctx.open[bar_i]) if bar_i < n_bars else float(close[bar_i])
                if oldest.side > 0:
                    mtm = (mark - oldest.entry_price) / max(oldest.entry_price, 1e-12)
                else:
                    mtm = (oldest.entry_price - mark) / max(oldest.entry_price, 1e-12)
                ok = mtm >= FAVOR_FRAC * float(oldest.tp)
            if not ok:
                stats["n_skipped_clarity"] += 1
                strength_hist.append(abs(float(cand.mean)))
                continue

        if n_open >= cap:
            stats["n_skipped_cap"] += 1
            strength_hist.append(abs(float(cand.mean)))
            continue

        book_idx = n_open + 1  # 1-based ordinal at decision time
        if is_addon:
            stats["n_addon"] += 1

        if uniform_baseline or book_idx <= 2 or fib_ext is None or hold_addon is None:
            tp = BASE_TP
            hold = BASE_HOLD
        else:
            tp = extended_tp_offset(float(fib_ext))
            hold = int(hold_addon)
            stats["n_book3plus"] += 1
            stats["tp_offsets_book3plus"].append(tp)

        # Entry fill approx for lifecycle: next bar open if exists, else close
        if bar_i + 1 < n_bars:
            entry_bar = bar_i + 1
            entry_px = float(ctx.open[entry_bar])
        else:
            entry_bar = bar_i
            entry_px = float(close[bar_i])

        exit_bar = _estimate_exit_bar(
            side=side,
            entry_bar=entry_bar,
            entry_price=entry_px,
            tp=tp,
            sl=BASE_SL,
            hold=hold,
            high=high,
            low=low,
        )
        book = OpenBook(
            side=side,
            entry_bar=entry_bar,
            entry_price=entry_px,
            tp=tp,
            sl=BASE_SL,
            hold=hold,
            exit_bar=exit_bar,
        )
        if side > 0:
            open_long.append(book)
        else:
            open_short.append(book)

        out.append(
            Signal(
                ts_ms=int(cand.ts_ms),
                side=Side.LONG if side > 0 else Side.SHORT,
                stop_offset=BASE_SL,
                target_offset=tp,
                max_hold_bars=hold,
                tag=f"b{book_idx}_tp{tp:.4f}_h{hold}",
                meta={
                    "book_idx": book_idx,
                    "clarity": clarity,
                    "fib_ext": fib_ext,
                    "tp_offset": tp,
                },
            )
        )
        stats["n_emitted"] += 1
        strength_hist.append(abs(float(cand.mean)))

    # keep stats JSON-light
    offs = stats["tp_offsets_book3plus"]
    if offs:
        stats["tp_offsets_book3plus"] = {
            "n": len(offs),
            "min": float(min(offs)),
            "max": float(max(offs)),
            "mean": float(sum(offs) / len(offs)),
        }
    else:
        stats["tp_offsets_book3plus"] = {"n": 0}
    return out, stats


def prepare(start: str) -> Ctx:
    strategy = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(PACK / "model.joblib")
    model = blob["model"]
    cols = list(blob["feature_columns"])
    target = str(strategy["target"])
    timeframe = str(strategy["timeframe"])
    family = target_family(target)
    min_edge = float(
        strategy.get("min_edge")
        or (DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST)
    )

    ohlcv = load_ohlcv(SYMBOL, timeframe)
    start_ts = pd.Timestamp(start, tz="UTC")
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")

    feats = build_space(ohlcv.copy(), SPACE, symbol=SYMBOL, timeframe=timeframe)
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    for c in feats.columns:
        if c.startswith("last_retrace_pct_"):
            feats[c] = feats[c].fillna(0.0)
    aligned = feats.dropna()
    lock_mask = aligned.index >= start_ts
    if int(lock_mask.sum()) < 50:
        raise RuntimeError(f"insufficient lockbox bars after {start}")

    X = aligned.loc[lock_mask].to_numpy(dtype=float)
    ts_idx = aligned.index[lock_mask]
    pred = model.predict(X)
    mean = pred.mean if pred.mean is not None else np.zeros(len(ts_idx))
    mean = np.asarray(mean, dtype=float).reshape(-1)
    # Direction gate at pack min_edge; same as live
    side_arr = direction_gate(mean, threshold=min_edge)
    # Also respect proxy family (directional uses sign of mean already via gate)

    end_ts = ts_idx[-1]
    window = ohlcv.loc[:end_ts]
    window = window.loc[window.index >= (start_ts - pd.Timedelta(days=14))].copy()

    touch_tf = touch_timeframe(timeframe, SYMBOL)
    try:
        touch = load_ohlcv(SYMBOL, touch_tf)
        dec_ms = int(TF_MS[timeframe])
        touch_end = end_ts + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[
            (touch.index >= (start_ts - pd.Timedelta(days=14))) & (touch.index <= touch_end)
        ]
        touch_ms = int(TF_MS[touch_tf])
        need = dec_ms // touch_ms
        last_dec = int(window["ts_ms"].iloc[-1])
        t_ts = touch_win["ts_ms"].to_numpy(dtype=np.int64)
        lo = int(np.searchsorted(t_ts, last_dec, side="left"))
        hi = int(np.searchsorted(t_ts, last_dec + dec_ms, side="left"))
        if hi - lo < need:
            window = window.iloc[:-1]
            end_ts = window.index[-1]
            touch_end = end_ts + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
            touch_win = touch.loc[
                (touch.index >= (start_ts - pd.Timedelta(days=14))) & (touch.index <= touch_end)
            ]
    except Exception:  # noqa: BLE001
        touch_win = None
        touch_tf = None

    funding = load_funding(SYMBOL)
    if funding.empty:
        raise RuntimeError("no funding — refusing lockbox concurrent grid without live cost")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))

    lev = leverage_from_stop(BASE_SL)
    try:
        instrument = research_instrument(SYMBOL)
    except Exception:  # noqa: BLE001
        instrument = None

    # Map signal timestamps to window bar indices
    win_ts = window["ts_ms"].to_numpy(dtype=np.int64)
    win_index = {int(t): i for i, t in enumerate(win_ts.tolist())}
    lock_ts = index_to_ms(ts_idx)
    candidates: list[Candidate] = []
    for i in range(len(ts_idx)):
        s = int(side_arr[i])
        if s == 0:
            continue
        t = int(lock_ts[i])
        if abs(float(mean[i])) < min_edge:
            continue
        bi = win_index.get(t)
        if bi is None:
            # nearest bar at or before
            j = int(np.searchsorted(win_ts, t, side="right") - 1)
            if j < 0:
                continue
            bi = j
        candidates.append(
            Candidate(bar_i=int(bi), ts_ms=t, side=s, mean=float(mean[i]))
        )
    candidates.sort(key=lambda c: c.ts_ms)

    high = window["high"].to_numpy(dtype=float)
    low = window["low"].to_numpy(dtype=float)
    close = window["close"].to_numpy(dtype=float)
    open_ = window["open"].to_numpy(dtype=float)
    rng = (high - low) / np.maximum(close, 1e-12)
    # mean of last RANGE_WIN bars (causal: through bar i)
    # vectorized rolling
    s = pd.Series(rng)
    range_6 = s.rolling(RANGE_WIN, min_periods=1).mean().to_numpy(dtype=float)
    range_med48 = (
        s.rolling(RANGE_WIN, min_periods=1)
        .mean()
        .shift(1)
        .rolling(RANGE_MEDIAN_WIN, min_periods=1)
        .median()
        .to_numpy(dtype=float)
    )

    return Ctx(
        target=target,
        timeframe=timeframe,
        min_edge=min_edge,
        start_ts=start_ts,
        end_ts=end_ts,
        window=window,
        touch_win=touch_win,
        touch_tf=touch_tf,
        funding_ts=funding_ts[fmask],
        funding_rt=funding_rt[fmask],
        lev=float(lev),
        instrument=instrument,
        candidates=candidates,
        open=open_,
        high=high,
        low=low,
        close=close,
        ts_ms=win_ts,
        range_6=range_6,
        range_med48=range_med48,
    )


def arm_id(
    *,
    kind: str,
    clarity: str = "",
    fib_ext: float | None = None,
    hold: int | None = None,
    k: int | None = None,
) -> str:
    if kind == "anchor_single":
        return "anchor_one_way_single"
    if kind == "anchor_hedge3":
        return "anchor_hedge3_uniform"
    return f"clarity={clarity}|fib_ext={fib_ext}|hold={hold}|K={k_label(int(k or 0))}"


def run_one(
    ctx: Ctx,
    *,
    signals: list[Signal],
    max_per_side: int,
    label: str,
    store: bool,
    meta_extra: dict[str, Any],
) -> dict[str, Any]:
    k_sim = resolve_k(max_per_side) if max_per_side > 0 else UNLIMITED_K
    if max_per_side <= 0:
        k_sim = UNLIMITED_K
    if k_sim <= 1:
        sim = research_sim(
            max_hold_bars=BASE_HOLD,
            decision_timeframe=ctx.timeframe,
        )
    else:
        sim = research_sim_hedge(
            max_hold_bars=max(BASE_HOLD, 18),
            decision_timeframe=ctx.timeframe,
            max_positions_per_side=int(k_sim),
            max_positions_per_symbol=int(k_sim) * 2,
        )

    sid = f"llm2-eth-conc-fib-{hashlib.sha1(label.encode()).hexdigest()[:10]}"
    bundle = run_strategy_backtest(
        ctx.window,
        signals,
        symbol=SYMBOL,
        timeframe=ctx.timeframe,
        strategy_id=sid,
        touch_ohlcv=ctx.touch_win,
        touch_timeframe=ctx.touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=ctx.lev),
        sizing=research_sizing(),
        sim=sim,
        instrument=ctx.instrument,
        funding_ts_ms=ctx.funding_ts,
        funding_rate=ctx.funding_rt,
        strategy_meta={
            "name": label,
            "symbol": SYMBOL,
            "timeframe": ctx.timeframe,
            "batch": "structure_v1_eth_concurrent_fib_clarity",
            "grid_version": GRID_VERSION,
            "leverage": ctx.lev,
            "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
            **meta_extra,
        },
        plot=False,
        print_headline=False,
        store_path=str(STORE) if store else None,
    )
    m = bundle.metrics
    start_ms = int(ctx.start_ts.value // 1_000_000)
    trades = [
        t
        for t in bundle.result.trades
        if int(getattr(t, "entry_ts_ms", 0) or 0) >= start_ms
    ]
    n = len(trades)
    entry_bar = int(getattr(m, "entry_bar_exits", 0) or 0)
    entry_bar_trades = sum(1 for t in trades if bool(getattr(t, "entry_bar_exit", False)))
    if entry_bar_trades:
        entry_bar = entry_bar_trades
    peak_m = peak_margin_utilization(
        trades,
        equity=getattr(bundle.result, "equity", None),
        starting_equity=float(m.starting_equity),
    )
    return {
        "label": label,
        "run_id": getattr(bundle, "run_id", None),
        "n_signals": int(len(signals)),
        "n_trades": int(n),
        "n_trades_engine": int(m.n_trades),
        "n_longs": int(getattr(m, "n_longs", 0) or 0),
        "n_shorts": int(getattr(m, "n_shorts", 0) or 0),
        "net_pnl": float(m.net_pnl),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "total_slippage": float(getattr(m, "total_slippage", float("nan"))),
        "total_funding": float(getattr(m, "total_funding", float("nan"))),
        "max_drawdown": float(getattr(m, "max_drawdown", float("nan"))),
        "entry_bar_exits": int(entry_bar),
        "entry_bar_exit_rate": float(entry_bar / n) if n else 0.0,
        "peak_concurrent_all": _peak_concurrent(trades),
        "peak_concurrent_long": _peak_concurrent(trades, side=1),
        "peak_concurrent_short": _peak_concurrent(trades, side=-1),
        "peak_margin_utilization": float(peak_m),
        "skips": _skip_counts(bundle),
        "warnings": list(getattr(bundle.result, "warnings", []) or [])[:5],
        **meta_extra,
    }


def expand_grid() -> list[dict[str, Any]]:
    arms: list[dict[str, Any]] = [
        {"kind": "anchor_single"},
        {"kind": "anchor_hedge3"},
    ]
    for clarity in CLARITY:
        for fib in FIB_EXT:
            for hm in HOLD_MULTS:
                hold = BASE_HOLD * int(hm)
                for k in K_VALUES:
                    arms.append(
                        {
                            "kind": "grid",
                            "clarity": clarity,
                            "fib_ext": float(fib),
                            "hold": int(hold),
                            "k": int(k),
                        }
                    )
    return arms


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=FORWARD_LOCKBOX_START)
    ap.add_argument("--store", action="store_true", default=False)
    ap.add_argument("--resume", action="store_true", default=True)
    ap.add_argument("--limit", type=int, default=0, help="cap arms (0=all)")
    ap.add_argument(
        "--out",
        default="",
        help="report path; default timestamped under artifacts/reports",
    )
    from llm2.evidence.lockbox_guard import add_lockbox_guard_args, require_lockbox_access
    from llm2.research_policy import PolicyError

    add_lockbox_guard_args(ap)
    args = ap.parse_args(argv)

    try:
        require_lockbox_access(
            experiment_id="structure_v1_eth_concurrent_fib_clarity_v2_ext",
            window_start=str(args.start),
            purpose="multi_arm_lockbox_grid",
            symbols=[SYMBOL],
            accepted_contamination=bool(args.i_accept_lockbox_contamination),
            open_finplot=False,
            notes="scripts/hunt_eth_concurrent_fib_clarity.py",
        )
    except PolicyError as exc:
        print(f"REFUSED: {exc}", flush=True)
        return 2

    stamp = run_conformance_check(quiet=True)
    if not stamp.get("passed"):
        print("tradesim conformance not green; refusing grid")
        return 1
    if not (PACK / "model.joblib").is_file():
        raise SystemExit(f"missing pack {PACK}")

    t0 = time.time()
    print("preparing context …", flush=True)
    ctx = prepare(args.start)
    print(
        f"candidates={len(ctx.candidates)} window={ctx.window.index[0]}->{ctx.end_ts} lev={ctx.lev}",
        flush=True,
    )

    arms = expand_grid()
    if args.limit and args.limit > 0:
        arms = arms[: int(args.limit)]

    stamp_str = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = Path(args.out) if args.out else (
        REPORT_DIR / f"structure_v1_eth_concurrent_fib_ext_{stamp_str}.json"
    )
    ck_path = REPORT_DIR / f"structure_v1_eth_concurrent_fib_ext_{GRID_VERSION}_checkpoint.json"
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    done: dict[str, dict[str, Any]] = {}
    if args.resume and ck_path.is_file():
        try:
            prev = json.loads(ck_path.read_text(encoding="utf-8"))
            for row in prev.get("trials", []):
                done[str(row["label"])] = row
            print(f"resumed {len(done)} trials from checkpoint", flush=True)
        except Exception as exc:  # noqa: BLE001
            print(f"checkpoint read failed: {exc}", flush=True)

    trials: list[dict[str, Any]] = list(done.values())

    print(
        f"grid {GRID_VERSION}: arms={len(arms)} fib_ext={list(FIB_EXT)} "
        f"tp_example fib0.233->{extended_tp_offset(0.233):.4%} "
        f"fib1.618->{extended_tp_offset(1.618):.4%}",
        flush=True,
    )

    for i, arm in enumerate(arms):
        kind = arm["kind"]
        if kind == "anchor_single":
            label = arm_id(kind="anchor_single")
            if label in done:
                continue
            sigs, build_stats = build_tiered_signals(
                ctx,
                clarity="none",
                fib_ext=None,
                hold_addon=None,
                max_per_side=1,
                uniform_baseline=True,
            )
            row = run_one(
                ctx,
                signals=sigs,
                max_per_side=1,
                label=label,
                store=bool(args.store),
                meta_extra={
                    "kind": kind,
                    "clarity": "none",
                    "fib_ext": None,
                    "tp_offset": BASE_TP,
                    "hold": BASE_HOLD,
                    "k": 1,
                    "uniform_baseline": True,
                    "build_stats": build_stats,
                },
            )
        elif kind == "anchor_hedge3":
            label = arm_id(kind="anchor_hedge3")
            if label in done:
                continue
            sigs, build_stats = build_tiered_signals(
                ctx,
                clarity="none",
                fib_ext=None,
                hold_addon=None,
                max_per_side=3,
                uniform_baseline=True,
            )
            row = run_one(
                ctx,
                signals=sigs,
                max_per_side=3,
                label=label,
                store=bool(args.store),
                meta_extra={
                    "kind": kind,
                    "clarity": "none",
                    "fib_ext": None,
                    "tp_offset": BASE_TP,
                    "hold": BASE_HOLD,
                    "k": 3,
                    "uniform_baseline": True,
                    "build_stats": build_stats,
                },
            )
        else:
            clarity = str(arm["clarity"])
            fib_ext = float(arm["fib_ext"])
            hold = int(arm["hold"])
            k = int(arm["k"])
            label = arm_id(
                kind="grid", clarity=clarity, fib_ext=fib_ext, hold=hold, k=k
            )
            if label in done:
                continue
            k_use = resolve_k(k)
            sigs, build_stats = build_tiered_signals(
                ctx,
                clarity=clarity,  # type: ignore[arg-type]
                fib_ext=fib_ext,
                hold_addon=hold,
                max_per_side=k_use,
                uniform_baseline=False,
            )
            row = run_one(
                ctx,
                signals=sigs,
                max_per_side=k_use if k > 0 else UNLIMITED_K,
                label=label,
                store=bool(args.store),
                meta_extra={
                    "kind": kind,
                    "clarity": clarity,
                    "fib_ext": fib_ext,
                    "tp_offset": extended_tp_offset(fib_ext),
                    "hold": hold,
                    "k": k,
                    "k_label": k_label(k),
                    "uniform_baseline": False,
                    "build_stats": build_stats,
                },
            )

        trials.append(row)
        done[label] = row
        ck_path.write_text(
            json.dumps(
                {
                    "updated_utc": datetime.now(timezone.utc).isoformat(),
                    "grid_version": GRID_VERSION,
                    "n_done": len(done),
                    "trials": list(done.values()),
                },
                indent=2,
                default=_json_default,
            )
            + "\n",
            encoding="utf-8",
        )
        peak = row.get("peak_concurrent_all", "?")
        print(
            f"[{i+1}/{len(arms)}] {label} n={row['n_trades']} "
            f"pf={row['profit_factor']:.3f} pnl={row['net_pnl']:.2f} "
            f"peak={peak} tp3={row.get('tp_offset')} "
            f"skip_cl={row.get('build_stats', {}).get('n_skipped_clarity', 0)}",
            flush=True,
        )

    # Rank
    grid_trials = [t for t in trials if t.get("kind") == "grid"]
    anchors = {t["label"]: t for t in trials if str(t.get("kind", "")).startswith("anchor")}
    base = anchors.get("anchor_hedge3_uniform")
    single = anchors.get("anchor_one_way_single")

    by_pnl = sorted(grid_trials, key=lambda r: float(r["net_pnl"]), reverse=True)
    by_pf = sorted(
        [t for t in grid_trials if int(t["n_trades"]) >= int((base or {}).get("n_trades", 0) or 0)],
        key=lambda r: float(r["profit_factor"]),
        reverse=True,
    )
    if not by_pf:
        by_pf = sorted(grid_trials, key=lambda r: float(r["profit_factor"]), reverse=True)

    def _beats_both(t: dict[str, Any]) -> bool:
        if not base:
            return False
        return float(t["net_pnl"]) > float(base["net_pnl"]) and float(
            t["profit_factor"]
        ) > float(base["profit_factor"])

    beat_both = [t for t in grid_trials if _beats_both(t)]
    high_entry_bar = [
        t for t in grid_trials if float(t.get("entry_bar_exit_rate", 0)) > 0.25
    ]

    payload = {
        "symbol": SYMBOL,
        "grid_version": GRID_VERSION,
        "lockbox_start": args.start,
        "data_end": str(ctx.end_ts),
        "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
        "engine": "botsgeneral/tradesim",
        "costs": "all_taker_0.055pct_entry_slip_0.05pct",
        "leverage": ctx.lev,
        "base_bracket": {"tp": BASE_TP, "sl": BASE_SL, "hold": BASE_HOLD},
        "fib_extension": {
            "values": list(FIB_EXT),
            "max": FIB_EXT_MAX,
            "formula": "TP_price = usual_TP + fib*(usual_TP - entry); offset = BASE_TP*(1+fib)",
            "offset_examples": {
                str(f): extended_tp_offset(f) for f in FIB_EXT
            },
        },
        "hold_addon": [BASE_HOLD * m for m in HOLD_MULTS],
        "k_values": list(K_VALUES),
        "k_unlimited_sentinel": 0,
        "clarity": list(CLARITY),
        "n_arms": len(arms),
        "n_trials": len(trials),
        "elapsed_sec": time.time() - t0,
        "note": (
            "Contaminated lockbox diagnostic v2_ext. Book 3+ use Fibonacci *extension* of "
            "the usual 1% TP distance (not absolute +23–62% returns). Max extension fib=1.618 "
            "→ 2.618% target. K=0 means unlimited concurrent books per side. "
            "Do not promote from this grid."
        ),
        "anchors": {
            "one_way_single": single,
            "hedge3_uniform": base,
        },
        "summary": {
            "n_grid": len(grid_trials),
            "n_beat_both_pnl_and_pf_vs_hedge3": len(beat_both),
            "n_entry_bar_rate_gt_25pct": len(high_entry_bar),
            "best_net_pnl": by_pnl[0] if by_pnl else None,
            "best_pf_min_trades_ge_hedge3": by_pf[0] if by_pf else None,
            "top5_pnl": by_pnl[:5],
            "top5_pf": by_pf[:5],
            "bottom5_pnl": list(reversed(by_pnl[-5:])) if by_pnl else [],
            "beats_both": beat_both[:20],
            "unlimited_arms": [
                t for t in grid_trials if t.get("k") == 0 or t.get("k_label") == "unlimited"
            ][:20],
        },
        "trials": trials,
    }

    out_path.write_text(
        json.dumps(payload, indent=2, default=_json_default) + "\n",
        encoding="utf-8",
    )
    alias = REPORT_DIR / "structure_v1_eth_concurrent_fib_ext_latest.json"
    alias.write_text(
        json.dumps(payload, indent=2, default=_json_default) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {out_path}", flush=True)
    print(f"wrote {alias}", flush=True)
    try:
        from llm2.evidence.peek_log import append_peek
        from llm2.research_policy import classify_evidence_for_window

        pe_cls = classify_evidence_for_window(
            window_start=str(args.start),
            window_end=str(ctx.end_ts),
            experiment_family="concurrent_grid",
        )
        append_peek(
            experiment_id=f"structure_v1_eth_concurrent_fib_clarity_{GRID_VERSION}",
            window_start=str(args.start),
            window_end=str(ctx.end_ts),
            purpose="multi_arm_lockbox_grid",
            arms=f"{len(arms)} arms fib_ext grid",
            n_arms=int(len(arms)),
            evidence_class=pe_cls,
            notes=str(out_path.name),
        )
    except Exception as exc:  # noqa: BLE001
        print(f"PEEK_LOG_WARN {type(exc).__name__}: {exc}", flush=True)
    print(
        f"beat_both={len(beat_both)} best_pnl={by_pnl[0]['label'] if by_pnl else None} "
        f"best_pf={by_pf[0]['label'] if by_pf else None}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
