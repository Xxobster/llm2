# Autonomy public-indicator hunt gen 1998

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T085903Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma489_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1270 | 0.5914 | 0.7705 | 0.0040 | 0.1989 | ok | RAN |
| ETHUSDT | 8 | `wma489_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1160 | 0.5879 | 0.6945 | 0.0037 | 0.1868 | ok | RAN |
| SOLUSDT | 4 | `wma489_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.0479 | 0.5618 | 0.2778 | 0.0010 | 0.1573 | ok | RAN |
| SOLUSDT | 8 | `wma489_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0403 | 0.5410 | 0.2287 | 0.0007 | 0.0929 | ok | RAN |
| SOLUSDT | 4 | `wma489_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.0080 | 0.5408 | 0.0480 | 0.0002 | 0.0969 | ok | RAN |
| SOLUSDT | 8 | `wma489_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0061 | 0.5611 | 0.0360 | 0.0001 | 0.1611 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma489_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7992 | 0.5291 | -1.2981 | -0.0083 | 0.0952 | ok | RAN |
| ETHUSDT | 8 | `wma489_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.7948 | 0.5372 | -1.3046 | -0.0085 | 0.0904 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma489_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0461 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma489_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma489_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma489_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma489_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma489_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma489_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma489_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma489_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma489_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma489_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma489_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma489_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma489_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma489_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma489_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
