# Autonomy public-indicator hunt gen 614

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T012508Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma290_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.2087 | 0.7207 | 4.8631 | 0.0263 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma290_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9982 | 0.7000 | 4.4833 | 0.0237 | 0.3789 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma290_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1560 | 0.6886 | 4.0475 | 0.0168 | 0.3713 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma290_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1593 | 0.6842 | 4.1029 | 0.0167 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma290_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2408 | 0.6000 | 1.2089 | 0.0082 | 0.2256 | ok | RAN |
| ETHUSDT | 8 | `wma290_above_at_h` | one_head_filter_pi_star | 195 | 16.0917 | 1.1635 | 0.5846 | 0.8799 | 0.0057 | 0.2103 | ok | RAN |
| SOLUSDT | 4 | `wma290_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3593 | 0.5950 | 1.8486 | 0.0056 | 0.2600 | ok | RAN |
| SOLUSDT | 8 | `wma290_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3182 | 0.5845 | 1.6938 | 0.0050 | 0.2657 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma290_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma290_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma290_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma290_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma290_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma290_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma290_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma290_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma290_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma290_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma290_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma290_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma290_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma290_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma290_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma290_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
