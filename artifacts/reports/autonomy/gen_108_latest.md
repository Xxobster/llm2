# Autonomy public-indicator hunt gen 108

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T163602Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma30_cross_up` | one_head_filter_pi_star | 12 | 1.0259 | 23.4803 | 0.8333 | 2.7755 | 0.0576 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma30_cross_up` | one_head_filter_pi_star | 23 | 1.8989 | 2.0237 | 0.6522 | 1.4269 | 0.0321 | 0.2174 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma30_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma30_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma30_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1940 | 0.6951 | 4.0873 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma30_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1718 | 0.6933 | 4.0197 | 0.0177 | 0.4172 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma30_cross_down` | one_head_filter_pi_star | 20 | 2.4112 | 1.3066 | 0.5500 | 0.5852 | 0.0117 | 0.1500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma30_cross_down` | one_head_filter_pi_star | 18 | 1.7361 | 1.7447 | 0.6111 | 0.9595 | 0.0095 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma30_above_at_h` | one_head_filter_pi_star | 156 | 12.8733 | 1.2362 | 0.5962 | 1.0815 | 0.0073 | 0.2051 | ok | RAN |
| ETHUSDT | 4 | `sma30_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2071 | 0.5938 | 0.9657 | 0.0065 | 0.2000 | ok | RAN |
| SOLUSDT | 4 | `sma30_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3683 | 0.5972 | 1.9893 | 0.0054 | 0.2454 | ok | RAN |
| SOLUSDT | 8 | `sma30_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3596 | 0.5972 | 1.9531 | 0.0053 | 0.2407 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma30_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma30_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma30_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma30_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma30_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma30_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma30_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma30_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma30_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
