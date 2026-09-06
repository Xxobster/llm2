# Autonomy public-indicator hunt gen 2126

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T012649Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma509_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1668 | 0.5956 | 0.9709 | 0.0050 | 0.1858 | ok | RAN |
| ETHUSDT | 4 | `wma509_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1470 | 0.5979 | 0.8834 | 0.0045 | 0.1958 | ok | RAN |
| SOLUSDT | 8 | `wma509_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.0982 | 0.5537 | 0.5291 | 0.0017 | 0.0960 | ok | RAN |
| SOLUSDT | 8 | `wma509_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0689 | 0.5706 | 0.3925 | 0.0014 | 0.1582 | ok | RAN |
| SOLUSDT | 4 | `wma509_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 1.0479 | 0.5795 | 0.2751 | 0.0010 | 0.1534 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma509_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 0.9620 | 0.5263 | -0.2275 | -0.0007 | 0.1053 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma509_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 0.8124 | 0.5323 | -1.2025 | -0.0077 | 0.0914 | ok | RAN |
| ETHUSDT | 4 | `wma509_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 0.7767 | 0.5220 | -1.4359 | -0.0094 | 0.0934 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma509_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma509_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma509_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma509_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma509_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma509_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma509_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma509_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma509_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma509_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma509_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma509_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma509_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma509_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma509_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma509_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
