# Autonomy public-indicator hunt gen 2521

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T032029Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5860_above_at_h` | one_head_filter_pi_star | 43 | 3.9869 | 1.7661 | 0.6279 | 1.4441 | 0.0093 | 0.1395 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5860_above_at_h` | one_head_filter_pi_star | 51 | 4.3816 | 1.1135 | 0.5490 | 0.2982 | 0.0021 | 0.0980 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5860_below_at_h` | one_head_filter_pi_star | 325 | 26.5755 | 0.9773 | 0.5354 | -0.1772 | -0.0005 | 0.1292 | ok | RAN |
| SOLUSDT | 8 | `ema5860_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9740 | 0.5403 | -0.2040 | -0.0005 | 0.1284 | ok | RAN |
| ETHUSDT | 4 | `ema5860_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9633 | 0.5565 | -0.3094 | -0.0012 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5860_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9418 | 0.5543 | -0.4855 | -0.0019 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `ema5860_above_at_h` | one_head_filter_pi_star | 40 | 12.0706 | 0.7663 | 0.5000 | -1.3176 | -0.0124 | 0.1750 | ok | RAN |
| ETHUSDT | 8 | `ema5860_above_at_h` | one_head_filter_pi_star | 41 | 11.9670 | 0.7711 | 0.4878 | -1.2575 | -0.0136 | 0.1951 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5860_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6251 | 0.3000 | -0.8291 | -0.0418 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5860_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4537 | 0.2500 | -1.3535 | -0.0666 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
