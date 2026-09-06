# Autonomy public-indicator hunt gen 1194

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T094323Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1048_neg_at_h` | one_head_filter_pi_star | 297 | 24.1615 | 1.8243 | 0.6633 | 4.4958 | 0.0195 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1048_neg_at_h` | one_head_filter_pi_star | 284 | 23.2002 | 1.7382 | 0.6514 | 4.0763 | 0.0182 | 0.3380 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1048_neg_at_h` | one_head_filter_pi_star | 283 | 23.1412 | 1.8115 | 0.6360 | 4.0847 | 0.0123 | 0.3251 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1048_neg_at_h` | one_head_filter_pi_star | 255 | 20.7448 | 1.7882 | 0.6353 | 3.7541 | 0.0120 | 0.3176 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1048_pos_at_h` | one_head_filter_pi_star | 69 | 5.6988 | 1.7028 | 0.6812 | 1.9275 | 0.0105 | 0.3043 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1048_pos_at_h` | one_head_filter_pi_star | 39 | 3.2420 | 1.4858 | 0.6667 | 1.1556 | 0.0079 | 0.2564 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1048_pos_at_h` | one_head_filter_pi_star | 66 | 5.8987 | 1.0487 | 0.5606 | 0.1790 | 0.0025 | 0.2121 | ok | RAN |
| ETHUSDT | 8 | `ret1048_pos_at_h` | one_head_filter_pi_star | 68 | 5.9136 | 1.0333 | 0.5735 | 0.1199 | 0.0017 | 0.2059 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1048_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4083 | 0.2667 | -1.2405 | -0.0515 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1048_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0565 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1048_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1048_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1048_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1048_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1048_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1048_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1048_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1048_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1048_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1048_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1048_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1048_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1048_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1048_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
