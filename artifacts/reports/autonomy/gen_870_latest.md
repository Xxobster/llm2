# Autonomy public-indicator hunt gen 870

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T222347Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma450_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0471 | 0.6943 | 4.5532 | 0.0240 | 0.3886 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma450_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9980 | 0.6957 | 4.3662 | 0.0237 | 0.3913 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma450_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2304 | 0.7000 | 4.2718 | 0.0167 | 0.3824 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma450_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1051 | 0.6833 | 4.1694 | 0.0155 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma450_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2305 | 0.5882 | 1.2065 | 0.0080 | 0.2193 | ok | RAN |
| SOLUSDT | 8 | `wma450_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4717 | 0.6075 | 2.2438 | 0.0071 | 0.2688 | ok | RAN |
| ETHUSDT | 8 | `wma450_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1859 | 0.6010 | 0.9856 | 0.0066 | 0.2124 | ok | RAN |
| SOLUSDT | 4 | `wma450_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3297 | 0.5885 | 1.6743 | 0.0054 | 0.2604 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma450_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma450_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma450_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma450_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma450_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma450_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma450_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma450_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma450_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma450_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma450_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma450_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma450_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma450_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma450_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma450_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
