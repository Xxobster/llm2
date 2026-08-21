# Pivot multi-timeframe forecast — architecture & data-coverage report

**Date:** 2026-08-10 (UTC)  
**Evidence class:** RESEARCH_ONLY / architecture  
**Maximum earned readiness:** `LIVE_STOP / RESEARCH_ONLY`  
**Deliverable:** Phase 1–4 design + audited coverage (no live orders)

Audit JSON: `artifacts/reports/pivot_forecast/data_coverage_latest.json`  
Fast probe: `python scripts/audit_pivot_data_coverage_fast.py`

---

## 1. Repository integration (preserve, add)

| Existing asset | Role | Pivot module must |
|---|---|---|
| `llm2/` package | Canonical research code | **Add** `llm2/pivot/` — do not replace `llm2/labels/*` structure legs |
| `llm2/data/loader.py` | `market_ohlcv` last-trade load (`last`∪`last_price`) | Reuse; extend only for mark/index if needed |
| `D:\projectsdata\candles\market_ohlcv.sqlite` | Shared OHLCV warehouse (~22 GB) | Read; never rewrite raw rows from pivot code |
| `botsgeneral/indicators` | Swings with `pivot_ts_ms` / `confirm_ts_ms` | **Do not fork** for features; optional compare only. New **forecast labels** live under `llm2/pivot/labels` |
| `botsgeneral/leakage` + `llm2/evidence/four_proof.py` | Causality gates | Wire before any train on warehouse-joined features |
| `botsgeneral/tradesim` | Backtest engine | Optional later sim only; not phase-1 deliverable |
| `llm2/models/{baselines,classical,boosting,deep}.py` | Model ladder | Wrap; new heads in `llm2/pivot/models/` |
| `llm2/validation/folds.py` | Outer V2 calendar + lockbox | Reuse purge/embargo patterns |
| `configs/preregister/*` | Hashed hypotheses | New gen YAML before outer OOS |
| D-052…D-060 | CAUS-STRUCT / closed direction nest | Forecast module is **orthogonal**; no restore of leaked retrace features |
| `crypto_alpha/research` | **Not present** in this monorepo | Map intent → `llm2/pivot/*` |
| `C:\projects\crypthor` | Finplot conventions (later) | Visualization phase only |

**Standing defaults unchanged:** lockbox `2026-05-01`; research signal default **Binance** last in warehouse; live Bybit is product target for deployments but warehouse is currently Binance-filled → label as **RESEARCH_PROXY** until Bybit native series exist.

---

## 2. Data-coverage matrix (audited, not assumed)

### 2.1 `market_ohlcv` — last-trade best series (probe 2026-08-10)

| Source | Symbol | 1m | 5m | 15m | 30m | 1h | 4h | 1d |
|---|---|---|---|---|---|---|---|---|
| **binance** | BTCUSDT | OK ~3.4M (2020→2026-07-18) | OK ~0.72M (→2026-07-11) | OK | **MISSING** | OK ~58k (→2026-08-05) | OK | OK |
| **binance** | ETHUSDT | OK ~3.5M (→2026-08-06) | OK ~0.70M (→2026-07-11) | OK | **MISSING** | OK (union last/last_price; tip gaps historically) | OK | OK |
| **binance** | SOLUSDT | OK ~3.1M (2020-09→2026-08-03) | OK ~0.61M (→2026-07-11) | OK | **MISSING** | OK | OK | OK |
| **bybit** | BTC/ETH/SOL | **all MISSING** | all MISSING | … | … | … | … | … |

Corrections vs prior verbal coverage:

- SOL is **not** “1h only” in the shared warehouse — 1m/5m/15m/4h/1d exist.
- 30m is absent for all three (not required for the 5m→daily ladder).
- **Bybit USDT perp native OHLCV is not in `market_ohlcv`.** Any claim of Bybit historical edges requires backfill (`source=bybit`) or remains research proxy on Binance closes.

### 2.2 5-minute forecast readiness

Genuine 1m **and** 5m exist for BTC/ETH/SOL on **Binance** → 5m decision grid is feasible **without** illicit upsampling from 15m/1h.

