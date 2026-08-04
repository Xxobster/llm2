CREATE TABLE IF NOT EXISTS generations (
    generation_id TEXT PRIMARY KEY,
    preregistered_at TEXT NOT NULL,
    max_trials INTEGER NOT NULL DEFAULT 200,
    hypothesis TEXT,
    config_hash TEXT,
    status TEXT NOT NULL DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS trials (
    trial_id TEXT PRIMARY KEY,
    generation_id TEXT NOT NULL REFERENCES generations(generation_id),
    tier INTEGER NOT NULL DEFAULT 0,
    seed INTEGER,
    symbol TEXT,
    timeframe TEXT,
    target TEXT,
    feature_space TEXT,
    model TEXT,
    params_json TEXT,
    inner_score REAL,
    outer_score REAL,
    outer_pf REAL,
    outer_trades INTEGER,
    notes TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TEXT NOT NULL,
    finished_at TEXT
);

CREATE TABLE IF NOT EXISTS forecasts (
    forecast_id TEXT PRIMARY KEY,
    trial_id TEXT NOT NULL REFERENCES trials(trial_id),
    ts_ms INTEGER NOT NULL,
    symbol TEXT,
    target TEXT,
    payload_json TEXT
);

CREATE TABLE IF NOT EXISTS forecast_results (
    result_id TEXT PRIMARY KEY,
    forecast_id TEXT NOT NULL REFERENCES forecasts(forecast_id),
    metric_name TEXT NOT NULL,
    metric_value REAL,
    computed_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS evaluation_runs (
    run_id TEXT PRIMARY KEY,
    trial_id TEXT REFERENCES trials(trial_id),
    run_type TEXT NOT NULL,
    gates_json TEXT,
    readiness TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interactions (
    interaction_id TEXT PRIMARY KEY,
    session_id TEXT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    tags TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS feedback (
    feedback_id TEXT PRIMARY KEY,
    interaction_id TEXT REFERENCES interactions(interaction_id),
    label TEXT,
    notes TEXT,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_trials_generation ON trials(generation_id);
CREATE INDEX IF NOT EXISTS idx_forecasts_trial ON forecasts(trial_id);
CREATE INDEX IF NOT EXISTS idx_interactions_session ON interactions(session_id);
