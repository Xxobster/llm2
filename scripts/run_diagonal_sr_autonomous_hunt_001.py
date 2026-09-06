"""Autonomous diagonal support/resistance hunt 001.

RESEARCH_ONLY. Rank on chronological test window before lockbox only.
Resumes from artifacts/sqlite/diagonal_sr_autonomous_hunt_001/hunt.sqlite.
"""

from __future__ import annotations

import argparse
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

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

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
from llm2.diagonal_sr.events import (  # noqa: E402
    EVENT_IDS_A,
    EVENT_IDS_B,
    LONG_EVENTS,
    MARKET_ENTRY_EVENTS,
    SHORT_EVENTS,
    build_event_pack,
    build_features_for_guard,
)
from llm2.diagonal_sr.mtf import geometry_context_map  # noqa: E402
from llm2.diagonal_sr.train import (  # noqa: E402
    chronological_cut_index,
    fit_one_head,
    load_ohlcv_sqlite,
    split_ohlcv_files,
)
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.pivot.strategy.ev import net_bracket_magnitudes  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

PREREG = _ROOT / "configs" / "preregister" / "diagonal_sr_autonomous_hunt_001.yaml"
OUT = ARTIFACTS / "reports" / "diagonal_sr"
DB_DIR = ARTIFACTS / "sqlite" / "diagonal_sr_autonomous_hunt_001"
CACHE = DB_DIR / "cache"

SYMBOLS = ("ETHUSDT", "SOLUSDT", "BTCUSDT")
TFS = ("15m", "1h", "4h")
BRACKETS_BASE = (
    (0.010, 0.010),
    (0.015, 0.010),
    (0.020, 0.010),
    (0.010, 0.015),
    (0.020, 0.020),
)
BRACKETS_4H_EXTRA = ((0.030, 0.020),)
NEVER_PROMOTE = ((0.005, 0.005),)
MODELS = ("lgbm", "lgbm_shallow", "ridge")
MAX_TPM = {"15m": 40.0, "1h": 20.0, "4h": 12.0}
WORK = {"15m": 4, "1h": 3, "4h": 2}
MAX_HOLD = {"15m": 6, "1h": 8, "4h": 6}
MAX_ROWS = {"15m": 120_000, "1h": 40_000, "4h": 20_000, "1d": 8_000}


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
        return {"symbol": symbol, "timeframe": tf, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "timeframe": tf, "status": "FAIL", "error": str(exc)[:400]}


def _map_to_bars(bar_ts: np.ndarray, test_index, values: np.ndarray) -> np.ndarray:
    pos = {int(t): i for i, t in enumerate(index_to_ms(test_index).tolist())}
    out = np.full(len(bar_ts), np.nan)
    vals = np.asarray(values, dtype=float)
    for j, t in enumerate(bar_ts):
        i = pos.get(int(t))
        if i is not None:
            out[j] = vals[i]
    return out


def _event_side(event: str, n: int) -> np.ndarray:
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


def _flag_arm(r: dict) -> str:
    if r.get("status") != "RAN":
        return ""
    ebr = r.get("entry_bar_exit_rate")
    ntr = r.get("n_trades") or 0
    tpm = r.get("trades_per_month")
    tf = r.get("timeframe") or "15m"
    never = bool(r.get("never_promote"))
    if never:
        return "NEVER_PROMOTE"
    if ebr is not None and float(ebr) > 0.35:
        return "EBR>35%"
    if ntr < 12:
        return "THIN"
    if tpm is not None and float(tpm) < 4.0:
        return "TPM<4"
    if tpm is not None and float(tpm) > float(MAX_TPM.get(tf, 40)):
        return "TPM>CAP"
    if ntr >= 50:
        return "FLAG"
    return "ok"


