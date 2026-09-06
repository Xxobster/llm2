# Autonomy public-indicator hunt gen 1689

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T034123Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3780_above_at_h` | one_head_filter_pi_star | 88 | 7.1768 | 1.7406 | 0.6591 | 1.9449 | 0.0085 | 0.1023 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3780_above_at_h` | one_head_filter_pi_star | 82 | 6.7409 | 1.5944 | 0.6463 | 1.6080 | 0.0081 | 0.1220 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3780_below_at_h` | one_head_filter_pi_star | 286 | 23.3865 | 1.0520 | 0.5455 | 0.3698 | 0.0011 | 0.1294 | ok | RAN |
| SOLUSDT | 4 | `ema3780_below_at_h` | one_head_filter_pi_star | 293 | 23.9589 | 1.0405 | 0.5461 | 0.2902 | 0.0008 | 0.1297 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema3780_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9795 | 0.5591 | -0.1671 | -0.0007 | 0.1297 | ok | RAN |
| ETHUSDT | 8 | `ema3780_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9709 | 0.5562 | -0.2302 | -0.0009 | 0.1361 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema3780_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.8188 | 0.5161 | -0.8354 | -0.0087 | 0.1290 | ok | RAN |
| ETHUSDT | 8 | `ema3780_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.7093 | 0.4839 | -1.4246 | -0.0156 | 0.1613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3780_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3780_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
