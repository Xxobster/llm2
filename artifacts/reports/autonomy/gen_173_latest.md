# Autonomy public-indicator hunt gen 173

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T205026Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret28_cross_up_0` | one_head_filter_pi_star | 24 | 2.0397 | 4.2754 | 0.7083 | 2.7045 | 0.0599 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret28_cross_down_0` | one_head_filter_pi_star | 45 | 3.7187 | 2.1524 | 0.6222 | 2.0538 | 0.0246 | 0.2889 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret28_cross_down_0` | one_head_filter_pi_star | 25 | 2.0557 | 4.3362 | 0.7600 | 2.5503 | 0.0230 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret28_neg_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8257 | 0.6731 | 3.9725 | 0.0213 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret28_neg_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.7976 | 0.6667 | 3.7040 | 0.0199 | 0.3824 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret28_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.0331 | 0.6766 | 3.8109 | 0.0165 | 0.3892 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret28_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.0594 | 0.6845 | 3.8524 | 0.0162 | 0.4048 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret28_cross_up_0` | one_head_filter_pi_star | 15 | 1.7179 | 1.7821 | 0.5333 | 1.0935 | 0.0150 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret28_pos_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.2183 | 0.6023 | 1.0691 | 0.0071 | 0.1930 | ok | RAN |
| ETHUSDT | 4 | `ret28_pos_at_h` | one_head_filter_pi_star | 170 | 14.0286 | 1.2177 | 0.5941 | 1.0491 | 0.0068 | 0.2059 | ok | RAN |
| SOLUSDT | 8 | `ret28_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4030 | 0.6000 | 2.0645 | 0.0059 | 0.2571 | ok | RAN |
| SOLUSDT | 4 | `ret28_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3798 | 0.6019 | 1.9752 | 0.0056 | 0.2559 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret28_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret28_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret28_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret28_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret28_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret28_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret28_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret28_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret28_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret28_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret28_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret28_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
