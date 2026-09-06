# Autonomy public-indicator hunt gen 1317

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T215709Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret231_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.1828 | 0.7134 | 4.5662 | 0.0262 | 0.3780 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret231_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.0512 | 0.6994 | 4.3631 | 0.0258 | 0.3931 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret231_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.9398 | 0.6557 | 3.7958 | 0.0139 | 0.3552 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret231_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8434 | 0.6545 | 3.5992 | 0.0131 | 0.3613 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret231_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.4894 | 0.6136 | 2.2241 | 0.0075 | 0.2784 | ok | RAN |
| SOLUSDT | 4 | `ret231_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.4643 | 0.6124 | 2.1455 | 0.0073 | 0.2697 | ok | RAN |
| ETHUSDT | 4 | `ret231_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1937 | 0.5825 | 0.9924 | 0.0068 | 0.2320 | ok | RAN |
| ETHUSDT | 8 | `ret231_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1227 | 0.5833 | 0.6485 | 0.0044 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret231_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret231_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret231_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret231_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret231_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret231_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret231_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret231_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret231_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret231_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret231_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret231_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret231_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret231_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret231_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret231_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
