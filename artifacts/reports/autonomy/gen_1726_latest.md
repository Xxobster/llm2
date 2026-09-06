# Autonomy public-indicator hunt gen 1726

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T073411Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma447_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.1624 | 0.5947 | 0.9679 | 0.0049 | 0.1947 | ok | RAN |
| ETHUSDT | 4 | `wma447_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1271 | 0.5914 | 0.7748 | 0.0040 | 0.1935 | ok | RAN |
| SOLUSDT | 8 | `wma447_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0999 | 0.5756 | 0.5506 | 0.0020 | 0.1628 | ok | RAN |
| SOLUSDT | 8 | `wma447_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.0415 | 0.5480 | 0.2326 | 0.0007 | 0.1017 | ok | RAN |
| SOLUSDT | 4 | `wma447_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.0215 | 0.5655 | 0.1173 | 0.0005 | 0.1548 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma447_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 0.9919 | 0.5376 | -0.0474 | -0.0002 | 0.1075 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma447_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8457 | 0.5372 | -0.9663 | -0.0061 | 0.0957 | ok | RAN |
| ETHUSDT | 8 | `wma447_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8015 | 0.5319 | -1.2774 | -0.0082 | 0.0957 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma447_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma447_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0722 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma447_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma447_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma447_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma447_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma447_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma447_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma447_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma447_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma447_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma447_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma447_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma447_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma447_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma447_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
