# Autonomy public-indicator hunt gen 1740

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T085419Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1008_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1008_above_at_h` | one_head_filter_pi_star | 113 | 9.2877 | 1.2313 | 0.6106 | 0.9497 | 0.0039 | 0.1239 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1008_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.1058 | 0.5537 | 0.4821 | 0.0019 | 0.1157 | ok | RAN |
| ETHUSDT | 8 | `ema1008_above_at_h` | one_head_filter_pi_star | 139 | 11.4705 | 1.0337 | 0.5612 | 0.1590 | 0.0014 | 0.1151 | ok | RAN |
| ETHUSDT | 4 | `ema1008_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.0261 | 0.5591 | 0.1699 | 0.0008 | 0.1545 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1008_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9951 | 0.5465 | -0.0334 | -0.0001 | 0.1279 | ok | RAN |
| SOLUSDT | 4 | `ema1008_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 0.9717 | 0.5418 | -0.1899 | -0.0006 | 0.1235 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1008_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 0.9164 | 0.5395 | -0.5860 | -0.0026 | 0.1535 | ok | RAN |
| ETHUSDT | 4 | `ema1008_above_at_h` | one_head_filter_pi_star | 136 | 11.2229 | 0.9348 | 0.5515 | -0.3149 | -0.0028 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1008_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1008_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1008_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1008_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1008_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1008_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1008_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1008_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1008_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1008_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1008_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1008_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1008_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1008_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1008_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
