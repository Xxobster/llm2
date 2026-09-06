# Autonomy public-indicator hunt gen 149

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T191500Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret36_neg_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.7968 | 0.6731 | 3.8472 | 0.0208 | 0.3558 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret36_cross_down_0` | one_head_filter_pi_star | 21 | 2.1345 | 1.5397 | 0.5238 | 0.8181 | 0.0205 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret36_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.7240 | 0.6716 | 3.6206 | 0.0192 | 0.3532 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret36_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1159 | 0.6790 | 3.8811 | 0.0173 | 0.4136 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret36_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.9475 | 0.6707 | 3.5501 | 0.0155 | 0.3832 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret36_cross_down_0` | one_head_filter_pi_star | 26 | 2.1410 | 1.8169 | 0.6538 | 1.1526 | 0.0132 | 0.1923 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret36_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.3173 | 0.6080 | 1.5066 | 0.0099 | 0.2443 | ok | RAN |
| SOLUSDT | 8 | `ret36_cross_up_0` | one_head_filter_pi_star | 29 | 2.4580 | 1.4158 | 0.5862 | 0.7801 | 0.0092 | 0.2069 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret36_pos_at_h` | one_head_filter_pi_star | 222 | 18.1020 | 1.5593 | 0.6171 | 2.7491 | 0.0078 | 0.2703 | ok | RAN |
| ETHUSDT | 8 | `ret36_pos_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 1.2443 | 0.6047 | 1.1848 | 0.0076 | 0.2326 | ok | RAN |
| SOLUSDT | 8 | `ret36_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.5328 | 0.6161 | 2.5657 | 0.0073 | 0.2654 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret36_cross_up_0` | one_head_filter_pi_star | 30 | 2.9575 | 0.8493 | 0.4667 | -0.3771 | -0.0078 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret36_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret36_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret36_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret36_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret36_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret36_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret36_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret36_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret36_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret36_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret36_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret36_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
