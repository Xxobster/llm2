# Autonomy public-indicator hunt gen 1589

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T165202Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret270_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2088 | 0.6012 | 1.1726 | 0.0063 | 0.1902 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret270_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 1.1176 | 0.5823 | 0.6703 | 0.0036 | 0.1772 | ok | RAN |
| SOLUSDT | 8 | `ret270_pos_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.1048 | 0.5611 | 0.5537 | 0.0019 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `ret270_pos_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.0727 | 0.5419 | 0.3976 | 0.0014 | 0.1061 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret270_neg_at_h` | one_head_filter_pi_star | 151 | 12.3474 | 1.0006 | 0.5695 | 0.0035 | 0.0000 | 0.1457 | ok | RAN |
| SOLUSDT | 8 | `ret270_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 0.9997 | 0.5600 | -0.0018 | -0.0000 | 0.1543 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret270_pos_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.8860 | 0.5515 | -0.6653 | -0.0043 | 0.0848 | ok | RAN |
| ETHUSDT | 4 | `ret270_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8655 | 0.5455 | -0.7954 | -0.0052 | 0.0802 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret270_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4364 | 0.3000 | -1.3199 | -0.0664 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret270_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret270_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret270_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret270_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret270_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret270_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret270_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret270_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret270_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret270_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret270_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret270_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret270_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret270_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret270_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
