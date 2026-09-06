# Autonomy public-indicator hunt gen 1772

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T114825Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1012_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.1091 | 0.5812 | 0.4826 | 0.0020 | 0.1368 | ok | RAN |
| SOLUSDT | 8 | `ema1012_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.0913 | 0.5702 | 0.3957 | 0.0017 | 0.1228 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1012_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9993 | 0.5531 | -0.0047 | -0.0000 | 0.1504 | ok | RAN |
| SOLUSDT | 4 | `ema1012_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9642 | 0.5426 | -0.2484 | -0.0008 | 0.1279 | ok | RAN |
| SOLUSDT | 8 | `ema1012_below_at_h` | one_head_filter_pi_star | 270 | 22.0781 | 0.9626 | 0.5407 | -0.2660 | -0.0008 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1012_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 0.9262 | 0.5442 | -0.4964 | -0.0023 | 0.1581 | ok | RAN |
| ETHUSDT | 8 | `ema1012_above_at_h` | one_head_filter_pi_star | 128 | 10.5627 | 0.9008 | 0.5391 | -0.4850 | -0.0041 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema1012_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 0.8646 | 0.5407 | -0.6779 | -0.0061 | 0.1259 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1012_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1012_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1012_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1012_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1012_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1012_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1012_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1012_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1012_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1012_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1012_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1012_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1012_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1012_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1012_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1012_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
