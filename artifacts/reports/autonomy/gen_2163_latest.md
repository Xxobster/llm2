# Autonomy public-indicator hunt gen 2163

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T070512Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma762_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1128 | 0.5730 | 0.6649 | 0.0033 | 0.1838 | ok | RAN |
| SOLUSDT | 4 | `sma762_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.1485 | 0.5606 | 0.6698 | 0.0027 | 0.1288 | ok | RAN |
| ETHUSDT | 4 | `sma762_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.0746 | 0.5714 | 0.4589 | 0.0023 | 0.1958 | ok | RAN |
| SOLUSDT | 8 | `sma762_above_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.0947 | 0.5492 | 0.4227 | 0.0017 | 0.1230 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma762_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.9851 | 0.5725 | -0.0719 | -0.0006 | 0.1232 | ok | RAN |
| SOLUSDT | 4 | `sma762_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.9399 | 0.5505 | -0.3723 | -0.0013 | 0.1414 | ok | RAN |
| SOLUSDT | 8 | `sma762_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.9330 | 0.5476 | -0.4279 | -0.0015 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma762_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.8106 | 0.5541 | -1.0346 | -0.0081 | 0.1081 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma762_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma762_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma762_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma762_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma762_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma762_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma762_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma762_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma762_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma762_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma762_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma762_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma762_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma762_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma762_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma762_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
