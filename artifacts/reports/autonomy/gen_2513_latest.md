# Autonomy public-indicator hunt gen 2513

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T023052Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5840_above_at_h` | one_head_filter_pi_star | 47 | 4.3577 | 1.8095 | 0.6170 | 1.5811 | 0.0112 | 0.1277 | ok | RAN |
| SOLUSDT | 8 | `ema5840_above_at_h` | one_head_filter_pi_star | 43 | 3.9869 | 1.8468 | 0.6047 | 1.5318 | 0.0099 | 0.0930 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5840_below_at_h` | one_head_filter_pi_star | 320 | 26.1667 | 0.9448 | 0.5281 | -0.4336 | -0.0011 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `ema5840_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9636 | 0.5562 | -0.3005 | -0.0012 | 0.1383 | ok | RAN |
| SOLUSDT | 4 | `ema5840_below_at_h` | one_head_filter_pi_star | 327 | 26.7391 | 0.9401 | 0.5291 | -0.4780 | -0.0013 | 0.1315 | ok | RAN |
| ETHUSDT | 8 | `ema5840_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9532 | 0.5556 | -0.3843 | -0.0015 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5840_above_at_h` | one_head_filter_pi_star | 41 | 11.9670 | 0.8152 | 0.5122 | -1.0105 | -0.0096 | 0.1951 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5840_above_at_h` | one_head_filter_pi_star | 39 | 11.7689 | 0.7044 | 0.4872 | -1.8722 | -0.0169 | 0.1538 | ok | RAN |
| BTCUSDT | 8 | `ema5840_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6281 | 0.3158 | -0.8186 | -0.0398 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5840_above_at_h` | one_head_filter_pi_star | 22 | 1.8721 | 0.6170 | 0.3182 | -0.9116 | -0.0451 | 0.0455 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
