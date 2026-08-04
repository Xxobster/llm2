"""Pulse-continuation experiment: does an up-pulse predict the next 96 bars?

Preregistration: ``configs/preregister/diag001_pulse_continuation.yaml``.

The hypothesis is the only diagnostic survivor with an effect size meaningfully above the
round trip: 87 bps of 96-bar forward return after an upward three-sigma pulse, against a
16 bps cost. That gap is what makes it worth a tradesim run; everything else that survived
false-discovery control was a correlation near 0.04, which cannot pay for itself.

Three arms are run, and the third is the one that matters:

``pulse``
    Long on the open after an upward pulse bar closes.
``random``
    The control the preregistration demands. Entries drawn at random from bars matched to
    the pulse bars on trailing volatility, same count, same hold, same costs. Without it, a
    positive result proves only that BTCUSDT rose over the sample.
``down_pulse``
    Downward pulses, which the diagnostics said do *not* continue (q = 0.34). This is a
    negative control: if it also prints a profit, the pulse flag is not what is being
    measured and both arms are drift.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

from llm2.backtest.conformance import run_conformance_check
from llm2.backtest.run import run_strategy_backtest
from llm2.data.loader import load_ohlcv
from llm2.diagnostics.events import detect_pulses
from llm2.paths import FORWARD_LOCKBOX_START, ROOT, ensure_artifact_dirs, touch_timeframe
from llm2.registry.db import ResearchDB
from llm2.registry.ledger import append_ledger
from llm2.validation.folds import build_outer_folds, index_to_ms

PREREG_PATH = ROOT / "configs" / "preregister" / "diag001_pulse_continuation.yaml"

MIN_TRADES_PER_FOLD = 10
MIN_POOLED_TRADES = 50


@dataclass
class ArmResult:
    name: str
    pooled_pf: float = 0.0
    pooled_pnl: float = 0.0
    n_trades: int = 0
    fold_rows: list[dict[str, Any]] = field(default_factory=list)
    gross_profit: float = 0.0
    gross_loss: float = 0.0
    funding_paid: float = 0.0
    fees_paid: float = 0.0
    entry_bar_stops: int = 0
    liquidations: int = 0


def load_prereg(path: Path = PREREG_PATH) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    cfg = yaml.safe_load(text)
    cfg["_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    validate_prereg(cfg)
    return cfg


def validate_prereg(cfg: dict[str, Any]) -> None:
    """Refuse to run a preregistration whose exits or folds were never frozen."""
    entry = cfg.get("entry_rule") or {}
    exits = cfg.get("exit_design") or {}
    folds = cfg.get("fold_design") or {}
    if entry.get("sl_pct") is None:
        raise RuntimeError(
            "entry_rule.sl_pct is null. Freeze the stop from volatility BEFORE running, "
            "or the first result becomes the thing that chooses it."
        )
    if not exits.get("frozen_utc") or not exits.get("leverage"):
        raise RuntimeError("exit_design must record frozen_utc and leverage before any run")
    if not folds.get("design_hash"):
        raise RuntimeError(
            "fold_design.design_hash is missing. Run scripts/design_pulse_folds.py and "
            "freeze the geometry from event counts before opening out-of-sample."
        )
    lev = float(exits["leverage"])
    sl = float(entry["sl_pct"])
    ceiling = int(np.floor(1.0 / (sl + 0.005 + 0.002)))
    if lev > ceiling:
        raise RuntimeError(
            f"leverage {lev} exceeds the stop-implied ceiling {ceiling} for sl={sl}; "
            "the stop would sit outside liquidation"
        )


def volatility_matched_control(
    ohlcv: pd.DataFrame,
    event_bars: np.ndarray,
    *,
    vol_window: int = 168,
    seed: int = 0,
    tolerance: float = 0.15,
) -> np.ndarray:
    """Random entry bars matched to the events on trailing volatility.

    A uniformly random control would be the wrong comparison. Pulses do not occur at random
    moments; they cluster in volatile regimes, and volatile regimes have their own drift and
    their own cost profile. Sampling the control from bars whose trailing volatility is
    within ``tolerance`` of each event's therefore asks the right question: given that we
    are in this kind of market, does the pulse itself add anything?
    """
    close = ohlcv["close"]
    vol = np.log(close).diff().rolling(vol_window, min_periods=vol_window // 2).std().shift(1)
    v = vol.to_numpy()
    rng = np.random.default_rng(seed)

    valid = np.flatnonzero(np.isfinite(v))
    event_set = set(int(b) for b in event_bars)
    picks: list[int] = []
    for bar in event_bars:
        target = v[int(bar)]
        if not np.isfinite(target) or target <= 0:
            continue
        lo, hi = target * (1 - tolerance), target * (1 + tolerance)
        pool = valid[(v[valid] >= lo) & (v[valid] <= hi)]
        pool = np.array([p for p in pool if p not in event_set], dtype=int)
        if pool.size == 0:
            continue
        picks.append(int(rng.choice(pool)))
    return np.unique(np.array(sorted(picks), dtype=int))


def sequential_entries(bars: np.ndarray, hold_bars: int) -> np.ndarray:
    """Drop signals that fire while a position from an earlier signal is still open."""
    kept, busy_until = [], -(10**9)
    for b in np.sort(np.asarray(bars, dtype=int)):
        if b >= busy_until:
            kept.append(int(b))
            busy_until = int(b) + hold_bars
    return np.array(kept, dtype=int)


def _signals_for(
    ts_ms: np.ndarray, bars: np.ndarray, *, side: int, sl_pct: float, hold_bars: int
) -> list:
    from tradesim import Side, Signal

    s = Side.LONG if side > 0 else Side.SHORT
    return [
        Signal(
            ts_ms=int(ts_ms[b]),
            side=s,
            stop_offset=float(sl_pct),
            target_offset=None,
            max_hold_bars=int(hold_bars),
            tag="pulse",
        )
        for b in bars
    ]


def _summarise(rows: list[dict[str, Any]], name: str) -> ArmResult:
    gp = float(sum(r["gross_profit"] for r in rows))
    gl = float(sum(r["gross_loss"] for r in rows))
    return ArmResult(
        name=name,
        # Pooled profit factor: pooled gross profit over absolute pooled gross loss. Never
        # the mean of the per-fold values, which would let one thin fold dominate.
        pooled_pf=(gp / gl) if gl > 0 else (float("inf") if gp > 0 else 0.0),
        pooled_pnl=float(sum(r["pnl"] for r in rows)),
        n_trades=int(sum(r["n"] for r in rows)),
        fold_rows=rows,
        gross_profit=gp,
        gross_loss=gl,
        funding_paid=float(sum(r.get("funding", 0.0) for r in rows)),
        fees_paid=float(sum(r.get("fees", 0.0) for r in rows)),
        entry_bar_stops=int(sum(r.get("entry_bar_stops", 0) for r in rows)),
        liquidations=int(sum(r.get("liquidations", 0) for r in rows)),
    )


def run_pulse_continuation(
    *,
    prereg_path: Path = PREREG_PATH,
    db: ResearchDB | None = None,
    seed: int = 0,
) -> dict[str, Any]:
    """Nested walk-forward tradesim evaluation of the frozen pulse hypothesis."""
    ensure_artifact_dirs()
    cfg = load_prereg(prereg_path)

    stamp = run_conformance_check(quiet=True)
    if not stamp.get("passed"):
        raise RuntimeError(
            "tradesim conformance is not green; no number from this run would be quotable"
        )

    from tradesim import (
        REASON_LIQUIDATION,
        SizingMode,
        research_costs,
        research_margin,
        research_sim,
        research_sizing,
    )

    db = db or ResearchDB()
    symbol = cfg["universe"]["symbol"]
    timeframe = cfg["universe"]["timeframe"]
    pd_cfg = cfg["pulse_definition"]
    hold = int(cfg["entry_rule"]["hold_bars"])
    sl = float(cfg["entry_rule"]["sl_pct"])
    leverage = float(cfg["exit_design"]["leverage"])
    gid = cfg["generation_id"]

    from llm2.research_policy import EventStudySpec, require_matched_control

    require_matched_control(
        EventStudySpec(
            name=gid,
            event_definition=(
                f"{pd_cfg['threshold_sigma']}-sigma pulse over {pd_cfg['lookback_bars']} bars"
            ),
            treatment_arm="long_after_up_pulse",
            control_arm="random_vol_matched",
            matching=(
                f"trailing volatility within 15 percent "
                f"(vol_window={pd_cfg['vol_window_bars']})"
            ),
        )
    )

    append_ledger(
        f"PREREG {gid} status={cfg.get('status')} sha256={cfg['_sha256'][:16]} "
        f"fold_design={cfg['fold_design']['design_hash']} hold={hold} sl={sl} lev={leverage} "
        f"engine_stamp={stamp['stamp']['fixture_pack_hash'][:12]}",
        tier=0,
    )
    db.create_generation(
        gid, max_trials=3, hypothesis=str(cfg["hypothesis"])[:500],
        config_hash=cfg["_sha256"][:16],
    )

    ohlcv = load_ohlcv(symbol, timeframe)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    ts_ms = index_to_ms(ohlcv.index)

    try:
        touch = load_ohlcv(symbol, touch_timeframe(timeframe, symbol))
        touch = touch.loc[index_to_ms(touch.index) < lock_ms]
    except Exception:  # noqa: BLE001
        touch = None

    # Funding is not optional here. A 96-bar hold on a 1h timeframe spans four days, which
    # is up to twelve eight-hourly settlements. Running without it silently deletes a cost
    # of the same order as the 87 bps effect being tested, so a missing warehouse must stop
    # the run rather than quietly produce a flattering number.
    from llm2.data.macro import load_funding

    funding = load_funding(symbol)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    if funding.empty:
        raise RuntimeError(f"no funding history for {symbol}; refusing to backtest a 96-bar hold")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)

    pulses = detect_pulses(
        ohlcv,
        lookback=int(pd_cfg["lookback_bars"]),
        vol_window=int(pd_cfg["vol_window_bars"]),
        threshold_sigma=float(pd_cfg["threshold_sigma"]),
        min_gap=int(pd_cfg["min_gap_bars"]),
    )
    up_bars = pulses.loc[pulses["direction"] > 0, "bar"].to_numpy(dtype=int)
    down_bars = pulses.loc[pulses["direction"] < 0, "bar"].to_numpy(dtype=int)
    ctrl_bars = volatility_matched_control(
        ohlcv, up_bars, vol_window=int(pd_cfg["vol_window_bars"]), seed=seed
    )

    arms_bars = {
        "pulse": (sequential_entries(up_bars, hold), 1),
        "random_vol_matched": (sequential_entries(ctrl_bars, hold), 1),
        "down_pulse": (sequential_entries(down_bars, hold), 1),
    }

    folds = build_outer_folds(ts_ms, purge_bars=hold, embargo_bars=hold)
    costs = research_costs()
    margin = research_margin(leverage=leverage)
    sizing = research_sizing()
    if sizing.mode == SizingMode.MIN_EXCHANGE:
        pass  # smallest venue-legal order; quantity comes from the instrument spec

    instrument = None
    try:
        from tradesim import research_instrument

        instrument = research_instrument(symbol)
    except Exception as exc:  # noqa: BLE001
        append_ledger(
            f"PULSE {gid}: instrument spec unavailable ({exc}); quantity rounding falls back "
            "to engine defaults and order feasibility is NOT venue-checked",
            tier=0,
        )

    results: dict[str, ArmResult] = {}
    for arm_name, (bars_all, side) in arms_bars.items():
        rows: list[dict[str, Any]] = []
        for fold in folds:
            oos = fold.oos_indices
            lo, hi = int(oos[0]), int(oos[-1])
            in_fold = bars_all[(bars_all >= lo) & (bars_all <= hi)]
            if in_fold.size == 0:
                rows.append({"fold": fold.fold_index, "n": 0, "pnl": 0.0,
                             "gross_profit": 0.0, "gross_loss": 0.0})
                continue

            # The window must extend past the last entry so a 96-bar hold can resolve
            # inside the data instead of being closed by end-of-data.
            end = min(len(ohlcv) - 1, hi + hold + 5)
            window = ohlcv.iloc[max(0, lo - 300) : end + 1]
            touch_tf = touch_timeframe(timeframe, symbol)
            touch_win = None
            if touch is not None:
                touch_win = touch.loc[window.index[0] : window.index[-1]]

            sim = research_sim(max_hold_bars=hold, decision_timeframe=timeframe)
            signals = _signals_for(
                ts_ms, in_fold, side=side, sl_pct=sl, hold_bars=hold
            )
            w0 = int(index_to_ms(window.index)[0])
            w1 = int(index_to_ms(window.index)[-1])
            fmask = (funding_ts >= w0) & (funding_ts <= w1)
            bundle = run_strategy_backtest(
                window,
                signals,
                symbol=symbol,
                timeframe=timeframe,
                strategy_id=f"llm2-{gid}-{arm_name}-f{fold.fold_index}",
                touch_ohlcv=touch_win,
                touch_timeframe=touch_tf if touch_win is not None else None,
                funding_ts_ms=funding_ts[fmask],
                funding_rate=funding_rt[fmask],
                costs=costs,
                margin=margin,
                sizing=sizing,
                sim=sim,
                instrument=instrument,
                strategy_meta={
                    "name": arm_name,
                    "batch": gid,
                    "sl_pct": sl,
                    "tp_pct": None,
                    "hold_bars": hold,
                    "leverage": leverage,
                    "prereg_sha256": cfg["_sha256"][:16],
                },
                plot=False,
                print_headline=False,
                store_path=None,
            )
            trades = bundle.result.trades
            # ``realized_pnl`` is net of fees, funding and slippage; ``gross_pnl`` is not.
            # Profit factor must be built from the net figure or the costs never appear.
            pnls = np.array([float(t.realized_pnl) for t in trades], dtype=float)
            entry_bar = sum(1 for t in trades if t.entry_bar_exit)
            liq = sum(1 for t in trades if REASON_LIQUIDATION in str(t.exit_reason))
            rows.append(
                {
                    "fold": fold.fold_index,
                    "n": int(len(trades)),
                    "signals": int(in_fold.size),
                    "pnl": float(pnls.sum()),
                    "gross_profit": float(pnls[pnls > 0].sum()),
                    "gross_loss": float(-pnls[pnls < 0].sum()),
                    "fees": float(sum(float(t.fees) for t in trades)),
                    "funding": float(sum(float(t.funding) for t in trades)),
                    "slippage": float(sum(float(t.slippage_cost) for t in trades)),
                    "exit_reasons": dict(
                        pd.Series([str(t.exit_reason) for t in trades]).value_counts()
                    ),
                    "entry_bar_stops": entry_bar,
                    "liquidations": liq,
                    "skips": dict(bundle.result.skip_counts),
                }
            )
        results[arm_name] = _summarise(rows, arm_name)

    pulse = results["pulse"]
    control = results["random_vol_matched"]
    down = results["down_pulse"]

    fold_counts = [r["n"] for r in pulse.fold_rows]
    enough = (
        len(fold_counts) >= 5
        and all(c >= MIN_TRADES_PER_FOLD for c in fold_counts)
        and pulse.n_trades >= MIN_POOLED_TRADES
    )
    beats_cost = pulse.pooled_pf > 1.20
    beats_control = pulse.pooled_pf > control.pooled_pf and pulse.pooled_pnl > control.pooled_pnl
    success = bool(enough and beats_cost and beats_control)

    for arm in results.values():
        db.register_trial(
            gid,
            tier=2 if success and arm.name == "pulse" else 0,
            symbol=symbol,
            timeframe=timeframe,
            target="pulse_continuation",
            feature_space="event",
            model=f"frozen_rule::{arm.name}",
            outer_pf=arm.pooled_pf,
            outer_trades=arm.n_trades,
            status="completed",
            notes=str(
                {
                    "pooled_pnl": arm.pooled_pnl,
                    "entry_bar_stops": arm.entry_bar_stops,
                    "liquidations": arm.liquidations,
                    "prereg_sha256": cfg["_sha256"][:16],
                    "engine_fixture": stamp["stamp"]["fixture_pack_hash"][:12],
                }
            )[:500],
        )

    verdict = "PULSE_SURVIVES_COSTS" if success else "PULSE_FAILS_ON_COST"
    append_ledger(
        f"{verdict} {gid}: pulse_pf={pulse.pooled_pf:.4f} pnl={pulse.pooled_pnl:.2f} "
        f"n={pulse.n_trades} | ctrl_pf={control.pooled_pf:.4f} pnl={control.pooled_pnl:.2f} "
        f"n={control.n_trades} | down_pf={down.pooled_pf:.4f} n={down.n_trades} | "
        f"entry_bar_stops={pulse.entry_bar_stops} liq={pulse.liquidations} "
        f"folds_ok={enough}",
        tier=2 if success else 0,
    )

    return {
        "status": "COMPLETE",
        "verdict": verdict,
        "success": success,
        "generation_id": gid,
        "prereg_sha256": cfg["_sha256"],
        "fold_design_hash": cfg["fold_design"]["design_hash"],
        "engine_stamp": stamp["stamp"],
        "arms": {k: v.__dict__ for k, v in results.items()},
        "criteria": {
            "enough_trades": enough,
            "pooled_pf_above_1_20": beats_cost,
            "beats_vol_matched_control": beats_control,
            "fold_trade_counts": fold_counts,
        },
    }
