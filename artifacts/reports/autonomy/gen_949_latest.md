# Autonomy public-indicator hunt gen 949

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T065517Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret185_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.1853 | 0.7076 | 4.7035 | 0.0268 | 0.3977 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret185_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 2.1559 | 0.6968 | 4.4278 | 0.0261 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret185_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1783 | 0.6810 | 4.0915 | 0.0168 | 0.3681 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret185_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 1.8600 | 0.6564 | 3.3707 | 0.0131 | 0.3742 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret185_pos_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.2628 | 0.6040 | 1.3417 | 0.0088 | 0.2327 | ok | RAN |
| SOLUSDT | 8 | `ret185_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4991 | 0.6134 | 2.3808 | 0.0076 | 0.2577 | ok | RAN |
| SOLUSDT | 4 | `ret185_pos_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.4161 | 0.6061 | 2.0502 | 0.0066 | 0.2727 | ok | RAN |
| ETHUSDT | 8 | `ret185_pos_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.0950 | 0.5751 | 0.5315 | 0.0033 | 0.2124 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret185_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret185_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret185_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret185_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret185_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret185_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret185_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret185_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret185_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret185_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret185_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret185_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret185_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret185_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret185_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret185_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
