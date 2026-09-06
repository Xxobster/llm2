# Autonomy public-indicator hunt gen 662

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T043202Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma320_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0604 | 0.7049 | 4.6182 | 0.0241 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma320_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0096 | 0.6973 | 4.4726 | 0.0239 | 0.3838 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma320_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1420 | 0.6852 | 3.9640 | 0.0165 | 0.3827 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma320_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1236 | 0.6867 | 3.9683 | 0.0163 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma320_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2394 | 0.5944 | 1.2442 | 0.0082 | 0.2167 | ok | RAN |
| ETHUSDT | 4 | `wma320_above_at_h` | one_head_filter_pi_star | 195 | 16.0917 | 1.1893 | 0.5897 | 0.9902 | 0.0067 | 0.2205 | ok | RAN |
| SOLUSDT | 4 | `wma320_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3968 | 0.6010 | 1.9910 | 0.0061 | 0.2677 | ok | RAN |
| SOLUSDT | 8 | `wma320_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.2875 | 0.5949 | 1.5249 | 0.0046 | 0.2615 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma320_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma320_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
