# Autonomy public-indicator hunt gen 2500

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T010928Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1108_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1108_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.1447 | 0.5739 | 0.6170 | 0.0026 | 0.1304 | ok | RAN |
| SOLUSDT | 4 | `ema1108_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.0999 | 0.5752 | 0.4360 | 0.0019 | 0.1416 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1108_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 0.9655 | 0.5420 | -0.2318 | -0.0007 | 0.1218 | ok | RAN |
| SOLUSDT | 4 | `ema1108_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9573 | 0.5402 | -0.3023 | -0.0009 | 0.1303 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1108_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 0.9364 | 0.5372 | -0.4597 | -0.0020 | 0.1446 | ok | RAN |
| ETHUSDT | 8 | `ema1108_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 0.9008 | 0.5455 | -0.7276 | -0.0032 | 0.1558 | ok | RAN |
| ETHUSDT | 8 | `ema1108_above_at_h` | one_head_filter_pi_star | 101 | 8.3354 | 0.8401 | 0.5347 | -0.7235 | -0.0072 | 0.1089 | ok | RAN |
| ETHUSDT | 4 | `ema1108_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 0.8085 | 0.5246 | -0.9267 | -0.0091 | 0.1148 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1108_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1108_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1108_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
