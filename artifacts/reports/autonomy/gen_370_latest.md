# Autonomy public-indicator hunt gen 370

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T191440Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret224_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1326 | 0.7111 | 4.6335 | 0.0260 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret224_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.1170 | 0.6989 | 4.4932 | 0.0247 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret224_neg_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 2.1199 | 0.6701 | 4.3930 | 0.0157 | 0.3608 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret224_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9292 | 0.6579 | 3.8176 | 0.0138 | 0.3737 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret224_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5104 | 0.6162 | 2.3572 | 0.0079 | 0.2649 | ok | RAN |
| SOLUSDT | 4 | `ret224_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.4255 | 0.6114 | 1.9728 | 0.0067 | 0.2800 | ok | RAN |
| ETHUSDT | 4 | `ret224_pos_at_h` | one_head_filter_pi_star | 199 | 16.3575 | 1.1408 | 0.5829 | 0.7553 | 0.0051 | 0.2312 | ok | RAN |
| ETHUSDT | 8 | `ret224_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.0995 | 0.5722 | 0.5425 | 0.0037 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret224_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5803 | 0.3158 | -0.8946 | -0.0430 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret224_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret224_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret224_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret224_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret224_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret224_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret224_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret224_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret224_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret224_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret224_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret224_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret224_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret224_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret224_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
