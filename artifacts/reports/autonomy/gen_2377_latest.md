# Autonomy public-indicator hunt gen 2377

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T105316Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5500_above_at_h` | one_head_filter_pi_star | 47 | 4.3577 | 1.9093 | 0.6383 | 1.6836 | 0.0116 | 0.1277 | ok | RAN |
| SOLUSDT | 4 | `ema5500_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 1.5895 | 0.6042 | 1.2435 | 0.0087 | 0.1458 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5500_below_at_h` | one_head_filter_pi_star | 319 | 26.0849 | 0.9864 | 0.5392 | -0.1062 | -0.0003 | 0.1317 | ok | RAN |
| SOLUSDT | 4 | `ema5500_below_at_h` | one_head_filter_pi_star | 322 | 26.3302 | 0.9747 | 0.5404 | -0.1972 | -0.0005 | 0.1335 | ok | RAN |
| ETHUSDT | 4 | `ema5500_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9621 | 0.5565 | -0.3149 | -0.0013 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5500_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9194 | 0.5487 | -0.6789 | -0.0027 | 0.1357 | ok | RAN |
| ETHUSDT | 8 | `ema5500_above_at_h` | one_head_filter_pi_star | 44 | 12.8427 | 0.8257 | 0.5000 | -1.0269 | -0.0092 | 0.2045 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5500_above_at_h` | one_head_filter_pi_star | 35 | 5.9615 | 0.6532 | 0.4857 | -1.4587 | -0.0197 | 0.1143 | ok | RAN |
| BTCUSDT | 4 | `ema5500_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5500_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0590 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
