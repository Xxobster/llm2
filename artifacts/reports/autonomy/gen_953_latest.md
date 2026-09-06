# Autonomy public-indicator hunt gen 953

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T072055Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1940_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.9118 | 0.6667 | 1.7154 | 0.1098 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1940_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1940_above_at_h` | one_head_filter_pi_star | 62 | 5.4523 | 1.5172 | 0.6290 | 1.3919 | 0.0177 | 0.2742 | ok | RAN |
| ETHUSDT | 4 | `ema1940_below_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 1.6152 | 0.6415 | 3.5949 | 0.0161 | 0.3113 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1940_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5665 | 0.6393 | 3.5793 | 0.0155 | 0.3050 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1940_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.8470 | 0.6540 | 4.2048 | 0.0132 | 0.3232 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1940_below_at_h` | one_head_filter_pi_star | 270 | 22.0781 | 1.8360 | 0.6519 | 4.1841 | 0.0130 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1940_above_at_h` | one_head_filter_pi_star | 101 | 8.2370 | 1.6392 | 0.6337 | 2.0267 | 0.0087 | 0.2574 | ok | RAN |
| SOLUSDT | 4 | `ema1940_above_at_h` | one_head_filter_pi_star | 101 | 8.2370 | 1.5469 | 0.6238 | 1.7859 | 0.0076 | 0.2475 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1940_above_at_h` | one_head_filter_pi_star | 39 | 3.4297 | 0.9259 | 0.5128 | -0.2035 | -0.0036 | 0.2564 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1940_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6375 | 0.3333 | -0.7032 | -0.0411 | 0.0667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1940_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0624 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
