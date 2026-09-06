# Autonomy public-indicator hunt gen 378

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T211717Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret232_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 2.3543 | 0.7205 | 4.7919 | 0.0294 | 0.3975 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret232_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.1249 | 0.7022 | 4.5782 | 0.0256 | 0.3820 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret232_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.0751 | 0.6719 | 4.3112 | 0.0152 | 0.3594 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret232_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.7505 | 0.6425 | 3.3359 | 0.0116 | 0.3472 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret232_pos_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2620 | 0.6122 | 1.3366 | 0.0092 | 0.2347 | ok | RAN |
| SOLUSDT | 4 | `ret232_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.5070 | 0.6250 | 2.4032 | 0.0079 | 0.2708 | ok | RAN |
| SOLUSDT | 8 | `ret232_pos_at_h` | one_head_filter_pi_star | 167 | 13.6172 | 1.5049 | 0.6108 | 2.2279 | 0.0079 | 0.2934 | ok | RAN |
| ETHUSDT | 8 | `ret232_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1844 | 0.5833 | 0.9973 | 0.0066 | 0.2344 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret232_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret232_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret232_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret232_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
