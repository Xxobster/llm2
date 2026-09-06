# Autonomy public-indicator hunt gen 2405

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T142549Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret387_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.1699 | 0.5858 | 0.9333 | 0.0052 | 0.1775 | ok | RAN |
| ETHUSDT | 4 | `ret387_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.0948 | 0.5852 | 0.5505 | 0.0030 | 0.1705 | ok | RAN |
| SOLUSDT | 8 | `ret387_pos_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.0636 | 0.5461 | 0.3137 | 0.0012 | 0.1064 | ok | RAN |
| SOLUSDT | 4 | `ret387_pos_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.0249 | 0.5564 | 0.1204 | 0.0005 | 0.1053 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret387_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 0.9727 | 0.5754 | -0.1647 | -0.0006 | 0.1508 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret387_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 0.8995 | 0.5449 | -0.6287 | -0.0022 | 0.1517 | ok | RAN |
| ETHUSDT | 4 | `ret387_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 0.7931 | 0.5345 | -1.2587 | -0.0087 | 0.1092 | ok | RAN |
| ETHUSDT | 8 | `ret387_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.7630 | 0.5206 | -1.5329 | -0.0101 | 0.0979 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret387_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0658 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret387_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret387_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret387_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret387_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret387_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret387_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret387_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret387_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret387_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret387_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret387_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret387_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret387_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret387_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret387_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
