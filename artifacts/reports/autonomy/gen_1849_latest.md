# Autonomy public-indicator hunt gen 1849

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T184930Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4180_above_at_h` | one_head_filter_pi_star | 83 | 6.8231 | 1.7936 | 0.6386 | 2.0180 | 0.0107 | 0.0964 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4180_above_at_h` | one_head_filter_pi_star | 91 | 7.4637 | 1.4660 | 0.6264 | 1.4086 | 0.0066 | 0.0879 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4180_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 1.0071 | 0.5443 | 0.0544 | 0.0001 | 0.1329 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema4180_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.9981 | 0.5161 | -0.0081 | -0.0001 | 0.1613 | ok | RAN |
| ETHUSDT | 4 | `ema4180_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9935 | 0.5595 | -0.0512 | -0.0002 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `ema4180_below_at_h` | one_head_filter_pi_star | 303 | 24.7766 | 0.9737 | 0.5314 | -0.1991 | -0.0005 | 0.1419 | ok | RAN |
| ETHUSDT | 8 | `ema4180_below_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 0.9738 | 0.5600 | -0.2176 | -0.0009 | 0.1343 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4180_above_at_h` | one_head_filter_pi_star | 40 | 11.8025 | 0.7157 | 0.4750 | -1.7310 | -0.0152 | 0.1500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4180_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4180_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
