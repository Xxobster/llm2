# Autonomy public-indicator hunt gen 1086

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T211955Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma585_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.0376 | 0.6985 | 4.5550 | 0.0240 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma585_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0040 | 0.6952 | 4.4291 | 0.0233 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma585_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.8888 | 0.6585 | 3.8567 | 0.0134 | 0.3512 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma585_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.9039 | 0.6633 | 3.8073 | 0.0131 | 0.3618 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma585_above_at_h` | one_head_filter_pi_star | 175 | 14.4412 | 1.2558 | 0.6057 | 1.3025 | 0.0088 | 0.2171 | ok | RAN |
| SOLUSDT | 8 | `wma585_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.5133 | 0.6105 | 2.4606 | 0.0079 | 0.2579 | ok | RAN |
| ETHUSDT | 4 | `wma585_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2238 | 0.6021 | 1.1814 | 0.0079 | 0.2147 | ok | RAN |
| SOLUSDT | 4 | `wma585_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4935 | 0.6108 | 2.3232 | 0.0078 | 0.2595 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma585_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma585_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma585_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma585_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma585_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma585_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
