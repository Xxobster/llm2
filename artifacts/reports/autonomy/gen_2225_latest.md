# Autonomy public-indicator hunt gen 2225

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T154145Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5120_above_at_h` | one_head_filter_pi_star | 44 | 4.0796 | 2.4719 | 0.6818 | 2.1523 | 0.0157 | 0.1136 | ok | RAN |
| SOLUSDT | 8 | `ema5120_above_at_h` | one_head_filter_pi_star | 44 | 4.0796 | 1.5939 | 0.6364 | 1.2005 | 0.0088 | 0.1591 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5120_below_at_h` | one_head_filter_pi_star | 304 | 24.8583 | 0.9810 | 0.5329 | -0.1433 | -0.0004 | 0.1349 | ok | RAN |
| SOLUSDT | 4 | `ema5120_below_at_h` | one_head_filter_pi_star | 315 | 25.7578 | 0.9620 | 0.5302 | -0.2986 | -0.0008 | 0.1302 | ok | RAN |
| ETHUSDT | 8 | `ema5120_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9517 | 0.5556 | -0.3958 | -0.0016 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5120_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9310 | 0.5526 | -0.5739 | -0.0023 | 0.1374 | ok | RAN |
| ETHUSDT | 8 | `ema5120_above_at_h` | one_head_filter_pi_star | 44 | 5.1704 | 0.7878 | 0.5000 | -0.8450 | -0.0113 | 0.1364 | ok | RAN |
| ETHUSDT | 4 | `ema5120_above_at_h` | one_head_filter_pi_star | 41 | 12.0975 | 0.7606 | 0.4878 | -1.6354 | -0.0126 | 0.1220 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5120_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5120_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
