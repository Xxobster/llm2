# Autonomy public-indicator hunt gen 440

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T115030Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma700_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0776 | 0.6898 | 4.4519 | 0.0247 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma700_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.0551 | 0.6875 | 4.2898 | 0.0232 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma700_below_at_h` | one_head_filter_pi_star | 222 | 18.0601 | 1.8119 | 0.6622 | 3.6568 | 0.0123 | 0.3198 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma700_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.6985 | 0.6343 | 2.5410 | 0.0104 | 0.3134 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma700_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.6347 | 0.6455 | 2.8437 | 0.0103 | 0.3228 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma700_above_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.6216 | 0.6242 | 2.5336 | 0.0099 | 0.3154 | ok | RAN |
| ETHUSDT | 8 | `sma700_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.1550 | 0.6000 | 0.7807 | 0.0055 | 0.2129 | ok | RAN |
| ETHUSDT | 4 | `sma700_above_at_h` | one_head_filter_pi_star | 139 | 11.4705 | 1.0908 | 0.5827 | 0.4405 | 0.0034 | 0.2158 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma700_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma700_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
