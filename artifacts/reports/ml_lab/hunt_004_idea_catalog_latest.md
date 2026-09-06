# ML lab hunt 004 (30 named ideas)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T162716Z`.
Rows: 449. Event-study skill pass: **22**. Tradesim screen pass: **2**.
Screen: bars before 2022-01-01. Adaptive channel offsets are frozen at the decision bar.

| Symbol | TF | Family | Idea | n | DA | signed | net | PF | ebr | skill | screen |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 1d | power | `power_ema_stack_long` | 152 | 0.730 | 0.048 | 0.046 |  |  | Y | fail |
| ETHUSDT | 1d | power | `power_ema_stack_long` | 158 | 0.627 | 0.038 | 0.037 |  |  | Y | fail |
| ETHUSDT | 1d | power | `power_donchian_er` | 68 | 0.559 | 0.035 | 0.034 |  |  |  | fail |
| ETHUSDT | 1d | mix | `mix_fastslow_ewma` | 653 | 0.560 | 0.022 | 0.021 |  |  | Y | fail |
| BTCUSDT | 1d | power | `power_atr_expand` | 185 | 0.535 | 0.022 | 0.021 |  |  | Y | fail |
| ETHUSDT | 1d | surf | `surf_inside_mother` | 157 | 0.605 | 0.021 | 0.020 |  |  | Y | fail |
| SOLUSDT | 4h | power | `power_ema_stack_long` | 386 | 0.565 | 0.021 | 0.020 | 2.417 | 0.596 | Y | fail |
| ETHUSDT | 1d | mix | `mix_drift_theta` | 718 | 0.540 | 0.019 | 0.018 |  |  | Y | fail |
| ETHUSDT | 1d | mix | `mix_holt_slope` | 714 | 0.560 | 0.017 | 0.016 |  |  | Y | fail |
| BTCUSDT | 1d | power | `power_linreg_er` | 287 | 0.575 | 0.017 | 0.016 |  |  | Y | fail |
| BTCUSDT | 1d | mix | `mix_drift_theta` | 795 | 0.547 | 0.015 | 0.014 |  |  | Y | fail |
| ETHUSDT | 1d | power | `power_linreg_er` | 246 | 0.524 | 0.015 | 0.013 |  |  | Y | fail |
| ETHUSDT | 1d | mix | `mix_roc_accel` | 417 | 0.518 | 0.014 | 0.013 |  |  | Y | fail |
| BTCUSDT | 1d | mix | `mix_fastslow_ewma` | 729 | 0.539 | 0.014 | 0.013 |  |  | Y | fail |
| BTCUSDT | 1d | power | `power_sma_pullback` | 42 | 0.524 | 0.012 | 0.011 |  |  |  | fail |
| BTCUSDT | 1d | mix | `mix_holt_slope` | 794 | 0.525 | 0.012 | 0.011 |  |  | Y | fail |
| ETHUSDT | 1d | power | `power_sma_pullback` | 73 | 0.562 | 0.012 | 0.011 |  |  |  | fail |
| SOLUSDT | 1h | surf | `surf_tp_vwap` | 73 | 0.671 | 0.011 | 0.010 |  |  |  | fail |
| ETHUSDT | 4h | power | `power_ema_stack_long` | 887 | 0.582 | 0.011 | 0.010 | 1.879 | 0.300 | Y | fail |
| BTCUSDT | 1d | power | `power_donchian_er` | 63 | 0.540 | 0.008 | 0.007 |  |  |  | fail |
| SOLUSDT | 4h | mix | `mix_turtle_hurst` | 283 | 0.562 | 0.008 | 0.007 | 1.711 | 0.893 | Y | fail |
| SOLUSDT | 4h | mix | `mix_holt_slope` | 2790 | 0.509 | 0.008 | 0.006 |  |  |  | fail |
| BTCUSDT | 1d | power | `power_volume_z` | 48 | 0.500 | 0.007 | 0.006 |  |  |  | fail |
| SOLUSDT | 4h | mix | `mix_drift_theta` | 2702 | 0.508 | 0.006 | 0.005 |  |  |  | fail |
| SOLUSDT | 4h | mix | `mix_fastslow_ewma` | 2413 | 0.499 | 0.006 | 0.005 |  |  |  | fail |
| BTCUSDT | 15m | power | `power_clv_range` | 60 | 0.517 | 0.006 | 0.005 |  |  |  | fail |
| SOLUSDT | 1h | power | `power_ema_stack_long` | 1570 | 0.522 | 0.005 | 0.004 | 1.576 | 0.187 | Y | PASS |
| ETHUSDT | 4h | power | `power_donchian_volume` | 211 | 0.493 | 0.005 | 0.004 |  |  |  | fail |
| BTCUSDT | 4h | power | `power_ema_stack_long` | 783 | 0.512 | 0.004 | 0.003 | 1.686 | 0.235 | Y | PASS |
| ETHUSDT | 15m | power | `power_vol_expand` | 147 | 0.653 | 0.004 | 0.003 | 5.196 | 0.171 | Y | fail |
| BTCUSDT | 1d | mix | `mix_roc_accel` | 470 | 0.494 | 0.004 | 0.002 |  |  |  | fail |
| BTCUSDT | 4h | power | `power_donchian_volume` | 218 | 0.491 | 0.003 | 0.002 |  |  |  | fail |
| ETHUSDT | 1h | power | `power_ema_stack_long` | 2651 | 0.535 | 0.003 | 0.002 | 1.194 | 0.092 | Y | fail |
| BTCUSDT | 1h | power | `power_volume_z` | 1056 | 0.508 | 0.003 | 0.002 |  |  |  | fail |
| BTCUSDT | 4h | power | `power_donchian_er` | 330 | 0.470 | 0.003 | 0.001 |  |  |  | fail |
| ETHUSDT | 4h | mix | `mix_holt_slope` | 4542 | 0.508 | 0.002 | 0.001 |  |  |  | fail |
| SOLUSDT | 1h | mix | `mix_turtle_hurst` | 1207 | 0.541 | 0.002 | 0.001 | 0.903 | 0.697 | Y | fail |
| ETHUSDT | 4h | mix | `mix_fastslow_ewma` | 3988 | 0.500 | 0.002 | 0.001 |  |  |  | fail |
| BTCUSDT | 4h | surf | `surf_linreg_channel` | 96 | 0.531 | 0.002 | 0.000 | 0.823 | 0.778 | Y | fail |
| BTCUSDT | 4h | power | `power_atr_expand` | 1002 | 0.504 | 0.002 | 0.000 |  |  |  | fail |
