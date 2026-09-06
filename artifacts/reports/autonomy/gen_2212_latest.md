# Autonomy public-indicator hunt gen 2212

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T140437Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1070_above_at_h` | one_head_filter_pi_star | 105 | 8.5617 | 1.3643 | 0.6286 | 1.3499 | 0.0055 | 0.1238 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1070_above_at_h` | one_head_filter_pi_star | 106 | 8.7123 | 1.2649 | 0.6132 | 1.0364 | 0.0044 | 0.1415 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1070_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.0023 | 0.5547 | 0.0151 | 0.0000 | 0.1296 | ok | RAN |
| ETHUSDT | 4 | `ema1070_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 0.9707 | 0.5443 | -0.2097 | -0.0009 | 0.1561 | ok | RAN |
| SOLUSDT | 4 | `ema1070_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 0.9348 | 0.5358 | -0.4682 | -0.0014 | 0.1321 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1070_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 0.9194 | 0.5420 | -0.5892 | -0.0026 | 0.1471 | ok | RAN |
| ETHUSDT | 8 | `ema1070_above_at_h` | one_head_filter_pi_star | 122 | 10.0282 | 0.9199 | 0.5410 | -0.3703 | -0.0034 | 0.1311 | ok | RAN |
| ETHUSDT | 4 | `ema1070_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 0.8494 | 0.5278 | -0.6712 | -0.0068 | 0.1019 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1070_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1070_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1070_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1070_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1070_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1070_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1070_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1070_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1070_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1070_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1070_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1070_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1070_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1070_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1070_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1070_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
