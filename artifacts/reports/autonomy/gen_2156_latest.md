# Autonomy public-indicator hunt gen 2156

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T060136Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1063_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1063_above_at_h` | one_head_filter_pi_star | 104 | 8.5479 | 1.2978 | 0.6250 | 1.1620 | 0.0050 | 0.1346 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1063_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.1804 | 0.5948 | 0.7309 | 0.0031 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1063_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 0.9888 | 0.5556 | -0.0727 | -0.0003 | 0.1574 | ok | RAN |
| SOLUSDT | 4 | `ema1063_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9604 | 0.5426 | -0.2783 | -0.0009 | 0.1279 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema1063_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 0.9246 | 0.5339 | -0.5355 | -0.0017 | 0.1315 | ok | RAN |
| ETHUSDT | 8 | `ema1063_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9102 | 0.5381 | -0.6454 | -0.0029 | 0.1525 | ok | RAN |
| ETHUSDT | 4 | `ema1063_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 0.9281 | 0.5528 | -0.3313 | -0.0030 | 0.1220 | ok | RAN |
| ETHUSDT | 8 | `ema1063_above_at_h` | one_head_filter_pi_star | 114 | 9.4082 | 0.8619 | 0.5263 | -0.6513 | -0.0060 | 0.1228 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1063_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1063_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1063_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1063_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1063_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1063_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1063_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1063_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1063_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1063_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1063_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1063_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1063_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1063_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1063_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
