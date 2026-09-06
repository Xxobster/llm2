# Autonomy public-indicator hunt gen 1825

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T164000Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4120_above_at_h` | one_head_filter_pi_star | 53 | 4.3569 | 2.1152 | 0.6981 | 1.9985 | 0.0136 | 0.0755 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4120_above_at_h` | one_head_filter_pi_star | 65 | 5.3434 | 1.7530 | 0.6615 | 1.6912 | 0.0102 | 0.1231 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4120_below_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.0167 | 0.5443 | 0.1275 | 0.0003 | 0.1297 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4120_below_at_h` | one_head_filter_pi_star | 330 | 26.9844 | 0.9868 | 0.5424 | -0.1025 | -0.0003 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `ema4120_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9830 | 0.5591 | -0.1399 | -0.0006 | 0.1354 | ok | RAN |
| ETHUSDT | 8 | `ema4120_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9703 | 0.5591 | -0.2461 | -0.0010 | 0.1354 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4120_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 0.7624 | 0.5000 | -1.1617 | -0.0110 | 0.1333 | ok | RAN |
| ETHUSDT | 8 | `ema4120_above_at_h` | one_head_filter_pi_star | 29 | 8.7512 | 0.7449 | 0.4828 | -1.2969 | -0.0122 | 0.1379 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema4120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema4120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
