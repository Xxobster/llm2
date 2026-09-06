# Autonomy public-indicator hunt gen 011

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T080352Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `roc_cross_up_0` | one_head_filter_pi_star | 13 | 1.1123 | 6.9205 | 0.9231 | 2.5770 | 0.0870 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 8 | `roc_cross_up_0` | one_head_filter_pi_star | 23 | 1.8926 | 1.9218 | 0.6957 | 1.3979 | 0.0286 | 0.3478 | TPM<MIN | RAN |
| ETHUSDT | 8 | `roc_neg_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.8460 | 0.6835 | 3.9494 | 0.0212 | 0.3670 | EBR>35% | RAN |
| ETHUSDT | 4 | `roc_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7996 | 0.6787 | 3.8287 | 0.0205 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `roc_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2432 | 0.6970 | 4.1797 | 0.0182 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 4 | `roc_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1934 | 0.6975 | 4.0567 | 0.0181 | 0.4259 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `roc_cross_up_0` | one_head_filter_pi_star | 12 | 1.1832 | 1.5319 | 0.6667 | 0.7043 | 0.0123 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `roc_cross_down_0` | one_head_filter_pi_star | 16 | 1.4805 | 1.6337 | 0.6875 | 0.8461 | 0.0121 | 0.0625 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `roc_pos_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2654 | 0.6037 | 1.1930 | 0.0084 | 0.2134 | ok | RAN |
| ETHUSDT | 4 | `roc_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1956 | 0.5901 | 0.9106 | 0.0063 | 0.1988 | ok | RAN |
| SOLUSDT | 8 | `roc_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3853 | 0.5945 | 2.0958 | 0.0058 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `roc_pos_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3488 | 0.5915 | 1.8967 | 0.0051 | 0.2394 | ok | RAN |
| SOLUSDT | 8 | `roc_cross_down_0` | one_head_filter_pi_star | 23 | 2.1282 | 1.2265 | 0.6087 | 0.3995 | 0.0028 | 0.0870 | TPM<MIN | RAN |
| ETHUSDT | 8 | `roc_cross_down_0` | one_head_filter_pi_star | 19 | 2.3109 | 1.0658 | 0.5789 | 0.1380 | 0.0024 | 0.1579 | TPM<MIN | RAN |
| ETHUSDT | 4 | `roc_cross_down_0` | one_head_filter_pi_star | 12 | 1.4595 | 1.0467 | 0.5833 | 0.0813 | 0.0017 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `roc_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `roc_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `roc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `roc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `roc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `roc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `roc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `roc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `roc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
