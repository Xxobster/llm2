# Autonomy public-indicator hunt gen 1357

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T013948Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret237_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.0545 | 0.7006 | 4.2770 | 0.0252 | 0.4072 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret237_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9937 | 0.7031 | 4.3467 | 0.0233 | 0.3646 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret237_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.9098 | 0.6629 | 3.6182 | 0.0136 | 0.3483 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret237_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8476 | 0.6500 | 3.6465 | 0.0132 | 0.3500 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret237_pos_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.2649 | 0.6036 | 1.2745 | 0.0094 | 0.2367 | ok | RAN |
| SOLUSDT | 4 | `ret237_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.5586 | 0.6180 | 2.4650 | 0.0082 | 0.2753 | ok | RAN |
| SOLUSDT | 8 | `ret237_pos_at_h` | one_head_filter_pi_star | 165 | 13.4542 | 1.4935 | 0.6182 | 2.1561 | 0.0077 | 0.2788 | ok | RAN |
| ETHUSDT | 4 | `ret237_pos_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.1697 | 0.5939 | 0.8962 | 0.0062 | 0.2386 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret237_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6197 | 0.3889 | -0.7841 | -0.0391 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret237_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret237_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret237_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret237_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret237_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret237_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret237_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret237_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret237_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret237_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret237_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret237_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret237_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret237_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret237_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
