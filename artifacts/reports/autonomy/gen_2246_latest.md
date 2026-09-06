# Autonomy public-indicator hunt gen 2246

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T181212Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma528_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1204 | 0.5989 | 0.7286 | 0.0038 | 0.1925 | ok | RAN |
| ETHUSDT | 4 | `wma528_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1215 | 0.5879 | 0.7228 | 0.0038 | 0.1978 | ok | RAN |
| SOLUSDT | 8 | `wma528_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.1088 | 0.5549 | 0.5890 | 0.0019 | 0.0934 | ok | RAN |
| SOLUSDT | 4 | `wma528_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0070 | 0.5401 | 0.0413 | 0.0001 | 0.0963 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma528_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9976 | 0.5579 | -0.0143 | -0.0001 | 0.1526 | ok | RAN |
| SOLUSDT | 8 | `wma528_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9761 | 0.5538 | -0.1411 | -0.0005 | 0.1613 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma528_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 0.8034 | 0.5213 | -1.2274 | -0.0081 | 0.0904 | ok | RAN |
| ETHUSDT | 4 | `wma528_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.7899 | 0.5193 | -1.3763 | -0.0088 | 0.0994 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma528_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma528_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma528_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma528_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
