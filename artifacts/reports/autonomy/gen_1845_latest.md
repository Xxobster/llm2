# Autonomy public-indicator hunt gen 1845

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T182820Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret307_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.2623 | 0.6025 | 1.2835 | 0.0075 | 0.1801 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret307_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.2175 | 0.6082 | 1.2111 | 0.0065 | 0.1871 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret307_pos_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.1356 | 0.5513 | 0.6667 | 0.0026 | 0.1090 | ok | RAN |
| SOLUSDT | 4 | `ret307_pos_at_h` | one_head_filter_pi_star | 170 | 13.9408 | 1.1043 | 0.5471 | 0.5581 | 0.0020 | 0.1118 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret307_neg_at_h` | one_head_filter_pi_star | 167 | 13.7461 | 0.9744 | 0.5569 | -0.1468 | -0.0005 | 0.1557 | ok | RAN |
| SOLUSDT | 4 | `ret307_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.9629 | 0.5648 | -0.2274 | -0.0008 | 0.1451 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret307_pos_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.9028 | 0.5625 | -0.5258 | -0.0038 | 0.0875 | ok | RAN |
| ETHUSDT | 8 | `ret307_pos_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.8897 | 0.5613 | -0.6090 | -0.0042 | 0.0903 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret307_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret307_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0742 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret307_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret307_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret307_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret307_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret307_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret307_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret307_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret307_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret307_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret307_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret307_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret307_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret307_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret307_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
