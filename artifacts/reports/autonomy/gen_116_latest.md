# Autonomy public-indicator hunt gen 116

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T170534Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma8_below_at_h` | one_head_filter_pi_star | 26 | 2.1896 | 2.0592 | 0.6538 | 1.3365 | 0.0232 | 0.2692 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma8_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.7285 | 0.6698 | 3.4109 | 0.0198 | 0.3721 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma8_cross_up` | one_head_filter_pi_star | 225 | 18.3804 | 1.7476 | 0.6667 | 3.6425 | 0.0193 | 0.3689 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma8_cross_up` | one_head_filter_pi_star | 164 | 13.4104 | 2.3644 | 0.7012 | 4.4477 | 0.0191 | 0.3963 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma8_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.0978 | 0.6770 | 3.8449 | 0.0171 | 0.4161 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma8_cross_up` | one_head_filter_pi_star | 14 | 1.2397 | 1.2709 | 0.5714 | 0.4127 | 0.0083 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma8_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2232 | 0.5988 | 1.0250 | 0.0073 | 0.2037 | ok | RAN |
| ETHUSDT | 8 | `sma8_cross_down` | one_head_filter_pi_star | 168 | 13.8636 | 1.2199 | 0.5952 | 1.0462 | 0.0071 | 0.2143 | ok | RAN |
| SOLUSDT | 8 | `sma8_cross_down` | one_head_filter_pi_star | 210 | 17.1235 | 1.4702 | 0.6095 | 2.4154 | 0.0065 | 0.2286 | ok | RAN |
| SOLUSDT | 4 | `sma8_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3910 | 0.5972 | 2.0935 | 0.0059 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `sma8_above_at_h` | one_head_filter_pi_star | 12 | 1.2932 | 1.2555 | 0.5000 | 0.4153 | 0.0058 | 0.5833 | EBR>35% | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma8_cross_down` | one_head_filter_pi_star | 29 | 2.7906 | 0.9974 | 0.5517 | -0.0062 | -0.0000 | 0.0690 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma8_cross_down` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma8_cross_down` | one_head_filter_pi_star | 11 | 1.1018 | 0.1500 | 0.2727 | -1.9862 | -0.0419 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma8_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma8_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma8_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma8_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma8_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma8_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma8_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma8_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma8_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma8_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
