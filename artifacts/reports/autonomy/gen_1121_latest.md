# Autonomy public-indicator hunt gen 1121

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T013228Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2360_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2360_below_at_h` | one_head_filter_pi_star | 360 | 29.2867 | 1.6190 | 0.6472 | 3.9318 | 0.0165 | 0.2972 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2360_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5814 | 0.6399 | 3.4941 | 0.0154 | 0.3006 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2360_below_at_h` | one_head_filter_pi_star | 276 | 22.4531 | 1.9400 | 0.6630 | 4.5119 | 0.0140 | 0.3297 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2360_below_at_h` | one_head_filter_pi_star | 278 | 22.6158 | 1.8589 | 0.6511 | 4.2683 | 0.0128 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2360_above_at_h` | one_head_filter_pi_star | 105 | 8.7269 | 1.6785 | 0.6476 | 2.2014 | 0.0100 | 0.2762 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2360_above_at_h` | one_head_filter_pi_star | 110 | 9.0411 | 1.5845 | 0.6273 | 2.0378 | 0.0086 | 0.2636 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2360_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.7706 | 0.3529 | -0.4312 | -0.0225 | 0.1176 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2360_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0463 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2360_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2360_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ema2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
