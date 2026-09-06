# Autonomy public-indicator hunt gen 914

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T025812Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret768_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 2.2688 | 0.7278 | 4.4063 | 0.0246 | 0.3987 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret768_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.9977 | 0.6868 | 4.0102 | 0.0208 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret768_neg_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.8461 | 0.6619 | 3.5987 | 0.0141 | 0.3381 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret768_neg_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.7924 | 0.6517 | 3.3377 | 0.0135 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret768_pos_at_h` | one_head_filter_pi_star | 71 | 5.7894 | 1.6080 | 0.6338 | 1.6694 | 0.0081 | 0.2535 | ok | RAN |
| SOLUSDT | 8 | `ret768_pos_at_h` | one_head_filter_pi_star | 91 | 7.4202 | 1.5483 | 0.6484 | 1.7528 | 0.0078 | 0.2747 | ok | RAN |
| ETHUSDT | 4 | `ret768_pos_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 1.1040 | 0.5639 | 0.4599 | 0.0046 | 0.2481 | ok | RAN |
| ETHUSDT | 8 | `ret768_pos_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 1.0895 | 0.5586 | 0.3642 | 0.0037 | 0.1982 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret768_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4745 | 0.2941 | -1.1358 | -0.0518 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret768_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4684 | 0.2500 | -1.1492 | -0.0600 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret768_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret768_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret768_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret768_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret768_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret768_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret768_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret768_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret768_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret768_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret768_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret768_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret768_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret768_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
