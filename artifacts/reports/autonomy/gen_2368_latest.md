# Autonomy public-indicator hunt gen 2368

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T093145Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5520_above_at_h` | one_head_filter_pi_star | 46 | 4.3190 | 2.6561 | 0.6522 | 2.5460 | 0.0200 | 0.1087 | ok | RAN |
| SOLUSDT | 8 | `sma5520_above_at_h` | one_head_filter_pi_star | 43 | 4.0373 | 2.2987 | 0.6744 | 2.1496 | 0.0180 | 0.0930 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5520_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.0014 | 0.5630 | 0.0116 | 0.0000 | 0.1320 | ok | RAN |
| ETHUSDT | 8 | `sma5520_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9900 | 0.5592 | -0.0807 | -0.0003 | 0.1361 | ok | RAN |
| SOLUSDT | 8 | `sma5520_below_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 0.9691 | 0.5352 | -0.2421 | -0.0006 | 0.1254 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma5520_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 0.9223 | 0.5179 | -0.6053 | -0.0017 | 0.1336 | ok | RAN |
| ETHUSDT | 4 | `sma5520_above_at_h` | one_head_filter_pi_star | 33 | 9.9583 | 0.9030 | 0.5152 | -0.4692 | -0.0047 | 0.1818 | ok | RAN |
| ETHUSDT | 8 | `sma5520_above_at_h` | one_head_filter_pi_star | 33 | 9.9583 | 0.7943 | 0.4848 | -1.0138 | -0.0111 | 0.1818 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5520_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5520_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
