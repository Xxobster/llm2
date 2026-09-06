# Autonomy public-indicator hunt gen 2468

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T214213Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1104_above_at_h` | one_head_filter_pi_star | 103 | 8.3987 | 1.3330 | 0.6214 | 1.1936 | 0.0054 | 0.1456 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1104_above_at_h` | one_head_filter_pi_star | 101 | 8.2356 | 1.2840 | 0.6040 | 1.0502 | 0.0046 | 0.1386 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1104_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 0.9858 | 0.5475 | -0.0993 | -0.0003 | 0.1293 | ok | RAN |
| SOLUSDT | 8 | `ema1104_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 0.9579 | 0.5407 | -0.2886 | -0.0009 | 0.1301 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1104_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 0.9376 | 0.5450 | -0.4365 | -0.0019 | 0.1577 | ok | RAN |
| ETHUSDT | 8 | `ema1104_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 0.9390 | 0.5436 | -0.4453 | -0.0020 | 0.1494 | ok | RAN |
| ETHUSDT | 8 | `ema1104_above_at_h` | one_head_filter_pi_star | 103 | 8.5004 | 0.8857 | 0.5340 | -0.5133 | -0.0049 | 0.1165 | ok | RAN |
| ETHUSDT | 4 | `ema1104_above_at_h` | one_head_filter_pi_star | 117 | 9.6172 | 0.8600 | 0.5385 | -0.6494 | -0.0063 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1104_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1104_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0568 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1104_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1104_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1104_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1104_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1104_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1104_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1104_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1104_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1104_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1104_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1104_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1104_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1104_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1104_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
