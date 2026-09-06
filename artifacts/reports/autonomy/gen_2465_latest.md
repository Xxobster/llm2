# Autonomy public-indicator hunt gen 2465

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T212147Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5720_above_at_h` | one_head_filter_pi_star | 52 | 4.3777 | 1.7913 | 0.6154 | 1.5545 | 0.0095 | 0.0962 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5720_above_at_h` | one_head_filter_pi_star | 51 | 4.3453 | 1.2891 | 0.5882 | 0.6965 | 0.0048 | 0.0980 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5720_below_at_h` | one_head_filter_pi_star | 328 | 26.8208 | 0.9827 | 0.5396 | -0.1344 | -0.0004 | 0.1280 | ok | RAN |
| ETHUSDT | 8 | `ema5720_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9760 | 0.5591 | -0.1957 | -0.0008 | 0.1354 | ok | RAN |
| SOLUSDT | 8 | `ema5720_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9524 | 0.5357 | -0.3799 | -0.0010 | 0.1280 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5720_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9333 | 0.5503 | -0.5445 | -0.0022 | 0.1391 | ok | RAN |
| ETHUSDT | 4 | `ema5720_above_at_h` | one_head_filter_pi_star | 38 | 6.4725 | 0.7297 | 0.4737 | -1.1017 | -0.0148 | 0.1316 | ok | RAN |
| ETHUSDT | 8 | `ema5720_above_at_h` | one_head_filter_pi_star | 47 | 12.7267 | 0.7174 | 0.4681 | -1.8349 | -0.0165 | 0.1702 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5720_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5720_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5440 | 0.3000 | -1.0991 | -0.0595 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
