# Autonomy public-indicator hunt gen 2113

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T235356Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4840_above_at_h` | one_head_filter_pi_star | 36 | 3.3801 | 1.7613 | 0.6389 | 1.2601 | 0.0099 | 0.1111 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4840_above_at_h` | one_head_filter_pi_star | 61 | 5.0145 | 1.5229 | 0.6393 | 1.2514 | 0.0081 | 0.0984 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema4840_above_at_h` | one_head_filter_pi_star | 36 | 10.8636 | 1.0177 | 0.5556 | 0.0851 | 0.0009 | 0.1389 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4840_below_at_h` | one_head_filter_pi_star | 305 | 24.9401 | 0.9744 | 0.5344 | -0.1916 | -0.0005 | 0.1377 | ok | RAN |
| SOLUSDT | 4 | `ema4840_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 0.9615 | 0.5335 | -0.3006 | -0.0008 | 0.1310 | ok | RAN |
| ETHUSDT | 8 | `ema4840_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9550 | 0.5556 | -0.3682 | -0.0015 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `ema4840_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9544 | 0.5559 | -0.3688 | -0.0015 | 0.1382 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4840_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.9635 | 0.5294 | -0.1728 | -0.0017 | 0.1471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4840_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4840_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
