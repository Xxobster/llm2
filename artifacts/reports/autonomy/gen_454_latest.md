# Autonomy public-indicator hunt gen 454

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T145705Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma190_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9750 | 0.6900 | 4.4324 | 0.0231 | 0.3700 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma190_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9781 | 0.6907 | 4.4695 | 0.0227 | 0.3608 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma190_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.3844 | 0.7079 | 4.7016 | 0.0190 | 0.3820 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma190_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2307 | 0.6982 | 4.2511 | 0.0177 | 0.3905 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma190_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2360 | 0.6056 | 1.1858 | 0.0080 | 0.2167 | ok | RAN |
| ETHUSDT | 4 | `wma190_above_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.1781 | 0.5969 | 0.9276 | 0.0063 | 0.2251 | ok | RAN |
| SOLUSDT | 4 | `wma190_above_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.3218 | 0.5913 | 1.6915 | 0.0050 | 0.2644 | ok | RAN |
| SOLUSDT | 8 | `wma190_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3217 | 0.5939 | 1.6942 | 0.0050 | 0.2640 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma190_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma190_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma190_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma190_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
