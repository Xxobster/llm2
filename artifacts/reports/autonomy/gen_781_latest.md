# Autonomy public-indicator hunt gen 781

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T135109Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret143_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.9032 | 0.6831 | 4.1358 | 0.0229 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret143_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8332 | 0.6786 | 4.0246 | 0.0206 | 0.3776 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret143_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.1165 | 0.6755 | 4.2154 | 0.0160 | 0.3617 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret143_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.0831 | 0.6757 | 4.0793 | 0.0153 | 0.3622 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret143_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2682 | 0.6167 | 1.3116 | 0.0089 | 0.2111 | ok | RAN |
| SOLUSDT | 8 | `ret143_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3741 | 0.5928 | 1.8886 | 0.0061 | 0.2629 | ok | RAN |
| SOLUSDT | 4 | `ret143_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.3462 | 0.5926 | 1.7108 | 0.0056 | 0.2646 | ok | RAN |
| ETHUSDT | 4 | `ret143_pos_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.1575 | 0.5852 | 0.8264 | 0.0055 | 0.2102 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret143_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret143_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret143_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret143_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret143_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret143_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret143_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret143_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret143_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret143_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret143_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret143_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret143_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret143_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret143_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret143_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
