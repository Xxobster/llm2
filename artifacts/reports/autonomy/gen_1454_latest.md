# Autonomy public-indicator hunt gen 1454

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T221843Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma404_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9542 | 0.6973 | 4.3233 | 0.0225 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma404_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8536 | 0.6809 | 3.8963 | 0.0215 | 0.3777 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma404_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.2593 | 0.7000 | 4.5025 | 0.0174 | 0.3889 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma404_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2280 | 0.7018 | 4.2799 | 0.0171 | 0.3801 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma404_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.2404 | 0.5989 | 1.2483 | 0.0084 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `wma404_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2014 | 0.5909 | 1.0322 | 0.0070 | 0.2102 | ok | RAN |
| SOLUSDT | 8 | `wma404_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4368 | 0.6085 | 2.1420 | 0.0068 | 0.2593 | ok | RAN |
| SOLUSDT | 4 | `wma404_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3454 | 0.5969 | 1.7542 | 0.0054 | 0.2704 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma404_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma404_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma404_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma404_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma404_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma404_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma404_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma404_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma404_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma404_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma404_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma404_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma404_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma404_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma404_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma404_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
