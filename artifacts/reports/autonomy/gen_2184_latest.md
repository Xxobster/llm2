# Autonomy public-indicator hunt gen 2184

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T102653Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5060_above_at_h` | one_head_filter_pi_star | 47 | 3.9475 | 2.3127 | 0.6170 | 2.0532 | 0.0147 | 0.1277 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma5060_above_at_h` | one_head_filter_pi_star | 61 | 5.1234 | 1.6590 | 0.6066 | 1.5291 | 0.0095 | 0.1148 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5060_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.0268 | 0.5625 | 0.2113 | 0.0008 | 0.1369 | ok | RAN |
| SOLUSDT | 4 | `sma5060_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.0043 | 0.5405 | 0.0330 | 0.0001 | 0.1294 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5060_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9782 | 0.5565 | -0.1751 | -0.0007 | 0.1369 | ok | RAN |
| SOLUSDT | 8 | `sma5060_below_at_h` | one_head_filter_pi_star | 296 | 24.2042 | 0.9330 | 0.5236 | -0.5116 | -0.0014 | 0.1385 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5060_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.8166 | 0.5000 | -1.0591 | -0.0099 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma5060_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.6469 | 0.4722 | -2.2985 | -0.0209 | 0.1111 | ok | RAN |
| ETHUSDT | 4 | `sma5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5060_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5060_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
