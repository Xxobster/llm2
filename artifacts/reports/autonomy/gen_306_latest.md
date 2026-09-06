# Autonomy public-indicator hunt gen 306

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T055557Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret160_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.1502 | 0.7119 | 4.8190 | 0.0267 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret160_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.0535 | 0.7000 | 4.5412 | 0.0253 | 0.4056 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret160_neg_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.3169 | 0.6937 | 4.3575 | 0.0180 | 0.3875 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret160_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1580 | 0.6802 | 4.1321 | 0.0161 | 0.3663 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret160_pos_at_h` | one_head_filter_pi_star | 194 | 15.8867 | 1.2133 | 0.5979 | 1.1187 | 0.0071 | 0.2113 | ok | RAN |
| SOLUSDT | 4 | `ret160_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.4224 | 0.6044 | 2.0560 | 0.0066 | 0.2637 | ok | RAN |
| SOLUSDT | 8 | `ret160_pos_at_h` | one_head_filter_pi_star | 180 | 14.7609 | 1.3918 | 0.6000 | 1.8743 | 0.0063 | 0.2667 | ok | RAN |
| ETHUSDT | 8 | `ret160_pos_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.1602 | 0.5907 | 0.8711 | 0.0056 | 0.2228 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret160_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret160_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret160_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret160_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