**Tip freshness risk:** 5m tips stall ~**2026-07-11** for BTC/ETH/SOL while some 1h tips reach **2026-08-05**. Before training, refresh tips (or freeze a data-snapshot ID excluding stale 5m tips). Causal resample of 1m → 5m for the tip may fill **recent** gaps only when 1m is complete; never invent OHLC from HTFs.

### 2.3 Other stores

| Path | Finding |
|---|---|
| `market_oi.sqlite` | Tables `market_oi`, `meta` — OI source for futures features |
| `binance_funding.sqlite` | Funding history present |
| `bybit_instruments.sqlite` | Tiny instrument metadata only |
| `D:\projectsdata\orderbook\market_data_agg.sqlite` | ~71 GB aggregate (use later microstructure phases; quality masks required) |
| `trades` / `tradeshistory` | Sparse / strategy dirs — public-trade backfill still a phase dependency |
| `cryptodb/market.sqlite` | D-028: **not** a causal feature source until timing pinned |

---

## 3. Object map (types)

```
HistoricalPivotEvent
  pivot_origin_ts   # extreme bar (label may use future inside builder only)
  confirmed_at_ts   # first time right-side evidence suffices
  pivot_side        # high | low
  pivot_timeframe
  pivot_price
  pivot_strength
  left_prominence_atr
  right_reversal_atr
  reversal_pct
  max_scale_membership
  label_config_version

PivotForecast @ decision_ts (closed 5m bar)
  P(first=high | H), P(first=low | H), P(none | H)
  cumulative hazards for each configured H
  E[time_to_pivot], E[rev%|high], E[rev%|low]
  rev quantiles q10..q90
  E[MFE%], E[MAE%]
  P(|move| ≥ barrier_k)
  uncertainty, data_mask
  model_version, feature_set_version, data_snapshot_id
```

**Target at closed t:** first qualified pivot **origin** in `(t, t+H]` (legal label).  
**Feature rule:** historical pivots appear only after `confirmed_at_ts ≤ t`.

---

## 4. Label family design (phase 6)

### 4.1 Family A — volatility-normalized fractal / prominence

Per timeframe `PivotLabelConfig`:

| Field | Role |
|---|---|
| `left_bars`, `right_bars` | Window for local max/min of high/low |
| `confirm_bars` | ≥ `right_bars` typically; confirms knowability |
| `min_left_prominence_atr` | Ascent (high) / descent (low) vs ATR |
| `min_right_reversal_atr` / `min_reversal_pct` | Exit move after pivot |
| `horizons` | Forecast H list |
| `event_match_tolerance` | Cross-TF match |
| `tie_break` | Deterministic (e.g. leftmost extreme of equal highs) |

Vectorized path: rolling max/min + shifts, mask extrema, ATR series, boolean filters, then **compiled** non-max-suppression for duplicates (Numba allowed if sequential).

### 4.2 Family B — directional-change (DC)

Ordered volatility thresholds: larger threshold ⟹ monotonic exceedance of smaller (enforce in tests).

Selection between A/B is **train/inner only**, never outer OOS.

### 4.3 Ambiguous HTF ordering

If high and low pivot origins fall in the same higher-TF candle, recover order from 5m; else `ambiguous=1`.

---

## 5. Multi-timeframe alignment (features)

At closed 5m timestamp `t_close`:

- HTF bars join only if `bar_close_ts ≤ t_close` (completed bars).
- Optional separately named `partial_*` features from closed 5m bricks inside incomplete HTF only — never mixed with exchange completed OHLC.
- Future-mutation + truncation tests mandatory (reuse leakage battery patterns).

Cross-scale membership: match by side + price+time tolerance → store `pivot_cross_scale_membership`; emit conditional P matrices (measured, not forced nest).

---

## 6. Competing-risks forecast (model ladder)

Per target timeframe, discrete bins under each H:

Hazards λ_high(k), λ_low(k) → cumulative incidence + P(none)=survival. Cum. incidence **non-decreasing** in H (hard test).

Heads: hazards, quantile rev% (pinball), MFE/MAE, time-to-event.

