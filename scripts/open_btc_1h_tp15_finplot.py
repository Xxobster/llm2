"""Finplot BTC 1h p80 TP1.5/SL1.5 (fleet 004 sibling). RESEARCH_ONLY."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import Side, research_instrument, research_margin, research_sizing  # noqa: E402
from tradesim import research_sim_limit_entry  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.strategy.score_oos import gate_mask, limit_price_side, score_symbol_oos  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL, TF, H = "BTCUSDT", "1h", 2
TP = SL = 0.015
WORK = 2
PACK = "level_vsa"
MAX_ROWS = 120_000
OUT = ARTIFACTS / "reports" / "pivot_forecast" / "finplot_arms"
TAG = "BTCUSDT_1h_p80_tp15_sl15_w2"


def _p80_mask(sc):
    base = gate_mask(sc, mode="p75", tp=0.01, sl=0.01)
    p = np.asarray(sc.p_any, dtype=float)
    idx = np.flatnonzero(base)
    cut = max(30, int(0.7 * idx.size)) if idx.size else 30
    thr_floor = float(np.nanmedian(sc.thr_any[idx[:cut]])) if idx.size else 0.35
    train_p = p[idx[:cut]] if idx.size else p
    train_p = train_p[np.isfinite(train_p)]
    thr_ceil = float(np.nanpercentile(train_p, 80)) if train_p.size else 0.5
    thr = thr_ceil if thr_ceil > thr_floor else thr_floor
    return base & np.isfinite(p) & (p >= thr), thr


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    # ~4 months of 1h ≈ 2880 bars; default 3200 with pad
    ap.add_argument("--max-bars", type=int, default=3200)
    ap.add_argument("--build-only", action="store_true")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    os.environ.pop("TRADESIM_NO_PLOT", None)
    warnings.filterwarnings("ignore", category=Warning, module=r"finplot(\.|$)")
    try:
        warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
    except Exception:
        pass

    print(f"SCORE {SYMBOL} {TF} pack={PACK} …", flush=True)
    sc = score_symbol_oos(
        SYMBOL,
        timeframe=TF,
        horizon_bars=H,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=1.0,
    )
    mask, thr = _p80_mask(sc)
    print(f"  p80 thr={thr:.4f} gated={int(mask.sum())}", flush=True)
    ts, is_short, lim = limit_price_side(sc, mask)
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[j]),
            side=Side.SHORT if is_short[j] else Side.LONG,
            limit_price=float(lim[j]),
            stop_offset=SL,
            target_offset=TP,
            max_hold_bars=H + 2,
            work_bars=WORK,
        )
        for j in range(len(ts))
    ]
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=WORK)
    print(
        f"  intent={int(mask.sum())} path_fill={fill['n_filled_path']} "
        f"fill%={100*float(fill['fill_rate']):.1f}",
        flush=True,
    )

    touch_tf = touch_timeframe(TF, SYMBOL)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    touch = load_ohlcv(SYMBOL, touch_tf)
    touch = touch.loc[touch.index < lock]
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    f_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    f_rt = funding.to_numpy(dtype=float)
    bar_ms = index_to_ms(sc.ohlcv.index)
    sig_ts = np.array([s.ts_ms for s in sigs], dtype=np.int64)
    i0 = int(np.searchsorted(bar_ms, int(sig_ts.min()), side="left"))
    i1 = int(np.searchsorted(bar_ms, int(sig_ts.max()), side="right"))
    window = sc.ohlcv.iloc[max(0, i0 - 80) : min(len(sc.ohlcv), i1 + 80)]
    w_ts = index_to_ms(window.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[TF])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    store = str(OUT / f"{TAG}_store")
    bundle = run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TF,
        strategy_id=TAG,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(SL))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=H + 2, decision_timeframe=TF),
        instrument=research_instrument(SYMBOL),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=False,
        print_headline=True,
        store_path=store,
    )
    run_id = bundle.run_id
    meta = {
        "run_id": run_id,
        "db": store,
        "tag": TAG,
        "tp": TP,
        "sl": SL,
        "max_bars": args.max_bars,
        "note": "fleet004 BTC 1h p80 tp15/sl15; ebr~22.7% PF~1.44",
    }
    (OUT / "btc_1h_tp15_latest.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"  run_id={run_id}", flush=True)
    if args.build_only:
        return 0

    print(f"PLOT {run_id} max_bars={args.max_bars}", flush=True)
    subprocess.Popen(
        [
            sys.executable,
            "-c",
            (
                "from tradesim.ensure_source import prefer_botsgeneral_tradesim;"
                "prefer_botsgeneral_tradesim();"
                "import warnings; warnings.filterwarnings('ignore', category=Warning, module=r'finplot(\\.|$)');"
                "from tradesim.research.__main__ import main;"
                f"raise SystemExit(main(['--db', r'{store}', 'plot', '--run-id', '{run_id}', "
                f"'--max-bars', '{int(args.max_bars)}']))"
            ),
        ],
        cwd=str(_ROOT),
    )
    print("Launched Finplot (~4 months of 1h).", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
