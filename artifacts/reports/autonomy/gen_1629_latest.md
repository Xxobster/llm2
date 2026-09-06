# Autonomy public-indicator hunt gen 1629

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T205023Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret276_neg_at_h` | one_head_filter_pi_star | 141 | 11.5184 | 1.1810 | 0.6028 | 0.9606 | 0.0053 | 0.1915 | ok | RAN |
| ETHUSDT | 8 | `ret276_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1174 | 0.5847 | 0.7177 | 0.0036 | 0.1858 | ok | RAN |
| SOLUSDT | 4 | `ret276_neg_at_h` | one_head_filter_pi_star | 152 | 12.4292 | 1.1215 | 0.5855 | 0.6453 | 0.0026 | 0.1447 | ok | RAN |
| SOLUSDT | 8 | `ret276_pos_at_h` | one_head_filter_pi_star | 181 | 14.8429 | 1.1249 | 0.5525 | 0.6662 | 0.0022 | 0.1050 | ok | RAN |
| SOLUSDT | 4 | `ret276_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.0972 | 0.5593 | 0.5082 | 0.0017 | 0.0960 | ok | RAN |
| SOLUSDT | 8 | `ret276_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0079 | 0.5549 | 0.0432 | 0.0002 | 0.1445 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret276_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8287 | 0.5440 | -1.0454 | -0.0068 | 0.0879 | ok | RAN |
| ETHUSDT | 4 | `ret276_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.8273 | 0.5380 | -1.0751 | -0.0069 | 0.0924 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret276_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0659 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret276_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret276_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret276_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret276_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret276_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret276_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret276_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret276_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret276_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret276_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret276_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret276_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret276_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret276_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret276_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
