# Autonomy public-indicator hunt gen 190

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T215442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma12_above_at_h` | one_head_filter_pi_star | 15 | 1.3351 | 5.4162 | 0.8667 | 2.1695 | 0.0979 | 0.7333 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma12_below_at_h` | one_head_filter_pi_star | 25 | 2.5821 | 7.5476 | 0.8800 | 3.7200 | 0.0664 | 0.6000 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma12_below_at_h` | one_head_filter_pi_star | 22 | 1.9779 | 2.6122 | 0.6818 | 2.1407 | 0.0340 | 0.5455 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma12_above_at_h` | one_head_filter_pi_star | 28 | 2.3857 | 2.2294 | 0.7500 | 1.9593 | 0.0231 | 0.3929 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma12_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.7965 | 0.6771 | 3.8555 | 0.0205 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma12_cross_up` | one_head_filter_pi_star | 14 | 1.1520 | 1.7919 | 0.5714 | 0.9155 | 0.0191 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma12_cross_up` | one_head_filter_pi_star | 215 | 17.5635 | 1.6518 | 0.6605 | 3.1228 | 0.0181 | 0.3535 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma12_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1451 | 0.6852 | 3.9630 | 0.0175 | 0.4136 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma12_cross_up` | one_head_filter_pi_star | 139 | 11.4234 | 2.0985 | 0.6978 | 3.3302 | 0.0155 | 0.3813 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma12_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2184 | 0.5926 | 1.0075 | 0.0071 | 0.2037 | ok | RAN |
| SOLUSDT | 4 | `wma12_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3846 | 0.5943 | 2.0833 | 0.0056 | 0.2453 | ok | RAN |
| SOLUSDT | 8 | `wma12_cross_down` | one_head_filter_pi_star | 201 | 16.3896 | 1.3345 | 0.5920 | 1.7475 | 0.0047 | 0.2189 | ok | RAN |
| SOLUSDT | 4 | `wma12_cross_down` | one_head_filter_pi_star | 11 | 1.0712 | 1.4222 | 0.6364 | 0.4567 | 0.0035 | 0.0909 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma12_cross_down` | one_head_filter_pi_star | 152 | 12.5433 | 1.1043 | 0.5789 | 0.4973 | 0.0033 | 0.1711 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma12_cross_down` | one_head_filter_pi_star | 11 | 1.1919 | 0.5385 | 0.4545 | -0.8264 | -0.0172 | 0.1818 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma12_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma12_cross_down` | one_head_filter_pi_star | 15 | 1.2765 | 0.1396 | 0.2000 | -2.1854 | -0.0766 | 0.0000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `wma12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma12_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma12_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma12_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma12_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
