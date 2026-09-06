# Autonomy public-indicator hunt gen 670

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T050441Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma325_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1019 | 0.7072 | 4.6513 | 0.0247 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma325_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.8878 | 0.6885 | 4.0503 | 0.0216 | 0.3825 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma325_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2027 | 0.6977 | 4.2116 | 0.0172 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma325_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1417 | 0.6879 | 4.1727 | 0.0161 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma325_above_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2547 | 0.6061 | 1.3320 | 0.0088 | 0.2273 | ok | RAN |
| ETHUSDT | 8 | `wma325_above_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 1.2256 | 0.6020 | 1.1853 | 0.0078 | 0.2239 | ok | RAN |
| SOLUSDT | 4 | `wma325_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3750 | 0.5953 | 1.9477 | 0.0058 | 0.2651 | ok | RAN |
| SOLUSDT | 8 | `wma325_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.2947 | 0.5907 | 1.5516 | 0.0047 | 0.2642 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma325_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma325_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma325_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma325_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
