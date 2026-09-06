# Autonomy public-indicator hunt gen 142

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T184804Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma100_cross_up` | one_head_filter_pi_star | 22 | 1.8331 | 4.5890 | 0.6818 | 2.5629 | 0.0269 | 0.2273 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma100_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8705 | 0.6897 | 4.0155 | 0.0220 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma100_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8094 | 0.6829 | 3.9425 | 0.0209 | 0.3610 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma100_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2114 | 0.6886 | 4.1741 | 0.0183 | 0.4132 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma100_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1854 | 0.6890 | 4.0543 | 0.0179 | 0.4146 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma100_cross_down` | one_head_filter_pi_star | 34 | 3.1594 | 1.7295 | 0.6471 | 1.3414 | 0.0133 | 0.1471 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma100_cross_down` | one_head_filter_pi_star | 29 | 2.4031 | 1.3432 | 0.5517 | 0.6803 | 0.0122 | 0.2759 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma100_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.3894 | 0.6145 | 1.8127 | 0.0115 | 0.2402 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma100_above_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.2154 | 0.6012 | 1.0046 | 0.0067 | 0.2139 | ok | RAN |
| SOLUSDT | 8 | `wma100_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3675 | 0.6019 | 1.9372 | 0.0054 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `wma100_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3237 | 0.5943 | 1.7286 | 0.0048 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma100_cross_up` | one_head_filter_pi_star | 20 | 1.7356 | 0.7916 | 0.4500 | -0.4277 | -0.0076 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma100_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma100_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
