"""Finplot + hold-time audit: hunt-005 Solana 4h close-location volume slope.

Inner screen only (bars before 2022-01-01). Not outer out-of-sample. Not live.
Does not retune Average-True-Range. Does not peep FORWARD_LOCKBOX_START.

  python -u scripts/plot_hunt005_sol_4h_cvd.py --show
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

os.environ.pop("TRADESIM_NO_PLOT", None)

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim.research.plot import plot_backtest  # noqa: E402

from llm2.backtest.run import ohlcv_to_bar_series  # noqa: E402
from llm2.confluence.sim_arms import cached_touch  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.diagonal_sr.bar_series import make_bar_series  # noqa: E402
from llm2.edge_lab.sim_atr import run_atr_bracket_arm  # noqa: E402
from llm2.ml_lab.idea_catalog_b import cvd_slope  # noqa: E402
from llm2.paths import ARTIFACTS, TF_MS  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402
from scripts.run_edge_lab_hunt_001 import SCREEN_END, _fmt, _screen_end_ms  # noqa: E402

SYMBOL = "SOLUSDT"
TF = "4h"
OUT = ARTIFACTS / "reports" / "ml_lab"


def _frac(n: int, d: int) -> str:
    if d <= 0:
        return ""
    return f"{n / d:.3f}"


def hold_audit(trades) -> dict[str, float | int]:
    """Decision-bar timestamps only. Same 4-hour bar ⇒ hold_ms == 0. Not 1-minute path."""
    n = len(trades)
    hold_ms = np.array([int(t.exit_ts_ms) - int(t.entry_ts_ms) for t in trades], dtype=np.int64)
    hold_min = hold_ms / 60_000.0
    ebr = np.array([bool(getattr(t, "entry_bar_exit", False)) or int(t.hold_bars) <= 0 for t in trades])
    return {
        "n": n,
        "entry_bar_4h": int(ebr.sum()),
        "hold_min_p50": float(np.median(hold_min)) if n else float("nan"),
        "hold_min_p10": float(np.percentile(hold_min, 10)) if n else float("nan"),
        "hold_min_p90": float(np.percentile(hold_min, 90)) if n else float("nan"),
        "hold_min_mean": float(np.mean(hold_min)) if n else float("nan"),
    }


def _first_true(mask: np.ndarray) -> int:
    hit = np.flatnonzero(mask)
    return int(hit[0]) if hit.size else -1


def path_hold_audit(trades, touch: object) -> dict[str, float | int]:
    """Walk 1-minute bars: limit fill vs take-profit / stop.

    Live-faithful: start the stop/target clock on the first 1-minute bar that
    touches the limit. Simulator-faithful (tradesim): replay from the 4-hour
    open, which can hit the target before the limit is touched.
    """
    t_ms = index_to_ms(touch.index)
    high = touch["high"].to_numpy(dtype=float)
    low = touch["low"].to_numpy(dtype=float)
    n_t = int(t_ms.size)
    tf4 = int(TF_MS["4h"])

    n = len(trades)
    same_1m = 0
    same_5m = 0
    same_15m = 0
    same_1h = 0
    exit_before_fill = 0
    before_fill_tp = 0
    before_fill_sl = 0
    before_fill_both = 0
    before_fill_pnl = 0.0
    before_fill_tp_pnl = 0.0
    before_fill_sl_pnl = 0.0
    no_fill = 0
    no_exit = 0
    no_1m = 0
    hold_after_fill = []
    reasons: dict[str, int] = {}

    for t in trades:
        is_long = int(t.side) > 0
        entry = float(t.entry_price)
        stop = float(t.stop_price)
        target = float(t.target_price) if t.target_price is not None else float("nan")
        bar0 = int(t.entry_ts_ms)
        bar1 = int(t.exit_ts_ms) + tf4
        i0 = int(np.searchsorted(t_ms, bar0, side="left"))
        i1 = int(np.searchsorted(t_ms, bar1, side="left"))
        if i0 >= n_t or i1 <= i0 or int(t_ms[i0]) != bar0:
            no_1m += 1
            continue
        slc_h = high[i0:i1]
        slc_l = low[i0:i1]
        fill_rel = _first_true(slc_l <= entry) if is_long else _first_true(slc_h >= entry)
        if fill_rel < 0:
            no_fill += 1
            continue
        if is_long:
            sl_m = slc_l <= stop
            tp_m = slc_h >= target if np.isfinite(target) else np.zeros(slc_h.size, dtype=bool)
        else:
            sl_m = slc_h >= stop
            tp_m = slc_l <= target if np.isfinite(target) else np.zeros(slc_l.size, dtype=bool)
        sim_exit = _first_true(sl_m | tp_m)
        live_exit = _first_true((sl_m | tp_m)[fill_rel:])
        if sim_exit >= 0 and sim_exit < fill_rel:
            exit_before_fill += 1
            pnl = float(t.realized_pnl)
            before_fill_pnl += pnl
            if sl_m[sim_exit] and tp_m[sim_exit]:
                before_fill_both += 1
            elif sl_m[sim_exit]:
                before_fill_sl += 1
                before_fill_sl_pnl += pnl
            else:
                before_fill_tp += 1
                before_fill_tp_pnl += pnl
        if live_exit < 0:
            no_exit += 1
            continue
        live_i = fill_rel + live_exit
        dt_ms = int(t_ms[i0 + live_i] - t_ms[i0 + fill_rel])
        hold_after_fill.append(dt_ms / 60_000.0)
        same_1m += int(dt_ms < 60_000)
        same_5m += int(dt_ms < 300_000)
        same_15m += int(dt_ms < 900_000)
        same_1h += int(dt_ms < 3_600_000)
        if sl_m[live_i] and tp_m[live_i]:
            reasons["same_1m_both_tp_sl"] = reasons.get("same_1m_both_tp_sl", 0) + 1
        elif sl_m[live_i]:
            reasons["stop"] = reasons.get("stop", 0) + 1
        else:
            reasons["target"] = reasons.get("target", 0) + 1

    h = np.asarray(hold_after_fill, dtype=float)
    scored = int(h.size)
    return {
        "n_trades": n,
        "n_scored": scored,
        "no_1m_cover": no_1m,
        "no_fill_touch": no_fill,
        "no_bracket_after_fill": no_exit,
        "sim_exit_before_fill": exit_before_fill,
        "before_fill_tp": before_fill_tp,
        "before_fill_sl": before_fill_sl,
        "before_fill_both": before_fill_both,
        "before_fill_pnl": before_fill_pnl,
        "before_fill_tp_pnl": before_fill_tp_pnl,
        "before_fill_sl_pnl": before_fill_sl_pnl,
        "same_1m": same_1m,
        "same_5m": same_5m,
        "same_15m": same_15m,
        "same_1h": same_1h,
        "hold_min_p10": float(np.percentile(h, 10)) if scored else float("nan"),
        "hold_min_p50": float(np.median(h)) if scored else float("nan"),
        "hold_min_mean": float(np.mean(h)) if scored else float("nan"),
        "hold_min_p90": float(np.percentile(h, 90)) if scored else float("nan"),
        "path_stop": int(reasons.get("stop", 0)),
        "path_target": int(reasons.get("target", 0)),
        "path_both_same_1m": int(reasons.get("same_1m_both_tp_sl", 0)),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", action="store_true", help="open Finplot (blocks until the window closes)")
    args = ap.parse_args()

    raw = load_ohlcv(SYMBOL, TF)
    ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
    sig = cvd_slope(ohlcv)
    sc = make_bar_series(SYMBOL, TF, ohlcv)
    mask = sig != 0
    is_short = sig[np.flatnonzero(mask)] < 0
    sim = run_atr_bracket_arm(
        SYMBOL,
        sc,
        mask,
        is_short,
        tag=f"{SYMBOL}|{TF}|cvd_slope|inner_pre2022",
        market=False,
        work=2,
        max_hold=8,
        k_sl=1.5,
        tp_ratio=1.5,
        sl_cap=0.030,
        return_bundle=True,
    )
    bundle = sim["_bundle"]
    trades = tuple(getattr(bundle.result, "trades", ()) or ())
    audit = hold_audit(trades)
    path = path_hold_audit(trades, cached_touch(SYMBOL, TF))
    n = int(audit["n"])
    ns = int(path["n_scored"])
    lines = [
        "# Hunt 005 Solana 4h cvd_slope — hold audit (inner screen < 2022-01-01)",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Window before `{SCREEN_END}`.",
        "This is **not** nested outer out-of-sample. Do not deploy.",
        "",
        f"Trades: **{n}**. Profit factor: **{_fmt(sim.get('profit_factor'))}**. "
        f"Trades/month: **{_fmt(sim.get('trades_per_month'))}**.",
        f"Decision-bar (4-hour) entry-bar exits: **{audit['entry_bar_4h']}** "
        f"({_frac(int(audit['entry_bar_4h']), n)}).",
        "",
        "Trade timestamps in the simulator are 4-hour bar opens. A same-4-hour-bar "
        "exit has hold_ms = 0. That is **not** a 1-minute round trip.",
        "",
        "## 1-minute path (limit fill to first stop or take-profit)",
        "",
        f"Scored: **{ns}** / {n}. Missing 1-minute cover: {path['no_1m_cover']}. "
        f"No limit touch on 1-minute: {path['no_fill_touch']}. "
        f"No bracket after fill: {path['no_bracket_after_fill']}.",
        f"Simulator 1-minute path from the 4-hour open would hit the bracket "
        f"**before** the limit fill: **{path['sim_exit_before_fill']}** "
        f"(take-profit {path['before_fill_tp']}, stop {path['before_fill_sl']}, "
        f"both {path['before_fill_both']}; summed realized pnl "
        f"{_fmt(path['before_fill_pnl'])}; take-profit branch "
        f"{_fmt(path['before_fill_tp_pnl'])}; stop branch "
        f"{_fmt(path['before_fill_sl_pnl'])}).",
        "",
        "| Same candle as 1-minute fill | n | fraction of scored |",
        "|---|---:|---:|",
        f"| 1-minute | {path['same_1m']} | {_frac(int(path['same_1m']), ns)} |",
        f"| 5-minute | {path['same_5m']} | {_frac(int(path['same_5m']), ns)} |",
        f"| 15-minute | {path['same_15m']} | {_frac(int(path['same_15m']), ns)} |",
        f"| 1-hour | {path['same_1h']} | {_frac(int(path['same_1h']), ns)} |",
        "",
        f"Hold minutes after fill: p10={_fmt(path['hold_min_p10'])}  "
        f"median={_fmt(path['hold_min_p50'])}  mean={_fmt(path['hold_min_mean'])}  "
        f"p90={_fmt(path['hold_min_p90'])}.",
        f"Path exits: stop={path['path_stop']}  take-profit={path['path_target']}  "
        f"both in same 1-minute={path['path_both_same_1m']}.",
        "",
    ]
    OUT.mkdir(parents=True, exist_ok=True)
    text = "\n".join(lines) + "\n"
    (OUT / "hunt_005_sol_4h_cvd_hold.md").write_text(text, encoding="utf-8")
    print(text, flush=True)

    if not args.show:
        return 0
    window = sim["_window"]
    bars = ohlcv_to_bar_series(window, symbol=SYMBOL, timeframe=TF)
    plot_backtest(
        bars,
        bundle.result,
        title=f"{SYMBOL} {TF} cvd_slope inner screen < {SCREEN_END} (not live)",
        max_bars=0,
        relative_equity=False,
        equity_mode="mtm",
        trade_style="boxes",
        metrics=bundle.metrics,
        strategy_meta={
            "name": "hunt005_cvd_slope",
            "symbol": SYMBOL,
            "timeframe": TF,
            "window": f"<{SCREEN_END}",
            "k_sl": 1.5,
            "not_live": True,
        },
        show=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
