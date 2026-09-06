# Autonomy public-indicator hunt gen 304

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T054716Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma360_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9631 | 0.6931 | 4.2952 | 0.0231 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma360_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8611 | 0.6832 | 4.1512 | 0.0212 | 0.3762 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma360_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.1029 | 0.6872 | 4.0966 | 0.0155 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma360_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.0341 | 0.6791 | 4.0692 | 0.0151 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma360_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2725 | 0.5969 | 1.3942 | 0.0093 | 0.2245 | ok | RAN |
| SOLUSDT | 4 | `sma360_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.4761 | 0.6066 | 2.2583 | 0.0076 | 0.2678 | ok | RAN |
| ETHUSDT | 4 | `sma360_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1996 | 0.5947 | 1.0464 | 0.0073 | 0.2263 | ok | RAN |
| SOLUSDT | 8 | `sma360_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4585 | 0.6000 | 2.1969 | 0.0072 | 0.2649 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma360_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma360_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
