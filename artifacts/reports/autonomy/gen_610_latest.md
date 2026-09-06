# Autonomy public-indicator hunt gen 610

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T011018Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret464_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 2.4772 | 0.7320 | 5.1881 | 0.0322 | 0.4379 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret464_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.1875 | 0.6982 | 4.5014 | 0.0265 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret464_pos_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.6490 | 0.6087 | 2.6792 | 0.0099 | 0.3106 | ok | RAN |
| SOLUSDT | 8 | `ret464_neg_at_h` | one_head_filter_pi_star | 211 | 17.1653 | 1.6158 | 0.6493 | 2.9808 | 0.0098 | 0.3270 | ok | RAN |
| SOLUSDT | 4 | `ret464_neg_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 1.5517 | 0.6359 | 2.6612 | 0.0090 | 0.3252 | ok | RAN |
| ETHUSDT | 4 | `ret464_pos_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.1680 | 0.5855 | 0.8104 | 0.0066 | 0.2303 | ok | RAN |
| ETHUSDT | 8 | `ret464_pos_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.1590 | 0.5817 | 0.7848 | 0.0064 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `ret464_pos_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.3707 | 0.5772 | 1.6179 | 0.0063 | 0.3020 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret464_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0430 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret464_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret464_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret464_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
