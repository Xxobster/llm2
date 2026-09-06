# Autonomy public-indicator hunt gen 482

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T164421Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret336_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.2671 | 0.7073 | 4.6754 | 0.0279 | 0.4085 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret336_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.3142 | 0.7229 | 4.5477 | 0.0277 | 0.3976 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret336_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8147 | 0.6649 | 3.4111 | 0.0123 | 0.3351 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret336_neg_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.6532 | 0.6569 | 3.0814 | 0.0106 | 0.3333 | ok | RAN |
| SOLUSDT | 8 | `ret336_pos_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.6983 | 0.6275 | 2.7048 | 0.0102 | 0.3072 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret336_pos_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.7029 | 0.6358 | 2.9259 | 0.0101 | 0.2775 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret336_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.1524 | 0.6011 | 0.7758 | 0.0057 | 0.2303 | ok | RAN |
| ETHUSDT | 8 | `ret336_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.0968 | 0.5897 | 0.5232 | 0.0037 | 0.2154 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret336_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0432 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret336_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5490 | 0.2632 | -1.0008 | -0.0502 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret336_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret336_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
