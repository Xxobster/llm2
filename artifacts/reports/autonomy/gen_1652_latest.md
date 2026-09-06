# Autonomy public-indicator hunt gen 1652

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T232201Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema994_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.1419 | 0.5847 | 0.6174 | 0.0025 | 0.1356 | ok | RAN |
| SOLUSDT | 4 | `ema994_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.0951 | 0.5714 | 0.4367 | 0.0017 | 0.1270 | ok | RAN |
| ETHUSDT | 4 | `ema994_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.0288 | 0.5566 | 0.1881 | 0.0009 | 0.1584 | ok | RAN |
| SOLUSDT | 8 | `ema994_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 1.0277 | 0.5502 | 0.1831 | 0.0006 | 0.1245 | ok | RAN |
| ETHUSDT | 8 | `ema994_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.0136 | 0.5546 | 0.0929 | 0.0004 | 0.1528 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema994_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 0.9667 | 0.5492 | -0.2252 | -0.0007 | 0.1230 | ok | RAN |
| ETHUSDT | 4 | `ema994_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 0.9722 | 0.5610 | -0.1288 | -0.0012 | 0.1220 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema994_above_at_h` | one_head_filter_pi_star | 131 | 10.8112 | 0.8898 | 0.5420 | -0.5524 | -0.0049 | 0.1298 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema994_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema994_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema994_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema994_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema994_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema994_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema994_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema994_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema994_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema994_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema994_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema994_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema994_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema994_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema994_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema994_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
