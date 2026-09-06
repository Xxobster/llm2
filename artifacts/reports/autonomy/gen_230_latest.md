# Autonomy public-indicator hunt gen 230

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T003627Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma32_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0208 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma32_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma32_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2063 | 0.6928 | 4.1185 | 0.0182 | 0.4217 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma32_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1917 | 0.6970 | 4.0640 | 0.0180 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma32_cross_down` | one_head_filter_pi_star | 23 | 1.9474 | 2.8220 | 0.7391 | 1.9250 | 0.0176 | 0.1304 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma32_cross_up` | one_head_filter_pi_star | 35 | 2.8800 | 1.2635 | 0.6000 | 0.6260 | 0.0111 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma32_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1899 | 0.5912 | 0.8814 | 0.0061 | 0.2075 | ok | RAN |
| SOLUSDT | 4 | `wma32_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3704 | 0.5972 | 2.0079 | 0.0054 | 0.2407 | ok | RAN |
| ETHUSDT | 4 | `wma32_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1628 | 0.5875 | 0.7744 | 0.0052 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `wma32_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3467 | 0.5877 | 1.8854 | 0.0052 | 0.2417 | ok | RAN |
| ETHUSDT | 8 | `wma32_cross_down` | one_head_filter_pi_star | 16 | 1.9290 | 1.0976 | 0.4375 | 0.1764 | 0.0030 | 0.1875 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma32_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma32_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `wma32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `wma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma32_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma32_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
