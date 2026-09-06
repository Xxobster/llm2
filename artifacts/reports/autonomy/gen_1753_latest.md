# Autonomy public-indicator hunt gen 1753

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T100409Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3940_above_at_h` | one_head_filter_pi_star | 87 | 7.1356 | 1.6154 | 0.6437 | 1.6968 | 0.0085 | 0.1149 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3940_above_at_h` | one_head_filter_pi_star | 84 | 6.9053 | 1.4615 | 0.6429 | 1.3421 | 0.0071 | 0.0952 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema3940_below_at_h` | one_head_filter_pi_star | 291 | 23.7953 | 1.0003 | 0.5395 | 0.0023 | 0.0000 | 0.1340 | ok | RAN |
| SOLUSDT | 4 | `ema3940_below_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 0.9775 | 0.5380 | -0.1729 | -0.0005 | 0.1392 | ok | RAN |
| ETHUSDT | 4 | `ema3940_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9784 | 0.5581 | -0.1771 | -0.0007 | 0.1366 | ok | RAN |
| ETHUSDT | 8 | `ema3940_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9506 | 0.5536 | -0.4111 | -0.0016 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema3940_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.8411 | 0.5000 | -0.7710 | -0.0080 | 0.1765 | ok | RAN |
| ETHUSDT | 4 | `ema3940_above_at_h` | one_head_filter_pi_star | 27 | 8.1477 | 0.8148 | 0.4815 | -0.7765 | -0.0084 | 0.1481 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3940_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3940_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
