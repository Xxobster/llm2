# Autonomy public-indicator hunt gen 606

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T005509Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma285_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.1540 | 0.7097 | 4.8464 | 0.0255 | 0.3656 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma285_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.0946 | 0.7126 | 4.5582 | 0.0250 | 0.3966 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma285_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2078 | 0.6905 | 4.2243 | 0.0172 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma285_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1823 | 0.6928 | 4.0987 | 0.0171 | 0.3675 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma285_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2680 | 0.6041 | 1.3326 | 0.0090 | 0.2234 | ok | RAN |
| ETHUSDT | 8 | `wma285_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2200 | 0.6010 | 1.1479 | 0.0078 | 0.2280 | ok | RAN |
| SOLUSDT | 4 | `wma285_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3533 | 0.5951 | 1.8394 | 0.0055 | 0.2634 | ok | RAN |
| SOLUSDT | 8 | `wma285_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3342 | 0.5951 | 1.7547 | 0.0052 | 0.2683 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma285_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma285_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma285_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma285_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
