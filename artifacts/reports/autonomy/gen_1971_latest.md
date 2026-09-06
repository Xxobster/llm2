# Autonomy public-indicator hunt gen 1971

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T060326Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma736_below_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2262 | 0.5890 | 1.2214 | 0.0065 | 0.1779 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma736_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.2250 | 0.5858 | 1.2314 | 0.0064 | 0.2012 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma736_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.1398 | 0.5625 | 0.6219 | 0.0026 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma736_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.0017 | 0.5396 | 0.0085 | 0.0000 | 0.1151 | ok | RAN |
| SOLUSDT | 4 | `sma736_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.9298 | 0.5606 | -0.4326 | -0.0015 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma736_below_at_h` | one_head_filter_pi_star | 196 | 15.9450 | 0.9002 | 0.5561 | -0.6254 | -0.0022 | 0.1327 | ok | RAN |
| ETHUSDT | 4 | `sma736_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 0.8571 | 0.5664 | -0.7243 | -0.0058 | 0.1119 | ok | RAN |
| ETHUSDT | 8 | `sma736_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8421 | 0.5533 | -0.8869 | -0.0065 | 0.1133 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma736_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma736_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0689 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma736_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma736_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma736_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma736_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma736_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma736_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma736_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma736_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma736_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma736_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma736_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma736_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma736_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma736_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
