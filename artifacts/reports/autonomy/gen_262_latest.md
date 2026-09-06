# Autonomy public-indicator hunt gen 262

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T024831Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma60_cross_up` | one_head_filter_pi_star | 11 | 1.0725 | 9.7254 | 0.7273 | 2.5012 | 0.0463 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma60_cross_down` | one_head_filter_pi_star | 19 | 1.6216 | 3.0561 | 0.7368 | 1.8049 | 0.0243 | 0.1579 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma60_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7736 | 0.6757 | 3.8107 | 0.0205 | 0.3694 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma60_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.7774 | 0.6743 | 3.7851 | 0.0203 | 0.3716 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma60_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2580 | 0.6970 | 4.2825 | 0.0188 | 0.4121 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma60_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1650 | 0.6875 | 4.0012 | 0.0178 | 0.4188 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma60_cross_up` | one_head_filter_pi_star | 20 | 1.7113 | 1.2213 | 0.5500 | 0.3841 | 0.0090 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma60_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2571 | 0.6076 | 1.1625 | 0.0078 | 0.2152 | ok | RAN |
| ETHUSDT | 8 | `wma60_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2172 | 0.5987 | 0.9895 | 0.0068 | 0.2102 | ok | RAN |
| SOLUSDT | 4 | `wma60_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3357 | 0.5953 | 1.8292 | 0.0050 | 0.2465 | ok | RAN |
| SOLUSDT | 8 | `wma60_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3200 | 0.5962 | 1.7482 | 0.0047 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma60_cross_down` | one_head_filter_pi_star | 18 | 2.1803 | 0.8897 | 0.5000 | -0.2737 | -0.0048 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma60_cross_down` | one_head_filter_pi_star | 16 | 1.3258 | 0.8512 | 0.5000 | -0.3082 | -0.0065 | 0.3125 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma60_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma60_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma60_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma60_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
