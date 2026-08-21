"""Phase 3: multi-head P(event) on surviving confluence events. Skip if none."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

from llm2.confluence.events import LONG_EVENTS, SHORT_EVENTS, build_event_pack  # noqa: E402
from llm2.confluence.train import (  # noqa: E402
    all_heads_ge_pi_star,
    chronological_cut_index,
    fit_one_head,
    split_ohlcv_files,
)
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.pivot.strategy.ev import net_bracket_magnitudes  # noqa: E402
from llm2.pivot.strategy.score_oos import limit_price_side, score_symbol_oos  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

_IMP_SPEC = importlib.util.spec_from_file_location(
    "confluence_imp001", _ROOT / "scripts" / "run_confluence_event_importance_001.py"
)
_imp001 = importlib.util.module_from_spec(_IMP_SPEC)
assert _IMP_SPEC.loader is not None
_IMP_SPEC.loader.exec_module(_imp001)

PREREG = _ROOT / "configs" / "preregister" / "confluence_event_pack_001.yaml"
IMP = ARTIFACTS / "reports" / "confluence" / "event_importance_001_latest.json"
TF = "15m"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _jsonable(x):
    if isinstance(x, dict):
        return {str(k): _jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_jsonable(v) for v in x]
    if isinstance(x, (np.floating, float)):
        v = float(x)
        return v if np.isfinite(v) else None
    if isinstance(x, (np.integer, int)):
        return int(x)
    if isinstance(x, (np.bool_, bool)):
        return bool(x)
    return x


def _load_ohlcv_sqlite(path: Path) -> pd.DataFrame:
    with sqlite3.connect(str(path)) as con:
        df = pd.read_sql("SELECT * FROM ohlcv", con)
    if "ts_ms" in df.columns:
        idx = pd.to_datetime(df["ts_ms"].to_numpy(dtype=np.int64), unit="ms", utc=True)
        df = df.drop(columns=["ts_ms"])
        df.index = idx
    return df


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "confluence"
    out_dir.mkdir(parents=True, exist_ok=True)
    db_dir = ARTIFACTS / "sqlite" / "confluence_event_pack_001"
    db_dir.mkdir(parents=True, exist_ok=True)

    if not IMP.exists():
        raise SystemExit(f"missing importance report {IMP}")
    imp = json.loads(IMP.read_text(encoding="utf-8"))
    survivors = imp.get("survivors") or []
    report = {
        "generation_id": "confluence_event_pack_001_train",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "not_live": True,
        "preregister_sha256": _sha(PREREG),
        "importance_stamp": imp.get("stamp"),
        "survivors_in": survivors,
        "gate": "all_heads_ge_pi_star_same_side",
        "skipped": False,
        "symbols": {},
    }

    if not survivors:
        report["skipped"] = True
        report["reason"] = "no Phase-2 survivors; do not train; do not add indicators"
        path = out_dir / "event_pack_train_001_latest.json"
        path.write_text(json.dumps(_jsonable(report), indent=2), encoding="utf-8")
        (out_dir / "event_pack_train_001_latest.md").write_text(
            "# Confluence pack train 001\n\n**Skipped.** No Phase-2 survivors.\n",
            encoding="utf-8",
        )
        append_ledger("CONFLUENCE_EVENT_PACK_TRAIN_001 skipped no survivors", tier=0)
        print("SKIP train: no survivors", flush=True)
        return 0

    mag = net_bracket_magnitudes(0.01, 0.01)
    pi_star = float(mag.pi_star)
    report["pi_star"] = pi_star
    append_ledger(f"CONFLUENCE_EVENT_PACK_TRAIN_001 start {stamp} n_surv={len(survivors)}", tier=0)

    by_sym: dict[str, list[dict]] = {}
    for row in survivors:
        by_sym.setdefault(row["symbol"], []).append(row)

    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    for symbol, rows in by_sym.items():
        ohlcv = load_ohlcv(symbol, TF)
        ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
        if len(ohlcv) > 120_000:
            ohlcv = ohlcv.iloc[-120_000:].copy()
        train_path = db_dir / f"{symbol}_15m_train.sqlite"
        test_path = db_dir / f"{symbol}_15m_test.sqlite"
        split_ohlcv_files(ohlcv, train_path=train_path, test_path=test_path)
        train_df = _load_ohlcv_sqlite(train_path)
        test_df = _load_ohlcv_sqlite(test_path)
        packs_tr: dict[int, object] = {}
        packs_te: dict[int, object] = {}
        heads: dict[str, dict] = {}
        probs: dict[str, np.ndarray] = {}
        for row in rows:
            eid = str(row["event"])
            h = int(row["horizon"])
            if h not in packs_tr:
                packs_tr[h] = build_event_pack(train_df, horizon=h)
                packs_te[h] = build_event_pack(test_df, horizon=h)
            fitted = fit_one_head(packs_tr[h], packs_te[h], eid)
            heads[eid] = {k: v for k, v in fitted.items() if k != "p_test"}
            if fitted["fitted"]:
                probs[eid] = fitted["p_test"]
            print(
                f"  {symbol} {eid} H={h} fitted={fitted['fitted']} ece={fitted.get('ece_inner')}",
                flush=True,
            )

        n_te = len(test_df)
        long_ids = [e for e in probs if e in LONG_EVENTS]
        short_ids = [e for e in probs if e in SHORT_EVENTS]
        fade_ids = [e for e in probs if e not in LONG_EVENTS and e not in SHORT_EVENTS]
        long_probs = {e: probs[e] for e in long_ids + fade_ids}
        short_probs = {e: probs[e] for e in short_ids + fade_ids}
        gate_long = (
            all_heads_ge_pi_star(long_probs, pi_star=pi_star, n=n_te)
            if long_probs
            else np.zeros(n_te, dtype=bool)
        )
        gate_short = (
            all_heads_ge_pi_star(short_probs, pi_star=pi_star, n=n_te)
            if short_probs
            else np.zeros(n_te, dtype=bool)
        )

        print(f"  {symbol} score_oos control on test window", flush=True)
        level_mode = "q50" if symbol == "ETHUSDT" else "ret"
        work = 5 if symbol == "SOLUSDT" else 4
        sc = score_symbol_oos(
            symbol,
            timeframe=TF,
            horizon_bars=4,
            feature_pack="level_vsa",
            max_rows=120_000,
            level_mode=level_mode,
            predict_next=False,
        )
        test_start = int(index_to_ms(test_df.index)[0])
        in_test = sc.ts_ms >= test_start
        ctrl_mask, level_override = _imp001._control_mask(symbol, sc)
        ctrl_test = ctrl_mask & in_test
        if level_override is not None:
            old = sc.level_ret
            sc.level_ret = level_override
            _, is_s, lim = limit_price_side(sc, ctrl_test)
            sc.level_ret = old
        else:
            _, is_s, lim = limit_price_side(sc, ctrl_test)
        ctrl = _imp001._run_limit(
            symbol, sc, ctrl_test, is_s, lim, tag=f"{symbol}_control_test", work=work
        )

        def _map_test_gate(gate_te: np.ndarray, want_short: bool) -> np.ndarray:
            bar_ts = index_to_ms(test_df.index)
            pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
            out = np.zeros(len(sc.ts_ms), dtype=bool)
            for j, t in enumerate(sc.ts_ms):
                i = pos.get(int(t))
                if i is None:
                    continue
                if gate_te[i]:
                    out[j] = True
            pivot_short = sc.p_high >= 0.5
            return out & in_test & ctrl_mask & (pivot_short == want_short)

        arms = {"control_test": ctrl}
        for name, gte, want_short in (
            ("long_pack_and_ctrl", gate_long, False),
            ("short_pack_and_ctrl", gate_short, True),
        ):
            m = _map_test_gate(gte, want_short)
            if level_override is not None:
                old = sc.level_ret
                sc.level_ret = level_override
                _, is_s, lim = limit_price_side(sc, m)
                sc.level_ret = old
            else:
                _, is_s, lim = limit_price_side(sc, m)
            arms[name] = _imp001._run_limit(
                symbol, sc, m, is_s, lim, tag=f"{symbol}_{name}", work=work
            )
            print(f"  BT {name} {arms[name].get('status')} n={arms[name].get('n_trades')}", flush=True)

        report["symbols"][symbol] = {
            "train_sqlite": str(train_path),
            "test_sqlite": str(test_path),
            "n_train_bars": int(len(train_df)),
            "n_test_bars": int(len(test_df)),
            "events": sorted({r["event"] for r in rows}),
            "horizons": {r["event"]: r["horizon"] for r in rows},
            "heads": heads,
            "n_test_gated_long_pack": int(gate_long.sum()),
            "n_test_gated_short_pack": int(gate_short.sum()),
            "cut_index": chronological_cut_index(len(ohlcv)),
            "arms": arms,
        }

    payload = json.dumps(_jsonable(report), indent=2)
    latest = out_dir / "event_pack_train_001_latest.json"
    latest.write_text(payload, encoding="utf-8")
    (out_dir / f"event_pack_train_001_{stamp}.json").write_text(payload, encoding="utf-8")
    md = [
        "# Confluence pack train 001",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"Gate: same-side heads ≥ π* = {pi_star:.4f} (1%/1% bracket). Test window only.",
        "",
        "| Symbol | Arm | n | PF | intent-exp | ebr |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for symbol, blk in report["symbols"].items():
        for name, arm in blk["arms"].items():
            md.append(
                f"| {symbol} | `{name}` | {arm.get('n_trades')} | {arm.get('profit_factor')} | "
                f"{arm.get('expectancy_intent_all')} | {arm.get('entry_bar_exit_rate')} |"
            )
    (out_dir / "event_pack_train_001_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    append_ledger(f"CONFLUENCE_EVENT_PACK_TRAIN_001 done path={latest}", tier=0)
    print(f"WROTE {latest}", flush=True)
    _ = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
