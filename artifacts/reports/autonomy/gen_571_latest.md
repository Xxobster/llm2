# Autonomy public-indicator hunt gen 571

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T223708Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma316_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9611 | 0.6902 | 4.2282 | 0.0233 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma316_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8908 | 0.6859 | 4.1150 | 0.0218 | 0.3822 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma316_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1436 | 0.6780 | 4.1542 | 0.0167 | 0.3729 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma316_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1348 | 0.6833 | 4.1365 | 0.0159 | 0.3667 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma316_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2002 | 0.5907 | 1.0724 | 0.0070 | 0.2176 | ok | RAN |
| ETHUSDT | 4 | `sma316_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.1991 | 0.5949 | 1.0705 | 0.0069 | 0.2205 | ok | RAN |
| SOLUSDT | 8 | `sma316_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.4458 | 0.6070 | 2.2070 | 0.0069 | 0.2587 | ok | RAN |
| SOLUSDT | 4 | `sma316_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3548 | 0.6010 | 1.8291 | 0.0057 | 0.2611 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma316_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma316_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma316_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma316_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma316_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma316_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma316_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma316_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma316_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma316_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma316_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma316_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma316_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma316_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma316_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma316_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
