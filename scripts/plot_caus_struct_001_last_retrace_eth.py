"""Finplot CAUS-STRUCT-001 leak (last_retrace_pct*) on ETHUSDT + ~300 trades.

Leaking columns (registry REMEDIATED_RETRAIN_REQUIRED):
  last_retrace_pct, last_retrace_pct_4h, last_retrace_pct_1w  (also 1h when
  decision TF is 15m).

The Fibonacci retracement of a leg is measured only after the *next opposite*
leg ends. The bug published that number at the leg's own confirm time (look-ahead).
Live saw NaN (later zero-filled); research saw the future-filled value.

Chart layout (clearest demonstration):
  1) realized equity
  2) ETHUSDT 1h candles + last ~300 trade lines (clean pre-lockbox OOS)
  3) last_retrace_pct: leaky publish vs causal publish
  4) absolute gap + premature look-ahead mask

Window: [2026-01-01, 2026-05-01) — ~4 months clean outer OOS; no lockbox.
Evidence: DISPLAY_ONLY_LEAK_DIAGNOSTIC (not promotion).
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

os.environ.pop("TRADESIM_NO_PLOT", None)

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_hedge,
)
from tradesim.research.plot import plot_backtest  # noqa: E402

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.experiments.eth_multitrade_nested import build_multitrade_signals  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

# Prefer botsgeneral indicators source.
sys.path.insert(0, r"C:\projects\botsgeneral\packages\indicators\src")
from indicators.compute import compute_structure  # noqa: E402

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
SL = 0.02
BASE_HOLD = 12
HOLD_ADDON = 24
MEAN_LOOKBACK = 168
LABEL_HORIZON = 6
STRENGTH_Q = 0.75
K = 7
FIB = 1.618
MAX_TRADES_ON_CHART = 300

# ~4 months clean OOS (exclusive of lockbox)
DISPLAY_START = "2026-01-01"
DISPLAY_END = FORWARD_LOCKBOX_START  # 2026-05-01

OUT_DIR = ARTIFACTS / "reports" / "caus_struct_001_last_retrace_finplot"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
LOG = OUT_DIR / "_finplot.log"

LEAK_COLS = (
    "last_retrace_pct",
    "last_retrace_pct_4h",
    "last_retrace_pct_1w",
)


def _log(msg: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(msg, flush=True)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(msg + "\n")


def _ohlcv_to_struct_input(ohlcv: pd.DataFrame) -> pd.DataFrame:
    ts = index_to_ms(ohlcv.index)
    return pd.DataFrame(
        {
            "ts_ms": ts,
            "open": ohlcv["open"].to_numpy(dtype=float),
            "high": ohlcv["high"].to_numpy(dtype=float),
            "low": ohlcv["low"].to_numpy(dtype=float),
            "close": ohlcv["close"].to_numpy(dtype=float),
            "volume": ohlcv["volume"].to_numpy(dtype=float)
            if "volume" in ohlcv.columns
            else np.zeros(len(ohlcv)),
        }
    )


def last_retrace_leaky_and_causal(
    ohlcv: pd.DataFrame, *, timeframe: str = TIMEFRAME
) -> pd.DataFrame:
    """Return decision-time series: leaky (pre-CAUS-STRUCT-001) vs causal (fixed)."""
    raw = _ohlcv_to_struct_input(ohlcv)
    bundle = compute_structure(
        raw, source="binance", symbol=SYMBOL, timeframe=timeframe
    )
    ts_ms = raw["ts_ms"].to_numpy(dtype=np.int64)
    n = len(ts_ms)
    legs = bundle.legs
    swings = bundle.swings
    swing_confirm = {s.swing_id: s.confirm_ts_ms for s in swings}

    leaky = np.full(n, np.nan)
    causal = np.full(n, np.nan)
    if not legs:
        idx = pd.to_datetime(ts_ms, unit="ms", utc=True)
        return pd.DataFrame({"leaky": leaky, "causal": causal}, index=idx)

    known_ts = np.asarray(
        [
            max(
                swing_confirm.get(lg.start_swing_id, lg.end_ts_ms),
                swing_confirm.get(lg.end_swing_id, lg.end_ts_ms),
            )
            for lg in legs
        ],
        dtype=np.int64,
    )
    order = np.argsort(known_ts, kind="mergesort")
    known_ts = known_ts[order]
    legs_o = [legs[i] for i in order.tolist()]
    retr = np.asarray([lg.retrace_pct for lg in legs_o], dtype=float)

    # LEAKY: publish retrace at the leg's own confirmation (old bug).
    idx = np.searchsorted(known_ts, ts_ms, side="right") - 1
    ok = idx >= 0
    leaky[ok] = retr[idx[ok]]

    # CAUSAL: publish only after the *successor* leg is known.
    if len(legs_o) >= 2:
        retr_known = known_ts[1:]
        retr_vals = retr[:-1]
        idx_r = np.searchsorted(retr_known, ts_ms, side="right") - 1
        ok_r = idx_r >= 0
        causal[ok_r] = retr_vals[idx_r[ok_r]]

    # Sanity: fixed warehouse path should match causal (within float noise).
    warehouse = bundle.bar_features["last_retrace_pct"].to_numpy(dtype=float)
    # warehouse is aligned to raw rows order in compute_structure
    if len(warehouse) == n:
        # Only compare where both finite
        both = np.isfinite(warehouse) & np.isfinite(causal)
        if both.any():
            max_gap = float(np.nanmax(np.abs(warehouse[both] - causal[both])))
        else:
            max_gap = 0.0
    else:
        max_gap = float("nan")

    idx = pd.to_datetime(ts_ms, unit="ms", utc=True)
    out = pd.DataFrame(
        {
            "leaky": leaky,
            "causal": causal,
            "warehouse": warehouse if len(warehouse) == n else np.full(n, np.nan),
            "warehouse_causal_max_abs": max_gap,
        },
        index=idx,
    )
    out["abs_gap"] = (out["leaky"] - out["causal"]).abs()
    # Look-ahead windows: research score had a number while truth was still unknown.
    out["premature"] = np.isfinite(out["leaky"]) & ~np.isfinite(out["causal"])
    return out


def _cfg() -> dict:
    return {
        "max_positions_per_side": K,
        "clarity": "mean_strength",
        "clarity_scope": "all",
        "fib_ext": FIB,
        "hold_addon": HOLD_ADDON,
        "base_hold": BASE_HOLD,
        "base_tp": 0.01,
        "base_sl": SL,
        "mean_lookback": MEAN_LOOKBACK,
        "uniform_books": False,
        "bar_ms": int(TF_MS[TIMEFRAME]),
        "strength_quantile": STRENGTH_Q,
        "geometry": "wall_clock",
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG.write_text("", encoding="utf-8")
    t0 = time.perf_counter()
    _log(
        "DISPLAY_ONLY_LEAK_DIAGNOSTIC CAUS-STRUCT-001 "
        f"cols={list(LEAK_COLS)} window=[{DISPLAY_START},{DISPLAY_END}) "
        f"TF={TIMEFRAME} trades_overlay_cap={MAX_TRADES_ON_CHART}"
    )
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")
    if "botsgeneral" not in str(__import__("indicators").__file__).lower():
        raise RuntimeError("indicators not botsgeneral")

    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    disp0 = pd.Timestamp(DISPLAY_START, tz="UTC")
    disp1 = pd.Timestamp(DISPLAY_END, tz="UTC")
    assert disp1 <= lock

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()

    # --- leak series on decision TF ---
    _log("computing leaky vs causal last_retrace_pct …")
    retr = last_retrace_leaky_and_causal(ohlcv)
    win = retr.loc[(retr.index >= disp0) & (retr.index < disp1)]
    n_prem = int(win["premature"].sum())
    n_bars = int(len(win))
    both = np.isfinite(win["leaky"]) & np.isfinite(win["causal"])
    n_disagree = int((both & (win["abs_gap"] > 1e-9)).sum())
    frac = n_disagree / n_bars if n_bars else 0.0
    gap_med = (
        float(win.loc[win["abs_gap"] > 1e-9, "abs_gap"].median())
        if (win["abs_gap"] > 1e-9).any()
        else 0.0
    )
    wh_gap = float(win["warehouse_causal_max_abs"].iloc[0]) if len(win) else float("nan")
    _log(
        f"window bars={n_bars} disagree_bars={n_disagree} ({100 * frac:.1f}%) "
        f"premature_nan_window={n_prem} median_abs_gap_when_diff={gap_med:.6g} "
        f"warehouse_vs_causal_max_abs={wh_gap}"
    )

    # higher-TF names for report (values are as-of aligned by structure_v1 later)
    try:
        ohlcv_4h = load_ohlcv(SYMBOL, "4h")
        ohlcv_4h = ohlcv_4h.loc[
            index_to_ms(ohlcv_4h.index) < int(lock.value // 1_000_000)
        ].copy()
        retr_4h = last_retrace_leaky_and_causal(ohlcv_4h, timeframe="4h")
        # Forward-as-of onto 1h (only completed HTF bars)
        leaky_4h = retr_4h["leaky"].reindex(ohlcv.index, method="ffill")
        causal_4h = retr_4h["causal"].reindex(ohlcv.index, method="ffill")
        # shift 1 higher-TF completion hygiene: reindex already uses open stamp
        # of 4h bar; structure warehouse is open-stamped at completion-known.
        # Keep simple; used only for optional pane annotation counts.
        n_prem_4h = int(
            (
                np.isfinite(leaky_4h.loc[disp0:disp1])
                & ~np.isfinite(causal_4h.loc[disp0:disp1])
            ).sum()
        )
        _log(f"4h premature as-of bars on 1h index (rough)={n_prem_4h}")
    except Exception as exc:  # noqa: BLE001
        leaky_4h = causal_4h = None
        _log(f"4h series skipped: {exc}")

    # --- display-only trade sim (clean space builders are fixed; not a promotion arm) ---
    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    ts_ms = index_to_ms(aligned.index)
    disp0_ms = int(disp0.value // 1_000_000)
    disp1_ms = int(disp1.value // 1_000_000)
    purge_ms = LABEL_HORIZON * int(TF_MS[TIMEFRAME])
    train_end_ms = disp0_ms - purge_ms
    tr = np.where(ts_ms < train_end_ms)[0]
    oos = np.where((ts_ms >= disp0_ms) & (ts_ms < disp1_ms))[0]
    if tr.size < 400 or oos.size < 40:
        raise RuntimeError(f"insufficient bars train={tr.size} oos={oos.size}")

    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    _log(f"train_n={tr.size} display_n={oos.size} features={len(cols)}")

    model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
    model.fit(X[tr], yv[tr])
    pred = model.predict(X[oos])
    mean = np.asarray(pred.mean, dtype=float).reshape(-1)
    side = proxy_side(mean, target_family(TARGET))
    close_oos = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)[oos]
    sigs, stats = build_multitrade_signals(
        ts_ms[oos], side, mean, cfg=_cfg(), close=close_oos
    )
    _log(
        f"signals emitted={stats.get('n_emitted')} "
        f"skipped_clarity={stats.get('n_skipped_clarity')}"
    )

    oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
    pad = max(50, HOLD_ADDON * 4)
    pos = int(ohlcv.index.searchsorted(oos0))
    window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    touch = load_ohlcv(SYMBOL, touch_tf)
    end, start = window.index[-1], window.index[0]
    dec_ms = int(TF_MS[TIMEFRAME])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    lev = float(leverage_from_stop(SL))

    bundle = run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id="eth_1h_leak_diag_last4m_clean",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=HOLD_ADDON,
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=K,
            max_positions_per_symbol=K * 2,
        ),
        instrument=research_instrument(SYMBOL),
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": "eth_1h_leak_diag_last4m_clean",
            "evidence_class": "DISPLAY_ONLY_LEAK_DIAGNOSTIC",
            "leak_cols": list(LEAK_COLS),
            "window": [DISPLAY_START, DISPLAY_END],
            "lockbox_used": False,
            "promotion": "FORBIDDEN",
        },
        plot=False,
        print_headline=True,
        store_path=str(STORE),
    )
    m = bundle.metrics
    n_tr = int(m.n_trades)
    _log(f"sim n={n_tr} run_id={getattr(bundle, 'run_id', None)}")

    blob = {
        "evidence_class": "DISPLAY_ONLY_LEAK_DIAGNOSTIC",
        "promotion_allowed": False,
        "leak_columns": list(LEAK_COLS),
        "registry_status": "REMEDIATED_RETRAIN_REQUIRED",
        "conformance": "CAUS-STRUCT-001",
        "window": [DISPLAY_START, DISPLAY_END],
        "timeframe": TIMEFRAME,
        "n_trades_sim": n_tr,
        "max_trades_plotted": MAX_TRADES_ON_CHART,
        "disagreement_bars": n_disagree,
        "disagreement_frac": frac,
        "premature_lookahead_bars": n_prem,
        "median_abs_gap_when_diff": gap_med,
        "run_id": getattr(bundle, "run_id", None),
        "profit_factor": float(m.profit_factor),
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "note": (
            "Educational: leaky vs causal last_retrace_pct on ETHUSDT 1h. "
            "Trade overlay is display-only. Pre-fix packs trained on the leak "
            "are not re-validated here."
        ),
    }
    latest = OUT_DIR / "metrics_latest.json"
    latest.write_text(json.dumps(blob, indent=2, default=str), encoding="utf-8")
    _log(f"wrote {latest}")

    plot_ohlcv = ohlcv.loc[(ohlcv.index >= disp0) & (ohlcv.index < disp1)].copy()
    bars = ohlcv_to_bar_series(plot_ohlcv, symbol=SYMBOL, timeframe=TIMEFRAME)
    plot_retr = retr.reindex(plot_ohlcv.index)
    title = (
        f"ETHUSDT {TIMEFRAME} | CAUS-STRUCT-001 last_retrace_pct LEAK | "
        f"[{DISPLAY_START},{DISPLAY_END}) | ≤{MAX_TRADES_ON_CHART} trades | "
        f"disagree={n_disagree}/{n_bars} bars ({100 * frac:.0f}%)"
    )

    def on_axes(view) -> None:
        import finplot as fplt

        ax_price = view.ax_price
        ax_r = view.extra_axes[0]
        ax_g = view.extra_axes[1]
        # tradesim bar frame uses the same index finplot candles use
        bars_df = view.bars_df
        if bars_df is None:
            return
        idx = bars_df.index
        # Reindex leak series onto clipped plot window (ms index or datetimes)
        if isinstance(idx, pd.DatetimeIndex):
            pr = plot_retr.reindex(idx)
        else:
            # integer bar index: map from bars_df columns if present
            pr = plot_retr.copy()
            pr = pr.iloc[-len(idx) :].copy() if len(pr) >= len(idx) else pr.reindex(plot_ohlcv.index)
            # Prefer mapping by position when bar count matches plot frame
            if len(plot_retr) == len(idx):
                pr = plot_retr.copy()
                pr.index = idx
            else:
                # rebuild from plot_ohlcv order matching df rows
                pr = plot_retr.reindex(plot_ohlcv.index)
                if len(pr) == len(idx):
                    pr.index = idx
                else:
                    # last resort: align last n
                    pr = plot_retr.iloc[-len(idx) :].copy()
                    pr.index = idx

        leaky = pr["leaky"].to_numpy(dtype=float)
        causal = pr["causal"].to_numpy(dtype=float)
        gap = pr["abs_gap"].to_numpy(dtype=float)
        # disagreement: values differ by more than epsilon
        disagree = (
            np.isfinite(leaky)
            & np.isfinite(causal)
            & (np.abs(leaky - causal) > 1e-9)
        ).astype(float)

        fplt.plot(
            pr.index,
            leaky,
            ax=ax_r,
            legend="last_retrace_pct LEAKY (old publish)",
            color="#ff7043",
            width=2,
        )
        fplt.plot(
            pr.index,
            causal,
            ax=ax_r,
            legend="last_retrace_pct CAUSAL (fixed)",
            color="#4fc3f7",
            width=2,
        )
        fplt.plot(
            pr.index,
            gap,
            ax=ax_g,
            legend="|leaky − causal| (look-ahead error)",
            color="#ce93d8",
            width=2,
        )
        fplt.plot(
            pr.index,
            disagree * (np.nanmax(gap[np.isfinite(gap)]) if np.isfinite(gap).any() else 1.0),
            ax=ax_g,
            legend="disagreement mask (scaled)",
            color="#ef5350",
            width=1,
            style=".",
        )

        # Markers on candles where leaky ≠ causal (research score used future-aware value)
        if "High" in bars_df.columns:
            hi = bars_df["High"].to_numpy(dtype=float)
        else:
            hi = bars_df["high"].to_numpy(dtype=float) if "high" in bars_df.columns else None
        if hi is not None and disagree.any():
            midx = pr.index[disagree.astype(bool)]
            mhi = hi[disagree.astype(bool)] * 1.003
            # subsample dense markers
            if len(midx) > 150:
                step = max(1, len(midx) // 150)
                midx = midx[::step]
                mhi = mhi[::step]
            fplt.plot(
                midx,
                mhi,
                ax=ax_price,
                legend=f"look-ahead disagreement ({int(disagree.sum())} bars)",
                color="#ff5252",
                style="^",
                width=2,
            )
    _log(f"opening Finplot bars={len(plot_ohlcv)} trades_cap={MAX_TRADES_ON_CHART} …")
    plot_backtest(
        bars,
        bundle.result,
        title=title,
        metrics=m,
        strategy_meta={
            "name": "eth_1h_leak_diag_last4m_clean",
            "evidence_class": "DISPLAY_ONLY_LEAK_DIAGNOSTIC",
            "leak_cols": list(LEAK_COLS),
        },
        trade_style="lines",
        trade_labels="none",
        max_zone_trades=MAX_TRADES_ON_CHART,
        extra_rows=2,
        extra_row_heights=(0.55, 0.45),
        on_axes=on_axes,
        show=True,
        show_metrics_window=True,
    )
    _log("finplot returned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
