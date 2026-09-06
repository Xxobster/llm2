# Autonomy public-indicator hunt gen 1446

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T212058Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma403_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0165 | 0.7000 | 4.5026 | 0.0238 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma403_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9382 | 0.6915 | 4.2565 | 0.0227 | 0.3883 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma403_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2249 | 0.6928 | 4.1652 | 0.0171 | 0.3916 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma403_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1590 | 0.6901 | 4.1675 | 0.0163 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `wma403_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.3089 | 0.6020 | 1.5551 | 0.0103 | 0.2296 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma403_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2881 | 0.6022 | 1.4621 | 0.0098 | 0.2204 | ok | RAN |
| SOLUSDT | 8 | `wma403_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4480 | 0.6105 | 2.1962 | 0.0068 | 0.2632 | ok | RAN |
| SOLUSDT | 4 | `wma403_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4081 | 0.6048 | 2.1065 | 0.0065 | 0.2667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma403_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma403_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma403_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma403_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma403_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma403_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma403_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma403_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma403_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma403_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma403_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma403_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma403_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma403_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma403_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma403_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
