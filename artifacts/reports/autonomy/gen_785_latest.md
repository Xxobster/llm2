# Autonomy public-indicator hunt gen 785

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T141827Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1520_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1520_below_at_h` | one_head_filter_pi_star | 285 | 23.2819 | 1.7480 | 0.6561 | 3.8972 | 0.0183 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1520_below_at_h` | one_head_filter_pi_star | 296 | 24.1805 | 1.6770 | 0.6520 | 3.8077 | 0.0168 | 0.3243 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1520_above_at_h` | one_head_filter_pi_star | 41 | 3.6056 | 1.3550 | 0.6098 | 0.8689 | 0.0127 | 0.2683 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1520_below_at_h` | one_head_filter_pi_star | 285 | 23.3047 | 1.7634 | 0.6456 | 3.9531 | 0.0119 | 0.3298 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1520_below_at_h` | one_head_filter_pi_star | 276 | 22.5688 | 1.6790 | 0.6377 | 3.6930 | 0.0111 | 0.3225 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1520_above_at_h` | one_head_filter_pi_star | 103 | 8.3987 | 1.6000 | 0.6602 | 1.9926 | 0.0086 | 0.2524 | ok | RAN |
| ETHUSDT | 4 | `ema1520_above_at_h` | one_head_filter_pi_star | 45 | 3.9573 | 1.2103 | 0.6000 | 0.5579 | 0.0085 | 0.2667 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1520_above_at_h` | one_head_filter_pi_star | 105 | 8.5617 | 1.5948 | 0.6476 | 2.0159 | 0.0083 | 0.2476 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1520_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1520_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
