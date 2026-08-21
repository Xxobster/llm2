"""Re-sim last outer fold (f5) for multitrade p75 vs control; dump metrics + trades."""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

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

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
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
    pf,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import build_outer_folds, index_to_ms  # noqa: E402

FOLD_INDEX = 5  # last outer fold: 2025-10-01 → 2026-05-01 exclusive
N_LAST = 200
GEN = "structure_v1_eth_multitrade_strength_p75_001"


def _trade_row(t: Any) -> dict[str, Any]:
    side = getattr(t, "side", None)
    side_v = int(getattr(side, "value", side) or 0)
    entry_ms = int(getattr(t, "entry_ts_ms", 0) or 0)
    exit_ms = int(getattr(t, "exit_ts_ms", 0) or 0)
    tag = str(getattr(t, "tag", "") or "")
    book = None
    if "_b" in tag:
        try:
            book = int(tag.rsplit("_b", 1)[-1])
        except ValueError:
            book = None
    pnl = float(getattr(t, "realized_pnl", 0) or 0)
    ru = getattr(t, "return_units", None)
    return {
        "entry_ts_utc": datetime.fromtimestamp(entry_ms / 1000, tz=timezone.utc).isoformat(),
        "exit_ts_utc": datetime.fromtimestamp(exit_ms / 1000, tz=timezone.utc).isoformat()
        if exit_ms
        else None,
        "entry_ts_ms": entry_ms,
        "exit_ts_ms": exit_ms or None,
        "side": "LONG" if side_v > 0 else ("SHORT" if side_v < 0 else str(side)),
        "book_idx": book,
        "tag": tag,
        "entry_price": float(getattr(t, "entry_price", float("nan"))),
        "exit_price": float(getattr(t, "exit_price", float("nan"))),
        "qty": float(getattr(t, "qty", float("nan"))),
        "realized_pnl": pnl,
        "return_units": float(ru) if ru is not None and math.isfinite(float(ru)) else None,
        "fees": float(getattr(t, "fees", getattr(t, "total_fees", float("nan"))) or float("nan")),
        "exit_reason": str(getattr(t, "exit_reason", "") or ""),
        "max_hold_bars": getattr(t, "max_hold_bars", None),
        "stop_offset": getattr(t, "stop_offset", None),
        "target_offset": getattr(t, "target_offset", None),
    }


def _metrics_obj(m: Any, trades: list[Any], stats: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    # Dump every public numeric attribute on metrics
    for name in dir(m):
        if name.startswith("_"):
            continue
        try:
            v = getattr(m, name)
        except Exception:
            continue
        if callable(v):
            continue
        if isinstance(v, (int, float, str, bool)) or v is None:
            if isinstance(v, float) and not math.isfinite(v):
                out[name] = None
            else:
                out[name] = v
        else:
            # nested sharpe-like
            if hasattr(v, "annualised") or hasattr(v, "annualized") or hasattr(v, "raw"):
                out[name] = {
                    k: getattr(v, k, None)
                    for k in (
                        "raw",
                        "annualised",
                        "annualized",
                        "hac",
                        "n",
                    )
                    if hasattr(v, k) or k in ("raw", "annualised")
                }
    pnls = [float(getattr(t, "realized_pnl", 0) or 0) for t in trades]
    rus = [
        float(getattr(t, "return_units", float("nan")))
        for t in trades
        if getattr(t, "return_units", None) is not None
    ]
    wins = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p < 0]
    exit_counts: dict[str, int] = {}
    for t in trades:
        r = str(getattr(t, "exit_reason", "") or "unknown")
        exit_counts[r] = exit_counts.get(r, 0) + 1
    out["derived"] = {
        "n_trades": len(trades),
        "net_pnl_from_trades": float(np.nansum(pnls)),
        "profit_factor_from_trades": pf(pnls),
        "win_rate_from_trades": float(len(wins) / len(pnls)) if pnls else None,
        "avg_win": float(np.mean(wins)) if wins else None,
        "avg_loss": float(np.mean(losses)) if losses else None,
        "expectancy_pnl": float(np.mean(pnls)) if pnls else None,
        "expectancy_return_units": float(np.nanmean(rus)) if rus else None,
        "median_return_units": float(np.nanmedian(rus)) if rus else None,
        "sum_return_units": float(np.nansum(rus)) if rus else None,
        "exit_reasons": exit_counts,
        "signal_stats": {k: int(stats.get(k, 0) or 0) for k in sorted(stats)},
    }
    return out


