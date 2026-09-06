# Autonomy public-indicator hunt gen 1838

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T175129Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma464_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1746 | 0.6044 | 1.0076 | 0.0053 | 0.1978 | ok | RAN |
| ETHUSDT | 4 | `wma464_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1170 | 0.5820 | 0.7147 | 0.0036 | 0.2011 | ok | RAN |
| SOLUSDT | 4 | `wma464_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0476 | 0.5574 | 0.2716 | 0.0010 | 0.1585 | ok | RAN |
| SOLUSDT | 8 | `wma464_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0171 | 0.5430 | 0.0988 | 0.0003 | 0.0968 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma464_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9955 | 0.5549 | -0.0262 | -0.0001 | 0.1561 | ok | RAN |
| SOLUSDT | 4 | `wma464_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 0.9639 | 0.5408 | -0.2170 | -0.0007 | 0.0969 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma464_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8341 | 0.5455 | -1.0474 | -0.0069 | 0.0963 | ok | RAN |
| ETHUSDT | 4 | `wma464_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8112 | 0.5351 | -1.2222 | -0.0077 | 0.0973 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma464_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma464_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma464_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma464_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma464_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma464_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma464_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma464_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma464_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma464_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma464_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma464_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma464_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma464_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma464_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma464_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
