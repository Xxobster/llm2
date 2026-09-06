# Autonomy public-indicator hunt gen 1902

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T233603Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma474_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1735 | 0.5989 | 0.9970 | 0.0053 | 0.1923 | ok | RAN |
| ETHUSDT | 4 | `wma474_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1627 | 0.5978 | 0.9529 | 0.0050 | 0.1957 | ok | RAN |
| SOLUSDT | 4 | `wma474_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.0731 | 0.5731 | 0.4076 | 0.0015 | 0.1579 | ok | RAN |
| SOLUSDT | 4 | `wma474_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0718 | 0.5503 | 0.4101 | 0.0013 | 0.1005 | ok | RAN |
| SOLUSDT | 8 | `wma474_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0276 | 0.5604 | 0.1589 | 0.0006 | 0.1593 | ok | RAN |
| SOLUSDT | 8 | `wma474_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0314 | 0.5508 | 0.1784 | 0.0006 | 0.0963 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma474_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8572 | 0.5470 | -0.8757 | -0.0057 | 0.0939 | ok | RAN |
| ETHUSDT | 4 | `wma474_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8338 | 0.5344 | -1.0428 | -0.0068 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma474_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma474_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma474_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma474_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma474_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma474_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma474_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma474_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma474_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma474_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma474_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma474_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma474_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma474_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma474_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma474_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
