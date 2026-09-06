# Autonomy public-indicator hunt gen 222

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T000305Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma28_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma28_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0205 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma28_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2035 | 0.6909 | 4.1131 | 0.0182 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma28_cross_up` | one_head_filter_pi_star | 35 | 2.8800 | 1.4708 | 0.6286 | 0.9947 | 0.0181 | 0.2571 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma28_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma28_cross_down` | one_head_filter_pi_star | 23 | 1.9474 | 2.8563 | 0.7826 | 1.8829 | 0.0154 | 0.1304 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma28_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.2352 | 0.5935 | 1.0504 | 0.0075 | 0.2000 | ok | RAN |
| ETHUSDT | 4 | `wma28_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| ETHUSDT | 8 | `wma28_cross_down` | one_head_filter_pi_star | 19 | 1.9119 | 1.2295 | 0.5263 | 0.3666 | 0.0058 | 0.1579 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma28_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3773 | 0.5935 | 2.0385 | 0.0056 | 0.2430 | ok | RAN |
| SOLUSDT | 4 | `wma28_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3367 | 0.5915 | 1.8434 | 0.0050 | 0.2394 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma28_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma28_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma28_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma28_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
