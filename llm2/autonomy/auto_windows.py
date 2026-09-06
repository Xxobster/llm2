"""Auto-extend unused public-formula windows so the hunt queue never idles.

RESEARCH_ONLY. Frozen before profit-factor ranking. Not a live deploy.
Does not scrape TradingView. Honors artifacts/autonomy/STOP (caller).
"""

from __future__ import annotations

import json
import os
import re
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import (
    any_in_next,
    cross_down,
    cross_up,
    ema,
    sma,
    window_last,
    wma,
)

_ROOT = Path(__file__).resolve().parents[2]
PACKS_PATH = _ROOT / "llm2" / "autonomy" / "packs.py"
QUEUE_YAML = _ROOT / "configs" / "autonomy" / "research_loop_v1.yaml"
AUTO_JSON = _ROOT / "configs" / "autonomy" / "auto_public_windows.json"
PREREG_DIR = _ROOT / "configs" / "preregister"
STATE_PATH = _ROOT / "artifacts" / "autonomy" / "loop_state.json"
LOCK_PATH = _ROOT / "artifacts" / "autonomy" / "auto_window_freeze.lock"

# Same 8-slot rotation as the manual freeze batches (short SMA / mid EMA / short
# return / WMA / prior-HL / long SMA / long EMA / long return).
SLOTS: tuple[dict[str, Any], ...] = (
    {"kind": "sma", "step": 6, "lo": 600, "hi": 900},
    {"kind": "ema", "step": 10, "lo": 900, "hi": 1600},
    {"kind": "ret", "step": 2, "lo": 180, "hi": 400},
    {"kind": "wma", "step": 5, "lo": 400, "hi": 800},
    {"kind": "xh", "step": 5, "lo": 400, "hi": 800},
    {"kind": "sma", "step": 20, "lo": 1800, "hi": 100_000},
    {"kind": "ema", "step": 20, "lo": 1600, "hi": 100_000},
    {"kind": "ret", "step": 8, "lo": 700, "hi": 100_000},
)

DEFAULT_MIN_REMAINING = 12
DEFAULT_BATCH = 8


@dataclass(frozen=True)
class WindowSpec:
    id: str
    kind: str
    period: int
    title: str
    events: tuple[str, ...]
    hypothesis: str


def events_for(kind: str, period: int) -> tuple[str, ...]:
    n = int(period)
    if kind == "sma":
        return (
            f"sma{n}_above_at_h",
            f"sma{n}_below_at_h",
            f"sma{n}_cross_up",
            f"sma{n}_cross_down",
        )
    if kind == "ema":
        return (
            f"ema{n}_above_at_h",
            f"ema{n}_below_at_h",
            f"ema{n}_cross_up",
            f"ema{n}_cross_down",
        )
    if kind == "ret":
        return (
            f"ret{n}_pos_at_h",
            f"ret{n}_neg_at_h",
            f"ret{n}_cross_up_0",
            f"ret{n}_cross_down_0",
        )
    if kind == "wma":
        return (
            f"wma{n}_above_at_h",
            f"wma{n}_below_at_h",
            f"wma{n}_cross_up",
            f"wma{n}_cross_down",
        )
    if kind == "xh":
        return (
            f"xh{n}_at_h",
            f"xl{n}_at_h",
            f"xh{n}_cross_up",
            f"xl{n}_cross_down",
        )
    raise ValueError(f"unknown window kind {kind!r}")


def title_for(kind: str, period: int) -> str:
    n = int(period)
    if kind == "sma":
        return f"SMA{n}_distance"
    if kind == "ema":
        return f"EMA{n}_distance"
    if kind == "ret":
        return f"Return{n}_bar"
    if kind == "wma":
        return f"WMA{n}_distance"
    if kind == "xh":
        return f"Prior{n}_high_low"
    raise ValueError(kind)


