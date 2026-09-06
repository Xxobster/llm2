# Autonomy public-indicator hunt gen 590

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T235307Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma275_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.1217 | 0.7081 | 4.7806 | 0.0247 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma275_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0494 | 0.7047 | 4.5615 | 0.0244 | 0.3782 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma275_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1692 | 0.6941 | 4.1234 | 0.0169 | 0.3765 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma275_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1061 | 0.6848 | 3.9263 | 0.0161 | 0.3758 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma275_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.1979 | 0.6000 | 1.0078 | 0.0070 | 0.2162 | ok | RAN |
| ETHUSDT | 8 | `wma275_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.1923 | 0.5956 | 1.0008 | 0.0069 | 0.2240 | ok | RAN |
| SOLUSDT | 4 | `wma275_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3642 | 0.5969 | 1.8598 | 0.0057 | 0.2653 | ok | RAN |
| SOLUSDT | 8 | `wma275_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3107 | 0.5862 | 1.6451 | 0.0049 | 0.2611 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma275_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma275_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma275_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma275_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
