# Autonomy public-indicator hunt gen 272

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T032953Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma280_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0270 | 0.6978 | 4.4229 | 0.0243 | 0.3901 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma280_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.8545 | 0.6833 | 3.9320 | 0.0214 | 0.3889 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma280_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.2088 | 0.6957 | 4.1506 | 0.0173 | 0.3789 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma280_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1097 | 0.6824 | 4.0626 | 0.0161 | 0.3765 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma280_above_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2772 | 0.6010 | 1.4374 | 0.0091 | 0.2172 | ok | RAN |
| ETHUSDT | 4 | `sma280_above_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.2162 | 0.5938 | 1.1353 | 0.0074 | 0.2240 | ok | RAN |
| SOLUSDT | 4 | `sma280_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3544 | 0.5902 | 1.8508 | 0.0057 | 0.2634 | ok | RAN |
| SOLUSDT | 8 | `sma280_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.3480 | 0.6000 | 1.7544 | 0.0055 | 0.2595 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma280_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma280_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
