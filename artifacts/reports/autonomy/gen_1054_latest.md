# Autonomy public-indicator hunt gen 1054

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T171048Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma565_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9684 | 0.6882 | 4.2609 | 0.0230 | 0.3817 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma565_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9626 | 0.6904 | 4.3919 | 0.0225 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma565_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 2.0510 | 0.6788 | 4.2198 | 0.0151 | 0.3627 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma565_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.9379 | 0.6667 | 3.8549 | 0.0139 | 0.3646 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma565_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2375 | 0.5979 | 1.2587 | 0.0083 | 0.2216 | ok | RAN |
| ETHUSDT | 8 | `wma565_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.2241 | 0.5924 | 1.1769 | 0.0078 | 0.2174 | ok | RAN |
| SOLUSDT | 4 | `wma565_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4571 | 0.6105 | 2.2340 | 0.0073 | 0.2579 | ok | RAN |
| SOLUSDT | 8 | `wma565_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4378 | 0.6000 | 2.1466 | 0.0069 | 0.2579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma565_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma565_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma565_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma565_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
