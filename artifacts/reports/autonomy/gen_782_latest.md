# Autonomy public-indicator hunt gen 782

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T135646Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma395_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0212 | 0.6940 | 4.4691 | 0.0239 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma395_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8680 | 0.6878 | 3.9981 | 0.0217 | 0.3862 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma395_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.1545 | 0.6923 | 4.2836 | 0.0163 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma395_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.0699 | 0.6813 | 4.0211 | 0.0155 | 0.3626 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma395_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2540 | 0.6044 | 1.2880 | 0.0087 | 0.2198 | ok | RAN |
| ETHUSDT | 4 | `wma395_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2289 | 0.5938 | 1.2091 | 0.0079 | 0.2188 | ok | RAN |
| SOLUSDT | 8 | `wma395_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4393 | 0.6129 | 2.1335 | 0.0067 | 0.2634 | ok | RAN |
| SOLUSDT | 4 | `wma395_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.4115 | 0.6039 | 2.1162 | 0.0066 | 0.2609 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma395_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma395_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma395_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma395_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
