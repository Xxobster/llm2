# Autonomy public-indicator hunt gen 1716

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T063349Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1004_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.0782 | 0.5620 | 0.3571 | 0.0014 | 0.1240 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1004_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 0.9885 | 0.5455 | -0.0554 | -0.0002 | 0.1322 | ok | RAN |
| ETHUSDT | 4 | `ema1004_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9903 | 0.5502 | -0.0653 | -0.0003 | 0.1528 | ok | RAN |
| SOLUSDT | 8 | `ema1004_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9620 | 0.5357 | -0.2615 | -0.0008 | 0.1270 | ok | RAN |
| SOLUSDT | 4 | `ema1004_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 0.9497 | 0.5397 | -0.3341 | -0.0011 | 0.1255 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1004_above_at_h` | one_head_filter_pi_star | 117 | 9.6172 | 0.9532 | 0.5556 | -0.2160 | -0.0021 | 0.1282 | ok | RAN |
| ETHUSDT | 8 | `ema1004_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9110 | 0.5354 | -0.6196 | -0.0029 | 0.1504 | ok | RAN |
| ETHUSDT | 4 | `ema1004_above_at_h` | one_head_filter_pi_star | 128 | 10.5627 | 0.8634 | 0.5391 | -0.6760 | -0.0061 | 0.1172 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1004_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1004_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1004_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1004_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1004_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1004_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1004_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1004_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1004_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1004_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1004_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1004_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1004_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1004_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1004_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1004_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
