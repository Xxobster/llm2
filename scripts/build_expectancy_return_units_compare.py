"""Build comparable expectancy_return_units table for all fleet packs."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import research_instrument  # noqa: E402
from tradesim.sizing import minimum_executable_qty  # noqa: E402

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

TRADES_ROOT = ARTIFACTS / "reports" / "structure_v1_fleet_streak_autopsy_001_trades"
OUT = ARTIFACTS / "reports" / "structure_v1_expectancy_return_units_compare_001.json"


def _eru_from_trades(df: pd.DataFrame, symbol: str) -> tuple[float, int, float, float | None]:
    ohlcv = load_ohlcv(symbol, "1h")
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)]
    ts = index_to_ms(ohlcv.index)
    close = ohlcv["close"].to_numpy(dtype=float)
    ts_to_px = {int(t): float(c) for t, c in zip(ts, close)}
    inst = research_instrument(symbol)
    pnls = df["pnl"].to_numpy(dtype=float)
    entry_ts = df["entry_ts_ms"].to_numpy(dtype=np.int64)
    tags = df["tag"].astype(str) if "tag" in df.columns else pd.Series([""] * len(df))
    size_mult = np.ones(len(df), dtype=float)
    for i, tag in enumerate(tags):
        if "_x2" in tag:
            size_mult[i] = 2.0
        elif "_x" in tag:
            try:
                size_mult[i] = float(tag.rsplit("_x", 1)[-1].split("_")[0])
            except Exception:
                size_mult[i] = 1.0
    rets: list[float] = []
    for p, ets, sm in zip(pnls, entry_ts, size_mult):
        px = ts_to_px.get(int(ets))
        if px is None or not np.isfinite(px) or px <= 0 or not np.isfinite(p):
            rets.append(float("nan"))
            continue
        q = float(minimum_executable_qty(inst, px)) * float(sm)
        notional = q * px
        rets.append(float(p) / notional if notional > 0 else float("nan"))
    rets_a = np.asarray(rets, dtype=float)
    valid = np.isfinite(rets_a)
    n = int(valid.sum())
    eru = float(np.mean(rets_a[valid])) if n else float("nan")
    a = pnls[np.isfinite(pnls)]
    wr = float(np.mean(a > 0)) if a.size else float("nan")
    gp = float(a[a > 0].sum()) if a.size else 0.0
    gl = float((-a[a < 0]).sum()) if a.size else 0.0
    pf: float | None
    if gl > 0:
        pf = gp / gl
    elif gp > 0:
        pf = None  # inf
    else:
        pf = float("nan")
    return eru, n, wr, pf


def _family(vid: str) -> str:
    v = vid.lower()
    if "multitrade" in v:
        return "multitrade"
    if "k5" in v or "double" in v:
        return "k5_double"
    if "clarity" in v:
        return "clarity_hold12"
    return "single"


def main() -> int:
    rows: list[dict] = []
    for csv in sorted(TRADES_ROOT.glob("*_trades.csv")):
        df = pd.read_csv(csv)
        if df.empty:
            continue
        vid = str(df["version_id"].iloc[0])
        symbol = str(df["symbol"].iloc[0]).upper()
        try:
            eru, n_valid, wr, pf = _eru_from_trades(df, symbol)
        except Exception as exc:  # noqa: BLE001
            rows.append(
                {
                    "version_id": vid,
                    "symbol": symbol,
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
            continue
        rows.append(
            {
                "version_id": vid,
                "symbol": symbol,
                "family": _family(vid),
                "n_trades": int(len(df)),
                "n_exp_valid": n_valid,
                "expectancy_return_units": eru,
                "expectancy_return_pct": (eru * 100.0) if math.isfinite(eru) else None,
                "win_rate": wr,
                "profit_factor": pf,
                "source": "fleet_autopsy_outer_v2",
                "window": "outer folds end < 2026-05-01 lockbox unused",
                "metric_note": (
                    "proxy E[r]=mean(pnl/(min_exchange_qty*entry_close*size_tag)); "
                    "MIN_EXCHANGE geometry; comparable across packs"
                ),
            }
        )
        print(
            f"{vid}: E[r]%={(eru * 100):.4f} n={n_valid} pf={pf}",
            flush=True,
        )

    # Nested research arms (tradesim headline metric)
    for arm in (
        {
            "version_id": "eth_k5_p75_strength (research)",
            "symbol": "ETHUSDT",
            "family": "research_arm",
            "n_trades": 5996,
            "n_exp_valid": 5996,
            "expectancy_return_units": 0.0064316547337478335,
            "expectancy_return_pct": 0.6431654733747834,
            "win_rate": None,
            "profit_factor": 7.044474928687612,
            "source": "structure_v1_eth_k5_expectancy_strength_p75_001",
            "window": "outer folds end < 2026-05-01",
            "metric_note": "tradesim expectancy_return_units stitched",
        },
        {
            "version_id": "eth_mt_v1_2 cooloff3 (research)",
            "symbol": "ETHUSDT",
            "family": "research_arm",
            "n_trades": 11882,
            "n_exp_valid": 11882,
            "expectancy_return_units": 0.007974530894855244,
            "expectancy_return_pct": 0.7974530894855244,
            "win_rate": None,
            "profit_factor": 4.309749181761305,
            "source": "structure_v1_eth_multitrade_loss_streak_cooloff_001",
            "window": "outer folds end < 2026-05-01",
            "metric_note": "tradesim expectancy_return_units stitched; failed vs control",
        },
        {
            "version_id": "eth_mt_v1_2 live control (research settle)",
            "symbol": "ETHUSDT",
            "family": "research_arm",
            "n_trades": 12608,
            "n_exp_valid": 12608,
            "expectancy_return_units": 0.008020978933362125,
            "expectancy_return_pct": 0.8020978933362125,
            "win_rate": None,
            "profit_factor": 4.255642815858733,
            "source": "structure_v1_eth_multitrade_loss_streak_cooloff_001 control",
            "window": "outer folds end < 2026-05-01",
            "metric_note": "tradesim expectancy_return_units stitched",
        },
    ):
        rows.append(arm)

    ok = [
        r
        for r in rows
        if r.get("expectancy_return_units") is not None
        and math.isfinite(float(r["expectancy_return_units"]))
    ]
    ok.sort(key=lambda r: -float(r["expectancy_return_units"]))
    payload = {
        "generation_id": "structure_v1_expectancy_return_units_compare_001",
        "evidence_class": "MEASURE_DIAGNOSTIC",
        "window": "outer fold geometry v2; hard end exclusive 2026-05-01; lockbox unused",
        "n_rows": len(ok),
        "rows": ok,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"wrote {OUT} rows={len(ok)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
