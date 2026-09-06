# Autonomy public-indicator hunt gen 709

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T074916Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret125_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9544 | 0.6856 | 4.2269 | 0.0228 | 0.3557 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret125_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.8217 | 0.6739 | 3.7787 | 0.0206 | 0.3804 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret125_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.2173 | 0.6831 | 4.4125 | 0.0165 | 0.3770 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret125_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.0895 | 0.6705 | 4.0100 | 0.0158 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret125_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.4414 | 0.6389 | 2.0875 | 0.0144 | 0.2278 | ok | RAN |
| ETHUSDT | 4 | `ret125_pos_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.3324 | 0.6185 | 1.5574 | 0.0111 | 0.2197 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret125_pos_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.3879 | 0.6022 | 1.9081 | 0.0063 | 0.2541 | ok | RAN |
| SOLUSDT | 4 | `ret125_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.3443 | 0.5978 | 1.7375 | 0.0056 | 0.2609 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret125_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret125_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret125_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret125_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret125_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret125_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret125_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret125_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret125_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret125_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret125_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret125_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret125_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret125_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret125_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret125_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
