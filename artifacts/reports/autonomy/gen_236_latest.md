# Autonomy public-indicator hunt gen 236

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T010104Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema68_cross_up` | one_head_filter_pi_star | 14 | 1.2333 | 11.8387 | 0.8571 | 2.8890 | 0.0559 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema68_cross_down` | one_head_filter_pi_star | 28 | 2.3202 | 1.9376 | 0.6429 | 1.5441 | 0.0284 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema68_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.9176 | 0.6878 | 4.2876 | 0.0224 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema68_cross_down` | one_head_filter_pi_star | 23 | 2.2256 | 3.5469 | 0.7391 | 2.4450 | 0.0224 | 0.0870 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema68_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.7605 | 0.6733 | 3.8221 | 0.0195 | 0.3564 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema68_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2867 | 0.6964 | 4.3624 | 0.0188 | 0.4048 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema68_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1368 | 0.6875 | 3.8990 | 0.0173 | 0.4125 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema68_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.3526 | 0.6163 | 1.5801 | 0.0107 | 0.2209 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema68_above_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.3040 | 0.6048 | 1.3707 | 0.0094 | 0.2156 | ok | RAN |
| SOLUSDT | 8 | `ema68_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3809 | 0.6009 | 1.9865 | 0.0056 | 0.2582 | ok | RAN |
| SOLUSDT | 4 | `ema68_above_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.3118 | 0.5913 | 1.6553 | 0.0046 | 0.2548 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema68_cross_up` | one_head_filter_pi_star | 27 | 2.3430 | 1.0105 | 0.5185 | 0.0242 | 0.0005 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema68_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema68_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema68_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema68_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema68_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema68_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema68_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema68_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema68_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema68_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema68_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema68_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
