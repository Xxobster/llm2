# Autonomy public-indicator hunt gen 1579

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T154458Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma685_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1455 | 0.5792 | 0.8431 | 0.0045 | 0.1858 | ok | RAN |
| ETHUSDT | 4 | `sma685_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1274 | 0.5810 | 0.7556 | 0.0038 | 0.1955 | ok | RAN |
| SOLUSDT | 4 | `sma685_above_at_h` | one_head_filter_pi_star | 159 | 13.0388 | 1.0693 | 0.5472 | 0.3652 | 0.0013 | 0.1195 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma685_above_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 0.9197 | 0.5082 | -0.3898 | -0.0016 | 0.1311 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma685_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 0.9537 | 0.5724 | -0.2327 | -0.0018 | 0.1103 | ok | RAN |
| SOLUSDT | 4 | `sma685_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.8563 | 0.5436 | -0.9232 | -0.0031 | 0.1436 | ok | RAN |
| SOLUSDT | 8 | `sma685_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 0.8521 | 0.5464 | -0.9557 | -0.0033 | 0.1392 | ok | RAN |
| ETHUSDT | 8 | `sma685_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8787 | 0.5535 | -0.6813 | -0.0048 | 0.1069 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma685_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma685_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma685_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma685_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
