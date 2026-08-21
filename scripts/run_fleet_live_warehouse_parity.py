"""Fleet-wide live vs warehouse parity for all llm2 structure units.

Runs per host (ln1 / ln3), per active unit:
  - shared/research candle tip for the unit's symbol
  - latest N decisions from micro_live_state
  - model replay from feature_snapshot
  - warehouse build_space recompute of pred_mean/side
  - pack 1h depth gate
  - strength_hist length when multitrade

Usage:
  python scripts/run_fleet_live_warehouse_parity.py
  python scripts/run_fleet_live_warehouse_parity.py --hosts 185.203.119.52,94.156.189.76 --n 8
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

os.environ.setdefault("LLM2_INDICATORS_DB", r"D:\projectsdata\indicators\indicators.sqlite")
os.environ.setdefault("LLM2_STRUCTURE_SOURCE", "binance")

from llm2.data.indicators import clear_indicator_cache  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.paths import ARTIFACTS, ROUND_TRIP_COST  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

DEFAULT_HOSTS = ("185.203.119.52", "94.156.189.76")
OUT = ARTIFACTS / "reports" / "fleet_live_warehouse_parity_latest.json"
MIN_1H_BARS = 5000
ABS_EPS = 1e-6
FEAT_EPS = 1e-9
STEP_1H = 3_600_000

# Unit name fragment → preferred local pack directory under artifacts/live_packs
PACK_HINTS: list[tuple[str, str]] = [
    # Longer / more specific fragments first.
    ("eth-15m-multitrade-wall-clock-p75", "structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1"),
    ("eth-multitrade-p75", "structure_v1_ethusdt_multitrade_p75_v1"),
    ("eth-multitrade-v1_2", "structure_v1_ethusdt_multitrade_v1_2"),
    ("eth-multitrade-v1-2", "structure_v1_ethusdt_multitrade_v1_2"),
    ("eth-multitrade-v1_1", "structure_v1_ethusdt_multitrade_v1_1"),
    ("eth-k5-double3h-p75", "structure_v1_ethusdt_k5_double3h_p75_v1"),
    ("eth-k5-double3h", "structure_v1_ethusdt_k5_double3h_v1"),
    ("btc-k5-double3h", "structure_v1_btcusdt_k5_double3h_v1"),
    ("sol-k5-double3h", "structure_v1_solusdt_k5_double3h_v1"),
    ("llm2-structure-eth", "structure_v1_ethusdt_direction"),
    ("llm2-structure-sol", "structure_v1_solusdt_direction"),
    ("llm2-structure-micro", "structure_v1_lgbm"),  # BTC single-book pack name historically
]
TF_MS_MAP = {
    "1m": 60_000,
    "5m": 300_000,
    "15m": 900_000,
    "1h": 3_600_000,
    "4h": 14_400_000,
    "1d": 86_400_000,
    "1w": 604_800_000,
}
MIN_BARS_BY_TF = {"15m": 5_000, "1h": 5_000, "4h": 2_000, "1w": 200}


def _ssh(host: str, cmd: str) -> str:
    return subprocess.check_output(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=35", f"root@{host}", cmd],
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def list_active_units(host: str) -> list[str]:
    raw = _ssh(
        host,
        "systemctl list-units --type=service --state=running --no-legend 'llm2-structure*' "
        "| awk '{print $1}'",
    )
    units = []
    for ln in raw.splitlines():
        name = ln.strip()
        if not name or "refresh" in name:
            continue
        if name.endswith(".service"):
            name = name[: -len(".service")]
        if name.startswith("llm2-structure"):
            units.append(name)
    return sorted(set(units))


def unit_working_dir(host: str, unit: str) -> str:
    wd = _ssh(host, f"systemctl show {unit}.service -p WorkingDirectory --value").strip()
    if not wd:
        # convention
        wd = f"/opt/{unit}"
    return wd


def scp_ledger(host: str, remote_state: Path, local: Path) -> bool:
    try:
        subprocess.check_call(
            [
                "scp",
                "-o",
                "BatchMode=yes",
                "-o",
                "ConnectTimeout=35",
                f"root@{host}:{remote_state.as_posix()}",
                str(local),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return local.is_file() and local.stat().st_size > 0
    except subprocess.CalledProcessError:
        return False


def remote_pack_meta(host: str, root: str) -> dict:
    script = f"""
import json, sqlite3
from pathlib import Path
root = Path({root!r})
out = {{"root": str(root), "symbol": None, "timeframe": "1h", "version_id": None,
       "execution_mode": None, "binance_1h_n": None, "binance_decision_tf_n": None,
       "pack_ok": False, "series": {{}}}}
