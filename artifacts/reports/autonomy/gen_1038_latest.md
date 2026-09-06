# Autonomy public-indicator hunt gen 1038

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T151434Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma555_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9898 | 0.6979 | 4.4214 | 0.0230 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma555_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9212 | 0.6866 | 4.2458 | 0.0220 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma555_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.8995 | 0.6667 | 3.6676 | 0.0134 | 0.3548 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma555_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.9086 | 0.6718 | 3.7971 | 0.0134 | 0.3641 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma555_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.5024 | 0.6122 | 2.4561 | 0.0079 | 0.2653 | ok | RAN |
| ETHUSDT | 8 | `wma555_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2195 | 0.6000 | 1.1568 | 0.0077 | 0.2316 | ok | RAN |
| SOLUSDT | 8 | `wma555_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4755 | 0.6064 | 2.2959 | 0.0073 | 0.2660 | ok | RAN |
| ETHUSDT | 4 | `wma555_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.1974 | 0.5899 | 1.0329 | 0.0072 | 0.2079 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma555_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma555_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma555_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma555_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
