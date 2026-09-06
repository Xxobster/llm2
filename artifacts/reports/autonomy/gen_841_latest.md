# Autonomy public-indicator hunt gen 841

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T193213Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1660_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1660_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.5878 | 0.6409 | 3.6470 | 0.0159 | 0.3116 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1660_below_at_h` | one_head_filter_pi_star | 309 | 25.2425 | 1.6054 | 0.6440 | 3.4623 | 0.0155 | 0.3172 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema1660_above_at_h` | one_head_filter_pi_star | 45 | 3.9573 | 1.3762 | 0.6222 | 0.9170 | 0.0128 | 0.3111 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1660_below_at_h` | one_head_filter_pi_star | 276 | 22.5688 | 1.7548 | 0.6449 | 3.9557 | 0.0121 | 0.3225 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1660_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 1.7630 | 0.6423 | 3.9028 | 0.0121 | 0.3192 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1660_above_at_h` | one_head_filter_pi_star | 77 | 6.2797 | 1.7015 | 0.6623 | 1.9515 | 0.0093 | 0.2338 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1660_above_at_h` | one_head_filter_pi_star | 102 | 8.3836 | 1.5379 | 0.6471 | 1.7678 | 0.0080 | 0.2843 | ok | RAN |
| ETHUSDT | 8 | `ema1660_above_at_h` | one_head_filter_pi_star | 42 | 3.6935 | 1.1127 | 0.5714 | 0.2924 | 0.0046 | 0.2619 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1660_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0423 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1660_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0640 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
