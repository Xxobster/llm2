# Autonomy public-indicator hunt gen 2193

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T113542Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5040_above_at_h` | one_head_filter_pi_star | 45 | 4.1723 | 2.0459 | 0.6444 | 1.8123 | 0.0130 | 0.1333 | ok | RAN |
| SOLUSDT | 8 | `ema5040_above_at_h` | one_head_filter_pi_star | 49 | 4.0281 | 1.3673 | 0.5918 | 0.7894 | 0.0056 | 0.0816 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5040_below_at_h` | one_head_filter_pi_star | 321 | 26.2484 | 0.9801 | 0.5327 | -0.1536 | -0.0004 | 0.1308 | ok | RAN |
| SOLUSDT | 8 | `ema5040_below_at_h` | one_head_filter_pi_star | 325 | 26.5755 | 0.9806 | 0.5354 | -0.1511 | -0.0004 | 0.1292 | ok | RAN |
| ETHUSDT | 4 | `ema5040_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9788 | 0.5587 | -0.1751 | -0.0007 | 0.1375 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5040_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9418 | 0.5533 | -0.4930 | -0.0020 | 0.1354 | ok | RAN |
| ETHUSDT | 8 | `ema5040_above_at_h` | one_head_filter_pi_star | 41 | 4.8179 | 0.8798 | 0.5122 | -0.3937 | -0.0058 | 0.1220 | ok | RAN |
| ETHUSDT | 4 | `ema5040_above_at_h` | one_head_filter_pi_star | 25 | 7.7081 | 0.8426 | 0.4800 | -0.6662 | -0.0076 | 0.1200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5040_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5040_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
