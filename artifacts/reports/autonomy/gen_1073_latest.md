# Autonomy public-indicator hunt gen 1073

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T193816Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2240_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0833 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema2240_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.5646 | 0.6395 | 3.5244 | 0.0153 | 0.3052 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2240_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5613 | 0.6366 | 3.4201 | 0.0150 | 0.3093 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2240_below_at_h` | one_head_filter_pi_star | 270 | 21.9650 | 1.8770 | 0.6630 | 4.2889 | 0.0131 | 0.3370 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2240_below_at_h` | one_head_filter_pi_star | 278 | 22.6158 | 1.8375 | 0.6511 | 4.1890 | 0.0127 | 0.3201 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2240_above_at_h` | one_head_filter_pi_star | 108 | 8.8767 | 1.7191 | 0.6389 | 2.3245 | 0.0101 | 0.2685 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2240_above_at_h` | one_head_filter_pi_star | 104 | 8.5479 | 1.6506 | 0.6442 | 2.0705 | 0.0090 | 0.2788 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2240_above_at_h` | one_head_filter_pi_star | 21 | 2.4677 | 0.8769 | 0.4286 | -0.3003 | -0.0066 | 0.4286 | EBR>35% | RAN |
| BTCUSDT | 8 | `ema2240_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.8469 | 0.3333 | -0.2545 | -0.0134 | 0.0667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2240_above_at_h` | one_head_filter_pi_star | 12 | 3.7398 | 0.5871 | 0.3333 | -1.6325 | -0.0295 | 0.4167 | EBR>35% | RAN |
| BTCUSDT | 4 | `ema2240_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4702 | 0.2667 | -1.0879 | -0.0601 | 0.0667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
