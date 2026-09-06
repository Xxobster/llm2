# Autonomy public-indicator hunt gen 414

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T052957Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma165_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0237 | 0.6990 | 4.6506 | 0.0239 | 0.3673 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma165_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.8501 | 0.6765 | 4.0699 | 0.0213 | 0.3676 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma165_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2298 | 0.6923 | 4.2580 | 0.0180 | 0.3905 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma165_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2081 | 0.6964 | 4.2003 | 0.0174 | 0.3929 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma165_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.1865 | 0.5946 | 0.9455 | 0.0064 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `wma165_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.1875 | 0.5955 | 0.9543 | 0.0064 | 0.2079 | ok | RAN |
| SOLUSDT | 4 | `wma165_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.2752 | 0.5920 | 1.4661 | 0.0043 | 0.2637 | ok | RAN |
| SOLUSDT | 8 | `wma165_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2738 | 0.5825 | 1.4705 | 0.0042 | 0.2621 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma165_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma165_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma165_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma165_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
