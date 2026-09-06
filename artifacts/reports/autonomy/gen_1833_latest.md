# Autonomy public-indicator hunt gen 1833

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T172505Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4140_above_at_h` | one_head_filter_pi_star | 79 | 6.4795 | 1.8296 | 0.6709 | 2.0181 | 0.0103 | 0.1013 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4140_above_at_h` | one_head_filter_pi_star | 95 | 7.7918 | 1.4806 | 0.6421 | 1.5036 | 0.0070 | 0.1053 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4140_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.0022 | 0.5463 | 0.0169 | 0.0000 | 0.1327 | ok | RAN |
| SOLUSDT | 4 | `ema4140_below_at_h` | one_head_filter_pi_star | 298 | 24.3677 | 0.9774 | 0.5302 | -0.1702 | -0.0005 | 0.1409 | ok | RAN |
| ETHUSDT | 8 | `ema4140_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9775 | 0.5575 | -0.1845 | -0.0007 | 0.1322 | ok | RAN |
| ETHUSDT | 4 | `ema4140_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9718 | 0.5591 | -0.2322 | -0.0009 | 0.1354 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4140_above_at_h` | one_head_filter_pi_star | 33 | 9.9583 | 0.8684 | 0.5152 | -0.6931 | -0.0070 | 0.1818 | ok | RAN |
| ETHUSDT | 8 | `ema4140_above_at_h` | one_head_filter_pi_star | 29 | 8.7512 | 0.7014 | 0.4828 | -1.3945 | -0.0148 | 0.1724 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4140_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4140_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