Ladder (no jump to large NN first):

1. Unconditional / regime base rates  
2. Calibrated logistic  
3. LightGBM (and CatBoost if present)  
4. Multi-task TCN/GRU  
5. TFT / multi-res transformer  

Calibrators fit on **inner** preds only (Platt / isotonic / temperature).

Metrics: PR-AUC primary, ROC secondary, Brier, logloss, ECE, event-level precision/recall with tolerance, lead time, pinball, regime/year splits. Beat base rate + GBT on outer Brier+PR-AUC or reject NN.

---

## 7. Leakage-risk report

| Risk | Severity | Mitigation |
|---|---|---|
| Pivot features stamped at origin not confirm | HARD | Store/use `confirmed_at_ts` only in features; tests |
| Warehouse join ignoring handed OHLCV | HARD | four_proof + leakage recompute builders for any warehouse space |
| Label uses future (OK) leaking into feature matrix | HARD | Separate label store; purge ≥ max H + label right window |
| Manufacturing 5m from 15m/1h | HARD | Refuse in resampler; test |
| HTF partial as completed | HARD | Explicit column namespace + tests |
| Daily pivots treated as independent 5m rows | MED | Event-level eval; cluster CV / sample weights |
| Bybit deploy claims from Binance train | MED | RESEARCH_PROXY label; backfill plan |
| Selecting label family on outer OOS | HARD | Preregister + inner only |
| Zero-fill missing microstructure | MED | availability masks; refuse silent fill |

Past CAUS-STRUCT-001 (`last_retrace_pct`) is **out of band** for this module; do not reintroduce.

---

## 8. SQLite layout (new catalog — additive)

New DB (proposal): `D:\projectsdata\pivot\pivot_research.sqlite`  
(or `artifacts/sqlite/pivot_research.sqlite` for portable runs)

Core tables (phase 5):  
`raw_*` (views/refs to warehouse where possible), `pivot_events`, `pivot_cross_scale_membership`, `derived_features`, `training_samples`, `model_runs`, `fold_predictions`, `calibration_results`, `pivot_forecasts`, `data_gaps`, `label_configs`.

Uniqueness: `(exchange, category, symbol, timeframe, ts_ms, …)` / execution ids.

---

## 9. Module tree (additive under `llm2/pivot/`)

```
llm2/pivot/
  __init__.py
  paths.py
  schema.py              # migrations
  data/coverage.py       # audit helpers
  data/resampler.py      # 1m→5m… causal, no reverse manufacture
  labels/config.py       # PivotLabelConfig
  labels/fractal.py      # family A vectorized
  labels/directional_change.py  # family B
  labels/cross_tf.py
  features/…             # later phases
  models/…
  validation/…
  reporting/…
  inference/…
configs/pivot_forecasting.yaml
configs/preregister/structure_v1_pivot_forecast_mtf_001.yaml
tests/test_pivot_*.py
scripts/audit_pivot_data_coverage_fast.py
```

---

## 10. Implementation order (this session and next)

| Phase | Status |
|---|---|
| 1–4 Audit + architecture + leakage + label spec | **This document + coverage JSON** |
| 5 Schema/migrations | Next code |
| 6 Vectorized family A labeler + tests | Next code |
| 7+ Features, ladder, calibration, OOS | Subsequent (not claimed until measured) |

---

## 11. Unresolved risks

1. No Bybit historical OHLCV in warehouse.  
2. 5m tip lag vs 1h tip (~weeks) — snapshot ID must codify freezes.  
3. Public-trade/LIQ continuous history incomplete until collectors backfill.  
4. Daily pivot n is small — multi-task transfer may still overfit; evaluate event-level.  
5. Order-book snapshot incompleteness (`orderbook_quality`).  

---

## 12. Commands (run so far)

```text
python scripts/audit_pivot_data_coverage_fast.py
```

---

## 13. What was preserved

No existing LLM2 live pack, hunt, structure_v1 labels, or botsgeneral APIs removed or renamed. Pivot work is additive under `llm2/pivot/` and new artifacts/reports paths.
