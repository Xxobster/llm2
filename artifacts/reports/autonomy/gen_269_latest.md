# Autonomy public-indicator hunt gen 269

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T031653Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret21_cross_down_0` | one_head_filter_pi_star | 12 | 1.0198 | 7.2544 | 0.6667 | 2.2190 | 0.0483 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret21_cross_up_0` | one_head_filter_pi_star | 29 | 2.4751 | 2.7335 | 0.6552 | 2.0498 | 0.0236 | 0.1379 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret21_neg_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.8521 | 0.6743 | 4.0680 | 0.0215 | 0.3899 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret21_neg_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8141 | 0.6773 | 3.8818 | 0.0208 | 0.3682 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret21_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2770 | 0.6951 | 4.2622 | 0.0185 | 0.4146 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret21_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.2242 | 0.7037 | 4.1515 | 0.0185 | 0.4259 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret21_cross_up_0` | one_head_filter_pi_star | 29 | 2.3863 | 1.4299 | 0.5172 | 0.7917 | 0.0138 | 0.2414 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret21_cross_down_0` | one_head_filter_pi_star | 39 | 3.2916 | 1.6442 | 0.6410 | 1.2537 | 0.0123 | 0.1282 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret21_cross_down_0` | one_head_filter_pi_star | 55 | 4.5407 | 1.2465 | 0.5636 | 0.6973 | 0.0103 | 0.1818 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret21_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2234 | 0.6049 | 1.0672 | 0.0070 | 0.1790 | ok | RAN |
| ETHUSDT | 8 | `ret21_pos_at_h` | one_head_filter_pi_star | 154 | 12.7083 | 1.2159 | 0.5974 | 0.9993 | 0.0068 | 0.2078 | ok | RAN |
| SOLUSDT | 8 | `ret21_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.4172 | 0.5991 | 2.2163 | 0.0060 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `ret21_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.4062 | 0.5991 | 2.1546 | 0.0059 | 0.2406 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret21_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret21_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret21_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret21_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret21_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret21_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret21_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret21_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret21_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret21_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret21_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
