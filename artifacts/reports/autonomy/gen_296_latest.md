# Autonomy public-indicator hunt gen 296

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T051208Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma340_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0319 | 0.6990 | 4.6481 | 0.0243 | 0.3827 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma340_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9561 | 0.6915 | 4.3493 | 0.0229 | 0.3830 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma340_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1571 | 0.6914 | 4.1665 | 0.0168 | 0.3829 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma340_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1092 | 0.6879 | 4.1236 | 0.0160 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma340_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2410 | 0.6043 | 1.2566 | 0.0082 | 0.2193 | ok | RAN |
| ETHUSDT | 4 | `sma340_above_at_h` | one_head_filter_pi_star | 199 | 16.3575 | 1.2256 | 0.5930 | 1.1881 | 0.0079 | 0.2312 | ok | RAN |
| SOLUSDT | 8 | `sma340_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.4480 | 0.5955 | 2.0809 | 0.0069 | 0.2640 | ok | RAN |
| SOLUSDT | 4 | `sma340_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4028 | 0.5979 | 1.9623 | 0.0064 | 0.2646 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma340_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma340_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