def _write_leaderboard(con, stamp: str, extra: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    rows.sort(
        key=lambda r: (
            0 if r.get("status") == "RAN" else 1,
            -(r.get("expectancy_intent_all") or -1e9),
        )
    )
    latest = {
        "generation_id": "diagonal_sr_autonomous_hunt_001",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "not_live": True,
        "n_arms": len(rows),
        "extra": extra,
        "arms": rows,
    }
    (OUT / "autonomous_hunt_001_latest.json").write_text(
        json.dumps(jsonable(latest), indent=2), encoding="utf-8"
    )
    md = [
        "# Autonomous diagonal support/resistance hunt 001",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`. Arms: {len(rows)}.",
        "Rank window: chronological test (last 30% before lockbox). Do not quote as live.",
        "",
        "| Symbol | TF | Gen | H | Event | Mode | Model | TP | SL | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |",
        "|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for r in rows:
        md.append(
            "| {symbol} | {tf} | {gen} | {h} | `{ev}` | {mode} | {model} | {tp} | {sl} | {n} | {tpm} | {pf} | {wr} | {sh} | {ex} | {ebr} | {flag} | {st} |".format(
                symbol=r.get("symbol"),
                tf=r.get("timeframe"),
                gen=r.get("generation"),
                h=r.get("horizon"),
                ev=r.get("event"),
                mode=r.get("mode"),
                model=r.get("model"),
                tp=r.get("tp"),
                sl=r.get("sl"),
                n=r.get("n_trades"),
                tpm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")),
                wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")),
                ex=_fmt(r.get("expectancy_intent_all")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                flag=_flag_arm(r),
                st=r.get("status"),
            )
        )
    (OUT / "autonomous_hunt_001_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    flagged = [r for r in rows if _flag_arm(r) == "FLAG" and r.get("mode") != "rule_event"]
    (OUT / "autonomous_hunt_001_flagged.json").write_text(
        json.dumps(jsonable({"n": len(flagged), "arms": flagged[:80]}), indent=2),
        encoding="utf-8",
    )


def _brackets_for(tf: str, *, include_never: bool) -> list[tuple[float, float]]:
    out = list(BRACKETS_BASE)
    if tf == "4h":
        out.extend(BRACKETS_4H_EXTRA)
    if include_never and tf == "15m":
        out = list(NEVER_PROMOTE) + out
    return out


def _iter_specs() -> list[dict]:
    specs: list[dict] = []

    # Gen A — diagonal only.
    # Phase A: rule_event baselines (no model), H=4, primary brackets.
    for symbol in SYMBOLS:
        for tf in TFS:
            for event in EVENT_IDS_A:
                for tp, sl in _brackets_for(tf, include_never=False)[:2]:
                    specs.append(
                        {
                            "phase": "A_rule",
                            "generation": "A",
                            "symbol": symbol,
                            "timeframe": tf,
                            "horizon": 4,
                            "event": event,
                            "mode": "rule_event",
                            "model": "none",
                            "tp": tp,
                            "sl": sl,
                            "gate": "occurrence",
                            "never_promote": False,
                        }
                    )

    # Phase B: standalone lgbm H=4 1%/1% across all TF.
    for symbol in SYMBOLS:
        for tf in TFS:
            for event in EVENT_IDS_A:
                specs.append(
                    {
                        "phase": "B_solo_lgbm_11",
                        "generation": "A",
                        "symbol": symbol,
                        "timeframe": tf,
                        "horizon": 4,
                        "event": event,
                        "mode": "standalone_pi_star",
                        "model": "lgbm",
                        "tp": 0.01,
                        "sl": 0.01,
                        "gate": "pi_star",
                        "never_promote": False,
                    }
                )

    # Phase C: remaining models × brackets on 15m H=4.
    for symbol in SYMBOLS:
        for event in EVENT_IDS_A:
            for model in MODELS:
                for tp, sl in _brackets_for("15m", include_never=True):
                    if model == "lgbm" and tp == 0.01 and sl == 0.01:
                        continue  # already in B
                    specs.append(
                        {
                            "phase": "C_15m_grid",
                            "generation": "A",
                            "symbol": symbol,
                            "timeframe": "15m",
                            "horizon": 4,
                            "event": event,
                            "mode": "standalone_pi_star",
                            "model": model,
                            "tp": tp,
                            "sl": sl,
                            "gate": "pi_star",
                            "never_promote": bool(tp == 0.005 and sl == 0.005),
                        }
                    )

    # Phase D: filter_pi_star (proximity AND model) 15m 1/1 and 2/1.
    for symbol in SYMBOLS:
        for event in EVENT_IDS_A:
            for tp, sl in ((0.01, 0.01), (0.02, 0.01)):
                specs.append(
                    {
                        "phase": "D_filter",
                        "generation": "A",
                        "symbol": symbol,
                        "timeframe": "15m",
                        "horizon": 4,
                        "event": event,
                        "mode": "filter_pi_star",
                        "model": "lgbm",
                        "tp": tp,
                        "sl": sl,
                        "gate": "pi_star",
                        "never_promote": False,
                    }
                )

    # Phase E: H=8 15m lgbm 1/1 and 2/1.
    for symbol in SYMBOLS:
        for event in EVENT_IDS_A:
            for tp, sl in ((0.01, 0.01), (0.02, 0.01)):
                specs.append(
                    {
                        "phase": "E_h8",
                        "generation": "A",
                        "symbol": symbol,
                        "timeframe": "15m",
                        "horizon": 8,
                        "event": event,
                        "mode": "standalone_pi_star",
                        "model": "lgbm",
                        "tp": tp,
                        "sl": sl,
                        "gate": "pi_star",
                        "never_promote": False,
                    }
                )

    # Phase F: 1h/4h remaining brackets × lgbm.
    for tf in ("1h", "4h"):
        for symbol in SYMBOLS:
            for event in EVENT_IDS_A:
                for tp, sl in _brackets_for(tf, include_never=False):
                    if tp == 0.01 and sl == 0.01:
                        continue
                    specs.append(
                        {
                            "phase": f"F_{tf}",
                            "generation": "A",
                            "symbol": symbol,
                            "timeframe": tf,
                            "horizon": 4,
                            "event": event,
                            "mode": "standalone_pi_star",
                            "model": "lgbm",
                            "tp": tp,
                            "sl": sl,
                            "gate": "pi_star",
                            "never_promote": False,
                        }
                    )

    # Gen B — diagonal + horizontal confluence events.
    for symbol in SYMBOLS:
        for tf in TFS:
            for event in EVENT_IDS_B:
                # rule
                specs.append(
                    {
                        "phase": "G_b_rule",
                        "generation": "B",
                        "symbol": symbol,
                        "timeframe": tf,
                        "horizon": 4,
                        "event": event,
                        "mode": "rule_event",
                        "model": "none",
                        "tp": 0.01,
                        "sl": 0.01,
                        "gate": "occurrence",
                        "never_promote": False,
                    }
                )
                for tp, sl in ((0.01, 0.01), (0.02, 0.01), (0.015, 0.01)):
                    specs.append(
                        {
                            "phase": "G_b_solo",
                            "generation": "B",
                            "symbol": symbol,
                            "timeframe": tf,
                            "horizon": 4,
                            "event": event,
                            "mode": "standalone_pi_star",
                            "model": "lgbm",
                            "tp": tp,
                            "sl": sl,
                            "gate": "pi_star",
                            "never_promote": False,
                        }
                    )

    return specs


def _arm_id(s: dict) -> str:
    return (
        f"{s['generation']}|{s['symbol']}|{s['timeframe']}|H{s['horizon']}|"
        f"{s['event']}|{s['mode']}|{s['model']}|tp{s['tp']}|sl{s['sl']}"
    )


class _Ctx:
    def __init__(self, symbol: str, tf: str):
        self.symbol = symbol
        self.tf = tf
        max_rows = MAX_ROWS[tf]
        self.ohlcv = _load_pre_lock(symbol, tf, max_rows)
        self.sc = make_bar_series(symbol, tf, self.ohlcv)
        cut = chronological_cut_index(len(self.ohlcv))
        self.test_start = int(index_to_ms(self.ohlcv.index)[cut])
        self.in_test = self.sc.ts_ms >= self.test_start
        db = DB_DIR / f"{symbol}_{tf}"
        db.mkdir(parents=True, exist_ok=True)
        self.train_path = db / "train.sqlite"
        self.test_path = db / "test.sqlite"
        if not (self.train_path.exists() and self.test_path.exists()):
            split_ohlcv_files(self.ohlcv, train_path=self.train_path, test_path=self.test_path)
        self.train_df = load_ohlcv_sqlite(self.train_path)
        self.test_df = load_ohlcv_sqlite(self.test_path)
        self.htf: dict[str, pd.DataFrame] = {}
        for htf in geometry_context_map(tf):
            try:
                self.htf[htf] = _load_pre_lock(symbol, htf, MAX_ROWS.get(htf, 20_000))
            except Exception as exc:  # noqa: BLE001
                print(f"  warn HTF {htf}: {exc}", flush=True)
        self.packs_tr: dict[tuple[str, int], object] = {}
        self.packs_te: dict[tuple[str, int], object] = {}
        self.heads: dict[tuple[str, int, str, str], dict] = {}

    def pack(self, generation: str, horizon: int, train: bool):
        key = (generation, horizon)
        store = self.packs_tr if train else self.packs_te
        if key not in store:
            df = self.train_df if train else self.test_df
            print(
                f"  event pack {self.symbol} {self.tf} gen={generation} H={horizon} train={train}",
                flush=True,
            )
            store[key] = build_event_pack(
                df,
                horizon=horizon,
                generation=generation,
                htf_ohlcv_by_tf=self.htf,
                decision_tf=self.tf,
            )
        return store[key]

    def head(self, generation: str, horizon: int, event: str, model: str) -> np.ndarray:
        key = (generation, horizon, event, model)
        if key not in self.heads:
            tr = self.pack(generation, horizon, True)
            te = self.pack(generation, horizon, False)
            print(
                f"  fit head {self.symbol} {event} gen={generation} H={horizon} model={model}",
                flush=True,
            )
            self.heads[key] = fit_one_head(
                tr, te, event, generation=generation, model_name=model
            )
        return np.asarray(self.heads[key]["p_test"], dtype=float)


def _run_spec(ctx: _Ctx, spec: dict) -> dict:
    symbol = spec["symbol"]
    tf = spec["timeframe"]
    tp = float(spec["tp"])
    sl = float(spec["sl"])
    h = int(spec["horizon"])
    gen = spec["generation"]
    event = spec["event"]
    mode = spec["mode"]
    model = spec["model"]
    max_hold = MAX_HOLD[tf]
    work = WORK[tf]
    tag = _arm_id(spec)
    mag = net_bracket_magnitudes(tp, sl)
    pi_star = float(mag.pi_star)
    sc = ctx.sc
    te = ctx.pack(gen, h, False)
    n_te = len(ctx.test_df)
    side_te = _event_side(event, n_te)

    if mode == "rule_event":
        occ = te.occurrence[event].to_numpy(dtype=float) if event in te.occurrence.columns else np.zeros(n_te)
        fire = occ >= 0.5
        fire_sc = _map_to_bars(sc.ts_ms, ctx.test_df.index, fire.astype(float))
        side_sc = _map_to_bars(sc.ts_ms, ctx.test_df.index, side_te)
        mask = ctx.in_test & (fire_sc >= 0.5) & np.isfinite(side_sc) & (side_sc != 0)
    else:
        p_te = ctx.head(gen, h, event, model if model != "none" else "lgbm")
        p_sc = _map_to_bars(sc.ts_ms, ctx.test_df.index, p_te)
        gated = np.isfinite(p_sc) & (p_sc >= pi_star) & ctx.in_test
        side_sc = _map_to_bars(sc.ts_ms, ctx.test_df.index, side_te)
        mask = gated & np.isfinite(side_sc) & (side_sc != 0)
        if mode == "filter_pi_star":
            # Structural proximity filter: require near the relevant diagonal on the test pack.
            feat = te.features
            if event in LONG_EVENTS:
                near = feat["near_lower"].to_numpy(dtype=float) if "near_lower" in feat else np.ones(n_te)
            else:
                near = feat["near_upper"].to_numpy(dtype=float) if "near_upper" in feat else np.ones(n_te)
            near_sc = _map_to_bars(sc.ts_ms, ctx.test_df.index, near)
            mask = mask & (near_sc >= 0.5)

    is_short = (side_sc < 0)[np.flatnonzero(mask)]
    market = event in MARKET_ENTRY_EVENTS
    if market:
        out = run_market_arm(
            symbol, sc, mask, is_short, tag=tag, max_hold=max_hold, tp=tp, sl=sl
        )
    else:
        lim = _limit_atr(sc, mask, is_short)
        out = run_limit_arm(
            symbol, sc, mask, is_short, lim, tag=tag, work=work, max_hold=max_hold, tp=tp, sl=sl
        )
    out["pi_star"] = pi_star
    out["entry"] = "market" if market else "limit"
    out["never_promote"] = bool(spec.get("never_promote"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-arms", type=int, default=0, help="0 = full closed grid")
    ap.add_argument("--skip-leakage", action="store_true")
    ap.add_argument("--leakage-only", action="store_true")
    args = ap.parse_args()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    prereg_sha = _sha(PREREG)
    text = PREREG.read_text(encoding="utf-8")
    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(
            text.rstrip() + f"\n\npreregister_sha256_at_run: {prereg_sha}\n", encoding="utf-8"
        )
    _ = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    DB_DIR.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB_DIR / "hunt.sqlite")
    append_ledger(f"DIAGONAL_SR_AUTONOMOUS_HUNT_001 start {stamp}", tier=0)
    print(f"preregister_sha256={prereg_sha}", flush=True)

    leak = []
    if not args.skip_leakage:
        for symbol in SYMBOLS:
            for tf in ("15m", "1h"):
                rec = _leak(symbol, tf)
                leak.append(rec)
                print("leakage", rec, flush=True)
                if rec["status"] != "PASS":
                    raise SystemExit(f"leakage FAIL {rec}")
        # Persist leakage result
        (OUT).mkdir(parents=True, exist_ok=True)
        (OUT / "leakage_001.json").write_text(json.dumps(leak, indent=2), encoding="utf-8")

    if args.leakage_only:
        print("leakage-only done", flush=True)
        return 0

    specs = _iter_specs()
    if args.max_arms and args.max_arms > 0:
        specs = specs[: args.max_arms]
    done0 = sum(1 for s in specs if arm_done(con, _arm_id(s)))
    print(f"planned_arms={len(specs)} already_done={done0}", flush=True)

    # Checkpoint planned count
    with (CACHE / "planned_arms.json").open("w", encoding="utf-8") as fh:
        json.dump({"n": len(specs), "stamp": stamp}, fh)

    ctxs: dict[tuple[str, str], _Ctx] = {}
    ran = 0
    for i, spec in enumerate(specs, start=1):
        aid = _arm_id(spec)
        if arm_done(con, aid):
            continue
        key = (spec["symbol"], spec["timeframe"])
        if key not in ctxs:
            print(f"=== context {key} ===", flush=True)
            ctxs[key] = _Ctx(spec["symbol"], spec["timeframe"])
        ctx = ctxs[key]
        print(f"[{i}/{len(specs)}] {aid}", flush=True)
        try:
            payload = _run_spec(ctx, spec)
        except Exception as exc:  # noqa: BLE001
            payload = {"status": "ERROR", "error": str(exc)[:500], "n_trades": 0}
            print(f"  ERROR {exc}", flush=True)
        payload.update(
            {
                "symbol": spec["symbol"],
                "timeframe": spec["timeframe"],
                "horizon": spec["horizon"],
                "event": spec["event"],
                "mode": spec["mode"],
                "model": spec["model"],
                "generation": spec["generation"],
                "tp": spec["tp"],
                "sl": spec["sl"],
                "gate": spec["gate"],
                "phase": spec["phase"],
                "never_promote": spec.get("never_promote", False),
                "arm_id": aid,
            }
        )
        save_arm(con, aid, spec, payload)
        ran += 1
        print(
            f"  {payload.get('status')} n={payload.get('n_trades')} PF={payload.get('profit_factor')} "
            f"WR={payload.get('win_rate')} Sharpe={payload.get('sharpe_annualised')} "
            f"tpm={payload.get('trades_per_month')}",
            flush=True,
        )
        if ran % 2 == 0 or payload.get("status") == "ERROR":
            _write_leaderboard(con, stamp, {"leakage": leak, "preregister_sha256": prereg_sha})

    _write_leaderboard(con, stamp, {"leakage": leak, "preregister_sha256": prereg_sha})
    append_ledger(
        f"DIAGONAL_SR_AUTONOMOUS_HUNT_001 checkpoint arms={ran} path={OUT / 'autonomous_hunt_001_latest.md'}",
        tier=0,
    )
    print(f"WROTE {OUT / 'autonomous_hunt_001_latest.md'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
