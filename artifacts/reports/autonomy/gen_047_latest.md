# Autonomy public-indicator hunt gen 047

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T123737Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.7984 | 0.6786 | 3.8648 | 0.0205 | 0.3705 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2511 | 0.6970 | 4.1834 | 0.0184 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma_cross_up` | one_head_filter_pi_star | 41 | 3.3738 | 1.3314 | 0.5854 | 0.7942 | 0.0094 | 0.1951 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma_above_at_h` | one_head_filter_pi_star | 152 | 12.5433 | 1.2428 | 0.5987 | 1.0703 | 0.0081 | 0.2039 | ok | RAN |
| ETHUSDT | 4 | `wma_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 8 | `wma_cross_down` | one_head_filter_pi_star | 64 | 5.4190 | 1.5040 | 0.6562 | 1.3718 | 0.0060 | 0.1094 | ok | RAN |
| SOLUSDT | 8 | `wma_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.4012 | 0.5943 | 2.1549 | 0.0060 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `wma_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3855 | 0.5935 | 2.0796 | 0.0057 | 0.2477 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma_cross_down` | one_head_filter_pi_star | 35 | 3.1523 | 0.7567 | 0.5429 | -0.7093 | -0.0089 | 0.1714 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6235 | 0.3333 | -0.7532 | -0.0373 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `wma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
