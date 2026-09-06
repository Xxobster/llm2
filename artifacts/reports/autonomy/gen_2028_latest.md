# Autonomy public-indicator hunt gen 2028

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T122740Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1046_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1046_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1046_above_at_h` | one_head_filter_pi_star | 115 | 9.5580 | 1.2368 | 0.6087 | 0.9740 | 0.0042 | 0.1478 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1046_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.2122 | 0.5926 | 0.8302 | 0.0036 | 0.1389 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1046_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.0241 | 0.5593 | 0.1649 | 0.0007 | 0.1568 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1046_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9576 | 0.5430 | -0.2973 | -0.0009 | 0.1250 | ok | RAN |
| SOLUSDT | 8 | `ema1046_below_at_h` | one_head_filter_pi_star | 270 | 21.9650 | 0.9403 | 0.5333 | -0.4299 | -0.0013 | 0.1296 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1046_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 0.9401 | 0.5556 | -0.2726 | -0.0025 | 0.1282 | ok | RAN |
| ETHUSDT | 4 | `ema1046_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 0.9198 | 0.5365 | -0.5766 | -0.0026 | 0.1502 | ok | RAN |
| ETHUSDT | 8 | `ema1046_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 0.7667 | 0.5093 | -1.1095 | -0.0108 | 0.1204 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1046_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1046_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1046_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1046_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1046_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1046_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1046_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1046_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1046_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1046_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1046_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1046_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1046_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1046_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
