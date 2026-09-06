# Autonomy public-indicator hunt gen 382

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T221253Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma145_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8760 | 0.6798 | 4.1825 | 0.0220 | 0.3695 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma145_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.8096 | 0.6765 | 3.9682 | 0.0208 | 0.3676 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma145_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2657 | 0.6928 | 4.3128 | 0.0186 | 0.4036 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma145_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2587 | 0.6959 | 4.3708 | 0.0179 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma145_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2901 | 0.6124 | 1.3600 | 0.0091 | 0.2247 | ok | RAN |
| ETHUSDT | 4 | `wma145_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.2336 | 0.5956 | 1.1614 | 0.0076 | 0.2131 | ok | RAN |
| SOLUSDT | 8 | `wma145_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2827 | 0.5825 | 1.5088 | 0.0044 | 0.2621 | ok | RAN |
| SOLUSDT | 4 | `wma145_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2772 | 0.5825 | 1.4811 | 0.0043 | 0.2621 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma145_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma145_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma145_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma145_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
