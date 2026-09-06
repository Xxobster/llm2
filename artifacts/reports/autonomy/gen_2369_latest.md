# Autonomy public-indicator hunt gen 2369

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T094211Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5480_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 2.1673 | 0.6458 | 2.0091 | 0.0131 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `ema5480_above_at_h` | one_head_filter_pi_star | 42 | 3.8941 | 1.8810 | 0.6190 | 1.5341 | 0.0109 | 0.1190 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5480_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9775 | 0.5368 | -0.1761 | -0.0005 | 0.1350 | ok | RAN |
| ETHUSDT | 8 | `ema5480_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9808 | 0.5569 | -0.1518 | -0.0006 | 0.1347 | ok | RAN |
| SOLUSDT | 4 | `ema5480_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 0.9656 | 0.5335 | -0.2660 | -0.0007 | 0.1310 | ok | RAN |
| ETHUSDT | 4 | `ema5480_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9521 | 0.5552 | -0.3976 | -0.0016 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5480_above_at_h` | one_head_filter_pi_star | 40 | 6.8132 | 0.8135 | 0.5000 | -0.7379 | -0.0086 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `ema5480_above_at_h` | one_head_filter_pi_star | 44 | 12.8427 | 0.7237 | 0.4773 | -1.7286 | -0.0156 | 0.1818 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5480_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6281 | 0.3158 | -0.8186 | -0.0428 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5480_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
