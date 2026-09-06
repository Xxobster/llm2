"""Indicator-regime hunt 003: Supertrend / Ichimoku / CCI one-head filters.

RESEARCH_ONLY. Rank on chronological test window before lockbox only.
1%/1% bracket only. Resumes from artifacts/sqlite/confluence_indicator_regime_003/.
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
from sklearn.ensemble import HistGradientBoostingRegressor

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

from llm2.confluence.events import (  # noqa: E402
    EVENT_IDS_003,
    LONG_EVENTS,
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
    save_arm,
)
from llm2.confluence.train import (  # noqa: E402
    FEATURE_COLS,
    chronological_cut_index,
    fit_one_head,
    split_ohlcv_files,
)
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

PREREG = _ROOT / "configs" / "preregister" / "confluence_indicator_regime_003.yaml"
PACK = "level_vsa"
OUT = ARTIFACTS / "reports" / "confluence"
DB_DIR = ARTIFACTS / "sqlite" / "confluence_indicator_regime_003"
CACHE = DB_DIR / "cache"
SYMBOLS_15M = ("ETHUSDT", "SOLUSDT", "BTCUSDT")
WORK_CTRL = {"ETHUSDT": 4, "SOLUSDT": 5, "BTCUSDT": 4}
HORIZONS = (4, 8)
TP_SL = (0.01, 0.01)


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
    if event in LONG_EVENTS or event in SHORT_EVENTS:
        if "cci_" in event:
            return "reversal"
        return "continuation"
    return "other"


def _level_mse_diag(train_df: pd.DataFrame, test_df: pd.DataFrame, *, horizon: int = 4) -> dict:
    """Diagnostic only: future RSI / CCI level forecast MSE. Never used to rank arms."""
    tr = build_event_pack(train_df, horizon=horizon, include_003=True)
    te = build_event_pack(test_df, horizon=horizon, include_003=True)
    out: dict = {"horizon": horizon, "note": "diagnostic_only_not_for_selection"}
    for col in ("rsi_14", "cci_20"):
        y_tr = tr.features[col].to_numpy(dtype=float).copy()
        y_te = te.features[col].to_numpy(dtype=float).copy()
        # Target = value at t+H
        fut_tr = np.full_like(y_tr, np.nan)
        fut_te = np.full_like(y_te, np.nan)
        if len(y_tr) > horizon:
            fut_tr[: -horizon] = y_tr[horizon:]
        if len(y_te) > horizon:
            fut_te[: -horizon] = y_te[horizon:]
        x_tr = tr.features[list(FEATURE_COLS)].to_numpy(dtype=float)
        x_te = te.features[list(FEATURE_COLS)].to_numpy(dtype=float)
        ok_tr = np.isfinite(fut_tr) & np.isfinite(x_tr).all(axis=1)
        ok_te = np.isfinite(fut_te) & np.isfinite(x_te).all(axis=1)
        if ok_tr.sum() < 200 or ok_te.sum() < 50:
            out[f"mse_{col}_persistence"] = None
            out[f"mse_{col}_hgb"] = None
            continue
        persist = y_te[ok_te]
        mse_p = float(np.mean((persist - fut_te[ok_te]) ** 2))
        model = HistGradientBoostingRegressor(max_depth=4, max_iter=120, random_state=20260821)
        model.fit(x_tr[ok_tr], fut_tr[ok_tr])
        pred = model.predict(x_te[ok_te])
        mse_m = float(np.mean((pred - fut_te[ok_te]) ** 2))
        out[f"mse_{col}_persistence"] = mse_p
        out[f"mse_{col}_hgb"] = mse_m
    return out


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
        "generation_id": "confluence_indicator_regime_003",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "promoted": None,
        "not_live": True,
        "n_arms": len(rows),
        "extra": extra,
        "arms": rows,
    }
    (OUT / "indicator_regime_003_latest.json").write_text(
        json.dumps(jsonable(latest), indent=2), encoding="utf-8"
    )
    md = [
        "# Indicator-regime hunt 003",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`. Arms: {len(rows)}.",
        "**Promoted: none** unless a filter arm clears frozen gates (this file does not auto-promote).",
        "Rank window: chronological test (last 30% before lockbox). 1%/1% only. Do not quote as live.",
        "",
        "| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | HAC Sharpe | exp_i | ebr | flag | status |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
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
            "| {symbol} | {h} | `{ev}` | {mode} | {n} | {tpm} | {pf} | {wr} | {sh} | {hac} | {ex} | {ebr} | {flag} | {st} |".format(
                symbol=r.get("symbol"),
                h=r.get("horizon"),
                ev=r.get("event"),
                mode=r.get("mode"),
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
    (OUT / "indicator_regime_003_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    flagged = [
        r
        for r in rows
        if r.get("status") == "RAN"
        and (r.get("n_trades") or 0) >= 50
        and (r.get("entry_bar_exit_rate") or 1) <= 0.35
        and r.get("mode") != "control"
    ]
    (OUT / "indicator_regime_003_flagged.json").write_text(
        json.dumps(jsonable({"n": len(flagged), "arms": flagged[:40]}), indent=2),
        encoding="utf-8",
    )


def _iter_specs() -> list[dict]:
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
            for event in EVENT_IDS_003:
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
    def __init__(self, symbol: str, tf: str, max_rows: int):
        self.symbol = symbol
        self.tf = tf
        self.max_rows = max_rows
        self.ohlcv = _load_pre_lock(symbol, tf, max_rows)
        self.sc = _score_cached(symbol, tf, max_rows)
        self.ctrl_mask, self.level_override = _imp001._control_mask(symbol, self.sc)
        self.work_ctrl = WORK_CTRL[symbol]
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
        self.level_diag: dict | None = None

    def pack(self, horizon: int, train: bool):
        store = self.packs_tr if train else self.packs_te
        if horizon not in store:
            df = self.train_df if train else self.test_df
            print(f"  event pack {self.symbol} {self.tf} H={horizon} train={train}", flush=True)
            store[horizon] = build_event_pack(df, horizon=horizon, include_003=True)
        return store[horizon]

    def head(self, horizon: int, event: str) -> np.ndarray:
        key = (horizon, event)
        if key not in self.heads:
            tr = self.pack(horizon, True)
            te = self.pack(horizon, False)
            print(f"  fit head {self.symbol} {event} H={horizon}", flush=True)
            self.heads[key] = fit_one_head(tr, te, event)
        return np.asarray(self.heads[key]["p_test"], dtype=float)

    def diag(self) -> dict:
        if self.level_diag is None:
            print(f"  level-MSE diagnostic {self.symbol} (not for selection)", flush=True)
            self.level_diag = _level_mse_diag(self.train_df, self.test_df, horizon=4)
        return self.level_diag


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
    max_hold = 6
    work = ctx.work_ctrl
    tag = _arm_id(spec)
    mag = net_bracket_magnitudes(tp, sl)
    pi_star = float(mag.pi_star)
    sc = ctx.sc

    if spec["mode"] == "control":
        mask = ctx.ctrl_mask & ctx.in_test
        is_s, lim = _pivot_side_lim(ctx, mask)
        out = run_limit_arm(
            symbol, sc, mask, is_s, lim, tag=tag, work=work, max_hold=max_hold, tp=tp, sl=sl
        )
        out["pi_star"] = pi_star
        return out

    p_te = ctx.head(h, spec["event"])
    p_sc = _map_to_sc(sc, ctx.test_df.index, p_te)
    gated = np.isfinite(p_sc) & (p_sc >= pi_star) & ctx.in_test
    mask = gated & ctx.ctrl_mask
    is_s, lim = _pivot_side_lim(ctx, mask)
    out = run_limit_arm(
        symbol, sc, mask, is_s, lim, tag=tag, work=work, max_hold=max_hold, tp=tp, sl=sl
    )
    out["pi_star"] = pi_star
    out["family"] = _family(spec["event"])
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
        PREREG.write_text(
            text.rstrip() + f"\n\npreregister_sha256_at_run: {prereg_sha}\n", encoding="utf-8"
        )
    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    _ = cfg
    DB_DIR.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB_DIR / "hunt.sqlite")
    append_ledger(f"CONFLUENCE_INDICATOR_REGIME_003 start {stamp}", tier=0)
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
    print(
        f"planned_arms={len(specs)} already_done={sum(1 for s in specs if arm_done(con, _arm_id(s)))}",
        flush=True,
    )

    ctxs: dict[tuple[str, str], _Ctx] = {}
    level_diags: dict[str, dict] = {}
    ran = 0
    for i, spec in enumerate(specs, start=1):
        aid = _arm_id(spec)
        if arm_done(con, aid):
            continue
        key = (spec["symbol"], spec["timeframe"])
        if key not in ctxs:
            print(f"=== context {key} ===", flush=True)
            ctxs[key] = _Ctx(spec["symbol"], spec["timeframe"], 120_000)
            level_diags[spec["symbol"]] = ctxs[key].diag()
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
            _write_leaderboard(
                con,
                stamp,
                {
                    "leakage": leak,
                    "preregister_sha256": prereg_sha,
                    "level_mse_diagnostic": level_diags,
                },
            )

    _write_leaderboard(
        con,
        stamp,
        {
            "leakage": leak,
            "preregister_sha256": prereg_sha,
            "level_mse_diagnostic": level_diags,
        },
    )
    append_ledger(
        f"CONFLUENCE_INDICATOR_REGIME_003 done arms={ran} "
        f"path={OUT / 'indicator_regime_003_latest.md'} promoted=none",
        tier=0,
    )
    print(f"WROTE {OUT / 'indicator_regime_003_latest.md'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
