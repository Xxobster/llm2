"""Physical train/test parquet splits with independent feature computation."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Callable

import pandas as pd

from llm2.paths import ARTIFACTS


def fold_dir(symbol: str, timeframe: str, fold_index: int) -> Path:
    return ARTIFACTS / "folds" / symbol.upper() / timeframe / f"fold_{fold_index:02d}"


@lru_cache(maxsize=1)
def parquet_engine() -> str:
    """Pick a parquet engine that actually works in this environment.

    ``pandas`` normally falls back from pyarrow to fastparquet on its own, but not when
    pyarrow is *importable yet broken*. On this machine an Application Control policy
    blocks pyarrow's native library, which leaves a half-initialised module: pandas selects
    it, then dies on ``register_extension_type`` with "pandas.period already defined".

    That failure took down every combo of the autonomy sweep at the train/test split step
    while the sweep dutifully logged the traceback and moved to the next one, so a run that
    looked like it was working produced no research at all. Picking the engine explicitly,
    once, by trying a real round trip, removes the whole failure mode.
    """
    probe = pd.DataFrame({"a": [1]})
    errors: list[str] = []
    for engine in ("pyarrow", "fastparquet"):
        try:
            import io

            buf = io.BytesIO()
            probe.to_parquet(buf, engine=engine, index=False)
            return engine
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{engine}: {type(exc).__name__}: {exc}")
    raise ImportError(
        "no working parquet engine; physical train/test splits cannot be written.\n  "
        + "\n  ".join(errors)
    )


def write_fold_parquet(
    df: pd.DataFrame,
    path: Path,
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.reset_index()
    if "timestamp" in out.columns:
        out["ts_ms"] = pd.to_datetime(out["timestamp"], utc=True).astype("int64") // 1_000_000
    out.to_parquet(path, index=False, engine=parquet_engine())
    return path


def split_and_materialize(
    ohlcv: pd.DataFrame,
    train_mask: pd.Series,
    test_mask: pd.Series,
    *,
    symbol: str,
    timeframe: str,
    fold_index: int,
    build_features: Callable[[pd.DataFrame], pd.DataFrame],
    build_labels: Callable[[pd.DataFrame], pd.DataFrame] | None = None,
) -> dict[str, Path]:
    """Write separate train/test parquet with features computed on each split only."""
    base = fold_dir(symbol, timeframe, fold_index)
    paths: dict[str, Path] = {}

    for split_name, mask in (("train", train_mask), ("test", test_mask)):
        raw = ohlcv.loc[mask].copy()
        feats = build_features(raw)
        merged = feats.join(raw[["open", "high", "low", "close", "volume"]], how="left")
        if build_labels is not None:
            labels = build_labels(raw)
            merged = merged.join(labels, how="left", rsuffix="_lbl")
        p = base / f"{split_name}.parquet"
        write_fold_parquet(merged, p)
        paths[split_name] = p

    return paths
