# Autonomy public-indicator hunt gen 1262

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T163108Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma695_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0443 | 0.6963 | 4.4928 | 0.0238 | 0.3665 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma695_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9921 | 0.6952 | 4.3070 | 0.0229 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma695_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8182 | 0.6718 | 3.4860 | 0.0126 | 0.3436 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma695_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.7322 | 0.6552 | 3.2705 | 0.0117 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma695_above_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.6379 | 0.6229 | 2.7508 | 0.0098 | 0.2857 | ok | RAN |
| SOLUSDT | 8 | `wma695_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.4561 | 0.6000 | 2.1169 | 0.0074 | 0.2833 | ok | RAN |
| ETHUSDT | 4 | `wma695_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.1720 | 0.5944 | 0.9510 | 0.0062 | 0.2167 | ok | RAN |
| ETHUSDT | 8 | `wma695_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.1587 | 0.5989 | 0.8468 | 0.0059 | 0.2147 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma695_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma695_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma695_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma695_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
