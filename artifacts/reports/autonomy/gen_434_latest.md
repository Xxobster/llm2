# Autonomy public-indicator hunt gen 434

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T102629Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret288_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.2762 | 0.7207 | 4.7266 | 0.0273 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret288_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.1425 | 0.7086 | 4.5947 | 0.0261 | 0.4114 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret288_neg_at_h` | one_head_filter_pi_star | 137 | 11.2026 | 2.0143 | 0.6861 | 3.4839 | 0.0154 | 0.3869 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret288_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.9016 | 0.6723 | 3.6386 | 0.0137 | 0.3446 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret288_pos_at_h` | one_head_filter_pi_star | 177 | 14.5149 | 1.6450 | 0.6271 | 2.7480 | 0.0097 | 0.2938 | ok | RAN |
| ETHUSDT | 4 | `ret288_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2259 | 0.6108 | 1.1343 | 0.0082 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `ret288_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4985 | 0.6022 | 2.2831 | 0.0076 | 0.2688 | ok | RAN |
| ETHUSDT | 8 | `ret288_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1852 | 0.5975 | 0.9354 | 0.0064 | 0.2013 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret288_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6154 | 0.3500 | -0.7982 | -0.0383 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret288_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5643 | 0.2778 | -0.9419 | -0.0472 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret288_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret288_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
