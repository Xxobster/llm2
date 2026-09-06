# Autonomy public-indicator hunt gen 226

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T001927Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret84_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8813 | 0.6701 | 4.1278 | 0.0218 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret84_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8172 | 0.6667 | 3.8591 | 0.0205 | 0.3692 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret84_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.1791 | 0.6796 | 4.2585 | 0.0166 | 0.3702 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret84_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.0841 | 0.6685 | 3.9896 | 0.0155 | 0.3702 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret84_pos_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.3102 | 0.6145 | 1.4909 | 0.0101 | 0.2402 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret84_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2305 | 0.6105 | 1.1953 | 0.0078 | 0.2211 | ok | RAN |
| SOLUSDT | 8 | `ret84_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4075 | 0.6022 | 2.0306 | 0.0063 | 0.2742 | ok | RAN |
| SOLUSDT | 4 | `ret84_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3425 | 0.6050 | 1.7807 | 0.0054 | 0.2600 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret84_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret84_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret84_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret84_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret84_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret84_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret84_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret84_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret84_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret84_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret84_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret84_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret84_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret84_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret84_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret84_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
