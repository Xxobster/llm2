# Autonomy public-indicator hunt gen 2428

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T170557Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1098_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.1926 | 0.5856 | 0.7775 | 0.0032 | 0.1351 | ok | RAN |
| SOLUSDT | 8 | `ema1098_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.1478 | 0.5798 | 0.6364 | 0.0027 | 0.1261 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1098_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9607 | 0.5405 | -0.2772 | -0.0008 | 0.1313 | ok | RAN |
| SOLUSDT | 8 | `ema1098_below_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 0.9384 | 0.5311 | -0.4469 | -0.0013 | 0.1282 | ok | RAN |
| ETHUSDT | 8 | `ema1098_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9556 | 0.5517 | -0.3141 | -0.0014 | 0.1466 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1098_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 0.8962 | 0.5388 | -0.7187 | -0.0033 | 0.1598 | ok | RAN |
| ETHUSDT | 4 | `ema1098_above_at_h` | one_head_filter_pi_star | 105 | 8.6655 | 0.8824 | 0.5429 | -0.5189 | -0.0054 | 0.1048 | ok | RAN |
| ETHUSDT | 8 | `ema1098_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 0.7868 | 0.5185 | -1.0202 | -0.0099 | 0.1296 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1098_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6169 | 0.2667 | -0.7191 | -0.0358 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1098_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1098_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1098_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1098_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1098_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1098_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1098_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1098_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1098_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1098_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1098_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1098_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1098_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1098_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1098_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
