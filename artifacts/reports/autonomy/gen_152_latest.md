# Autonomy public-indicator hunt gen 152

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T192650Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma70_cross_up` | one_head_filter_pi_star | 15 | 1.2744 | 10.5533 | 0.7333 | 2.7561 | 0.0562 | 0.2667 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma70_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8398 | 0.6847 | 3.9299 | 0.0216 | 0.3793 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma70_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.7358 | 0.6751 | 3.6830 | 0.0192 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma70_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2224 | 0.6909 | 4.2286 | 0.0185 | 0.4121 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma70_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1490 | 0.6832 | 3.9523 | 0.0177 | 0.4037 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma70_cross_down` | one_head_filter_pi_star | 28 | 2.6114 | 1.5681 | 0.5714 | 1.1077 | 0.0176 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma70_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.4264 | 0.6209 | 1.9524 | 0.0124 | 0.2363 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma70_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2419 | 0.6011 | 1.1345 | 0.0075 | 0.2135 | ok | RAN |
| SOLUSDT | 8 | `sma70_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3764 | 0.6009 | 1.9858 | 0.0055 | 0.2523 | ok | RAN |
| SOLUSDT | 4 | `sma70_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3315 | 0.5953 | 1.7719 | 0.0049 | 0.2512 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma70_cross_down` | one_head_filter_pi_star | 14 | 1.3547 | 0.7707 | 0.5000 | -0.4490 | -0.0071 | 0.2143 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma70_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma70_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma70_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma70_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
