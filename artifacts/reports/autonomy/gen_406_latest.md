# Autonomy public-indicator hunt gen 406

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T033709Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma160_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0063 | 0.6919 | 4.5825 | 0.0235 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma160_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.9036 | 0.6832 | 4.2639 | 0.0224 | 0.3663 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma160_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2877 | 0.6977 | 4.4485 | 0.0183 | 0.3895 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma160_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2274 | 0.6886 | 4.2230 | 0.0180 | 0.4072 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma160_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.3045 | 0.6133 | 1.4788 | 0.0096 | 0.2210 | ok | RAN |
| ETHUSDT | 4 | `wma160_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.1431 | 0.5904 | 0.7661 | 0.0050 | 0.2128 | ok | RAN |
| SOLUSDT | 8 | `wma160_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3103 | 0.5894 | 1.6356 | 0.0047 | 0.2657 | ok | RAN |
| SOLUSDT | 4 | `wma160_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.2607 | 0.5900 | 1.4109 | 0.0041 | 0.2600 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma160_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma160_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
