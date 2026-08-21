"""Follow-up: timing gates on P75 baseline (ret level) — multi-symbol LIMIT.

Prior full stack emptied the book because pi*+band + MAE/ATR hard-fail left <50
intents. This run applies VSA / vol / MTF / session / time-bucket on cal-P75.
Leakage already green for level_vsa; still re-checks SOL 15m. RESEARCH_ONLY.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

from tradesim import Side, research_instrument, research_margin, research_sizing  # noqa: E402
from tradesim import research_sim_limit_entry  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.features.packs import build_feature_frame  # noqa: E402
from llm2.pivot.strategy.ev import net_bracket_magnitudes  # noqa: E402
from llm2.pivot.strategy.score_oos import gate_mask, limit_price_side, score_symbol_oos  # noqa: E402
from llm2.pivot.strategy.timing_gates import (  # noqa: E402
    funding_near_mask,
    map_htf_side_agree,
    medium_atr_mask,
    session_utc_mask,
    time_bucket_work_bars,
    vsa_absorption_ok,
)
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TF, HTF, H, TP, SL = "15m", "1h", 4, 0.01, 0.01
PACK = "level_vsa"
MAX_ROWS = 120_000


@dataclass(frozen=True)
class Arm:
    id: str
    gate: str = "p75"
    vsa: bool = False
    vol: bool = False
    mtf: bool = False
    session: bool = False
    time_bucket: bool = False
    work: int = 4


ARMS = (
    Arm("p75_w4"),
    Arm("p75_vsa_w4", vsa=True),
    Arm("p75_vol_w4", vol=True),
    Arm("p75_mtf_w4", mtf=True),
    Arm("p75_session_w4", session=True),
    Arm("p75_vsa_vol_mtf_w4", vsa=True, vol=True, mtf=True),
    Arm("p75_full_w4", vsa=True, vol=True, mtf=True, session=True, time_bucket=True, work=4),
    Arm("p75_full_w2", vsa=True, vol=True, mtf=True, session=True, time_bucket=True, work=2),
    Arm("pi_band_w4", gate="pi_star_level", work=4),
    Arm("pi_band_vsa_w4", gate="pi_star_level", vsa=True, work=4),
)


def _leak(symbol: str, tf: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = load_ohlcv(symbol, tf)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-6000:].copy()

        def _b(df, **_k):
            return build_feature_frame(df, pack=PACK)

        rep = run_leakage_audit(
            ohlcv=ohlcv, build_features=_b, interval=tf, symbol=symbol, timeframe=tf
        )
        require_clean_audit(rep)
        return {"symbol": symbol, "tf": tf, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "tf": tf, "status": "FAIL", "error": str(exc)[:300]}


def _metrics(bundle) -> dict:
    m = bundle.metrics
    out = {
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "net_pnl": float(m.net_pnl),
        "win_rate": float(m.win_rate),
        "expectancy": float(m.expectancy),
    }
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    if trades:
        holds = [float(getattr(t, "hold_bars", 1)) for t in trades]
        out["entry_bar_exit_rate"] = float(np.mean(np.asarray(holds) <= 0))
    return out


def _bt(symbol, ohlcv, signals, tag):
    if len(signals) < 12:
        return {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(TF, symbol)
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
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[TF])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=TF,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(SL))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=H + 2, decision_timeframe=TF),
        instrument=research_instrument(symbol),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=False,
        print_headline=False,
        store_path=None,
    )
    return {"status": "RAN", "metrics": _metrics(bundle), "n_signals": len(signals)}


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    print(f"pivot timing gates p75 stamp={stamp}", flush=True)
    leak = [_leak(s, TF) for s in SYMBOLS] + [_leak(s, HTF) for s in SYMBOLS]
    for x in leak:
        print(f"  leakage {x['symbol']} {x['tf']}: {x['status']}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        return 2

    pi = net_bracket_magnitudes(TP, SL).pi_star
    out_sym = {}
    for sym in SYMBOLS:
        print(f"SCORE {sym} …", flush=True)
        sc = score_symbol_oos(
            sym, timeframe=TF, horizon_bars=H, feature_pack=PACK, max_rows=MAX_ROWS, level_mode="ret"
        )
        htf = score_symbol_oos(
            sym, timeframe=HTF, horizon_bars=2, feature_pack=PACK, max_rows=MAX_ROWS, level_mode="ret"
        )
        rows = []
        for arm in ARMS:
            mask = gate_mask(
                sc, mode=arm.gate, tp=TP, sl=SL, pi_star=pi, min_abs_level=0.0015, max_abs_level=0.02
            )
            is_short = sc.p_high >= 0.5
            if arm.vsa:
                mask = mask & vsa_absorption_ok(sc.ohlcv, sc.ts_ms, is_short)
            if arm.vol:
                mask = mask & medium_atr_mask(sc.atr_frac)
            if arm.session:
                mask = mask & session_utc_mask(sc.ts_ms) & funding_near_mask(sc.ts_ms)
            if arm.mtf:
                mask = mask & map_htf_side_agree(
                    sc.ts_ms, is_short, htf_ts_ms=htf.ts_ms, htf_p_high=htf.p_high
                )
            n_g = int(mask.sum())
            if n_g < 15:
                rows.append({"arm": arm.id, "status": "TOO_FEW_GATED", "n_gated": n_g})
                print(f"  {arm.id}: TOO_FEW_GATED n={n_g}", flush=True)
                continue
            ts, short, lim = limit_price_side(sc, mask)
            idx = np.flatnonzero(mask)
            wb = (
                time_bucket_work_bars(sc.time_bars[idx], horizon=H, default_work=arm.work)
                if arm.time_bucket
                else np.full(len(idx), arm.work, dtype=np.int64)
            )
            intents = [
                LimitIntent(
                    decision_ts_ms=int(ts[j]),
                    side=Side.SHORT if short[j] else Side.LONG,
                    limit_price=float(lim[j]),
                    stop_offset=SL,
                    target_offset=TP,
                    max_hold_bars=H + 2,
                    work_bars=int(wb[j]),
                )
                for j in range(len(ts))
            ]
            sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=arm.work)
            print(f"  BT {arm.id} gated={n_g} fill={fill['n_filled_path']} …", flush=True)
            res = _bt(sym, sc.ohlcv, sigs, f"{sym.lower()}_{arm.id}")
            row = {"arm": arm.id, "n_gated": n_g, "fill_stats": fill, **res}
            if res.get("status") == "RAN":
                row["expectancy_intent_all"] = res["metrics"]["net_pnl"] / n_g
                row["expectancy_fill_only"] = res["metrics"]["expectancy"]
                print(
                    f"    PF={res['metrics']['profit_factor']:.3f} n={res['metrics']['n_trades']} "
                    f"WR={res['metrics']['win_rate']:.3f} "
                    f"ebr={res['metrics'].get('entry_bar_exit_rate')}",
                    flush=True,
                )
            rows.append(row)
        out_sym[sym] = rows

    report = {
        "generation_id": "pivot_timing_gates_p75_001",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "pi_star": pi,
        "leakage": leak,
        "symbols": out_sym,
        "note": "pi_star_level no longer hard-fails on train MAE vs ATR",
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    path = out_dir / f"timing_gates_p75_{stamp}.json"
    latest = out_dir / "timing_gates_p75_latest.json"
    md = out_dir / f"timing_gates_p75_{stamp}.md"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    lines = [f"# Timing gates on P75 (`{stamp}`)", "", f"**RESEARCH_ONLY** pi*={pi:.3f}", ""]
    for sym, rows in out_sym.items():
        lines += [f"## {sym}", "| arm | n_gated | fill% | n_tr | WR | PF | exp_intent | entry_bar% | pnl |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for a in rows:
            if a.get("status") != "RAN":
                lines.append(f"| {a.get('arm')} | {a.get('n_gated')} | — | — | — | {a.get('status')} | — | — | — |")
                continue
            m = a["metrics"]
            fr = 100 * float((a.get("fill_stats") or {}).get("fill_rate", float("nan")))
            lines.append(
                f"| {a['arm']} | {a['n_gated']} | {fr:.1f}% | {m['n_trades']} | {m['win_rate']:.3f} | "
                f"{m['profit_factor']:.3f} | {a.get('expectancy_intent_all', float('nan')):.5f} | "
                f"{100*float(m.get('entry_bar_exit_rate', float('nan'))):.1f}% | {m['net_pnl']:.2f} |"
            )
        lines.append("")
    md.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    try:
        print("\n".join(lines), flush=True)
    except UnicodeEncodeError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
