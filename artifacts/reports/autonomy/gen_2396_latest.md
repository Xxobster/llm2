# Autonomy public-indicator hunt gen 2396

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T132201Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1094_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.2650 | 0.6106 | 1.0662 | 0.0045 | 0.1416 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1094_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.0276 | 0.5565 | 0.1252 | 0.0005 | 0.1565 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1094_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 0.9511 | 0.5356 | -0.3266 | -0.0010 | 0.1297 | ok | RAN |
| SOLUSDT | 4 | `ema1094_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9481 | 0.5391 | -0.3566 | -0.0011 | 0.1367 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1094_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 0.9279 | 0.5365 | -0.5184 | -0.0023 | 0.1502 | ok | RAN |
| ETHUSDT | 8 | `ema1094_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9266 | 0.5381 | -0.5361 | -0.0024 | 0.1483 | ok | RAN |
| ETHUSDT | 4 | `ema1094_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 0.8916 | 0.5323 | -0.5175 | -0.0049 | 0.1290 | ok | RAN |
| ETHUSDT | 8 | `ema1094_above_at_h` | one_head_filter_pi_star | 115 | 9.4908 | 0.8840 | 0.5391 | -0.5437 | -0.0051 | 0.1130 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1094_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1094_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1094_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1094_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1094_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1094_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1094_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1094_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1094_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1094_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1094_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1094_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1094_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1094_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1094_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1094_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
