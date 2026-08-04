"""ABC bounce — one-shot forward-lockbox evaluation (preregistered).

Preregistration: ``configs/preregister/abc_bounce_001.yaml``.

Training diagnostics (D-030) found negative BC-continuation near classical factors.
That window is contaminated for selection. This module evaluates the bounce hypothesis
exactly once on the pristine lockbox, against a volatility-matched random control,
using warehouse ``indicators.legs`` geometry and tradesim only.

Do not tune factor targets, tolerance, hold, or stop after opening the lockbox.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

from llm2.backtest.conformance import run_conformance_check
from llm2.backtest.run import run_strategy_backtest
from llm2.data.loader import load_ohlcv
from llm2.diagnostics.abc_factor import FACTOR_TOL, build_abc_triples, load_legs
from llm2.experiments.pulse_continuation import sequential_entries
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROOT, ensure_artifact_dirs, touch_timeframe
from llm2.registry.db import ResearchDB
from llm2.registry.ledger import append_ledger
from llm2.research_policy import (
    EventStudySpec,
    LockboxPreregGate,
    refuse_abc_bounce_reopen_while_underpowered,
    refuse_abc_continuation_without_lockbox_prereg,
    refuse_wavetheory_simulator_for_abc,
    require_lockbox_prereg_frozen,
    require_matched_control,
    require_warehouse_legs_for_abc,
)
from llm2.validation.folds import index_to_ms

PREREG_PATH = ROOT / "configs" / "preregister" / "abc_bounce_001.yaml"
FAMILY_STATUS_PATH = ARTIFACTS / "reports" / "abc_bounce" / "abc_bounce_001_family_status.json"
MIN_POOLED_TRADES = 50
_PARAMETER_KEYS = (
    "event_definition",
    "entry_rule",
    "exit_design",
    "universe",
    "controls",
    "success_criteria",
)


@dataclass
class ArmResult:
    name: str
    pooled_pf: float = 0.0
    pooled_pnl: float = 0.0
    n_trades: int = 0
    n_signals: int = 0
    gross_profit: float = 0.0
    gross_loss: float = 0.0
    funding_paid: float = 0.0
    fees_paid: float = 0.0
    entry_bar_stops: int = 0
    liquidations: int = 0
    detail: dict[str, Any] = field(default_factory=dict)


def parameter_sha256(cfg: dict[str, Any]) -> str:
    """Digest of frozen trade parameters only (excludes family-status commentary)."""
    payload = {k: cfg.get(k) for k in _PARAMETER_KEYS}
    blob = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def load_family_status(path: Path = FAMILY_STATUS_PATH) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_family_status(payload: dict[str, Any], path: Path = FAMILY_STATUS_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")


def load_prereg(path: Path = PREREG_PATH) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    cfg = yaml.safe_load(text)
    cfg["_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    cfg["_parameter_sha256"] = parameter_sha256(cfg)
    validate_prereg(cfg)
    return cfg


def validate_prereg(cfg: dict[str, Any]) -> None:
    entry = cfg.get("entry_rule") or {}
    exits = cfg.get("exit_design") or {}
    universe = cfg.get("universe") or {}
    controls = cfg.get("controls") or {}
    required = controls.get("required") or []
    control_names = tuple(
        str(c.get("name", "")) for c in required if isinstance(c, dict)
    )
    require_lockbox_prereg_frozen(
        LockboxPreregGate(
            name=str(cfg.get("generation_id", "abc_bounce")),
            status=str(cfg.get("status", "")),
            evaluation=str(universe.get("evaluation", "")),
            frozen_utc=exits.get("frozen_utc"),
            leverage=exits.get("leverage"),
            sl_pct=entry.get("sl_pct"),
            control_policy=str(controls.get("policy", "")),
            control_arm_names=control_names,
        )
    )
    if universe.get("lockbox_start") != FORWARD_LOCKBOX_START:
        raise RuntimeError(
            f"lockbox_start must equal FORWARD_LOCKBOX_START ({FORWARD_LOCKBOX_START})"
        )
    lev = float(exits["leverage"])
    sl = float(entry["sl_pct"])
    ceiling = int(np.floor(1.0 / (sl + 0.005 + 0.002)))
    if lev > ceiling:
        raise RuntimeError(f"leverage {lev} exceeds stop-implied ceiling {ceiling} for sl={sl}")
    if not str(cfg.get("continuation_claim_status", "")).startswith("CLOSED"):
        raise RuntimeError(
            "abc_bounce prereg must keep continuation_claim_status CLOSED "
            "(D-030); this runner evaluates bounce only"
        )
    name = str((cfg.get("entry_rule") or {}).get("name", ""))
    if "continuation" in name.lower():
        refuse_abc_continuation_without_lockbox_prereg(
            claim=name, preregistered_on_lockbox=False
        )
    geom = str((cfg.get("event_definition") or {}).get("geometry", ""))
    require_warehouse_legs_for_abc(geom or "indicators.legs")
    refuse_wavetheory_simulator_for_abc(geom)


def project_sequential_lockbox_trades(cfg: dict[str, Any]) -> int:
    """How many one-position-at-a-time bounce trades the current lockbox would yield."""
    symbol = cfg["universe"]["symbol"]
    timeframe = cfg["universe"]["timeframe"]
    hold = int(cfg["entry_rule"]["hold_bars"])
    ed = cfg["event_definition"]
    targets = tuple(float(x) for x in ed["factor_targets"])
    tol = float(ed["factor_tolerance"])
    lock_start = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    lock_ms = int(lock_start.timestamp() * 1000)
    ohlcv = load_ohlcv(symbol, timeframe)
    legs = load_legs(symbol, timeframe)
    events = bounce_events_from_legs(ohlcv, legs, targets=targets, tol=tol)
    if events.empty:
        return 0
    events = events[events["confirm_ts_ms"] >= lock_ms]
    lb_start_i = int(ohlcv.index.searchsorted(lock_start))
    events = events[events["entry_bar"] >= lb_start_i]
    if events.empty:
        return 0
    bars = (events["entry_bar"].to_numpy(dtype=int) - lb_start_i)
    return int(sequential_entries(bars, hold).size)


def _vol_matched_with_sides(
    ohlcv: pd.DataFrame,
    event_bars: np.ndarray,
    sides: np.ndarray,
    *,
    vol_window: int = 168,
    seed: int = 0,
    tolerance: float = 0.15,
    pool_lo: int | None = None,
    pool_hi: int | None = None,
) -> np.ndarray:
    """Return Nx2 array of [control_bar, inherited_side] vol-matched to each event.

    ``pool_lo`` / ``pool_hi`` restrict eligible control bars (inclusive). For a lockbox
    evaluation the pool must be the lockbox itself — matching from the contaminated train
    window and then dropping those bars leaves a near-empty control.
    """
    if event_bars.size == 0:
        return np.zeros((0, 2), dtype=int)
    close = ohlcv["close"]
    vol = np.log(close).diff().rolling(vol_window, min_periods=vol_window // 2).std().shift(1)
    v = vol.to_numpy()
    rng = np.random.default_rng(seed)
    valid = np.flatnonzero(np.isfinite(v))
    if pool_lo is not None:
        valid = valid[valid >= int(pool_lo)]
    if pool_hi is not None:
        valid = valid[valid <= int(pool_hi)]
    event_set = set(int(b) for b in event_bars)
    rows: list[tuple[int, int]] = []
    for bar, side in zip(event_bars.tolist(), sides.tolist(), strict=True):
        target = v[int(bar)]
        if not np.isfinite(target) or target <= 0:
            continue
        lo, hi = target * (1 - tolerance), target * (1 + tolerance)
        pool = valid[(v[valid] >= lo) & (v[valid] <= hi)]
        pool = np.array([p for p in pool if p not in event_set], dtype=int)
        if pool.size == 0:
            continue
        rows.append((int(rng.choice(pool)), int(side)))
    if not rows:
        return np.zeros((0, 2), dtype=int)
    return np.asarray(rows, dtype=int)


def bounce_events_from_legs(
    ohlcv: pd.DataFrame,
    legs: pd.DataFrame,
    *,
    targets: tuple[float, ...] = (0.618, 1.000, 1.618),
    tol: float = FACTOR_TOL,
) -> pd.DataFrame:
    """Build bounce entry bars: next bar after C confirmation, side = opposite of BC."""
    triples = build_abc_triples(legs)
    if triples.empty:
        return pd.DataFrame()
    f = triples["factor"].to_numpy(dtype=float)
    near = np.zeros(len(triples), dtype=bool)
    for t in targets:
        near |= np.abs(f - float(t)) <= float(tol)
    triples = triples.loc[near].copy()
    if triples.empty:
        return pd.DataFrame()

    close_idx = ohlcv.index.sort_values()
    conf = pd.to_datetime(triples["confirm_time"], utc=True)
    # Bar at or before confirm; entry on the *next* open (confirm bar already closed).
    pos = close_idx.searchsorted(conf, side="right") - 1
    entry_pos = pos + 1
    valid = (pos >= 0) & (entry_pos < len(close_idx))
    triples = triples.loc[valid].copy()
    entry_pos = entry_pos[valid]
    triples["entry_bar"] = entry_pos.astype(int)
    triples["entry_time"] = close_idx[entry_pos]
    # Bounce: opposite of BC direction
    triples["side"] = (-triples["bc_dir"].astype(int)).astype(int)
    triples = triples.drop_duplicates(subset=["entry_bar"], keep="first")
    return triples.reset_index(drop=True)


def _signals_for(
    ts_ms: np.ndarray,
    bars: np.ndarray,
    sides: np.ndarray,
    *,
    sl_pct: float,
    hold_bars: int,
) -> list:
    from tradesim import Side, Signal

    out = []
    for b, side in zip(bars.tolist(), sides.tolist(), strict=True):
        s = Side.LONG if int(side) > 0 else Side.SHORT
        out.append(
            Signal(
                ts_ms=int(ts_ms[int(b)]),
                side=s,
                stop_offset=float(sl_pct),
                target_offset=None,
                max_hold_bars=int(hold_bars),
                tag="abc_bounce",
            )
        )
    return out


def _run_arm(
    *,
    ohlcv: pd.DataFrame,
    touch: pd.DataFrame | None,
    ts_ms: np.ndarray,
    bars: np.ndarray,
    sides: np.ndarray,
    hold: int,
    sl: float,
    leverage: float,
    symbol: str,
    timeframe: str,
    arm_name: str,
    gid: str,
    prereg_sha: str,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    costs: Any,
    margin: Any,
    sizing: Any,
    instrument: Any,
) -> ArmResult:
    from tradesim import REASON_LIQUIDATION, research_sim

    if bars.size == 0:
        return ArmResult(name=arm_name)

    sim = research_sim(max_hold_bars=hold, decision_timeframe=timeframe)
    signals = _signals_for(ts_ms, bars, sides, sl_pct=sl, hold_bars=hold)
    w0 = int(ts_ms[0])
    w1 = int(ts_ms[-1])
    fmask = (funding_ts >= w0) & (funding_ts <= w1)
    touch_tf = touch_timeframe(timeframe, symbol) if touch is not None else None
    bundle = run_strategy_backtest(
        ohlcv,
        signals,
        symbol=symbol,
        timeframe=timeframe,
        strategy_id=f"llm2-{gid}-{arm_name}",
        touch_ohlcv=touch,
        touch_timeframe=touch_tf,
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
            "prereg_sha256": prereg_sha[:16],
        },
        plot=False,
        print_headline=False,
        store_path=None,
    )
    trades = bundle.result.trades
    pnls = np.array([float(t.realized_pnl) for t in trades], dtype=float)
    gp = float(pnls[pnls > 0].sum())
    gl = float(-pnls[pnls < 0].sum())
    entry_bar = sum(1 for t in trades if t.entry_bar_exit)
    liq = sum(1 for t in trades if REASON_LIQUIDATION in str(t.exit_reason))
    return ArmResult(
        name=arm_name,
        pooled_pf=(gp / gl) if gl > 0 else (float("inf") if gp > 0 else 0.0),
        pooled_pnl=float(pnls.sum()),
        n_trades=int(len(trades)),
        n_signals=int(bars.size),
        gross_profit=gp,
        gross_loss=gl,
        funding_paid=float(sum(float(t.funding) for t in trades)),
        fees_paid=float(sum(float(t.fees) for t in trades)),
        entry_bar_stops=int(entry_bar),
        liquidations=int(liq),
        detail={"skips": dict(bundle.result.skip_counts)},
    )


def run_abc_bounce(
    *,
    prereg_path: Path = PREREG_PATH,
    db: ResearchDB | None = None,
    seed: int = 0,
    allow_underpowered_reopen: bool = False,
) -> dict[str, Any]:
    """One-shot lockbox evaluation of the frozen ABC bounce hypothesis."""
    ensure_artifact_dirs()
    cfg = load_prereg(prereg_path)

    # Bounce is the hypothesis — continuation refuse must not block bounce itself.
    # validate_prereg already checked geometry / frozen exits; clear continuation misuse
    # by requiring the prereg not claim continuation success.
    if "bounce" not in str(cfg.get("hypothesis", "")).lower() and cfg.get(
        "entry_rule", {}
    ).get("name") != "bounce_against_bc":
        raise RuntimeError("this runner only evaluates bounce_against_bc")

    family = load_family_status() or {}
    if str(family.get("family_status", "")).upper() in {"UNDERPOWERED", "UNDERPOWERED_HOLD"}:
        frozen_param = (
            (family.get("first_lockbox_open") or {}).get("parameter_sha256")
            or family.get("parameter_sha256")
        )
        if not frozen_param:
            # Bootstrap from the first-open whole-file sha when parameter digest was
            # not recorded yet; subsequent holds use parameter_sha256 only.
            frozen_param = cfg["_parameter_sha256"]
            first = family.setdefault("first_lockbox_open", {})
            first["parameter_sha256"] = frozen_param
            write_family_status(family)
        projected = project_sequential_lockbox_trades(cfg)
        refuse_abc_bounce_reopen_while_underpowered(
            family_status=str(family.get("family_status")),
            prereg_sha256=cfg["_parameter_sha256"],
            frozen_prereg_sha256=str(frozen_param),
            projected_sequential_trades=projected,
            min_pooled_trades=MIN_POOLED_TRADES,
            force=allow_underpowered_reopen,
        )

    stamp = run_conformance_check(quiet=True)
    if not stamp.get("passed"):
        raise RuntimeError(
            "tradesim conformance is not green; no number from this run would be quotable"
        )

    from tradesim import (
        SizingMode,
        research_costs,
        research_margin,
        research_sizing,
    )

    db = db or ResearchDB()
    symbol = cfg["universe"]["symbol"]
    timeframe = cfg["universe"]["timeframe"]
    hold = int(cfg["entry_rule"]["hold_bars"])
    sl = float(cfg["entry_rule"]["sl_pct"])
    leverage = float(cfg["exit_design"]["leverage"])
    gid = cfg["generation_id"]
    ed = cfg["event_definition"]
    targets = tuple(float(x) for x in ed["factor_targets"])
    tol = float(ed["factor_tolerance"])

    require_matched_control(
        EventStudySpec(
            name=gid,
            event_definition=f"ABC factor near {targets} tol={tol} warehouse legs",
            treatment_arm="bounce_against_bc",
            control_arm="volatility_matched_random",
            matching="trailing 168-bar volatility within 15 percent",
        )
    )

    append_ledger(
        f"PREREG {gid} status={cfg.get('status')} sha256={cfg['_sha256'][:16]} "
        f"hold={hold} sl={sl} lev={leverage} eval=forward_lockbox_once "
        f"engine_stamp={stamp['stamp']['fixture_pack_hash'][:12]}",
        tier=0,
    )
    db.create_generation(
        gid,
        max_trials=2,
        hypothesis=str(cfg["hypothesis"])[:500],
        config_hash=cfg["_sha256"][:16],
    )

    lock_start = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv_full = load_ohlcv(symbol, timeframe)
    # Full history for vol matching and chaining AB legs that end before the lockbox.
    ohlcv = ohlcv_full.copy()
    legs = load_legs(symbol, timeframe)
    lock_ms = int(lock_start.timestamp() * 1000)
    ohlcv_lb = ohlcv.loc[ohlcv.index >= lock_start].copy()
    if ohlcv_lb.empty:
        raise RuntimeError("lockbox OHLCV is empty")

    # Build from all legs, then keep triples whose C confirm is inside the lockbox.
    events = bounce_events_from_legs(ohlcv, legs, targets=targets, tol=tol)
    if not events.empty:
        events = events[events["confirm_ts_ms"] >= lock_ms].copy()
    # Restrict entry bars to lockbox range
    lb_start_i = int(ohlcv.index.searchsorted(lock_start))
    if not events.empty:
        events = events[events["entry_bar"] >= lb_start_i].copy()
        # Remap entry_bar to lockbox-local indices for sequential + signals on ohlcv_lb
        events["entry_bar_lb"] = events["entry_bar"] - lb_start_i

    try:
        touch = load_ohlcv(symbol, touch_timeframe(timeframe, symbol))
        touch = touch.loc[touch.index >= lock_start]
    except Exception:  # noqa: BLE001
        touch = None

    from llm2.data.macro import load_funding

    funding = load_funding(symbol)
    funding = funding[funding.index >= lock_start]
    if funding.empty:
        raise RuntimeError(f"no funding history for {symbol} in lockbox; refusing backtest")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)

    ts_ms = index_to_ms(ohlcv_lb.index)
    costs = research_costs()
    margin = research_margin(leverage=leverage)
    sizing = research_sizing()
    if sizing.mode == SizingMode.MIN_EXCHANGE:
        pass
    instrument = None
    try:
        from tradesim import research_instrument

        instrument = research_instrument(symbol)
    except Exception as exc:  # noqa: BLE001
        append_ledger(
            f"ABC_BOUNCE {gid}: instrument unavailable ({exc}); venue checks degraded",
            tier=0,
        )

    if events.empty:
        bounce_bars = np.array([], dtype=int)
        bounce_sides = np.array([], dtype=int)
    else:
        # One position at a time on lockbox-local bars
        raw_bars = events["entry_bar_lb"].to_numpy(dtype=int)
        kept = sequential_entries(raw_bars, hold)
        keep_set = set(int(x) for x in kept)
        mask = np.array([int(b) in keep_set for b in raw_bars], dtype=bool)
        # Prefer first occurrence order from sequential_entries
        order = {int(b): i for i, b in enumerate(kept.tolist())}
        sub = events.loc[mask].copy()
        sub["_ord"] = sub["entry_bar_lb"].map(order)
        sub = sub.sort_values("_ord")
        bounce_bars = sub["entry_bar_lb"].to_numpy(dtype=int)
        bounce_sides = sub["side"].to_numpy(dtype=int)

    # Control: vol-match inside the lockbox only; inherit each event's bounce side.
    full_event_bars = (
        (bounce_bars + lb_start_i) if bounce_bars.size else np.array([], dtype=int)
    )
    ctrl_pairs = _vol_matched_with_sides(
        ohlcv,
        full_event_bars,
        bounce_sides,
        vol_window=168,
        seed=seed,
        tolerance=0.15,
        pool_lo=lb_start_i,
        pool_hi=len(ohlcv) - 1,
    )
    if ctrl_pairs.size == 0:
        ctrl_lb = np.array([], dtype=int)
        ctrl_sides = np.array([], dtype=int)
    else:
        ctrl_lb_raw = (ctrl_pairs[:, 0] - lb_start_i).astype(int)
        ctrl_side_raw = ctrl_pairs[:, 1].astype(int)
        kept = sequential_entries(ctrl_lb_raw, hold)
        keep_set = set(int(x) for x in kept)
        mask = np.array([int(b) in keep_set for b in ctrl_lb_raw], dtype=bool)
        order = {int(b): i for i, b in enumerate(kept.tolist())}
        tmp = pd.DataFrame({"bar": ctrl_lb_raw, "side": ctrl_side_raw})
        tmp = tmp.loc[mask].copy()
        tmp["_ord"] = tmp["bar"].map(order)
        tmp = tmp.sort_values("_ord")
        ctrl_lb = tmp["bar"].to_numpy(dtype=int)
        ctrl_sides = tmp["side"].to_numpy(dtype=int)

    bounce = _run_arm(
        ohlcv=ohlcv_lb,
        touch=touch,
        ts_ms=ts_ms,
        bars=bounce_bars,
        sides=bounce_sides,
        hold=hold,
        sl=sl,
        leverage=leverage,
        symbol=symbol,
        timeframe=timeframe,
        arm_name="bounce",
        gid=gid,
        prereg_sha=cfg["_sha256"],
        funding_ts=funding_ts,
        funding_rt=funding_rt,
        costs=costs,
        margin=margin,
        sizing=sizing,
        instrument=instrument,
    )
    control = _run_arm(
        ohlcv=ohlcv_lb,
        touch=touch,
        ts_ms=ts_ms,
        bars=ctrl_lb,
        sides=ctrl_sides,
        hold=hold,
        sl=sl,
        leverage=leverage,
        symbol=symbol,
        timeframe=timeframe,
        arm_name="random_vol_matched",
        gid=gid,
        prereg_sha=cfg["_sha256"],
        funding_ts=funding_ts,
        funding_rt=funding_rt,
        costs=costs,
        margin=margin,
        sizing=sizing,
        instrument=instrument,
    )

    enough = bounce.n_trades >= MIN_POOLED_TRADES
    underpowered = not enough
    beats_cost = bounce.pooled_pf >= 1.20
    beats_control = (
        bounce.pooled_pf > control.pooled_pf and bounce.pooled_pnl > control.pooled_pnl
    )
    no_liq = bounce.liquidations == 0
    success = bool(enough and beats_cost and beats_control and no_liq)

    if underpowered:
        verdict = "ABC_BOUNCE_UNDERPOWERED"
    elif success:
        verdict = "ABC_BOUNCE_SURVIVES_COSTS"
    else:
        verdict = "ABC_BOUNCE_FAILS_FAMILY_CLOSED"

    for arm in (bounce, control):
        db.register_trial(
            gid,
            tier=2 if success and arm.name == "bounce" else 0,
            symbol=symbol,
            timeframe=timeframe,
            target="abc_bounce",
            feature_space="warehouse_legs",
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
                    "verdict": verdict,
                }
            )[:500],
        )

    append_ledger(
        f"{verdict} {gid}: bounce_pf={bounce.pooled_pf:.4f} pnl={bounce.pooled_pnl:.2f} "
        f"n={bounce.n_trades} | ctrl_pf={control.pooled_pf:.4f} pnl={control.pooled_pnl:.2f} "
        f"n={control.n_trades} | entry_bar_stops={bounce.entry_bar_stops} "
        f"liq={bounce.liquidations} underpowered={underpowered}",
        tier=2 if success else 0,
    )

    out = {
        "status": "COMPLETE",
        "verdict": verdict,
        "success": success,
        "family_closed": (not success) and (not underpowered),
        "underpowered": underpowered,
        "generation_id": gid,
        "prereg_sha256": cfg["_sha256"],
        "engine_stamp": stamp["stamp"],
        "n_raw_events": int(len(events)) if events is not None else 0,
        "arms": {
            "bounce": bounce.__dict__,
            "random_vol_matched": control.__dict__,
        },
        "criteria": {
            "pooled_trades_ge_50": enough,
            "pooled_pf_ge_1_20": beats_cost,
            "beats_vol_matched_control": beats_control,
            "no_liquidation": no_liq,
        },
        "readiness": "RESEARCH_ONLY",
        "stamped_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
    }

    out_dir = ARTIFACTS / "reports" / "abc_bounce"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp_s = out["stamped_utc"]
    json_path = out_dir / f"abc_bounce_{symbol}_{stamp_s}.json"
    md_path = out_dir / f"abc_bounce_{symbol}_{stamp_s}.md"
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(f"# ABC bounce lockbox — {symbol} ({stamp_s})\n\n")
        fh.write(f"**Readiness: RESEARCH_ONLY.** Verdict: `{verdict}`\n\n")
        fh.write(f"- prereg sha256: `{cfg['_sha256']}`\n")
        fh.write(f"- success: {success}, family_closed: {out['family_closed']}, "
                 f"underpowered: {underpowered}\n")
        fh.write(
            f"- bounce: PF={bounce.pooled_pf:.4f} pnl={bounce.pooled_pnl:.2f} "
            f"n={bounce.n_trades} fees={bounce.fees_paid:.2f} funding={bounce.funding_paid:.2f} "
            f"entry_bar_stops={bounce.entry_bar_stops} liq={bounce.liquidations}\n"
        )
        fh.write(
            f"- control: PF={control.pooled_pf:.4f} pnl={control.pooled_pnl:.2f} "
            f"n={control.n_trades}\n"
        )
        fh.write(
            "\nGeometry: warehouse `indicators.legs`. Engine: tradesim. "
            "No wavetheory simulator (D-026). Continuation claim remains CLOSED.\n"
        )
    out["report_json"] = str(json_path)
    out["report_md"] = str(md_path)

    # Persist family hold — UNDERPOWERED stays open; success/failure close or promote.
    if underpowered:
        fam_status = "UNDERPOWERED_HOLD"
    elif success:
        fam_status = "LOCKBOX_PASS_CANDIDATE"
    else:
        fam_status = "CLOSED"
    write_family_status(
        {
            "generation_id": gid,
            "family_status": fam_status,
            "readiness": "RESEARCH_ONLY",
            "parameter_sha256": cfg["_parameter_sha256"],
            "prereg_sha256_text": cfg["_sha256"],
            "first_lockbox_open": {
                "report": str(md_path),
                "verdict": verdict,
                "n_trades": bounce.n_trades,
                "bounce_pf": bounce.pooled_pf,
                "control_pf": control.pooled_pf,
                "parameter_sha256": cfg["_parameter_sha256"],
                "prereg_sha256_text": cfg["_sha256"],
            },
            "reopen_policy": (
                "Second frozen one-shot only when the same parameter digest projects "
                ">= 50 sequential lockbox trades. Do not widen factor_tolerance."
            ),
            "continuation_claim_status": "CLOSED_unless_separate_lockbox_prereg",
        }
    )
    return out
