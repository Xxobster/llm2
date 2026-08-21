"""Layer C — live Bybit fill prices vs tradesim for the same pack / window.

Evidence class: LIVE_BT_FILL_PARITY_DIAGNOSTIC_CONTAMINATED when the window
touches Forward Lockbox Start (2026-05-01). Micro-live began 2026-08-03/04, so
the operational live window is entirely post-lockbox. Lockbox does **not** end;
it is an open-ended seal from FORWARD_LOCKBOX_START forward.

Does not authorize deployment. Prefer outer-fold settle for promotion numbers.

Example (report-only, contaminates peek log):
  python scripts/audit_live_bt_fill_parity.py \\
    --pack artifacts/live_packs/structure_v1_ethusdt_direction \\
    --account Xxobster7 \\
    --start 2026-08-03 --end 2026-08-06 \\
    --i-accept-lockbox-contamination
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    Signal,
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_hedge,
)

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.indicators import load_bar_features  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.evidence.fill_parity import (  # noqa: E402
    match_fills,
    normalize_bybit_closed_row,
    normalize_tradesim_trade,
    summarize_pct_devs,
)
from llm2.evidence.lockbox_guard import (  # noqa: E402
    add_lockbox_guard_args,
    require_lockbox_access,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.models.base import Prediction  # noqa: E402
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    ROUND_TRIP_COST,
    TF_MS,
    touch_timeframe,
)
from llm2.research_policy import PolicyError  # noqa: E402
from llm2.signals.translate import predictions_to_signals  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

EXPERIMENT_ID = "live_bt_fill_parity_layer_c"
SPACE = "structure_v1"
LIVE_START_DOCUMENTED = "2026-08-03"  # certificate / first decisions (UTC)
# Lockbox has no end date — open-ended from FORWARD_LOCKBOX_START.


def _json_default(obj: object) -> object:
    if isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
        return None
    if isinstance(obj, (np.floating,)):
        v = float(obj)
        return None if not np.isfinite(v) else v
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, Path):
        return str(obj)
    raise TypeError(type(obj))


def _default_edge(strategy: dict[str, Any]) -> float:
    family = target_family(str(strategy.get("target", "fwd_return")))
    default = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    edge = float(strategy.get("min_edge", default))
    if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
        edge = DIRECTION_BAND
    return edge


def _signals_with_max_hold(
    signals: list[Signal],
    *,
    max_hold_bars: int,
    symbol: str,
) -> list[Signal]:
    out: list[Signal] = []
    for s in signals:
        out.append(
            Signal(
                ts_ms=int(s.ts_ms),
                side=s.side,
                symbol=symbol,
                stop_offset=s.stop_offset,
                target_offset=s.target_offset,
                max_hold_bars=int(max_hold_bars),
                tag=s.tag,
            )
        )
    return out


def run_pack_backtest(
    *,
    pack_dir: Path,
    start: pd.Timestamp,
    end: pd.Timestamp,
) -> tuple[list[Any], dict[str, Any]]:
    """Replay frozen pack on warehouse candles → tradesim trades."""
    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(pack_dir / "model.joblib")
    model = blob["model"]
    cols = list(blob["feature_columns"])
    symbol = str(strategy["symbol"]).upper()
    timeframe = str(strategy["timeframe"])
    family = target_family(str(strategy.get("target", "fwd_return")))
    edge = _default_edge(strategy)
    tp = float(strategy.get("tp_pct", 0.01))
    sl = float(strategy.get("sl_pct", 0.02))
    hold = int(strategy.get("horizon_bars", 6))
    lev = float(strategy.get("leverage") or leverage_from_stop(sl))

    ohlcv = load_ohlcv(symbol, timeframe)
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    # Need history before start for features; evaluate signals in [start, end)
    feat_ohlcv = ohlcv.loc[ohlcv.index < end].copy()
    feats = build_space(feat_ohlcv, SPACE, symbol=symbol, timeframe=timeframe)
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    for c in feats.columns:
        if c.startswith("last_retrace_pct_"):
            feats[c] = feats[c].fillna(0.0)
    aligned = feats.dropna()
    mask = (aligned.index >= start) & (aligned.index < end)
    aligned = aligned.loc[mask]
    if len(aligned) < 1:
        raise RuntimeError(f"{symbol}: no feature bars in [{start}, {end})")

    pred = model.predict(aligned.to_numpy(dtype=float))
    mean = pred.mean if getattr(pred, "mean", None) is not None else np.zeros(len(aligned))
    mean = np.asarray(mean, dtype=float).reshape(-1)
    side = proxy_side(mean, family).astype(np.int8)
    # index may be datetime64[ms]; never use asi8//1e6 (that assumes ns storage).
    ts_ms = index_to_ms(aligned.index)
    signals = predictions_to_signals(
        ts_ms,
        Prediction(side=side, mean=mean),
        tp_pct=tp,
        sl_pct=sl,
        min_edge=edge,
    )
    signals = _signals_with_max_hold(signals, max_hold_bars=hold, symbol=symbol)

    touch_tf = touch_timeframe(timeframe, symbol)
    touch = load_ohlcv(symbol, touch_tf)
    if touch.index.tz is None:
        touch.index = touch.index.tz_localize("UTC")
    # Pad decision window for max-hold exits
    pad = pd.Timedelta(hours=max(hold + 2, 8))
    win = ohlcv.loc[(ohlcv.index >= start - pd.Timedelta(days=2)) & (ohlcv.index < end + pad)]
    touch_end = end + pad
    touch_win = touch.loc[(touch.index >= start - pd.Timedelta(days=1)) & (touch.index < touch_end)]

    funding = load_funding(symbol)
    if funding is not None and len(funding):
        f_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
        f_rt = funding.to_numpy(dtype=float).reshape(-1)
        w0 = int(win.index.asi8[0] // 1_000_000)
        w1 = int(win.index.asi8[-1] // 1_000_000)
        fmask = (f_ts >= w0) & (f_ts <= w1)
        f_ts, f_rt = f_ts[fmask], f_rt[fmask]
    else:
        f_ts = np.asarray([], dtype=np.int64)
        f_rt = np.asarray([], dtype=float)

    costs = research_costs_baseline()
    instrument = research_instrument(symbol)
    sizing = research_sizing()
    margin = research_margin(leverage=lev)
    # Live packs use Bybit hedge mode (one long + one short book).
    sim = research_sim_hedge(starting_equity=10_000.0, max_hold_bars=hold)

    bundle = run_strategy_backtest(
        win,
        signals,
        symbol=symbol,
        timeframe=timeframe,
        strategy_id=f"llm2-fill-parity-{symbol}",
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf if len(touch_win) else None,
        strategy_meta={
            "name": strategy.get("strategy_id", pack_dir.name),
            "batch": EXPERIMENT_ID,
            "tp_pct": tp,
            "sl_pct": sl,
            "pack": str(pack_dir),
        },
        costs=costs,
        margin=margin,
        sizing=sizing,
        instrument=instrument,
        sim=sim,
        funding_ts_ms=f_ts if f_ts.size else None,
        funding_rate=f_rt if f_rt.size else None,
        plot=False,
        print_headline=False,
        store_path=None,
        starting_equity=10_000.0,
    )
    trades = list(bundle.result.trades)
    # Keep trades that enter inside the evaluate window
    start_ms = int(start.value // 1_000_000)
    end_ms = int(end.value // 1_000_000)
    trades = [t for t in trades if start_ms <= int(t.entry_ts_ms) < end_ms]
    meta = {
        "symbol": symbol,
        "timeframe": timeframe,
        "family": family,
        "edge": edge,
        "tp_pct": tp,
        "sl_pct": sl,
        "max_hold_bars": hold,
        "leverage": lev,
        "n_signals": len(signals),
        "n_bt_trades_in_window": len(trades),
        "engine": getattr(getattr(bundle, "stamp", None), "engine", "tradesim"),
    }
    return trades, meta


def fetch_live_closed_via_vps(
    *,
    account: str,
    symbol: str,
    since: str,
    host: str = "ln1",
) -> dict[str, Any]:
    """SCP helper to VPS and pull closed-pnl JSON (IP-whitelisted keys)."""
    helper = Path(__file__).resolve().parent / "_vps_closed_pnl.py"
    remote = "/tmp/_vps_closed_pnl.py"
    subprocess.check_call(
        [
            "scp",
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=12",
            str(helper),
            f"{host}:{remote}",
        ],
        timeout=40,
    )
    out = subprocess.check_output(
        [
            "ssh",
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=12",
            host,
            f"python3 {remote} {account} {symbol} {since}",
        ],
        text=True,
        timeout=120,
        stderr=subprocess.STDOUT,
    )
    line = [ln for ln in out.splitlines() if ln.strip().startswith("{")][-1]
    return json.loads(line)


def load_live_fills(args: argparse.Namespace, symbol: str) -> tuple[list[Any], dict[str, Any]]:
    if args.live_fills_json:
        path = Path(args.live_fills_json)
        raw = path.read_bytes()
        if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
            text = raw.decode("utf-16")
        else:
            text = raw.decode("utf-8")
        blob = json.loads(text)
        rows = blob.get("trades") if isinstance(blob, dict) else blob
        if not isinstance(rows, list):
            raise RuntimeError(f"unexpected live fills schema in {path}")
        meta = {
            "source": str(path),
            "n_raw": len(rows),
            "account": blob.get("account") if isinstance(blob, dict) else None,
        }
        return rows, meta
    if args.skip_live_fetch:
        return [], {"source": "skipped", "n_raw": 0}
    blob = fetch_live_closed_via_vps(
        account=args.account,
        symbol=symbol,
        since=args.start,
        host=args.vps_host,
    )
    if blob.get("error"):
        raise RuntimeError(f"live closed-pnl fetch failed: {blob}")
    rows = list(blob.get("trades") or [])
    meta = {
        "source": blob.get("source") or "vps",
        "n_raw": len(rows),
        "account": blob.get("account"),
        "retrieved_utc": blob.get("retrieved_utc"),
    }
    return rows, meta


def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--pack",
        type=Path,
        default=ARTIFACTS / "live_packs" / "structure_v1_ethusdt_direction",
        help="Frozen live pack directory",
    )
    p.add_argument("--account", default="Xxobster7")
    p.add_argument("--start", default=LIVE_START_DOCUMENTED, help="Window start UTC (inclusive)")
    p.add_argument(
        "--end",
        default=None,
        help="Window end UTC exclusive (default: now)",
    )
    p.add_argument("--live-fills-json", type=Path, default=None, help="Offline Bybit closed-pnl dump")
    p.add_argument("--skip-live-fetch", action="store_true", help="BT-only dry run")
    p.add_argument("--vps-host", default="ln1")
    p.add_argument(
        "--match-tol-hours",
        type=float,
        default=3.0,
        help="Max |exit_ts live − BT| for a match (hours)",
    )
    add_lockbox_guard_args(p)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_argparser().parse_args(argv)
    pack_dir = args.pack.resolve()
    if not (pack_dir / "strategy.json").is_file():
        raise SystemExit(f"pack missing strategy.json: {pack_dir}")

    start = pd.Timestamp(args.start, tz="UTC")
    end = pd.Timestamp(args.end, tz="UTC") if args.end else pd.Timestamp.now(tz="UTC")
    if end <= start:
        raise SystemExit("end must be after start")

    calendar = {
        "forward_lockbox_start": FORWARD_LOCKBOX_START,
        "forward_lockbox_end": None,
        "lockbox_note": (
            "Lockbox is open-ended from FORWARD_LOCKBOX_START; it does not end. "
            "Any evaluation on/after that date requires --i-accept-lockbox-contamination."
        ),
        "live_trading_started_documented": LIVE_START_DOCUMENTED,
        "live_trading_note": (
            "User-authorized micro-live certificate 2026-08-03; VPS fleet services "
            "2026-08-04. First logged decisions ~2026-08-03 16:00 UTC (BTC)."
        ),
        "window_start": start.isoformat(),
        "window_end_exclusive": end.isoformat(),
        "window_is_post_lockbox": start >= pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        or end > pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC"),
    }

    peek = require_lockbox_access(
        experiment_id=EXPERIMENT_ID,
        window_start=start.isoformat(),
        window_end=end.isoformat(),
        purpose="live_bt_fill_pct_deviation_layer_c",
        symbols=[json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))["symbol"]],
        accepted_contamination=bool(args.i_accept_lockbox_contamination),
        open_finplot=False,
        accepted_finplot=False,
        notes="Layer C fill % deviation vs tradesim; diagnostic only",
    )

    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    symbol = str(strategy["symbol"]).upper()

    # Stale functools caches can hide a warehouse tip refresh.
    if hasattr(load_bar_features, "cache_clear"):
        load_bar_features.cache_clear()

    live_rows, live_meta = load_live_fills(args, symbol)
    live_fills = []
    for r in live_rows:
        nf = normalize_bybit_closed_row(r)
        if nf is not None and nf.symbol == symbol:
            # Restrict to window by exit time
            if start.value // 1_000_000 <= nf.exit_ts_ms < end.value // 1_000_000:
                live_fills.append(nf)

    bt_trades, bt_meta = run_pack_backtest(pack_dir=pack_dir, start=start, end=end)
    bt_fills = []
    for t in bt_trades:
        nf = normalize_tradesim_trade(t, symbol=symbol)
        if nf is not None:
            bt_fills.append(nf)

    tol_ms = int(float(args.match_tol_hours) * 3_600_000)
    matches = match_fills(live_fills, bt_fills, match_tol_ms=tol_ms)
    summary = summarize_pct_devs(matches)

    evidence_class = (
        "LIVE_BT_FILL_PARITY_DIAGNOSTIC_CONTAMINATED"
        if peek is not None
        else "LIVE_BT_FILL_PARITY_DIAGNOSTIC"
    )
    report = {
        "experiment_id": EXPERIMENT_ID,
        "evidence_class": evidence_class,
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "principal_blocker": (
            "Fill % deviation is diagnostic. Live calendar is post-lockbox; "
            "do not use for ranking or readiness. Prefer Layer A indicator parity "
            "and outer-fold settle for promotion."
        ),
        "calendar": calendar,
        "pack": str(pack_dir),
        "account": args.account,
        "live_meta": live_meta,
        "backtest_meta": bt_meta,
        "match_tol_hours": float(args.match_tol_hours),
        "n_live_fills_in_window": len(live_fills),
        "n_bt_fills_in_window": len(bt_fills),
        "summary": summary,
        "matches": matches,
        "peek_record_id": (peek or {}).get("id") if isinstance(peek, dict) else None,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
    }

    out_dir = ARTIFACTS / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = out_dir / f"live_bt_fill_parity_{stamp}.json"
    latest = out_dir / "live_bt_fill_parity_latest.json"
    text = json.dumps(report, indent=2, default=_json_default)
    out_path.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")

    print(
        json.dumps(
            {
                "ok": True,
                "evidence_class": evidence_class,
                "calendar": calendar,
                "summary": summary,
                "n_live": len(live_fills),
                "n_bt": len(bt_fills),
                "report": str(out_path),
            },
            indent=2,
            default=_json_default,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PolicyError as exc:
        print(json.dumps({"ok": False, "error": "PolicyError", "detail": str(exc)}), file=sys.stderr)
        raise SystemExit(2) from exc
