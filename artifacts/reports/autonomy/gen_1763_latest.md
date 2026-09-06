# Autonomy public-indicator hunt gen 1763

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T105804Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma709_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.2316 | 0.5848 | 1.2381 | 0.0067 | 0.1871 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma709_above_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.2630 | 0.5812 | 1.0599 | 0.0045 | 0.1368 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma709_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1104 | 0.5655 | 0.6369 | 0.0033 | 0.1964 | ok | RAN |
| SOLUSDT | 4 | `sma709_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.1022 | 0.5484 | 0.4595 | 0.0019 | 0.1210 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma709_below_at_h` | one_head_filter_pi_star | 203 | 16.5144 | 0.9500 | 0.5517 | -0.3088 | -0.0010 | 0.1281 | ok | RAN |
| SOLUSDT | 8 | `sma709_below_at_h` | one_head_filter_pi_star | 213 | 17.3280 | 0.9405 | 0.5446 | -0.3776 | -0.0012 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma709_above_at_h` | one_head_filter_pi_star | 129 | 10.6036 | 0.9445 | 0.5659 | -0.2613 | -0.0022 | 0.1163 | ok | RAN |
| ETHUSDT | 8 | `sma709_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 0.8751 | 0.5503 | -0.6801 | -0.0051 | 0.1074 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma709_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma709_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma709_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma709_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma709_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma709_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma709_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma709_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma709_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma709_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma709_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma709_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma709_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma709_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma709_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma709_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
