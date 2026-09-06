# Autonomy public-indicator hunt gen 394

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T005430Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret248_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.1651 | 0.6982 | 4.3829 | 0.0264 | 0.3787 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret248_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.0627 | 0.6893 | 4.3535 | 0.0241 | 0.3672 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret248_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.8992 | 0.6554 | 3.6108 | 0.0136 | 0.3616 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret248_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.8437 | 0.6514 | 3.4419 | 0.0126 | 0.3543 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret248_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.6487 | 0.6307 | 2.8073 | 0.0093 | 0.2784 | ok | RAN |
| SOLUSDT | 4 | `ret248_pos_at_h` | one_head_filter_pi_star | 176 | 14.4329 | 1.6144 | 0.6420 | 2.6651 | 0.0092 | 0.2727 | ok | RAN |
| ETHUSDT | 4 | `ret248_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1930 | 0.5989 | 0.9793 | 0.0067 | 0.2246 | ok | RAN |
| ETHUSDT | 8 | `ret248_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.1854 | 0.5914 | 0.9914 | 0.0066 | 0.2204 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret248_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0411 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret248_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret248_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret248_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
