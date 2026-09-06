# Autonomy public-indicator hunt gen 2049

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T145931Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4680_above_at_h` | one_head_filter_pi_star | 34 | 3.1923 | 2.0083 | 0.6176 | 1.5484 | 0.0135 | 0.0588 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4680_above_at_h` | one_head_filter_pi_star | 61 | 5.0145 | 1.7160 | 0.6557 | 1.5193 | 0.0099 | 0.0820 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema4680_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9862 | 0.5601 | -0.1091 | -0.0004 | 0.1349 | ok | RAN |
| SOLUSDT | 8 | `ema4680_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9773 | 0.5377 | -0.1761 | -0.0005 | 0.1321 | ok | RAN |
| SOLUSDT | 4 | `ema4680_below_at_h` | one_head_filter_pi_star | 314 | 25.6761 | 0.9756 | 0.5350 | -0.1893 | -0.0005 | 0.1306 | ok | RAN |
| ETHUSDT | 4 | `ema4680_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9668 | 0.5572 | -0.2674 | -0.0011 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4680_above_at_h` | one_head_filter_pi_star | 36 | 4.2304 | 0.9178 | 0.5278 | -0.2581 | -0.0038 | 0.1389 | ok | RAN |
| ETHUSDT | 4 | `ema4680_above_at_h` | one_head_filter_pi_star | 42 | 12.2589 | 0.8871 | 0.5238 | -0.7263 | -0.0057 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4680_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4680_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
