# Autonomy public-indicator hunt gen 562

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T220158Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret416_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.2352 | 0.7018 | 4.4895 | 0.0265 | 0.3801 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret416_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.1933 | 0.7152 | 4.5343 | 0.0258 | 0.3879 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret416_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.7499 | 0.6649 | 3.2283 | 0.0116 | 0.3298 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret416_neg_at_h` | one_head_filter_pi_star | 151 | 12.3474 | 1.6741 | 0.6623 | 2.6702 | 0.0114 | 0.3907 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret416_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.5746 | 0.5971 | 2.7515 | 0.0087 | 0.2767 | ok | RAN |
| SOLUSDT | 8 | `ret416_pos_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.5010 | 0.5896 | 2.2671 | 0.0082 | 0.3121 | ok | RAN |
| ETHUSDT | 8 | `ret416_pos_at_h` | one_head_filter_pi_star | 199 | 16.3575 | 1.1905 | 0.5930 | 1.0258 | 0.0070 | 0.2412 | ok | RAN |
| ETHUSDT | 4 | `ret416_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1468 | 0.5885 | 0.8192 | 0.0058 | 0.2448 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret416_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0460 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret416_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0581 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret416_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret416_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
