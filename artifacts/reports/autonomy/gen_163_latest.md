# Autonomy public-indicator hunt gen 163

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T201047Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma35_cross_up` | one_head_filter_pi_star | 12 | 1.2249 | 29.3199 | 0.8333 | 3.1906 | 0.0706 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma35_cross_down` | one_head_filter_pi_star | 14 | 1.3547 | 1.9120 | 0.7143 | 1.1054 | 0.0265 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma35_cross_down` | one_head_filter_pi_star | 26 | 2.2865 | 3.1451 | 0.6923 | 2.1576 | 0.0242 | 0.0769 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma35_cross_down` | one_head_filter_pi_star | 24 | 1.9888 | 1.7007 | 0.6250 | 1.0690 | 0.0227 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma35_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8886 | 0.6861 | 4.1896 | 0.0224 | 0.3767 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma35_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7913 | 0.6757 | 3.8736 | 0.0209 | 0.3694 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma35_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1923 | 0.6914 | 4.0944 | 0.0180 | 0.4198 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma35_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1597 | 0.6914 | 3.9988 | 0.0176 | 0.4198 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma35_cross_up` | one_head_filter_pi_star | 21 | 1.7337 | 1.2888 | 0.5714 | 0.5024 | 0.0100 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma35_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2180 | 0.5949 | 1.0268 | 0.0066 | 0.2025 | ok | RAN |
| SOLUSDT | 4 | `sma35_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3633 | 0.5953 | 1.9734 | 0.0054 | 0.2419 | ok | RAN |
| SOLUSDT | 8 | `sma35_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3610 | 0.5953 | 1.9510 | 0.0053 | 0.2419 | ok | RAN |
| ETHUSDT | 8 | `sma35_above_at_h` | one_head_filter_pi_star | 156 | 12.8733 | 1.1523 | 0.5897 | 0.7211 | 0.0049 | 0.1987 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma35_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma35_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma35_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma35_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma35_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma35_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma35_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
