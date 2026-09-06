# Autonomy public-indicator hunt gen 168

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T202950Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma12_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9537 | 0.6927 | 3.9517 | 0.0240 | 0.3698 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma12_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7923 | 0.6787 | 3.8100 | 0.0204 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma12_below_at_h` | one_head_filter_pi_star | 155 | 12.6745 | 2.1882 | 0.6903 | 3.9428 | 0.0182 | 0.4129 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma12_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma12_above_at_h` | one_head_filter_pi_star | 127 | 10.4802 | 1.3296 | 0.5984 | 1.3023 | 0.0119 | 0.2362 | ok | RAN |
| SOLUSDT | 8 | `sma12_cross_up` | one_head_filter_pi_star | 34 | 2.8015 | 1.9820 | 0.7353 | 1.5047 | 0.0116 | 0.2647 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma12_above_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.4939 | 0.6190 | 2.2744 | 0.0083 | 0.2798 | ok | RAN |
| ETHUSDT | 8 | `sma12_cross_up` | one_head_filter_pi_star | 41 | 3.3738 | 1.2621 | 0.6341 | 0.6144 | 0.0066 | 0.2195 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma12_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2035 | 0.5901 | 0.9496 | 0.0066 | 0.1988 | ok | RAN |
| SOLUSDT | 4 | `sma12_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3778 | 0.5953 | 2.0412 | 0.0055 | 0.2419 | ok | RAN |
| SOLUSDT | 8 | `sma12_cross_down` | one_head_filter_pi_star | 93 | 7.6269 | 1.4387 | 0.6452 | 1.5475 | 0.0055 | 0.1398 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma12_cross_down` | one_head_filter_pi_star | 49 | 4.2530 | 0.9681 | 0.5510 | -0.0917 | -0.0009 | 0.0816 | ok | RAN |
| BTCUSDT | 8 | `sma12_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6733 | 0.3333 | -0.5810 | -0.0332 | 0.0667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma12_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `sma12_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma12_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma12_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma12_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma12_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma12_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
