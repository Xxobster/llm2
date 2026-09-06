# Autonomy public-indicator hunt gen 277

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T035113Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret22_cross_down_0` | one_head_filter_pi_star | 14 | 1.1898 | 5.1502 | 0.7143 | 2.3329 | 0.0565 | 0.4286 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret22_cross_down_0` | one_head_filter_pi_star | 12 | 1.0259 | 8.4604 | 0.7500 | 2.3373 | 0.0448 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret22_cross_down_0` | one_head_filter_pi_star | 20 | 1.6880 | 4.1890 | 0.7000 | 2.3592 | 0.0249 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret22_neg_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.9237 | 0.6912 | 4.1771 | 0.0226 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret22_neg_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.8544 | 0.6825 | 4.0360 | 0.0212 | 0.3886 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret22_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.2232 | 0.7037 | 4.1403 | 0.0185 | 0.4198 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret22_cross_down_0` | one_head_filter_pi_star | 33 | 2.8045 | 1.5219 | 0.5758 | 1.0251 | 0.0179 | 0.1818 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret22_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1607 | 0.6909 | 4.0107 | 0.0176 | 0.4121 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret22_cross_up_0` | one_head_filter_pi_star | 22 | 1.9953 | 2.2209 | 0.6818 | 1.4903 | 0.0167 | 0.1818 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret22_pos_at_h` | one_head_filter_pi_star | 150 | 12.3782 | 1.2194 | 0.6067 | 1.0201 | 0.0068 | 0.1867 | ok | RAN |
| ETHUSDT | 4 | `ret22_pos_at_h` | one_head_filter_pi_star | 156 | 12.8733 | 1.1999 | 0.6026 | 0.9405 | 0.0063 | 0.1859 | ok | RAN |
| SOLUSDT | 4 | `ret22_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3817 | 0.5991 | 2.0451 | 0.0056 | 0.2500 | ok | RAN |
| SOLUSDT | 8 | `ret22_pos_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.2846 | 0.5865 | 1.5775 | 0.0043 | 0.2500 | ok | RAN |
| ETHUSDT | 8 | `ret22_cross_up_0` | one_head_filter_pi_star | 23 | 1.9247 | 1.0678 | 0.3913 | 0.1356 | 0.0028 | 0.1739 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret22_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret22_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret22_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret22_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret22_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret22_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret22_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret22_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret22_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret22_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
