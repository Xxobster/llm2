# Trading Project Profile — LLM2 Predictability Laboratory

Completed from verified repository and warehouse evidence. Unknown fields remain `UNRESOLVED`.

This profile contains project choices and user preferences. It cannot weaken the non-negotiable causality, accounting, evidence, authorization or live-safety rules in `TRADING_BOT_RESEARCH_STANDARD_V2.md`.

## 1. Project identity

```yaml
project_name: LLM2
repository_root: D:\projects\LLM2
project_memory_directory: docs/project_memory
research_core_version: trading_bot_v2_1
live_strategy_module: UNRESOLVED
backtest_entrypoint: llm2.backtest.run
walk_forward_entrypoint: llm2.validation.walk_forward
live_entrypoint: UNRESOLVED
research_database: artifacts/sqlite/research.sqlite
market_database: D:\projectsdata\candles\market_ohlcv.sqlite
live_database: UNRESOLVED
plotting_tool: finplot
```

## 2. Target product contract

```yaml
target_venue: bybit
product_type: linear_perpetual
symbols: [BTCUSDT, ETHUSDT, SOLUSDT, BNBUSDT, XRPUSDT, ADAUSDT, DOGEUSDT, AVAXUSDT, LINKUSDT, DOTUSDT, TRXUSDT, XLMUSDT, VETUSDT, HYPEUSDT]
primary_research_symbols: [BTCUSDT, ETHUSDT, SOLUSDT]
expansion_symbol_queue: [BNBUSDT, XRPUSDT, ADAUSDT, DOGEUSDT, AVAXUSDT, LINKUSDT, DOTUSDT, TRXUSDT, XLMUSDT, VETUSDT]
future_market_queue: [EURUSD, DXY, XAUUSD]
settlement_currency: USDT
signal_market: binance_usd_m_perp_research_proxy
execution_market: bybit_usdt_perp
signal_price_source: last
entry_price_source: last
tp_trigger_source: LastPrice
sl_trigger_source: LastPrice
liquidation_source: MarkPrice
strategy_timeframes: [15m, 1h, 4h]
execution_replay_timeframe: 1m_or_5m_touch
timezone: UTC
session_definition: 24x7
research_data_label: RESEARCH_PROXY
```

## 3. Account and order contract

```yaml
account_or_subaccount: UNRESOLVED
position_mode: one_way
margin_mode: isolated
sizing_mode: min_exchange
wallet_allocation_usdt: 10000
risk_per_trade: UNRESOLVED
max_portfolio_exposure: UNRESOLVED
max_concurrent_positions: 1
max_margin_utilization: 0.60
baseline_max_drawdown_budget: 0.20
moderate_stress_max_drawdown_budget: 0.25
max_daily_loss: UNRESOLVED
max_weekly_loss: UNRESOLVED
max_risk_of_ruin_or_loss_limit_breach: 0.01
leverage_policy: lowest_operational_leverage_meeting_frozen_capital_and_liquidation_constraints
entry_order_type: market
entry_time_in_force: IOC
maker_timeout_ms: UNRESOLVED
maker_reprice_policy: UNRESOLVED
exit_order_types: limit_tp_limit_sl
max_hold_policy: UNRESOLVED
one_position_rules: one_position_per_symbol
```

## 4. Costs and execution assumptions

```yaml
fee_source: bybit_non_vip_taker
maker_fee: 0.0002
taker_fee: 0.00055
baseline_spread_model: included_in_entry_slippage
baseline_slippage_model: entry_0.0005_tp_sl_limit_zero_exit_slip
latency_model: next_bar_open_entry
historical_funding_source: D:\projectsdata\candles\binance_funding.sqlite
maker_fill_evidence: none_use_all_taker
moderate_cost_stress: 2x_entry_slip_all_taker
severe_cost_stress: 3x_entry_slip_all_taker
round_trip_cost_hurdle: 0.0016
```

## 5. Research design and preferences

```yaml
economic_hypothesis: |
  Liquid crypto perpetual returns are near-efficient for direction;
  volatility, regime and cross-sectional rank may contain reproducible
  structure after costs. LLM2 tests seven targets and many model families
  under nested walk-forward with surrogate falsification.
candidate_budget: 200_trials_per_generation
root_random_seed: 20260802
outer_fold_count: 5
outer_scheme: expanding_calendar
inner_scheme: expanding
purge_rule: horizon_bars_both_sides
embargo_rule: horizon_bars_both_sides
forward_lockbox_start: 2026-05-01
minimum_oos_evidence: see_frozen_gate_profile
gate_profile: trading_bot_v2_1_frozen
min_complete_outer_folds: 5
min_resolved_trades_per_gating_fold: 10
min_pooled_resolved_oos_trades: 50
preferred_pooled_resolved_oos_trades: 100
annualized_daily_sharpe_gate: 1.0
hac_annualized_sharpe_gate: 0.75
pooled_profit_factor_gate: 1.20
moderate_stress_profit_factor_gate: 1.05
positive_fold_fraction_gate: 0.80
bootstrap_positive_expectancy_probability_gate: 0.90
bootstrap_min_resamples: 10000
bootstrap_method_and_block_rule: circular_block_bootstrap_block_len_from_train_acf
hac_lag_or_bandwidth_rule: newey_west_lag_floor_sqrt_n
dsr_probability_gate: 0.95
pbo_gate_when_valid: 0.20
win_rate_hard_gate: false
screening_objective_order:
  - pooled_pf_ge_1_20
  - trades_per_month_ge_4
  - maximize_annualized_daily_mtm_sharpe
```

## 6. Engine and evidence hashes

```yaml
rules_package: TRADING_BOT_CURSOR_RULES_V2.zip
standard_sha256: f78251a7683ce6458889faf75b4a2cb7fd98e3333b42b22b049e7b5f0483cbf7
frozen_gates_sha256: 89cea3c3106c26d61effb30da34ccbbbc71a8318cc08c6580687f1ec33af5bad
core_mdc_sha256: d1b46bdab397dff6adbe17446bdd85da2e5b16b20ed01c92d1a6855b8f1ee397
tradesim_source: C:\projects\botsgeneral\packages\tradesim
leakage_source: C:\projects\botsgeneral\packages\leakage
installed_at_utc: 2026-08-02T07:50:00Z
```

## 7. Alert tiers

```yaml
tier_0: predictability_audit_ledger_only
tier_1_screen_pass: beats_baselines_and_surrogate_challenge
tier_2_gate_candidate: frozen_gates_B_C_D_E_pass_ALERT_USER
tier_3_shadow_ready: full_v21_including_dsr
```

## 8. Live / VPS

```yaml
vps_host: "94.156.189.76"   # intended only — not authorized
live_process_name: UNRESOLVED
credential_reference: xxobster7   # intended account ref — not authorized
authorization_status: LIVE_STOP
maximum_earned_readiness: RESEARCH_ONLY
live_certificate: configs/live/structure_v1_lgbm_certificate.yaml  # status BLOCKED
deploy_rule: refuse_vps_deploy_without_live_certificate
```
