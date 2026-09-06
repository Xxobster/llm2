# Autonomy public-indicator hunt gen 174

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T205408Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `wma15_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 1.4958 | 0.4615 | 0.5663 | 0.0372 | 0.0769 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma15_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0774 | 0.7088 | 4.1841 | 0.0271 | 0.3791 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma15_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma15_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0180 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma15_below_at_h` | one_head_filter_pi_star | 142 | 11.6115 | 2.0822 | 0.6690 | 3.6532 | 0.0174 | 0.4085 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma15_cross_up` | one_head_filter_pi_star | 53 | 4.3644 | 1.9233 | 0.6792 | 1.7594 | 0.0127 | 0.3585 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma15_cross_up` | one_head_filter_pi_star | 141 | 11.5949 | 1.3662 | 0.6170 | 1.5626 | 0.0109 | 0.2837 | ok | RAN |
| ETHUSDT | 8 | `wma15_above_at_h` | one_head_filter_pi_star | 134 | 11.0579 | 1.2825 | 0.6045 | 1.1683 | 0.0101 | 0.2239 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma15_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.4179 | 0.6055 | 1.5940 | 0.0085 | 0.3486 | ok | RAN |
| ETHUSDT | 4 | `wma15_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 4 | `wma15_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3856 | 0.5991 | 2.0836 | 0.0057 | 0.2442 | ok | RAN |
| SOLUSDT | 8 | `wma15_cross_down` | one_head_filter_pi_star | 97 | 7.9549 | 1.3651 | 0.6186 | 1.3503 | 0.0046 | 0.1237 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma15_cross_down` | one_head_filter_pi_star | 97 | 8.0398 | 0.9699 | 0.5464 | -0.1300 | -0.0010 | 0.1443 | ok | RAN |
| BTCUSDT | 4 | `wma15_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `wma15_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma15_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma15_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma15_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma15_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma15_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma15_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
