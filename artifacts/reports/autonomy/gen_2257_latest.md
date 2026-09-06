# Autonomy public-indicator hunt gen 2257

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T192944Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5200_above_at_h` | one_head_filter_pi_star | 55 | 4.5720 | 1.7672 | 0.6727 | 1.6598 | 0.0109 | 0.1273 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema5200_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 1.5312 | 0.6250 | 1.2062 | 0.0085 | 0.0833 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5200_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9781 | 0.5346 | -0.1708 | -0.0005 | 0.1289 | ok | RAN |
| ETHUSDT | 8 | `ema5200_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9783 | 0.5581 | -0.1755 | -0.0007 | 0.1366 | ok | RAN |
| SOLUSDT | 8 | `ema5200_below_at_h` | one_head_filter_pi_star | 309 | 25.2672 | 0.9511 | 0.5307 | -0.3779 | -0.0010 | 0.1359 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5200_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9341 | 0.5513 | -0.5530 | -0.0022 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `ema5200_above_at_h` | one_head_filter_pi_star | 38 | 6.4725 | 0.9200 | 0.5263 | -0.3023 | -0.0037 | 0.1053 | ok | RAN |
| ETHUSDT | 8 | `ema5200_above_at_h` | one_head_filter_pi_star | 45 | 13.1346 | 0.8672 | 0.5111 | -0.8487 | -0.0068 | 0.1333 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5200_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5200_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0615 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
