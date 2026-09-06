# Autonomy public-indicator hunt gen 1905

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T235212Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4320_above_at_h` | one_head_filter_pi_star | 75 | 6.1654 | 1.9404 | 0.6667 | 2.1695 | 0.0125 | 0.1067 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4320_above_at_h` | one_head_filter_pi_star | 59 | 4.8501 | 1.7260 | 0.5932 | 1.6141 | 0.0108 | 0.1017 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema4320_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9984 | 0.5608 | -0.0121 | -0.0001 | 0.1365 | ok | RAN |
| SOLUSDT | 4 | `ema4320_below_at_h` | one_head_filter_pi_star | 300 | 24.5313 | 0.9841 | 0.5333 | -0.1186 | -0.0003 | 0.1333 | ok | RAN |
| SOLUSDT | 8 | `ema4320_below_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 0.9775 | 0.5385 | -0.1745 | -0.0005 | 0.1323 | ok | RAN |
| ETHUSDT | 4 | `ema4320_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9638 | 0.5569 | -0.2949 | -0.0012 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4320_above_at_h` | one_head_filter_pi_star | 22 | 6.8562 | 0.7117 | 0.4091 | -1.2554 | -0.0136 | 0.1818 | ok | RAN |
| ETHUSDT | 4 | `ema4320_above_at_h` | one_head_filter_pi_star | 38 | 11.0914 | 0.7318 | 0.4737 | -1.5963 | -0.0153 | 0.1579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4320_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4320_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