strat = root / "pack" / "strategy.json"
if strat.is_file():
    s = json.loads(strat.read_text(encoding="utf-8"))
    out["symbol"] = s.get("symbol")
    out["timeframe"] = s.get("timeframe") or "1h"
    out["version_id"] = s.get("version_id")
    out["execution_mode"] = s.get("execution_mode")
    out["pack_ok"] = (root / "pack" / "model.joblib").is_file()
ind = root / "pack" / "indicators_live_slice.sqlite"
if ind.is_file():
    con = sqlite3.connect(f"file:{{ind}}?mode=ro", uri=True)
    try:
        tf = out["timeframe"]
        for tfx in sorted({{tf, "1h", "4h", "1w", "15m"}}):
            row = con.execute(
                "SELECT COUNT(*) FROM bar_features WHERE source='binance' AND timeframe=?",
                (tfx,),
            ).fetchone()
            out["series"][tfx] = int(row[0]) if row else 0
        out["binance_1h_n"] = out["series"].get("1h")
        out["binance_decision_tf_n"] = out["series"].get(tf)
        mx = con.execute(
            "SELECT MAX(ts_ms) FROM bar_features WHERE source='binance' AND timeframe=?",
            (tf,),
        ).fetchone()
        out["binance_decision_tf_max_ts"] = int(mx[0]) if mx and mx[0] else None
        mx1 = con.execute(
            "SELECT MAX(ts_ms) FROM bar_features WHERE source='binance' AND timeframe='1h'"
        ).fetchone()
        out["binance_1h_max_ts"] = int(mx1[0]) if mx1 and mx1[0] else None
    except Exception as e:
        out["ind_error"] = str(e)
    finally:
        con.close()
print(json.dumps(out))
"""
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8", newline="\n") as fh:
        fh.write(script)
        path = fh.name
    try:
        subprocess.check_call(
            ["scp", "-o", "BatchMode=yes", path, f"root@{host}:/tmp/_fleet_pack_meta.py"],
            stdout=subprocess.DEVNULL,
        )
        raw = _ssh(
            host,
            f"sed -i 's/\\r$//' /tmp/_fleet_pack_meta.py; "
            f"{root}/venv/bin/python /tmp/_fleet_pack_meta.py 2>/dev/null || python3 /tmp/_fleet_pack_meta.py",
        )
    finally:
        Path(path).unlink(missing_ok=True)
    lines = [ln for ln in raw.splitlines() if ln.strip().startswith("{")]
    if not lines:
        return {"root": root, "error": raw[-400:]}
    return json.loads(lines[-1])


def resolve_local_pack(unit: str, symbol: str | None) -> Path | None:
    u = unit.lower()
    for frag, pack_name in PACK_HINTS:
        if frag in u:
            p = ARTIFACTS / "live_packs" / pack_name
            if p.is_dir() and (p / "model.joblib").is_file():
                return p
    # symbol fallback
    if symbol:
        cand = ARTIFACTS / "live_packs" / f"structure_v1_{symbol.lower()}_direction"
        if cand.is_dir() and (cand / "model.joblib").is_file():
            return cand
    return None


def warehouse_tip(symbol: str, timeframe: str = "1h") -> dict:
    ohlcv = load_ohlcv(symbol, timeframe)
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    step = int(TF_MS_MAP.get(timeframe, STEP_1H))
    if "ts_ms" in ohlcv.columns:
        ts = ohlcv["ts_ms"].astype(np.int64).to_numpy()
    else:
        ts = index_to_ms(ohlcv.index)
    closed = ohlcv.loc[ts + step <= now_ms]
    if closed.empty:
        return {"error": "no_closed_bars", "timeframe": timeframe}
    last = closed.iloc[-1]
    last_ts = int(ts[ts + step <= now_ms][-1])
    tip50 = closed.iloc[-50:]
    t50 = (
        tip50["ts_ms"].astype(np.int64).to_numpy()
        if "ts_ms" in tip50.columns
        else index_to_ms(tip50.index)
    )
    blob = "".join(
        f"{int(t)}|{float(o)}|{float(h)}|{float(l)}|{float(c)}\n"
        for t, o, h, l, c in zip(
            t50,
            tip50["open"].to_numpy(float),
            tip50["high"].to_numpy(float),
            tip50["low"].to_numpy(float),
            tip50["close"].to_numpy(float),
        )
    ).encode()
    return {
        "timeframe": timeframe,
        "tip_ts_ms": last_ts,
        "tip_ohlc": [float(last["open"]), float(last["high"]), float(last["low"]), float(last["close"])],
        "tip50_sha256": hashlib.sha256(blob).hexdigest(),
        "n_closed": int(len(closed)),
    }


def shared_tip(host: str, symbol: str, timeframe: str = "1h") -> dict:
    step = int(TF_MS_MAP.get(timeframe, STEP_1H))
    script = f"""
