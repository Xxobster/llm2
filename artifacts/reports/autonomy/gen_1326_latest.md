# Autonomy public-indicator hunt gen 1326

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T224553Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma735_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.1133 | 0.7022 | 4.5024 | 0.0248 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma735_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0135 | 0.6845 | 4.3481 | 0.0232 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma735_below_at_h` | one_head_filter_pi_star | 216 | 17.6625 | 1.9514 | 0.6759 | 4.1124 | 0.0138 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma735_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.8481 | 0.6736 | 3.6222 | 0.0127 | 0.3368 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma735_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.2897 | 0.6084 | 1.4026 | 0.0099 | 0.2229 | ok | RAN |
| SOLUSDT | 8 | `wma735_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.5764 | 0.6067 | 2.6347 | 0.0089 | 0.2809 | ok | RAN |
| SOLUSDT | 4 | `wma735_above_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.5111 | 0.6127 | 2.3009 | 0.0084 | 0.2948 | ok | RAN |
| ETHUSDT | 4 | `wma735_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.1867 | 0.5956 | 1.0157 | 0.0068 | 0.2131 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma735_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma735_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma735_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma735_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma735_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma735_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
