# Autonomy public-indicator hunt gen 1953

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T042417Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4440_above_at_h` | one_head_filter_pi_star | 47 | 3.8637 | 2.0116 | 0.6383 | 1.6698 | 0.0125 | 0.1277 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4440_above_at_h` | one_head_filter_pi_star | 72 | 5.9188 | 1.9516 | 0.6667 | 2.1549 | 0.0123 | 0.0972 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4440_below_at_h` | one_head_filter_pi_star | 329 | 26.9026 | 0.9686 | 0.5380 | -0.2486 | -0.0006 | 0.1307 | ok | RAN |
| ETHUSDT | 4 | `ema4440_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9754 | 0.5588 | -0.1957 | -0.0008 | 0.1353 | ok | RAN |
| ETHUSDT | 8 | `ema4440_below_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 0.9675 | 0.5581 | -0.2740 | -0.0011 | 0.1331 | ok | RAN |
| SOLUSDT | 4 | `ema4440_below_at_h` | one_head_filter_pi_star | 306 | 25.0219 | 0.9415 | 0.5327 | -0.4499 | -0.0012 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4440_above_at_h` | one_head_filter_pi_star | 26 | 7.8459 | 0.8830 | 0.5000 | -0.4851 | -0.0054 | 0.1538 | ok | RAN |
| ETHUSDT | 4 | `ema4440_above_at_h` | one_head_filter_pi_star | 32 | 9.4420 | 0.7616 | 0.4688 | -1.2132 | -0.0121 | 0.0938 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
