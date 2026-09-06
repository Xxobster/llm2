# Autonomy public-indicator hunt gen 021

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T093118Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `plus_vi_cross_up` | one_head_filter_pi_star | 21 | 1.7280 | 1.8967 | 0.5714 | 1.2138 | 0.0260 | 0.2381 | TPM<MIN | RAN |
| SOLUSDT | 8 | `minus_vi_cross_up` | one_head_filter_pi_star | 19 | 1.5631 | 2.7775 | 0.6842 | 1.6653 | 0.0239 | 0.2632 | TPM<MIN | RAN |
| SOLUSDT | 4 | `minus_vi_cross_up` | one_head_filter_pi_star | 21 | 1.7954 | 1.9816 | 0.5714 | 1.3259 | 0.0212 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 4 | `minus_vi_dom_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8147 | 0.6802 | 3.8819 | 0.0208 | 0.3694 | EBR>35% | RAN |
| ETHUSDT | 8 | `minus_vi_dom_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7579 | 0.6757 | 3.7153 | 0.0199 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `minus_vi_dom_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1711 | 0.6909 | 4.0261 | 0.0177 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 8 | `minus_vi_dom_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1673 | 0.6946 | 4.0090 | 0.0175 | 0.4132 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `plus_vi_cross_up` | one_head_filter_pi_star | 31 | 2.6949 | 1.7096 | 0.6452 | 1.2408 | 0.0136 | 0.1613 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `plus_vi_cross_up` | one_head_filter_pi_star | 16 | 1.3909 | 1.5491 | 0.6250 | 0.7384 | 0.0091 | 0.1875 | TPM<MIN | RAN |
| ETHUSDT | 4 | `plus_vi_cross_up` | one_head_filter_pi_star | 17 | 1.4701 | 1.2161 | 0.4706 | 0.3411 | 0.0090 | 0.1765 | TPM<MIN | RAN |
| ETHUSDT | 8 | `plus_vi_dom_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2539 | 0.5926 | 1.1548 | 0.0079 | 0.2037 | ok | RAN |
| ETHUSDT | 4 | `plus_vi_dom_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1953 | 0.5901 | 0.9048 | 0.0063 | 0.2050 | ok | RAN |
| SOLUSDT | 8 | `plus_vi_dom_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3748 | 0.5943 | 2.0201 | 0.0055 | 0.2453 | ok | RAN |
| SOLUSDT | 4 | `plus_vi_dom_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3698 | 0.5962 | 1.9952 | 0.0055 | 0.2394 | ok | RAN |
| ETHUSDT | 4 | `minus_vi_cross_up` | one_head_filter_pi_star | 32 | 2.6517 | 1.0462 | 0.5625 | 0.1129 | 0.0022 | 0.1562 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `minus_vi_cross_up` | one_head_filter_pi_star | 33 | 2.8140 | 0.9156 | 0.5455 | -0.2293 | -0.0041 | 0.1515 | TPM<MIN | RAN |
| BTCUSDT | 4 | `plus_vi_dom_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `plus_vi_dom_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `minus_vi_dom_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `plus_vi_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `minus_vi_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `minus_vi_dom_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `plus_vi_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `minus_vi_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
