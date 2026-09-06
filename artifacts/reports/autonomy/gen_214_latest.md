# Autonomy public-indicator hunt gen 214

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T233046Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma22_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma22_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.8028 | 0.6786 | 3.8805 | 0.0204 | 0.3705 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma22_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma22_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1867 | 0.6928 | 4.0603 | 0.0179 | 0.4157 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma22_cross_down` | one_head_filter_pi_star | 32 | 2.7095 | 2.6204 | 0.7500 | 2.0679 | 0.0126 | 0.1562 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma22_cross_up` | one_head_filter_pi_star | 42 | 3.4560 | 1.2418 | 0.5476 | 0.6059 | 0.0082 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma22_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2179 | 0.5963 | 1.0035 | 0.0070 | 0.2050 | ok | RAN |
| ETHUSDT | 4 | `wma22_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 8 | `wma22_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3928 | 0.5953 | 2.1177 | 0.0059 | 0.2512 | ok | RAN |
| SOLUSDT | 4 | `wma22_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3931 | 0.5972 | 2.1197 | 0.0058 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma22_cross_down` | one_head_filter_pi_star | 25 | 2.3294 | 0.5231 | 0.4400 | -1.2430 | -0.0124 | 0.0800 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma22_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6235 | 0.3333 | -0.7532 | -0.0366 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma22_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma22_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma22_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
