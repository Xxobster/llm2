# Autonomy public-indicator hunt gen 1203

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T103315Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma628_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.0687 | 0.6850 | 4.5034 | 0.0240 | 0.3700 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma628_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9002 | 0.6734 | 4.0878 | 0.0215 | 0.3618 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma628_below_at_h` | one_head_filter_pi_star | 224 | 18.2228 | 1.8570 | 0.6607 | 3.8514 | 0.0131 | 0.3170 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma628_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.6833 | 0.6533 | 3.1126 | 0.0108 | 0.3166 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma628_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5623 | 0.6187 | 2.2222 | 0.0088 | 0.3309 | ok | RAN |
| ETHUSDT | 4 | `sma628_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 1.2422 | 0.6014 | 1.1314 | 0.0084 | 0.2028 | ok | RAN |
| ETHUSDT | 8 | `sma628_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.2243 | 0.6101 | 1.1006 | 0.0082 | 0.2327 | ok | RAN |
| SOLUSDT | 4 | `sma628_above_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.5044 | 0.6093 | 2.1231 | 0.0081 | 0.3046 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma628_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma628_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma628_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma628_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma628_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma628_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma628_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma628_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma628_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma628_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma628_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma628_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma628_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma628_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma628_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma628_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
