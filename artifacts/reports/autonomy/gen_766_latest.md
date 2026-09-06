# Autonomy public-indicator hunt gen 766

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T121711Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma385_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9916 | 0.6984 | 4.4750 | 0.0232 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma385_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.8808 | 0.6875 | 4.1431 | 0.0219 | 0.3906 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma385_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2086 | 0.6923 | 4.1493 | 0.0169 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma385_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1330 | 0.6946 | 3.9884 | 0.0160 | 0.3653 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma385_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2412 | 0.5944 | 1.2379 | 0.0083 | 0.2167 | ok | RAN |
| ETHUSDT | 4 | `wma385_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2305 | 0.6000 | 1.2123 | 0.0082 | 0.2263 | ok | RAN |
| SOLUSDT | 8 | `wma385_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4765 | 0.6091 | 2.3665 | 0.0072 | 0.2538 | ok | RAN |
| SOLUSDT | 4 | `wma385_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3725 | 0.5930 | 1.9105 | 0.0059 | 0.2613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma385_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma385_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma385_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma385_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
