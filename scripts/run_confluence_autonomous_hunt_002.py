"""Autonomous confluence hunt 002: one-head filters, regimes, TP/SL grid.

RESEARCH_ONLY. Rank on chronological test window before lockbox only.
Resumes from artifacts/sqlite/confluence_autonomous_hunt_002/hunt.sqlite.
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

from llm2.confluence.events import (  # noqa: E402
    CONTINUATION_EVENTS,
    EVENT_IDS,
    EVENT_IDS_002,
    LONG_EVENTS,
    MARKET_ENTRY_EVENTS,
    RANGE_EVENTS,
    REVERSAL_EVENTS,
    SHORT_EVENTS,
    build_event_pack,
    build_features_for_guard,
)
from llm2.confluence.sim_arms import (  # noqa: E402
    arm_done,
    jsonable,
    load_arms,
    open_checkpoint,
    run_limit_arm,
    run_market_arm,
    save_arm,
)
from llm2.confluence.train import chronological_cut_index, fit_one_head, split_ohlcv_files  # noqa: E402
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

PREREG = _ROOT / "configs" / "preregister" / "confluence_autonomous_hunt_002.yaml"
PACK = "level_vsa"
OUT = ARTIFACTS / "reports" / "confluence"
DB_DIR = ARTIFACTS / "sqlite" / "confluence_autonomous_hunt_002"
CACHE = DB_DIR / "cache"
ALL_EVENTS = EVENT_IDS + EVENT_IDS_002
BRACKETS = ((0.005, 0.005), (0.010, 0.010), (0.015, 0.010), (0.020, 0.010), (0.010, 0.015))
SYMBOLS_15M = ("ETHUSDT", "SOLUSDT", "BTCUSDT")
WORK_CTRL = {"ETHUSDT": 4, "SOLUSDT": 5, "BTCUSDT": 4}


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


def _score_cached(symbol: str, tf: str, max_rows: int):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"score_{symbol}_{tf}.pkl"
    if path.exists():
        print(f"  load cached score_oos {path.name}", flush=True)
        with path.open("rb") as fh:
            return pickle.load(fh)
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
    with path.open("wb") as fh:
        pickle.dump(sc, fh, protocol=4)
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


def _known_now_side(event: str, feat: pd.DataFrame) -> np.ndarray:
    n = len(feat)
    if event in LONG_EVENTS:
        return np.ones(n, dtype=float)
    if event in SHORT_EVENTS:
        return np.full(n, -1.0)
    pos = feat["close_pos_in_range20"].to_numpy(dtype=float)
    ret4 = feat["ret4"].to_numpy(dtype=float)
    pdi = feat["plus_di"].to_numpy(dtype=float)
    mdi = feat["minus_di"].to_numpy(dtype=float)
    ema = feat["ema21_dist"].to_numpy(dtype=float)
    pulse = feat["pulse_dir"].to_numpy(dtype=float)
    if event == "range_hold":
        return np.where(pos >= 0.66, -1.0, np.where(pos <= 0.34, 1.0, 0.0))
    if event == "adx_fade":
        return np.where(pdi > mdi, -1.0, 1.0)
    if event == "vsa_dryup_expand":
        return np.where(ema < 0.0, 1.0, -1.0)
    if event in {"atr_squeeze_expand", "pulse_extend"}:
        src = pulse if event == "pulse_extend" else ret4
        return np.sign(src)
    if event == "structure_break_hold":
        up = feat["fresh_break_high"].to_numpy(dtype=float) > 0.5
        dn = feat["fresh_break_low"].to_numpy(dtype=float) > 0.5
        return np.where(up, 1.0, np.where(dn, -1.0, 0.0))
    return np.zeros(n, dtype=float)


def _limit_atr(sc, mask: np.ndarray, is_short: np.ndarray) -> np.ndarray:
    idx = np.flatnonzero(mask)
    c = sc.close[idx]
    atr = sc.atr_frac[idx]
    move = np.clip(np.where(np.isfinite(atr), atr, 0.005), 0.0015, 0.03)
    return np.where(is_short, c * (1.0 + move), c * (1.0 - move))


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
        "generation_id": "confluence_autonomous_hunt_002",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "not_live": True,
        "n_arms": len(rows),
        "extra": extra,
        "arms": rows,
    }
    (OUT / "autonomous_hunt_002_latest.json").write_text(
        json.dumps(jsonable(latest), indent=2), encoding="utf-8"
    )
    md = [
        "# Autonomous confluence hunt 002",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`. Arms: {len(rows)}.",
        "Rank window: chronological test (last 30% before lockbox). Do not quote as live.",
        "",
        "| Symbol | TF | H | Event | Mode | TP | SL | n | /mo | PF | WR | Sharpe | HAC Sharpe | exp_i | ebr | flag | status |",
        "|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for r in rows:
        ebr = r.get("entry_bar_exit_rate")
        ntr = r.get("n_trades") or 0
        flag = ""
        if r.get("status") == "RAN":
            if ebr is not None and float(ebr) > 0.35:
                flag = "EBR>35%"
            elif ntr < 12:
                flag = "THIN"
            else:
                flag = "ok"
        md.append(
            "| {symbol} | {tf} | {h} | `{ev}` | {mode} | {tp} | {sl} | {n} | {tpm} | {pf} | {wr} | {sh} | {hac} | {ex} | {ebr} | {flag} | {st} |".format(
                symbol=r.get("symbol"),
                tf=r.get("timeframe"),
                h=r.get("horizon"),
                ev=r.get("event"),
                mode=r.get("mode"),
                tp=r.get("tp"),
                sl=r.get("sl"),
                n=r.get("n_trades"),
                tpm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")),
                wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")),
                hac=_fmt(r.get("sharpe_hac_annualised")),
                ex=_fmt(r.get("expectancy_intent_all")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                flag=flag,
                st=r.get("status"),
            )
        )
    (OUT / "autonomous_hunt_002_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    flagged = [
        r
        for r in rows
        if r.get("status") == "RAN"
        and (r.get("n_trades") or 0) >= 50
        and (r.get("entry_bar_exit_rate") or 1) <= 0.35
        and r.get("mode") != "control"
    ]
    (OUT / "autonomous_hunt_002_flagged.json").write_text(
        json.dumps(jsonable({"n": len(flagged), "arms": flagged[:40]}), indent=2),
        encoding="utf-8",
    )


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


def _family(event: str) -> str:
    if event in RANGE_EVENTS:
        return "range"
    if event in CONTINUATION_EVENTS:
        return "continuation"
    if event in REVERSAL_EVENTS:
        return "reversal"
    return "other"


def _iter_specs() -> list[dict]:
    specs: list[dict] = []
    # Phase A: 15m controls, all brackets (fast baseline table).
    for symbol in SYMBOLS_15M:
        for tp, sl in BRACKETS:
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
    # Phase B: one-head filter H=4, 1%/1% (the 001 next step).
    for symbol in SYMBOLS_15M:
        for event in ALL_EVENTS:
            specs.append(
                {
                    "phase": "B_filter_11",
                    "symbol": symbol,
                    "timeframe": "15m",
                    "horizon": 4,
                    "event": event,
                    "mode": "one_head_filter_pi_star",
                    "tp": 0.01,
                    "sl": 0.01,
                    "gate": "pi_star",
                }
            )
    # Phase C: standalone H=4, 1%/1%.
    for symbol in SYMBOLS_15M:
        for event in ALL_EVENTS:
            specs.append(
                {
                    "phase": "C_solo_11",
                    "symbol": symbol,
                    "timeframe": "15m",
                    "horizon": 4,
                    "event": event,
                    "mode": "one_head_standalone_pi_star",
                    "tp": 0.01,
                    "sl": 0.01,
                    "gate": "pi_star",
                }
            )
    # Phase D: remaining 15m H=4 brackets.
    for symbol in SYMBOLS_15M:
        for event in ALL_EVENTS:
            for tp, sl in BRACKETS:
                if tp == 0.01 and sl == 0.01:
                    continue
                for mode in ("one_head_filter_pi_star", "one_head_standalone_pi_star"):
                    specs.append(
                        {
                            "phase": "D_h4_grid",
                            "symbol": symbol,
                            "timeframe": "15m",
                            "horizon": 4,
                            "event": event,
                            "mode": mode,
                            "tp": tp,
                            "sl": sl,
                            "gate": "pi_star",
                        }
                    )
    # Phase E: H=8 and H=16, 15m, 1/1 then 2/1.
    for h in (8, 16):
        for symbol in SYMBOLS_15M:
            for event in ALL_EVENTS:
                for tp, sl in ((0.01, 0.01), (0.02, 0.01)):
                    for mode in ("one_head_filter_pi_star", "one_head_standalone_pi_star"):
                        specs.append(
                            {
                                "phase": f"E_h{h}",
                                "symbol": symbol,
                                "timeframe": "15m",
                                "horizon": h,
                                "event": event,
                                "mode": mode,
                                "tp": tp,
                                "sl": sl,
                                "gate": "pi_star",
                            }
                        )
    # Phase F: 3-way regime, 15m, all brackets, H=4.
    for symbol in SYMBOLS_15M:
        for tp, sl in BRACKETS:
            specs.append(
                {
                    "phase": "F_regime",
                    "symbol": symbol,
                    "timeframe": "15m",
                    "horizon": 4,
                    "event": "regime_argmax",
                    "mode": "regime_argmax",
                    "tp": tp,
                    "sl": sl,
                    "gate": "pi_star",
                }
            )
    # Phase G: 1h sibling, H=4, 1/1 and 2/1.
    for symbol in SYMBOLS_15M:
        for tp, sl in ((0.01, 0.01), (0.02, 0.01)):
            specs.append(
                {
                    "phase": "G_1h_control",
                    "symbol": symbol,
                    "timeframe": "1h",
                    "horizon": 4,
                    "event": "control",
                    "mode": "control",
                    "tp": tp,
                    "sl": sl,
                    "gate": "p75",
                }
            )
            for event in ALL_EVENTS:
                for mode in ("one_head_filter_pi_star", "one_head_standalone_pi_star"):
                    specs.append(
                        {
                            "phase": "G_1h",
                            "symbol": symbol,
                            "timeframe": "1h",
                            "horizon": 4,
                            "event": event,
                            "mode": mode,
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
    def __init__(self, symbol: str, tf: str, max_rows: int):
        self.symbol = symbol
        self.tf = tf
        self.max_rows = max_rows
        self.ohlcv = _load_pre_lock(symbol, tf, max_rows)
        self.sc = _score_cached(symbol, tf, max_rows)
        if tf == "15m":
            self.ctrl_mask, self.level_override = _imp001._control_mask(symbol, self.sc)
            self.work_ctrl = WORK_CTRL[symbol]
        else:
            from llm2.pivot.strategy.score_oos import gate_mask

            self.ctrl_mask = gate_mask(self.sc, mode="p75", tp=0.01, sl=0.01)
            self.level_override = None
            self.work_ctrl = 3
        cut = chronological_cut_index(len(self.ohlcv))
        self.test_start = int(index_to_ms(self.ohlcv.index)[cut])
        self.in_test = self.sc.ts_ms >= self.test_start
        db = DB_DIR / f"{symbol}_{tf}"
        db.mkdir(parents=True, exist_ok=True)
        self.train_path = db / "train.sqlite"
        self.test_path = db / "test.sqlite"
        if not (self.train_path.exists() and self.test_path.exists()):
            split_ohlcv_files(self.ohlcv, train_path=self.train_path, test_path=self.test_path)
        self.train_df = _load_ohlcv_sqlite(self.train_path)
        self.test_df = _load_ohlcv_sqlite(self.test_path)
        self.packs_tr: dict[int, object] = {}
        self.packs_te: dict[int, object] = {}
        self.heads: dict[tuple[int, str], dict] = {}
        self.feat_te = None

    def pack(self, horizon: int, train: bool):
        store = self.packs_tr if train else self.packs_te
        if horizon not in store:
            df = self.train_df if train else self.test_df
            print(f"  event pack {self.symbol} {self.tf} H={horizon} train={train}", flush=True)
            store[horizon] = build_event_pack(df, horizon=horizon, include_002=True)
        return store[horizon]

    def head(self, horizon: int, event: str) -> np.ndarray:
        key = (horizon, event)
        if key not in self.heads:
            tr = self.pack(horizon, True)
            te = self.pack(horizon, False)
            print(f"  fit head {self.symbol} {event} H={horizon}", flush=True)
            self.heads[key] = fit_one_head(tr, te, event)
        return np.asarray(self.heads[key]["p_test"], dtype=float)

    def test_feat(self) -> pd.DataFrame:
        if self.feat_te is None:
            self.feat_te = self.pack(4, False).features
        return self.feat_te


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
    tf = spec["timeframe"]
    tp = float(spec["tp"])
    sl = float(spec["sl"])
    h = int(spec["horizon"])
    max_hold = 6 if tf == "15m" else 8
    work = ctx.work_ctrl if spec["mode"] != "one_head_standalone_pi_star" else (4 if tf == "15m" else 3)
    if symbol == "SOLUSDT" and tf == "15m" and spec["mode"] == "control":
        work = 5
    tag = _arm_id(spec)
    mag = net_bracket_magnitudes(tp, sl)
    pi_star = float(mag.pi_star)
    sc = ctx.sc

    if spec["mode"] == "control":
        mask = ctx.ctrl_mask & ctx.in_test
        is_s, lim = _pivot_side_lim(ctx, mask)
        return run_limit_arm(
            symbol, sc, mask, is_s, lim, tag=tag, work=work, max_hold=max_hold, tp=tp, sl=sl
        )

    if spec["mode"] == "regime_argmax":
        te = ctx.pack(h, False)
        p_rev = np.zeros(len(ctx.test_df))
        p_con = np.zeros(len(ctx.test_df))
        n_rev = n_con = n_rng = 0
        for eid in REVERSAL_EVENTS:
            if eid in te.labels.columns:
                p = ctx.head(h, eid)
                p_rev = np.fmax(p_rev, np.where(np.isfinite(p), p, 0.0))
                n_rev += 1
        for eid in CONTINUATION_EVENTS:
            if eid in te.labels.columns:
                p = ctx.head(h, eid)
                p_con = np.fmax(p_con, np.where(np.isfinite(p), p, 0.0))
                n_con += 1
        p_rng = ctx.head(h, "range_hold")
        n_rng += 1
        _ = (n_rev, n_con, n_rng)
        feat = ctx.test_feat()
        ret4 = feat["ret4"].to_numpy(dtype=float)
        pos = feat["close_pos_in_range20"].to_numpy(dtype=float)
        stacked = np.vstack(
            [
                np.where(np.isfinite(p_rev), p_rev, -1.0),
                np.where(np.isfinite(p_con), p_con, -1.0),
                np.where(np.isfinite(p_rng), p_rng, -1.0),
            ]
        )
        which = np.argmax(stacked, axis=0)
        pmax = stacked[which, np.arange(stacked.shape[1])]
        fire = pmax >= pi_star
        side = np.zeros(len(ctx.test_df))
        # 0 reverse fade, 1 continue follow, 2 range mean-revert
        side = np.where(which == 0, -np.sign(ret4), side)
        side = np.where(which == 1, np.sign(ret4), side)
        side = np.where(which == 2, np.where(pos >= 0.66, -1.0, np.where(pos <= 0.34, 1.0, 0.0)), side)
        side_sc = _map_to_sc(sc, ctx.test_df.index, side)
        fire_sc = _map_to_sc(sc, ctx.test_df.index, fire.astype(float))
        which_sc = _map_to_sc(sc, ctx.test_df.index, which.astype(float))
        mask = ctx.in_test & np.isfinite(side_sc) & (side_sc != 0) & (fire_sc >= 0.5)
        cont = mask & (which_sc == 1.0)
        other = mask & ~cont
        is_short_cont = (side_sc < 0)[np.flatnonzero(cont)]
        is_short_other = (side_sc < 0)[np.flatnonzero(other)]
        if int(cont.sum()) >= 15:
            out_m = run_market_arm(
                symbol, sc, cont, is_short_cont, tag=tag + "|mkt", max_hold=max_hold, tp=tp, sl=sl
            )
        else:
            out_m = {"status": "TOO_FEW_GATED", "n_intent": int(cont.sum()), "n_trades": 0, "net_pnl": 0.0}
        if int(other.sum()) >= 15:
            lim = _limit_atr(sc, other, is_short_other)
            out_l = run_limit_arm(
                symbol,
                sc,
                other,
                is_short_other,
                lim,
                tag=tag + "|lim",
                work=work,
                max_hold=max_hold,
                tp=tp,
                sl=sl,
            )
        else:
            out_l = {"status": "TOO_FEW_GATED", "n_intent": int(other.sum()), "n_trades": 0, "net_pnl": 0.0}
        pick = out_l if (out_l.get("n_trades") or 0) >= (out_m.get("n_trades") or 0) else out_m
        pick = dict(pick)
        pick["regime_market"] = {k: out_m.get(k) for k in ("status", "n_trades", "profit_factor", "n_intent")}
        pick["regime_limit"] = {k: out_l.get(k) for k in ("status", "n_trades", "profit_factor", "n_intent")}
        pick["pi_star"] = pi_star
        return pick

    p_te = ctx.head(h, spec["event"])
    p_sc = _map_to_sc(sc, ctx.test_df.index, p_te)
    gated = np.isfinite(p_sc) & (p_sc >= pi_star) & ctx.in_test

    if spec["mode"] == "one_head_filter_pi_star":
        mask = gated & ctx.ctrl_mask
        is_s, lim = _pivot_side_lim(ctx, mask)
        out = run_limit_arm(
            symbol, sc, mask, is_s, lim, tag=tag, work=work, max_hold=max_hold, tp=tp, sl=sl
        )
        out["pi_star"] = pi_star
        out["family"] = _family(spec["event"])
        return out

    # standalone
    feat = ctx.test_feat() if h == 4 else ctx.pack(h, False).features
    side_te = _known_now_side(spec["event"], feat)
    side_sc = _map_to_sc(sc, ctx.test_df.index, side_te)
    mask = gated & np.isfinite(side_sc) & (side_sc != 0)
    is_short = (side_sc < 0)[np.flatnonzero(mask)]
    market = spec["event"] in MARKET_ENTRY_EVENTS
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
    out["family"] = _family(spec["event"])
    out["entry"] = "market" if market else "limit"
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-arms", type=int, default=0, help="0 = full closed grid")
    ap.add_argument("--skip-leakage", action="store_true")
    args = ap.parse_args()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    prereg_sha = _sha(PREREG)
    text = PREREG.read_text(encoding="utf-8")
    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(text.rstrip() + f"\n\npreregister_sha256_at_run: {prereg_sha}\n", encoding="utf-8")
    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    _ = cfg
    DB_DIR.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB_DIR / "hunt.sqlite")
    append_ledger(f"CONFLUENCE_AUTONOMOUS_HUNT_002 start {stamp}", tier=0)
    print(f"preregister_sha256={prereg_sha}", flush=True)

    leak = []
    if not args.skip_leakage:
        for symbol in SYMBOLS_15M:
            rec = _leak(symbol, "15m")
            leak.append(rec)
            print("leakage", rec, flush=True)
            if rec["status"] != "PASS":
                raise SystemExit(f"leakage FAIL {rec}")

    specs = _iter_specs()
    if args.max_arms and args.max_arms > 0:
        specs = specs[: args.max_arms]
    print(f"planned_arms={len(specs)} already_done={sum(1 for s in specs if arm_done(con, _arm_id(s)))}", flush=True)

    ctxs: dict[tuple[str, str], _Ctx] = {}
    ran = 0
    for i, spec in enumerate(specs, start=1):
        aid = _arm_id(spec)
        if arm_done(con, aid):
            continue
        key = (spec["symbol"], spec["timeframe"])
        if key not in ctxs:
            max_rows = 120_000 if spec["timeframe"] == "15m" else 40_000
            print(f"=== context {key} ===", flush=True)
            ctxs[key] = _Ctx(spec["symbol"], spec["timeframe"], max_rows)
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
                "tp": spec["tp"],
                "sl": spec["sl"],
                "gate": spec["gate"],
                "phase": spec["phase"],
                "arm_id": aid,
            }
        )
        save_arm(con, aid, spec, payload)
        ran += 1
        print(
            f"  {payload.get('status')} n={payload.get('n_trades')} PF={payload.get('profit_factor')} "
            f"WR={payload.get('win_rate')} Sharpe={payload.get('sharpe_annualised')}",
            flush=True,
        )
        if ran % 3 == 0 or payload.get("status") == "ERROR":
            _write_leaderboard(con, stamp, {"leakage": leak, "preregister_sha256": prereg_sha})

    _write_leaderboard(con, stamp, {"leakage": leak, "preregister_sha256": prereg_sha})
    append_ledger(f"CONFLUENCE_AUTONOMOUS_HUNT_002 checkpoint arms={ran} path={OUT / 'autonomous_hunt_002_latest.md'}", tier=0)
    print(f"WROTE {OUT / 'autonomous_hunt_002_latest.md'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
