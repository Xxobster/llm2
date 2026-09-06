# Autonomy public-indicator hunt gen 2068

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T175418Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1051_above_at_h` | one_head_filter_pi_star | 107 | 8.7248 | 1.2991 | 0.6168 | 1.1199 | 0.0048 | 0.1402 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1051_above_at_h` | one_head_filter_pi_star | 111 | 9.1233 | 1.1627 | 0.6126 | 0.6658 | 0.0029 | 0.1351 | ok | RAN |
| ETHUSDT | 4 | `ema1051_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.0343 | 0.5580 | 0.2265 | 0.0010 | 0.1518 | ok | RAN |
| ETHUSDT | 4 | `ema1051_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 1.0180 | 0.5772 | 0.0813 | 0.0008 | 0.1301 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1051_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 0.9507 | 0.5418 | -0.3386 | -0.0011 | 0.1235 | ok | RAN |
| SOLUSDT | 8 | `ema1051_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 0.9419 | 0.5283 | -0.4153 | -0.0012 | 0.1245 | ok | RAN |
| ETHUSDT | 8 | `ema1051_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 0.9539 | 0.5488 | -0.3047 | -0.0014 | 0.1581 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1051_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 0.8486 | 0.5225 | -0.7005 | -0.0065 | 0.1081 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1051_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1051_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1051_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1051_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1051_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1051_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1051_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1051_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1051_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1051_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1051_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1051_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1051_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1051_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1051_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1051_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
