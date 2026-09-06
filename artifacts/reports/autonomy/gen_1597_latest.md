# Autonomy public-indicator hunt gen 1597

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T174624Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret271_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.1423 | 0.5657 | 0.7362 | 0.0026 | 0.1086 | ok | RAN |
| ETHUSDT | 4 | `ret271_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.0676 | 0.5810 | 0.4113 | 0.0022 | 0.1788 | ok | RAN |
| ETHUSDT | 8 | `ret271_neg_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.0236 | 0.5676 | 0.1529 | 0.0008 | 0.1946 | ok | RAN |
| SOLUSDT | 4 | `ret271_pos_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.0413 | 0.5429 | 0.2265 | 0.0008 | 0.1200 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret271_neg_at_h` | one_head_filter_pi_star | 148 | 12.1262 | 1.0020 | 0.5676 | 0.0108 | 0.0000 | 0.1554 | ok | RAN |
| SOLUSDT | 8 | `ret271_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 0.9476 | 0.5482 | -0.2990 | -0.0011 | 0.1446 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret271_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 0.8590 | 0.5455 | -0.8374 | -0.0055 | 0.0966 | ok | RAN |
| ETHUSDT | 8 | `ret271_pos_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.7957 | 0.5389 | -1.2584 | -0.0082 | 0.0833 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret271_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4364 | 0.3000 | -1.3199 | -0.0640 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret271_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret271_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret271_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret271_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret271_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret271_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret271_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret271_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret271_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret271_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret271_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret271_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret271_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret271_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret271_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
