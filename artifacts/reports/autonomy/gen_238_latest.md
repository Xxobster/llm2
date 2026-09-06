# Autonomy public-indicator hunt gen 238

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T010846Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma36_cross_up` | one_head_filter_pi_star | 21 | 1.7337 | 1.8893 | 0.7143 | 1.2372 | 0.0289 | 0.2381 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma36_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8007 | 0.6787 | 3.8626 | 0.0207 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma36_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8007 | 0.6787 | 3.8626 | 0.0207 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma36_cross_down` | one_head_filter_pi_star | 23 | 2.0226 | 2.7480 | 0.6957 | 1.9107 | 0.0203 | 0.1304 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma36_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2257 | 0.6988 | 4.1692 | 0.0184 | 0.4217 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma36_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1767 | 0.6909 | 4.0482 | 0.0178 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma36_cross_down` | one_head_filter_pi_star | 19 | 2.1888 | 1.3150 | 0.5263 | 0.6335 | 0.0104 | 0.2632 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma36_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2071 | 0.5938 | 0.9657 | 0.0065 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `wma36_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1899 | 0.5912 | 0.8814 | 0.0061 | 0.2075 | ok | RAN |
| SOLUSDT | 8 | `wma36_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3488 | 0.5915 | 1.8967 | 0.0052 | 0.2394 | ok | RAN |
| SOLUSDT | 4 | `wma36_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3367 | 0.5915 | 1.8434 | 0.0050 | 0.2394 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma36_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma36_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `wma36_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma36_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma36_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma36_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma36_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma36_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma36_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
