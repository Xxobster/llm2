# Autonomy public-indicator hunt gen 073

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T142037Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `macdh_cross_up_0` | one_head_filter_pi_star | 16 | 1.6219 | 3.7079 | 0.8125 | 2.1459 | 0.0458 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `macdh_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 1.5859 | 0.4444 | 0.7636 | 0.0412 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 8 | `macdh_cross_up_0` | one_head_filter_pi_star | 47 | 3.9822 | 2.0794 | 0.6809 | 2.2891 | 0.0212 | 0.2766 | TPM<MIN | RAN |
| ETHUSDT | 8 | `macdh_neg_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.7257 | 0.6837 | 3.4801 | 0.0199 | 0.3535 | EBR>35% | RAN |
| SOLUSDT | 4 | `macdh_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.3246 | 0.7024 | 4.3994 | 0.0191 | 0.4107 | EBR>35% | RAN |
| ETHUSDT | 4 | `macdh_neg_at_h` | one_head_filter_pi_star | 214 | 17.5014 | 1.6882 | 0.6776 | 3.3107 | 0.0187 | 0.3785 | EBR>35% | RAN |
| SOLUSDT | 8 | `macdh_neg_at_h` | one_head_filter_pi_star | 140 | 11.4479 | 2.1545 | 0.6786 | 3.6433 | 0.0173 | 0.3786 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `macdh_cross_up_0` | one_head_filter_pi_star | 18 | 1.6183 | 1.8344 | 0.6667 | 1.1417 | 0.0141 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `macdh_cross_down_0` | one_head_filter_pi_star | 17 | 1.5163 | 1.1785 | 0.5294 | 0.3322 | 0.0110 | 0.4118 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `macdh_pos_at_h` | one_head_filter_pi_star | 163 | 13.3544 | 1.2417 | 0.5706 | 1.1452 | 0.0078 | 0.2331 | ok | RAN |
| SOLUSDT | 8 | `macdh_pos_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4751 | 0.6091 | 2.3384 | 0.0073 | 0.2589 | ok | RAN |
| ETHUSDT | 4 | `macdh_pos_at_h` | one_head_filter_pi_star | 162 | 13.2725 | 1.2178 | 0.5802 | 0.9983 | 0.0068 | 0.1914 | ok | RAN |
| SOLUSDT | 8 | `macdh_cross_up_0` | one_head_filter_pi_star | 37 | 3.1671 | 1.3207 | 0.6216 | 0.7341 | 0.0053 | 0.1892 | TPM<MIN | RAN |
| SOLUSDT | 4 | `macdh_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3021 | 0.5849 | 1.7043 | 0.0046 | 0.2453 | ok | RAN |
| ETHUSDT | 8 | `macdh_cross_down_0` | one_head_filter_pi_star | 46 | 4.0355 | 1.0506 | 0.5435 | 0.1506 | 0.0022 | 0.2391 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `macdh_cross_down_0` | one_head_filter_pi_star | 38 | 3.1182 | 1.0448 | 0.5789 | 0.1109 | 0.0006 | 0.1316 | TPM<MIN | RAN |
| BTCUSDT | 4 | `macdh_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7748 | 0.3500 | -0.4429 | -0.0226 | 0.0500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `macdh_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `macdh_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `macdh_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `macdh_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `macdh_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `macdh_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `macdh_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
