# Autonomy public-indicator hunt gen 457

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T150809Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema700_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0292 | 0.6837 | 4.1538 | 0.0228 | 0.3827 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema700_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8360 | 0.6717 | 3.7395 | 0.0200 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema700_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.8322 | 0.6635 | 3.6756 | 0.0126 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema700_below_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.7782 | 0.6511 | 3.6695 | 0.0119 | 0.3106 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema700_above_at_h` | one_head_filter_pi_star | 147 | 11.9864 | 1.6550 | 0.6259 | 2.6044 | 0.0100 | 0.3265 | ok | RAN |
| SOLUSDT | 4 | `ema700_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.5726 | 0.6349 | 2.1514 | 0.0088 | 0.3333 | ok | RAN |
| ETHUSDT | 8 | `ema700_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.2312 | 0.6164 | 1.0896 | 0.0083 | 0.2013 | ok | RAN |
| ETHUSDT | 4 | `ema700_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1781 | 0.5941 | 0.8791 | 0.0064 | 0.2059 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema700_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema700_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
