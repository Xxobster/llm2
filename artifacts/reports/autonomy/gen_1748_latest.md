# Autonomy public-indicator hunt gen 1748

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T093706Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1009_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.1740 | 0.6036 | 0.7176 | 0.0032 | 0.1351 | ok | RAN |
| SOLUSDT | 4 | `ema1009_above_at_h` | one_head_filter_pi_star | 125 | 10.2746 | 1.1680 | 0.5760 | 0.7294 | 0.0030 | 0.1200 | ok | RAN |
| SOLUSDT | 4 | `ema1009_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.0184 | 0.5512 | 0.1230 | 0.0004 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1009_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 0.9775 | 0.5420 | -0.1579 | -0.0005 | 0.1336 | ok | RAN |
| ETHUSDT | 4 | `ema1009_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 0.9785 | 0.5494 | -0.1477 | -0.0007 | 0.1459 | ok | RAN |
| ETHUSDT | 8 | `ema1009_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 0.9805 | 0.5571 | -0.0960 | -0.0008 | 0.1286 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1009_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 0.9391 | 0.5446 | -0.4199 | -0.0019 | 0.1518 | ok | RAN |
| ETHUSDT | 4 | `ema1009_above_at_h` | one_head_filter_pi_star | 141 | 11.6355 | 0.9546 | 0.5603 | -0.2238 | -0.0020 | 0.1064 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1009_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1009_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1009_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1009_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1009_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1009_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1009_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1009_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1009_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1009_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1009_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1009_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1009_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1009_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1009_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1009_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
