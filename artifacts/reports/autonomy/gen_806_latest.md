# Autonomy public-indicator hunt gen 806

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T161603Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma410_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8827 | 0.6891 | 4.0318 | 0.0217 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma410_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.8476 | 0.6848 | 3.9585 | 0.0209 | 0.3859 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma410_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2853 | 0.6989 | 4.4522 | 0.0180 | 0.3920 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma410_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.0871 | 0.6857 | 3.9746 | 0.0157 | 0.3600 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma410_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2434 | 0.6138 | 1.2735 | 0.0084 | 0.2063 | ok | RAN |
| ETHUSDT | 4 | `wma410_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1903 | 0.5885 | 1.0017 | 0.0068 | 0.2292 | ok | RAN |
| SOLUSDT | 4 | `wma410_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.3974 | 0.5979 | 1.9708 | 0.0064 | 0.2698 | ok | RAN |
| SOLUSDT | 8 | `wma410_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3056 | 0.5895 | 1.5852 | 0.0049 | 0.2579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma410_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma410_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma410_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma410_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma410_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma410_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma410_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma410_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma410_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma410_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma410_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma410_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma410_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma410_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma410_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma410_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
