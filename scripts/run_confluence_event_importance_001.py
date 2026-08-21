"""Oracle event-importance vs current pivot 15m controls.

RESEARCH_ONLY. Oracle uses the true future event bit — never promote as live edge.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

from tradesim import Side, Signal, research_instrument, research_margin, research_sizing  # noqa: E402
from tradesim import research_sim, research_sim_limit_entry  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.confluence.events import (  # noqa: E402
    CONTINUATION_EVENTS,
    EVENT_IDS,
    MARKET_ENTRY_EVENTS,
    REVERSAL_EVENTS,
    build_event_pack,
    build_features_for_guard,
)
from llm2.confluence.importance import (  # noqa: E402
    EBR_CAP,
    event_correlation,
    promote_rule,
    prune_duplicates,
    signed_return_effects,
)
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.features.packs import build_feature_frame  # noqa: E402
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

PREREG = _ROOT / "configs" / "preregister" / "confluence_event_pack_001.yaml"
TP = SL = 0.01
MAX_ROWS = 120_000
PACK = "level_vsa"
TF = "15m"
SYMBOLS = ("ETHUSDT", "SOLUSDT", "BTCUSDT")
HORIZONS = (4, 8)
_INSTRUMENT: dict[str, object] = {}


def _instrument(symbol: str):
    inst = _INSTRUMENT.get(symbol)
    if inst is None:
        inst = research_instrument(symbol, refresh_if_missing=False, max_age_ms=10**15)
        _INSTRUMENT[symbol] = inst
    return inst


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _leak_confluence(symbol: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = load_ohlcv(symbol, TF)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-6000:].copy()
        require_clean_audit(
            run_leakage_audit(
                ohlcv=ohlcv,
                build_features=build_features_for_guard,
                interval=TF,
                symbol=symbol,
                timeframe=TF,
            )
        )
        return {"symbol": symbol, "builder": "confluence_known_now", "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "status": "FAIL", "error": str(exc)[:400]}


def _leak_pivot(symbol: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = load_ohlcv(symbol, TF)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-6000:].copy()

        def _b(df, **_k):
            return build_feature_frame(df, pack=PACK)

        require_clean_audit(
            run_leakage_audit(
                ohlcv=ohlcv, build_features=_b, interval=TF, symbol=symbol, timeframe=TF
            )
        )
        return {"symbol": symbol, "builder": PACK, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "status": "FAIL", "error": str(exc)[:400]}


def _span_months(ohlcv: pd.DataFrame) -> float:
    if ohlcv is None or len(ohlcv) < 2:
        return float("nan")
    days = float((ohlcv.index[-1] - ohlcv.index[0]).total_seconds() / 86400.0)
    return days / 30.44 if days > 0 else float("nan")


def _bt(symbol, tf, ohlcv, signals, *, tag: str, max_hold: int, sl: float, market: bool):
    if len(signals) < 12:
        return {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(tf, symbol)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    touch = load_ohlcv(symbol, touch_tf)
    touch = touch.loc[touch.index < lock]
    funding = load_funding(symbol)
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
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[tf])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
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
        instrument=_instrument(symbol),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=False,
        print_headline=False,
        store_path=None,
    )
    m = bundle.metrics
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    holds = [float(getattr(t, "hold_bars", 1)) for t in trades] if trades else []
    ebr = float(np.mean(np.asarray(holds) <= 0)) if holds else float("nan")
    months = _span_months(ohlcv)
    n_tr = int(m.n_trades)
    return {
        "status": "RAN",
        "n_trades": n_tr,
        "profit_factor": float(m.profit_factor),
        "win_rate": float(m.win_rate),
        "net_pnl": float(m.net_pnl),
        "expectancy": float(m.expectancy),
        "entry_bar_exit_rate": ebr,
        "trades_per_month": float(n_tr / months) if months and np.isfinite(months) else float("nan"),
    }


def _p80_mask(sc) -> tuple[np.ndarray, float]:
    base = gate_mask(sc, mode="p75", tp=TP, sl=SL)
    p = np.asarray(sc.p_any, dtype=float)
    idx = np.flatnonzero(base)
    cut = max(30, int(0.7 * idx.size)) if idx.size else 30
    thr_floor = float(np.nanmedian(sc.thr_any[idx[:cut]])) if idx.size else 0.35
    train_p = p[idx[:cut]] if idx.size else p
    train_p = train_p[np.isfinite(train_p)]
    thr_ceil = float(np.nanpercentile(train_p, 80)) if train_p.size else 0.5
    thr = thr_ceil if thr_ceil > thr_floor else thr_floor
    return base & np.isfinite(p) & (p >= thr), thr


def _atr_clip(sc, lo=0.8, hi=1.5) -> np.ndarray:
    lr = np.asarray(sc.level_ret, dtype=float)
    atr = np.asarray(sc.atr_frac, dtype=float)
    out = np.sign(lr) * np.clip(np.abs(lr), lo * atr, hi * atr)
    out[~np.isfinite(lr) | ~np.isfinite(atr)] = np.nan
    return out


def _control_mask(symbol: str, sc) -> tuple[np.ndarray, np.ndarray | None]:
    if symbol == "BTCUSDT":
        mask, _ = _p80_mask(sc)
        return mask, None
    base = gate_mask(sc, mode="p75", tp=TP, sl=SL)
    if symbol == "SOLUSDT":
        return base, _atr_clip(sc)
    return base, None


def _align(sc, pack) -> tuple[np.ndarray, dict[str, np.ndarray], dict[str, np.ndarray]]:
    bar_ts = index_to_ms(sc.ohlcv.index)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
    idx = np.array([pos.get(int(t), -1) for t in sc.ts_ms], dtype=np.int64)
    ok = idx >= 0
    labs: dict[str, np.ndarray] = {}
    sides: dict[str, np.ndarray] = {}
    for eid in EVENT_IDS:
        lab = np.full(len(sc.ts_ms), np.nan)
        sd = np.full(len(sc.ts_ms), np.nan)
        lab[ok] = pack.labels[eid].to_numpy(dtype=float)[idx[ok]]
        sd[ok] = pack.side[eid].to_numpy(dtype=float)[idx[ok]]
        labs[eid] = lab
        sides[eid] = sd
    return idx, labs, sides


def _limit_from_atr(sc, mask: np.ndarray, is_short: np.ndarray) -> np.ndarray:
    idx = np.flatnonzero(mask)
    c = sc.close[idx]
    atr = sc.atr_frac[idx]
    move = np.clip(np.where(np.isfinite(atr), atr, 0.005), 0.0015, 0.03)
    short = is_short[idx] if is_short.shape == sc.close.shape else np.asarray(is_short).reshape(-1)
    return np.where(short, c * (1.0 + move), c * (1.0 - move))


def _run_limit(symbol, sc, mask, is_short, lim, *, tag: str, work: int) -> dict:
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent}
    ts = sc.ts_ms[np.flatnonzero(mask)]
    h = int(getattr(sc, "horizon_bars", 4) or 4)
    max_hold = h + 2
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[j]),
            side=Side.SHORT if is_short[j] else Side.LONG,
            limit_price=float(lim[j]),
            stop_offset=SL,
            target_offset=TP,
            max_hold_bars=max_hold,
            work_bars=work,
        )
        for j in range(len(ts))
    ]
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=work)
    res = _bt(symbol, sc.timeframe, sc.ohlcv, sigs, tag=tag, max_hold=max_hold, sl=SL, market=False)
    out = {"tag": tag, "n_intent": n_intent, "fill_pct": float(fill["fill_rate"]), **res}
    if out.get("status") == "RAN" and n_intent > 0:
        out["expectancy_intent_all"] = float(out["net_pnl"]) / n_intent
    return out


def _run_market(symbol, sc, mask, is_short, *, tag: str) -> dict:
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent}
    idx = np.flatnonzero(mask)
    h = int(getattr(sc, "horizon_bars", 4) or 4)
    max_hold = h + 2
    sigs = [
        Signal(
            ts_ms=int(sc.ts_ms[i]),
            side=Side.SHORT if is_short[i] else Side.LONG,
            stop_offset=SL,
            target_offset=TP,
            max_hold_bars=max_hold,
            tag=tag,
        )
        for i in idx
    ]
    res = _bt(symbol, sc.timeframe, sc.ohlcv, sigs, tag=tag, max_hold=max_hold, sl=SL, market=True)
    out = {"tag": tag, "n_intent": n_intent, "fill_pct": 1.0, **res}
    if out.get("status") == "RAN" and n_intent > 0:
        out["expectancy_intent_all"] = float(out["net_pnl"]) / n_intent
    return out


def _jsonable(x):
    if isinstance(x, dict):
        return {str(k): _jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_jsonable(v) for v in x]
    if isinstance(x, (np.floating, float)):
        v = float(x)
        return v if np.isfinite(v) else None
    if isinstance(x, (np.integer, int)):
        return int(x)
    if isinstance(x, (np.bool_, bool)):
        return bool(x)
    return x


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    prereg_sha = _sha(PREREG)
    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    text = PREREG.read_text(encoding="utf-8")
    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(text.rstrip() + f"\n\npreregister_sha256_at_run: {prereg_sha}\n", encoding="utf-8")
    append_ledger(f"CONFLUENCE_EVENT_IMPORTANCE_001 start {stamp}", tier=0)
    print(f"preregister_sha256={prereg_sha}", flush=True)

    leak = [_leak_confluence(s) for s in SYMBOLS] + [_leak_pivot(s) for s in SYMBOLS]
    print("leakage", leak, flush=True)

    out_dir = ARTIFACTS / "reports" / "confluence"
    out_dir.mkdir(parents=True, exist_ok=True)

    report: dict = {
        "generation_id": "confluence_event_pack_001",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "not_live": True,
        "oracle_never_promote": True,
        "preregister": "configs/preregister/confluence_event_pack_001.yaml",
        "preregister_sha256": prereg_sha,
        "leakage": leak,
        "symbols": {},
        "survivors": [],
    }

    for symbol in SYMBOLS:
        print(f"=== {symbol} score_oos ===", flush=True)
        level_mode = "q50" if symbol == "ETHUSDT" else "ret"
        work = 5 if symbol == "SOLUSDT" else 4
        sc = score_symbol_oos(
            symbol,
            timeframe=TF,
            horizon_bars=4,
            feature_pack=PACK,
            max_rows=MAX_ROWS,
            level_mode=level_mode,
            predict_next=False,
        )
        ctrl_mask, level_override = _control_mask(symbol, sc)
        if level_override is not None:
            old = sc.level_ret
            sc.level_ret = level_override
            ts, is_short, lim = limit_price_side(sc, ctrl_mask)
            sc.level_ret = old
        else:
            ts, is_short, lim = limit_price_side(sc, ctrl_mask)
        ctrl = _run_limit(
            symbol, sc, ctrl_mask, is_short, lim, tag=f"{symbol}_control", work=work
        )
        print(f"  control {ctrl.get('status')} n={ctrl.get('n_trades')} PF={ctrl.get('profit_factor')}", flush=True)

        pivot_side = np.where(sc.p_high >= 0.5, -1.0, 1.0)
        close = sc.ohlcv["close"].to_numpy(dtype=float)

        sym_block: dict = {"control": ctrl, "horizons": {}}
        survivors_here: list[dict] = []

        for h in HORIZONS:
            print(f"  event pack H={h}", flush=True)
            pack = build_event_pack(sc.ohlcv, horizon=h)
            _, labs, sides = _align(sc, pack)
            corr = event_correlation(pack.labels)
            effects = signed_return_effects(close, pack.side, horizon=h)
            q_map = {e.name: e.q_value for e in effects}
            effect_rows = [
                {
                    "name": e.name,
                    "mean_bps": e.detail.get("mean_bps"),
                    "n": e.n,
                    "p_value": e.p_value,
                    "q_value": e.q_value,
                    "significant": e.significant,
                }
                for e in effects
            ]

            arms: list[dict] = []
            intent_exp_and: dict[str, float] = {}
            for eid in EVENT_IDS:
                lab = labs[eid]
                sd = sides[eid]
                ev_mask = np.isfinite(lab) & (lab >= 0.5) & (sd != 0)
                is_short_ev = sd < 0
                tag_a = f"{eid}_H{h}_alone"
                tag_c = f"{eid}_H{h}_and_ctrl"
                if eid in MARKET_ENTRY_EVENTS:
                    alone = _run_market(symbol, sc, ev_mask, is_short_ev, tag=tag_a)
                else:
                    lim_ev = _limit_from_atr(sc, ev_mask, is_short_ev)
                    alone = _run_limit(
                        symbol, sc, ev_mask, is_short_ev[np.flatnonzero(ev_mask)], lim_ev, tag=tag_a, work=work
                    )
                match = ev_mask & ctrl_mask & (np.sign(sd) == np.sign(pivot_side))
                if level_override is not None:
                    old = sc.level_ret
                    sc.level_ret = level_override
                    _, is_s_m, lim_m = limit_price_side(sc, match)
                    sc.level_ret = old
                else:
                    _, is_s_m, lim_m = limit_price_side(sc, match)
                and_arm = _run_limit(symbol, sc, match, is_s_m, lim_m, tag=tag_c, work=work)
                intent_exp_and[eid] = float(and_arm.get("expectancy_intent_all") or -1e9)
                family = "continuation" if eid in CONTINUATION_EVENTS else "reversal"
                arms.append(
                    {
                        "event": eid,
                        "family": family,
                        "entry": "market" if eid in MARKET_ENTRY_EVENTS else "limit",
                        "alone": alone,
                        "and_control": and_arm,
                    }
                )
                print(
                    f"    {eid} alone={alone.get('status')} n={alone.get('n_trades')} "
                    f"AND={and_arm.get('status')} n={and_arm.get('n_trades')} "
                    f"exp_i={and_arm.get('expectancy_intent_all')}",
                    flush=True,
                )

            pruned = prune_duplicates(corr, intent_exp_and)
            dropped = {d["dropped"] for d in pruned["dropped"]}
            promotions = {}
            for arm in arms:
                eid = arm["event"]
                promotions[eid] = promote_rule(
                    control=ctrl,
                    arm=arm["and_control"],
                    q_value=float(q_map.get(eid, float("nan"))),
                    duplicate=eid in dropped,
                )
                if promotions[eid]["promote"]:
                    survivors_here.append(
                        {
                            "symbol": symbol,
                            "event": eid,
                            "horizon": h,
                            "family": arm["family"],
                            "and_control": arm["and_control"],
                            "promotion": promotions[eid],
                        }
                    )

            sym_block["horizons"][str(h)] = {
                "correlation": {
                    a: {b: (None if not np.isfinite(corr.loc[a, b]) else float(corr.loc[a, b])) for b in corr.columns}
                    for a in corr.columns
                },
                "signed_return_fdr": effect_rows,
                "duplicate_prune": pruned,
                "arms": arms,
                "promotions_and_vs_control": promotions,
            }

        # Keep at most one H per event (inner intent expectancy).
        best: dict[str, dict] = {}
        for row in survivors_here:
            eid = row["event"]
            prev = best.get(eid)
            if prev is None or float(row["and_control"].get("expectancy_intent_all") or -1e9) > float(
                prev["and_control"].get("expectancy_intent_all") or -1e9
            ):
                best[eid] = row
        sym_block["survivors"] = list(best.values())
        report["symbols"][symbol] = sym_block
        report["survivors"].extend(list(best.values()))
        print(f"  survivors {symbol}: {[r['event'] for r in best.values()]}", flush=True)

    report = _jsonable(report)
    latest = out_dir / "event_importance_001_latest.json"
    stamped = out_dir / f"event_importance_001_{stamp}.json"
    payload = json.dumps(report, indent=2)
    latest.write_text(payload, encoding="utf-8")
    stamped.write_text(payload, encoding="utf-8")

    lines = [
        "# Confluence event importance 001",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Oracle arms never promote.",
        f"Stamp `{stamp}`. Preregister sha256 `{prereg_sha[:16]}…`.",
        "",
        "Oracle = true future event bit. Do not quote these profit factors as live edge.",
        "",
        "## Survivors (AND with current pivot control)",
        "",
    ]
    if not report["survivors"]:
        lines.append("**None.** Valid research outcome. Do not add more indicators.")
    else:
        lines.append("| Symbol | Event | H | Family | n | PF | intent-exp | ebr | q |")
        lines.append("|---|---|---:|---|---:|---:|---:|---:|---:|")
        for row in report["survivors"]:
            a = row["and_control"]
            p = row["promotion"]
            lines.append(
                f"| {row['symbol']} | `{row['event']}` | {row['horizon']} | {row['family']} | "
                f"{a.get('n_trades')} | {a.get('profit_factor')} | {a.get('expectancy_intent_all')} | "
                f"{a.get('entry_bar_exit_rate')} | {p.get('q_value')} |"
            )
    md = "\n".join(lines) + "\n"
    (out_dir / "event_importance_001_latest.md").write_text(md, encoding="utf-8")
    (out_dir / f"event_importance_001_{stamp}.md").write_text(md, encoding="utf-8")
    n_surv = len(report["survivors"])
    append_ledger(
        f"CONFLUENCE_EVENT_IMPORTANCE_001 done survivors={n_surv} path={latest}",
        tier=0,
    )
    print(f"WROTE {latest} survivors={n_surv}", flush=True)
    _ = cfg
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
