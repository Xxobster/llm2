"""SQLite schema for pivot multi-timeframe research (additive catalog)."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from llm2.pivot.paths import PIVOT_DATA_DIR, PIVOT_DB_DEFAULT

SCHEMA_VERSION = 1

_MIGRATIONS: list[str] = [
    """
    CREATE TABLE IF NOT EXISTS schema_meta (
      key TEXT PRIMARY KEY,
      value TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS label_configs (
      config_id TEXT PRIMARY KEY,
      config_json TEXT NOT NULL,
      config_sha256 TEXT NOT NULL,
      created_utc TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS pivot_events (
      event_id INTEGER PRIMARY KEY AUTOINCREMENT,
      exchange TEXT NOT NULL,
      category TEXT NOT NULL DEFAULT 'linear',
      symbol TEXT NOT NULL,
      pivot_timeframe TEXT NOT NULL,
      pivot_side TEXT NOT NULL CHECK (pivot_side IN ('high','low')),
      pivot_origin_ts_ms INTEGER NOT NULL,
      confirmed_at_ts_ms INTEGER NOT NULL,
      pivot_price REAL NOT NULL,
      pivot_strength REAL,
      left_prominence_atr REAL,
      right_reversal_atr REAL,
      reversal_pct REAL,
      max_scale_membership TEXT,
      label_family TEXT NOT NULL,
      label_config_version TEXT NOT NULL,
      ambiguous INTEGER NOT NULL DEFAULT 0,
      UNIQUE (
        exchange, category, symbol, pivot_timeframe, pivot_side,
        pivot_origin_ts_ms, label_family, label_config_version
      )
    );
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_pivot_events_confirm
      ON pivot_events(symbol, pivot_timeframe, confirmed_at_ts_ms);
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_pivot_events_origin
      ON pivot_events(symbol, pivot_timeframe, pivot_origin_ts_ms);
    """,
    """
    CREATE TABLE IF NOT EXISTS pivot_cross_scale_membership (
      member_id INTEGER PRIMARY KEY AUTOINCREMENT,
      child_event_id INTEGER NOT NULL,
      parent_event_id INTEGER NOT NULL,
      match_score REAL,
      price_tol_pct REAL,
      time_tol_ms INTEGER,
      FOREIGN KEY(child_event_id) REFERENCES pivot_events(event_id),
      FOREIGN KEY(parent_event_id) REFERENCES pivot_events(event_id),
      UNIQUE(child_event_id, parent_event_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS data_gaps (
      gap_id INTEGER PRIMARY KEY AUTOINCREMENT,
      exchange TEXT NOT NULL,
      symbol TEXT NOT NULL,
      timeframe TEXT NOT NULL,
      series TEXT NOT NULL,
      start_ts_ms INTEGER NOT NULL,
      end_ts_ms INTEGER NOT NULL,
      n_missing INTEGER,
      note TEXT,
      UNIQUE(exchange, symbol, timeframe, series, start_ts_ms, end_ts_ms)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS model_runs (
      run_id TEXT PRIMARY KEY,
      generation_id TEXT NOT NULL,
      git_commit TEXT,
      config_sha256 TEXT,
      seed INTEGER,
      data_snapshot_id TEXT,
      created_utc TEXT NOT NULL,
      notes TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS fold_predictions (
      pred_id INTEGER PRIMARY KEY AUTOINCREMENT,
      run_id TEXT NOT NULL,
      fold_index INTEGER NOT NULL,
      symbol TEXT NOT NULL,
      decision_ts_ms INTEGER NOT NULL,
      target_timeframe TEXT NOT NULL,
      horizon TEXT NOT NULL,
      p_high REAL,
      p_low REAL,
      p_none REAL,
      FOREIGN KEY(run_id) REFERENCES model_runs(run_id),
      UNIQUE(run_id, fold_index, symbol, decision_ts_ms, target_timeframe, horizon)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS calibration_results (
      cal_id INTEGER PRIMARY KEY AUTOINCREMENT,
      run_id TEXT NOT NULL,
      method TEXT NOT NULL,
      target_timeframe TEXT NOT NULL,
      horizon TEXT NOT NULL,
      metrics_json TEXT NOT NULL,
      FOREIGN KEY(run_id) REFERENCES model_runs(run_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS pivot_forecasts (
      forecast_id INTEGER PRIMARY KEY AUTOINCREMENT,
      run_id TEXT NOT NULL,
      exchange TEXT NOT NULL,
      symbol TEXT NOT NULL,
      decision_ts_ms INTEGER NOT NULL,
      target_timeframe TEXT NOT NULL,
      horizon TEXT NOT NULL,
      p_first_high REAL,
      p_first_low REAL,
      p_none REAL,
      p_cum_any REAL,
      e_time_to_pivot REAL,
      e_rev_pct_high REAL,
      e_rev_pct_low REAL,
      q10_rev REAL, q25_rev REAL, q50_rev REAL, q75_rev REAL, q90_rev REAL,
      e_mfe_pct REAL,
      e_mae_pct REAL,
      uncertainty REAL,
      data_mask INTEGER,
      model_version TEXT,
      feature_set_version TEXT,
      data_snapshot_id TEXT,
      created_utc TEXT NOT NULL,
      UNIQUE(run_id, symbol, decision_ts_ms, target_timeframe, horizon)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS training_samples (
      sample_id INTEGER PRIMARY KEY AUTOINCREMENT,
      symbol TEXT NOT NULL,
      decision_ts_ms INTEGER NOT NULL,
      target_timeframe TEXT NOT NULL,
      label_family TEXT NOT NULL,
      label_config_version TEXT NOT NULL,
      y_first_side TEXT,
      y_time_to_event_bars INTEGER,
      y_rev_pct REAL,
      feature_blob_id TEXT,
      UNIQUE(symbol, decision_ts_ms, target_timeframe, label_family, label_config_version)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS orderbook_quality (
      qid INTEGER PRIMARY KEY AUTOINCREMENT,
      exchange TEXT NOT NULL,
      symbol TEXT NOT NULL,
      ts_ms INTEGER NOT NULL,
      warning TEXT NOT NULL,
      detail TEXT
    );
    """,
]


def ensure_pivot_db(path: Path | None = None) -> Path:
    """Create parent dir, apply migrations, stamp schema version."""
    db_path = Path(path) if path is not None else PIVOT_DB_DEFAULT
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(db_path), timeout=120.0)
    try:
        con.execute("PRAGMA journal_mode=WAL")
        con.execute("PRAGMA synchronous=NORMAL")
        for sql in _MIGRATIONS:
            con.executescript(sql)
        con.execute(
            "INSERT INTO schema_meta(key, value) VALUES('schema_version', ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (str(SCHEMA_VERSION),),
        )
        con.commit()
    finally:
        con.close()
    return db_path


def connect_pivot_db(path: Path | None = None, *, readonly: bool = False) -> sqlite3.Connection:
    db_path = ensure_pivot_db(path) if not readonly else Path(path or PIVOT_DB_DEFAULT)
    if readonly:
        return sqlite3.connect(f"file:{db_path}?mode=ro", uri=True, timeout=120.0)
    return sqlite3.connect(str(db_path), timeout=120.0)
