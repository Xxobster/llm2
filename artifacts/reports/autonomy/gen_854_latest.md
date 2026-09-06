# Autonomy public-indicator hunt gen 854

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T204945Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma440_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9586 | 0.6904 | 4.3673 | 0.0232 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma440_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8305 | 0.6862 | 3.9406 | 0.0208 | 0.3883 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma440_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2790 | 0.6977 | 4.3762 | 0.0171 | 0.3895 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma440_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1061 | 0.6914 | 4.0713 | 0.0159 | 0.3714 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma440_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2278 | 0.5978 | 1.1802 | 0.0081 | 0.2228 | ok | RAN |
| SOLUSDT | 8 | `wma440_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.4822 | 0.6162 | 2.3928 | 0.0074 | 0.2475 | ok | RAN |
| ETHUSDT | 8 | `wma440_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.2091 | 0.5978 | 1.1080 | 0.0072 | 0.2065 | ok | RAN |
| SOLUSDT | 4 | `wma440_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.2600 | 0.5773 | 1.3810 | 0.0045 | 0.2680 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma440_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma440_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
