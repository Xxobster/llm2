"""Fleet-wide structure_v1 streak + miscalibration autopsy.

Evidence: MEASURE_DIAGNOSTIC. Outer folds only; lockbox unused.
Discovers every pack under artifacts/live_packs with strategy.json + model.joblib.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim,
    research_sim_hedge,
)

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.evidence.streak_autopsy import (  # noqa: E402
    DEFAULT_STREAK_N,
    annotate_trades_with_preds,
    build_analyst_prompt,
    chronological_streaks,
    cross_pack_similarity,
    miscalibration_summary,
    offline_llm_proposals,
    pack_dossier,
    rank_packs_by_pain,
    realized_vol_tercile,
    recent_hit_rate_causal,
    signed_forward_returns,
    strength_tercile_labels,
)
from llm2.experiments.eth_multitrade_nested import (  # noqa: E402
    build_multitrade_signals,
    pf,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.labels.fwd_return import build_fwd_return_labels  # noqa: E402
from llm2.llm.controller import LLMController  # noqa: E402
from llm2.live.multitrade import parse_multitrade_config  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    ROUND_TRIP_COST,
    TF_MS,
    touch_timeframe,
)
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.signals.cluster_concurrency import build_cluster_size_signals  # noqa: E402
from llm2.signals.singlebook_clarity import (  # noqa: E402
    SingleBookArm,
    build_singlebook_signals,
)
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    build_outer_folds,
    index_to_ms,
)

TIMEFRAME = "1h"
SPACE = "structure_v1"
LABEL_HORIZON = 6
SL = 0.02
GEN = "structure_v1_fleet_streak_autopsy_001"
LIVE_PACKS = ARTIFACTS / "live_packs"


def _min_edge(target: str) -> float:
    return (
        float(DIRECTION_BAND)
        if target_family(target) == "directional"
        else float(ROUND_TRIP_COST)
    )


def _labels(ohlcv: pd.DataFrame, target: str) -> pd.Series:
    if target == "direction":
        return build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    if target == "fwd_return":
        return build_fwd_return_labels(ohlcv, horizon=LABEL_HORIZON)["fwd_return"]
    raise ValueError(target)


def _load_strategy(pack_dir: Path) -> dict[str, Any]:
    return json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))


def discover_packs(*, only: list[str] | None = None) -> list[Path]:
    packs: list[Path] = []
    if not LIVE_PACKS.is_dir():
        return packs
    for d in sorted(LIVE_PACKS.iterdir()):
        if not d.is_dir():
            continue
        if not (d / "strategy.json").is_file():
            continue
        if not (d / "model.joblib").is_file():
            continue
        if only:
            name = d.name
            strat = _load_strategy(d)
            vid = str(strat.get("version_id") or name)
            if name not in only and vid not in only:
                continue
        packs.append(d)
    return packs


def geometry_from_strategy(strategy: dict[str, Any]) -> dict[str, Any]:
    """Classify pack execution geometry for signal builders."""
    symbol = str(strategy.get("symbol") or "").upper()
    target = str(strategy.get("target") or "direction").lower()
    hold = int(strategy.get("horizon_bars") or 6)
    tp = float(strategy.get("tp_pct") or 0.01)
    sl = float(strategy.get("sl_pct") or SL)
    min_edge = float(strategy.get("min_edge") or _min_edge(target))
    mt = parse_multitrade_config(strategy)
    version_id = str(
        strategy.get("version_id")
        or (mt or {}).get("version_id")
        or strategy.get("strategy_id")
        or "unknown"
    )

    if mt is not None:
        size_double = int(
            (strategy.get("multitrade") or {}).get("size_double_within_bars") or 0
        )
        uniform = bool((strategy.get("multitrade") or {}).get("uniform_books", False))
        mode = "k5_size_double" if size_double > 0 and uniform else "multitrade_fib"
        return {
            "version_id": version_id,
            "symbol": symbol,
            "target": target,
            "mode": mode,
            "min_edge": min_edge,
            "hold": int(mt.get("base_hold") or hold),
            "hold_addon": int(mt.get("hold_addon") or hold),
            "tp": float(mt.get("base_tp") or tp),
            "sl": float(mt.get("base_sl") or sl),
            "k": int(mt.get("max_positions_per_side") or 1),
            "clarity": str(mt.get("clarity") or "none"),
            "clarity_scope": str(mt.get("clarity_scope") or "addon"),
            "fib_ext": float(mt.get("fib_ext") or 0.0),
            "strength_quantile": float(mt.get("strength_quantile") or 0.5),
            "size_double_within_bars": size_double,
            "uniform_books": uniform,
            "mean_lookback": int(mt.get("mean_lookback") or 168),
        }

    arm_clarity = "none"
    note = str(strategy.get("what_it_does") or "") + str(
        strategy.get("version_lineage") or ""
    )
    if "mean_strength" in note.lower() or "clarity" in strategy.get(
        "strategy_id", ""
    ).lower() or "clarity" in version_id:
        arm_clarity = "mean_strength"
    # clarity_hold packs
    if "clarity_hold12" in version_id or "clarity" in Path(
        str(strategy.get("strategy_id") or "")
    ).name:
        arm_clarity = "mean_strength"
        hold = max(hold, 12)
    return {
        "version_id": version_id,
        "symbol": symbol,
        "target": target,
        "mode": "single",
        "min_edge": min_edge,
        "hold": hold,
        "tp": tp,
        "sl": sl,
        "k": 1,
        "clarity": arm_clarity,
        "clarity_scope": "all",
        "strength_quantile": 0.5,
        "size_double_within_bars": 0,
        "uniform_books": False,
        "fib_ext": 0.0,
        "hold_addon": hold,
        "mean_lookback": 168,
    }


def _build_signals(
    geom: dict[str, Any],
    oos_ts: np.ndarray,
    side: np.ndarray,
    mean: np.ndarray,
    close_oos: np.ndarray,
    instrument: Any,
) -> tuple[list[Any], dict[str, Any], Any]:
    arm = SingleBookArm(
        clarity=str(geom["clarity"]),  # type: ignore[arg-type]
        horizon_bars=int(geom["hold"]),
        tp_pct=float(geom["tp"]),
        sl_pct=float(geom["sl"]),
    )
    mode = geom["mode"]
    if mode == "k5_size_double":
        sigs, stats = build_cluster_size_signals(
            oos_ts,
            side,
            mean,
            close_oos,
            arm=arm,
            min_edge=float(geom["min_edge"]),
            max_per_side=int(geom["k"]),
            instrument=instrument,
            size_double_within_bars=int(geom["size_double_within_bars"] or 3),
            strength_quantile=float(geom["strength_quantile"]),
        )
        sim = research_sim_hedge(
            max_hold_bars=int(geom["hold"]),
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=int(geom["k"]),
            max_positions_per_symbol=int(geom["k"]) * 2,
        )
        return sigs, stats, sim
    if mode == "multitrade_fib":
        cfg = {
            "max_positions_per_side": int(geom["k"]),
            "clarity": geom["clarity"],
            "clarity_scope": geom["clarity_scope"],
            "fib_ext": float(geom["fib_ext"]),
            "hold_addon": int(geom["hold_addon"]),
            "base_tp": float(geom["tp"]),
            "base_sl": float(geom["sl"]),
            "base_hold": int(geom["hold"]),
            "mean_lookback": int(geom["mean_lookback"]),
            "uniform_books": bool(geom.get("uniform_books")),
            "strength_quantile": float(geom.get("strength_quantile") or 0.5),
        }
        sigs, stats = build_multitrade_signals(
            oos_ts, side, mean, cfg=cfg, close=close_oos
        )
        hold = max(int(geom["hold"]), int(geom["hold_addon"]))
        sim = research_sim_hedge(
            max_hold_bars=hold,
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=int(geom["k"]),
            max_positions_per_symbol=int(geom["k"]) * 2,
        )
        return sigs, stats, sim
    # single
    sigs, stats = build_singlebook_signals(
        oos_ts,
        side,
        mean,
        arm=arm,
        min_edge=float(geom["min_edge"]),
        strength_quantile=float(geom["strength_quantile"]),
    )
    sim = research_sim(
        max_hold_bars=int(geom["hold"]), decision_timeframe=TIMEFRAME
    )
    return sigs, stats, sim


def analyse_pack(pack_dir: Path, *, min_streak: int) -> dict[str, Any]:
    strategy = _load_strategy(pack_dir)
    geom = geometry_from_strategy(strategy)
    symbol = geom["symbol"]
    target = geom["target"]
    version_id = geom["version_id"]
    print(f"AUDIT {pack_dir.name} vid={version_id} mode={geom['mode']} …", flush=True)

    if not symbol:
        return {"version_id": version_id, "error": "missing_symbol", "pack": pack_dir.name}

    try:
        ohlcv = load_ohlcv(symbol, TIMEFRAME)
    except Exception as exc:  # noqa: BLE001
        return {
            "version_id": version_id,
            "error": f"load_ohlcv: {exc}",
            "pack": pack_dir.name,
        }

    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    if len(ohlcv) < 500:
        return {
            "version_id": version_id,
            "error": "insufficient_bars",
            "pack": pack_dir.name,
            "n_bars": int(len(ohlcv)),
        }

    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TIMEFRAME)
    y = _labels(ohlcv, target)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(
        ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON
    )
    touch = load_ohlcv(symbol, touch_timeframe(TIMEFRAME, symbol))
    touch_tf = touch_timeframe(TIMEFRAME, symbol)
    funding = load_funding(symbol)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(float(geom["sl"])))
    instrument = research_instrument(symbol)
    family = target_family(target)
    full_close = ohlcv["close"].to_numpy(dtype=float)
    full_ts = index_to_ms(ohlcv.index)
    # funding sign nearest settlement at entry (optional)
    fund_map = {int(t): float(r) for t, r in zip(funding_ts, funding_rt)}

    rows: list[dict[str, Any]] = []
    pred_ts_all: list[int] = []
    pred_mean_all: list[float] = []
    pred_side_all: list[int] = []

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        close_oos = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)[oos]
        for i in range(len(oos_ts)):
            pred_ts_all.append(int(oos_ts[i]))
            pred_mean_all.append(float(mean[i]))
            pred_side_all.append(int(side[i]))

        sigs, stats, sim = _build_signals(
            geom, oos_ts, side, mean, close_oos, instrument
        )
        hold = max(int(geom["hold"]), int(geom.get("hold_addon") or geom["hold"]))
        mean_by_ts = {int(oos_ts[i]): float(mean[i]) for i in range(len(oos_ts))}

        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, hold * 4)
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
            symbol=symbol,
            timeframe=TIMEFRAME,
            strategy_id=f"{version_id}-f{fold.fold_index}",
            touch_ohlcv=touch_win,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=sim,
            instrument=instrument,
            funding_ts_ms=funding_ts[fmask],
            funding_rate=funding_rt[fmask],
            strategy_meta={"name": version_id, "generation_id": GEN},
            plot=False,
            print_headline=False,
            store_path=None,
        )
        for t in bundle.result.trades:
            ets = int(t.entry_ts_ms)
            xis = int(t.exit_ts_ms)
            s = int(getattr(t.side, "value", t.side))
            tag = str(getattr(t, "tag", "") or "")
            book = 1
            if "_b" in tag:
                try:
                    book = int(tag.rsplit("_b", 1)[-1].split("_")[0])
                except ValueError:
                    book = 1
            pnl = float(getattr(t, "realized_pnl", 0) or 0)
            m = float(mean_by_ts.get(ets, float("nan")))
            fwds = signed_forward_returns(
                full_close, full_ts, entry_ts_ms=ets, side=s
            )
            fund = fund_map.get(ets, 0.0)
            rows.append(
                {
                    "version_id": version_id,
                    "symbol": symbol,
                    "fold": int(fold.fold_index),
                    "trade_id": int(getattr(t, "trade_id", 0) or 0),
                    "entry_ts_ms": ets,
                    "exit_ts_ms": xis,
                    "side": s,
                    "book_idx": book,
                    "pred_mean": m,
                    "abs_mean": abs(m) if np.isfinite(m) else float("nan"),
                    "pnl": pnl,
                    "win": bool(pnl > 0),
                    "exit_reason": str(getattr(t, "exit_reason", "") or "unknown"),
                    "signed_fwd_1": fwds["signed_fwd_1"],
                    "signed_fwd_3": fwds["signed_fwd_3"],
                    "signed_fwd_6": fwds["signed_fwd_6"],
                    "signed_fwd_12": fwds["signed_fwd_12"],
                    "funding_sign": int(np.sign(fund)) if np.isfinite(fund) else 0,
                    "tag": tag,
                }
            )
        print(
            f"  fold {fold.fold_index}: trades={len(bundle.result.trades)} "
            f"signals={stats.get('n_emitted', 0)}",
            flush=True,
        )

    if not rows:
        return {
            "version_id": version_id,
            "symbol": symbol,
            "geometry": geom,
            "error": "no_trades",
            "pack": pack_dir.name,
        }

    df = pd.DataFrame(rows)
    df = annotate_trades_with_preds(
        df,
        pred_ts_ms=np.asarray(pred_ts_all, dtype=np.int64),
        pred_mean=np.asarray(pred_mean_all, dtype=float),
        pred_side=np.asarray(pred_side_all, dtype=int),
    )
    df["strength_tercile"] = strength_tercile_labels(df["abs_mean"].to_numpy(dtype=float))
    df["vol_tercile"] = realized_vol_tercile(
        full_close, full_ts, df["entry_ts_ms"].to_numpy(dtype=np.int64)
    )
    df["recent_hit_rate"] = recent_hit_rate_causal(df, lookback_trades=10)

    streaks = chronological_streaks(df, min_streak=min_streak)
    streaks_side = chronological_streaks(
        df, min_streak=min_streak, group_cols=["side"]
    )
    streaks_book = chronological_streaks(
        df, min_streak=min_streak, group_cols=["book_idx"]
    )
    miscal = miscalibration_summary(df, min_edge=float(geom["min_edge"]))
    dossier = pack_dossier(
        version_id=version_id,
        symbol=symbol,
        geometry=geom,
        trades_df=df,
        streaks=streaks,
        miscal=miscal,
        min_streak=min_streak,
    )
    dossier["streaks_by_side"] = streaks_side.get("by_group")
    dossier["streaks_by_book"] = streaks_book.get("by_group")
    dossier["overall_pf"] = pf(df["pnl"].to_numpy(dtype=float))
    dossier["overall_wr"] = float(df["win"].mean())
    dossier["pack_dir"] = pack_dir.name
    return {"dossier": dossier, "trades": df}


def propose_with_llm(fleet: dict[str, Any], *, use_ollama: bool) -> dict[str, Any]:
    offline = offline_llm_proposals(fleet)
    prompt = build_analyst_prompt(fleet)
    ctrl = LLMController()
    try:
        resp = ctrl.complete(prompt, use_ollama=use_ollama)
        text = resp.text
        source = "ollama" if use_ollama and not str(text).startswith("[ollama unavailable") else (
            "ollama_fallback_stub" if use_ollama else "controller_stub"
        )
        if str(text).startswith("[ollama unavailable") or str(text).startswith("[stub]"):
            # blend offline proposals with controller note
            offline = dict(offline)
            offline["controller_note"] = text[:2000]
            offline["source"] = "offline_template_after_" + source
            offline["promotion_blocked"] = True
            offline["interaction_id"] = resp.interaction_id
            return offline
        return {
            "promotion_blocked": True,
            "source": source,
            "interaction_id": resp.interaction_id,
            "raw_text": text,
            "fallback_template": offline,
            "note": "Prefer parsing raw_text; template is safety fallback.",
        }
    except Exception as exc:  # noqa: BLE001
        offline = dict(offline)
        offline["controller_error"] = f"{type(exc).__name__}: {exc}"
        offline["source"] = "offline_template_error"
        return offline


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", nargs="*", default=None, help="Pack dir names or version_ids")
    ap.add_argument("--min-streak", type=int, default=DEFAULT_STREAK_N)
    ap.add_argument("--use-ollama", action="store_true", help="Try local Ollama for proposals")
    ap.add_argument(
        "--max-packs",
        type=int,
        default=0,
        help="Limit packs (0=all) for smoke tests",
    )
    args = ap.parse_args()
    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")

    packs = discover_packs(only=args.only)
    if args.max_packs and args.max_packs > 0:
        packs = packs[: int(args.max_packs)]
    if not packs:
        raise SystemExit("no packs found")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    trades_root = out_dir / f"{GEN}_trades"
    trades_root.mkdir(parents=True, exist_ok=True)

    dossiers: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    for pack in packs:
        try:
            res = analyse_pack(pack, min_streak=int(args.min_streak))
            if "error" in res and "dossier" not in res:
                errors.append(res)
                print(f"  ERROR {res}", flush=True)
                continue
            d = res["dossier"]
            df: pd.DataFrame = res["trades"]
            dossiers.append(d)
            csv_path = trades_root / f"{d['version_id']}_trades.csv"
            df.to_csv(csv_path, index=False)
            print(
                f"  DONE {d['version_id']}: n={d['n_trades']} "
                f"max_loss_streak={d['streaks']['max_loss_streak']} "
                f"pain={d['pain_score']:.2f} -> {csv_path.name}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001
            errors.append(
                {
                    "pack": pack.name,
                    "error": f"{type(exc).__name__}: {exc}",
                    "traceback": traceback.format_exc()[-1500:],
                }
            )
            print(f"  FATAL {pack.name}: {exc}", flush=True)

    pain_rank = rank_packs_by_pain(dossiers)
    shared = cross_pack_similarity(dossiers)
    fleet = {
        "generation_id": GEN,
        "created_utc": stamp,
        "evidence_class": "MEASURE_DIAGNOSTIC",
        "max_readiness": "RESEARCH_ONLY",
        "hard_end_exclusive": FORWARD_LOCKBOX_START,
        "lockbox_used": False,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES,
        "conformance_passed": bool(conf.get("passed")),
        "min_streak": int(args.min_streak),
        "n_packs_attempted": len(packs),
        "n_packs_ok": len(dossiers),
        "errors": errors,
        "pain_rank": pain_rank,
        "cross_pack_loss_streak_buckets": shared,
        "dossiers": dossiers,
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "trades_dir": str(trades_root.relative_to(_ROOT)).replace("\\", "/"),
        "note": (
            "Chronological win/loss streaks by exit_ts_ms. "
            "Not a promotion gate. MIN_EXCHANGE dust caveat on dollar PnL."
        ),
    }
    fleet = stamp_min_size_equity_caveat(fleet)

    # dossiers for each pack (json + short md)
    dossier_dir = out_dir / f"{GEN}_dossiers"
    dossier_dir.mkdir(parents=True, exist_ok=True)
    for d in dossiers:
        vid = d["version_id"]
        (dossier_dir / f"{vid}.json").write_text(
            json.dumps(d, indent=2, default=str), encoding="utf-8"
        )
        md = [
            f"# Streak autopsy — {vid}",
            "",
            f"- symbol: {d.get('symbol')}",
            f"- n_trades: {d.get('n_trades')}",
            f"- pain_score: {d.get('pain_score')}",
            f"- max_loss_streak: {(d.get('streaks') or {}).get('max_loss_streak')}",
            f"- max_win_streak: {(d.get('streaks') or {}).get('max_win_streak')}",
            f"- high_strength_loss_frac: {(d.get('miscalibration') or {}).get('frac_high_strength_and_loss')}",
            "",
            "## Elevated loss-streak start buckets",
            "",
        ]
        for b in (d.get("elevated_loss_streak_buckets") or [])[:8]:
            md.append(
                f"- `{b.get('bucket')}` starts={b.get('n_streak_starts')} "
                f"lift={b.get('lift_vs_share')}"
            )
        (dossier_dir / f"{vid}.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    proposals = propose_with_llm(fleet, use_ollama=bool(args.use_ollama))
    proposals_path = out_dir / f"{GEN}_llm_proposals.json"
    proposals_path.write_text(
        json.dumps(proposals, indent=2, default=str), encoding="utf-8"
    )
    fleet["llm_proposals_path"] = str(proposals_path.relative_to(_ROOT)).replace(
        "\\", "/"
    )
    fleet["recommended_control"] = pain_rank[0] if pain_rank else None
    fleet["recommended_arm"] = (proposals.get("proposals") or [None])[0]

    latest = out_dir / f"{GEN}_latest.json"
    # slim dossiers in latest for size (full in dossier_dir)
    slim = dict(fleet)
    slim["dossiers"] = [
        {
            k: d.get(k)
            for k in (
                "version_id",
                "symbol",
                "geometry",
                "pain_score",
                "streaks",
                "miscalibration",
                "n_trades",
                "overall_pf",
                "overall_wr",
                "elevated_loss_streak_buckets",
                "pack_dir",
            )
        }
        for d in dossiers
    ]
    latest.write_text(json.dumps(slim, indent=2, default=str), encoding="utf-8")
    (out_dir / f"{GEN}_{stamp}.json").write_text(
        latest.read_text(encoding="utf-8"), encoding="utf-8"
    )

    print(json.dumps({"pain_rank": pain_rank[:5], "recommended_arm": fleet["recommended_arm"]}, indent=2, default=str))
    print(f"wrote {latest}")
    print(f"proposals {proposals_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
