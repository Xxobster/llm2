# Autonomy public-indicator hunt gen 547

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T210339Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma298_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9525 | 0.6947 | 4.3361 | 0.0233 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma298_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.8920 | 0.6865 | 4.0788 | 0.0220 | 0.3730 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma298_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.2039 | 0.6893 | 4.3079 | 0.0171 | 0.3729 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma298_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0580 | 0.6807 | 3.8148 | 0.0155 | 0.3735 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma298_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2354 | 0.6000 | 1.2360 | 0.0081 | 0.2205 | ok | RAN |
| SOLUSDT | 8 | `sma298_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.3850 | 0.6099 | 1.8595 | 0.0061 | 0.2582 | ok | RAN |
| ETHUSDT | 4 | `sma298_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.1500 | 0.5924 | 0.8001 | 0.0055 | 0.2228 | ok | RAN |
| SOLUSDT | 4 | `sma298_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3242 | 0.5969 | 1.6614 | 0.0052 | 0.2653 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma298_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma298_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma298_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma298_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma298_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma298_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma298_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma298_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma298_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma298_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma298_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma298_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma298_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma298_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma298_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma298_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
