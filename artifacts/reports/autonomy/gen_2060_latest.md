# Autonomy public-indicator hunt gen 2060

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T164244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1050_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1050_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1050_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.3896 | 0.6293 | 1.4951 | 0.0064 | 0.1379 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1050_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.1604 | 0.5798 | 0.6860 | 0.0029 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1050_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 0.9789 | 0.5407 | -0.1427 | -0.0004 | 0.1220 | ok | RAN |
| ETHUSDT | 4 | `ema1050_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9518 | 0.5471 | -0.3275 | -0.0015 | 0.1525 | ok | RAN |
| ETHUSDT | 8 | `ema1050_above_at_h` | one_head_filter_pi_star | 122 | 10.0282 | 0.9633 | 0.5492 | -0.1683 | -0.0015 | 0.1311 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1050_above_at_h` | one_head_filter_pi_star | 133 | 10.9753 | 0.9585 | 0.5564 | -0.1954 | -0.0017 | 0.1128 | ok | RAN |
| ETHUSDT | 8 | `ema1050_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 0.9286 | 0.5432 | -0.5161 | -0.0023 | 0.1481 | ok | RAN |
| SOLUSDT | 4 | `ema1050_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 0.8775 | 0.5289 | -0.8530 | -0.0027 | 0.1364 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1050_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1050_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1050_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1050_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1050_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1050_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1050_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1050_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1050_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1050_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1050_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1050_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1050_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1050_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
