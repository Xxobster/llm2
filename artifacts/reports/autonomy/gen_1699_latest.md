# Autonomy public-indicator hunt gen 1699

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T044729Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma701_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2824 | 0.6012 | 1.5177 | 0.0078 | 0.1908 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma701_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1687 | 0.5819 | 0.9581 | 0.0050 | 0.1864 | ok | RAN |
| SOLUSDT | 4 | `sma701_above_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.0566 | 0.5298 | 0.2836 | 0.0010 | 0.1192 | ok | RAN |
| SOLUSDT | 8 | `sma701_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.0088 | 0.5354 | 0.0430 | 0.0002 | 0.1260 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma701_below_at_h` | one_head_filter_pi_star | 197 | 16.0263 | 0.9542 | 0.5635 | -0.2803 | -0.0009 | 0.1371 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma701_below_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 0.9061 | 0.5385 | -0.6024 | -0.0020 | 0.1346 | ok | RAN |
| ETHUSDT | 8 | `sma701_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.9368 | 0.5652 | -0.3231 | -0.0025 | 0.1159 | ok | RAN |
| ETHUSDT | 4 | `sma701_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.7801 | 0.5375 | -1.2801 | -0.0097 | 0.1125 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma701_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma701_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma701_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma701_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma701_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma701_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma701_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma701_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma701_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma701_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma701_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma701_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma701_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma701_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma701_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma701_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
