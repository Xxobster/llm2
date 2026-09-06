# Autonomy public-indicator hunt gen 718

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T082854Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma355_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0284 | 0.6989 | 4.5139 | 0.0240 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma355_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0059 | 0.6940 | 4.4718 | 0.0233 | 0.3770 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma355_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1847 | 0.6941 | 4.1926 | 0.0167 | 0.3824 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma355_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1712 | 0.6909 | 4.0237 | 0.0165 | 0.3758 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma355_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2572 | 0.5979 | 1.3552 | 0.0088 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `wma355_above_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.1924 | 0.5842 | 0.9953 | 0.0068 | 0.2211 | ok | RAN |
| SOLUSDT | 8 | `wma355_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4201 | 0.6041 | 2.1089 | 0.0064 | 0.2640 | ok | RAN |
| SOLUSDT | 4 | `wma355_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3285 | 0.5894 | 1.7251 | 0.0052 | 0.2657 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma355_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma355_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma355_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma355_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
