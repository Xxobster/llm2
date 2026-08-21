"""Shared tradesim arm runner + SQLite checkpoint for confluence hunts."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from tradesim import Side, Signal, research_instrument, research_margin, research_sizing
from tradesim import research_sim, research_sim_limit_entry

from llm2.backtest.run import run_strategy_backtest
from llm2.data.loader import load_ohlcv
from llm2.data.macro import load_funding
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline
from llm2.paths import FORWARD_LOCKBOX_START, TF_MS, touch_timeframe
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits
from llm2.validation.folds import index_to_ms

_INSTRUMENT: dict[str, object] = {}
_TOUCH: dict[tuple[str, str], pd.DataFrame] = {}
_FUNDING: dict[str, pd.DataFrame] = {}


def jsonable(x: Any) -> Any:
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    if isinstance(x, (np.floating, float)):
        v = float(x)
        return v if np.isfinite(v) else None
    if isinstance(x, (np.integer, int)):
        return int(x)
    if isinstance(x, (np.bool_, bool)):
        return bool(x)
    return x


def instrument(symbol: str):
    inst = _INSTRUMENT.get(symbol)
    if inst is None:
        inst = research_instrument(symbol, refresh_if_missing=False, max_age_ms=10**15)
        _INSTRUMENT[symbol] = inst
    return inst


def _lock_ts() -> pd.Timestamp:
    return pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")


def cached_touch(symbol: str, tf: str) -> pd.DataFrame:
    key = (symbol, tf)
    if key not in _TOUCH:
        touch_tf = touch_timeframe(tf, symbol)
        touch = load_ohlcv(symbol, touch_tf)
        _TOUCH[key] = touch.loc[touch.index < _lock_ts()]
    return _TOUCH[key]


def cached_funding(symbol: str) -> pd.DataFrame:
    if symbol not in _FUNDING:
        funding = load_funding(symbol)
        _FUNDING[symbol] = funding[funding.index < _lock_ts()]
    return _FUNDING[symbol]


def metrics_from_bundle(bundle, *, n_intent: int, fill_pct: float, tag: str) -> dict[str, Any]:
    m = bundle.metrics
    sh = m.sharpe
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    holds = [float(getattr(t, "hold_bars", 1)) for t in trades] if trades else []
    ebr = float(m.entry_bar_exit_rate) if hasattr(m, "entry_bar_exit_rate") else float("nan")
    if holds and (not np.isfinite(ebr)):
        ebr = float(np.mean(np.asarray(holds) <= 0))
    n_tr = int(m.n_trades)
    touch_resolved = 0
    if trades:
        touch_resolved = int(sum(1 for t in trades if getattr(t, "resolved_by_touch", False)))
    out = {
        "tag": tag,
        "status": "RAN",
        "n_intent": int(n_intent),
        "fill_pct": float(fill_pct),
        "n_trades": n_tr,
        "n_longs": int(m.n_longs),
        "n_shorts": int(m.n_shorts),
        "trades_per_month": float(m.trades_per_month),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(m.win_rate),
        "win_rate_ci_low": float(m.win_rate_ci_low),
        "win_rate_ci_high": float(m.win_rate_ci_high),
        "expectancy": float(m.expectancy),
        "net_pnl": float(m.net_pnl),
        "total_return": float(m.total_return),
        "payoff_ratio": float(m.payoff_ratio),
        "sharpe_annualised": float(sh.annualised),
        "sharpe_raw": float(sh.raw_periodic),
        "sharpe_hac_annualised": float(sh.hac_annualised),
        "sortino_annualised": float(m.sortino_annualised),
        "max_drawdown_pct": float(m.max_drawdown_pct),
        "exposure": float(m.exposure),
        "total_fees": float(m.total_fees),
        "total_funding": float(m.total_funding),
        "n_liquidations": int(m.n_liquidations),
        "entry_bar_exit_rate": ebr,
        "avg_hold_bars": float(m.avg_hold_bars),
        "n_exits_tp": int(m.n_exits_tp),
        "n_exits_sl": int(m.n_exits_sl),
        "span_days": float(m.span_days),
        "touch_resolved": touch_resolved,
        "touch_resolved_rate": float(touch_resolved / n_tr) if n_tr else float("nan"),
        "ambiguous_rate": float(getattr(m, "ambiguous_rate", float("nan"))),
    }
    if n_intent > 0 and np.isfinite(out["net_pnl"]):
        out["expectancy_intent_all"] = float(out["net_pnl"]) / n_intent
    else:
        out["expectancy_intent_all"] = float("nan")
    return out


def run_signals_bt(
    symbol: str,
    tf: str,
    ohlcv: pd.DataFrame,
    signals: list,
    *,
    tag: str,
    max_hold: int,
    sl: float,
    market: bool,
    n_intent: int,
    fill_pct: float,
) -> dict[str, Any]:
    if len(signals) < 12:
        return {
            "tag": tag,
            "status": "TOO_FEW",
            "n_intent": int(n_intent),
            "n_signals": len(signals),
            "n_trades": 0,
        }
    touch = cached_touch(symbol, tf)
    funding = cached_funding(symbol)
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
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[tf])) - pd.Timedelta(milliseconds=1)
    touch_tf = touch_timeframe(tf, symbol)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    if len(touch_win) < 12:
        raise RuntimeError(
            f"empty {touch_tf} touch window for {symbol} {tf} tag={tag} "
            f"n_touch={len(touch)} n_win={len(touch_win)} — refuse Open-High-Low-Close fallback"
        )
    sim = (
        research_sim(max_hold_bars=max_hold, decision_timeframe=tf)
        if market
        else research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=tf)
    )
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=tf,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(sl))),
        sizing=research_sizing(),
        sim=sim,
        instrument=instrument(symbol),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=False,
        print_headline=False,
        store_path=None,
    )
    out = metrics_from_bundle(bundle, n_intent=n_intent, fill_pct=fill_pct, tag=tag)
    out["touch_timeframe"] = touch_tf
    out["n_touch_window"] = int(len(touch_win))
    return out


def run_limit_arm(
    symbol: str,
    sc,
    mask: np.ndarray,
    is_short: np.ndarray,
    lim: np.ndarray,
    *,
    tag: str,
    work: int,
    max_hold: int,
    tp: float,
    sl: float,
) -> dict[str, Any]:
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent, "n_trades": 0}
    ts = sc.ts_ms[np.flatnonzero(mask)]
    short = np.asarray(is_short, dtype=bool).reshape(-1)
    if short.size != ts.size:
        raise ValueError(f"is_short length {short.size} != gated {ts.size}")
    is_short = short
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[j]),
            side=Side.SHORT if is_short[j] else Side.LONG,
            limit_price=float(lim[j]),
            stop_offset=sl,
            target_offset=tp,
            max_hold_bars=max_hold,
            work_bars=work,
        )
        for j in range(len(ts))
    ]
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=work)
    return run_signals_bt(
        symbol,
        sc.timeframe,
        sc.ohlcv,
        sigs,
        tag=tag,
        max_hold=max_hold,
        sl=sl,
        market=False,
        n_intent=n_intent,
        fill_pct=float(fill["fill_rate"]),
    )


def run_market_arm(
    symbol: str,
    sc,
    mask: np.ndarray,
    is_short: np.ndarray,
    *,
    tag: str,
    max_hold: int,
    tp: float,
    sl: float,
) -> dict[str, Any]:
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent, "n_trades": 0}
    idx = np.flatnonzero(mask)
    short = np.asarray(is_short, dtype=bool).reshape(-1)
    if short.size != idx.size:
        raise ValueError(f"is_short length {short.size} != gated {idx.size}")
    sigs = [
        Signal(
            ts_ms=int(sc.ts_ms[idx[j]]),
            side=Side.SHORT if short[j] else Side.LONG,
            stop_offset=sl,
            target_offset=tp,
            max_hold_bars=max_hold,
            tag=tag,
        )
        for j in range(len(idx))
    ]
    return run_signals_bt(
        symbol,
        sc.timeframe,
        sc.ohlcv,
        sigs,
        tag=tag,
        max_hold=max_hold,
        sl=sl,
        market=True,
        n_intent=n_intent,
        fill_pct=1.0,
    )


def open_checkpoint(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(path))
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS arms (
            arm_id TEXT PRIMARY KEY,
            symbol TEXT,
            timeframe TEXT,
            horizon INTEGER,
            event TEXT,
            mode TEXT,
            tp REAL,
            sl REAL,
            gate TEXT,
            status TEXT,
            n_trades INTEGER,
            payload TEXT,
            updated_utc TEXT
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS meta (
            k TEXT PRIMARY KEY,
            v TEXT
        )
        """
    )
    con.commit()
    return con


def arm_done(con: sqlite3.Connection, arm_id: str) -> bool:
    row = con.execute("SELECT 1 FROM arms WHERE arm_id=?", (arm_id,)).fetchone()
    return row is not None


def save_arm(con: sqlite3.Connection, arm_id: str, row: dict[str, Any], payload: dict[str, Any]) -> None:
    con.execute(
        """
        INSERT OR REPLACE INTO arms
        (arm_id, symbol, timeframe, horizon, event, mode, tp, sl, gate, status, n_trades, payload, updated_utc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
        """,
        (
            arm_id,
            row.get("symbol"),
            row.get("timeframe"),
            row.get("horizon"),
            row.get("event"),
            row.get("mode"),
            row.get("tp"),
            row.get("sl"),
            row.get("gate"),
            payload.get("status"),
            payload.get("n_trades"),
            json.dumps(jsonable(payload)),
        ),
    )
    con.commit()


def load_arms(con: sqlite3.Connection) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for arm_id, payload in con.execute("SELECT arm_id, payload FROM arms"):
        rec = json.loads(payload)
        rec["arm_id"] = arm_id
        out.append(rec)
    return out
