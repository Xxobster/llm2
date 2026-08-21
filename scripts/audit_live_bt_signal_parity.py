"""Decompose live-vs-backtest divergence into named, countable causes.

Three layers, audited independently so a difference is attributed, not guessed:

  A  PREDICTION   live ``pred_mean`` at bar T  vs  locally recomputed pred_mean.
                  Uses the decide-time ``feature_snapshot`` in the ledger to name the
                  exact feature column that moved when predictions differ.
  B  GATE         research multitrade gate replayed on the *live* prediction series,
                  under four state models, each compared with live's own decisions:
                    C0 cold strength history + hold-based slot occupancy (old research)
                    C1 seeded strength history + hold-based occupancy
                    C2 cold strength history + exit-aware occupancy
                    C3 seeded + exit-aware  (the intended parity model)
  C  EXECUTION    size multiplier / take-profit per book / max-hold per book.

Read-only. Evidence class: PARITY_AUDIT (never promotes readiness).
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import joblib  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.live.multitrade import (  # noqa: E402
    decide_entry_gate,
    parse_multitrade_config,
    slot_release_ts_ms,
)
from llm2.paths import ARTIFACTS, ROUND_TRIP_COST, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

LEDGERS_LN1 = ARTIFACTS / "reports" / "_llm2_ln1_all_unit_ledgers.json"
LEDGER_15M = ARTIFACTS / "reports" / "_live_15m_ledger_dump.json"
OUT_DIR = ARTIFACTS / "reports" / "live_bt_signal_parity_audit"
PACKS = ARTIFACTS / "live_packs"

UNITS: list[dict[str, str]] = [
    {
        "account": "Xxobster8",
        "label": "ETH_multitrade_v1_2",
        "ledger_key": "llm2-structure-eth-multitrade-v1_2",
        "pack": "structure_v1_ethusdt_multitrade_v1_2",
    },
    {
        "account": "Xxobster7",
        "label": "BTC_single",
        "ledger_key": "llm2-structure",
        "pack": "structure_v1_lgbm",
    },
    {
        "account": "Xxobster7",
        "label": "ETH_single",
        "ledger_key": "llm2-structure-eth",
        "pack": "structure_v1_ethusdt_direction",
    },
    {
        "account": "Xxobster7",
        "label": "SOL_single",
        "ledger_key": "llm2-structure-sol",
        "pack": "structure_v1_solusdt_direction",
    },
    {
        "account": "Xxobster10",
        "label": "BTC_k5_double3h",
        "ledger_key": "llm2-structure-btc-k5-double3h-v1",
        "pack": "structure_v1_btcusdt_k5_double3h_v1",
    },
    {
        "account": "Xxobster10",
        "label": "SOL_k5_double3h",
        "ledger_key": "llm2-structure-sol-k5-double3h-v1",
        "pack": "structure_v1_solusdt_k5_double3h_v1",
    },
    {
        "account": "unassigned",
        "label": "ETH_k5_double3h",
        "ledger_key": "llm2-structure-eth-k5-double3h-v1",
        "pack": "structure_v1_ethusdt_k5_double3h_v1",
    },
]

PRED_TOL = 1e-9


def _utc(ms: int) -> str:
    return datetime.fromtimestamp(int(ms) / 1000, tz=timezone.utc).isoformat()


def _resolve_edge(strategy: dict) -> tuple[float, str]:
    family = target_family(str(strategy.get("target") or "fwd_return"))
    default_edge = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    edge = float(strategy.get("min_edge", default_edge))
    if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
        edge = DIRECTION_BAND
    return edge, family


def _load_ledgers() -> dict[str, Any]:
    out: dict[str, Any] = {}
    if LEDGERS_LN1.is_file():
        out.update(json.loads(LEDGERS_LN1.read_text(encoding="utf-8")))
    return out


def _recompute(
    symbol: str,
    timeframe: str,
    cols: list[str],
    model: Any,
    family: str,
    *,
    start_ms: int,
    end_ms: int,
) -> pd.DataFrame:
    ohlcv = load_ohlcv(symbol, timeframe)
    o_ms = index_to_ms(ohlcv.index)
    ohlcv = ohlcv.loc[(o_ms >= start_ms) & (o_ms <= end_ms)].copy()
    feats = build_space(
        ohlcv, "structure_v1", symbol=symbol, timeframe=timeframe, recent_only=False
    )
    aligned = feats.reindex(columns=cols)
    for c in aligned.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            aligned[c] = aligned[c].fillna(0.0)
    valid = aligned.dropna()
    pred = model.predict(valid.to_numpy(dtype=float))
    mean = np.asarray(
        pred.mean if hasattr(pred, "mean") else pred, dtype=float
    ).reshape(-1)
    side = proxy_side(mean, family)
    out = pd.DataFrame(
        {"pred_mean": mean, "side": side.astype(int)}, index=valid.index
    )
    out["ts_ms"] = index_to_ms(valid.index)
    return out, valid, ohlcv


def _replay_gate(
    bars: list[dict],
    cfg: dict,
    *,
    edge: float,
    seeded_hist: list[float],
    exit_aware: bool,
    dec_ohlcv: pd.DataFrame,
    dec_ts: np.ndarray,
    tf_ms: int,
) -> dict[str, Any]:
    """Replay the *live* gate function over live predictions under a state model."""
    hist: list[float] = list(seeded_hist)
    open_until: dict[int, list[int]] = {1: [], -1: []}
    last_entry: dict[int, int | None] = {1: None, -1: None}
    emitted: list[dict] = []
    skips: dict[str, int] = {}
    for b in bars:
        ts = int(b["ts_ms"])
        s = int(b["side"])
        m = float(b["pred_mean"])
        if s == 0 or not np.isfinite(m) or abs(m) < edge:
            continue
        open_until[s] = [t for t in open_until[s] if int(t) > ts]
        gate = decide_entry_gate(
            side=s,
            pred_mean=m,
            n_open_same_side=len(open_until[s]),
            strength_hist=hist,
            cfg=cfg,
            bar_ts_ms=ts,
            last_entry_ts_ms=last_entry[s],
        )
        if gate.get("append_strength"):
            hist.append(float(gate.get("abs_mean") or abs(m)))
            hist = hist[-int(cfg["mean_lookback"]) :]
        if not gate["allow"]:
            key = str(gate.get("skip_reason") or "gate")
            skips[key] = skips.get(key, 0) + 1
            continue
        hold = int(gate["max_hold_bars"])
        tp = float(gate["tp_pct"])
        sl = float(gate["sl_pct"])
        if exit_aware:
            free_at = slot_release_ts_ms(
                ts,
                s,
                tp_pct=tp,
                sl_pct=sl,
                max_hold_bars=hold,
                bar_ts_ms=dec_ts,
                bar_open=dec_ohlcv["open"].to_numpy(dtype=float),
                bar_high=dec_ohlcv["high"].to_numpy(dtype=float),
                bar_low=dec_ohlcv["low"].to_numpy(dtype=float),
                tf_ms=tf_ms,
            )
        else:
            free_at = ts + hold * tf_ms
        open_until[s].append(free_at)
        last_entry[s] = ts
        emitted.append(
            {
                "ts_ms": ts,
                "side": s,
                "book_idx": int(gate["book_idx"]),
                "tp_pct": tp,
                "max_hold_bars": hold,
                "size_mult": float(gate.get("size_mult") or 1.0),
            }
        )
    return {"emitted": emitted, "skips": skips}


def _cmp(emitted: list[dict], live_orders: list[dict]) -> dict[str, Any]:
    e = {(int(x["ts_ms"]), int(x["side"])) for x in emitted}
    l = {(int(x["bar_ts_ms"]), int(x["side"])) for x in live_orders}
    inter = e & l
    return {
        "n_replay": len(e),
        "n_live": len(l),
        "match": len(inter),
        "replay_only": sorted(_utc(t) for t, _ in (e - l)),
        "live_only": sorted(_utc(t) for t, _ in (l - e)),
        "exact": len(e - l) == 0 and len(l - e) == 0,
    }


def audit_unit(u: dict, ledgers: dict) -> dict[str, Any]:
    unit = ledgers.get(u["ledger_key"]) or {}
    decisions = unit.get("decisions") or []
    if not decisions:
        return {**u, "error": "no_decisions"}

    pack = PACKS / u["pack"]
    strategy = json.loads((pack / "strategy.json").read_text(encoding="utf-8"))
    symbol = str(strategy["symbol"])
    timeframe = str(strategy["timeframe"])
    tf_ms = int(TF_MS[timeframe])
    edge, family = _resolve_edge(strategy)
    mt_cfg = parse_multitrade_config(strategy)

    blob = joblib.load(pack / "model.joblib")
    model = blob["model"] if isinstance(blob, dict) and "model" in blob else blob
    cols = list(
        (blob.get("feature_columns") if isinstance(blob, dict) else None)
        or strategy.get("feature_columns")
        or []
    )

    live_bars = []
    live_orders = []
    for d in decisions:
        det = d.get("detail") or {}
        pm = d.get("pred_mean")
        if pm is None:
            continue
        row = {
            "ts_ms": int(d["bar_ts_ms"]),
            "side": int(d.get("side") or 0),
            "pred_mean": float(pm),
            "skip_reason": det.get("skip_reason"),
            "gate": det.get("multitrade_gate") or {},
            "snapshot": (det.get("feature_snapshot") or {}).get("values") or {},
            "order_retCode": det.get("order_retCode"),
        }
        live_bars.append(row)
        if det.get("order_retCode") in (0, "0"):
            live_orders.append(
                {
                    "bar_ts_ms": int(d["bar_ts_ms"]),
                    "side": int(d.get("side") or 0),
                    "book_idx": int((det.get("multitrade_gate") or {}).get("book_idx") or 1),
                    "tp_pct": float(det.get("tp_pct") or strategy.get("tp_pct") or 0.01),
                    "max_hold_bars": int(
                        det.get("max_hold_bars") or strategy.get("horizon_bars") or 6
                    ),
                    "qty": float(det.get("order_qty") or 0.0),
                    "size_mult": float(
                        (det.get("multitrade_gate") or {}).get("size_mult") or 1.0
                    ),
                }
            )
    live_bars.sort(key=lambda r: r["ts_ms"])
    if not live_bars:
        return {**u, "error": "no_pred_bars"}

    first_ms = live_bars[0]["ts_ms"]
    last_ms = live_bars[-1]["ts_ms"]
    lookback = int((mt_cfg or {}).get("mean_lookback") or 168)
    warm_ms = first_ms - (lookback + 500) * tf_ms

    local, feat_df, dec_ohlcv = _recompute(
        symbol, timeframe, cols, model, family, start_ms=warm_ms, end_ms=last_ms + tf_ms
    )
    local_by_ts = {int(t): i for i, t in enumerate(local["ts_ms"].to_numpy())}

    # ---- Layer A: prediction parity -------------------------------------------------
    diffs = []
    feature_offenders: dict[str, int] = {}
    n_cmp = 0
    n_missing = 0
    for r in live_bars:
        idx = local_by_ts.get(r["ts_ms"])
        if idx is None:
            n_missing += 1
            continue
        n_cmp += 1
        d = float(local["pred_mean"].iloc[idx]) - r["pred_mean"]
        diffs.append(abs(d))
        if abs(d) > PRED_TOL and r["snapshot"]:
            row = feat_df.iloc[idx]
            worst = None
            worst_gap = 0.0
            for c in cols:
                lv = r["snapshot"].get(c)
                if lv is None:
                    continue
                gap = abs(float(row[c]) - float(lv))
                scale = max(1.0, abs(float(lv)))
                if gap / scale > worst_gap:
                    worst_gap = gap / scale
                    worst = c
            if worst:
                feature_offenders[worst] = feature_offenders.get(worst, 0) + 1
    # Trailing run of exact bars: shows whether the unit is parity-clean *now* even
    # when earlier history was computed by a since-fixed live defect.
    trailing = 0
    last_bad = None
    for r in reversed(live_bars):
        idx = local_by_ts.get(r["ts_ms"])
        if idx is None:
            break
        if abs(float(local["pred_mean"].iloc[idx]) - r["pred_mean"]) <= PRED_TOL:
            trailing += 1
        else:
            last_bad = _utc(r["ts_ms"])
            break

    diffs_a = np.asarray(diffs, dtype=float) if diffs else np.zeros(0)
    layer_a = {
        "trailing_identical_bars": trailing,
        "last_divergent_bar_utc": last_bad,
        "bars_compared": n_cmp,
        "bars_missing_locally": n_missing,
        "max_abs_pred_diff": float(diffs_a.max()) if diffs_a.size else None,
        "median_abs_pred_diff": float(np.median(diffs_a)) if diffs_a.size else None,
        "n_bars_pred_differ": int((diffs_a > PRED_TOL).sum()) if diffs_a.size else 0,
        "n_bars_side_flip": int(
            sum(
                1
                for r in live_bars
                if (i := local_by_ts.get(r["ts_ms"])) is not None
                and int(local["side"].iloc[i]) != int(r["side"])
            )
        ),
        "top_divergent_features": sorted(
            feature_offenders.items(), key=lambda kv: -kv[1]
        )[:8],
    }

    # ---- Layer B: gate parity -------------------------------------------------------
    layer_b: dict[str, Any] = {}
    if mt_cfg is not None:
        dec_ts = index_to_ms(dec_ohlcv.index)
        pre = [
            r
            for r in (
                {"ts_ms": int(t), "side": int(local["side"].iloc[i]), "pred_mean": float(local["pred_mean"].iloc[i])}
                for i, t in enumerate(local["ts_ms"].to_numpy())
            )
            if r["ts_ms"] < first_ms
        ]
        seeded = [
            abs(r["pred_mean"])
            for r in pre
            if r["side"] != 0 and abs(r["pred_mean"]) >= edge
        ][-lookback:]
        for name, seed, ex_aware in (
            ("C0_cold_holdslots", [], False),
            ("C1_seeded_holdslots", seeded, False),
            ("C2_cold_exitaware", [], True),
            ("C3_seeded_exitaware", seeded, True),
        ):
            rep = _replay_gate(
                live_bars,
                mt_cfg,
                edge=edge,
                seeded_hist=list(seed),
                exit_aware=ex_aware,
                dec_ohlcv=dec_ohlcv,
                dec_ts=dec_ts,
                tf_ms=tf_ms,
            )
            layer_b[name] = {**_cmp(rep["emitted"], live_orders), "skips": rep["skips"]}
        layer_b["seed_strength_n"] = len(seeded)
    else:
        # Single book: live allows one open position per symbol.
        emitted = []
        busy_until = 0
        hold = int(strategy.get("horizon_bars") or 6)
        for r in live_bars:
            if r["side"] == 0 or abs(r["pred_mean"]) < edge:
                continue
            if r["ts_ms"] < busy_until:
                continue
            emitted.append({"ts_ms": r["ts_ms"], "side": r["side"]})
            busy_until = r["ts_ms"] + hold * tf_ms
        layer_b["single_book_holdslots"] = _cmp(emitted, live_orders)

    # ---- Layer C: execution fields --------------------------------------------------
    size_mults = sorted({round(float(o["size_mult"]), 4) for o in live_orders})
    tps = sorted({round(float(o["tp_pct"]), 6) for o in live_orders})
    holds = sorted({int(o["max_hold_bars"]) for o in live_orders})
    layer_c = {
        "live_size_mults": size_mults,
        "live_tp_pcts": tps,
        "live_max_holds": holds,
        "bt_applies_size_mult": False,
        "size_double_configured": bool((mt_cfg or {}).get("size_double_within_bars")),
    }

    return {
        **u,
        "symbol": symbol,
        "timeframe": timeframe,
        "target": strategy.get("target"),
        "min_edge_used": edge,
        "multitrade": mt_cfg is not None,
        "window": [_utc(first_ms), _utc(last_ms)],
        "n_decision_bars": len(live_bars),
        "n_live_orders": len(live_orders),
        "layer_a_prediction": layer_a,
        "layer_b_gate": layer_b,
        "layer_c_execution": layer_c,
    }


def main() -> int:
    ledgers = _load_ledgers()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    out = []
    for u in UNITS:
        if only and u["label"] not in only and u["account"] not in only:
            continue
        try:
            rep = audit_unit(u, ledgers)
        except Exception as exc:  # noqa: BLE001
            rep = {**u, "error": f"{type(exc).__name__}: {exc}"}
        out.append(rep)
        print(json.dumps(rep, indent=2, default=str), flush=True)
    path = OUT_DIR / "audit_latest.json"
    path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print("WROTE", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
