# Autonomy public-indicator hunt gen 184

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T213152Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma75_cross_up` | one_head_filter_pi_star | 17 | 1.5838 | 11.4809 | 0.7647 | 2.9727 | 0.0395 | 0.2353 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma75_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8575 | 0.6866 | 4.0593 | 0.0218 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma75_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.7586 | 0.6784 | 3.6759 | 0.0199 | 0.3668 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma75_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2813 | 0.6946 | 4.3299 | 0.0189 | 0.4132 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma75_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.2081 | 0.6957 | 4.0968 | 0.0182 | 0.4099 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma75_cross_down` | one_head_filter_pi_star | 19 | 1.8385 | 1.9645 | 0.6842 | 1.3304 | 0.0172 | 0.2105 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma75_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.3182 | 0.6089 | 1.5152 | 0.0096 | 0.2291 | ok | RAN |
| ETHUSDT | 4 | `sma75_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2936 | 0.6034 | 1.3856 | 0.0091 | 0.2346 | ok | RAN |
| SOLUSDT | 8 | `sma75_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3764 | 0.6009 | 1.9858 | 0.0055 | 0.2523 | ok | RAN |
| SOLUSDT | 4 | `sma75_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3052 | 0.5905 | 1.6352 | 0.0046 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma75_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma75_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `sma75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma75_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma75_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
