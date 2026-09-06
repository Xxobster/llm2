# Autonomy public-indicator hunt gen 254

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T021427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma55_cross_up` | one_head_filter_pi_star | 13 | 1.2818 | 15.5502 | 0.7692 | 3.1273 | 0.0772 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma55_cross_down` | one_head_filter_pi_star | 15 | 1.2802 | 2.7835 | 0.7333 | 1.5731 | 0.0290 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma55_cross_down` | one_head_filter_pi_star | 20 | 1.9390 | 3.3237 | 0.7500 | 2.0852 | 0.0254 | 0.1000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma55_cross_down` | one_head_filter_pi_star | 21 | 1.8326 | 1.8802 | 0.6190 | 1.3134 | 0.0252 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma55_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.8727 | 0.6804 | 4.1662 | 0.0220 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma55_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.7804 | 0.6773 | 3.8361 | 0.0206 | 0.3727 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma55_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2138 | 0.6933 | 4.1549 | 0.0184 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma55_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2114 | 0.6909 | 4.1604 | 0.0183 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma55_cross_up` | one_head_filter_pi_star | 17 | 1.5014 | 1.5488 | 0.5882 | 0.7460 | 0.0141 | 0.2941 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma55_cross_down` | one_head_filter_pi_star | 12 | 1.0472 | 1.2698 | 0.5000 | 0.3416 | 0.0120 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma55_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2703 | 0.6038 | 1.2318 | 0.0081 | 0.2138 | ok | RAN |
| ETHUSDT | 8 | `wma55_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.2361 | 0.6000 | 1.0542 | 0.0073 | 0.2065 | ok | RAN |
| SOLUSDT | 4 | `wma55_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3456 | 0.6000 | 1.8743 | 0.0051 | 0.2465 | ok | RAN |
| SOLUSDT | 8 | `wma55_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3424 | 0.5962 | 1.8572 | 0.0050 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma55_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma55_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma55_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma55_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma55_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma55_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
