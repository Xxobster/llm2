# Autonomy public-indicator hunt gen 1169

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T071352Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2480_below_at_h` | one_head_filter_pi_star | 357 | 29.0427 | 1.5956 | 0.6443 | 3.8050 | 0.0162 | 0.2997 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema2480_below_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.5569 | 0.6364 | 3.3450 | 0.0150 | 0.3061 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2480_below_at_h` | one_head_filter_pi_star | 265 | 21.5583 | 1.9092 | 0.6566 | 4.3474 | 0.0139 | 0.3283 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2480_below_at_h` | one_head_filter_pi_star | 276 | 22.4531 | 1.7674 | 0.6413 | 3.9085 | 0.0119 | 0.3261 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2480_above_at_h` | one_head_filter_pi_star | 101 | 8.3014 | 1.6491 | 0.6535 | 2.0283 | 0.0096 | 0.2673 | ok | RAN |
| SOLUSDT | 4 | `ema2480_above_at_h` | one_head_filter_pi_star | 107 | 8.7945 | 1.6580 | 0.6449 | 2.1428 | 0.0092 | 0.2804 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2480_above_at_h` | one_head_filter_pi_star | 26 | 3.0553 | 0.8735 | 0.4615 | -0.3264 | -0.0065 | 0.2692 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2480_above_at_h` | one_head_filter_pi_star | 15 | 4.5265 | 0.6492 | 0.3333 | -1.3117 | -0.0226 | 0.2667 | ok | RAN |
| BTCUSDT | 4 | `ema2480_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7376 | 0.3684 | -0.5246 | -0.0260 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2480_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7376 | 0.3684 | -0.5246 | -0.0270 | 0.1053 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
