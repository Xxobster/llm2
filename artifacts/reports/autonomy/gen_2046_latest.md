# Autonomy public-indicator hunt gen 2046

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T143320Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma497_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1546 | 0.5914 | 0.9056 | 0.0046 | 0.1828 | ok | RAN |
| ETHUSDT | 4 | `wma497_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1408 | 0.5892 | 0.8495 | 0.0043 | 0.1946 | ok | RAN |
| SOLUSDT | 8 | `wma497_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.0420 | 0.5591 | 0.2488 | 0.0009 | 0.1613 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma497_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0024 | 0.5401 | 0.0141 | 0.0000 | 0.0963 | ok | RAN |
| SOLUSDT | 4 | `wma497_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 0.9926 | 0.5348 | -0.0434 | -0.0001 | 0.1070 | ok | RAN |
| SOLUSDT | 4 | `wma497_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 0.9695 | 0.5575 | -0.1805 | -0.0007 | 0.1494 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma497_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8341 | 0.5372 | -1.0615 | -0.0068 | 0.0957 | ok | RAN |
| ETHUSDT | 8 | `wma497_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8047 | 0.5401 | -1.2405 | -0.0080 | 0.0856 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma497_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma497_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma497_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma497_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma497_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma497_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma497_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma497_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma497_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma497_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma497_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma497_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma497_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma497_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma497_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma497_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
