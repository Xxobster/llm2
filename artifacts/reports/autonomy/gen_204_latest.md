# Autonomy public-indicator hunt gen 204

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T225145Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema38_cross_up` | one_head_filter_pi_star | 17 | 1.4534 | 17.9336 | 0.8235 | 3.2656 | 0.0703 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema38_cross_down` | one_head_filter_pi_star | 25 | 2.1337 | 5.1518 | 0.8400 | 2.8271 | 0.0359 | 0.1600 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema38_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8131 | 0.6774 | 3.9917 | 0.0209 | 0.3733 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema38_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.7695 | 0.6773 | 3.7800 | 0.0202 | 0.3727 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema38_cross_down` | one_head_filter_pi_star | 19 | 2.2303 | 1.5163 | 0.5789 | 0.9639 | 0.0195 | 0.2105 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema38_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1275 | 0.6832 | 3.9148 | 0.0172 | 0.4099 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema38_below_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.0297 | 0.6730 | 3.6456 | 0.0159 | 0.4151 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema38_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2617 | 0.6051 | 1.1917 | 0.0081 | 0.2166 | ok | RAN |
| ETHUSDT | 4 | `ema38_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2382 | 0.6025 | 1.0873 | 0.0074 | 0.2112 | ok | RAN |
| SOLUSDT | 4 | `ema38_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3893 | 0.6055 | 2.0760 | 0.0057 | 0.2523 | ok | RAN |
| SOLUSDT | 8 | `ema38_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3604 | 0.6000 | 1.9466 | 0.0053 | 0.2465 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema38_cross_up` | one_head_filter_pi_star | 12 | 1.0598 | 0.8297 | 0.5000 | -0.2653 | -0.0088 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema38_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema38_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema38_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema38_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema38_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema38_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema38_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema38_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema38_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema38_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema38_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema38_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
