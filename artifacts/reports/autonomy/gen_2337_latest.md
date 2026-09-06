# Autonomy public-indicator hunt gen 2337

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T052619Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5400_above_at_h` | one_head_filter_pi_star | 58 | 5.3638 | 1.9921 | 0.6379 | 2.0109 | 0.0126 | 0.1207 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5400_above_at_h` | one_head_filter_pi_star | 56 | 4.6035 | 1.7668 | 0.6250 | 1.6490 | 0.0105 | 0.1250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5400_below_at_h` | one_head_filter_pi_star | 306 | 25.0219 | 0.9796 | 0.5359 | -0.1555 | -0.0004 | 0.1307 | ok | RAN |
| ETHUSDT | 8 | `ema5400_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9644 | 0.5562 | -0.2880 | -0.0012 | 0.1331 | ok | RAN |
| SOLUSDT | 4 | `ema5400_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 0.9435 | 0.5285 | -0.4456 | -0.0012 | 0.1266 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5400_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9417 | 0.5523 | -0.4943 | -0.0020 | 0.1395 | ok | RAN |
| ETHUSDT | 4 | `ema5400_above_at_h` | one_head_filter_pi_star | 44 | 5.1704 | 0.8261 | 0.5227 | -0.5823 | -0.0081 | 0.1364 | ok | RAN |
| ETHUSDT | 8 | `ema5400_above_at_h` | one_head_filter_pi_star | 44 | 12.9827 | 0.8157 | 0.5000 | -1.1544 | -0.0100 | 0.1818 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5400_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5400_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
