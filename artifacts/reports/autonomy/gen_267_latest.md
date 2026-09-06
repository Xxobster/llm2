# Autonomy public-indicator hunt gen 267

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T030912Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma78_cross_up` | one_head_filter_pi_star | 12 | 1.2434 | 2.0390 | 0.6667 | 1.1886 | 0.0304 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma78_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8946 | 0.6923 | 4.1354 | 0.0222 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma78_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8192 | 0.6869 | 3.9233 | 0.0211 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma78_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.3220 | 0.6964 | 4.4497 | 0.0194 | 0.4048 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma78_cross_up` | one_head_filter_pi_star | 26 | 2.1664 | 1.9871 | 0.5769 | 1.2838 | 0.0186 | 0.1923 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma78_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1654 | 0.6894 | 3.9852 | 0.0176 | 0.4099 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma78_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.3613 | 0.6124 | 1.6441 | 0.0107 | 0.2247 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma78_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.3256 | 0.6089 | 1.5135 | 0.0099 | 0.2291 | ok | RAN |
| SOLUSDT | 8 | `sma78_cross_down` | one_head_filter_pi_star | 21 | 2.0321 | 1.4083 | 0.6190 | 0.7523 | 0.0092 | 0.2381 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma78_above_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.4295 | 0.6124 | 2.1682 | 0.0061 | 0.2536 | ok | RAN |
| SOLUSDT | 4 | `sma78_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3016 | 0.5915 | 1.6271 | 0.0046 | 0.2535 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma78_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma78_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma78_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma78_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma78_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma78_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma78_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma78_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma78_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma78_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma78_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma78_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma78_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
