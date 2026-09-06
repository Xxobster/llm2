# Autonomy public-indicator hunt gen 074

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T142432Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `tenkan_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.9256 | 0.6959 | 4.2450 | 0.0233 | 0.3825 | EBR>35% | RAN |
| SOLUSDT | 8 | `tenkan_above_at_h` | one_head_filter_pi_star | 64 | 5.3870 | 2.7629 | 0.7500 | 3.3095 | 0.0224 | 0.4219 | EBR>35% | RAN |
| SOLUSDT | 4 | `tenkan_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.3262 | 0.6957 | 4.3129 | 0.0192 | 0.4286 | EBR>35% | RAN |
| ETHUSDT | 8 | `tenkan_cross_up` | one_head_filter_pi_star | 203 | 16.5832 | 1.6604 | 0.6552 | 3.1482 | 0.0180 | 0.3498 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `tenkan_cross_up` | one_head_filter_pi_star | 114 | 9.3313 | 2.1528 | 0.7193 | 3.2675 | 0.0151 | 0.3772 | EBR>35% | RAN |
| ETHUSDT | 8 | `tenkan_above_at_h` | one_head_filter_pi_star | 174 | 14.2166 | 1.4706 | 0.6437 | 2.1553 | 0.0141 | 0.2931 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `tenkan_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.1824 | 0.5886 | 0.8436 | 0.0061 | 0.1962 | ok | RAN |
| SOLUSDT | 4 | `tenkan_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3671 | 0.5962 | 1.9766 | 0.0054 | 0.2441 | ok | RAN |
| ETHUSDT | 8 | `tenkan_cross_down` | one_head_filter_pi_star | 132 | 10.8928 | 1.1674 | 0.5833 | 0.7540 | 0.0050 | 0.1439 | ok | RAN |
| SOLUSDT | 8 | `tenkan_cross_down` | one_head_filter_pi_star | 175 | 14.2696 | 1.3610 | 0.6000 | 1.7505 | 0.0049 | 0.1829 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `tenkan_cross_down` | one_head_filter_pi_star | 11 | 1.0712 | 1.0122 | 0.6364 | 0.0165 | 0.0001 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `tenkan_below_at_h` | one_head_filter_pi_star | 8 | 0.8773 | 0.6979 | 0.3750 | -0.4297 | -0.0050 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `tenkan_cross_down` | one_head_filter_pi_star | 20 | 1.8013 | 0.5242 | 0.5000 | -1.1340 | -0.0241 | 0.1500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `tenkan_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `tenkan_cross_down` | one_head_filter_pi_star | 14 | 1.1914 | 0.1459 | 0.2143 | -2.0956 | -0.0832 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `tenkan_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `tenkan_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `tenkan_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `tenkan_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `tenkan_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `tenkan_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `tenkan_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `tenkan_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `tenkan_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