import json, sqlite3, time, hashlib
now=int(time.time()*1000); step={step}
con=sqlite3.connect('/var/lib/botsgeneral/shared_candles.db')
rows=con.execute(
  "SELECT ts_ms,open,high,low,close FROM candles WHERE exchange='binance' "
  "AND symbol=? AND timeframe=? ORDER BY ts_ms",
  ({symbol!r}, {timeframe!r})
).fetchall()
closed=[r for r in rows if r[0]+step<=now]
if not closed:
  print(json.dumps({{'error':'no_closed','timeframe':{timeframe!r}}})); raise SystemExit(0)
tip=closed[-1]; tip50=closed[-50:]
blob=''.join(f'{{r[0]}}|{{r[1]}}|{{r[2]}}|{{r[3]}}|{{r[4]}}\\n' for r in tip50).encode()
print(json.dumps({{
  'timeframe': {timeframe!r},
  'tip_ts_ms': tip[0],
  'tip_ohlc': [float(x) for x in tip[1:]],
  'tip50_sha256': hashlib.sha256(blob).hexdigest(),
  'n_closed': len(closed),
}}))
"""
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8", newline="\n") as fh:
        fh.write(script)
        path = fh.name
    try:
        subprocess.check_call(
            ["scp", "-o", "BatchMode=yes", path, f"root@{host}:/tmp/_fleet_shared_tip.py"],
            stdout=subprocess.DEVNULL,
        )
        raw = _ssh(host, "sed -i 's/\\r$//' /tmp/_fleet_shared_tip.py; python3 /tmp/_fleet_shared_tip.py")
    finally:
        Path(path).unlink(missing_ok=True)
    lines = [ln for ln in raw.splitlines() if ln.strip().startswith("{")]
    return json.loads(lines[-1]) if lines else {"error": raw[-200:]}


_feat_cache: dict[tuple[str, str, tuple[str, ...]], tuple] = {}


def warehouse_features(symbol: str, timeframe: str, cols: list[str]):
    key = (symbol, timeframe, tuple(cols))
    if key in _feat_cache:
        return _feat_cache[key]
    clear_indicator_cache()
    ohlcv = load_ohlcv(symbol, timeframe)
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    feats = build_space(
        ohlcv, "structure_v1", symbol=symbol, timeframe=timeframe, recent_only=False
    )
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    for c in feats.columns:
        if str(c).startswith("last_retrace_pct_"):
            feats[c] = feats[c].fillna(0.0)
    aligned = feats.dropna()
    feat_ts = index_to_ms(pd.DatetimeIndex(aligned.index))
    X = aligned.to_numpy(dtype=float)
    _feat_cache[key] = (aligned, feat_ts, X)
    return _feat_cache[key]


def audit_unit(host: str, unit: str, *, n_decisions: int) -> dict:
    wd = unit_working_dir(host, unit)
    meta = remote_pack_meta(host, wd)
    symbol = str(meta.get("symbol") or "").upper() or None
    timeframe = str(meta.get("timeframe") or "1h")
    local_pack = resolve_local_pack(unit, symbol)
    out: dict = {
        "host": host,
        "unit": unit,
        "working_directory": wd,
        "remote_meta": meta,
        "local_pack": str(local_pack) if local_pack else None,
        "symbol": symbol,
        "timeframe": timeframe,
    }
    if not symbol:
        out["status"] = "SKIP_NO_SYMBOL"
        return out
    if not local_pack:
        out["status"] = "SKIP_NO_LOCAL_PACK"
        return out

    # candles (decision timeframe — 15m units must not be scored on 1h tip)
    shared = shared_tip(host, symbol, timeframe)
    wh = warehouse_tip(symbol, timeframe)
    out["candles"] = {
        "shared": shared,
        "warehouse": wh,
        "ok": (
            not shared.get("error")
            and not wh.get("error")
            and shared.get("tip_ts_ms") == wh.get("tip_ts_ms")
            and shared.get("tip_ohlc") == wh.get("tip_ohlc")
            and shared.get("tip50_sha256") == wh.get("tip50_sha256")
        ),
    }
    need = int(MIN_BARS_BY_TF.get(timeframe, MIN_1H_BARS))
    n_dec = meta.get("binance_decision_tf_n")
    if n_dec is None:
        n_dec = meta.get("binance_1h_n")
    series = meta.get("series") or {}
    # 15m structure needs HTF 1h+4h in the pack slice
    htf_ok = True
    if timeframe == "15m":
        htf_ok = int(series.get("1h") or 0) >= MIN_BARS_BY_TF["1h"] and int(
            series.get("4h") or 0
        ) >= MIN_BARS_BY_TF["4h"]
    out["pack_depth"] = {
        "decision_tf": timeframe,
        "binance_decision_tf_n": n_dec,
        "binance_1h_n": meta.get("binance_1h_n"),
        "series": series,
        "deep_ok": isinstance(n_dec, int) and int(n_dec) >= need and htf_ok,
        "htf_ok": htf_ok,
    }

    # ledger
    local_ledger = (
        ARTIFACTS
        / "reports"
        / "_fleet_ledgers"
        / f"{host.replace('.', '_')}_{unit}_state.sqlite"
    )
    local_ledger.parent.mkdir(parents=True, exist_ok=True)
    ledgers = [
        Path(wd) / "state" / "micro_live_state.sqlite",
        Path(wd) / "artifacts" / "live_ledger.sqlite",
    ]
    got = False
    for rem in ledgers:
        if scp_ledger(host, rem, local_ledger):
            got = True
            out["ledger_remote"] = str(rem)
            break
    if not got:
        out["status"] = "NO_LEDGER"
        return out

    strategy = json.loads((local_pack / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(local_pack / "model.joblib")
    cols = list(blob.get("feature_columns") or strategy.get("feature_columns") or [])
    # Match micro_runner._decide: return→ROUND_TRIP_COST band; direction→±0.10.
    # Never remap min_edge on return/fwd_return packs (was forcing BTC through 0.10 → side_match=0).
    target = str(strategy.get("target") or "fwd_return")
    family = target_family(target)
    default_edge = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    edge = float(strategy.get("min_edge", default_edge))
    if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
        edge = DIRECTION_BAND
    lookback = int((strategy.get("multitrade") or {}).get("mean_lookback") or 168)
    out["side_gate"] = {
        "target": target,
        "family": family,
        "edge": edge,
        "proxy_band": DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST,
    }

    con = sqlite3.connect(f"file:{local_ledger}?mode=ro", uri=True)
    try:
        tables = {
            r[0]
            for r in con.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        }
        if "decisions" not in tables:
            out["status"] = "NO_DECISIONS_TABLE"
            return out
        rows = con.execute(
            "SELECT bar_ts_ms, decided_utc, side, pred_mean, detail "
            "FROM decisions ORDER BY bar_ts_ms DESC LIMIT ?",
            (int(n_decisions),),
        ).fetchall()
        states = {}
        if "state" in tables:
            states = dict(con.execute("SELECT key, value FROM state").fetchall())
    finally:
        con.close()

    try:
        strength = [float(x) for x in json.loads(states.get("strength_hist_json") or "[]")]
    except Exception:
        strength = []
    out["strength_hist"] = {
        "n": len(strength),
        "target": lookback if (strategy.get("multitrade") or strategy.get("execution_mode") == "multitrade") else None,
    }

    aligned, feat_ts, X = warehouse_features(symbol, timeframe, cols)
    ts_to_i = {int(t): i for i, t in enumerate(feat_ts)}
    pred_raw = blob["model"].predict(X)
    means = np.asarray(
        pred_raw.mean if hasattr(pred_raw, "mean") else pred_raw, dtype=float
    ).reshape(-1)

    comparisons = []
    snap_ok = 0
    snap_n = 0
    scored = 0
    side_ok = 0
    pred_ok = 0
    for bar_ts_ms, decided_utc, side, pred_mean, detail in reversed(rows):
        try:
            det = json.loads(detail) if isinstance(detail, str) else (detail or {})
        except Exception:
            det = {}
        snap = (det.get("feature_snapshot") or {}).get("values")
        live_pred = float(pred_mean) if pred_mean is not None else float("nan")
        live_side = int(side) if side is not None else None
        snap_replay = None
        if snap:
            snap_n += 1
            Xs = np.array([[float(snap[c]) for c in cols]], dtype=float)
            pr = blob["model"].predict(Xs)
            m = float(np.asarray(pr.mean if hasattr(pr, "mean") else pr).reshape(-1)[0])
            d = abs(m - live_pred) if np.isfinite(live_pred) else float("nan")
            snap_replay = {
                "ok": bool(np.isfinite(d) and d < ABS_EPS),
                "abs_diff": d if np.isfinite(d) else None,
            }
            if snap_replay["ok"]:
                snap_ok += 1

        i = ts_to_i.get(int(bar_ts_ms))
        row: dict = {
            "bar_ts_ms": int(bar_ts_ms),
            "bar_utc": pd.to_datetime(int(bar_ts_ms), unit="ms", utc=True).isoformat(),
            "live_pred_mean": live_pred if np.isfinite(live_pred) else None,
            "live_side": live_side,
            "skip_reason": det.get("skip_reason")
            or (det.get("multitrade_gate") or {}).get("skip_reason"),
            "snapshot_model_ok": (snap_replay or {}).get("ok"),
        }
        if i is None:
            row["error"] = "bar_missing_in_warehouse_feats"
            comparisons.append(row)
            continue
        wh_mean = float(means[i])
        # Live decide uses proxy_side only (fee/`DIRECTION_BAND` inside proxy_side).
        wh_side = int(proxy_side(np.asarray([wh_mean]), family)[0])
        live_side_from_pred = (
            int(proxy_side(np.asarray([live_pred]), family)[0])
            if np.isfinite(live_pred)
            else None
        )
        abs_diff = abs(wh_mean - live_pred) if np.isfinite(live_pred) else float("nan")
        row.update(
            {
                "warehouse_pred_mean": wh_mean,
                "warehouse_side": wh_side,
                "live_side_from_pred": live_side_from_pred,
                "live_side_matches_proxy": (
                    live_side is not None and live_side_from_pred == live_side
                ),
                "abs_diff": abs_diff if np.isfinite(abs_diff) else None,
                "pred_match": bool(np.isfinite(abs_diff) and abs_diff < ABS_EPS),
                "side_match": live_side == wh_side,
            }
        )
        if np.isfinite(live_pred):
            scored += 1
            if live_side == wh_side:
                side_ok += 1
            if np.isfinite(abs_diff) and abs_diff < ABS_EPS:
                pred_ok += 1
        comparisons.append(row)

    out["comparisons"] = comparisons
    out["headline"] = {
        "n_decisions": len(comparisons),
        "n_scored": scored,
        "side_match_rate": (side_ok / scored) if scored else None,
        "pred_exact_rate": (pred_ok / scored) if scored else None,
        "snapshot_model_ok_rate": (snap_ok / snap_n) if snap_n else None,
        "max_abs_pred_diff": max(
            (
                float(c["abs_diff"])
                for c in comparisons
                if c.get("abs_diff") is not None
            ),
            default=None,
        ),
    }
    deep_ok = out["pack_depth"]["deep_ok"]
    candles_ok = out["candles"]["ok"]
    model_ok = out["headline"]["snapshot_model_ok_rate"] in (None, 1.0) or (
        out["headline"]["snapshot_model_ok_rate"] or 0
    ) >= 0.99
    structure_ok = (
        scored == 0
        or (
            (out["headline"]["side_match_rate"] or 0) >= 0.99
            and (out["headline"]["pred_exact_rate"] or 0) >= 0.5
        )
    )
    if deep_ok and candles_ok and model_ok and structure_ok and scored > 0 and (
        out["headline"]["pred_exact_rate"] or 0
    ) >= 0.99:
        out["status"] = "PASS"
    elif deep_ok and candles_ok and model_ok and scored > 0:
        out["status"] = "PARTIAL_TIP_DRIFT"
    elif deep_ok and model_ok:
        out["status"] = "OK_STRUCT_NO_OR_PARTIAL_SCORED"
    else:
        out["status"] = "FAIL"
    return out


def maybe_refresh_indicators(symbols: set[str]) -> list[dict]:
    """Extend research OHLCV tip then bar_features for symbols under test (1h/4h/1w)."""
    sys.path.insert(0, r"C:\projects\botsgeneral\packages\indicators\src")
    results: list[dict] = []
    try:
        from indicators.candles import refresh_candles
        from indicators.update import update_series
    except Exception as exc:  # noqa: BLE001
        return [{"error": f"indicators import failed: {exc}"}]
    try:
        refresh_candles(symbols=sorted(symbols), timeframes=["1h", "4h", "1w"])
        results.append({"step": "refresh_candles", "symbols": sorted(symbols), "ok": True})
    except Exception as exc:  # noqa: BLE001
        results.append(
            {"step": "refresh_candles", "ok": False, "error": f"{type(exc).__name__}: {exc}"}
        )
    for sym in sorted(symbols):
        for tf in ("1h", "4h", "1w"):
            try:
                r = update_series(sym, tf, source="binance")
                results.append(
                    {
                        "symbol": sym,
                        "timeframe": tf,
                        "n_bars": r.n_bars,
                        "error": r.error or None,
                    }
                )
            except Exception as exc:  # noqa: BLE001
                results.append({"symbol": sym, "timeframe": tf, "error": str(exc)})
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--hosts", default=",".join(DEFAULT_HOSTS))
    ap.add_argument("--n", type=int, default=8, help="max decisions per unit")
    ap.add_argument("--skip-indicator-refresh", action="store_true")
    ap.add_argument("--units-filter", default="", help="comma substrings; empty=all")
    args = ap.parse_args(argv)

    hosts = [h.strip() for h in args.hosts.split(",") if h.strip()]
    filters = [f.strip().lower() for f in args.units_filter.split(",") if f.strip()]

    # discover units first
    plan: list[tuple[str, str]] = []
    for host in hosts:
        try:
            units = list_active_units(host)
        except Exception as exc:  # noqa: BLE001
            print(f"HOST_FAIL {host}: {exc}", flush=True)
            continue
        for u in units:
            if filters and not any(f in u.lower() for f in filters):
                continue
            plan.append((host, u))

    symbols_needed: set[str] = set()
    # pre-resolve symbols via remote strategy when possible is expensive; use unit hints
    for _, u in plan:
        lu = u.lower()
        if "btc" in lu or u.endswith("-micro") or "structure-micro" in lu:
            symbols_needed.add("BTCUSDT")
        if "eth" in lu:
            symbols_needed.add("ETHUSDT")
        if "sol" in lu:
            symbols_needed.add("SOLUSDT")

    refresh_log = []
    if not args.skip_indicator_refresh and symbols_needed:
        print(f"refresh research indicators: {sorted(symbols_needed)}", flush=True)
        refresh_log = maybe_refresh_indicators(symbols_needed)

    results = []
    for host, unit in plan:
        print(f"=== {host} {unit} ===", flush=True)
        try:
            row = audit_unit(host, unit, n_decisions=int(args.n))
        except Exception as exc:  # noqa: BLE001
            row = {"host": host, "unit": unit, "status": "ERROR", "error": str(exc)}
        results.append(row)
        h = row.get("headline") or {}
        print(
            f"  status={row.get('status')} symbol={row.get('symbol')} "
            f"scored={h.get('n_scored')} pred_rate={h.get('pred_exact_rate')} "
            f"side_rate={h.get('side_match_rate')} snap={h.get('snapshot_model_ok_rate')} "
            f"candles={((row.get('candles') or {}).get('ok'))} "
            f"depth={((row.get('pack_depth') or {}).get('binance_1h_n'))}",
            flush=True,
        )

    summary = {
        "n_units": len(results),
        "by_status": {},
        "pass": [],
        "partial": [],
        "fail": [],
    }
    for r in results:
        st = str(r.get("status") or "UNKNOWN")
        summary["by_status"][st] = summary["by_status"].get(st, 0) + 1
        key = f"{r.get('host')}:{r.get('unit')}"
        if st == "PASS":
            summary["pass"].append(key)
        elif "PARTIAL" in st or "OK_STRUCT" in st:
            summary["partial"].append(key)
        elif st not in {"SKIP_NO_SYMBOL", "SKIP_NO_LOCAL_PACK"}:
            summary["fail"].append(key)

    report = {
        "evidence_class": "FLEET_LIVE_WAREHOUSE_PARITY",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "hosts": hosts,
        "indicator_refresh": refresh_log,
        "summary": summary,
        "units": results,
        "note": (
            "Diagnostic. Model snapshot exactness is the hard model integrity check. "
            "Warehouse tip pred residual can remain after full_history live structure "
            "if research indicators lag; tip candes compared shared vs research OHLCV. "
            "Do not retune knobs from fleet partials."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (ARTIFACTS / "reports" / f"fleet_live_warehouse_parity_{stamp}.json").write_text(
        json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2), flush=True)
    print(f"wrote {OUT}", flush=True)
    fails = summary["by_status"].get("FAIL", 0) + summary["by_status"].get("ERROR", 0)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
