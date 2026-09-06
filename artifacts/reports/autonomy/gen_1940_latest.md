# Autonomy public-indicator hunt gen 1940

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T031158Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1034_above_at_h` | one_head_filter_pi_star | 115 | 9.4526 | 1.2101 | 0.6000 | 0.9022 | 0.0036 | 0.1130 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1034_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.1256 | 0.5833 | 0.5358 | 0.0024 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1034_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 0.9809 | 0.5472 | -0.1305 | -0.0004 | 0.1260 | ok | RAN |
| ETHUSDT | 4 | `ema1034_above_at_h` | one_head_filter_pi_star | 132 | 10.8928 | 0.9780 | 0.5606 | -0.1055 | -0.0009 | 0.1136 | ok | RAN |
| SOLUSDT | 4 | `ema1034_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 0.9399 | 0.5418 | -0.4160 | -0.0013 | 0.1355 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1034_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 0.9446 | 0.5417 | -0.3752 | -0.0017 | 0.1574 | ok | RAN |
| ETHUSDT | 8 | `ema1034_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 0.8777 | 0.5322 | -0.9020 | -0.0041 | 0.1545 | ok | RAN |
| ETHUSDT | 8 | `ema1034_above_at_h` | one_head_filter_pi_star | 120 | 9.8638 | 0.9007 | 0.5333 | -0.4659 | -0.0042 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1034_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1034_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1034_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1034_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1034_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1034_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1034_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1034_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1034_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1034_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1034_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1034_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1034_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1034_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1034_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1034_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
