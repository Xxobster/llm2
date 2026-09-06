# Autonomy public-indicator hunt gen 373

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T200400Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret41_neg_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.7886 | 0.6798 | 3.7533 | 0.0211 | 0.3645 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret41_cross_up_0` | one_head_filter_pi_star | 39 | 3.2496 | 2.0781 | 0.5641 | 1.8257 | 0.0168 | 0.2564 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret41_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.5769 | 0.6531 | 2.9771 | 0.0164 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret41_neg_at_h` | one_head_filter_pi_star | 157 | 12.8380 | 2.0399 | 0.6879 | 3.6856 | 0.0163 | 0.4076 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret41_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.9245 | 0.6627 | 3.4803 | 0.0155 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret41_cross_down_0` | one_head_filter_pi_star | 40 | 3.3146 | 1.2566 | 0.5000 | 0.5799 | 0.0102 | 0.1500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret41_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2644 | 0.6105 | 1.2623 | 0.0083 | 0.2326 | ok | RAN |
| SOLUSDT | 4 | `ret41_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.5149 | 0.6140 | 2.5658 | 0.0072 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `ret41_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.5115 | 0.6209 | 2.5911 | 0.0072 | 0.2464 | ok | RAN |
| ETHUSDT | 4 | `ret41_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1926 | 0.5902 | 0.9788 | 0.0063 | 0.2240 | ok | RAN |
| SOLUSDT | 8 | `ret41_cross_down_0` | one_head_filter_pi_star | 38 | 3.2433 | 1.1339 | 0.5000 | 0.2994 | 0.0028 | 0.1579 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret41_cross_up_0` | one_head_filter_pi_star | 37 | 3.2204 | 0.9461 | 0.4865 | -0.1476 | -0.0022 | 0.1622 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret41_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret41_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret41_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret41_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret41_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret41_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret41_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret41_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret41_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret41_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret41_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret41_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
