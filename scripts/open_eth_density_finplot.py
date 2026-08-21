"""Finplot ETH density-ladder arms: P75 control + P75+ATR band (RESEARCH_ONLY)."""

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

SYMBOL, TF, H, TP, SL, WORK = "ETHUSDT", "15m", 4, 0.01, 0.01, 4
PACK, LEVEL = "level_vsa", "atr"
MAX_ROWS = 120_000
OUT = ARTIFACTS / "reports" / "pivot_forecast" / "finplot_arms"


def _bt(ohlcv, signals, *, tag: str, store_path: str):
    touch_tf = touch_timeframe(TF, SYMBOL)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    touch = load_ohlcv(SYMBOL, touch_tf)
    touch = touch.loc[touch.index < lock]
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    f_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    f_rt = funding.to_numpy(dtype=float)
    bar_ms = index_to_ms(ohlcv.index)
    sig_ts = np.array([s.ts_ms for s in signals], dtype=np.int64)
    i0 = int(np.searchsorted(bar_ms, int(sig_ts.min()), side="left"))
    i1 = int(np.searchsorted(bar_ms, int(sig_ts.max()), side="right"))
    window = ohlcv.iloc[max(0, i0 - 80) : min(len(ohlcv), i1 + 80)]
    w_ts = index_to_ms(window.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[TF])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    return run_strategy_backtest(
        window,
        signals,
        symbol=SYMBOL,
        timeframe=TF,
        strategy_id=tag,
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
        store_path=store_path,
    )


def _arm(sc, mask, *, tag: str):
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
    store = str(OUT / f"{tag}_store")
    print(
        f"  {tag}: intent_N={int(mask.sum())} path_fill={fill['n_filled_path']} "
        f"fill%={100*fill['n_filled_path']/max(int(mask.sum()),1):.1f}",
        flush=True,
    )
    bundle = _bt(sc.ohlcv, sigs, tag=tag, store_path=store)
    return bundle.run_id, store


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--max-bars", type=int, default=12000)
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    os.environ.pop("TRADESIM_NO_PLOT", None)
    warnings.filterwarnings("ignore", category=Warning, module=r"finplot(\.|$)")
    try:
        warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
    except Exception:
        pass

    print(f"SCORE {SYMBOL} pack={PACK} level={LEVEL} …", flush=True)
    sc = score_symbol_oos(
        SYMBOL,
        timeframe=TF,
        horizon_bars=H,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode=LEVEL,
    )
    p75 = gate_mask(sc, mode="p75", tp=TP, sl=SL)
    abs_lr = np.abs(sc.level_ret)
    atr = sc.atr_frac
    atr_band = (
        p75
        & np.isfinite(abs_lr)
        & np.isfinite(atr)
        & (abs_lr >= 0.5 * atr)
        & (abs_lr <= 2.0 * atr)
    )

    runs = []
    for tag, mask in (
        (f"{SYMBOL}_p75_ctrl_{LEVEL}_w{WORK}", p75),
        (f"{SYMBOL}_p75_atr_band_{LEVEL}_w{WORK}", atr_band),
    ):
        run_id, db = _arm(sc, mask, tag=tag)
        runs.append((run_id, db, tag))
        print(f"  run_id={run_id}", flush=True)

    (OUT / "eth_density_arms_latest.json").write_text(
        json.dumps(
            [{"run_id": r, "db": d, "tag": t, "max_bars": args.max_bars} for r, d, t in runs],
            indent=2,
        ),
        encoding="utf-8",
    )

    for run_id, db, tag in runs:
        print(f"PLOT {tag} {run_id} max_bars={args.max_bars}", flush=True)
        subprocess.Popen(
            [
                sys.executable,
                "-c",
                (
                    "from tradesim.ensure_source import prefer_botsgeneral_tradesim;"
                    "prefer_botsgeneral_tradesim();"
                    "import warnings; warnings.filterwarnings('ignore', category=Warning, module=r'finplot(\\.|$)');"
                    "from tradesim.research.__main__ import main;"
                    f"raise SystemExit(main(['--db', r'{db}', 'plot', '--run-id', '{run_id}', "
                    f"'--max-bars', '{int(args.max_bars)}']))"
                ),
            ],
            cwd=str(_ROOT),
        )
    print("Launched 2 ETH Finplot processes (~4 months).", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
