"""Run a bounded multi-config campaign from configs/generations/*.yaml."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from llm2.hunt.runner import HuntConfig, run_nested_hunt
from llm2.paths import ROOT, ensure_artifact_dirs


def load_cfg(path: Path) -> HuntConfig:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    return HuntConfig(
        generation_id=raw["generation_id"],
        symbol=raw.get("symbol", "BTCUSDT"),
        timeframe=raw.get("timeframe", "1h"),
        target=raw.get("target", "fwd_return"),
        feature_space=raw.get("feature_space", "ohlcv_v1"),
        horizon=int(raw.get("horizon", 6)),
        max_trials=int(raw.get("max_trials", 6)),
        seed=int(raw.get("seed", 42)),
        tp_pct=float(raw.get("tp_pct", 0.01)),
        sl_pct=float(raw.get("sl_pct", 0.02)),
        models=list(raw.get("models", HuntConfig(generation_id="x").models)),
        run_backtest=bool(raw.get("run_backtest", True)),
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--glob", default="configs/generations/gen_00*.yaml")
    p.add_argument("--no-backtest", action="store_true")
    args = p.parse_args()
    ensure_artifact_dirs()
    paths = sorted((ROOT).glob(args.glob))
    if not paths:
        print("No configs matched", args.glob)
        return 1
    summaries = []
    for path in paths:
        cfg = load_cfg(path)
        if args.no_backtest:
            cfg.run_backtest = False
        print("===", cfg.generation_id, "===")
        summary = run_nested_hunt(cfg)
        summaries.append(summary)
        print(json.dumps(summary, indent=2, default=str))
        if summary.get("best_tier", 0) >= 2:
            print("ALERT Tier>=2 — stop campaign for human review")
            break
    out = ROOT / "artifacts" / "reports" / "campaign_summary.json"
    out.write_text(json.dumps(summaries, indent=2, default=str), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
