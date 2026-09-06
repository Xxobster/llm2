# Autonomy public-indicator hunt gen 017

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T083513Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `trix_cross_up_0` | one_head_filter_pi_star | 32 | 2.7782 | 1.5877 | 0.6875 | 1.0143 | 0.0216 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `trix_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8317 | 0.6718 | 3.8475 | 0.0213 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 8 | `trix_neg_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.7739 | 0.6699 | 3.7405 | 0.0200 | 0.3738 | EBR>35% | RAN |
| ETHUSDT | 8 | `trix_cross_up_0` | one_head_filter_pi_star | 44 | 3.8201 | 1.6683 | 0.6364 | 1.3147 | 0.0191 | 0.2273 | TPM<MIN | RAN |
| SOLUSDT | 8 | `trix_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1260 | 0.6867 | 4.0158 | 0.0175 | 0.3976 | EBR>35% | RAN |
| SOLUSDT | 4 | `trix_cross_up_0` | one_head_filter_pi_star | 41 | 3.8805 | 2.2109 | 0.6585 | 2.1484 | 0.0175 | 0.2439 | TPM<MIN | RAN |
| SOLUSDT | 4 | `trix_neg_at_h` | one_head_filter_pi_star | 182 | 14.9459 | 1.9364 | 0.6703 | 3.7569 | 0.0155 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `trix_cross_down_0` | one_head_filter_pi_star | 24 | 2.2155 | 1.5241 | 0.6667 | 0.9754 | 0.0122 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 8 | `trix_cross_up_0` | one_head_filter_pi_star | 53 | 4.9557 | 1.6442 | 0.6038 | 1.6070 | 0.0106 | 0.2075 | ok | RAN |
| SOLUSDT | 8 | `trix_cross_down_0` | one_head_filter_pi_star | 32 | 2.6549 | 1.5274 | 0.5938 | 1.0121 | 0.0105 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `trix_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2535 | 0.6064 | 1.2765 | 0.0082 | 0.2234 | ok | RAN |
| SOLUSDT | 4 | `trix_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.5453 | 0.6179 | 2.6943 | 0.0076 | 0.2594 | ok | RAN |
| ETHUSDT | 8 | `trix_cross_down_0` | one_head_filter_pi_star | 59 | 4.9422 | 1.1934 | 0.5593 | 0.5930 | 0.0067 | 0.2542 | ok | RAN |
| SOLUSDT | 8 | `trix_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.4648 | 0.6121 | 2.3531 | 0.0066 | 0.2570 | ok | RAN |
| ETHUSDT | 8 | `trix_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1770 | 0.5975 | 0.8415 | 0.0055 | 0.2075 | ok | RAN |
| ETHUSDT | 4 | `trix_cross_down_0` | one_head_filter_pi_star | 33 | 2.9697 | 1.0670 | 0.5152 | 0.1673 | 0.0026 | 0.2424 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `trix_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `trix_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `trix_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `trix_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `trix_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `trix_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `trix_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `trix_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
