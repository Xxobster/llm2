# Autonomy public-indicator hunt gen 286

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T042835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma75_cross_up` | one_head_filter_pi_star | 18 | 1.5541 | 7.4261 | 0.6667 | 2.7605 | 0.0426 | 0.2778 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma75_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.7911 | 0.6776 | 3.7852 | 0.0207 | 0.3738 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma75_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.7639 | 0.6761 | 3.7344 | 0.0205 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma75_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1847 | 0.6890 | 4.0896 | 0.0180 | 0.4085 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma75_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1518 | 0.6894 | 3.9900 | 0.0176 | 0.4161 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma75_cross_down` | one_head_filter_pi_star | 33 | 2.8165 | 1.7951 | 0.6667 | 1.3603 | 0.0169 | 0.1515 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `wma75_cross_down` | one_head_filter_pi_star | 13 | 1.1123 | 1.3351 | 0.6154 | 0.4932 | 0.0126 | 0.3077 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma75_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2594 | 0.6013 | 1.1735 | 0.0079 | 0.2152 | ok | RAN |
| ETHUSDT | 4 | `wma75_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2223 | 0.5975 | 1.0257 | 0.0069 | 0.2138 | ok | RAN |
| SOLUSDT | 8 | `wma75_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3206 | 0.5924 | 1.7445 | 0.0047 | 0.2464 | ok | RAN |
| SOLUSDT | 4 | `wma75_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3150 | 0.5962 | 1.7312 | 0.0046 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `wma75_cross_down` | one_head_filter_pi_star | 14 | 1.1949 | 1.1142 | 0.5714 | 0.1666 | 0.0044 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma75_cross_up` | one_head_filter_pi_star | 21 | 1.8278 | 1.1188 | 0.4762 | 0.2244 | 0.0044 | 0.2381 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma75_cross_down` | one_head_filter_pi_star | 18 | 1.5708 | 0.9889 | 0.5556 | -0.0217 | -0.0004 | 0.2222 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma75_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma75_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma75_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma75_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
