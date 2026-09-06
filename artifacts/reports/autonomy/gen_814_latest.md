# Autonomy public-indicator hunt gen 814

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T165958Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma415_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9946 | 0.6979 | 4.4003 | 0.0235 | 0.3906 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma415_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9352 | 0.6931 | 4.2815 | 0.0224 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma415_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2272 | 0.6897 | 4.3232 | 0.0170 | 0.3908 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma415_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.1090 | 0.6854 | 4.1075 | 0.0161 | 0.3764 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma415_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2388 | 0.6000 | 1.2476 | 0.0083 | 0.2205 | ok | RAN |
| ETHUSDT | 4 | `wma415_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2253 | 0.5914 | 1.1636 | 0.0078 | 0.2258 | ok | RAN |
| SOLUSDT | 8 | `wma415_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4780 | 0.6138 | 2.2791 | 0.0071 | 0.2646 | ok | RAN |
| SOLUSDT | 4 | `wma415_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.3988 | 0.6022 | 1.9562 | 0.0063 | 0.2688 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma415_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma415_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma415_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma415_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
