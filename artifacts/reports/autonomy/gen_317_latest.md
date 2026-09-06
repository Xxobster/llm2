# Autonomy public-indicator hunt gen 317

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T064214Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret31_cross_up_0` | one_head_filter_pi_star | 18 | 1.8669 | 2.5543 | 0.6111 | 1.7592 | 0.0217 | 0.2778 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret31_neg_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.7364 | 0.6667 | 3.6578 | 0.0201 | 0.3568 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret31_neg_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7637 | 0.6651 | 3.7458 | 0.0200 | 0.3732 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret31_cross_down_0` | one_head_filter_pi_star | 22 | 1.8116 | 2.9166 | 0.6818 | 1.7593 | 0.0180 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret31_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.0405 | 0.6748 | 3.8047 | 0.0163 | 0.4110 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret31_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0276 | 0.6807 | 3.7519 | 0.0161 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret31_cross_down_0` | one_head_filter_pi_star | 44 | 3.6326 | 1.4545 | 0.5682 | 1.0532 | 0.0151 | 0.2273 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret31_pos_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.2884 | 0.6131 | 1.3574 | 0.0086 | 0.2321 | ok | RAN |
| SOLUSDT | 8 | `ret31_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.4529 | 0.6047 | 2.3238 | 0.0067 | 0.2512 | ok | RAN |
| SOLUSDT | 4 | `ret31_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4618 | 0.6095 | 2.3170 | 0.0066 | 0.2571 | ok | RAN |
| ETHUSDT | 8 | `ret31_pos_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.1952 | 0.5904 | 0.9508 | 0.0062 | 0.2108 | ok | RAN |
| ETHUSDT | 8 | `ret31_cross_up_0` | one_head_filter_pi_star | 32 | 2.6779 | 1.0625 | 0.5312 | 0.1559 | 0.0035 | 0.1875 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret31_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret31_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret31_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret31_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret31_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret31_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret31_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret31_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret31_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret31_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret31_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret31_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
