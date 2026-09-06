# Autonomy public-indicator hunt gen 1229

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T130421Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret219_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 2.0972 | 0.7035 | 4.4626 | 0.0261 | 0.4070 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret219_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 1.9755 | 0.6863 | 3.8486 | 0.0229 | 0.4052 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret219_neg_at_h` | one_head_filter_pi_star | 183 | 14.9792 | 2.1064 | 0.6885 | 4.1763 | 0.0153 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret219_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8090 | 0.6545 | 3.4855 | 0.0126 | 0.3665 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret219_pos_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 1.3017 | 0.6020 | 1.4839 | 0.0101 | 0.2289 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret219_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5147 | 0.6150 | 2.4120 | 0.0081 | 0.2674 | ok | RAN |
| SOLUSDT | 4 | `ret219_pos_at_h` | one_head_filter_pi_star | 167 | 13.6172 | 1.4832 | 0.6168 | 2.1474 | 0.0072 | 0.2754 | ok | RAN |
| ETHUSDT | 8 | `ret219_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1439 | 0.5864 | 0.7681 | 0.0051 | 0.2356 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret219_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret219_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret219_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret219_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret219_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret219_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret219_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret219_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret219_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret219_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret219_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret219_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret219_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret219_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret219_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret219_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
