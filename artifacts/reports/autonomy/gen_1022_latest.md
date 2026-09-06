# Autonomy public-indicator hunt gen 1022

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T132245Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma545_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9706 | 0.6919 | 4.2489 | 0.0228 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma545_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9534 | 0.6904 | 4.3510 | 0.0228 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma545_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 2.0813 | 0.6789 | 4.1703 | 0.0154 | 0.3632 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma545_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8599 | 0.6667 | 3.6381 | 0.0131 | 0.3590 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma545_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.5118 | 0.6042 | 2.4282 | 0.0079 | 0.2552 | ok | RAN |
| ETHUSDT | 8 | `wma545_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2161 | 0.5938 | 1.1517 | 0.0077 | 0.2292 | ok | RAN |
| ETHUSDT | 4 | `wma545_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1957 | 0.6073 | 1.0823 | 0.0071 | 0.2199 | ok | RAN |
| SOLUSDT | 4 | `wma545_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4409 | 0.6064 | 2.1489 | 0.0069 | 0.2606 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma545_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma545_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma545_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma545_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
