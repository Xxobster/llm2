"""Generation C: nested outer-OOS settle of diagonal S/R hunt 001 survivors.

RESEARCH_ONLY. Rule-event arms only (no model refit). Pre-lockbox folds V2.
Resumes from artifacts/sqlite/diagonal_sr_nested_settle_001/settle.sqlite.
"""

from __future__ import annotations

import hashlib
import json
import os
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

from llm2.confluence.sim_arms import (  # noqa: E402
    arm_done,
    jsonable,
    load_arms,
    open_checkpoint,
    run_limit_arm,
    run_market_arm,
    save_arm,
)
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.diagonal_sr.bar_series import make_bar_series  # noqa: E402
from llm2.diagonal_sr.events import MARKET_ENTRY_EVENTS, build_event_pack  # noqa: E402
from llm2.diagonal_sr.mtf import geometry_context_map  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import OUTER_FOLD_RANGES, build_outer_folds, index_to_ms  # noqa: E402

PREREG = _ROOT / "configs" / "preregister" / "diagonal_sr_nested_settle_001.yaml"
OUT = ARTIFACTS / "reports" / "diagonal_sr"
DB_DIR = ARTIFACTS / "sqlite" / "diagonal_sr_nested_settle_001"
MAX_ROWS = {"15m": 120_000, "1h": 40_000, "4h": 20_000, "1d": 8_000}
WORK = {"15m": 4, "1h": 3, "4h": 2}
MAX_HOLD = {"15m": 6, "1h": 8, "4h": 6}
MAX_TPM = {"15m": 40.0, "1h": 20.0, "4h": 12.0}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _lock_ms() -> int:
    return int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)


def _load_pre_lock(symbol: str, tf: str, max_rows: int):
    ohlcv = load_ohlcv(symbol, tf)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < _lock_ms()].copy()
    if len(ohlcv) > max_rows:
        ohlcv = ohlcv.iloc[-max_rows:].copy()
    return ohlcv


def _side(event: str, n: int) -> np.ndarray:
    from llm2.diagonal_sr.events import LONG_EVENTS, SHORT_EVENTS

    if event in LONG_EVENTS:
        return np.ones(n, dtype=float)
    if event in SHORT_EVENTS:
        return np.full(n, -1.0)
    return np.zeros(n, dtype=float)


def _limit_atr(sc, mask: np.ndarray, is_short: np.ndarray) -> np.ndarray:
    idx = np.flatnonzero(mask)
    c = sc.close[idx]
    atr = sc.atr_frac[idx]
    move = np.clip(np.where(np.isfinite(atr), atr, 0.005), 0.0015, 0.03)
    return np.where(is_short, c * (1.0 + move), c * (1.0 - move))


def _fmt(v) -> str:
    try:
        x = float(v)
    except (TypeError, ValueError):
        return ""
    if not np.isfinite(x):
        return ""
    return f"{x:.4f}"


class _Ctx:
    def __init__(self, symbol: str, tf: str, generation: str):
        self.symbol = symbol
        self.tf = tf
        self.generation = generation
        self.ohlcv = _load_pre_lock(symbol, tf, MAX_ROWS[tf])
        self.sc = make_bar_series(symbol, tf, self.ohlcv)
        self.htf = {}
        for htf in geometry_context_map(tf):
            try:
                self.htf[htf] = _load_pre_lock(symbol, htf, MAX_ROWS.get(htf, 20_000))
            except Exception as exc:  # noqa: BLE001
                print(f"  warn HTF {htf}: {exc}", flush=True)
        print(f"  event pack {symbol} {tf} gen={generation}", flush=True)
        self.pack = build_event_pack(
            self.ohlcv,
            horizon=4,
            generation=generation,
            htf_ohlcv_by_tf=self.htf,
            decision_tf=tf,
        )
        self.folds = build_outer_folds(self.sc.ts_ms, purge_bars=24, embargo_bars=24)
        self.oos_union = np.zeros(len(self.sc.ts_ms), dtype=bool)
        for f in self.folds:
            self.oos_union |= (self.sc.ts_ms >= f.oos_start_ms) & (self.sc.ts_ms < f.oos_end_ms)


