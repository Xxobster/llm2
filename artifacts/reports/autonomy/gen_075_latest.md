# Autonomy public-indicator hunt gen 075

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T142806Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `stdist_cross_down_0` | one_head_filter_pi_star | 13 | 1.0705 | 2.5758 | 0.5385 | 1.2612 | 0.0230 | 0.2308 | TPM<MIN | RAN |
| ETHUSDT | 8 | `stdist_cross_down_0` | one_head_filter_pi_star | 23 | 1.9680 | 1.9497 | 0.6087 | 1.2955 | 0.0229 | 0.3043 | TPM<MIN | RAN |
| SOLUSDT | 8 | `stdist_cross_up_0` | one_head_filter_pi_star | 17 | 1.4779 | 2.7369 | 0.7647 | 1.6131 | 0.0210 | 0.1176 | TPM<MIN | RAN |
| ETHUSDT | 4 | `stdist_neg_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.7765 | 0.6651 | 3.7977 | 0.0208 | 0.3670 | EBR>35% | RAN |
| ETHUSDT | 8 | `stdist_neg_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.7265 | 0.6698 | 3.5833 | 0.0197 | 0.3726 | EBR>35% | RAN |
| SOLUSDT | 8 | `stdist_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1843 | 0.6864 | 4.1941 | 0.0181 | 0.4142 | EBR>35% | RAN |
| SOLUSDT | 4 | `stdist_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1727 | 0.6860 | 4.2110 | 0.0179 | 0.4070 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `stdist_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2675 | 0.6125 | 1.2115 | 0.0081 | 0.2125 | ok | RAN |
| ETHUSDT | 4 | `stdist_pos_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.2575 | 0.6154 | 1.1813 | 0.0079 | 0.2130 | ok | RAN |
| SOLUSDT | 4 | `stdist_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3536 | 0.5971 | 1.8688 | 0.0052 | 0.2476 | ok | RAN |
| SOLUSDT | 8 | `stdist_pos_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3011 | 0.5894 | 1.6382 | 0.0045 | 0.2415 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `stdist_cross_up_0` | one_head_filter_pi_star | 12 | 1.1162 | 0.4648 | 0.1667 | -1.0712 | -0.0333 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `stdist_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `stdist_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `stdist_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `stdist_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `stdist_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `stdist_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stdist_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `stdist_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stdist_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stdist_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `stdist_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stdist_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
