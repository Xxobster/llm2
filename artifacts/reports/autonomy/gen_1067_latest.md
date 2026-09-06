# Autonomy public-indicator hunt gen 1067

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T185809Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma607_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0613 | 0.6898 | 4.3726 | 0.0243 | 0.4064 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma607_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.9098 | 0.6733 | 4.1090 | 0.0215 | 0.3713 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma607_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.7782 | 0.6649 | 3.4089 | 0.0121 | 0.3247 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma607_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7791 | 0.6571 | 3.5050 | 0.0116 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma607_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.6121 | 0.6276 | 2.4476 | 0.0094 | 0.3172 | ok | RAN |
| SOLUSDT | 4 | `sma607_above_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.5794 | 0.6149 | 2.4241 | 0.0093 | 0.3168 | ok | RAN |
| ETHUSDT | 4 | `sma607_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.1953 | 0.6082 | 0.9798 | 0.0071 | 0.2105 | ok | RAN |
| ETHUSDT | 8 | `sma607_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.1201 | 0.5917 | 0.6304 | 0.0044 | 0.2189 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma607_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma607_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma607_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma607_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma607_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma607_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma607_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma607_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma607_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma607_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma607_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma607_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma607_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma607_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma607_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma607_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
