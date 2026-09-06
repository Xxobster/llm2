# Autonomy public-indicator hunt gen 982

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T105323Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma520_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9421 | 0.6935 | 4.2233 | 0.0226 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma520_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8425 | 0.6736 | 3.9598 | 0.0204 | 0.3731 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma520_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.1273 | 0.6862 | 4.2979 | 0.0156 | 0.3670 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma520_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.9449 | 0.6701 | 3.9228 | 0.0139 | 0.3604 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma520_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2401 | 0.6075 | 1.2492 | 0.0084 | 0.2258 | ok | RAN |
| ETHUSDT | 4 | `wma520_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2115 | 0.6010 | 1.1308 | 0.0076 | 0.2176 | ok | RAN |
| SOLUSDT | 8 | `wma520_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.4016 | 0.5980 | 2.0598 | 0.0065 | 0.2513 | ok | RAN |
| SOLUSDT | 4 | `wma520_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3251 | 0.5842 | 1.6502 | 0.0054 | 0.2579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma520_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma520_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
