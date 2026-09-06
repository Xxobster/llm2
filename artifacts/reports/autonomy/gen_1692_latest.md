# Autonomy public-indicator hunt gen 1692

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T040140Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1001_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0822 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1001_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1001_above_at_h` | one_head_filter_pi_star | 119 | 9.7808 | 1.1412 | 0.5798 | 0.6209 | 0.0026 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `ema1001_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.0754 | 0.5600 | 0.4938 | 0.0023 | 0.1511 | ok | RAN |
| SOLUSDT | 8 | `ema1001_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.0527 | 0.5656 | 0.2432 | 0.0010 | 0.1475 | ok | RAN |
| SOLUSDT | 8 | `ema1001_below_at_h` | one_head_filter_pi_star | 221 | 18.0714 | 1.0077 | 0.5520 | 0.0479 | 0.0002 | 0.1222 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1001_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9636 | 0.5426 | -0.2553 | -0.0008 | 0.1279 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1001_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 0.9277 | 0.5397 | -0.5241 | -0.0023 | 0.1464 | ok | RAN |
| ETHUSDT | 8 | `ema1001_above_at_h` | one_head_filter_pi_star | 128 | 10.5627 | 0.9338 | 0.5469 | -0.3222 | -0.0029 | 0.1328 | ok | RAN |
| ETHUSDT | 4 | `ema1001_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 0.9268 | 0.5630 | -0.3614 | -0.0033 | 0.1333 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1001_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1001_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1001_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1001_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1001_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1001_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1001_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1001_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1001_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1001_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1001_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1001_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1001_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1001_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
