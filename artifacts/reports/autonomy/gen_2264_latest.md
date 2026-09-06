# Autonomy public-indicator hunt gen 2264

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T202121Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5260_above_at_h` | one_head_filter_pi_star | 48 | 4.5068 | 2.4555 | 0.6667 | 2.2980 | 0.0172 | 0.1042 | ok | RAN |
| SOLUSDT | 4 | `sma5260_above_at_h` | one_head_filter_pi_star | 46 | 3.9170 | 2.3968 | 0.6522 | 2.1603 | 0.0171 | 0.1304 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma5260_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 1.0733 | 0.5484 | 0.3117 | 0.0032 | 0.1290 | ok | RAN |
| ETHUSDT | 4 | `sma5260_above_at_h` | one_head_filter_pi_star | 28 | 8.2617 | 1.0263 | 0.5357 | 0.1086 | 0.0011 | 0.1429 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5260_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9911 | 0.5588 | -0.0707 | -0.0003 | 0.1324 | ok | RAN |
| SOLUSDT | 4 | `sma5260_below_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 0.9527 | 0.5348 | -0.3683 | -0.0010 | 0.1297 | ok | RAN |
| ETHUSDT | 8 | `sma5260_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9654 | 0.5572 | -0.2846 | -0.0011 | 0.1349 | ok | RAN |
| SOLUSDT | 8 | `sma5260_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 0.9361 | 0.5273 | -0.4923 | -0.0013 | 0.1254 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5260_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5260_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
