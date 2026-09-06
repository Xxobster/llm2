# Autonomy public-indicator hunt gen 1141

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T034805Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret206_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 2.3650 | 0.7099 | 4.8083 | 0.0278 | 0.4074 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret206_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.1188 | 0.7033 | 4.6977 | 0.0260 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret206_neg_at_h` | one_head_filter_pi_star | 151 | 12.3474 | 1.9888 | 0.6821 | 3.5529 | 0.0146 | 0.3642 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret206_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.8579 | 0.6596 | 3.5570 | 0.0133 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret206_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2698 | 0.6031 | 1.3837 | 0.0094 | 0.2320 | ok | RAN |
| SOLUSDT | 8 | `ret206_pos_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.6359 | 0.6310 | 2.6971 | 0.0091 | 0.2917 | ok | RAN |
| SOLUSDT | 4 | `ret206_pos_at_h` | one_head_filter_pi_star | 168 | 13.7768 | 1.3791 | 0.6012 | 1.8016 | 0.0063 | 0.2857 | ok | RAN |
| ETHUSDT | 8 | `ret206_pos_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.0954 | 0.5816 | 0.5222 | 0.0036 | 0.2245 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret206_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret206_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5803 | 0.3158 | -0.8946 | -0.0447 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret206_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret206_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret206_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret206_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret206_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret206_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret206_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret206_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret206_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret206_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret206_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret206_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret206_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret206_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
