# Autonomy public-indicator hunt gen 1149

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T044630Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret207_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.2027 | 0.7048 | 4.6259 | 0.0266 | 0.4096 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret207_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.1700 | 0.7048 | 4.6151 | 0.0250 | 0.3916 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret207_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 2.0735 | 0.6769 | 4.2094 | 0.0153 | 0.3538 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret207_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.0330 | 0.6721 | 3.9666 | 0.0152 | 0.3716 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret207_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2160 | 0.5924 | 1.0709 | 0.0076 | 0.2283 | ok | RAN |
| SOLUSDT | 8 | `ret207_pos_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.4983 | 0.6149 | 2.1576 | 0.0075 | 0.2981 | ok | RAN |
| SOLUSDT | 4 | `ret207_pos_at_h` | one_head_filter_pi_star | 170 | 13.9408 | 1.4411 | 0.6059 | 2.0481 | 0.0070 | 0.2941 | ok | RAN |
| ETHUSDT | 8 | `ret207_pos_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 1.1362 | 0.5821 | 0.7316 | 0.0049 | 0.2338 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret207_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0411 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret207_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret207_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret207_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret207_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret207_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret207_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret207_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret207_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret207_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret207_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret207_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret207_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret207_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret207_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret207_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
