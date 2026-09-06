# Autonomy public-indicator hunt gen 934

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T051201Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma490_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0790 | 0.7026 | 4.7055 | 0.0243 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma490_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0318 | 0.6923 | 4.5303 | 0.0235 | 0.3795 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma490_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.1360 | 0.6902 | 4.2975 | 0.0161 | 0.3696 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma490_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1143 | 0.6833 | 4.1559 | 0.0156 | 0.3778 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma490_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.5227 | 0.6178 | 2.4829 | 0.0079 | 0.2565 | ok | RAN |
| SOLUSDT | 4 | `wma490_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4562 | 0.6062 | 2.2214 | 0.0072 | 0.2591 | ok | RAN |
| ETHUSDT | 4 | `wma490_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2036 | 0.5928 | 1.0975 | 0.0071 | 0.2216 | ok | RAN |
| ETHUSDT | 8 | `wma490_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.1451 | 0.5851 | 0.8066 | 0.0053 | 0.2181 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma490_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma490_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma490_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma490_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma490_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma490_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
