"""Finplot last 200 multitrade p75 trades via existing tradesim boxes.

Does **not** re-implement zones. Uses the shared project path:

  from tradesim.research.plot import plot_backtest
  plot_backtest(..., trade_style=\"boxes\", max_zone_trades=200, metrics=...)

Same pattern as scripts/plot_eth_k5_flat_vs_double.py, plot_structure_lockbox.py,
plot_eth_concurrent_fib_arm.py, plot_structure_eth_concurrent.py.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.pop("TRADESIM_NO_PLOT", None)

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_hedge,
)
from tradesim.research.plot import plot_backtest  # noqa: E402

from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.experiments.eth_multitrade_nested import (  # noqa: E402
    LABEL_HORIZON,
    SL,
    SPACE,
    SYMBOL,
    TARGET,
    TIMEFRAME,
    build_multitrade_signals,
    live_control_cfg,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import build_outer_folds, index_to_ms  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

FOLD_INDEX = 5
N_LAST = 200
GEN = "structure_v1_eth_multitrade_strength_p75_001"
LOG = ARTIFACTS / "reports" / "_finplot_multitrade_p75_boxes.log"
PAD_BARS = 48


def _log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    print(msg, flush=True)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(msg + "\n")


def _run_candidate_fold():
    """Outer fold 5 re-sim for p75 multitrade (walk-forward LGBM + tradesim)."""
    cfg = live_control_cfg()
    cfg.update(
        {
            "clarity_scope": "all",
            "max_positions_per_side": 7,
            "strength_quantile": 0.75,
        }
    )
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
    fold = next(f for f in folds if int(f.fold_index) == FOLD_INDEX)
    tr, oos = fold.train_indices, fold.oos_indices

    model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
    model.fit(X[tr], yv[tr])
    pred = model.predict(X[oos])
    mean = np.asarray(pred.mean, dtype=float).reshape(-1)
    side = proxy_side(mean, target_family(TARGET))
    oos_ts = ts_ms[oos]
    close_oos = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)[oos]
    sigs, stats = build_multitrade_signals(
        oos_ts, side, mean, cfg=cfg, close=close_oos
    )

    touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(SYMBOL)

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

    label = f"{GEN}_candidate"
    bundle = run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=f"{label}-f{FOLD_INDEX}",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=int(cfg["hold_addon"]),
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=int(cfg["max_positions_per_side"]),
            max_positions_per_symbol=int(cfg["max_positions_per_side"]) * 2,
        ),
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": label,
            "generation_id": GEN,
            "fold": FOLD_INDEX,
            "strength_quantile": 0.75,
            "clarity_scope": "all",
            "k": 7,
            "evidence_class": "OUTER_TRANSFER_COMPARE_FOLD_REOPEN",
            "sizing": "MIN_EXCHANGE",
            "live_deploy": "FORBIDDEN",
        },
        plot=False,
        print_headline=False,
        store_path=None,
    )
    return bundle, ohlcv, oos0, oos1, stats, cfg, lev


def main() -> int:
    LOG.write_text("", encoding="utf-8")
    _log("re-sim multitrade p75 fold5 then plot_backtest(trade_style=boxes)")
    bundle, ohlcv, oos0, oos1, stats, cfg, lev = _run_candidate_fold()
    m = bundle.metrics
    n = int(m.n_trades)
    _log(
        f"fold5 n_trades={n} pf={m.profit_factor} exp_ru={getattr(m, 'expectancy_return_units', None)} "
        f"wr={m.win_rate}"
    )

    # Clip chart to last N trades exit span (still pre-lockbox).
    trades = list(bundle.result.trades)
    trades_sorted = sorted(
        trades,
        key=lambda t: (int(t.exit_ts_ms), int(t.entry_ts_ms)),
    )
    last = trades_sorted[-N_LAST:] if len(trades_sorted) > N_LAST else trades_sorted
    t0 = pd.to_datetime(min(int(t.entry_ts_ms) for t in last), unit="ms", utc=True)
    t1 = pd.to_datetime(max(int(t.exit_ts_ms) for t in last), unit="ms", utc=True)
    plot_start = t0 - pd.Timedelta(hours=PAD_BARS)
    plot_end = t1 + pd.Timedelta(hours=12)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    plot_end = min(plot_end, lock - pd.Timedelta(milliseconds=1))

    idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
    win = ohlcv.copy()
    win.index = idx
    win = win.loc[(win.index >= plot_start) & (win.index <= plot_end)]
    bars = ohlcv_to_bar_series(win, symbol=SYMBOL, timeframe=TIMEFRAME)
    _log(f"plot window bars={len(win)} {win.index[0]} -> {win.index[-1]} last_n={len(last)}")

    title = (
        f"{SYMBOL} multitrade p75 | fold{FOLD_INDEX} OOS | last {N_LAST} trades "
        f"(boxes) | PF={float(m.profit_factor):.3f} n={n} | MIN_EXCHANGE"
    )
    # Canonical boxes + full MetricsReport scrollable window (project standard).
    plot_backtest(
        bars,
        bundle.result,
        title=title,
        metrics=bundle.metrics,
        trade_style="boxes",
        max_zone_trades=N_LAST,
        strategy_meta={
            "name": f"{GEN}_candidate",
            "generation_id": GEN,
            "fold": FOLD_INDEX,
            "oos_range": f"{oos0} -> {oos1}",
            "display_trades": f"last {N_LAST} by tradesim max_zone_trades",
            "strength_quantile": 0.75,
            "clarity_scope": "all",
            "k_per_side": 7,
            "fib_ext": cfg.get("fib_ext"),
            "base_hold": cfg.get("base_hold"),
            "hold_addon": cfg.get("hold_addon"),
            "tp_pct": cfg.get("base_tp"),
            "sl_pct": cfg.get("base_sl"),
            "leverage": lev,
            "sizing": "MIN_EXCHANGE",
            "evidence_class": "OUTER_TRANSFER_COMPARE_FOLD_REOPEN",
            "signal_stats": stats,
            "live_deploy": "FORBIDDEN",
            "note": (
                "Green/red boxes = hold win/loss (tradesim trade_style=boxes). "
                "Click price pane to reopen full metrics if closed."
            ),
        },
        show=True,
        show_metrics_window=True,
    )
    _log("plot_backtest returned")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        import traceback

        msg = f"FATAL {type(exc).__name__}: {exc}\n{traceback.format_exc()}"
        print(msg, flush=True)
        LOG.parent.mkdir(parents=True, exist_ok=True)
        LOG.write_text(msg, encoding="utf-8")
        raise
