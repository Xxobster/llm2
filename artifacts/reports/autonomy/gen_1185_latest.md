# Autonomy public-indicator hunt gen 1185

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T085248Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2520_below_at_h` | one_head_filter_pi_star | 359 | 29.2054 | 1.6304 | 0.6462 | 3.8908 | 0.0168 | 0.3008 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2520_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.6324 | 0.6462 | 3.7471 | 0.0167 | 0.3099 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2520_below_at_h` | one_head_filter_pi_star | 268 | 21.8023 | 1.8670 | 0.6530 | 4.1956 | 0.0127 | 0.3396 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2520_below_at_h` | one_head_filter_pi_star | 297 | 24.1615 | 1.7791 | 0.6431 | 4.1018 | 0.0119 | 0.3165 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2520_above_at_h` | one_head_filter_pi_star | 105 | 8.6105 | 1.6218 | 0.6381 | 2.0867 | 0.0093 | 0.2571 | ok | RAN |
| SOLUSDT | 8 | `ema2520_above_at_h` | one_head_filter_pi_star | 96 | 7.8738 | 1.5953 | 0.6354 | 1.8743 | 0.0090 | 0.2604 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2520_above_at_h` | one_head_filter_pi_star | 17 | 5.1300 | 0.6774 | 0.4118 | -1.4079 | -0.0193 | 0.2353 | ok | RAN |
| BTCUSDT | 4 | `ema2520_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0444 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2520_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2520_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
