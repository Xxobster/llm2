"""One-shot VPS timing of the structure micro-live decision path. No orders."""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

os.environ.setdefault(
    "LLM2_INDICATORS_DB",
    "/opt/llm2-structure/pack/indicators_live_slice.sqlite",
)
os.environ.setdefault("LLM2_STRUCTURE_SOURCE", "bybit")
sys.path.insert(0, "/opt/llm2-structure")

from llm2.data.indicators import clear_indicator_cache  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.live.micro_runner import (  # noqa: E402
    _features_from_rest_ohlcv,
    _load_pack,
    decide_once,
    fetch_mark_last,
    fetch_ohlcv_rest,
)
from llm2.live.refresh_structure import refresh_symbol  # noqa: E402


def ms(t0: float) -> float:
    return (time.perf_counter() - t0) * 1000.0


def main() -> int:
    pack_dir = Path("/opt/llm2-structure/pack")
    pack = _load_pack(pack_dir)
    symbol = pack["strategy"]["symbol"]
    tf = pack["strategy"]["timeframe"]
    cols = list(pack["blob"]["feature_columns"])
    out: dict[str, float] = {}

    t0 = time.perf_counter()
    ohlcv = fetch_ohlcv_rest(symbol, tf, limit=300)
    out["fetch_ohlcv_ms"] = ms(t0)
    closed = ohlcv.iloc[:-1]

    t0 = time.perf_counter()
    refresh_symbol(
        symbol=symbol,
        timeframes=("1h", "4h", "1w"),
        indicator_db=pack_dir / "indicators_live_slice.sqlite",
        limit=350,
    )
    out["refresh_350_ms"] = ms(t0)
    clear_indicator_cache()

    t0 = time.perf_counter()
    feats = _features_from_rest_ohlcv(
        closed, symbol=symbol, timeframe=tf, feature_columns=cols, pack_dir=pack_dir
    )
    out["features_helper_ms"] = ms(t0)
    print("features_helper_rows", None if feats is None else len(feats))
    if feats is not None:
        nan_cols = feats.iloc[-1][feats.iloc[-1].isna()].index.tolist()
        print("last_row_nan_cols", nan_cols[:20], "n=", len(nan_cols))

    clear_indicator_cache()
    t0 = time.perf_counter()
    raw = build_space(
        closed, "structure_v1", symbol=symbol, timeframe=tf, recent_only=True
    )
    out["build_space_cold_ms"] = ms(t0)
    print("build_space_cols", len(raw.columns), "rows", len(raw))
    print("build_last_nan", int(raw.iloc[-1].isna().sum()))

    t0 = time.perf_counter()
    decision = decide_once(pack=pack, ohlcv=closed, pack_dir=pack_dir)
    out["decide_once_ms"] = ms(t0)
    print("decision", {k: decision.get(k) for k in ("side", "pred_mean", "reason", "bar_ts")})

    t0 = time.perf_counter()
    _ = fetch_mark_last(symbol)
    out["fetch_mark_ms"] = ms(t0)

    t0 = time.perf_counter()
    _ = decide_once(pack=pack, ohlcv=closed, pack_dir=pack_dir)
    out["decide_once_warm_ms"] = ms(t0)

    pred_ms = 0.0
    if feats is not None and not feats.iloc[-1].isna().any():
        x = feats.iloc[[-1]].to_numpy(dtype=float)
        model = pack["blob"]["model"]
        t0 = time.perf_counter()
        model.predict(x)
        pred_ms = ms(t0)
    out["model_predict_ms"] = pred_ms
    out["total_like_live_ms"] = (
        out["fetch_ohlcv_ms"]
        + out["refresh_350_ms"]
        + out["decide_once_ms"]
        + out["fetch_mark_ms"]
    )

    print("TIMINGS_MS")
    for k in sorted(out):
        print(f"{k}: {out[k]:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
