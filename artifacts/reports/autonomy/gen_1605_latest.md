# Autonomy public-indicator hunt gen 1605

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T183908Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret273_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 1.1690 | 0.6000 | 0.9334 | 0.0051 | 0.1871 | ok | RAN |
| ETHUSDT | 8 | `ret273_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.0981 | 0.5932 | 0.6104 | 0.0032 | 0.2034 | ok | RAN |
| SOLUSDT | 8 | `ret273_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.1140 | 0.5759 | 0.5664 | 0.0021 | 0.1203 | ok | RAN |
| SOLUSDT | 4 | `ret273_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.0634 | 0.5697 | 0.3453 | 0.0013 | 0.1515 | ok | RAN |
| SOLUSDT | 4 | `ret273_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.0407 | 0.5543 | 0.2194 | 0.0008 | 0.1200 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret273_neg_at_h` | one_head_filter_pi_star | 204 | 16.5958 | 0.9406 | 0.5539 | -0.3782 | -0.0013 | 0.1324 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret273_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8957 | 0.5355 | -0.6196 | -0.0039 | 0.0929 | ok | RAN |
| ETHUSDT | 4 | `ret273_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8089 | 0.5371 | -1.1762 | -0.0077 | 0.0800 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret273_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret273_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret273_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret273_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret273_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret273_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret273_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret273_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret273_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret273_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret273_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret273_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret273_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret273_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret273_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret273_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
