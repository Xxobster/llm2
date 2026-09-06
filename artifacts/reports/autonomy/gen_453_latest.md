# Autonomy public-indicator hunt gen 453

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T145318Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret61_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.7660 | 0.6793 | 3.6233 | 0.0199 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret61_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.7369 | 0.6701 | 3.7158 | 0.0194 | 0.3711 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret61_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.3363 | 0.7024 | 4.4562 | 0.0185 | 0.4048 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret61_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2413 | 0.6933 | 4.2436 | 0.0178 | 0.3926 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret61_pos_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.3377 | 0.6111 | 1.6103 | 0.0104 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `ret61_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.3335 | 0.6085 | 1.6441 | 0.0103 | 0.2328 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret61_pos_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3254 | 0.5902 | 1.7432 | 0.0050 | 0.2537 | ok | RAN |
| SOLUSDT | 8 | `ret61_pos_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2893 | 0.5902 | 1.5637 | 0.0043 | 0.2537 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret61_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret61_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret61_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret61_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret61_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret61_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret61_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret61_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret61_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret61_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret61_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret61_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret61_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret61_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret61_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret61_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
