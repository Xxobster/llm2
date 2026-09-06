# Autonomy public-indicator hunt gen 1142

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T035459Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma620_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1319 | 0.7059 | 4.6016 | 0.0249 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma620_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.1003 | 0.6990 | 4.7313 | 0.0241 | 0.3622 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma620_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8776 | 0.6550 | 3.7758 | 0.0133 | 0.3550 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma620_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8093 | 0.6564 | 3.5176 | 0.0125 | 0.3641 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma620_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5944 | 0.6203 | 2.7415 | 0.0091 | 0.2674 | ok | RAN |
| ETHUSDT | 8 | `wma620_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2572 | 0.6080 | 1.3219 | 0.0089 | 0.2102 | ok | RAN |
| SOLUSDT | 8 | `wma620_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5323 | 0.6054 | 2.5278 | 0.0086 | 0.2703 | ok | RAN |
| ETHUSDT | 4 | `wma620_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.1928 | 0.5968 | 0.9994 | 0.0070 | 0.2097 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma620_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma620_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
