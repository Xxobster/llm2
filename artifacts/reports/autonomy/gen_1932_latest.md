# Autonomy public-indicator hunt gen 1932

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T022733Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1033_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.2050 | 0.5948 | 0.8529 | 0.0037 | 0.1379 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1033_above_at_h` | one_head_filter_pi_star | 119 | 9.7808 | 1.2138 | 0.6050 | 0.8805 | 0.0037 | 0.1429 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1033_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 0.9680 | 0.5455 | -0.2181 | -0.0007 | 0.1344 | ok | RAN |
| SOLUSDT | 8 | `ema1033_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 0.9598 | 0.5368 | -0.2864 | -0.0009 | 0.1360 | ok | RAN |
| ETHUSDT | 4 | `ema1033_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 0.9673 | 0.5455 | -0.2233 | -0.0010 | 0.1515 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1033_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 0.9415 | 0.5455 | -0.3954 | -0.0018 | 0.1500 | ok | RAN |
| ETHUSDT | 8 | `ema1033_above_at_h` | one_head_filter_pi_star | 114 | 9.4082 | 0.9049 | 0.5351 | -0.4410 | -0.0042 | 0.1316 | ok | RAN |
| ETHUSDT | 4 | `ema1033_above_at_h` | one_head_filter_pi_star | 126 | 10.3986 | 0.9072 | 0.5476 | -0.4447 | -0.0042 | 0.1349 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1033_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1033_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0327 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1033_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1033_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1033_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1033_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1033_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1033_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1033_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1033_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1033_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1033_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1033_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1033_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1033_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1033_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
