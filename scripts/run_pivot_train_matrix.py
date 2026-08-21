"""Run multi-model / multi-feature pivot first-event forecasting experiments.

Binance last-trade only. RESEARCH_ONLY — no live orders.
Models are numerical classifiers (logistic, LightGBM variants, hist-GB, MLP).
Chat-style LLMs are not used as the numeric forecasting core (project rules).
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.pivot.labels.config import PivotLabelConfig  # noqa: E402
from llm2.pivot.train.samples import build_samples  # noqa: E402
from llm2.pivot.train.walk_forward import model_catalog, walk_forward_eval  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION  # noqa: E402

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
# Decision timeframes: 15m primary (coverage + speed); 1h secondary; 5m subsample BTC
SETTINGS = [
    # (timeframe, horizon_bars, max_rows, label_atr_min, label_tag)
    ("15m", 4, 120_000, 0.5, "frac_std"),
    ("15m", 4, 120_000, 0.85, "frac_strict"),
    ("1h", 4, 60_000, 0.6, "frac_std"),
    ("5m", 6, 80_000, 0.5, "frac_std"),  # tip window only
]
FEATURE_PACKS = ("price_vol", "price_vol_mom", "price_vol_mom_phys", "full")


def _label_cfg(tf: str, atr_min: float, tag: str) -> PivotLabelConfig:
    left = right = confirm = 3 if tf in {"5m", "15m", "1h"} else 2
    return PivotLabelConfig(
        timeframe=tf,
        left_bars=left,
        right_bars=right,
        confirm_bars=confirm,
        min_left_prominence_atr=float(atr_min),
        min_right_reversal_atr=float(atr_min),
        min_reversal_pct=0.001 if tf == "5m" else (0.0015 if tf == "15m" else 0.002),
        atr_period=14,
        label_family=f"fractal_prominence_atr_{tag}",
        suppress_neighbor_bars=2,
    )


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(f"PIVOT_TRAIN_MATRIX start fold={FOLD_GEOMETRY_VERSION}", tier=0)
    print(
        f"pivot train matrix stamp={stamp} lockbox_end={FORWARD_LOCKBOX_START}",
        flush=True,
    )
    catalog = model_catalog()
    print("models:", [m.name for m in catalog] + ["baserate"], flush=True)

    rows: list[dict] = []
    # Subsample full design to keep runtime tractable: all packs × models on BTC 15m;
    # other symbols use price_vol_mom + key models; 5m only BTC.
    for symbol in SYMBOLS:
        for tf, h_bars, max_rows, atr_min, tag in SETTINGS:
            if tf == "5m" and symbol != "BTCUSDT":
                continue
            packs = (
                FEATURE_PACKS
                if (symbol == "BTCUSDT" and tf == "15m" and tag == "frac_std")
                else ("price_vol_mom",)
            )
            for pack in packs:
                cfg = _label_cfg(tf, atr_min, tag)
                print(
                    f"SAMPLES {symbol} {tf} pack={pack} label={tag} H={h_bars} …",
                    flush=True,
                )
                try:
                    samp = build_samples(
                        symbol=symbol,
                        timeframe=tf,
                        feature_pack=pack,
                        label_cfg=cfg,
                        horizon_bars=h_bars,
                        max_rows=max_rows,
                    )
                except Exception as exc:  # noqa: BLE001
                    rows.append(
                        {
                            "symbol": symbol,
                            "timeframe": tf,
                            "feature_pack": pack,
                            "label": tag,
                            "status": "SAMPLE_FAIL",
                            "error": str(exc)[:300],
                        }
                    )
                    print(f"  FAIL sample {exc}", flush=True)
                    continue
                print(
                    f"  n={samp['n_rows']} events={samp['n_events']} "
                    f"counts={samp['class_counts']}",
                    flush=True,
                )
                purge = max(h_bars + cfg.right_bars + 2, 12)
                # baserate
                br = walk_forward_eval(
                    samp["X"],
                    samp["y"],
                    samp["ts_ms"],
                    model_spec=None,
                    purge_bars=purge,
                    embargo_bars=purge,
                    is_baserate=True,
                )
                rows.append(
                    {
                        "symbol": symbol,
                        "timeframe": tf,
                        "feature_pack": pack,
                        "label": tag,
                        "horizon_bars": h_bars,
                        "model": "baserate",
                        "n_rows": samp["n_rows"],
                        "class_counts": samp["class_counts"],
                        "label_config_version": samp["label_config_version"],
                        "result": br,
                    }
                )
                print(
                    f"  baserate pr_auc={br.get('pooled', {}).get('pr_auc_any')} "
                    f"brier={br.get('pooled', {}).get('brier_mc')}",
                    flush=True,
                )
                # model set: full on BTC 15m std; subset elsewhere
                models = catalog if (symbol == "BTCUSDT" and tf == "15m" and tag == "frac_std" and pack == "price_vol_mom") else [
                    m for m in catalog if m.name in {"logistic", "lgbm_m", "hist_gb", "mlp_sklearn"}
                ]
                if symbol == "BTCUSDT" and tf == "15m" and tag == "frac_std":
                    models = catalog  # all models for core pack grid
                for ms in models:
                    # For non-core packs on BTC, only lgbm_m + logistic
                    if (
                        symbol == "BTCUSDT"
                        and tf == "15m"
                        and tag == "frac_std"
                        and pack != "price_vol_mom"
                        and ms.name not in {"logistic", "lgbm_m", "hist_gb"}
                    ):
                        continue
                    print(f"  model {ms.name} …", flush=True)
                    try:
                        res = walk_forward_eval(
                            samp["X"],
                            samp["y"],
                            samp["ts_ms"],
                            model_spec=ms,
                            purge_bars=purge,
                            embargo_bars=purge,
                        )
                    except Exception as exc:  # noqa: BLE001
                        res = {"status": "MODEL_FAIL", "error": str(exc)[:300]}
                    rows.append(
                        {
                            "symbol": symbol,
                            "timeframe": tf,
                            "feature_pack": pack,
                            "label": tag,
                            "horizon_bars": h_bars,
                            "model": ms.name,
                            "n_rows": samp["n_rows"],
                            "class_counts": samp["class_counts"],
                            "label_config_version": samp["label_config_version"],
                            "result": res,
                        }
                    )
                    pooled = res.get("pooled") or {}
                    print(
                        f"    {res.get('status')} pr_auc={pooled.get('pr_auc_any')} "
                        f"brier={pooled.get('brier_mc')} "
                        f"prec@5%={pooled.get('precision_top5pct_any')}",
                        flush=True,
                    )

    # Rank by outer pooled PR-AUC any (higher better); Brier as secondary (lower better)
    ranked = []
    for r in rows:
        res = r.get("result") or {}
        if res.get("status") != "OK":
            continue
        p = res.get("pooled") or {}
        ranked.append(
            {
                "symbol": r["symbol"],
                "timeframe": r["timeframe"],
                "feature_pack": r["feature_pack"],
                "label": r["label"],
                "model": r["model"],
                "pr_auc_any": p.get("pr_auc_any"),
                "brier_mc": p.get("brier_mc"),
                "log_loss": p.get("log_loss"),
                "precision_top5pct_any": p.get("precision_top5pct_any"),
                "acc_side_argmax": p.get("acc_side_argmax"),
                "frac_any": p.get("frac_any"),
            }
        )
    ranked.sort(
        key=lambda x: (
            -(x["pr_auc_any"] if x["pr_auc_any"] == x["pr_auc_any"] else -1),
            x["brier_mc"] if x["brier_mc"] == x["brier_mc"] else 9,
        )
    )

    report = {
        "generation_id": "pivot_mtf_forecast_001_train_matrix",
        "stamp": stamp,
        "source": "binance",
        "product_note": "Binance last OHLCV only (RESEARCH). Not a live authorization.",
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "lockbox_start": FORWARD_LOCKBOX_START,
        "metrics_primary": "outer_pooled_pr_auc_any (first pivot within horizon)",
        "models_note": (
            "Numerical classifiers only. Chat/general LLMs are not the forecasting core."
        ),
        "n_rows": len(rows),
        "leaderboard_top20": ranked[:20],
        "all_results": rows,
        "readiness_max": "RESEARCH_ONLY",
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"train_matrix_{stamp}.json"
    latest = out_dir / "train_matrix_latest.json"
    payload = json.dumps(report, indent=2, default=str)
    out.write_text(payload, encoding="utf-8")
    latest.write_text(payload, encoding="utf-8")
    print(f"\nWROTE {out}", flush=True)
    print("=== TOP 10 by PR-AUC(any pivot) ===", flush=True)
    for i, r in enumerate(ranked[:10], 1):
        print(
            f"{i:2}. {r['symbol']} {r['timeframe']} {r['feature_pack']} "
            f"{r['label']} {r['model']}: PR-AUC={r['pr_auc_any']:.4f} "
            f"Brier={r['brier_mc']:.4f} prec@5%={r['precision_top5pct_any']}",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
