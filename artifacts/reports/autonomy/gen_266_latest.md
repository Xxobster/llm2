# Autonomy public-indicator hunt gen 266

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T030522Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret120_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9069 | 0.6895 | 4.0963 | 0.0223 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret120_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.8406 | 0.6831 | 3.8996 | 0.0214 | 0.3607 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret120_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.2692 | 0.6952 | 4.5147 | 0.0167 | 0.3690 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret120_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.0785 | 0.6667 | 4.1113 | 0.0152 | 0.3594 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret120_pos_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.4043 | 0.6265 | 1.8353 | 0.0126 | 0.2349 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret120_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.2869 | 0.6053 | 1.4027 | 0.0094 | 0.2211 | ok | RAN |
| SOLUSDT | 8 | `ret120_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.4020 | 0.6067 | 1.9537 | 0.0064 | 0.2640 | ok | RAN |
| SOLUSDT | 4 | `ret120_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3640 | 0.6010 | 1.8348 | 0.0060 | 0.2694 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret120_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret120_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret120_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret120_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