def _run_mask(ctx: _Ctx, spec: dict, mask: np.ndarray, tag: str) -> dict:
    event = spec["event"]
    tp, sl = float(spec["tp"]), float(spec["sl"])
    occ = ctx.pack.occurrence[event].to_numpy(dtype=float)
    fire = occ >= 0.5
    side = _side(event, len(ctx.ohlcv))
    # pack aligned to ohlcv == sc
    mask = mask & fire & (side != 0)
    is_short = (side < 0)[np.flatnonzero(mask)]
    market = event in MARKET_ENTRY_EVENTS
    if market:
        out = run_market_arm(
            spec["symbol"],
            ctx.sc,
            mask,
            is_short,
            tag=tag,
            max_hold=MAX_HOLD[spec["timeframe"]],
            tp=tp,
            sl=sl,
        )
    else:
        lim = _limit_atr(ctx.sc, mask, is_short)
        out = run_limit_arm(
            spec["symbol"],
            ctx.sc,
            mask,
            is_short,
            lim,
            tag=tag,
            work=WORK[spec["timeframe"]],
            max_hold=MAX_HOLD[spec["timeframe"]],
            tp=tp,
            sl=sl,
        )
    return out


def _survivors(cfg: dict) -> list[dict]:
    return list(cfg["survivors"])


def _arm_id(spec: dict, kind: str, fold: int | None = None) -> str:
    base = (
        f"{spec['symbol']}|{spec['timeframe']}|{spec['generation']}|"
        f"{spec['event']}|tp{spec['tp']}|sl{spec['sl']}|{kind}"
    )
    if fold is not None:
        return f"{base}|fold{fold}"
    return base


