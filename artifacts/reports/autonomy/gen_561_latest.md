# Autonomy public-indicator hunt gen 561

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T215736Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema960_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 1.8459 | 0.6667 | 4.0037 | 0.0199 | 0.3458 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema960_below_at_h` | one_head_filter_pi_star | 245 | 20.0143 | 1.6054 | 0.6449 | 3.2336 | 0.0159 | 0.3388 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema960_below_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 1.8727 | 0.6542 | 4.0528 | 0.0129 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema960_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.7420 | 0.6417 | 3.7309 | 0.0115 | 0.2992 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema960_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.6612 | 0.6379 | 2.2791 | 0.0096 | 0.3190 | ok | RAN |
| SOLUSDT | 4 | `ema960_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.6506 | 0.6343 | 2.3984 | 0.0096 | 0.3134 | ok | RAN |
| ETHUSDT | 8 | `ema960_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.1915 | 0.5887 | 0.8954 | 0.0073 | 0.2128 | ok | RAN |
| ETHUSDT | 4 | `ema960_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 1.1526 | 0.5852 | 0.7044 | 0.0060 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema960_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema960_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
