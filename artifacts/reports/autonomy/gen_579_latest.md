# Autonomy public-indicator hunt gen 579

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T230853Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma322_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9683 | 0.6947 | 4.4136 | 0.0231 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma322_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.8729 | 0.6831 | 4.0557 | 0.0217 | 0.3880 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma322_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2191 | 0.6879 | 4.3485 | 0.0171 | 0.3931 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma322_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1744 | 0.6857 | 4.3178 | 0.0164 | 0.3714 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma322_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2388 | 0.5990 | 1.2548 | 0.0081 | 0.2135 | ok | RAN |
| ETHUSDT | 4 | `sma322_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2282 | 0.5946 | 1.1995 | 0.0079 | 0.2216 | ok | RAN |
| SOLUSDT | 4 | `sma322_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4997 | 0.6062 | 2.3630 | 0.0075 | 0.2642 | ok | RAN |
| SOLUSDT | 8 | `sma322_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.4783 | 0.6066 | 2.2359 | 0.0073 | 0.2678 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma322_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma322_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma322_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma322_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma322_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma322_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma322_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma322_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma322_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma322_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma322_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma322_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma322_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma322_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma322_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma322_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
