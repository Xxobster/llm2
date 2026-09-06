# Autonomy public-indicator hunt gen 846

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T200141Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma435_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9630 | 0.6979 | 4.3662 | 0.0228 | 0.3906 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma435_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9293 | 0.6853 | 4.2519 | 0.0228 | 0.3858 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma435_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2633 | 0.6932 | 4.4958 | 0.0173 | 0.3864 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma435_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1427 | 0.6944 | 4.2398 | 0.0162 | 0.3778 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma435_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2627 | 0.5957 | 1.3405 | 0.0089 | 0.2234 | ok | RAN |
| ETHUSDT | 8 | `wma435_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2423 | 0.5989 | 1.2610 | 0.0082 | 0.2246 | ok | RAN |
| SOLUSDT | 8 | `wma435_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.3917 | 0.5956 | 1.8918 | 0.0062 | 0.2678 | ok | RAN |
| SOLUSDT | 4 | `wma435_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3630 | 0.5960 | 1.8728 | 0.0057 | 0.2576 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma435_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma435_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma435_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma435_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
