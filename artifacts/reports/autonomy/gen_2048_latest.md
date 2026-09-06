# Autonomy public-indicator hunt gen 2048

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T144925Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma4720_above_at_h` | one_head_filter_pi_star | 55 | 5.0864 | 1.5929 | 0.5818 | 1.3022 | 0.0083 | 0.1273 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma4720_above_at_h` | one_head_filter_pi_star | 58 | 4.8828 | 1.2941 | 0.5690 | 0.7641 | 0.0047 | 0.1207 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma4720_below_at_h` | one_head_filter_pi_star | 302 | 24.6948 | 0.9950 | 0.5430 | -0.0367 | -0.0001 | 0.1358 | ok | RAN |
| SOLUSDT | 4 | `sma4720_below_at_h` | one_head_filter_pi_star | 312 | 25.3818 | 0.9769 | 0.5385 | -0.1779 | -0.0005 | 0.1346 | ok | RAN |
| ETHUSDT | 8 | `sma4720_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9814 | 0.5565 | -0.1459 | -0.0006 | 0.1369 | ok | RAN |
| ETHUSDT | 4 | `sma4720_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9499 | 0.5519 | -0.4041 | -0.0017 | 0.1365 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma4720_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 0.8359 | 0.5000 | -0.7645 | -0.0083 | 0.1667 | ok | RAN |
| ETHUSDT | 4 | `sma4720_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.7637 | 0.4706 | -1.2475 | -0.0133 | 0.1471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4720_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4720_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
