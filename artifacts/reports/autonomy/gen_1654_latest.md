# Autonomy public-indicator hunt gen 1654

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T233333Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma436_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1370 | 0.5873 | 0.8253 | 0.0042 | 0.1958 | ok | RAN |
| ETHUSDT | 4 | `wma436_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1233 | 0.5957 | 0.7585 | 0.0038 | 0.1862 | ok | RAN |
| SOLUSDT | 4 | `wma436_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0639 | 0.5723 | 0.3472 | 0.0013 | 0.1618 | ok | RAN |
| SOLUSDT | 8 | `wma436_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0554 | 0.5640 | 0.3045 | 0.0011 | 0.1628 | ok | RAN |
| SOLUSDT | 8 | `wma436_above_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.0451 | 0.5460 | 0.2511 | 0.0008 | 0.1034 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma436_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 0.9473 | 0.5266 | -0.3161 | -0.0010 | 0.1064 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma436_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8534 | 0.5405 | -0.9028 | -0.0058 | 0.0973 | ok | RAN |
| ETHUSDT | 4 | `wma436_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8375 | 0.5355 | -1.0175 | -0.0065 | 0.0984 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma436_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma436_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma436_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma436_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
