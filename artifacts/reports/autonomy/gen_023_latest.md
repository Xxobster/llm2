# Autonomy public-indicator hunt gen 023

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T100016Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ppo_cross_down_0` | one_head_filter_pi_star | 25 | 2.0546 | 5.8600 | 0.6800 | 2.6638 | 0.0480 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 4 | `ppo_cross_down_0` | one_head_filter_pi_star | 19 | 1.5763 | 4.4096 | 0.6316 | 2.1837 | 0.0396 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `ppo_cross_up_0` | one_head_filter_pi_star | 19 | 1.7672 | 1.9921 | 0.6316 | 1.2594 | 0.0225 | 0.2105 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ppo_neg_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.7859 | 0.6773 | 3.8547 | 0.0210 | 0.3727 | EBR>35% | RAN |
| ETHUSDT | 8 | `ppo_neg_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.7426 | 0.6713 | 3.6523 | 0.0197 | 0.3704 | EBR>35% | RAN |
| SOLUSDT | 8 | `ppo_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2373 | 0.6970 | 4.2126 | 0.0186 | 0.4242 | EBR>35% | RAN |
| SOLUSDT | 4 | `ppo_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2019 | 0.6909 | 4.1020 | 0.0180 | 0.4121 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ppo_cross_up_0` | one_head_filter_pi_star | 39 | 3.4297 | 1.7203 | 0.6154 | 1.4103 | 0.0139 | 0.1282 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ppo_cross_down_0` | one_head_filter_pi_star | 35 | 2.8923 | 1.3456 | 0.6000 | 0.7727 | 0.0113 | 0.3143 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ppo_cross_up_0` | one_head_filter_pi_star | 21 | 1.9533 | 1.3234 | 0.5714 | 0.5476 | 0.0096 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ppo_cross_down_0` | one_head_filter_pi_star | 42 | 3.4708 | 1.2626 | 0.5714 | 0.6673 | 0.0095 | 0.2857 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ppo_cross_up_0` | one_head_filter_pi_star | 34 | 3.2900 | 1.3698 | 0.5882 | 0.8054 | 0.0078 | 0.1471 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ppo_pos_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2337 | 0.6038 | 1.0556 | 0.0072 | 0.2075 | ok | RAN |
| ETHUSDT | 4 | `ppo_pos_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 1.2347 | 0.6000 | 1.1115 | 0.0071 | 0.2061 | ok | RAN |
| SOLUSDT | 4 | `ppo_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3391 | 0.5953 | 1.8489 | 0.0050 | 0.2419 | ok | RAN |
| SOLUSDT | 8 | `ppo_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3268 | 0.5924 | 1.7749 | 0.0048 | 0.2464 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ppo_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ppo_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ppo_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ppo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ppo_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ppo_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ppo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ppo_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
