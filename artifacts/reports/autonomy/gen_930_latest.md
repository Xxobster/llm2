# Autonomy public-indicator hunt gen 930

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T044640Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret784_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.1798 | 0.7097 | 4.4091 | 0.0242 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret784_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1598 | 0.7074 | 4.4635 | 0.0235 | 0.3723 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret784_neg_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.9064 | 0.6683 | 3.8316 | 0.0146 | 0.3365 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret784_neg_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8803 | 0.6566 | 3.5768 | 0.0142 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret784_pos_at_h` | one_head_filter_pi_star | 58 | 4.7293 | 1.8952 | 0.6552 | 1.8872 | 0.0109 | 0.2414 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret784_pos_at_h` | one_head_filter_pi_star | 49 | 3.9955 | 1.6050 | 0.6531 | 1.3593 | 0.0084 | 0.2449 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret784_pos_at_h` | one_head_filter_pi_star | 124 | 10.1926 | 1.1270 | 0.5645 | 0.5787 | 0.0054 | 0.2500 | ok | RAN |
| ETHUSDT | 8 | `ret784_pos_at_h` | one_head_filter_pi_star | 104 | 8.5830 | 1.0791 | 0.5769 | 0.3397 | 0.0033 | 0.2212 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret784_pos_at_h` | one_head_filter_pi_star | 12 | 1.0212 | 0.4536 | 0.2500 | -1.0266 | -0.0457 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret784_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3148 | 0.2353 | -1.5963 | -0.0677 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret784_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret784_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret784_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret784_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret784_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret784_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret784_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret784_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret784_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret784_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret784_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret784_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret784_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret784_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
