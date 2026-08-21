"""Pivot stack: ATR/q50 level heads + timing gates (LIMIT only, work 2-4).

Preregistered RESEARCH_ONLY (multi-symbol BTC/ETH/SOL, 15m TP1/SL1):
  Level heads: ret | atr-normalized | quantile-50
  Gates: pi*+distance band, VSA absorption, medium ATR, MTF 1h side, session/funding,
         time-bucket cancel
  No re-entry. Leakage audit before score.

Not a promotion. Intent-all expectancy always reported.
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
from llm2.pivot.strategy.level_economy import level_error_stats  # noqa: E402
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    ScoredOOS,
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.pivot.strategy.timing_gates import (  # noqa: E402
    funding_near_mask,
    map_htf_side_agree,
    medium_atr_mask,
    session_utc_mask,
    time_bucket_work_bars,
    vsa_absorption_ok,
)
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TF = "15m"
HTF = "1h"
H = 4
TP = 0.01
SL = 0.01
PACK = "level_vsa"
MAX_ROWS = 120_000
GENERATION = "pivot_timing_level_stack_001"


@dataclass(frozen=True)
class Arm:
    id: str
    level_mode: str  # ret|atr|q50
    gate: str  # p75|pi_star_level
    vsa: bool = False
    vol: bool = False
    mtf: bool = False
    session: bool = False
    time_bucket: bool = False
    work: int = 4
    note: str = ""


ARMS: tuple[Arm, ...] = (
    Arm("ret_p75_w4", "ret", "p75", work=4, note="baseline ret level"),
    Arm("atr_p75_w4", "atr", "p75", work=4, note="ATR-normalized level"),
    Arm("q50_p75_w4", "q50", "p75", work=4, note="quantile-50 level"),
    Arm("ret_pi_band_w4", "ret", "pi_star_level", work=4, note="pi* + distance band"),
    Arm("ret_pi_band_vsa_w4", "ret", "pi_star_level", vsa=True, work=4, note="+VSA absorb"),
    Arm("ret_pi_band_vsa_vol_w4", "ret", "pi_star_level", vsa=True, vol=True, work=4),
    Arm(
        "ret_full_w4",
        "ret",
        "pi_star_level",
        vsa=True,
        vol=True,
        mtf=True,
        session=True,
        time_bucket=True,
        work=4,
        note="full timing stack w4",
    ),
    Arm(
        "ret_full_w2",
        "ret",
        "pi_star_level",
        vsa=True,
        vol=True,
        mtf=True,
        session=True,
        time_bucket=True,
        work=2,
        note="full timing stack w2",
    ),
    Arm(
        "atr_full_w4",
        "atr",
        "pi_star_level",
        vsa=True,
        vol=True,
        mtf=True,
        session=True,
        time_bucket=True,
        work=4,
        note="ATR level + full gates",
    ),
)


def _leakage(symbol: str, pack: str, tf: str = TF) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = load_ohlcv(symbol, tf)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-8000:].copy()

        def _b(df, **_k):
            return build_feature_frame(df, pack=pack)

        rep = run_leakage_audit(
            ohlcv=ohlcv,
            build_features=_b,
            interval=tf,
            symbol=symbol,
            timeframe=tf,
        )
        require_clean_audit(rep)
        return {"symbol": symbol, "pack": pack, "tf": tf, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {
            "symbol": symbol,
            "pack": pack,
            "tf": tf,
            "status": "FAIL",
            "error": str(exc)[:400],
        }


def _metrics(bundle) -> dict:
    m = bundle.metrics
    out = {
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "net_pnl": float(m.net_pnl),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
    }
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    if trades:
        holds = [float(getattr(t, "hold_bars", 1)) for t in trades]
        out["entry_bar_exit_rate"] = float(np.mean(np.asarray(holds) <= 0))
    return out


def _bt(symbol: str, ohlcv: pd.DataFrame, signals, *, tag: str, max_hold: int):
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
    pad = 80
    window = ohlcv.iloc[max(0, i0 - pad) : min(len(ohlcv), i1 + pad)]
    w_ts = index_to_ms(window.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    dec_ms = int(TF_MS[TF])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    lev = float(leverage_from_stop(SL))
    try:
        bundle = run_strategy_backtest(
            window,
            signals,
            symbol=symbol,
            timeframe=TF,
            strategy_id=tag,
            touch_ohlcv=touch_win if len(touch_win) else None,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=TF),
            instrument=research_instrument(symbol),
            funding_ts_ms=f_ts[fmask],
            funding_rate=f_rt[fmask],
            plot=False,
            print_headline=False,
            store_path=None,
        )
    except Exception as exc:  # noqa: BLE001
        return {"status": "BT_ERROR", "error": str(exc)[:400], "n_signals": len(signals)}
    return {"status": "RAN", "metrics": _metrics(bundle), "n_signals": len(signals)}


def _compose_mask(scored: ScoredOOS, arm: Arm, *, pi_star: float, htf: ScoredOOS | None):
    mask = gate_mask(
        scored,
        mode=arm.gate,
        tp=TP,
        sl=SL,
        pi_star=pi_star,
        min_abs_level=0.0015,
        max_abs_level=0.02,
    )
    is_short = scored.p_high >= 0.5

    if arm.vsa:
        vsa = vsa_absorption_ok(scored.ohlcv, scored.ts_ms, is_short)
        mask = mask & vsa
    if arm.vol:
        mask = mask & medium_atr_mask(scored.atr_frac)
    if arm.session:
        mask = mask & session_utc_mask(scored.ts_ms) & funding_near_mask(scored.ts_ms)
    if arm.mtf and htf is not None:
        # build side on current mask-independent; apply agree then AND
        agree = map_htf_side_agree(
            scored.ts_ms,
            is_short,
            htf_ts_ms=htf.ts_ms,
            htf_p_high=htf.p_high,
        )
        mask = mask & agree
    return mask


def _run_arm(symbol: str, scored: ScoredOOS, arm: Arm, htf: ScoredOOS | None) -> dict:
    br = net_bracket_magnitudes(TP, SL)
    mask = _compose_mask(scored, arm, pi_star=br.pi_star, htf=htf)
    n_gate = int(mask.sum())
    if n_gate < 15:
        return {
            "arm": arm.id,
            "status": "TOO_FEW_GATED",
            "n_gated": n_gate,
            "note": arm.note,
        }
    ts, is_short, lim = limit_price_side(scored, mask)
    idx = np.flatnonzero(mask)
    if arm.time_bucket:
        wb = time_bucket_work_bars(
            scored.time_bars[idx], horizon=H, default_work=arm.work
        )
    else:
        wb = np.full(len(idx), int(arm.work), dtype=np.int64)

    intents = []
    for j in range(len(ts)):
        intents.append(
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if is_short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=SL,
                target_offset=TP,
                max_hold_bars=H + 2,
                work_bars=int(wb[j]),
                meta={"arm": arm.id},
            )
        )
    sigs, fill = materialize_working_limits(
        scored.ohlcv, intents, work_bars=int(arm.work)
    )
    print(
        f"  BT {symbol} {arm.id} gated={n_gate} path_fill={fill.get('n_filled_path')} …",
        flush=True,
    )
    res = _bt(symbol, scored.ohlcv, sigs, tag=f"{symbol.lower()}_{arm.id}", max_hold=H + 2)
    out = {
        "arm": arm.id,
        "level_mode": arm.level_mode,
        "note": arm.note,
        "n_gated": n_gate,
        "fill_stats": fill,
        "pi_star": br.pi_star,
        **res,
    }
    if res.get("status") == "RAN" and n_gate > 0:
        out["expectancy_intent_all"] = float(res["metrics"]["net_pnl"]) / n_gate
        out["expectancy_fill_only"] = float(res["metrics"]["expectancy"])
        days = max(
            1.0,
            (
                pd.Timestamp(scored.ohlcv.index[-1]) - pd.Timestamp(scored.ohlcv.index[0])
            ).total_seconds()
            / 86400.0,
        )
        out["trades_per_month"] = float(res["metrics"]["n_trades"]) / (days / 30.0)
        print(
            f"    PF={res['metrics']['profit_factor']:.3f} n={res['metrics']['n_trades']} "
            f"WR={res['metrics']['win_rate']:.3f} "
            f"ebr={res['metrics'].get('entry_bar_exit_rate')} "
            f"intent_exp={out['expectancy_intent_all']:.5f}",
            flush=True,
        )
    else:
        print(f"    {res.get('status')}", flush=True)
    return out


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(f"PIVOT_TIMING_LEVEL_STACK start {stamp}", tier=0)
    print(f"{GENERATION} stamp={stamp}", flush=True)

    leak = []
    for sym in SYMBOLS:
        leak.append(_leakage(sym, PACK, TF))
        leak.append(_leakage(sym, PACK, HTF))
    for x in leak:
        print(f"  leakage {x['symbol']} {x['tf']} {x['pack']}: {x['status']}", flush=True)
        if x["status"] != "PASS":
            print(f"    {x.get('error','')[:200]}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        print("LEAKAGE FAIL — abort", flush=True)
        path = ARTIFACTS / "reports" / "pivot_forecast" / f"timing_level_stack_{stamp}.json"
        path.write_text(
            json.dumps(
                {"stamp": stamp, "leakage": leak, "readiness_max": "RESEARCH_ONLY"},
                indent=2,
            ),
            encoding="utf-8",
        )
        return 2

    # Score caches: (symbol, level_mode) and HTF side
    scored_ltf: dict[tuple[str, str], ScoredOOS] = {}
    scored_htf: dict[str, ScoredOOS] = {}
    mae_table: dict[str, dict] = {}

    for sym in SYMBOLS:
        print(f"SCORE HTF {sym} …", flush=True)
        scored_htf[sym] = score_symbol_oos(
            sym,
            timeframe=HTF,
            horizon_bars=2,
            atr_min=2.0,
            feature_pack=PACK,
            max_rows=MAX_ROWS,
            level_mode="ret",
        )
        for mode in ("ret", "atr", "q50"):
            key = (sym, mode)
            print(f"SCORE LTF {sym} level_mode={mode} …", flush=True)
            sc = score_symbol_oos(
                sym,
                timeframe=TF,
                horizon_bars=H,
                atr_min=2.0,
                feature_pack=PACK,
                max_rows=MAX_ROWS,
                level_mode=mode,
            )
            scored_ltf[key] = sc
            m = np.isfinite(sc.y_level) & np.isfinite(sc.level_ret)
            mae_table[f"{sym}_{mode}"] = level_error_stats(
                y_level_ret=sc.y_level[m],
                pred_level_ret=sc.level_ret[m],
                atr_frac=sc.atr_frac[m],
            )
            print(
                f"  MAE={mae_table[f'{sym}_{mode}']['mae_pct']:.4f} "
                f"P90={mae_table[f'{sym}_{mode}']['p90_abs_pct']:.4f}",
                flush=True,
            )

    results = {}
    for sym in SYMBOLS:
        results[sym] = []
        for arm in ARMS:
            sc = scored_ltf[(sym, arm.level_mode)]
            results[sym].append(_run_arm(sym, sc, arm, scored_htf[sym]))

    report = {
        "generation_id": GENERATION,
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "setup": {
            "tf": TF,
            "htf": HTF,
            "tp": TP,
            "sl": SL,
            "pack": PACK,
            "no_reentry": True,
            "pi_star": net_bracket_magnitudes(TP, SL)._asdict(),
        },
        "leakage": leak,
        "level_mae": mae_table,
        "symbols": results,
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"timing_level_stack_{stamp}.json"
    latest = out_dir / "timing_level_stack_latest.json"
    md_path = out_dir / f"timing_level_stack_{stamp}.md"
    text = json.dumps(report, indent=2, default=str)
    path.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    md_path.write_text(_md(report), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    try:
        print(_md(report), flush=True)
    except UnicodeEncodeError:
        print("(markdown on disk)", flush=True)
    return 0


def _md(r: dict) -> str:
    lines = [
        f"# Pivot timing + level stack (`{r['stamp']}`)",
        "",
        f"**{r['readiness_max']}** | pack=`{r['setup']['pack']}` | no re-entry",
        "",
        "## Leakage",
    ]
    for x in r["leakage"]:
        lines.append(f"- {x['symbol']} {x['tf']}: **{x['status']}**")
    lines.append("")
    lines.append("## Level MAE (ret space)")
    lines.append("| key | MAE | P90 | corr |")
    lines.append("|---|---:|---:|---:|")
    for k, v in r["level_mae"].items():
        lines.append(
            f"| {k} | {v.get('mae_pct')} | {v.get('p90_abs_pct')} | {v.get('corr')} |"
        )
    lines.append("")
    for sym, arms in r["symbols"].items():
        lines.append(f"## {sym}")
        lines.append(
            "| arm | n_gated | fill% | n_tr | /mo | WR | PF | exp_fill | exp_intent | "
            "entry_bar% | pnl |"
        )
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for a in arms:
            if a.get("status") != "RAN":
                lines.append(
                    f"| {a.get('arm')} | {a.get('n_gated')} | — | — | — | — | "
                    f"{a.get('status')} | — | — | — | — |"
                )
                continue
            m = a["metrics"]
            fs = a.get("fill_stats") or {}
            lines.append(
                f"| {a['arm']} | {a['n_gated']} | "
                f"{100*float(fs.get('fill_rate', float('nan'))):.1f}% | "
                f"{m['n_trades']} | {a.get('trades_per_month', float('nan')):.1f} | "
                f"{m['win_rate']:.3f} | {m['profit_factor']:.3f} | "
                f"{a.get('expectancy_fill_only', float('nan')):.4f} | "
                f"{a.get('expectancy_intent_all', float('nan')):.5f} | "
                f"{100*float(m.get('entry_bar_exit_rate', float('nan'))):.1f}% | "
                f"{m['net_pnl']:.2f} |"
            )
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
