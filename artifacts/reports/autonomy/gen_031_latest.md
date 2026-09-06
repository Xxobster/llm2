# Autonomy public-indicator hunt gen 031

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T113136Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `cci_cross_up_neg100` | one_head_filter_pi_star | 19 | 1.7380 | 4.5622 | 0.7895 | 2.7205 | 0.0220 | 0.5789 | EBR>35% | RAN |
| ETHUSDT | 4 | `cci_oversold_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.6906 | 0.6722 | 3.2518 | 0.0207 | 0.3833 | EBR>35% | RAN |
| ETHUSDT | 8 | `cci_cross_up_neg100` | one_head_filter_pi_star | 202 | 16.5016 | 1.7809 | 0.6683 | 3.5813 | 0.0198 | 0.3911 | EBR>35% | RAN |
| ETHUSDT | 4 | `cci_cross_down_100` | one_head_filter_pi_star | 31 | 3.0876 | 1.9365 | 0.6452 | 1.9596 | 0.0193 | 0.1613 | TPM<MIN | RAN |
| SOLUSDT | 4 | `cci_oversold_at_h` | one_head_filter_pi_star | 128 | 10.4667 | 2.1119 | 0.6797 | 3.3606 | 0.0192 | 0.4062 | EBR>35% | RAN |
| SOLUSDT | 8 | `cci_cross_up_neg100` | one_head_filter_pi_star | 159 | 13.0016 | 2.1273 | 0.6918 | 3.8760 | 0.0175 | 0.4214 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `cci_cross_up_neg100` | one_head_filter_pi_star | 44 | 3.8513 | 1.7031 | 0.6591 | 1.7033 | 0.0152 | 0.3182 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `cci_cross_down_100` | one_head_filter_pi_star | 154 | 12.7083 | 1.2430 | 0.6039 | 1.1256 | 0.0074 | 0.2013 | ok | RAN |
| ETHUSDT | 4 | `cci_overbought_at_h` | one_head_filter_pi_star | 131 | 10.8103 | 1.1688 | 0.5954 | 0.7493 | 0.0061 | 0.2061 | ok | RAN |
| SOLUSDT | 8 | `cci_cross_down_100` | one_head_filter_pi_star | 195 | 15.9004 | 1.3392 | 0.5897 | 1.7918 | 0.0052 | 0.2615 | ok | RAN |
| SOLUSDT | 4 | `cci_overbought_at_h` | one_head_filter_pi_star | 172 | 14.1048 | 1.1873 | 0.5581 | 0.9906 | 0.0034 | 0.2733 | ok | RAN |
| SOLUSDT | 4 | `cci_cross_down_100` | one_head_filter_pi_star | 53 | 4.3502 | 1.1605 | 0.5849 | 0.4579 | 0.0026 | 0.1321 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `cci_cross_down_100` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `cci_overbought_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5998 | 0.3333 | -0.8270 | -0.0456 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 8 | `cci_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `cci_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `cci_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `cci_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `cci_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `cci_cross_up_neg100` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `cci_cross_down_100` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cci_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cci_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cci_cross_up_neg100` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
