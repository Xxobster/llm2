"""Finplot the settled structure_v1 best model with readable markers.

Default: plot one outer fold at a time with a trade cap (Finplot cannot show 5k overlays).
Use --fold all to walk every fold (opens sequential windows), or --fold 5 for the V2 gap fold.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

os.environ.pop("TRADESIM_NO_PLOT", None)

_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim,
)
from tradesim.research.plot import plot_backtest  # noqa: E402

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.runner import _labels_for_target, _make_model  # noqa: E402
from llm2.hunt.targets import proxy_side, target_family  # noqa: E402
from llm2.models.base import Prediction  # noqa: E402
from llm2.paths import FORWARD_LOCKBOX_START, ROUND_TRIP_COST, touch_timeframe  # noqa: E402
from llm2.signals.translate import predictions_to_signals  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, build_outer_folds, index_to_ms  # noqa: E402

SYMBOL = "BTCUSDT"
TIMEFRAME = "1h"
TARGET = "fwd_return"
SPACE = "structure_v1"
MODEL = "lgbm_regressor"
HORIZON = 6
TP = 0.01
SL = 0.02
ACCOUNT = "Xxobster7"
BOT_NAME = "llm2-structure-micro"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
DEFAULT_TRADE_CAP = 80


def _bots_account_pnl(account: str = ACCOUNT) -> dict:
    """Pull live equity / unrealised PnL via botsgeneral.pnl (never logs secrets).

    Tries local keys first; on IP-whitelist failures, falls back to ``botsgeneral``
    on the ln1 VPS (where Xxobster7 keys are bound).
    """
    summary: dict = {"account": account, "bots": [BOT_NAME]}
    try:
        from botsgeneral.keys import resolve_accounts
        from botsgeneral.pnl import account_summary
    except Exception as exc:  # noqa: BLE001
        summary["error"] = f"botsgeneral import failed: {type(exc).__name__}: {exc}"
        return _bots_account_pnl_via_vps(account, summary)

    try:
        accounts = resolve_accounts()
    except Exception as exc:  # noqa: BLE001
        summary["error"] = f"resolve_accounts: {type(exc).__name__}: {exc}"
        return _bots_account_pnl_via_vps(account, summary)

    creds = None
    for name, c in accounts.items():
        if str(name).lower() == account.lower():
            creds = c
            break
    if creds is None:
        summary["error"] = f"account {account!r} not in resolved keys"
        return _bots_account_pnl_via_vps(account, summary)

    local = account_summary(account, creds)
    local["bots"] = [BOT_NAME]
    err = str(local.get("error") or "")
    if local.get("total_equity") is not None and "Unmatched IP" not in err:
        return local
    summary.update(local)
    return _bots_account_pnl_via_vps(account, summary)


def _bots_account_pnl_via_vps(account: str, fallback: dict) -> dict:
    """SSH to ln1 and run botsgeneral.pnl for the account (IP-whitelisted host)."""
    import json
    import subprocess
    from pathlib import Path

    helper = Path(__file__).resolve().parent / "_vps_account_pnl.py"
    try:
        # Helper is already deployed under /opt/llm2-structure when possible; fall back to /tmp.
        remote_helper = "/opt/llm2-structure/_vps_account_pnl.py"
        subprocess.call(
            [
                "scp",
                "-o",
                "BatchMode=yes",
                "-o",
                "ConnectTimeout=8",
                "-o",
                "ServerAliveInterval=5",
                str(helper),
                f"ln1:{remote_helper}",
            ],
            timeout=25,
        )
        out = subprocess.check_output(
            [
                "ssh",
                "-o",
                "BatchMode=yes",
                "-o",
                "ConnectTimeout=8",
                "ln1",
                f"python3 {remote_helper} {account} || python3 /tmp/_vps_account_pnl.py {account}",
            ],
            text=True,
            timeout=45,
            stderr=subprocess.STDOUT,
        )
        line = [ln for ln in out.splitlines() if ln.strip().startswith("{")][-1]
        remote = json.loads(line)
        remote["bots"] = list(
            dict.fromkeys(list(remote.get("bots") or []) + [BOT_NAME])
        )
        remote["pnl_source"] = "botsgeneral.pnl@ln1"
        return remote
    except Exception as exc:  # noqa: BLE001
        fallback = dict(fallback)
        fallback["vps_pnl_error"] = f"{type(exc).__name__}: {exc}"
        fallback["bots"] = [BOT_NAME]
        return fallback


def _plot_fold(
    *,
    fold,
    aligned: pd.DataFrame,
    ohlcv: pd.DataFrame,
    X_all: np.ndarray,
    y_all: np.ndarray,
    ts_ms: np.ndarray,
    touch,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    trade_cap: int,
    store: bool,
    show: bool,
) -> None:
    family = target_family(TARGET)
    m = _make_model(MODEL)
    m.fit(X_all[fold.train_indices], y_all[fold.train_indices])
    pred = m.predict(X_all[fold.oos_indices])
    mean = pred.mean if pred.mean is not None else np.zeros(len(fold.oos_indices))
    side = proxy_side(np.asarray(mean, dtype=float), family)
    signals = predictions_to_signals(
        ts_ms[fold.oos_indices],
        Prediction(side=side, mean=np.asarray(mean, dtype=float)),
        tp_pct=TP,
        sl_pct=SL,
        min_edge=ROUND_TRIP_COST,
    )
    oos_start = aligned.index[fold.oos_indices[0]]
    oos_end = aligned.index[fold.oos_indices[-1]]
    # Pad window so holds can resolve
    window = ohlcv.loc[:oos_end].tail(max(len(fold.oos_indices) + 500, 1000))
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    touch_win = None
    if touch is not None:
        from llm2.paths import TF_MS as _TF_MS

        _touch_end = oos_end + pd.Timedelta(milliseconds=int(_TF_MS[TIMEFRAME])) - pd.Timedelta(
            milliseconds=1
        )
        touch_win = touch.loc[:_touch_end].tail(max(len(window) * 60, 20_000))

    lev = leverage_from_stop(SL)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    try:
        instrument = research_instrument(SYMBOL)
    except Exception:  # noqa: BLE001
        instrument = None
    print(
        f"\n=== fold {fold.fold_index} {oos_start} -> {oos_end} "
        f"signals={len(signals)} trade_cap={trade_cap} ==="
    )
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=f"llm2-structure_v1-lgbm-fold{fold.fold_index}",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf if touch_win is not None else None,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim(max_hold_bars=HORIZON, decision_timeframe=TIMEFRAME),
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": f"{SYMBOL} {TIMEFRAME} {MODEL}",
            "symbol": SYMBOL,
            "timeframe": TIMEFRAME,
            "batch": f"structure_v1_fold_v2_f{fold.fold_index}",
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "tp_pct": TP,
            "sl_pct": SL,
            "min_size_caveat": True,
            "position_mode": "ONE_WAY max_positions=1",
        },
        plot=False,
        print_headline=True,
        store_path=str(STORE) if store else None,
    )
    trades = list(bundle.result.trades)
    if trades:
        last_entry = getattr(trades[-1], "entry_ts_ms", None) or getattr(
            trades[-1], "entry_time", None
        )
        print(f"fold{fold.fold_index} last_entry={last_entry} n_trades={len(trades)}")
    if show:
        bars = ohlcv_to_bar_series(window, symbol=SYMBOL, timeframe=TIMEFRAME)
        cached = os.environ.get("LLM2_BOTS_PNL_JSON")
        if cached:
            import json as _json

            try:
                live_pnl = _json.loads(cached)
                live_pnl.setdefault("bots", [BOT_NAME])
            except Exception:  # noqa: BLE001
                live_pnl = _bots_account_pnl(ACCOUNT)
        else:
            live_pnl = _bots_account_pnl(ACCOUNT)
        m = bundle.metrics
        plot_backtest(
            bars,
            bundle.result,
            title=(
                f"{SYMBOL} {TIMEFRAME} | {ACCOUNT} | {BOT_NAME} | "
                f"structure_v1 {MODEL} fold{fold.fold_index} "
                f"[{oos_start.date()} -> {oos_end.date()}] "
                f"BT_PnL={m.net_pnl:.2f} PF={m.profit_factor:.2f}"
            ),
            metrics=bundle.metrics,
            trade_style="boxes",
            max_zone_trades=trade_cap,
            strategy_meta={
                "name": f"{SYMBOL} {TIMEFRAME} structure_v1 {MODEL}",
                "symbol": SYMBOL,
                "timeframe": TIMEFRAME,
                "venue_product": "Bybit USDT perpetual",
                "account": ACCOUNT,
                "account_ref": ACCOUNT,
                "bots": [BOT_NAME],
                "bots_pnl": live_pnl,
                "backtest_net_pnl": float(m.net_pnl),
                "backtest_profit_factor": float(m.profit_factor),
                "backtest_n_trades": int(m.n_trades),
                "max_hold_bars": HORIZON,
                "tp_pct": TP,
                "sl_pct": SL,
                "fold": fold.fold_index,
                "fold_geometry": FOLD_GEOMETRY_VERSION,
                "position_mode": "research ONE_WAY max=1; live hedge positionIdx 1/2",
                "note": (
                    f"Green/red boxes = hold span win/loss. Red + max_hold means timed out "
                    f"after {HORIZON} bars without TP/SL — not a TP fill. "
                    f"Showing last {trade_cap} trades."
                ),
            },
            show=True,
        )
    print(
        f"fold{fold.fold_index} PF={bundle.metrics.profit_factor:.4f} "
        f"n={bundle.metrics.n_trades} funding={bundle.metrics.total_funding:.2f}"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--fold",
        default="-1",
        help="fold index, 'all', or -1 for last fold (V2 gap fold after extension)",
    )
    ap.add_argument("--trade-cap", type=int, default=DEFAULT_TRADE_CAP)
    ap.add_argument("--store", action="store_true")
    ap.add_argument(
        "--no-show",
        action="store_true",
        help="run fold backtest + print metrics without opening Finplot",
    )
    args = ap.parse_args()

    stamp = run_conformance_check(quiet=True)
    if not stamp.get("passed"):
        print("tradesim conformance not green; refusing plot")
        return 1

    STORE.parent.mkdir(parents=True, exist_ok=True)
    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = build_space(ohlcv, SPACE, symbol=SYMBOL)
    y = _labels_for_target(ohlcv, TARGET, HORIZON, SYMBOL)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    X_all = aligned.drop(columns=["y"]).to_numpy(dtype=float)
    y_all = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=HORIZON, embargo_bars=HORIZON)
    print(f"fold_geometry={FOLD_GEOMETRY_VERSION} n_folds={len(folds)}")

    try:
        touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
        touch = touch.loc[index_to_ms(touch.index) < lock_ms]
    except Exception:  # noqa: BLE001
        touch = None

    funding = load_funding(SYMBOL)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    if funding.empty:
        raise RuntimeError("no funding — refusing plot that would omit a live cost")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)

    if str(args.fold).lower() == "all":
        selected = folds
    else:
        idx = int(args.fold)
        if idx < 0:
            idx = len(folds) + idx
        selected = [folds[idx]]

    for fold in selected:
        _plot_fold(
            fold=fold,
            aligned=aligned,
            ohlcv=ohlcv,
            X_all=X_all,
            y_all=y_all,
            ts_ms=ts_ms,
            touch=touch,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            trade_cap=int(args.trade_cap),
            store=bool(args.store),
            show=not bool(args.no_show),
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
