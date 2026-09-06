# Autonomy public-indicator hunt gen 310

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T061216Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma95_cross_up` | one_head_filter_pi_star | 18 | 1.5735 | 9.6031 | 0.7778 | 3.0473 | 0.0465 | 0.2778 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma95_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.9740 | 0.6942 | 4.4137 | 0.0237 | 0.3786 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma95_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.7679 | 0.6766 | 3.7488 | 0.0199 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma95_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2180 | 0.6946 | 4.1490 | 0.0183 | 0.4132 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma95_below_at_h` | one_head_filter_pi_star | 155 | 12.6745 | 2.1255 | 0.6839 | 3.8579 | 0.0171 | 0.4194 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma95_cross_down` | one_head_filter_pi_star | 29 | 2.4751 | 1.6878 | 0.6552 | 1.1469 | 0.0132 | 0.1724 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma95_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2724 | 0.6047 | 1.2583 | 0.0084 | 0.2267 | ok | RAN |
| ETHUSDT | 8 | `wma95_cross_down` | one_head_filter_pi_star | 29 | 2.4031 | 1.2081 | 0.5517 | 0.4401 | 0.0081 | 0.2414 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma95_above_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 1.2357 | 0.6047 | 1.1110 | 0.0073 | 0.2093 | ok | RAN |
| SOLUSDT | 8 | `wma95_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3675 | 0.6019 | 1.9372 | 0.0054 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `wma95_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3403 | 0.5962 | 1.8100 | 0.0050 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma95_cross_up` | one_head_filter_pi_star | 20 | 1.7407 | 1.0110 | 0.5000 | 0.0210 | 0.0004 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma95_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma95_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma95_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma95_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
