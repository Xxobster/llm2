"""Orchestrate a diagnostics pass, persist it and render it as a readable report.

Everything runs on the training window only. The forward lockbox is never read, and no
selection happens here: the output is a description of what is in the data, and any
shortlist it produces has to be preregistered before it goes near the walk-forward.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from llm2.data.loader import load_ohlcv
from llm2.data.macro import available_externals, load_funding
from llm2.data.indicators import INDICATORS_DB
from llm2.diagnostics import confluence, crossasset, events, marketstructure, structure
from llm2.diagnostics.stats import Effect, effects_to_frame
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, RESEARCH_DB, ensure_artifact_dirs

DIAGNOSTICS_SCHEMA = """
CREATE TABLE IF NOT EXISTS diagnostics_runs (
    run_id TEXT PRIMARY KEY,
    created_at TEXT NOT NULL,
    symbol TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    train_start TEXT,
    train_end TEXT,
    n_bars INTEGER,
    n_external INTEGER,
    config_json TEXT
);
CREATE TABLE IF NOT EXISTS diagnostics_effects (
    run_id TEXT NOT NULL,
    family TEXT NOT NULL,
    name TEXT NOT NULL,
    statistic REAL,
    n INTEGER,
    p_value REAL,
    q_value REAL,
    ci_low REAL,
    ci_high REAL,
    significant INTEGER,
    detail_json TEXT,
    PRIMARY KEY (run_id, family, name)
);
CREATE INDEX IF NOT EXISTS idx_diag_effects_sig ON diagnostics_effects(run_id, significant);
"""


@dataclass
class DiagnosticsResult:
    run_id: str
    symbol: str
    timeframe: str
    n_bars: int
    train_start: str
    train_end: str
    families: dict[str, list[Effect]] = field(default_factory=dict)
    notes: dict[str, object] = field(default_factory=dict)

    def survivors(self, family: str | None = None) -> list[Effect]:
        """Effects that survive false-discovery-rate control within their own family."""
        out: list[Effect] = []
        for fam, effs in self.families.items():
            if family is not None and fam != family:
                continue
            out.extend(e for e in effs if e.significant)
        return sorted(out, key=lambda e: abs(e.statistic), reverse=True)


def run_diagnostics(
    symbol: str = "BTCUSDT",
    timeframe: str = "1h",
    *,
    train_end: str = FORWARD_LOCKBOX_START,
    external_timeframe: str | None = None,
    horizons: tuple[int, ...] = (1, 6, 24),
    confluence_symbols: tuple[str, ...] = ("DXY", "SPX", "VIX", "XAUUSD"),
    structure_peers: tuple[str, ...] = ("DXY", "XAUUSD", "ETHUSDT"),
    include_funding: bool = True,
    include_structure: bool = True,
    seed: int = 0,
) -> DiagnosticsResult:
    """Full descriptive pass for one symbol at one timeframe."""
    ensure_artifact_dirs()
    ohlcv = load_ohlcv(symbol, timeframe)
    ohlcv = ohlcv[ohlcv.index < pd.Timestamp(train_end, tz="UTC")]
    if len(ohlcv) < 5000:
        raise ValueError(f"{symbol} {timeframe}: only {len(ohlcv)} training bars")

    ext_tf = external_timeframe or timeframe
    ext_symbols = [s.symbol for s in available_externals(ext_tf)]
    if not ext_symbols:
        ext_tf = "1d"
        ext_symbols = [s.symbol for s in available_externals("1d")]

    panel = crossasset.external_panel_for(ohlcv, ext_symbols, ext_tf)
    value_cols = [c for c in panel.columns if not c.endswith("__age_sec")]

    if include_funding:
        panel = _attach_funding(panel, symbol)
        value_cols = [c for c in panel.columns if not c.endswith("__age_sec")]

    run_id = f"diag_{symbol}_{timeframe}_{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}"
    result = DiagnosticsResult(
        run_id=run_id,
        symbol=symbol,
        timeframe=timeframe,
        n_bars=len(ohlcv),
        train_start=str(ohlcv.index[0]),
        train_end=str(ohlcv.index[-1]),
    )

    h_mid = horizons[len(horizons) // 2]

    result.families["autocorrelation"] = structure.autocorrelation(ohlcv["close"])
    result.families["mean_reversion"] = structure.mean_reversion(ohlcv, horizon=h_mid)
    result.families["momentum"] = structure.momentum(ohlcv, horizon=h_mid)
    result.families["seasonality"] = structure.seasonality(ohlcv, horizon=h_mid)
    result.families["volatility_clustering"] = structure.volatility_clustering(ohlcv)
    result.families["regime"] = structure.regime_conditional(ohlcv, horizon=h_mid)
    result.families["cycles"] = structure.cycles(ohlcv["close"], seed=seed)
    result.families["nonlinear_lag"] = structure.nonlinear_lag(ohlcv, horizon=h_mid)

    result.families["lead_lag"] = crossasset.lead_lag_scan(ohlcv, panel, horizons=horizons)
    result.families["contemporaneous"] = crossasset.contemporaneous_scan(ohlcv, panel)
    result.families["transfer_entropy"] = crossasset.transfer_entropy_scan(
        ohlcv, panel, horizon=h_mid, n_surrogates=100
    )
    result.families["regime_crossasset"] = crossasset.regime_conditional_correlation(
        ohlcv, panel, horizon=h_mid
    )

    conf_syms = [s for s in confluence_symbols if s in value_cols]
    if conf_syms:
        result.families["confluence"] = confluence.confluence_table(
            ohlcv, panel, conf_syms, horizon=max(horizons)
        )
        result.families["marginal"] = confluence.marginal_contribution(
            ohlcv, panel, conf_syms, horizon=max(horizons)
        )
        result.notes["state_space"] = confluence.state_space_report(conf_syms, len(ohlcv))

    if include_structure:
        try:
            result.families["structure_label"] = marketstructure.structure_label_effect(
                ohlcv, symbol, timeframe, horizons=(horizons[0], h_mid, max(horizons))
            )
            result.families["fibonacci_placebo"] = marketstructure.fibonacci_placebo_test(
                ohlcv, symbol, timeframe, horizons=(h_mid, max(horizons))
            )
            result.families["support_resistance"] = marketstructure.support_resistance_effect(
                ohlcv, symbol, timeframe, horizons=(h_mid, max(horizons))
            )
            peers = tuple(s for s in structure_peers if s != symbol)
            result.families["structure_confluence"] = marketstructure.structure_confluence(
                ohlcv, symbol, timeframe, peers, horizon=max(horizons)
            )
            result.notes["structure_source"] = str(INDICATORS_DB)
            result.notes["structure_peers"] = list(peers)
        except FileNotFoundError as exc:
            # A missing warehouse is a recorded absence, not a silent skip: otherwise a
            # report with no structure section is indistinguishable from one where
            # structure was tested and found nothing.
            result.notes["structure_unavailable"] = str(exc)

    pulses = events.detect_pulses(ohlcv)
    result.notes["n_pulses"] = int(len(pulses))
    if len(pulses) >= 30:
        result.families["pre_event"] = events.pre_event_displacement(
            panel[value_cols], ohlcv, pulses, seed=seed
        )
        result.families["post_pulse"] = events.pulse_forward_outcome(ohlcv, pulses)

    result.notes["external_timeframe"] = ext_tf
    result.notes["external_series"] = value_cols
    result.notes["n_external"] = len(value_cols)
    return result


def _attach_funding(panel: pd.DataFrame, symbol: str) -> pd.DataFrame:
    """Add funding rate and a cumulative funding pressure column, causally aligned.

    Funding is the only series in the warehouse that measures positioning rather than
    price: a persistently positive rate means longs are paying to stay long, which is
    crowding rather than a valuation.
    """
    try:
        funding = load_funding(symbol)
    except (ValueError, FileNotFoundError):
        return panel

    from llm2.data.macro import align_causal

    aligned = align_causal(funding, pd.DatetimeIndex(panel.index))
    out = panel.copy()
    # The rate itself, as a stationary level. A persistently positive rate means longs are
    # paying to stay long, so the level is the crowding measure; the downstream scan is told
    # not to difference it. An earlier version stored exp(cumsum(rate)) instead, which both
    # charged funding hourly rather than at the three daily settlements and produced a
    # near-integrated series that the unit-root guard correctly refused.
    out["FUNDING_RATE"] = aligned["value"]
    out["FUNDING_RATE__age_sec"] = aligned["age_sec"]
    return out


# ------------------------------------------------------------------------- persistence


def persist(result: DiagnosticsResult, db_path=None) -> None:
    path = db_path or RESEARCH_DB
    conn = sqlite3.connect(path, timeout=60.0)
    try:
        conn.executescript(DIAGNOSTICS_SCHEMA)
        conn.execute(
            "INSERT OR REPLACE INTO diagnostics_runs "
            "(run_id, created_at, symbol, timeframe, train_start, train_end, n_bars, n_external, config_json) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            (
                result.run_id,
                datetime.now(timezone.utc).isoformat(),
                result.symbol,
                result.timeframe,
                result.train_start,
                result.train_end,
                result.n_bars,
                int(result.notes.get("n_external", 0)),
                json.dumps(result.notes, default=str),
            ),
        )
        rows = [
            (
                result.run_id,
                family,
                e.name,
                _f(e.statistic),
                int(e.n),
                _f(e.p_value),
                _f(e.q_value),
                _f(e.ci_low),
                _f(e.ci_high),
                int(e.significant),
                json.dumps(e.detail, default=str),
            )
            for family, effs in result.families.items()
            for e in effs
        ]
        conn.executemany(
            "INSERT OR REPLACE INTO diagnostics_effects "
            "(run_id, family, name, statistic, n, p_value, q_value, ci_low, ci_high, significant, detail_json) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            rows,
        )
        conn.commit()
    finally:
        conn.close()


def _f(x) -> float | None:
    return None if x is None or not np.isfinite(x) else float(x)


# ----------------------------------------------------------------------------- render


def render_markdown(result: DiagnosticsResult, *, top_n: int = 12) -> str:
    lines: list[str] = []
    add = lines.append

    add(f"# Diagnostics: {result.symbol} {result.timeframe}")
    add("")
    add(f"Run `{result.run_id}`")
    add("")
    add(f"- Training window: {result.train_start} to {result.train_end} ({result.n_bars:,} bars)")
    add(f"- External series aligned: {result.notes.get('n_external', 0)} "
        f"at {result.notes.get('external_timeframe')}")
    add(f"- Pulses detected: {result.notes.get('n_pulses', 0)}")
    add("")
    add("Training window only; the forward lockbox is untouched. Nothing here is a strategy: "
        "surviving hypotheses must be preregistered before any walk-forward.")
    add("")

    survivors = result.survivors()
    add("## Headline")
    add("")
    if survivors:
        add(f"**{len(survivors)} effects survive false-discovery-rate control** across "
            f"{sum(len(v) for v in result.families.values())} tests.")
    else:
        add(f"**Nothing survives false-discovery-rate control** across "
            f"{sum(len(v) for v in result.families.values())} tests.")
    add("")

    add("| Family | Tests | Survive FDR | Strongest surviving effect |")
    add("| --- | ---: | ---: | --- |")
    for family, effs in result.families.items():
        sig = [e for e in effs if e.significant]
        best = max(sig, key=lambda e: abs(e.statistic)).name if sig else "-"
        add(f"| {family} | {len(effs)} | {len(sig)} | {best} |")
    add("")

    for family, effs in result.families.items():
        if not effs:
            continue
        add(f"## {family}")
        add("")
        frame = effects_to_frame(effs)
        ranked = frame.reindex(frame["statistic"].abs().sort_values(ascending=False).index)
        add(_table(ranked.head(top_n)))
        add("")

    if "state_space" in result.notes:
        ss = result.notes["state_space"]
        add("## Confluence state space")
        add("")
        add(f"{ss['n_symbols']} series give {ss['states_possible']} joint states; "
            f"{ss['rows']:,} bars support at most {ss['max_states_supportable']} states "
            f"at {ss['min_samples_per_state']} observations each.")
        add("")

    return "\n".join(lines)


def _table(frame: pd.DataFrame) -> str:
    cols = [c for c in ("name", "statistic", "n", "p_value", "q_value", "significant") if c in frame]
    head = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join("---" for _ in cols) + " |"
    rows = []
    for _, r in frame[cols].iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if isinstance(v, (float, np.floating)):
                cells.append("-" if not np.isfinite(v) else (f"{v:.4g}" if abs(v) < 1e4 else f"{v:.3e}"))
            else:
                cells.append(str(v))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join([head, sep, *rows])


def write_report(result: DiagnosticsResult) -> str:
    out_dir = ARTIFACTS / "reports" / "diagnostics"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{result.run_id}.md"
    path.write_text(render_markdown(result), encoding="utf-8")

    frames = []
    for family, effs in result.families.items():
        f = effects_to_frame(effs)
        if not f.empty:
            f.insert(0, "family", family)
            frames.append(f)
    if frames:
        pd.concat(frames, ignore_index=True).to_csv(out_dir / f"{result.run_id}.csv", index=False)
    return str(path)
