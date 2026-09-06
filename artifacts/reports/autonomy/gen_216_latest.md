# Autonomy public-indicator hunt gen 216

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T233929Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma120_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.0452 | 0.6884 | 4.5869 | 0.0238 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma120_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9621 | 0.6888 | 4.4463 | 0.0229 | 0.3724 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma120_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.3092 | 0.6994 | 4.5144 | 0.0181 | 0.3815 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma120_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2707 | 0.7024 | 4.3574 | 0.0180 | 0.3929 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma120_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2516 | 0.6054 | 1.2633 | 0.0084 | 0.2216 | ok | RAN |
| ETHUSDT | 8 | `sma120_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.1913 | 0.6032 | 0.9799 | 0.0066 | 0.2169 | ok | RAN |
| SOLUSDT | 4 | `sma120_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3166 | 0.6000 | 1.6794 | 0.0049 | 0.2585 | ok | RAN |
| SOLUSDT | 8 | `sma120_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3091 | 0.5902 | 1.6469 | 0.0048 | 0.2634 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma120_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma120_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
