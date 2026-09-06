# Autonomy public-indicator hunt gen 363

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T172317Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma142_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9103 | 0.6788 | 4.2866 | 0.0216 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma142_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8203 | 0.6720 | 3.9212 | 0.0203 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma142_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.2086 | 0.6882 | 4.3904 | 0.0171 | 0.3710 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma142_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2117 | 0.6910 | 4.3009 | 0.0171 | 0.3652 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma142_above_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.2804 | 0.6073 | 1.4181 | 0.0093 | 0.2304 | ok | RAN |
| ETHUSDT | 8 | `sma142_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2635 | 0.6054 | 1.3144 | 0.0090 | 0.2162 | ok | RAN |
| SOLUSDT | 4 | `sma142_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3204 | 0.5918 | 1.6690 | 0.0051 | 0.2602 | ok | RAN |
| SOLUSDT | 8 | `sma142_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.3016 | 0.5926 | 1.5807 | 0.0049 | 0.2698 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma142_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma142_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma142_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma142_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma142_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma142_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma142_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma142_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma142_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma142_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma142_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma142_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma142_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma142_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma142_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma142_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
