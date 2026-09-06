# Autonomy public-indicator hunt gen 1037

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T150752Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret182_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.2448 | 0.7159 | 4.9181 | 0.0277 | 0.4034 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret182_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.0154 | 0.6923 | 4.1925 | 0.0241 | 0.3905 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret182_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1465 | 0.6818 | 4.1889 | 0.0163 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret182_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.0701 | 0.6728 | 3.8632 | 0.0157 | 0.3765 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret182_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.5566 | 0.6186 | 2.5822 | 0.0082 | 0.2629 | ok | RAN |
| ETHUSDT | 4 | `ret182_pos_at_h` | one_head_filter_pi_star | 199 | 16.4218 | 1.2180 | 0.5930 | 1.1938 | 0.0076 | 0.2261 | ok | RAN |
| SOLUSDT | 4 | `ret182_pos_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.4572 | 0.6103 | 2.2273 | 0.0072 | 0.2667 | ok | RAN |
| ETHUSDT | 8 | `ret182_pos_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.1156 | 0.5855 | 0.6487 | 0.0041 | 0.2124 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret182_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret182_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret182_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret182_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret182_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret182_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret182_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret182_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret182_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret182_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret182_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret182_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret182_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret182_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret182_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret182_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