def hypothesis_for(kind: str, period: int) -> str:
    n = int(period)
    if kind == "sma":
        head = (
            f"Distance and crosses of close versus the {n}-bar simple moving average at t+H, "
            "used as one-head filters, can beat the"
        )
    elif kind == "ema":
        head = (
            f"Distance and crosses of close versus the {n}-bar exponential moving average at t+H, "
            "used as one-head filters, can beat the"
        )
    elif kind == "ret":
        head = (
            f"Sign and zero-crosses of the {n}-bar close-to-close return at t+H, "
            "used as one-head filters, can beat the"
        )
    elif kind == "wma":
        head = (
            f"Distance and crosses of close versus the {n}-bar weighted moving average at t+H, "
            "used as one-head filters, can beat the"
        )
    elif kind == "xh":
        head = (
            f"Distance and crosses of close versus the prior {n}-bar high and low at t+H, "
            "used as one-head filters, can beat the"
        )
    else:
        raise ValueError(kind)
    return (
        head
        + " 15-minute Limit 1%/1% pivot control under frozen entry-bar and trades-per-month caps."
    )


def load_auto_payload(path: Path = AUTO_JSON) -> dict[str, Any]:
    if not path.is_file():
        return {"windows": []}
    return json.loads(path.read_text(encoding="utf-8")) or {"windows": []}


def auto_windows(path: Path = AUTO_JSON) -> list[WindowSpec]:
    out: list[WindowSpec] = []
    for raw in load_auto_payload(path).get("windows") or []:
        kind = str(raw["kind"])
        period = int(raw["period"])
        gid = str(raw["id"])
        out.append(
            WindowSpec(
                id=gid,
                kind=kind,
                period=period,
                title=str(raw.get("title") or title_for(kind, period)),
                events=tuple(raw.get("events") or events_for(kind, period)),
                hypothesis=str(raw.get("hypothesis") or hypothesis_for(kind, period)),
            )
        )
    return out


def auto_gen_events(path: Path = AUTO_JSON) -> dict[str, tuple[str, ...]]:
    return {w.id: w.events for w in auto_windows(path)}


def used_periods_from_text(text: str) -> dict[str, set[int]]:
    return {
        "sma": {int(x) for x in re.findall(r"sma(\d+)_", text)},
        "ema": {int(x) for x in re.findall(r"ema(\d+)_", text)},
        "ret": {int(x) for x in re.findall(r"ret(\d+)_", text)},
        "wma": {int(x) for x in re.findall(r"wma(\d+)_", text)},
        "xh": {int(x) for x in re.findall(r"xh(\d+)_", text)},
        "xl": {int(x) for x in re.findall(r"xl(\d+)_", text)},
    }


def used_periods(*, packs_text: str, windows: Iterable[WindowSpec]) -> dict[str, set[int]]:
    used = used_periods_from_text(packs_text)
    for w in windows:
        used.setdefault(w.kind, set()).add(int(w.period))
        if w.kind == "xh":
            used.setdefault("xl", set()).add(int(w.period))
    return used


def next_free(used: set[int], start: int, step: int) -> int:
    x = int(start)
    while x in used or x <= 0:
        x += int(step)
    return x


def next_in_band(used: set[int], *, step: int, lo: int, hi: int) -> int:
    in_band = [x for x in used if lo <= x < hi]
    start = (max(in_band) + step) if in_band else lo
    if start < hi:
        cand = next_free(used, start, step)
        if cand < hi:
            return cand
    for x in range(lo, hi):
        if x not in used:
            return x
    return next_free(used, hi, step)


def all_gen_ids(*, packs_text: str, windows: Iterable[WindowSpec]) -> set[str]:
    ids = set(re.findall(r'"(\d+)": GEN_', packs_text))
    ids.update(w.id for w in windows)
    return ids


def next_gen_id(ids: set[str]) -> str:
    nums = [int(x) for x in ids if x.isdigit()]
    if not nums:
        raise ValueError("no existing generation ids")
    return str(max(nums) + 1)


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name, dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


def save_auto_payload(payload: dict[str, Any], path: Path = AUTO_JSON) -> None:
    _atomic_write(path, json.dumps(payload, indent=2) + "\n")


