# Autonomy public-indicator hunt gen 755

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T111046Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma472_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.1131 | 0.6957 | 4.6526 | 0.0249 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma472_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0193 | 0.6947 | 4.4491 | 0.0244 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma472_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.0060 | 0.6791 | 3.9998 | 0.0147 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma472_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.9358 | 0.6649 | 3.6757 | 0.0133 | 0.3403 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma472_above_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.6085 | 0.6207 | 2.6108 | 0.0094 | 0.2931 | ok | RAN |
| SOLUSDT | 8 | `sma472_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.5441 | 0.6150 | 2.5724 | 0.0086 | 0.2700 | ok | RAN |
| ETHUSDT | 8 | `sma472_above_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 1.2213 | 0.5920 | 1.1198 | 0.0077 | 0.2126 | ok | RAN |
| ETHUSDT | 4 | `sma472_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2002 | 0.5862 | 1.0306 | 0.0072 | 0.2069 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma472_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma472_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma472_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma472_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
