# Autonomy public-indicator hunt gen 2017

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T111154Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4600_above_at_h` | one_head_filter_pi_star | 55 | 4.5213 | 1.6848 | 0.6364 | 1.4178 | 0.0103 | 0.1273 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4600_above_at_h` | one_head_filter_pi_star | 68 | 5.5900 | 1.5589 | 0.6176 | 1.4203 | 0.0088 | 0.1029 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4600_below_at_h` | one_head_filter_pi_star | 302 | 24.6948 | 0.9996 | 0.5331 | -0.0026 | -0.0000 | 0.1391 | ok | RAN |
| ETHUSDT | 8 | `ema4600_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9951 | 0.5610 | -0.0387 | -0.0002 | 0.1366 | ok | RAN |
| SOLUSDT | 8 | `ema4600_below_at_h` | one_head_filter_pi_star | 330 | 26.9844 | 0.9623 | 0.5364 | -0.2955 | -0.0008 | 0.1303 | ok | RAN |
| ETHUSDT | 4 | `ema4600_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9665 | 0.5581 | -0.2741 | -0.0011 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4600_above_at_h` | one_head_filter_pi_star | 39 | 11.3833 | 0.8629 | 0.5128 | -0.7094 | -0.0070 | 0.2051 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4600_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.6713 | 0.4706 | -2.0472 | -0.0189 | 0.0882 | ok | RAN |
| BTCUSDT | 8 | `ema4600_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4600_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
