# Autonomy public-indicator hunt gen 1705

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T052626Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3820_above_at_h` | one_head_filter_pi_star | 85 | 6.9716 | 2.1384 | 0.6941 | 2.5757 | 0.0123 | 0.0941 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3820_above_at_h` | one_head_filter_pi_star | 62 | 5.0968 | 1.5404 | 0.6452 | 1.3290 | 0.0075 | 0.1290 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3820_below_at_h` | one_head_filter_pi_star | 294 | 24.0406 | 1.0308 | 0.5408 | 0.2213 | 0.0006 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `ema3820_below_at_h` | one_head_filter_pi_star | 313 | 25.4632 | 1.0217 | 0.5431 | 0.1610 | 0.0004 | 0.1278 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema3820_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9785 | 0.5569 | -0.1727 | -0.0007 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `ema3820_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9732 | 0.5572 | -0.2181 | -0.0009 | 0.1320 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema3820_above_at_h` | one_head_filter_pi_star | 35 | 4.1128 | 0.8615 | 0.5143 | -0.4217 | -0.0069 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3820_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3820_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3820_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
