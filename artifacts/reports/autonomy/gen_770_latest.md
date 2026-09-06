# Autonomy public-indicator hunt gen 770

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T124313Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret624_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1495 | 0.7021 | 4.6455 | 0.0252 | 0.3670 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret624_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.1063 | 0.7062 | 4.4327 | 0.0241 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret624_neg_at_h` | one_head_filter_pi_star | 220 | 18.1087 | 1.8051 | 0.6500 | 3.6978 | 0.0133 | 0.3227 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret624_neg_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 1.7240 | 0.6422 | 3.3871 | 0.0121 | 0.3257 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret624_pos_at_h` | one_head_filter_pi_star | 121 | 9.8669 | 1.6947 | 0.6446 | 2.4219 | 0.0091 | 0.2562 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret624_pos_at_h` | one_head_filter_pi_star | 96 | 7.9793 | 1.5214 | 0.6458 | 1.7565 | 0.0070 | 0.2292 | ok | RAN |
| ETHUSDT | 8 | `ret624_pos_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.0873 | 0.5605 | 0.4405 | 0.0034 | 0.2357 | ok | RAN |
| ETHUSDT | 4 | `ret624_pos_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.0816 | 0.5641 | 0.4060 | 0.0033 | 0.2051 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret624_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0650 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret624_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3625 | 0.2667 | -1.3559 | -0.0816 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret624_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret624_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret624_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret624_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret624_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret624_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret624_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret624_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret624_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret624_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret624_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret624_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret624_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret624_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
