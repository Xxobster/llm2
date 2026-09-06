# Autonomy public-indicator hunt gen 346

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T144253Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret200_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.0795 | 0.6970 | 4.3956 | 0.0248 | 0.3939 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret200_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.9809 | 0.6919 | 4.1561 | 0.0235 | 0.4070 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret200_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.0274 | 0.6810 | 3.7534 | 0.0155 | 0.3865 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret200_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.0168 | 0.6748 | 3.6689 | 0.0152 | 0.3742 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret200_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.5999 | 0.6264 | 2.6229 | 0.0088 | 0.2759 | ok | RAN |
| ETHUSDT | 8 | `ret200_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2103 | 0.5956 | 1.0667 | 0.0074 | 0.2295 | ok | RAN |
| SOLUSDT | 4 | `ret200_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4721 | 0.6096 | 2.2207 | 0.0073 | 0.2781 | ok | RAN |
| ETHUSDT | 4 | `ret200_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1746 | 0.5885 | 0.9273 | 0.0062 | 0.2396 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret200_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6894 | 0.3158 | -0.6415 | -0.0323 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret200_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret200_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret200_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
