# Autonomy public-indicator hunt gen 205

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T225523Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret60_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.8139 | 0.6848 | 3.8373 | 0.0209 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret60_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.7125 | 0.6667 | 3.6081 | 0.0192 | 0.3682 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret60_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.2712 | 0.7039 | 4.4343 | 0.0184 | 0.4022 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret60_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2947 | 0.6988 | 4.3291 | 0.0180 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret60_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.3449 | 0.6158 | 1.6845 | 0.0107 | 0.2316 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret60_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2883 | 0.6053 | 1.4066 | 0.0089 | 0.2263 | ok | RAN |
| SOLUSDT | 4 | `ret60_pos_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3457 | 0.5962 | 1.8617 | 0.0053 | 0.2582 | ok | RAN |
| SOLUSDT | 8 | `ret60_pos_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3032 | 0.5909 | 1.6160 | 0.0046 | 0.2424 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret60_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret60_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret60_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret60_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret60_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret60_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret60_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret60_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret60_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret60_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret60_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret60_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret60_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret60_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret60_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret60_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
