# Autonomy public-indicator hunt gen 1635

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T212350Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma692_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.1539 | 0.5814 | 0.8729 | 0.0045 | 0.1977 | ok | RAN |
| ETHUSDT | 8 | `sma692_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1266 | 0.5758 | 0.7200 | 0.0038 | 0.1939 | ok | RAN |
| SOLUSDT | 4 | `sma692_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 1.1321 | 0.5508 | 0.5811 | 0.0025 | 0.1271 | ok | RAN |
| SOLUSDT | 8 | `sma692_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.0903 | 0.5528 | 0.4131 | 0.0017 | 0.1220 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma692_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9904 | 0.5631 | -0.0603 | -0.0002 | 0.1359 | ok | RAN |
| SOLUSDT | 4 | `sma692_below_at_h` | one_head_filter_pi_star | 202 | 16.4331 | 0.9863 | 0.5594 | -0.0826 | -0.0003 | 0.1337 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma692_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 0.9349 | 0.5762 | -0.3490 | -0.0026 | 0.1192 | ok | RAN |
| ETHUSDT | 4 | `sma692_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 0.9108 | 0.5672 | -0.4476 | -0.0036 | 0.1119 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma692_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma692_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma692_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma692_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma692_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma692_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma692_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma692_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma692_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma692_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma692_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma692_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma692_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma692_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma692_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma692_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
