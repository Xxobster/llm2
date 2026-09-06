# Autonomy public-indicator hunt gen 1628

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T204449Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema991_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.1454 | 0.5935 | 0.6465 | 0.0025 | 0.1301 | ok | RAN |
| SOLUSDT | 8 | `ema991_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.0575 | 0.5676 | 0.2485 | 0.0010 | 0.1351 | ok | RAN |
| SOLUSDT | 8 | `ema991_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.0138 | 0.5521 | 0.0932 | 0.0003 | 0.1313 | ok | RAN |
| SOLUSDT | 4 | `ema991_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.0082 | 0.5520 | 0.0546 | 0.0002 | 0.1280 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema991_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 0.9991 | 0.5520 | -0.0058 | -0.0000 | 0.1538 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema991_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 0.9546 | 0.5615 | -0.2177 | -0.0020 | 0.1231 | ok | RAN |
| ETHUSDT | 8 | `ema991_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 0.9209 | 0.5319 | -0.5807 | -0.0025 | 0.1447 | ok | RAN |
| ETHUSDT | 4 | `ema991_above_at_h` | one_head_filter_pi_star | 131 | 10.8112 | 0.8726 | 0.5420 | -0.6266 | -0.0057 | 0.1145 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema991_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema991_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema991_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema991_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema991_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema991_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema991_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema991_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema991_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema991_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema991_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema991_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema991_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema991_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema991_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema991_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