def _write_leaderboard(con, stamp: str, extra: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    stitched = [r for r in rows if r.get("kind") == "stitched"]
    stitched.sort(key=lambda r: -(r.get("profit_factor") or -1e9) if r.get("status") == "RAN" else 1)
    latest = {
        "generation_id": "diagonal_sr_nested_settle_001",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "not_live": True,
        "n_rows": len(rows),
        "n_stitched": len(stitched),
        "extra": extra,
        "stitched": stitched,
        "all": rows,
    }
    (OUT / "nested_settle_001_latest.json").write_text(
        json.dumps(jsonable(latest), indent=2), encoding="utf-8"
    )
    md = [
        "# Diagonal S/R nested settle 001",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        "Stitched outer out-of-sample before lockbox. Not live.",
        "",
        "| Symbol | TF | Event | TP | SL | n | /mo | PF | WR | Sharpe | HAC | ebr | folds+ | status |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in stitched:
        md.append(
            "| {sym} | {tf} | `{ev}` | {tp} | {sl} | {n} | {tpm} | {pf} | {wr} | {sh} | {hac} | {ebr} | {fp} | {st} |".format(
                sym=r.get("symbol"),
                tf=r.get("timeframe"),
                ev=r.get("event"),
                tp=r.get("tp"),
                sl=r.get("sl"),
                n=r.get("n_trades"),
                tpm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")),
                wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")),
                hac=_fmt(r.get("sharpe_hac_annualised")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                fp=r.get("n_folds_positive"),
                st=r.get("status"),
            )
        )
    (OUT / "nested_settle_001_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    prereg_sha = _sha(PREREG)
    text = PREREG.read_text(encoding="utf-8")
    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(text.rstrip() + f"\n\npreregister_sha256_at_run: {prereg_sha}\n", encoding="utf-8")
        prereg_sha = _sha(PREREG)
    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    DB_DIR.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB_DIR / "settle.sqlite")
    append_ledger(f"DIAGONAL_SR_NESTED_SETTLE_001 start {stamp}", tier=0)
    print(f"preregister_sha256={prereg_sha}", flush=True)

    survivors = _survivors(cfg)
    ctxs: dict[tuple[str, str, str], _Ctx] = {}
    extra = {"preregister_sha256": prereg_sha, "fold_ranges": list(OUTER_FOLD_RANGES)}
    n_planned = 0
    for spec in survivors:
        key = (spec["symbol"], spec["timeframe"], spec["generation"])
        if key not in ctxs:
            print(f"=== context {key} ===", flush=True)
            ctxs[key] = _Ctx(*key)
        ctx = ctxs[key]
        n_planned += 1 + len(ctx.folds)

        # Per-fold
        fold_rows = []
        for f in ctx.folds:
            aid = _arm_id(spec, "fold", f.fold_index)
            n_planned += 0
            if arm_done(con, aid):
                continue
            mask = (ctx.sc.ts_ms >= f.oos_start_ms) & (ctx.sc.ts_ms < f.oos_end_ms)
            print(f"  fold{f.fold_index} {aid}", flush=True)
            try:
                payload = _run_mask(ctx, spec, mask, aid)
            except Exception as exc:  # noqa: BLE001
                payload = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
                print(f"  ERROR {exc}", flush=True)
            payload.update(
                {
                    "symbol": spec["symbol"],
                    "timeframe": spec["timeframe"],
                    "generation": spec["generation"],
                    "event": spec["event"],
                    "tp": spec["tp"],
                    "sl": spec["sl"],
                    "kind": "fold",
                    "fold_index": f.fold_index,
                    "arm_id": aid,
                }
            )
            save_arm(con, aid, spec, payload)
            print(
                f"    {payload.get('status')} n={payload.get('n_trades')} PF={payload.get('profit_factor')}",
                flush=True,
            )
            fold_rows.append(payload)

        # Stitched union of outer OOS
        aid = _arm_id(spec, "stitched")
        if not arm_done(con, aid):
            print(f"  stitched {aid}", flush=True)
            try:
                payload = _run_mask(ctx, spec, ctx.oos_union, aid)
            except Exception as exc:  # noqa: BLE001
                payload = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
                print(f"  ERROR {exc}", flush=True)
            # Fold diagnostics from DB (including just-saved)
            pos = 0
            elig = 0
            prefix = (
                f"{spec['symbol']}|{spec['timeframe']}|{spec['generation']}|"
                f"{spec['event']}|tp{spec['tp']}|sl{spec['sl']}|fold"
            )
            for arm_id, raw in con.execute("SELECT arm_id, payload FROM arms"):
                if not str(arm_id).startswith(prefix):
                    continue
                fr = json.loads(raw)
                if fr.get("status") != "RAN":
                    continue
                elig += 1
                if float(fr.get("net_pnl") or 0) > 0 and float(fr.get("profit_factor") or 0) > 1:
                    pos += 1
            payload.update(
                {
                    "symbol": spec["symbol"],
                    "timeframe": spec["timeframe"],
                    "generation": spec["generation"],
                    "event": spec["event"],
                    "tp": spec["tp"],
                    "sl": spec["sl"],
                    "kind": "stitched",
                    "n_folds_ran": elig,
                    "n_folds_positive": pos,
                    "arm_id": aid,
                }
            )
            save_arm(con, aid, spec, payload)
            print(
                f"    STITCH {payload.get('status')} n={payload.get('n_trades')} "
                f"PF={payload.get('profit_factor')} folds+={pos}/{elig}",
                flush=True,
            )
            _write_leaderboard(con, stamp, extra)

    _write_leaderboard(con, stamp, extra)
    append_ledger("DIAGONAL_SR_NESTED_SETTLE_001 done", tier=0)
    print(f"WROTE {OUT / 'nested_settle_001_latest.md'} planned_approx={n_planned}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
