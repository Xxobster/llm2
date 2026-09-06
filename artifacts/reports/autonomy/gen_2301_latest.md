# Autonomy public-indicator hunt gen 2301

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T004818Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret372_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2557 | 0.5928 | 1.3508 | 0.0075 | 0.1916 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret372_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 1.1740 | 0.5948 | 0.9145 | 0.0054 | 0.2026 | ok | RAN |
| SOLUSDT | 8 | `ret372_neg_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.0132 | 0.5714 | 0.0828 | 0.0003 | 0.1478 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret372_pos_at_h` | one_head_filter_pi_star | 154 | 12.5572 | 1.0001 | 0.5260 | 0.0007 | 0.0000 | 0.1169 | ok | RAN |
| SOLUSDT | 4 | `ret372_pos_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 0.9894 | 0.5310 | -0.0556 | -0.0002 | 0.1034 | ok | RAN |
| SOLUSDT | 4 | `ret372_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 0.9319 | 0.5549 | -0.4169 | -0.0015 | 0.1484 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret372_pos_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 0.8251 | 0.5323 | -1.1310 | -0.0073 | 0.1095 | ok | RAN |
| ETHUSDT | 8 | `ret372_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8023 | 0.5316 | -1.2146 | -0.0085 | 0.1053 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret372_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6493 | 0.2632 | -0.7123 | -0.0353 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret372_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0613 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret372_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret372_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret372_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret372_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret372_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret372_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret372_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret372_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret372_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret372_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret372_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret372_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret372_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret372_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
