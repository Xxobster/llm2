# Autonomy public-indicator hunt gen 2357

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T075951Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret380_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2038 | 0.5872 | 1.1375 | 0.0059 | 0.1686 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret380_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.1742 | 0.5890 | 0.9491 | 0.0053 | 0.1902 | ok | RAN |
| SOLUSDT | 4 | `ret380_pos_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.0832 | 0.5612 | 0.3983 | 0.0016 | 0.1079 | ok | RAN |
| SOLUSDT | 8 | `ret380_pos_at_h` | one_head_filter_pi_star | 158 | 12.8834 | 1.0295 | 0.5316 | 0.1568 | 0.0006 | 0.0949 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret380_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.9481 | 0.5600 | -0.3317 | -0.0011 | 0.1450 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret380_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9107 | 0.5436 | -0.5720 | -0.0019 | 0.1538 | ok | RAN |
| ETHUSDT | 4 | `ret380_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.8617 | 0.5440 | -0.8571 | -0.0059 | 0.1036 | ok | RAN |
| ETHUSDT | 8 | `ret380_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8406 | 0.5426 | -0.9559 | -0.0066 | 0.1011 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret380_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0713 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret380_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0713 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret380_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret380_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret380_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret380_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret380_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret380_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret380_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret380_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret380_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret380_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret380_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret380_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret380_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret380_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
