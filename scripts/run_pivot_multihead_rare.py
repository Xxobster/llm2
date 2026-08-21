"""Tight rarity + multi-head pivot forecast settle (agreed next steps).

- Strict ATR labels + longer horizons (rarer any-event)
- Heads: P(any), P(high|event), time-to-pivot bars, level return at pivot
- LGBM / HistGB only vs baserate; no chat LLM
- Metrics: PR-AUC vs baserate, Brier, ECE (binary); MAE/corr for time & level
- Outer fold geometry V2, pre-lockbox only

Binance candles only. RESEARCH_ONLY.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.pivot.labels.config import PivotLabelConfig  # noqa: E402
from llm2.pivot.train.multihead import model_specs_tight, multihead_walk_forward  # noqa: E402
from llm2.pivot.train.samples import build_samples  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION  # noqa: E402

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
# Rarer "any" events: SHORT horizon + high ATR (long H makes any-pivot almost always true).
SETTINGS = [
    # (tf, H_bars, max_rows, atr_min, tag)
    ("15m", 3, 120_000, 1.5, "rare_H3_atr1.5"),
    ("15m", 4, 120_000, 2.0, "rare_H4_atr2.0"),
    ("1h", 3, 60_000, 1.5, "rare_H3_atr1.5"),
    ("5m", 6, 90_000, 1.5, "rare_H6_atr1.5"),  # BTC only
]
PACK = "price_vol_mom"


def _cfg(tf: str, atr: float, tag: str) -> PivotLabelConfig:
    lb = 3 if tf != "1d" else 2
    return PivotLabelConfig(
        timeframe=tf,
        left_bars=lb,
        right_bars=lb,
        confirm_bars=lb,
        min_left_prominence_atr=atr,
        min_right_reversal_atr=atr,
        min_reversal_pct=0.0015 if tf == "15m" else (0.001 if tf == "5m" else 0.002),
        atr_period=14,
        label_family=f"fractal_{tag}",
        suppress_neighbor_bars=3,
    )


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(f"PIVOT_MULTIHEAD_RARE start fold={FOLD_GEOMETRY_VERSION}", tier=0)
    print(f"multihead rare stamp={stamp}", flush=True)
    models = model_specs_tight()
    print("models", [m.name for m in models] + ["baserate"], flush=True)

    rows = []
    for symbol in SYMBOLS:
        for tf, h, max_rows, atr, tag in SETTINGS:
            if tf == "5m" and symbol != "BTCUSDT":
                continue
            cfg = _cfg(tf, atr, tag)
            print(f"SAMPLES {symbol} {tf} {tag} H={h} atr>={atr} …", flush=True)
            try:
                samp = build_samples(
                    symbol=symbol,
                    timeframe=tf,
                    feature_pack=PACK,
                    label_cfg=cfg,
                    horizon_bars=h,
                    max_rows=max_rows,
                )
            except Exception as exc:  # noqa: BLE001
                print(f"  SAMPLE_FAIL {exc}", flush=True)
                rows.append(
                    {
                        "symbol": symbol,
                        "timeframe": tf,
                        "tag": tag,
                        "status": "SAMPLE_FAIL",
                        "error": str(exc)[:300],
                    }
                )
                continue
            print(
                f"  n={samp['n_rows']} frac_any={samp['frac_any']:.3f} "
                f"counts={samp['class_counts']}",
                flush=True,
            )
            purge = max(h + cfg.right_bars + 4, 24)
            for name, ms, is_br in (
                [("baserate", None, True)]
                + [(m.name, m, False) for m in models]
            ):
                print(f"  head-eval {name} …", flush=True)
                try:
                    res = multihead_walk_forward(
                        samp,
                        model_spec=ms,
                        purge_bars=purge,
                        embargo_bars=purge,
                        is_baserate=is_br,
                    )
                except Exception as exc:  # noqa: BLE001
                    res = {"status": "FAIL", "error": str(exc)[:300]}
                any_p = (res.get("pooled") or {}).get("any") or {}
                print(
                    f"    {res.get('status')} any PR-AUC={any_p.get('pr_auc')} "
                    f"Brier={any_p.get('brier')} ECE={any_p.get('ece')} "
                    f"frac={any_p.get('frac_pos')}",
                    flush=True,
                )
                rows.append(
                    {
                        "symbol": symbol,
                        "timeframe": tf,
                        "horizon_bars": h,
                        "atr_min": atr,
                        "tag": tag,
                        "feature_pack": PACK,
                        "model": name,
                        "n_rows": samp["n_rows"],
                        "frac_any": samp["frac_any"],
                        "class_counts": samp["class_counts"],
                        "label_config_version": samp["label_config_version"],
                        "result": res,
                    }
                )

    # Lifts vs baserate for any-head
    leaders = []
    by_key: dict[tuple, dict] = {}
    for r in rows:
        res = r.get("result") or {}
        if res.get("status") != "OK":
            continue
        key = (r["symbol"], r["timeframe"], r["tag"])
        any_m = (res.get("pooled") or {}).get("any") or {}
        by_key.setdefault(key, {})[r["model"]] = {
            "any": any_m,
            "high_given_event": (res.get("pooled") or {}).get("high_given_event"),
            "time_to_event": (res.get("pooled") or {}).get("time_to_event"),
            "level_ret": (res.get("pooled") or {}).get("level_ret"),
            "row": r,
        }
    for key, models_d in by_key.items():
        br = models_d.get("baserate", {}).get("any") or {}
        for mname, blob in models_d.items():
            if mname == "baserate":
                continue
            any_m = blob.get("any") or {}
            pr = any_m.get("pr_auc")
            pr_b = br.get("pr_auc")
            lift = (
                float(pr - pr_b)
                if pr is not None and pr_b is not None and pr == pr and pr_b == pr_b
                else float("nan")
            )
            leaders.append(
                {
                    "symbol": key[0],
                    "timeframe": key[1],
                    "tag": key[2],
                    "model": mname,
                    "frac_any": any_m.get("frac_pos"),
                    "pr_auc_any": pr,
                    "pr_auc_baserate": pr_b,
                    "pr_auc_lift": lift,
                    "brier_any": any_m.get("brier"),
                    "brier_baserate": br.get("brier"),
                    "ece_any": any_m.get("ece"),
                    "high_given_pr_auc": (blob.get("high_given_event") or {}).get("pr_auc"),
                    "high_given_ece": (blob.get("high_given_event") or {}).get("ece"),
                    "time_mae_bars": (blob.get("time_to_event") or {}).get("mae_bars"),
                    "time_corr": (blob.get("time_to_event") or {}).get("corr"),
                    "level_mae_ret": (blob.get("level_ret") or {}).get("mae_ret"),
                    "level_corr": (blob.get("level_ret") or {}).get("corr"),
                }
            )
    leaders.sort(
        key=lambda x: (
            -(x["pr_auc_lift"] if x["pr_auc_lift"] == x["pr_auc_lift"] else -9),
            x["brier_any"] if x["brier_any"] == x["brier_any"] else 9,
        )
    )

    report = {
        "generation_id": "pivot_mtf_forecast_001_multihead_rare",
        "stamp": stamp,
        "source": "binance",
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "lockbox_start": FORWARD_LOCKBOX_START,
        "metric_clarification": {
            "prior_0p815": (
                "Was outer PR-AUC for any-pivot on an easy dense-label setting "
                "(baserate already ~0.785), NOT classification precision 81.5%."
            ),
            "primary_now": "PR-AUC_any - PR-AUC_baserate, plus Brier and ECE; time MAE/corr; level MAE/corr",
        },
        "heads": ["P_any", "P_high_given_event", "E_time_bars", "E_level_ret"],
        "leaderboard": leaders[:25],
        "all_results": rows,
        "readiness_max": "RESEARCH_ONLY",
        "note": "No live. Promote only if calibration ECE is low and lift is material on outer OOS.",
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"multihead_rare_{stamp}.json"
    latest = out_dir / "multihead_rare_latest.json"
    text = json.dumps(report, indent=2, default=str)
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    print(f"\nWROTE {out}", flush=True)
    print("=== TOP lifts PR-AUC_any vs baserate ===", flush=True)
    for i, L in enumerate(leaders[:12], 1):
        print(
            f"{i:2}. {L['symbol']} {L['timeframe']} {L['tag']} {L['model']}: "
            f"lift={L['pr_auc_lift']} PR={L['pr_auc_any']} vs base={L['pr_auc_baserate']} "
            f"frac_any={L['frac_any']} ECE={L['ece_any']} "
            f"time_corr={L['time_corr']} level_corr={L['level_corr']}",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
