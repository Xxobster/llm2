# Autonomy public-indicator hunt gen 1214

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T114141Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma665_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.0978 | 0.6935 | 4.6297 | 0.0241 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma665_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0663 | 0.7037 | 4.5175 | 0.0237 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma665_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.9396 | 0.6716 | 3.9182 | 0.0135 | 0.3483 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma665_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.8549 | 0.6632 | 3.6279 | 0.0131 | 0.3523 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma665_above_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.6241 | 0.6243 | 2.7192 | 0.0096 | 0.2890 | ok | RAN |
| SOLUSDT | 8 | `wma665_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.5636 | 0.6126 | 2.6546 | 0.0089 | 0.2723 | ok | RAN |
| ETHUSDT | 8 | `wma665_above_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.2057 | 0.6000 | 1.0258 | 0.0077 | 0.2286 | ok | RAN |
| ETHUSDT | 4 | `wma665_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.1824 | 0.5866 | 0.9466 | 0.0066 | 0.2067 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma665_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma665_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma665_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma665_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
