# Autonomy public-indicator hunt gen 467

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T154634Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma232_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0454 | 0.6983 | 4.4690 | 0.0245 | 0.3966 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma232_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.9781 | 0.6966 | 4.2227 | 0.0234 | 0.3933 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma232_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2244 | 0.6897 | 4.2802 | 0.0174 | 0.3793 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma232_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2256 | 0.6909 | 4.1982 | 0.0168 | 0.3818 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma232_above_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.2434 | 0.6000 | 1.2951 | 0.0085 | 0.2200 | ok | RAN |
| SOLUSDT | 4 | `sma232_above_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.3589 | 0.5981 | 1.8875 | 0.0057 | 0.2536 | ok | RAN |
| SOLUSDT | 8 | `sma232_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3620 | 0.5930 | 1.8731 | 0.0057 | 0.2563 | ok | RAN |
| ETHUSDT | 8 | `sma232_above_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.1146 | 0.5792 | 0.6386 | 0.0041 | 0.2178 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma232_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma232_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma232_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma232_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma232_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma232_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma232_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma232_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma232_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma232_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma232_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma232_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma232_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma232_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma232_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma232_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
