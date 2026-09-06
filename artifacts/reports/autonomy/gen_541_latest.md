# Autonomy public-indicator hunt gen 541

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T203953Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret83_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8404 | 0.6649 | 3.9885 | 0.0204 | 0.3660 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret83_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.7794 | 0.6649 | 3.7520 | 0.0195 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret83_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 2.0582 | 0.6701 | 4.1550 | 0.0152 | 0.3553 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret83_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0348 | 0.6667 | 3.9120 | 0.0150 | 0.3656 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret83_pos_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.3226 | 0.6180 | 1.5631 | 0.0104 | 0.2247 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret83_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2589 | 0.6158 | 1.3216 | 0.0086 | 0.2263 | ok | RAN |
| SOLUSDT | 8 | `ret83_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4231 | 0.6085 | 2.1144 | 0.0065 | 0.2698 | ok | RAN |
| SOLUSDT | 4 | `ret83_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.3202 | 0.5968 | 1.6552 | 0.0051 | 0.2634 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret83_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret83_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret83_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret83_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret83_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret83_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret83_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret83_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret83_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret83_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret83_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret83_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret83_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret83_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret83_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret83_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
