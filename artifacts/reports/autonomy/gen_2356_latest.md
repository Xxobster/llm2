# Autonomy public-indicator hunt gen 2356

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T075205Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1089_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.2101 | 0.5913 | 0.8423 | 0.0037 | 0.1217 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1089_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.1228 | 0.5847 | 0.5353 | 0.0021 | 0.1356 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1089_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 0.9656 | 0.5396 | -0.2423 | -0.0007 | 0.1283 | ok | RAN |
| ETHUSDT | 4 | `ema1089_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 0.9703 | 0.5504 | -0.2053 | -0.0009 | 0.1471 | ok | RAN |
| SOLUSDT | 4 | `ema1089_below_at_h` | one_head_filter_pi_star | 265 | 21.5583 | 0.9506 | 0.5358 | -0.3521 | -0.0011 | 0.1283 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1089_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9049 | 0.5388 | -0.6988 | -0.0030 | 0.1595 | ok | RAN |
| ETHUSDT | 8 | `ema1089_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 0.8865 | 0.5403 | -0.5370 | -0.0049 | 0.1129 | ok | RAN |
| ETHUSDT | 4 | `ema1089_above_at_h` | one_head_filter_pi_star | 122 | 10.0282 | 0.8746 | 0.5492 | -0.5939 | -0.0055 | 0.1230 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1089_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1089_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1089_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1089_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1089_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1089_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1089_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1089_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1089_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1089_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1089_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1089_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1089_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1089_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1089_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1089_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
