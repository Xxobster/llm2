# Autonomy public-indicator hunt gen 1633

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T211240Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema3640_above_at_h` | one_head_filter_pi_star | 75 | 6.1654 | 1.5972 | 0.6667 | 1.5844 | 0.0083 | 0.1200 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3640_above_at_h` | one_head_filter_pi_star | 92 | 7.5629 | 1.5093 | 0.6630 | 1.5354 | 0.0075 | 0.1196 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3640_below_at_h` | one_head_filter_pi_star | 300 | 24.5313 | 1.0565 | 0.5467 | 0.4058 | 0.0011 | 0.1267 | ok | RAN |
| SOLUSDT | 8 | `ema3640_below_at_h` | one_head_filter_pi_star | 294 | 23.9175 | 1.0251 | 0.5408 | 0.1799 | 0.0005 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema3640_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9962 | 0.5610 | -0.0304 | -0.0001 | 0.1308 | ok | RAN |
| ETHUSDT | 4 | `ema3640_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9868 | 0.5592 | -0.1057 | -0.0004 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema3640_above_at_h` | one_head_filter_pi_star | 36 | 4.2304 | 0.7943 | 0.5000 | -0.6639 | -0.0102 | 0.1389 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema3640_above_at_h` | one_head_filter_pi_star | 29 | 3.4078 | 0.6583 | 0.4483 | -1.1118 | -0.0180 | 0.1379 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3640_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3640_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
