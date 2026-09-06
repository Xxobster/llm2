# Autonomy public-indicator hunt gen 2108

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T231613Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1056_above_at_h` | one_head_filter_pi_star | 104 | 8.5484 | 1.3567 | 0.6346 | 1.3399 | 0.0058 | 0.1442 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1056_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.0528 | 0.5600 | 0.2446 | 0.0010 | 0.1200 | ok | RAN |
| ETHUSDT | 4 | `ema1056_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.0032 | 0.5652 | 0.0156 | 0.0001 | 0.1232 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1056_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9669 | 0.5437 | -0.2264 | -0.0007 | 0.1310 | ok | RAN |
| SOLUSDT | 8 | `ema1056_below_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 0.9598 | 0.5470 | -0.2649 | -0.0009 | 0.1282 | ok | RAN |
| ETHUSDT | 4 | `ema1056_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 0.9632 | 0.5446 | -0.2500 | -0.0011 | 0.1518 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1056_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 0.9045 | 0.5425 | -0.6414 | -0.0030 | 0.1698 | ok | RAN |
| ETHUSDT | 8 | `ema1056_above_at_h` | one_head_filter_pi_star | 113 | 9.3257 | 0.8825 | 0.5398 | -0.5281 | -0.0050 | 0.1239 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1056_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1056_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1056_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1056_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1056_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1056_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1056_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1056_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1056_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1056_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1056_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1056_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1056_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1056_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1056_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1056_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
