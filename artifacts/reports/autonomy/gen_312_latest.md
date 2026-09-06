# Autonomy public-indicator hunt gen 312

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T062111Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma380_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0445 | 0.7043 | 4.4999 | 0.0241 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma380_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9581 | 0.6957 | 4.2820 | 0.0229 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma380_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.0217 | 0.6771 | 4.0975 | 0.0144 | 0.3594 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma380_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.8826 | 0.6649 | 3.7098 | 0.0131 | 0.3608 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma380_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2738 | 0.6096 | 1.3803 | 0.0095 | 0.2299 | ok | RAN |
| ETHUSDT | 4 | `sma380_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2640 | 0.5902 | 1.3400 | 0.0092 | 0.2350 | ok | RAN |
| SOLUSDT | 4 | `sma380_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5244 | 0.6201 | 2.3711 | 0.0081 | 0.2682 | ok | RAN |
| SOLUSDT | 8 | `sma380_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.4600 | 0.5989 | 2.1601 | 0.0074 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma380_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma380_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
