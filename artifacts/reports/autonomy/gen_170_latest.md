# Autonomy public-indicator hunt gen 170

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T203812Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret20_neg_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8355 | 0.6773 | 4.0246 | 0.0218 | 0.3773 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret20_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8256 | 0.6816 | 3.9595 | 0.0214 | 0.3767 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret20_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2201 | 0.6951 | 4.1616 | 0.0183 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret20_neg_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.1992 | 0.6981 | 3.9753 | 0.0176 | 0.4214 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret20_cross_down_0` | one_head_filter_pi_star | 54 | 4.4582 | 1.4266 | 0.5926 | 1.0760 | 0.0159 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret20_cross_down_0` | one_head_filter_pi_star | 31 | 2.6164 | 1.8232 | 0.6452 | 1.4258 | 0.0149 | 0.1935 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret20_cross_up_0` | one_head_filter_pi_star | 29 | 2.5382 | 1.6777 | 0.5862 | 1.1285 | 0.0128 | 0.1724 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret20_cross_up_0` | one_head_filter_pi_star | 16 | 1.3656 | 1.7692 | 0.5625 | 0.8655 | 0.0121 | 0.1250 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret20_cross_down_0` | one_head_filter_pi_star | 21 | 1.7847 | 1.3265 | 0.5714 | 0.5591 | 0.0104 | 0.1905 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret20_pos_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.2618 | 0.6125 | 1.2199 | 0.0079 | 0.1938 | ok | RAN |
| SOLUSDT | 8 | `ret20_pos_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3920 | 0.6039 | 2.0673 | 0.0058 | 0.2512 | ok | RAN |
| ETHUSDT | 8 | `ret20_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1745 | 0.5875 | 0.8170 | 0.0058 | 0.2062 | ok | RAN |
| SOLUSDT | 4 | `ret20_pos_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3224 | 0.5894 | 1.7468 | 0.0048 | 0.2464 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret20_cross_up_0` | one_head_filter_pi_star | 19 | 1.6203 | 0.9926 | 0.4211 | -0.0139 | -0.0004 | 0.3684 | EBR>35% | RAN |
| BTCUSDT | 4 | `ret20_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret20_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret20_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret20_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret20_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret20_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret20_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret20_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret20_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret20_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
