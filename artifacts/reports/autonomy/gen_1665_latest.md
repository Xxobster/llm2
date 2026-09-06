# Autonomy public-indicator hunt gen 1665

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T003132Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema3720_above_at_h` | one_head_filter_pi_star | 90 | 7.3817 | 1.7824 | 0.6667 | 2.0887 | 0.0101 | 0.1000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3720_above_at_h` | one_head_filter_pi_star | 84 | 6.8505 | 1.4552 | 0.6190 | 1.3067 | 0.0058 | 0.1071 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3720_below_at_h` | one_head_filter_pi_star | 300 | 24.4056 | 1.0434 | 0.5467 | 0.3155 | 0.0009 | 0.1300 | ok | RAN |
| SOLUSDT | 4 | `ema3720_below_at_h` | one_head_filter_pi_star | 289 | 23.6318 | 1.0250 | 0.5398 | 0.1793 | 0.0005 | 0.1315 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema3720_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9854 | 0.5579 | -0.1158 | -0.0005 | 0.1365 | ok | RAN |
| ETHUSDT | 4 | `ema3720_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9661 | 0.5569 | -0.2744 | -0.0011 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema3720_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.7755 | 0.5000 | -1.2744 | -0.0117 | 0.1471 | ok | RAN |
| ETHUSDT | 8 | `ema3720_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.7388 | 0.5000 | -1.4647 | -0.0141 | 0.1562 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3720_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3720_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
