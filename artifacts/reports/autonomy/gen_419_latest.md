# Autonomy public-indicator hunt gen 419

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T064124Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma190_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9499 | 0.6927 | 4.3845 | 0.0222 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma190_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.8903 | 0.6927 | 4.1726 | 0.0217 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma190_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2154 | 0.6919 | 4.2226 | 0.0173 | 0.3837 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma190_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2569 | 0.6994 | 4.3021 | 0.0171 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma190_above_at_h` | one_head_filter_pi_star | 196 | 16.1742 | 1.2877 | 0.6020 | 1.4695 | 0.0096 | 0.2296 | ok | RAN |
| ETHUSDT | 8 | `sma190_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2551 | 0.5990 | 1.3121 | 0.0088 | 0.2284 | ok | RAN |
| SOLUSDT | 4 | `sma190_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3485 | 0.5969 | 1.7872 | 0.0055 | 0.2653 | ok | RAN |
| SOLUSDT | 8 | `sma190_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3034 | 0.5862 | 1.6119 | 0.0049 | 0.2611 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma190_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma190_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma190_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma190_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
