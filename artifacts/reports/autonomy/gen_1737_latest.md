# Autonomy public-indicator hunt gen 1737

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T083830Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema3900_above_at_h` | one_head_filter_pi_star | 85 | 6.9749 | 1.5794 | 0.6706 | 1.6356 | 0.0078 | 0.1059 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3900_above_at_h` | one_head_filter_pi_star | 90 | 7.3817 | 1.3091 | 0.6000 | 1.0194 | 0.0045 | 0.1111 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema3900_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 1.0120 | 0.5632 | 0.0963 | 0.0004 | 0.1351 | ok | RAN |
| SOLUSDT | 8 | `ema3900_below_at_h` | one_head_filter_pi_star | 305 | 24.8124 | 1.0049 | 0.5344 | 0.0366 | 0.0001 | 0.1311 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema3900_below_at_h` | one_head_filter_pi_star | 312 | 25.5125 | 0.9623 | 0.5353 | -0.2884 | -0.0008 | 0.1346 | ok | RAN |
| ETHUSDT | 8 | `ema3900_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9759 | 0.5578 | -0.1961 | -0.0008 | 0.1329 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema3900_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.8239 | 0.5000 | -0.8685 | -0.0085 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3900_above_at_h` | one_head_filter_pi_star | 33 | 9.9583 | 0.6721 | 0.4545 | -1.8976 | -0.0167 | 0.1212 | ok | RAN |
| ETHUSDT | 4 | `ema3900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3900_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3900_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
