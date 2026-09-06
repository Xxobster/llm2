"""Public-indicator filter hunt (autonomy gens 004+).

Usage:
  python -u scripts/run_autonomy_public_indicator_hunt.py --gen 004

RESEARCH_ONLY. 1%/1% only. Pre-lockbox test window. Checkpointed SQLite.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import pickle
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

from llm2.autonomy.packs import (  # noqa: E402
    EXTRA_FEATURE_COLS,
    GEN_BY_ID,
    build_autonomy_pack,
    build_features_for_guard,
)
from llm2.autonomy.policy import (  # noqa: E402
    ENTRY_BAR_EXIT_CAP,
    MAX_TRADES_PER_MONTH,
    MIN_TRADES_FLAG,
    MIN_TRADES_PER_MONTH,
    is_gate_candidate,
)
from llm2.confluence.sim_arms import (  # noqa: E402
    arm_done,
    jsonable,
    load_arms,
    open_checkpoint,
    run_limit_arm,
    save_arm,
)
from llm2.confluence.train import chronological_cut_index, fit_event_head, split_ohlcv_files  # noqa: E402
from llm2.confluence.train import FEATURE_COLS as BASE_FEATURE_COLS  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.pivot.features.packs import build_feature_frame  # noqa: E402
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

PACK = "level_vsa"
OUT = ARTIFACTS / "reports" / "autonomy"
SYMBOLS_15M = ("ETHUSDT", "SOLUSDT", "BTCUSDT")
WORK_CTRL = {"ETHUSDT": 4, "SOLUSDT": 5, "BTCUSDT": 4}
HORIZONS = (4, 8)
TP_SL = (0.01, 0.01)

GEN_EVENTS = dict(GEN_BY_ID)

FEATURE_COLS = tuple(BASE_FEATURE_COLS) + EXTRA_FEATURE_COLS


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _lock() -> pd.Timestamp:
    return pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")


def _load_pre_lock(symbol: str, tf: str, max_rows: int) -> pd.DataFrame:
    ohlcv = load_ohlcv(symbol, tf)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(_lock().value // 1_000_000)].copy()
    if len(ohlcv) > max_rows:
        ohlcv = ohlcv.iloc[-max_rows:].copy()
    return ohlcv


def _load_ohlcv_sqlite(path: Path) -> pd.DataFrame:
    import sqlite3

    with sqlite3.connect(str(path)) as con:
        df = pd.read_sql("SELECT * FROM ohlcv", con)
    if "ts_ms" in df.columns:
        idx = pd.to_datetime(df["ts_ms"].to_numpy(dtype=np.int64), unit="ms", utc=True)
        df = df.drop(columns=["ts_ms"])
        df.index = idx
    return df


def _leak(symbol: str, tf: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = _load_pre_lock(symbol, tf, 6000)
        require_clean_audit(
            run_leakage_audit(
                ohlcv=ohlcv,
                build_features=build_features_for_guard,
                interval=tf,
                symbol=symbol,
                timeframe=tf,
            )
        )

        def _b(df, **_k):
            return build_feature_frame(df, pack=PACK)

        require_clean_audit(
            run_leakage_audit(
                ohlcv=ohlcv, build_features=_b, interval=tf, symbol=symbol, timeframe=tf
            )
        )
        return {"symbol": symbol, "timeframe": tf, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "timeframe": tf, "status": "FAIL", "error": str(exc)[:400]}


def _score_cached(symbol: str, tf: str, max_rows: int, cache: Path):
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / f"score_{symbol}_{tf}.pkl"
    if path.exists():
        try:
            with path.open("rb") as fh:
                return pickle.load(fh)
        except (pickle.UnpicklingError, EOFError, OSError) as exc:
            print(f"  cache rebuild {path.name} ({exc})", flush=True)
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass
    level_mode = "q50" if symbol == "ETHUSDT" and tf == "15m" else "ret"
    print(f"  score_oos {symbol} {tf} …", flush=True)
    sc = score_symbol_oos(
        symbol,
        timeframe=tf,
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=max_rows,
        level_mode=level_mode,
        predict_next=False,
    )
    tmp = path.with_suffix(".pkl.tmp")
    try:
        with tmp.open("wb") as fh:
            pickle.dump(sc, fh, protocol=4)
        tmp.replace(path)
    except OSError as exc:
        print(f"  cache write skipped ({exc})", flush=True)
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass
    return sc


def _map_to_sc(sc, test_index, values: np.ndarray) -> np.ndarray:
    bar_ts = index_to_ms(test_index)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
    out = np.full(len(sc.ts_ms), np.nan)
    vals = np.asarray(values, dtype=float)
    for j, t in enumerate(sc.ts_ms):
        i = pos.get(int(t))
        if i is not None:
            out[j] = vals[i]
    return out


def _fmt(v) -> str:
    if v is None:
        return ""
    try:
        x = float(v)
    except (TypeError, ValueError):
        return str(v)
    if not np.isfinite(x):
        return ""
    return f"{x:.4f}"


def _fit_head(train_pack, test_pack, event_id: str) -> np.ndarray:
    cols = [c for c in FEATURE_COLS if c in train_pack.features.columns]
    x_tr = train_pack.features[cols].to_numpy(dtype=float)
    y_tr = train_pack.labels[event_id].to_numpy(dtype=float)
    x_te = test_pack.features[cols].to_numpy(dtype=float)
    y_te = test_pack.labels[event_id].to_numpy(dtype=float)
    ok_tr = np.isfinite(y_tr) & np.isfinite(x_tr).all(axis=1)
    ok_te = np.isfinite(y_te) & np.isfinite(x_te).all(axis=1)
    p = np.full(len(test_pack.labels), np.nan)
    if ok_tr.sum() < 200 or len(np.unique(y_tr[ok_tr])) < 2:
        return p
    head = fit_event_head(x_tr[ok_tr], y_tr[ok_tr].astype(np.int32), x_te[ok_te])
    p[ok_te] = head["p_test"]
    return p


def _write_leaderboard(con, stamp: str, gen: str, extra: dict, db_dir: Path) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    rows.sort(key=lambda r: (0 if r.get("status") == "RAN" else 1, -(r.get("expectancy_intent_all") or -1e9)))
    latest = {
        "generation_id": f"autonomy_public_indicator_{gen}",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "promoted": None,
        "not_live": True,
        "n_arms": len(rows),
        "extra": extra,
        "arms": rows,
    }
    (OUT / f"gen_{gen}_latest.json").write_text(json.dumps(jsonable(latest), indent=2), encoding="utf-8")
    md = [
        f"# Autonomy public-indicator hunt gen {gen}",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`. Arms: {len(rows)}.",
        f"Gates: ebr≤{ENTRY_BAR_EXIT_CAP}, tpm∈[{MIN_TRADES_PER_MONTH},{MAX_TRADES_PER_MONTH}], n≥{MIN_TRADES_FLAG}, PF≥max(1.20, control).",
        "",
        "| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    controls = {a["symbol"]: a for a in rows if a.get("mode") == "control" and a.get("status") == "RAN"}
    flagged = []
    for r in rows:
        ebr = r.get("entry_bar_exit_rate")
        ntr = r.get("n_trades") or 0
        tpm = r.get("trades_per_month")
        flag = ""
        if r.get("status") == "RAN":
            if ebr is not None and float(ebr) > ENTRY_BAR_EXIT_CAP:
                flag = "EBR>35%"
            elif tpm is not None and float(tpm) > MAX_TRADES_PER_MONTH:
                flag = "TPM>MAX"
            elif tpm is not None and float(tpm) < MIN_TRADES_PER_MONTH:
                flag = "TPM<MIN"
            elif ntr < 12:
                flag = "THIN"
            else:
                flag = "ok"
            if is_gate_candidate(r, controls.get(r.get("symbol"))):
                flag = "GATE_CAND"
                flagged.append(r)
        md.append(
            "| {symbol} | {h} | `{ev}` | {mode} | {n} | {tpm} | {pf} | {wr} | {sh} | {ex} | {ebr} | {flag} | {st} |".format(
                symbol=r.get("symbol"),
                h=r.get("horizon"),
                ev=r.get("event"),
                mode=r.get("mode"),
                n=r.get("n_trades"),
                tpm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")),
                wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")),
                ex=_fmt(r.get("expectancy_intent_all")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                flag=flag,
                st=r.get("status"),
            )
        )
    (OUT / f"gen_{gen}_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (OUT / f"gen_{gen}_flagged.json").write_text(
        json.dumps(jsonable({"n": len(flagged), "arms": flagged}), indent=2), encoding="utf-8"
    )


def _iter_specs(events: tuple[str, ...]) -> list[dict]:
    specs: list[dict] = []
    tp, sl = TP_SL
    for symbol in SYMBOLS_15M:
        specs.append(
            {
                "phase": "A_control",
                "symbol": symbol,
                "timeframe": "15m",
                "horizon": 4,
                "event": "control",
                "mode": "control",
                "tp": tp,
                "sl": sl,
                "gate": "control",
            }
        )
    for symbol in SYMBOLS_15M:
        for h in HORIZONS:
            for event in events:
                specs.append(
                    {
                        "phase": "B_filter_11",
                        "symbol": symbol,
                        "timeframe": "15m",
                        "horizon": h,
                        "event": event,
                        "mode": "one_head_filter_pi_star",
                        "tp": tp,
                        "sl": sl,
                        "gate": "pi_star",
                    }
                )
    return specs


def _arm_id(s: dict) -> str:
    return (
        f"{s['symbol']}|{s['timeframe']}|H{s['horizon']}|{s['event']}|"
        f"{s['mode']}|tp{s['tp']}|sl{s['sl']}|{s['gate']}"
    )


class _Ctx:
    def __init__(self, symbol: str, tf: str, max_rows: int, gen: str, db_dir: Path, cache: Path):
        self.symbol = symbol
        self.tf = tf
        self.gen = gen
        self.ohlcv = _load_pre_lock(symbol, tf, max_rows)
        self.sc = _score_cached(symbol, tf, max_rows, cache)
        self.ctrl_mask, self.level_override = _imp001._control_mask(symbol, self.sc)
        self.work_ctrl = WORK_CTRL[symbol]
        cut = chronological_cut_index(len(self.ohlcv))
        self.test_start = int(index_to_ms(self.ohlcv.index)[cut])
        self.in_test = self.sc.ts_ms >= self.test_start
        db = db_dir / f"{symbol}_{tf}"
        db.mkdir(parents=True, exist_ok=True)
        self.train_path = db / "train.sqlite"
        self.test_path = db / "test.sqlite"
        if not (self.train_path.exists() and self.test_path.exists()):
            split_ohlcv_files(self.ohlcv, train_path=self.train_path, test_path=self.test_path)
        self.train_df = _load_ohlcv_sqlite(self.train_path)
        self.test_df = _load_ohlcv_sqlite(self.test_path)
        self.packs_tr: dict[int, object] = {}
        self.packs_te: dict[int, object] = {}
        self.heads: dict[tuple[int, str], np.ndarray] = {}

    def pack(self, horizon: int, train: bool):
        store = self.packs_tr if train else self.packs_te
        if horizon not in store:
            df = self.train_df if train else self.test_df
            print(f"  pack {self.symbol} gen={self.gen} H={horizon} train={train}", flush=True)
            store[horizon] = build_autonomy_pack(df, gen=self.gen, horizon=horizon)
        return store[horizon]

    def head(self, horizon: int, event: str) -> np.ndarray:
        key = (horizon, event)
        if key not in self.heads:
            print(f"  fit {self.symbol} {event} H={horizon}", flush=True)
            self.heads[key] = _fit_head(self.pack(horizon, True), self.pack(horizon, False), event)
        return self.heads[key]


def _pivot_side_lim(ctx: _Ctx, mask: np.ndarray):
    sc = ctx.sc
    if ctx.level_override is not None:
        old = sc.level_ret
        sc.level_ret = ctx.level_override
        _, is_s, lim = limit_price_side(sc, mask)
        sc.level_ret = old
    else:
        _, is_s, lim = limit_price_side(sc, mask)
    return is_s, lim


def _run_spec(ctx: _Ctx, spec: dict) -> dict:
    symbol = spec["symbol"]
    tp = float(spec["tp"])
    sl = float(spec["sl"])
    h = int(spec["horizon"])
    tag = _arm_id(spec)
    mag = net_bracket_magnitudes(tp, sl)
    pi_star = float(mag.pi_star)
    sc = ctx.sc
    work = ctx.work_ctrl
    if spec["mode"] == "control":
        mask = ctx.ctrl_mask & ctx.in_test
        is_s, lim = _pivot_side_lim(ctx, mask)
        out = run_limit_arm(symbol, sc, mask, is_s, lim, tag=tag, work=work, max_hold=6, tp=tp, sl=sl)
        out["pi_star"] = pi_star
        return out
    p_te = ctx.head(h, spec["event"])
    p_sc = _map_to_sc(sc, ctx.test_df.index, p_te)
    gated = np.isfinite(p_sc) & (p_sc >= pi_star) & ctx.in_test
    mask = gated & ctx.ctrl_mask
    is_s, lim = _pivot_side_lim(ctx, mask)
    out = run_limit_arm(symbol, sc, mask, is_s, lim, tag=tag, work=work, max_hold=6, tp=tp, sl=sl)
    out["pi_star"] = pi_star
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", required=True, choices=sorted(GEN_EVENTS))
    ap.add_argument("--max-arms", type=int, default=0)
    ap.add_argument("--skip-leakage", action="store_true")
    args = ap.parse_args()
    gen = args.gen
    events = GEN_EVENTS[gen]
    prereg = _ROOT / "configs" / "preregister" / f"autonomy_gen_{gen}_public_indicators.yaml"
    db_dir = ARTIFACTS / "sqlite" / f"autonomy_gen_{gen}"
    cache = db_dir / "cache"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    prereg_sha = _sha(prereg) if prereg.exists() else ""
    text = prereg.read_text(encoding="utf-8") if prereg.exists() else ""
    if prereg.exists() and "preregister_sha256_at_run:" not in text:
        prereg.write_text(text.rstrip() + f"\n\npreregister_sha256_at_run: {prereg_sha}\n", encoding="utf-8")
        prereg_sha = _sha(prereg)
    db_dir.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(db_dir / "hunt.sqlite")
    append_ledger(f"AUTONOMY_GEN_{gen} start {stamp}", tier=0)
    print(f"gen={gen} preregister_sha256={prereg_sha}", flush=True)

    leak = []
    if not args.skip_leakage:
        for symbol in SYMBOLS_15M:
            rec = _leak(symbol, "15m")
            leak.append(rec)
            print("leakage", rec, flush=True)
            if rec["status"] != "PASS":
                raise SystemExit(f"leakage FAIL {rec}")

    specs = _iter_specs(events)
    if args.max_arms > 0:
        specs = specs[: args.max_arms]
    print(f"planned_arms={len(specs)}", flush=True)

    ctxs: dict[tuple[str, str], _Ctx] = {}
    ran = 0
    for i, spec in enumerate(specs, start=1):
        aid = _arm_id(spec)
        if arm_done(con, aid):
            continue
        key = (spec["symbol"], spec["timeframe"])
        if key not in ctxs:
            print(f"=== context {key} ===", flush=True)
            ctxs[key] = _Ctx(spec["symbol"], spec["timeframe"], 120_000, gen, db_dir, cache)
        print(f"[{i}/{len(specs)}] {aid}", flush=True)
        try:
            payload = _run_spec(ctxs[key], spec)
        except Exception as exc:  # noqa: BLE001
            payload = {"status": "ERROR", "error": str(exc)[:500], "n_trades": 0}
            print(f"  ERROR {exc}", flush=True)
        payload.update({**spec, "arm_id": aid})
        save_arm(con, aid, spec, payload)
        ran += 1
        print(
            f"  {payload.get('status')} n={payload.get('n_trades')} PF={payload.get('profit_factor')}",
            flush=True,
        )
        if ran % 3 == 0:
            _write_leaderboard(con, stamp, gen, {"leakage": leak, "preregister_sha256": prereg_sha}, db_dir)

    _write_leaderboard(con, stamp, gen, {"leakage": leak, "preregister_sha256": prereg_sha}, db_dir)
    append_ledger(f"AUTONOMY_GEN_{gen} done arms={ran}", tier=0)
    print(f"WROTE {OUT / f'gen_{gen}_latest.md'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
