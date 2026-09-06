# Autonomy public-indicator hunt gen 1146

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T042159Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1000_neg_at_h` | one_head_filter_pi_star | 265 | 21.6481 | 1.7377 | 0.6566 | 3.8587 | 0.0180 | 0.3321 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1000_neg_at_h` | one_head_filter_pi_star | 299 | 24.3242 | 1.6958 | 0.6488 | 3.9524 | 0.0175 | 0.3311 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1000_pos_at_h` | one_head_filter_pi_star | 44 | 3.6570 | 1.9257 | 0.7045 | 1.9648 | 0.0139 | 0.3182 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1000_pos_at_h` | one_head_filter_pi_star | 38 | 3.1588 | 2.0077 | 0.7368 | 1.9001 | 0.0129 | 0.2105 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1000_neg_at_h` | one_head_filter_pi_star | 282 | 22.9413 | 1.8347 | 0.6383 | 4.0130 | 0.0126 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1000_neg_at_h` | one_head_filter_pi_star | 282 | 22.9413 | 1.8438 | 0.6418 | 4.2337 | 0.0123 | 0.3191 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret1000_pos_at_h` | one_head_filter_pi_star | 67 | 5.7356 | 1.0442 | 0.5672 | 0.1591 | 0.0020 | 0.2388 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1000_pos_at_h` | one_head_filter_pi_star | 57 | 5.0126 | 0.8719 | 0.5439 | -0.4514 | -0.0072 | 0.1930 | ok | RAN |
| BTCUSDT | 8 | `ret1000_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4479 | 0.3125 | -1.1181 | -0.0454 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1000_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.1528 | 0.2308 | -2.0042 | -0.0689 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1000_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1000_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1000_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1000_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1000_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1000_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1000_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1000_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1000_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1000_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1000_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1000_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1000_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1000_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
