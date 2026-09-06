# Autonomy public-indicator hunt gen 1470

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T000030Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma407_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.9552 | 0.6966 | 4.1801 | 0.0228 | 0.3933 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma407_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8574 | 0.6862 | 3.9447 | 0.0211 | 0.3777 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma407_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.3041 | 0.6977 | 4.4202 | 0.0180 | 0.3895 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma407_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2313 | 0.6982 | 4.2377 | 0.0167 | 0.3669 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma407_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2839 | 0.6000 | 1.4084 | 0.0096 | 0.2410 | ok | RAN |
| ETHUSDT | 8 | `wma407_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1922 | 0.5928 | 1.0365 | 0.0067 | 0.2113 | ok | RAN |
| SOLUSDT | 4 | `wma407_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3804 | 0.6010 | 1.9399 | 0.0059 | 0.2626 | ok | RAN |
| SOLUSDT | 8 | `wma407_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3706 | 0.6000 | 1.9233 | 0.0059 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma407_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma407_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma407_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma407_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma407_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma407_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma407_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma407_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma407_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma407_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma407_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma407_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma407_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma407_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma407_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma407_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
