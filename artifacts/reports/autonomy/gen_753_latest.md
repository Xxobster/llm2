# Autonomy public-indicator hunt gen 753

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T110108Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema1440_below_at_h` | one_head_filter_pi_star | 292 | 23.8537 | 1.7930 | 0.6610 | 4.1684 | 0.0189 | 0.3253 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1440_below_at_h` | one_head_filter_pi_star | 296 | 24.1805 | 1.6090 | 0.6453 | 3.4762 | 0.0156 | 0.3209 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1440_above_at_h` | one_head_filter_pi_star | 83 | 6.8499 | 1.3424 | 0.6024 | 1.1510 | 0.0136 | 0.2530 | ok | RAN |
| SOLUSDT | 8 | `ema1440_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 1.7329 | 0.6418 | 3.7569 | 0.0119 | 0.3321 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1440_above_at_h` | one_head_filter_pi_star | 68 | 5.7863 | 1.2672 | 0.5882 | 0.8260 | 0.0110 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ema1440_below_at_h` | one_head_filter_pi_star | 280 | 22.8958 | 1.6553 | 0.6321 | 3.5475 | 0.0109 | 0.3179 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1440_above_at_h` | one_head_filter_pi_star | 102 | 8.3185 | 1.6521 | 0.6569 | 2.0620 | 0.0090 | 0.2451 | ok | RAN |
| SOLUSDT | 4 | `ema1440_above_at_h` | one_head_filter_pi_star | 103 | 8.3987 | 1.6139 | 0.6505 | 1.9725 | 0.0089 | 0.2718 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1440_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0423 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1440_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0626 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
