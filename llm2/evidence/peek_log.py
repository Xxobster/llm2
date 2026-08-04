"""Append-only research peek log — contamination is explicit.

Viewing a holdout for charts, multi-arm grids, or parameter ranking is permanent
for that claim set. Copying SQLite elsewhere does not clear the log.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from llm2.paths import (
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    POST_MULTITRADE_FREEZE_START,
    ROOT,
)

# Re-export for callers that import from peek_log only.
__all__ = [
    "POST_MULTITRADE_FREEZE_START",
    "PEEK_LOG_PATH",
    "LOCKED_MULTITRADE_ARM",
    "append_peek",
    "read_peeks",
    "window_overlaps_contaminated_lockbox",
    "is_post_freeze_window",
    "seed_known_multitrade_peeks",
]

PEEK_LOG_PATH = ARTIFACTS / "evidence" / "peek_log.jsonl"
LOCKED_MULTITRADE_ARM = {
    "version_id": "eth_multitrade_v1_1",
    "strategy_id": "structure_v1_lgbm_ETHUSDT_1h_direction_multitrade_v1_1",
    "clarity": "mean_strength",
    "switch_book": 3,
    "addon_tp_pct": 0.02618,
    "hold_addon": 12,
    "k_per_side": 7,
    "sl_pct": 0.02,
    "base_tp_pct": 0.01,
    "base_hold": 6,
    "evidence_class_for_promotion": "outer_fold_stitch_or_post_freeze_forward_only",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def default_peek_log_path() -> Path:
    override = (os.environ.get("LLM2_PEEK_LOG") or "").strip()
    if override:
        return Path(override)
    return PEEK_LOG_PATH


def append_peek(
    *,
    experiment_id: str,
    window_start: str,
    window_end: str,
    purpose: str,
    arms: str | Iterable[Any] | None = None,
    evidence_class: str = "LOCKBOX_OPENED_CONTAMINATED",
    n_arms: int | None = None,
    notes: str = "",
    path: Path | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Append one peek event. Always diagnostic for promotion if window overlaps lockbox."""
    log_path = path or default_peek_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if arms is None:
        arms_out: Any = None
    elif isinstance(arms, str):
        arms_out = arms
    else:
        arms_out = list(arms)
        if n_arms is None:
            n_arms = len(arms_out)
    record: dict[str, Any] = {
        "ts_utc": _utc_now(),
        "experiment_id": str(experiment_id),
        "window_start": str(window_start),
        "window_end": str(window_end),
        "purpose": str(purpose),
        "arms": arms_out,
        "n_arms": n_arms,
        "evidence_class": str(evidence_class),
        "notes": str(notes or ""),
        "policy": {
            "copy_db_does_not_reset": True,
            "quotable_historical_edge": "outer_fold_settle_only",
            "multitrade_knobs_this_window": "diagnostic_only",
            "clean_param_claim_from": POST_MULTITRADE_FREEZE_START,
        },
    }
    if extra:
        record["extra"] = extra
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, default=str, sort_keys=False) + "\n")
    return record


def read_peeks(*, path: Path | None = None) -> list[dict[str, Any]]:
    log_path = path or default_peek_log_path()
    if not log_path.is_file():
        return []
    out: list[dict[str, Any]] = []
    for line in log_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def window_overlaps_contaminated_lockbox(window_start: str, window_end: str) -> bool:
    """True if [start, end) intersects [FORWARD_LOCKBOX_START, POST_MULTITRADE_FREEZE_START)."""
    import pandas as pd

    w0 = pd.Timestamp(window_start, tz="UTC")
    w1 = pd.Timestamp(window_end, tz="UTC")
    c0 = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    c1 = pd.Timestamp(POST_MULTITRADE_FREEZE_START, tz="UTC")
    # half-open overlap
    return w0 < c1 and w1 > c0


def is_post_freeze_window(window_start: str) -> bool:
    import pandas as pd

    return pd.Timestamp(window_start, tz="UTC") >= pd.Timestamp(
        POST_MULTITRADE_FREEZE_START, tz="UTC"
    )


def seed_known_multitrade_peeks(*, path: Path | None = None, force: bool = False) -> int:
    """Idempotent seed of 2026-08-04 multitrade / concurrent lockbox peeks (D-035/D-036)."""
    log_path = path or default_peek_log_path()
    if log_path.is_file() and not force:
        existing = {r.get("experiment_id") for r in read_peeks(path=log_path)}
        if "structure_v1_eth_switch_tp_ablation_001" in existing:
            return 0
    seeds = [
        {
            "experiment_id": "structure_v1_lockbox_eth_sol_finplot",
            "window_start": FORWARD_LOCKBOX_START,
            "window_end": "2026-08-03",
            "purpose": "finplot_lockbox_open",
            "arms": "frozen single-book ETH/SOL direction packs",
            "n_arms": 2,
            "notes": "D-035 initial lockbox open",
        },
        {
            "experiment_id": "structure_v1_eth_concurrent_fib_clarity_v2_ext",
            "window_start": FORWARD_LOCKBOX_START,
            "window_end": "2026-08-04",
            "purpose": "multi_arm_lockbox_grid",
            "arms": "258 arms fib_ext × clarity × hold × K",
            "n_arms": 258,
            "notes": "Fibonacci extension / concurrent grid; diagnostic only",
        },
        {
            "experiment_id": "structure_v1_eth_concurrent_reproducibility",
            "window_start": FORWARD_LOCKBOX_START,
            "window_end": "2026-08-04",
            "purpose": "reproduce_lockbox_hedge3",
            "arms": "hedge×3 vs single + walk-forward outer",
            "n_arms": None,
            "notes": "Outer-fold hedge×3 is quotable; lockbox PF optimism is not",
        },
        {
            "experiment_id": "structure_v1_eth_switch_tp_ablation_001",
            "window_start": FORWARD_LOCKBOX_START,
            "window_end": "2026-08-04",
            "purpose": "multi_arm_lockbox_grid",
            "arms": "150 arms switch_book × addon_tp × hold × K × clarity + controls",
            "n_arms": 150,
            "notes": "Plain TP schedule ablation; keep live eth_multitrade_v1_1",
        },
        {
            "experiment_id": "eth_multitrade_v1_1_live_freeze",
            "window_start": FORWARD_LOCKBOX_START,
            "window_end": "2026-08-04",
            "purpose": "lock_arm_for_live_micro",
            "arms": LOCKED_MULTITRADE_ARM,
            "n_arms": 1,
            "notes": (
                f"Locked micro-live arm. Clean multitrade *parameter* claims only on "
                f">={POST_MULTITRADE_FREEZE_START} or outer-fold settle—not this peek."
            ),
            "evidence_class": "MICRO_LIVE_AUTHORIZED_ARM_LOCKED",
        },
    ]
    n = 0
    for s in seeds:
        append_peek(path=log_path, **s)
        n += 1
    try:
        rel = str(log_path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        rel = str(log_path)
    meta = {
        "seeded_utc": _utc_now(),
        "post_multitrade_freeze_start": POST_MULTITRADE_FREEZE_START,
        "forward_lockbox_start": FORWARD_LOCKBOX_START,
        "locked_arm": LOCKED_MULTITRADE_ARM,
        "prereg": "configs/preregister/structure_v1_eth_multitrade_v1_1_post_freeze_001.yaml",
        "relative_log": rel,
    }
    (log_path.parent / "peek_log_meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    return n
