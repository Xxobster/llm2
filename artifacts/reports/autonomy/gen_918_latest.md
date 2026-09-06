# Autonomy public-indicator hunt gen 918

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T032558Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma480_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0614 | 0.7031 | 4.6263 | 0.0248 | 0.3958 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma480_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9515 | 0.6923 | 4.3469 | 0.0225 | 0.3795 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma480_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.1874 | 0.6882 | 4.4198 | 0.0166 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma480_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0703 | 0.6774 | 4.1452 | 0.0151 | 0.3656 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma480_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2311 | 0.6022 | 1.1893 | 0.0079 | 0.2204 | ok | RAN |
| ETHUSDT | 4 | `wma480_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2242 | 0.5969 | 1.2039 | 0.0079 | 0.2194 | ok | RAN |
| SOLUSDT | 8 | `wma480_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.4974 | 0.6044 | 2.3059 | 0.0076 | 0.2692 | ok | RAN |
| SOLUSDT | 4 | `wma480_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.4413 | 0.6011 | 2.1248 | 0.0069 | 0.2678 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma480_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma480_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
