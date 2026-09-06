# Autonomy public-indicator hunt gen 2243

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T175059Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma772_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2378 | 0.5943 | 1.2791 | 0.0065 | 0.1829 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma772_above_at_h` | one_head_filter_pi_star | 111 | 9.1025 | 1.2802 | 0.5946 | 1.1256 | 0.0048 | 0.1171 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma772_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1083 | 0.5784 | 0.6351 | 0.0031 | 0.1730 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma772_above_at_h` | one_head_filter_pi_star | 125 | 10.2506 | 0.9629 | 0.5280 | -0.1811 | -0.0007 | 0.1120 | ok | RAN |
| SOLUSDT | 8 | `sma772_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.9542 | 0.5606 | -0.2817 | -0.0010 | 0.1364 | ok | RAN |
| SOLUSDT | 4 | `sma772_below_at_h` | one_head_filter_pi_star | 219 | 17.9078 | 0.9448 | 0.5479 | -0.3555 | -0.0012 | 0.1370 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma772_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 0.8568 | 0.5556 | -0.7626 | -0.0058 | 0.1046 | ok | RAN |
| ETHUSDT | 8 | `sma772_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8383 | 0.5479 | -0.8536 | -0.0068 | 0.1164 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma772_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma772_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma772_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma772_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma772_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma772_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma772_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma772_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma772_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma772_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma772_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma772_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma772_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma772_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma772_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma772_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
