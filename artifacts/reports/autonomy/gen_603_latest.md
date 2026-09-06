# Autonomy public-indicator hunt gen 603

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T004400Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma346_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9805 | 0.6865 | 4.3469 | 0.0232 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma346_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8901 | 0.6856 | 4.1641 | 0.0217 | 0.3814 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma346_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.1305 | 0.6848 | 4.1940 | 0.0159 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma346_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.9937 | 0.6723 | 3.8020 | 0.0148 | 0.3729 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma346_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2423 | 0.5959 | 1.2845 | 0.0083 | 0.2176 | ok | RAN |
| SOLUSDT | 8 | `sma346_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4870 | 0.6054 | 2.2683 | 0.0075 | 0.2595 | ok | RAN |
| SOLUSDT | 4 | `sma346_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.3883 | 0.5968 | 1.8817 | 0.0061 | 0.2634 | ok | RAN |
| ETHUSDT | 8 | `sma346_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.1485 | 0.5897 | 0.8121 | 0.0053 | 0.2256 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma346_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma346_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma346_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma346_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma346_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma346_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma346_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma346_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma346_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma346_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma346_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma346_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma346_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma346_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma346_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma346_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
