# Autonomy public-indicator hunt gen 1438

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T180846Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma402_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0109 | 0.6979 | 4.4793 | 0.0238 | 0.3854 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma402_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8826 | 0.6862 | 4.1440 | 0.0219 | 0.3830 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma402_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.0888 | 0.6889 | 4.0899 | 0.0158 | 0.3889 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma402_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1444 | 0.6914 | 4.2029 | 0.0156 | 0.3600 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma402_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2883 | 0.6031 | 1.4895 | 0.0096 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `wma402_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2643 | 0.5989 | 1.3568 | 0.0089 | 0.2193 | ok | RAN |
| SOLUSDT | 8 | `wma402_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.5104 | 0.6134 | 2.4617 | 0.0075 | 0.2629 | ok | RAN |
| SOLUSDT | 4 | `wma402_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3297 | 0.5920 | 1.7303 | 0.0053 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma402_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma402_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma402_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma402_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma402_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma402_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma402_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma402_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma402_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma402_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma402_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma402_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma402_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma402_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma402_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma402_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
