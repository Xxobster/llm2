"""Stage-1 WAVE001 scan: metrics triggers, amplitude events, structure breaks, the
cross-series wave panel and shape k-NN motifs, all false-discovery-rate corrected together
as one family, written to ``artifacts/reports/wave001/``.

**RESEARCH_ONLY.** This script runs diagnostics; it does not call tradesim, does not select
or freeze a strategy, and by itself cannot earn anything above ``SHADOW_READY`` (see
``configs/preregister/wave001_candidate_space.yaml``).
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from llm2.diagnostics.stats import Effect, apply_fdr, effects_to_frame
from llm2.diagnostics.wave import fit_wave
from llm2.diagnostics.waveevent import run_amplitude_event_study, score_events
from llm2.diagnostics.wavemetrics import build_causal_metrics, detect_triggers
from llm2.diagnostics.wavemotif import run_shape_knn_study
from llm2.paths import ARTIFACTS

SYMBOL, TIMEFRAME = "BTCUSDT", "1h"
MTF_TIMEFRAME = "4h"
TRAIN_END = "2026-05-01"
HORIZONS = (6, 24, 96)
CONFIG_PATH = Path("configs/preregister/wave001_candidate_space.yaml")

# Broad Tier A: every liquid crypto in the lab primary set, every 1h-capable price-like
# macro in EXTERNAL_REGISTRY, plus volume and funding. Daily-only macros (SPX/VIX/FRED/
# stablecoins) stay out of the 1h panel — they belong on a 1d scan. cryptodb/market.sqlite
# is excluded until D-028 timing semantics are resolved.
PANEL_CRYPTO_SYMBOLS: tuple[str, ...] = (
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT",
    "XRPUSDT",
    "ADAUSDT",
    "DOGEUSDT",
    "AVAXUSDT",
    "LINKUSDT",
)
PANEL_MACRO_1H: tuple[str, ...] = (
    "DXY",
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "USDCHF",
    "USDCAD",
    "AUDUSD",
    "NZDUSD",
    "EURJPY",
    "EURGBP",
    "XAUUSD",
    "XAGUSD",
    "COPPER",
    "WTI",
    "BRENT",
    "HSI",
    "HKG40",
)


def _tier_b_from_ohlcv(ohlcv: pd.DataFrame) -> dict[str, pd.Series]:
    """Closed Tier B transforms (D-029): nonlinear / bounded, not linear price filters."""
    c = ohlcv["close"].astype(float)
    h = ohlcv["high"].astype(float)
    l = ohlcv["low"].astype(float)
    v = ohlcv["volume"].astype(float) if "volume" in ohlcv.columns else pd.Series(np.nan, index=ohlcv.index)
    ret = np.log(c.replace(0, np.nan)).diff()
    # RSI(14)
    gain = ret.clip(lower=0.0)
    loss = (-ret).clip(lower=0.0)
    avg_g = gain.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    avg_l = loss.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    rs = avg_g / avg_l.replace(0, np.nan)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    # Realised vol (20)
    rvol = ret.rolling(20, min_periods=20).std()
    # Signed volume imbalance
    svi = np.sign(ret).fillna(0.0) * v
    # Return run length (vectorised: reset whenever the sign changes or is zero)
    sign = np.sign(ret).fillna(0.0).to_numpy()
    change = np.empty(len(sign), dtype=bool)
    change[0] = True
    change[1:] = (sign[1:] == 0) | (sign[1:] != sign[:-1])
    group = np.cumsum(change)
    run = pd.Series(1.0, index=ohlcv.index).groupby(group).cumsum().to_numpy()
    run = np.where(sign == 0, 0.0, run)
    # ATR-normalised displacement from 50-bar mean
    prev_c = c.shift(1)
    tr = pd.concat([(h - l), (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14, min_periods=14).mean()
    disp = (c - c.rolling(50, min_periods=50).mean()) / atr.replace(0, np.nan)
    return {
        "rsi_14": rsi,
        "realised_vol": rvol,
        "signed_volume_imbalance": svi,
        "return_run_length": pd.Series(run, index=ohlcv.index),
        "atr_normalised_displacement": disp,
    }


def _build_panel_inputs(
    reference_close: pd.Series,
    idx: pd.DatetimeIndex,
    ohlcv: pd.DataFrame | None = None,
) -> tuple[dict[str, pd.Series], pd.DataFrame, dict[str, str], dict[str, bool]]:
    """Tier A + closed Tier B panel and raw-return companion for wavepanel.

    Crypto closes share the bar clock. Macros use causal as-of alignment with publication
    lag. Funding and Tier B are non-log wave inputs. ``cryptodb`` is not read (D-028).
    """
    from llm2.data.macro import build_external_panel, load_funding, stationary_level_columns
    from llm2.data.panel import build_close_panel

    close_panel: dict[str, pd.Series] = {SYMBOL: reference_close.reindex(idx)}
    admitted_kinds: dict[str, str] = {SYMBOL: "close"}
    log_flags: dict[str, bool] = {SYMBOL: True}

    try:
        crypto = build_close_panel([SYMBOL, *PANEL_CRYPTO_SYMBOLS], TIMEFRAME)
        crypto = crypto.reindex(idx, method="ffill")
        for sym in PANEL_CRYPTO_SYMBOLS:
            if sym in crypto.columns and crypto[sym].notna().sum() >= 500:
                close_panel[sym] = crypto[sym]
                admitted_kinds[sym] = "close"
                log_flags[sym] = True
    except Exception as exc:  # noqa: BLE001
        print(f"    panel: crypto closes unavailable ({exc})")

    # Own-series volume and Tier B transforms of the reference OHLCV are NOT admitted as
    # external leads: they are deterministic functions of the series being predicted and
    # manufacture large "leads" that are just the transform's own lag (RSI of BTC cannot
    # lead BTC). They remain available inside wavemetrics / waveevent on the reference.
    try:
        funding = load_funding(SYMBOL).reindex(idx, method="ffill")
        if funding.notna().sum() >= 500:
            close_panel["FUNDING_RATE"] = funding
            admitted_kinds["FUNDING_RATE"] = "funding"
            log_flags["FUNDING_RATE"] = False
    except Exception as exc:  # noqa: BLE001
        print(f"    panel: funding unavailable ({exc})")

    stat_levels = stationary_level_columns()
    price_like_macros = [s for s in PANEL_MACRO_1H if s not in stat_levels]
    try:
        macro = build_external_panel(idx, price_like_macros, TIMEFRAME, include_age=False)
        for sym in price_like_macros:
            if sym in macro.columns and macro[sym].notna().sum() >= 500:
                close_panel[sym] = macro[sym]
                admitted_kinds[sym] = "macro"
                log_flags[sym] = True
    except Exception as exc:  # noqa: BLE001
        print(f"    panel: macro series unavailable ({exc})")

    _ = ohlcv  # reserved; Tier B stays out of the external lead panel (see above)
    return_cols: dict[str, pd.Series] = {}
    for name, series in close_panel.items():
        s = series.reindex(idx)
        if name in stat_levels or not log_flags.get(name, True):
            # Stationary level / oscillator: cluster on first difference (or level for funding).
            return_cols[name] = s if name == "FUNDING_RATE" else s.diff()
        else:
            return_cols[name] = np.log(s.replace(0, np.nan)).diff()
    return_panel = pd.DataFrame(return_cols, index=idx)
    return close_panel, return_panel, admitted_kinds, log_flags


def _candidate_space_hash() -> str:
    with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    cfg.pop("candidate_space_sha256", None)
    payload = json.dumps(cfg, sort_keys=True, default=str)
    return hashlib.sha256(payload.encode()).hexdigest()


def _trigger_effects(metrics: pd.DataFrame, close: pd.Series, period: float) -> list[Effect]:
    """Score wavemetrics triggers with the same direction/magnitude machinery as waveevent."""
    triggers = detect_triggers(metrics, period=period)
    return score_events(close, triggers, horizons=HORIZONS, min_events=10)


def main() -> int:
    from llm2.data.loader import load_ohlcv

    space_hash = _candidate_space_hash()
    print(f"candidate space sha256: {space_hash}")

    ohlcv_full = load_ohlcv(SYMBOL, TIMEFRAME)
    ohlcv = ohlcv_full[ohlcv_full.index < pd.Timestamp(TRAIN_END, tz="UTC")]

    fit = fit_wave(ohlcv["close"], symbol=SYMBOL, timeframe=TIMEFRAME)
    period = fit.period_bars
    print(fit.summary())
    if not np.isfinite(period) or period <= 2:
        print("No usable period fit; aborting the scan (this is a valid null result).")
        return 1

    all_effects: list[Effect] = []

    print("\n[1/5] wavemetrics triggers ...")
    metrics = build_causal_metrics(ohlcv["close"], ohlcv.get("volume"), period)
    trigger_effects = _trigger_effects(metrics, ohlcv["close"], period)
    for e in trigger_effects:
        e.detail["family"] = "wavemetrics_triggers"
    all_effects += trigger_effects
    print(f"    {len(trigger_effects)} effects")

    print("[2/5] amplitude-event study (waveevent) ...")
    try:
        event_effects = run_amplitude_event_study(ohlcv, period, horizons=HORIZONS)
    except Exception as exc:  # noqa: BLE001 - a family-level failure must not abort the scan
        print(f"    SKIPPED: {exc}")
        event_effects = []
    for e in event_effects:
        e.detail["family"] = "waveevent"
    all_effects += event_effects
    print(f"    {len(event_effects)} effects")

    print("[3/5] structure-break study (structurebreak) ...")
    try:
        from llm2.diagnostics.structurebreak import run_structure_break_study

        break_effects = run_structure_break_study(
            ohlcv, SYMBOL, TIMEFRAME, period=period, mtf_timeframe=MTF_TIMEFRAME, horizons=HORIZONS
        )
    except Exception as exc:  # noqa: BLE001
        print(f"    SKIPPED: {exc}")
        break_effects = []
    for e in break_effects:
        e.detail["family"] = "structurebreak"
    all_effects += break_effects
    print(f"    {len(break_effects)} effects")

    print("[4/5] cross-series wave panel (wavepanel) ...")
    panel_clusters: list[list[str]] = []
    try:
        from llm2.diagnostics.wavepanel import run_wave_panel_scan

        close_panel, return_panel, admitted_kinds, log_flags = _build_panel_inputs(
            ohlcv["close"], ohlcv.index, ohlcv=ohlcv
        )
        print(f"    panel members ({len(close_panel)}): {sorted(close_panel)}")
        panel_effects, panel_clusters = run_wave_panel_scan(
            close_panel,
            return_panel,
            SYMBOL,
            admitted_kinds,
            period=period,
            log_price_flags=log_flags,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"    SKIPPED: {exc}")
        panel_effects = []
    for e in panel_effects:
        e.detail["family"] = "wavepanel"
    all_effects += panel_effects
    print(f"    {len(panel_effects)} effects across {len(panel_clusters)} raw-return clusters")

    print("[5/5] shape k-NN motifs (wavemotif) ...")
    try:
        motif_rows = run_shape_knn_study(
            ohlcv["close"], period=period, train_end=ohlcv.index[int(len(ohlcv) * 0.8)], horizon=24
        )
    except Exception as exc:  # noqa: BLE001
        print(f"    SKIPPED: {exc}")
        motif_rows = []
    print(f"    {len(motif_rows)} (L, k) combinations")

    print("\nApplying false-discovery-rate control across all diagnostic-family effects ...")
    all_effects = apply_fdr(all_effects)
    n_sig = sum(e.significant for e in all_effects)
    print(f"{n_sig}/{len(all_effects)} effects survive q <= 0.05 across the pooled family.")

    run_id = f"wave001_{SYMBOL}_{TIMEFRAME}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    out_dir = ARTIFACTS / "reports" / "wave001"
    out_dir.mkdir(parents=True, exist_ok=True)

    frame = effects_to_frame(all_effects)
    payload = {
        "run_id": run_id,
        "study_id": "wave001",
        "readiness": "RESEARCH_ONLY",
        "candidate_space_sha256": space_hash,
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "mtf_timeframe": MTF_TIMEFRAME,
        "period_bars": period,
        "peak_ratio": fit.peak_ratio,
        "p_value": fit.p_value,
        "train_end": TRAIN_END,
        "n_effects": len(all_effects),
        "n_significant": n_sig,
        "motif_results": motif_rows,
        "effects": json.loads(frame.to_json(orient="records")) if len(frame) else [],
    }
    json_path = out_dir / f"{run_id}.json"
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, default=str)

    md_path = out_dir / f"{run_id}.md"
    finite_q = [e for e in all_effects if np.isfinite(e.q_value)]
    top = sorted(finite_q, key=lambda e: e.q_value)[:30]
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(f"# WAVE001 stage-1 scan — {run_id}\n\n")
        fh.write(f"Candidate space sha256: `{space_hash}`\n\n")
        fh.write(
            f"Engine: `llm2.diagnostics.wave.causal_wave`; period {period:.2f} bars "
            f"(peak {fit.peak_ratio:.2f}x AR(1) null, p={fit.p_value:.4f})\n\n"
        )
        fh.write(
            f"**Readiness: RESEARCH_ONLY.** {n_sig}/{len(all_effects)} effects survive "
            f"q <= 0.05 across the pooled false-discovery family.\n\n"
        )
        fh.write("## Top effects by q-value\n\n")
        fh.write("| name | statistic | n | p | q | significant |\n|---|---|---|---|---|---|\n")
        for e in top:
            fh.write(
                f"| {e.name} | {e.statistic:.5f} | {e.n} | {e.p_value:.4f} | "
                f"{e.q_value:.4f} | {e.significant} |\n"
            )
        fh.write("\n## Shape k-NN motif results\n\n")
        fh.write("| L | k | n_valid | corr | p |\n|---|---|---|---|---|\n")
        for r in motif_rows:
            corr = r.get("corr_pred_vs_realised", float("nan"))
            p_val = r.get("p_value", float("nan"))
            corr_s = f"{corr:.4f}" if np.isfinite(corr) else "nan"
            p_s = f"{p_val:.4f}" if np.isfinite(p_val) else "nan"
            fh.write(f"| {r['L']} | {r['k']} | {r['n_valid']} | {corr_s} | {p_s} |\n")

    print(f"\nwrote {json_path}\nwrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
