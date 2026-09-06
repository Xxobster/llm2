# Autonomy public-indicator hunt gen 531

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T195957Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma286_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9891 | 0.6984 | 4.4390 | 0.0236 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma286_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9138 | 0.6898 | 4.2438 | 0.0224 | 0.3850 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma286_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.1962 | 0.6906 | 4.3862 | 0.0169 | 0.3867 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma286_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1667 | 0.6875 | 4.2313 | 0.0166 | 0.3693 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma286_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2811 | 0.6000 | 1.4544 | 0.0095 | 0.2205 | ok | RAN |
| ETHUSDT | 4 | `sma286_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2679 | 0.6041 | 1.3834 | 0.0090 | 0.2284 | ok | RAN |
| SOLUSDT | 4 | `sma286_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3896 | 0.6040 | 1.9820 | 0.0061 | 0.2624 | ok | RAN |
| SOLUSDT | 8 | `sma286_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3141 | 0.5922 | 1.6702 | 0.0050 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma286_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma286_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma286_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma286_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma286_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma286_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma286_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma286_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma286_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma286_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma286_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma286_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma286_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma286_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma286_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma286_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
