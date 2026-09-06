# Autonomy public-indicator hunt gen 1029

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T141012Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret180_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 2.1408 | 0.6941 | 4.6802 | 0.0254 | 0.3941 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret180_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.0241 | 0.6971 | 4.4178 | 0.0243 | 0.3886 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret180_neg_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.0811 | 0.6730 | 3.8371 | 0.0159 | 0.3774 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret180_neg_at_h` | one_head_filter_pi_star | 157 | 12.8380 | 2.0483 | 0.6688 | 3.8452 | 0.0155 | 0.3694 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret180_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2757 | 0.6010 | 1.4600 | 0.0091 | 0.2374 | ok | RAN |
| SOLUSDT | 8 | `ret180_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.5769 | 0.6262 | 2.7463 | 0.0084 | 0.2573 | ok | RAN |
| ETHUSDT | 8 | `ret180_pos_at_h` | one_head_filter_pi_star | 195 | 16.0917 | 1.1785 | 0.5846 | 0.9441 | 0.0063 | 0.2103 | ok | RAN |
| SOLUSDT | 4 | `ret180_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.3825 | 0.5936 | 1.8746 | 0.0061 | 0.2781 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret180_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret180_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret180_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret180_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret180_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret180_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret180_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret180_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret180_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret180_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret180_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret180_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret180_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret180_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret180_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret180_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
