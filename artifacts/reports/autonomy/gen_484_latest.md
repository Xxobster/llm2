# Autonomy public-indicator hunt gen 484

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T165215Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema365_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.1414 | 0.6990 | 4.7750 | 0.0253 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema365_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9671 | 0.6904 | 4.2913 | 0.0226 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema365_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.9210 | 0.6599 | 3.8584 | 0.0137 | 0.3604 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema365_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8435 | 0.6566 | 3.6279 | 0.0132 | 0.3687 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema365_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.2628 | 0.6136 | 1.3295 | 0.0091 | 0.2102 | ok | RAN |
| SOLUSDT | 8 | `ema365_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5051 | 0.6087 | 2.4184 | 0.0078 | 0.2663 | ok | RAN |
| SOLUSDT | 4 | `ema365_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4125 | 0.6043 | 2.0034 | 0.0066 | 0.2620 | ok | RAN |
| ETHUSDT | 8 | `ema365_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1528 | 0.5969 | 0.8131 | 0.0056 | 0.2251 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema365_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema365_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema365_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema365_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema365_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema365_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
