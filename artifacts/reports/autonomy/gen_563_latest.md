# Autonomy public-indicator hunt gen 563

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T220549Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma310_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9402 | 0.6927 | 4.2804 | 0.0228 | 0.3698 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma310_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8781 | 0.6862 | 4.1254 | 0.0220 | 0.3830 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma310_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1578 | 0.6875 | 4.2184 | 0.0165 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma310_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.0421 | 0.6839 | 3.8532 | 0.0154 | 0.3678 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma310_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2051 | 0.5918 | 1.0913 | 0.0071 | 0.2245 | ok | RAN |
| SOLUSDT | 4 | `sma310_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4393 | 0.6053 | 2.1256 | 0.0070 | 0.2632 | ok | RAN |
| ETHUSDT | 4 | `sma310_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.1911 | 0.5936 | 1.0025 | 0.0068 | 0.2246 | ok | RAN |
| SOLUSDT | 8 | `sma310_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4020 | 0.6022 | 1.9354 | 0.0064 | 0.2527 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma310_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma310_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma310_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma310_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma310_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma310_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
