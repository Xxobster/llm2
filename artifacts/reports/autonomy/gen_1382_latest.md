# Autonomy public-indicator hunt gen 1382

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T035803Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma770_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0964 | 0.7081 | 4.5505 | 0.0244 | 0.3676 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma770_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8477 | 0.6635 | 4.0146 | 0.0205 | 0.3654 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma770_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8571 | 0.6765 | 3.7016 | 0.0127 | 0.3382 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma770_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.7552 | 0.6614 | 3.2984 | 0.0118 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma770_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.6186 | 0.6257 | 2.6893 | 0.0095 | 0.2905 | ok | RAN |
| SOLUSDT | 8 | `wma770_above_at_h` | one_head_filter_pi_star | 170 | 13.8619 | 1.5065 | 0.6000 | 2.2806 | 0.0081 | 0.2941 | ok | RAN |
| ETHUSDT | 8 | `wma770_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.1725 | 0.5964 | 0.8523 | 0.0063 | 0.2169 | ok | RAN |
| ETHUSDT | 4 | `wma770_above_at_h` | one_head_filter_pi_star | 153 | 12.6258 | 1.1533 | 0.5882 | 0.7664 | 0.0056 | 0.2157 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma770_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma770_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma770_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma770_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma770_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma770_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
