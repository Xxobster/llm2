# Autonomy public-indicator hunt gen 278

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T035504Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma65_cross_up` | one_head_filter_pi_star | 11 | 1.1228 | 14.7733 | 0.8182 | 2.9095 | 0.0616 | 0.2727 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma65_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.8460 | 0.6854 | 4.0275 | 0.0215 | 0.3709 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma65_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.7886 | 0.6789 | 3.8469 | 0.0207 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma65_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2516 | 0.6928 | 4.2712 | 0.0188 | 0.4217 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma65_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2325 | 0.6909 | 4.2287 | 0.0187 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma65_cross_down` | one_head_filter_pi_star | 22 | 1.8777 | 2.0233 | 0.6818 | 1.2381 | 0.0182 | 0.1364 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma65_cross_up` | one_head_filter_pi_star | 22 | 1.8824 | 1.3105 | 0.5909 | 0.5383 | 0.0127 | 0.2273 | TPM<MIN | RAN |
| SOLUSDT | 4 | `wma65_cross_down` | one_head_filter_pi_star | 12 | 1.0259 | 1.2617 | 0.5833 | 0.3507 | 0.0108 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma65_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2353 | 0.5975 | 1.0924 | 0.0074 | 0.2138 | ok | RAN |
| ETHUSDT | 8 | `wma65_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2303 | 0.6025 | 1.0493 | 0.0071 | 0.2050 | ok | RAN |
| SOLUSDT | 4 | `wma65_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3562 | 0.5963 | 1.9332 | 0.0053 | 0.2431 | ok | RAN |
| ETHUSDT | 8 | `wma65_cross_down` | one_head_filter_pi_star | 19 | 1.8933 | 1.1564 | 0.5263 | 0.3184 | 0.0050 | 0.2632 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma65_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3046 | 0.5924 | 1.6665 | 0.0045 | 0.2464 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma65_cross_down` | one_head_filter_pi_star | 13 | 1.3697 | 0.6060 | 0.4615 | -0.9468 | -0.0187 | 0.2308 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma65_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma65_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma65_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma65_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma65_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma65_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma65_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma65_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma65_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma65_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
