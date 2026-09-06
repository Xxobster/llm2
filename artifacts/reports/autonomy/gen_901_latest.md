# Autonomy public-indicator hunt gen 901

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T013257Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ret173_neg_at_h` | one_head_filter_pi_star | 10 | 1.9598 | 3.2951 | 0.7000 | 2.1790 | 0.1127 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret173_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.2363 | 0.7079 | 4.7946 | 0.0282 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret173_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.9650 | 0.6872 | 4.1574 | 0.0236 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret173_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.0814 | 0.6790 | 3.8879 | 0.0162 | 0.3827 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret173_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0415 | 0.6627 | 3.8077 | 0.0156 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret173_pos_at_h` | one_head_filter_pi_star | 201 | 16.4677 | 1.2150 | 0.6020 | 1.1513 | 0.0072 | 0.2139 | ok | RAN |
| SOLUSDT | 8 | `ret173_pos_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.4405 | 0.6040 | 2.1695 | 0.0068 | 0.2525 | ok | RAN |
| SOLUSDT | 4 | `ret173_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3936 | 0.6000 | 1.9877 | 0.0063 | 0.2650 | ok | RAN |
| ETHUSDT | 4 | `ret173_pos_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.1775 | 0.5938 | 0.9950 | 0.0061 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret173_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret173_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret173_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret173_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret173_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret173_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret173_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret173_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret173_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret173_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret173_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret173_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret173_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret173_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret173_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
