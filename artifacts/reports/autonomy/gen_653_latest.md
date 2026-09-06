# Autonomy public-indicator hunt gen 653

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T035614Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret111_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.6458 | 0.6567 | 3.3681 | 0.0176 | 0.3582 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret111_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.6574 | 0.6564 | 3.2251 | 0.0171 | 0.3436 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret111_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.2476 | 0.6851 | 4.4274 | 0.0171 | 0.3702 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret111_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 2.1846 | 0.6800 | 4.5760 | 0.0161 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret111_pos_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.3999 | 0.6354 | 1.9217 | 0.0127 | 0.2486 | ok | RAN |
| ETHUSDT | 8 | `ret111_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.3461 | 0.6263 | 1.6527 | 0.0110 | 0.2368 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret111_pos_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.4256 | 0.6047 | 2.0018 | 0.0066 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ret111_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3544 | 0.5947 | 1.8147 | 0.0058 | 0.2579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret111_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret111_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret111_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret111_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret111_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret111_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret111_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret111_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret111_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret111_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret111_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret111_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret111_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret111_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret111_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret111_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
