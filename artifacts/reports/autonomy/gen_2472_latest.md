# Autonomy public-indicator hunt gen 2472

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T220942Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5780_above_at_h` | one_head_filter_pi_star | 37 | 3.4740 | 2.8467 | 0.6757 | 2.3479 | 0.0210 | 0.1081 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma5780_above_at_h` | one_head_filter_pi_star | 45 | 4.2251 | 1.8038 | 0.6222 | 1.5564 | 0.0111 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5780_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9871 | 0.5588 | -0.1031 | -0.0004 | 0.1382 | ok | RAN |
| ETHUSDT | 8 | `sma5780_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9828 | 0.5579 | -0.1413 | -0.0006 | 0.1365 | ok | RAN |
| SOLUSDT | 4 | `sma5780_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9547 | 0.5339 | -0.3671 | -0.0009 | 0.1239 | ok | RAN |
| SOLUSDT | 8 | `sma5780_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9456 | 0.5341 | -0.4402 | -0.0011 | 0.1246 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5780_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.8031 | 0.5000 | -1.1629 | -0.0098 | 0.1389 | ok | RAN |
| ETHUSDT | 4 | `sma5780_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.7944 | 0.5000 | -1.0554 | -0.0103 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5780_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5780_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
