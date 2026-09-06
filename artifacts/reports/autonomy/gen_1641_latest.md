# Autonomy public-indicator hunt gen 1641

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T215559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema3660_above_at_h` | one_head_filter_pi_star | 77 | 6.3298 | 1.7561 | 0.6883 | 1.9076 | 0.0100 | 0.1039 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3660_above_at_h` | one_head_filter_pi_star | 71 | 5.8233 | 1.5822 | 0.6479 | 1.4689 | 0.0077 | 0.0986 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3660_below_at_h` | one_head_filter_pi_star | 288 | 23.5500 | 1.0652 | 0.5486 | 0.4630 | 0.0013 | 0.1354 | ok | RAN |
| SOLUSDT | 4 | `ema3660_below_at_h` | one_head_filter_pi_star | 302 | 24.6948 | 1.0122 | 0.5464 | 0.0891 | 0.0002 | 0.1291 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema3660_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9532 | 0.5552 | -0.3904 | -0.0016 | 0.1337 | ok | RAN |
| ETHUSDT | 4 | `ema3660_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9527 | 0.5546 | -0.4009 | -0.0016 | 0.1351 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3660_above_at_h` | one_head_filter_pi_star | 36 | 4.2304 | 0.6697 | 0.4722 | -1.2786 | -0.0185 | 0.1389 | ok | RAN |
| ETHUSDT | 8 | `ema3660_above_at_h` | one_head_filter_pi_star | 33 | 9.7370 | 0.6701 | 0.4545 | -1.7058 | -0.0191 | 0.1515 | ok | RAN |
| ETHUSDT | 4 | `ema3660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3660_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3660_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
