# Autonomy public-indicator hunt gen 1836

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T174115Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1021_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1021_above_at_h` | one_head_filter_pi_star | 112 | 9.2060 | 1.1803 | 0.5893 | 0.7484 | 0.0033 | 0.1429 | ok | RAN |
| SOLUSDT | 4 | `ema1021_above_at_h` | one_head_filter_pi_star | 118 | 9.6986 | 1.1689 | 0.6186 | 0.7120 | 0.0030 | 0.1356 | ok | RAN |
| ETHUSDT | 4 | `ema1021_above_at_h` | one_head_filter_pi_star | 127 | 10.4811 | 1.0197 | 0.5669 | 0.0921 | 0.0008 | 0.1102 | ok | RAN |
| SOLUSDT | 8 | `ema1021_below_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 1.0283 | 0.5583 | 0.1835 | 0.0006 | 0.1292 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1021_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9720 | 0.5466 | -0.1972 | -0.0009 | 0.1483 | ok | RAN |
| ETHUSDT | 8 | `ema1021_above_at_h` | one_head_filter_pi_star | 126 | 10.3986 | 0.9620 | 0.5635 | -0.1774 | -0.0016 | 0.1190 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1021_below_at_h` | one_head_filter_pi_star | 249 | 20.3410 | 0.9420 | 0.5382 | -0.4307 | -0.0019 | 0.1526 | ok | RAN |
| SOLUSDT | 4 | `ema1021_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 0.8890 | 0.5341 | -0.7929 | -0.0025 | 0.1365 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1021_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1021_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1021_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1021_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1021_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1021_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1021_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1021_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1021_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1021_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1021_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1021_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1021_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1021_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1021_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
