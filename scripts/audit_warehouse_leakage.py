"""Warehouse causality audit for the WAVE001 mining plan.

Two kinds of check, kept explicitly separate:

1. **SQL-level confirmation-time spot checks** on the raw warehouses themselves — is a
   value that a feature would read actually knowable at the bar it would be read on? These
   do not touch any of the new ``llm2.diagnostics`` code; they re-verify the warehouses'
   own causal contracts directly against the tables.
2. **The shared ``leakage`` engine's prefix-invariance / future-mutation / name-scan audit**
   against :func:`llm2.diagnostics.wavemetrics.build_causal_metrics`, the feature builder
   every WAVE001 mining module is built on top of.

Databases covered: ``market_ohlcv.sqlite``, ``indicators.sqlite``, ``binance_funding.sqlite``
(all under ``D:\\projectsdata``) and ``D:\\projectsdata\\cryptodb\\market.sqlite``. Every
check prints PASS/FAIL/BLOCKER and the script exits non-zero if anything hard-fails.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

MARKET_DB = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
INDICATORS_DB = Path(r"D:\projectsdata\indicators\indicators.sqlite")
FUNDING_DB = Path(r"D:\projectsdata\candles\binance_funding.sqlite")
CRYPTODB = Path(r"D:\projectsdata\cryptodb\market.sqlite")

SYMBOL, TIMEFRAME, SOURCE = "BTCUSDT", "1h", "binance"

RESULTS: list[dict] = []


def _record(name: str, status: str, detail: str) -> None:
    """status is one of PASS / FAIL / BLOCKER / SKIP."""
    RESULTS.append({"check": name, "status": status, "detail": detail})
    print(f"[{status:7s}] {name}: {detail}")


# --------------------------------------------------------------------------------------
# 1. market_ohlcv.sqlite
# --------------------------------------------------------------------------------------


def audit_market_ohlcv() -> None:
    if not MARKET_DB.is_file():
        _record("market_ohlcv.timestamp_integrity", "BLOCKER", f"missing: {MARKET_DB}")
        return
    conn = sqlite3.connect(f"file:{MARKET_DB}?mode=ro", uri=True, timeout=60.0)
    try:
        df = pd.read_sql(
            "SELECT ts_ms, is_complete FROM market_ohlcv WHERE symbol = ? AND timeframe = ? "
            "AND source = ? ORDER BY ts_ms",
            conn,
            params=(SYMBOL, TIMEFRAME, SOURCE),
        )
    finally:
        conn.close()

    if df.empty:
        _record("market_ohlcv.timestamp_integrity", "BLOCKER", f"no rows for {SYMBOL} {TIMEFRAME}")
        return

    ts = df["ts_ms"].to_numpy()
    dup = int(pd.Series(ts).duplicated().sum())
    non_monotonic = int(np.sum(np.diff(ts) <= 0))
    step_ms = 3_600_000
    gaps = np.diff(ts)
    n_gap = int(np.sum(gaps > step_ms))
    max_gap_bars = float(np.max(gaps) / step_ms) if gaps.size else 0.0

    ok = dup == 0 and non_monotonic == 0
    _record(
        "market_ohlcv.timestamp_integrity",
        "PASS" if ok else "FAIL",
        f"{len(df):,} bars, {dup} duplicate ts_ms, {non_monotonic} non-monotonic steps, "
        f"{n_gap} gaps > 1 bar (largest {max_gap_bars:.1f} bars) — duplicates/non-monotonic "
        "would make later code's use of position-as-time ambiguous",
    )

    if "is_complete" in df.columns and df["is_complete"].notna().any():
        incomplete = int((df["is_complete"] == 0).sum())
        _record(
            "market_ohlcv.is_complete_flag",
            "PASS" if incomplete <= 1 else "FAIL",
            f"{incomplete} bars flagged incomplete (only the newest in-progress bar should be)",
        )
    else:
        _record("market_ohlcv.is_complete_flag", "SKIP", "column absent or all-null for this series")


# --------------------------------------------------------------------------------------
# 2. indicators.sqlite — confirmation-time spot checks (re-verifies the module's own claim)
# --------------------------------------------------------------------------------------


def audit_indicators() -> None:
    if not INDICATORS_DB.is_file():
        _record("indicators.confirmation_time", "BLOCKER", f"missing: {INDICATORS_DB}")
        return

    from llm2.data.indicators import SWING_LEFT, SWING_RIGHT, load_bar_features

    conn = sqlite3.connect(f"file:{INDICATORS_DB}?mode=ro", uri=True, timeout=60.0)
    try:
        swings = pd.read_sql(
            "SELECT kind, pivot_ts_ms, confirm_ts_ms, price FROM swings WHERE symbol = ? "
            "AND timeframe = ? AND source = ? AND swing_left = ? AND swing_right = ?",
            conn,
            params=(SYMBOL, TIMEFRAME, SOURCE, SWING_LEFT, SWING_RIGHT),
        )
    finally:
        conn.close()

    if swings.empty:
        _record("indicators.confirmation_time", "BLOCKER", f"no swings for {SYMBOL} {TIMEFRAME}")
        return

    try:
        bar_features = load_bar_features(SYMBOL, TIMEFRAME, source=SOURCE)
    except (FileNotFoundError, ValueError) as exc:
        _record("indicators.confirmation_time", "BLOCKER", str(exc))
        return

    # A pivot's own confirmation instant is knowable directly from the swings table; join
    # bar_features' cited pivot (last_sh_ts_ms / last_sl_ts_ms) back to that swing's
    # confirm_ts_ms and check it is at or before the bar citing it.
    bf = bar_features[["ts_ms", "last_sh_ts_ms", "last_sl_ts_ms", "nearest_support", "nearest_resistance", "close"]].copy()

    # The warehouse's swing kind labels are 'high'/'low' (verified directly against
    # indicators.sqlite; do not confuse with the 'SH'/'SL' shorthand in bar_features'
    # own column names, which is a different naming convention for the same concept).
    for kind, ts_col in (("high", "last_sh_ts_ms"), ("low", "last_sl_ts_ms")):
        sw = swings[swings["kind"] == kind][["pivot_ts_ms", "confirm_ts_ms"]].drop_duplicates("pivot_ts_ms")
        merged = bf[["ts_ms", ts_col]].dropna().merge(
            sw, left_on=ts_col, right_on="pivot_ts_ms", how="left"
        )
        unmatched = int(merged["confirm_ts_ms"].isna().sum())
        matched = merged.dropna(subset=["confirm_ts_ms"])
        cited_early = int((matched["confirm_ts_ms"] > matched["ts_ms"]).sum())
        label = "swing_high" if kind == "high" else "swing_low"
        status = "PASS" if cited_early == 0 else "FAIL"
        detail = (
            f"{len(matched):,} bars checked, {cited_early} cited a {label} before its own "
            f"confirmation ({unmatched} pivots not found in swings table)"
        )
        _record(f"indicators.{label}_confirmation_time", status, detail)

    sr = bf.dropna(subset=["nearest_support", "nearest_resistance", "close"])
    support_above_close = int((sr["nearest_support"] > sr["close"]).sum())
    resistance_below_close = int((sr["nearest_resistance"] < sr["close"]).sum())
    ok = support_above_close == 0 and resistance_below_close == 0
    _record(
        "indicators.support_resistance_ordering",
        "PASS" if ok else "FAIL",
        f"{len(sr):,} bars checked, {support_above_close} with support above close, "
        f"{resistance_below_close} with resistance below close",
    )


# --------------------------------------------------------------------------------------
# 3. binance_funding.sqlite
# --------------------------------------------------------------------------------------


def audit_funding() -> None:
    if not FUNDING_DB.is_file():
        _record("binance_funding.settlement_time", "BLOCKER", f"missing: {FUNDING_DB}")
        return

    conn = sqlite3.connect(f"file:{FUNDING_DB}?mode=ro", uri=True, timeout=60.0)
    try:
        df = pd.read_sql(
            "SELECT funding_time_ms FROM funding_rate WHERE symbol = ? AND source = ? "
            "ORDER BY funding_time_ms",
            conn,
            params=(SYMBOL, SOURCE),
        )
    finally:
        conn.close()

    if df.empty:
        _record("binance_funding.settlement_time", "BLOCKER", f"no rows for {SYMBOL}")
        return

    ts = df["funding_time_ms"].to_numpy()
    dup = int(pd.Series(ts).duplicated().sum())
    non_monotonic = int(np.sum(np.diff(ts) <= 0))
    intervals_hr = np.diff(ts) / 3_600_000.0
    off_schedule = int(np.sum(np.abs(intervals_hr - 8.0) > 0.5)) if intervals_hr.size else 0

    ok = dup == 0 and non_monotonic == 0
    _record(
        "binance_funding.settlement_time",
        "PASS" if ok else "FAIL",
        f"{len(df):,} settlements, {dup} duplicates, {non_monotonic} non-monotonic gaps, "
        f"{off_schedule} intervals off the nominal 8h schedule by > 30 minutes",
    )


# --------------------------------------------------------------------------------------
# 4. cryptodb/market.sqlite — daily research warehouse; timing semantics unresolved
# --------------------------------------------------------------------------------------


def audit_cryptodb() -> None:
    if not CRYPTODB.is_file():
        _record("cryptodb.market.timing_semantics", "BLOCKER", f"missing: {CRYPTODB}")
        return

    conn = sqlite3.connect(f"file:{CRYPTODB}?mode=ro", uri=True, timeout=60.0)
    try:
        df = pd.read_sql(
            "SELECT date FROM venue_pair_daily WHERE venue = 'bybit' AND symbol = 'BTCUSDT' "
            "AND market_type = 'spot' ORDER BY date",
            conn,
        )
    finally:
        conn.close()

    if df.empty:
        _record("cryptodb.market.timing_semantics", "BLOCKER", "no BTCUSDT bybit spot daily rows to spot-check")
        return

    dates = pd.to_datetime(df["date"], errors="coerce")
    bad_dates = int(dates.isna().sum())
    dup_dates = int(df["date"].duplicated().sum())
    _record(
        "cryptodb.market.date_column_integrity",
        "PASS" if (bad_dates == 0 and dup_dates == 0) else "FAIL",
        f"{len(df):,} daily rows for BTCUSDT@bybit spot, {bad_dates} unparseable dates, "
        f"{dup_dates} duplicate dates",
    )

    # This is the substantive finding: every table in this warehouse stores a plain
    # calendar ``date`` string with no bar-open/bar-close/publication-instant convention
    # attached anywhere in the schema (no ts_ms, no confirm_ts_ms, no explicit UTC session
    # boundary documented in source_audit). asset_daily in particular blends several
    # providers (coinmetrics archive vs API) whose own cutover instant is not recorded per
    # row. Until each table's day-boundary and same-day availability is pinned down (most
    # likely UTC midnight-to-midnight, knowable only at the following UTC midnight, but
    # NOT yet verified against the vendor APIs the way market_ohlcv and indicators.sqlite
    # were), this warehouse cannot be treated as confirmation-time-safe and nothing that
    # depends on same-day cryptodb values in a live-timed decision should be trusted.
    _record(
        "cryptodb.market.timing_semantics",
        "BLOCKER",
        "no per-row knowable-at instant is recorded anywhere in this warehouse's schema "
        "(only a calendar 'date' string); the day-boundary/publication-lag convention used "
        "by market_ohlcv.sqlite and indicators.sqlite has NOT been established here and "
        "must be pinned down (per source in source_audit) before any WAVE001 family reads "
        "same-day cryptodb values as a causal feature",
    )


# --------------------------------------------------------------------------------------
# 5. Shared leakage engine against build_causal_metrics
# --------------------------------------------------------------------------------------


def audit_wavemetrics_leakage() -> None:
    from leakage.ensure_source import prefer_botsgeneral_leakage

    prefer_botsgeneral_leakage()
    import leakage

    if "botsgeneral" not in (leakage.__file__ or ""):
        _record("leakage.wavemetrics_prefix_invariance", "BLOCKER", "leakage package is not the botsgeneral source")
        return

    from leakage import format_report, require_clean_audit, run_leakage_audit

    from llm2.data.loader import load_ohlcv
    from llm2.diagnostics.wave import fit_wave
    from llm2.diagnostics.wavemetrics import build_causal_metrics
    from llm2.paths import LEAKAGE_REGISTRY

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME, source=SOURCE)
    fit = fit_wave(ohlcv["close"], symbol=SYMBOL, timeframe=TIMEFRAME)
    period = fit.period_bars if np.isfinite(fit.period_bars) and fit.period_bars > 2 else 24.0

    def _builder(bars: pd.DataFrame, *, interval: str = TIMEFRAME) -> pd.DataFrame:
        # `period` is pinned once outside this closure (not re-fit per call) so the audit
        # isolates build_causal_metrics' own causality rather than dominant_period's.
        return build_causal_metrics(bars["close"], bars.get("volume"), period)

    LEAKAGE_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    report = run_leakage_audit(
        ohlcv=ohlcv,
        build_features=_builder,
        interval=TIMEFRAME,
        registry_path=str(LEAKAGE_REGISTRY),
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        cuts=3,
    )
    print(format_report(report))
    try:
        require_clean_audit(report)
        _record(
            "leakage.wavemetrics_prefix_invariance",
            "PASS",
            f"{report.n_columns} columns clean; pinned period={period:.2f} bars",
        )
    except Exception as exc:  # noqa: BLE001
        _record(
            "leakage.wavemetrics_prefix_invariance",
            "FAIL",
            f"{exc}; leakage_potential={list(report.leakage_potential)}",
        )


def main() -> int:
    audit_market_ohlcv()
    audit_indicators()
    audit_funding()
    audit_cryptodb()
    try:
        audit_wavemetrics_leakage()
    except Exception as exc:  # noqa: BLE001
        _record("leakage.wavemetrics_prefix_invariance", "FAIL", f"audit raised: {exc}")

    n_fail = sum(1 for r in RESULTS if r["status"] == "FAIL")
    n_blocker = sum(1 for r in RESULTS if r["status"] == "BLOCKER")
    n_pass = sum(1 for r in RESULTS if r["status"] == "PASS")

    print(f"\n{n_pass} PASS, {n_fail} FAIL, {n_blocker} BLOCKER, {len(RESULTS)} checks total.")

    from llm2.paths import ARTIFACTS

    out_dir = ARTIFACTS / "reports" / "wave001"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "warehouse_leakage_audit.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(
            {
                "audited_utc": pd.Timestamp.utcnow().isoformat(),
                "symbol": SYMBOL,
                "timeframe": TIMEFRAME,
                "results": RESULTS,
                "n_pass": n_pass,
                "n_fail": n_fail,
                "n_blocker": n_blocker,
            },
            fh,
            indent=2,
            default=str,
        )
    print(f"wrote {out_path}")
    return 1 if n_fail > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
