# Autonomy public-indicator hunt gen 1702

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T050636Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma443_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1733 | 0.5946 | 1.0191 | 0.0052 | 0.1892 | ok | RAN |
| ETHUSDT | 4 | `wma443_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1470 | 0.6000 | 0.8582 | 0.0045 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `wma443_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0610 | 0.5698 | 0.3434 | 0.0013 | 0.1686 | ok | RAN |
| SOLUSDT | 4 | `wma443_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0593 | 0.5690 | 0.3321 | 0.0012 | 0.1552 | ok | RAN |
| SOLUSDT | 8 | `wma443_above_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.0437 | 0.5607 | 0.2397 | 0.0008 | 0.0983 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma443_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 0.9264 | 0.5263 | -0.4473 | -0.0014 | 0.1053 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma443_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8299 | 0.5319 | -1.0862 | -0.0070 | 0.0957 | ok | RAN |
| ETHUSDT | 8 | `wma443_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8317 | 0.5450 | -1.0793 | -0.0070 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma443_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma443_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma443_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma443_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma443_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma443_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma443_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma443_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma443_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma443_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma443_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma443_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma443_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma443_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma443_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma443_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
