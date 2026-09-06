# Autonomy public-indicator hunt gen 491

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T171946Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma250_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0150 | 0.6989 | 4.4865 | 0.0239 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma250_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9788 | 0.6957 | 4.3160 | 0.0235 | 0.3859 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma250_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1953 | 0.6937 | 4.1016 | 0.0172 | 0.3875 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma250_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.1115 | 0.6839 | 4.0429 | 0.0159 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma250_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2936 | 0.6043 | 1.5105 | 0.0098 | 0.2353 | ok | RAN |
| ETHUSDT | 4 | `sma250_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.2839 | 0.6077 | 1.3997 | 0.0093 | 0.2320 | ok | RAN |
| SOLUSDT | 8 | `sma250_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.4420 | 0.6085 | 2.2385 | 0.0068 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `sma250_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3329 | 0.5939 | 1.7372 | 0.0055 | 0.2640 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma250_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma250_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma250_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma250_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
