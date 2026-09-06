# Autonomy public-indicator hunt gen 2270

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T210505Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma532_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1492 | 0.6000 | 0.8618 | 0.0045 | 0.1833 | ok | RAN |
| ETHUSDT | 4 | `wma532_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.0805 | 0.5820 | 0.4984 | 0.0026 | 0.1852 | ok | RAN |
| SOLUSDT | 8 | `wma532_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.1299 | 0.5598 | 0.6999 | 0.0023 | 0.0978 | ok | RAN |
| SOLUSDT | 4 | `wma532_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0728 | 0.5484 | 0.4128 | 0.0013 | 0.1022 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma532_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 0.9821 | 0.5525 | -0.1042 | -0.0004 | 0.1492 | ok | RAN |
| SOLUSDT | 8 | `wma532_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 0.9802 | 0.5543 | -0.1196 | -0.0004 | 0.1630 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma532_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8303 | 0.5263 | -1.0829 | -0.0070 | 0.0947 | ok | RAN |
| ETHUSDT | 8 | `wma532_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8171 | 0.5348 | -1.1731 | -0.0075 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma532_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma532_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma532_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma532_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma532_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma532_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma532_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma532_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma532_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma532_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma532_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma532_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma532_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma532_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma532_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma532_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
