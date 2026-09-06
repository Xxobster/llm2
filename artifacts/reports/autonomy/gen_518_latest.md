# Autonomy public-indicator hunt gen 518

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T190655Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma230_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0633 | 0.6995 | 4.5946 | 0.0248 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma230_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9367 | 0.6811 | 4.2677 | 0.0217 | 0.3730 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma230_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.3170 | 0.7039 | 4.5848 | 0.0184 | 0.3799 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma230_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1508 | 0.6946 | 4.0355 | 0.0167 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma230_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2822 | 0.6054 | 1.3854 | 0.0094 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `wma230_above_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.2124 | 0.6050 | 1.1222 | 0.0075 | 0.2400 | ok | RAN |
| SOLUSDT | 8 | `wma230_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3543 | 0.5935 | 1.8597 | 0.0055 | 0.2664 | ok | RAN |
| SOLUSDT | 4 | `wma230_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2655 | 0.5854 | 1.4299 | 0.0042 | 0.2683 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma230_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma230_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma230_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma230_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma230_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma230_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma230_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma230_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma230_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma230_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma230_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma230_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma230_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma230_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma230_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma230_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
