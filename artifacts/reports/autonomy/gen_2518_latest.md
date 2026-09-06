# Autonomy public-indicator hunt gen 2518

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T030213Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma571_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.2076 | 0.6034 | 1.1843 | 0.0061 | 0.1899 | GATE_CAND | RAN |
| ETHUSDT | 4 | `wma571_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1668 | 0.5899 | 0.9768 | 0.0050 | 0.1910 | ok | RAN |
| SOLUSDT | 4 | `wma571_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.1493 | 0.5549 | 0.8121 | 0.0027 | 0.1099 | ok | RAN |
| SOLUSDT | 8 | `wma571_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0638 | 0.5426 | 0.3652 | 0.0012 | 0.0957 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma571_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 0.9933 | 0.5580 | -0.0404 | -0.0001 | 0.1547 | ok | RAN |
| SOLUSDT | 8 | `wma571_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.9837 | 0.5561 | -0.1012 | -0.0003 | 0.1582 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma571_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8503 | 0.5330 | -0.9296 | -0.0060 | 0.1044 | ok | RAN |
| ETHUSDT | 4 | `wma571_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.8266 | 0.5337 | -1.1183 | -0.0072 | 0.0984 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma571_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma571_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma571_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma571_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma571_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma571_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma571_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma571_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma571_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma571_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma571_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma571_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma571_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma571_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma571_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma571_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