def preregister_text(spec: WindowSpec) -> str:
    ev = ", ".join(spec.events)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"""# Autonomy gen {spec.id} — {spec.title}
# RESEARCH_ONLY. Frozen before profit-factor ranking.
generation_id: autonomy_gen_{spec.id}_public_indicators
status: OPEN
readiness_max: RESEARCH_ONLY
frozen_at_utc: "{ts}"
rank_window: chronological_test_30pct_pre_lockbox
entry_bar_exit_rate_cap: 0.35
trades_per_month_min: 4
trades_per_month_max: 40
failure_is_success: true
lockbox: do_not_rank_on_or_after_2026-05-01
hypothesis: >
  {spec.hypothesis}
events: [{ev}]
brackets: [{{tp: 0.01, sl: 0.01}}]
horizons_bars: [4, 8]
modes: [control, one_head_filter_pi_star]
do_not: [scrape TradingView / paste Pine, peep lockbox for ranking, deploy]
"""


def queue_yaml_block(spec: WindowSpec) -> str:
    return (
        f'  - id: "{spec.id}"\n'
        f"    title: {spec.title}\n"
        f"    preregister: configs/preregister/autonomy_gen_{spec.id}_public_indicators.yaml\n"
        f"    script: scripts/run_autonomy_public_indicator_hunt.py\n"
        f'    args: ["--gen", "{spec.id}"]\n'
        f"    report_json: artifacts/reports/autonomy/gen_{spec.id}_latest.json\n"
        f"    planned_arms: 27\n"
    )


def append_queue_yaml(specs: list[WindowSpec], queue_path: Path = QUEUE_YAML) -> None:
    if not specs:
        return
    text = queue_path.read_text(encoding="utf-8").rstrip() + "\n"
    for spec in specs:
        marker = f'  - id: "{spec.id}"\n'
        if marker in text:
            continue
        text += queue_yaml_block(spec)
    _atomic_write(queue_path, text)


def write_preregisters(specs: list[WindowSpec], prereg_dir: Path = PREREG_DIR) -> None:
    prereg_dir.mkdir(parents=True, exist_ok=True)
    for spec in specs:
        path = prereg_dir / f"autonomy_gen_{spec.id}_public_indicators.yaml"
        if path.exists():
            continue
        path.write_text(preregister_text(spec), encoding="utf-8")


def discovered_gen_ids(*, queue_path: Path = QUEUE_YAML, prereg_dir: Path = PREREG_DIR) -> list[str]:
    ids: set[str] = set()
    if queue_path.is_file():
        ids.update(re.findall(r'^\s*-\s*id:\s*"?(\d+)"?', queue_path.read_text(encoding="utf-8"), re.M))
    if prereg_dir.is_dir():
        for path in prereg_dir.glob("autonomy_gen_*_public_indicators.yaml"):
            parts = path.stem.split("_")
            if len(parts) >= 3:
                ids.add(parts[2])
    return sorted(ids, key=lambda x: (len(x), x))


def completed_ids(state_path: Path = STATE_PATH) -> set[str]:
    if not state_path.is_file():
        return set()
    data = json.loads(state_path.read_text(encoding="utf-8"))
    return {str(x) for x in (data.get("completed") or [])}


def remaining_count(
    *,
    queue_path: Path = QUEUE_YAML,
    prereg_dir: Path = PREREG_DIR,
    state_path: Path = STATE_PATH,
) -> int:
    done = completed_ids(state_path)
    return sum(1 for gid in discovered_gen_ids(queue_path=queue_path, prereg_dir=prereg_dir) if gid not in done)


def plan_batch(
    *,
    n: int = DEFAULT_BATCH,
    packs_text: str,
    existing: list[WindowSpec],
) -> list[WindowSpec]:
    used = used_periods(packs_text=packs_text, windows=existing)
    ids = all_gen_ids(packs_text=packs_text, windows=existing)
    next_id = int(next_gen_id(ids))
    planned: list[WindowSpec] = []
    for i, slot in enumerate(SLOTS):
        if i >= n:
            break
        kind = str(slot["kind"])
        period = next_in_band(
            used.get(kind, set()),
            step=int(slot["step"]),
            lo=int(slot["lo"]),
            hi=int(slot["hi"]),
        )
        used.setdefault(kind, set()).add(period)
        spec = WindowSpec(
            id=str(next_id + i),
            kind=kind,
            period=period,
            title=title_for(kind, period),
            events=events_for(kind, period),
            hypothesis=hypothesis_for(kind, period),
        )
        planned.append(spec)
    return planned


