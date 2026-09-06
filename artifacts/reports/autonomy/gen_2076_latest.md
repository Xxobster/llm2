# Autonomy public-indicator hunt gen 2076

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T185322Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1052_above_at_h` | one_head_filter_pi_star | 112 | 9.2055 | 1.2745 | 0.6161 | 1.0899 | 0.0046 | 0.1339 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1052_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.1012 | 0.5868 | 0.4544 | 0.0019 | 0.1322 | ok | RAN |
| SOLUSDT | 8 | `ema1052_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.0064 | 0.5480 | 0.0433 | 0.0001 | 0.1280 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1052_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9361 | 0.5367 | -0.4561 | -0.0014 | 0.1274 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1052_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9472 | 0.5424 | -0.3772 | -0.0017 | 0.1483 | ok | RAN |
| ETHUSDT | 8 | `ema1052_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9372 | 0.5459 | -0.4353 | -0.0020 | 0.1485 | ok | RAN |
| ETHUSDT | 8 | `ema1052_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 0.8908 | 0.5315 | -0.4904 | -0.0047 | 0.1261 | ok | RAN |
| ETHUSDT | 4 | `ema1052_above_at_h` | one_head_filter_pi_star | 143 | 11.8016 | 0.8532 | 0.5385 | -0.7598 | -0.0066 | 0.1119 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1052_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1052_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1052_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1052_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1052_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1052_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1052_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1052_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1052_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1052_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1052_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1052_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1052_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1052_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1052_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1052_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
