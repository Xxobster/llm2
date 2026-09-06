# Autonomy public-indicator hunt gen 462

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T152725Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma195_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0072 | 0.6939 | 4.5643 | 0.0235 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma195_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9436 | 0.6895 | 4.3088 | 0.0224 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma195_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.3663 | 0.7101 | 4.5669 | 0.0188 | 0.3905 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma195_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2306 | 0.6936 | 4.3244 | 0.0176 | 0.3815 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma195_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2015 | 0.6022 | 1.0440 | 0.0069 | 0.2151 | ok | RAN |
| ETHUSDT | 4 | `wma195_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.1688 | 0.5957 | 0.8859 | 0.0058 | 0.2181 | ok | RAN |
| SOLUSDT | 4 | `wma195_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3194 | 0.5922 | 1.6765 | 0.0050 | 0.2670 | ok | RAN |
| SOLUSDT | 8 | `wma195_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3181 | 0.5897 | 1.6658 | 0.0049 | 0.2718 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma195_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma195_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma195_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma195_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
