# Autonomy public-indicator hunt gen 533

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T200824Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret81_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.7949 | 0.6667 | 3.7085 | 0.0201 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret81_neg_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.7430 | 0.6600 | 3.6737 | 0.0190 | 0.3650 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret81_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.2168 | 0.6780 | 4.2345 | 0.0169 | 0.3729 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret81_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.0373 | 0.6702 | 3.9278 | 0.0148 | 0.3617 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret81_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.3048 | 0.6170 | 1.5011 | 0.0101 | 0.2234 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret81_pos_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.2815 | 0.6087 | 1.3912 | 0.0091 | 0.2174 | ok | RAN |
| SOLUSDT | 4 | `ret81_pos_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4658 | 0.6091 | 2.3348 | 0.0073 | 0.2640 | ok | RAN |
| SOLUSDT | 8 | `ret81_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.3651 | 0.6011 | 1.8648 | 0.0057 | 0.2606 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret81_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret81_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0459 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret81_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret81_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret81_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret81_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret81_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret81_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret81_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret81_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret81_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret81_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret81_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret81_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret81_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret81_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