def run_fold(cfg: dict[str, Any], *, label: str) -> dict[str, Any]:
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
        strategy_meta={"name": label, "fold": FOLD_INDEX, "generation_id": GEN},
        plot=False,
        print_headline=False,
        store_path=None,
    )
    trades = list(bundle.result.trades)
    # chronological by exit then entry
    trades_sorted = sorted(
        trades,
        key=lambda t: (
            int(getattr(t, "exit_ts_ms", 0) or 0),
            int(getattr(t, "entry_ts_ms", 0) or 0),
        ),
    )
    rows = [_trade_row(t) for t in trades_sorted]
    last = rows[-N_LAST:] if len(rows) > N_LAST else rows
    return {
        "label": label,
        "cfg": {
            "strength_quantile": float(cfg.get("strength_quantile", 0.5)),
            "clarity_scope": cfg.get("clarity_scope"),
            "max_positions_per_side": cfg.get("max_positions_per_side"),
            "fib_ext": cfg.get("fib_ext"),
            "base_hold": cfg.get("base_hold"),
            "hold_addon": cfg.get("hold_addon"),
            "base_tp": cfg.get("base_tp"),
            "base_sl": cfg.get("base_sl"),
        },
        "fold_index": FOLD_INDEX,
        "oos_start": str(oos0),
        "oos_end": str(oos1),
        "n_train": int(len(tr)),
        "n_oos_bars": int(len(oos)),
        "n_signals": len(sigs),
        "leverage": lev,
        "metrics": _metrics_obj(bundle.metrics, trades_sorted, stats),
        "n_trades_total": len(rows),
        "all_trades": rows,
        "last_n_trades": last,
        "last_n": N_LAST if len(rows) > N_LAST else len(rows),
    }


def main() -> int:
    control_cfg = live_control_cfg()
    control_cfg.update(
        {
            "clarity_scope": "all",
            "max_positions_per_side": 7,
            "strength_quantile": 0.5,
        }
    )
    cand_cfg = dict(control_cfg)
    cand_cfg["strength_quantile"] = 0.75

    print("control f5 …", flush=True)
    control = run_fold(control_cfg, label=f"{GEN}_control")
    print(
        f"  control n={control['n_trades_total']} "
        f"pf={control['metrics']['derived']['profit_factor_from_trades']} "
        f"exp_ru={control['metrics']['derived']['expectancy_return_units']}",
        flush=True,
    )
    print("candidate f5 …", flush=True)
    candidate = run_fold(cand_cfg, label=f"{GEN}_candidate")
    print(
        f"  candidate n={candidate['n_trades_total']} "
        f"pf={candidate['metrics']['derived']['profit_factor_from_trades']} "
        f"exp_ru={candidate['metrics']['derived']['expectancy_return_units']}",
        flush=True,
    )

    out_dir = ARTIFACTS / "reports" / f"{GEN}_fold{FOLD_INDEX}_detail"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    for arm, key in ((control, "control"), (candidate, "candidate")):
        pd.DataFrame(arm["all_trades"]).to_csv(
            out_dir / f"{key}_all_trades.csv", index=False
        )
        pd.DataFrame(arm["last_n_trades"]).to_csv(
            out_dir / f"{key}_last{N_LAST}_trades.csv", index=False
        )
        (out_dir / f"{key}_metrics.json").write_text(
            json.dumps(arm["metrics"], indent=2, default=str), encoding="utf-8"
        )

    # Slim report for chat: metrics + last 200 only (full trades in CSV)
    slim_control = {k: v for k, v in control.items() if k != "all_trades"}
    slim_cand = {k: v for k, v in candidate.items() if k != "all_trades"}
    report = {
        "generation_id": GEN,
        "created_utc": stamp,
        "fold_index": FOLD_INDEX,
        "fold_oos_window": ["2025-10-01", "2026-05-01"],
        "evidence_class": "OUTER_TRANSFER_COMPARE_FOLD_REOPEN",
        "max_readiness": "RESEARCH_ONLY",
        "note": (
            "Re-sim of last outer fold only for inspection; not a new selection. "
            "Last 200 trades by exit time. MIN_EXCHANGE dust. Full trades in CSV."
        ),
        "control": slim_control,
        "candidate": slim_cand,
        "files": {
            "control_all_trades": f"{out_dir.name}/control_all_trades.csv",
            "candidate_all_trades": f"{out_dir.name}/candidate_all_trades.csv",
            "control_last200": f"{out_dir.name}/control_last{N_LAST}_trades.csv",
            "candidate_last200": f"{out_dir.name}/candidate_last{N_LAST}_trades.csv",
        },
    }
    latest = out_dir / "report_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(json.dumps({"wrote": str(latest), "dir": str(out_dir)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
