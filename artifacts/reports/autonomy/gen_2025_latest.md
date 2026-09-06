# Autonomy public-indicator hunt gen 2025

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T120616Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4620_above_at_h` | one_head_filter_pi_star | 68 | 5.5900 | 1.6434 | 0.6176 | 1.5658 | 0.0095 | 0.1029 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4620_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 1.6734 | 0.6562 | 1.6075 | 0.0092 | 0.1094 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema4620_above_at_h` | one_head_filter_pi_star | 36 | 10.5076 | 1.0069 | 0.5556 | 0.0327 | 0.0003 | 0.1389 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4620_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9892 | 0.5399 | -0.0835 | -0.0002 | 0.1288 | ok | RAN |
| SOLUSDT | 4 | `ema4620_below_at_h` | one_head_filter_pi_star | 329 | 26.9026 | 0.9725 | 0.5380 | -0.2166 | -0.0006 | 0.1337 | ok | RAN |
| ETHUSDT | 8 | `ema4620_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9604 | 0.5569 | -0.3246 | -0.0013 | 0.1370 | ok | RAN |
| ETHUSDT | 4 | `ema4620_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9599 | 0.5559 | -0.3299 | -0.0013 | 0.1324 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4620_above_at_h` | one_head_filter_pi_star | 35 | 10.3272 | 0.8163 | 0.4857 | -0.9266 | -0.0101 | 0.1714 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4620_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4620_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