def _acquire_lock(lock_path: Path = LOCK_PATH) -> int | None:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        try:
            old = int(lock_path.read_text(encoding="utf-8").strip() or "0")
        except ValueError:
            old = 0
        if old > 0:
            try:
                os.kill(old, 0)
                return None
            except OSError:
                pass
        try:
            lock_path.unlink()
        except OSError:
            return None
        try:
            fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            return None
    os.write(fd, str(os.getpid()).encode("ascii"))
    os.close(fd)
    return os.getpid()


def _release_lock(lock_path: Path = LOCK_PATH) -> None:
    try:
        if lock_path.is_file() and lock_path.read_text(encoding="utf-8").strip() == str(os.getpid()):
            lock_path.unlink()
    except OSError:
        pass


def freeze_batch(
    *,
    n: int = DEFAULT_BATCH,
    root: Path = _ROOT,
) -> list[WindowSpec]:
    packs = root / "llm2" / "autonomy" / "packs.py"
    auto_path = root / "configs" / "autonomy" / "auto_public_windows.json"
    queue_path = root / "configs" / "autonomy" / "research_loop_v1.yaml"
    prereg_dir = root / "configs" / "preregister"
    payload = load_auto_payload(auto_path)
    existing = auto_windows(auto_path)
    packs_text = packs.read_text(encoding="utf-8")
    planned = plan_batch(n=n, packs_text=packs_text, existing=existing)
    if not planned:
        return []
    windows_raw = list(payload.get("windows") or [])
    for spec in planned:
        windows_raw.append(
            {
                "id": spec.id,
                "kind": spec.kind,
                "period": spec.period,
                "title": spec.title,
                "events": list(spec.events),
                "hypothesis": spec.hypothesis,
            }
        )
    payload["windows"] = windows_raw
    payload["updated_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    save_auto_payload(payload, auto_path)
    write_preregisters(planned, prereg_dir)
    append_queue_yaml(planned, queue_path)
    return planned


def ensure_queue_depth(
    *,
    min_remaining: int = DEFAULT_MIN_REMAINING,
    batch: int = DEFAULT_BATCH,
    root: Path = _ROOT,
) -> list[str]:
    """Freeze batches of unused public windows until remaining >= min_remaining."""
    lock = root / "artifacts" / "autonomy" / "auto_window_freeze.lock"
    if _acquire_lock(lock) is None:
        return []
    added: list[str] = []
    try:
        queue_path = root / "configs" / "autonomy" / "research_loop_v1.yaml"
        prereg_dir = root / "configs" / "preregister"
        state_path = root / "artifacts" / "autonomy" / "loop_state.json"
        while remaining_count(queue_path=queue_path, prereg_dir=prereg_dir, state_path=state_path) < min_remaining:
            specs = freeze_batch(n=batch, root=root)
            if not specs:
                break
            added.extend(s.id for s in specs)
    finally:
        _release_lock(lock)
    return added


def emit_auto_windows_for_ids(
    *,
    close: np.ndarray,
    high: np.ndarray,
    low: np.ndarray,
    n: int,
    horizon: int,
    occ: dict[str, np.ndarray],
    bits: dict[str, np.ndarray],
    sides: dict[str, np.ndarray],
    ids: Iterable[str],
    windows: Iterable[WindowSpec] | None = None,
) -> None:
    """Fill occ/bits/sides for auto-frozen windows that this generation actually uses."""
    wanted = set(ids)
    specs = list(windows) if windows is not None else auto_windows()
    for spec in specs:
        if not wanted.intersection(spec.events):
            continue
        _emit_one(
            spec,
            close=close,
            high=high,
            low=low,
            n=n,
            horizon=horizon,
            occ=occ,
            bits=bits,
            sides=sides,
        )


def _emit_one(
    spec: WindowSpec,
    *,
    close: np.ndarray,
    high: np.ndarray,
    low: np.ndarray,
    n: int,
    horizon: int,
    occ: dict[str, np.ndarray],
    bits: dict[str, np.ndarray],
    sides: dict[str, np.ndarray],
) -> None:
    period = int(spec.period)
    kind = spec.kind
    if kind in {"sma", "ema", "wma"}:
        if kind == "sma":
            ma = sma(close, period)
        elif kind == "ema":
            ma = ema(close, period)
        else:
            ma = wma(close, period) if n >= period else np.full(n, np.nan)
        with np.errstate(divide="ignore", invalid="ignore"):
            dist = (close - ma) / np.where(np.abs(close) > 1e-12, close, np.nan)
        dist_h = window_last(dist, horizon)
        above, below, cu, cd = spec.events
        occ[above] = dist > 0.0
        occ[below] = dist < 0.0
        bits[above] = np.isfinite(dist_h) & (dist_h > 0.0)
        bits[below] = np.isfinite(dist_h) & (dist_h < 0.0)
        sides[above] = np.where(bits[above], 1.0, 0.0)
        sides[below] = np.where(bits[below], -1.0, 0.0)
        occ[cu] = cross_up(dist, 0.0)
        occ[cd] = cross_down(dist, 0.0)
        bits[cu] = any_in_next(occ[cu], horizon)
        bits[cd] = any_in_next(occ[cd], horizon)
        sides[cu] = np.where(bits[cu], 1.0, 0.0)
        sides[cd] = np.where(bits[cd], -1.0, 0.0)
        return
    if kind == "ret":
        series = np.full(n, np.nan)
        if n > period:
            series[period:] = close[period:] / np.where(close[:-period] > 0, close[:-period], np.nan) - 1.0
        series_h = window_last(series, horizon)
        pos, neg, cu, cd = spec.events
        occ[pos] = series > 0.0
        occ[neg] = series < 0.0
        bits[pos] = np.isfinite(series_h) & (series_h > 0.0)
        bits[neg] = np.isfinite(series_h) & (series_h < 0.0)
        sides[pos] = np.where(bits[pos], 1.0, 0.0)
        sides[neg] = np.where(bits[neg], -1.0, 0.0)
        occ[cu] = cross_up(series, 0.0)
        occ[cd] = cross_down(series, 0.0)
        bits[cu] = any_in_next(occ[cu], horizon)
        bits[cd] = any_in_next(occ[cd], horizon)
        sides[cu] = np.where(bits[cu], 1.0, 0.0)
        sides[cd] = np.where(bits[cd], -1.0, 0.0)
        return
    if kind == "xh":
        mp = max(1, period // 2)
        prior_hh = pd.Series(high).shift(1).rolling(period, min_periods=mp).max().to_numpy()
        prior_ll = pd.Series(low).shift(1).rolling(period, min_periods=mp).min().to_numpy()
        xh_dist = close - prior_hh
        xl_dist = close - prior_ll
        xh_h = window_last(xh_dist, horizon)
        xl_h = window_last(xl_dist, horizon)
        xh_at, xl_at, xh_cu, xl_cd = spec.events
        occ[xh_at] = np.isfinite(xh_dist) & (xh_dist > 0.0)
        occ[xl_at] = np.isfinite(xl_dist) & (xl_dist < 0.0)
        bits[xh_at] = np.isfinite(xh_h) & (xh_h > 0.0)
        bits[xl_at] = np.isfinite(xl_h) & (xl_h < 0.0)
        sides[xh_at] = np.where(bits[xh_at], 1.0, 0.0)
        sides[xl_at] = np.where(bits[xl_at], -1.0, 0.0)
        occ[xh_cu] = cross_up(xh_dist, 0.0)
        occ[xl_cd] = cross_down(xl_dist, 0.0)
        bits[xh_cu] = any_in_next(occ[xh_cu], horizon)
        bits[xl_cd] = any_in_next(occ[xl_cd], horizon)
        sides[xh_cu] = np.where(bits[xh_cu], 1.0, 0.0)
        sides[xl_cd] = np.where(bits[xl_cd], -1.0, 0.0)
        return
    raise ValueError(spec.kind)
