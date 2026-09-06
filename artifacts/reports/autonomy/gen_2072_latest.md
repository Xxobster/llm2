# Autonomy public-indicator hunt gen 2072

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T182414Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4780_above_at_h` | one_head_filter_pi_star | 41 | 3.4912 | 1.6037 | 0.5854 | 1.1498 | 0.0092 | 0.1220 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma4780_above_at_h` | one_head_filter_pi_star | 67 | 5.6273 | 1.4961 | 0.5821 | 1.2656 | 0.0074 | 0.0896 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma4780_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.0309 | 0.5638 | 0.2418 | 0.0010 | 0.1365 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma4780_below_at_h` | one_head_filter_pi_star | 308 | 25.0564 | 1.0036 | 0.5455 | 0.0275 | 0.0001 | 0.1331 | ok | RAN |
| SOLUSDT | 8 | `sma4780_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 0.9827 | 0.5370 | -0.1306 | -0.0004 | 0.1350 | ok | RAN |
| ETHUSDT | 8 | `sma4780_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9605 | 0.5519 | -0.3193 | -0.0013 | 0.1335 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4780_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.8091 | 0.5000 | -1.0880 | -0.0101 | 0.1316 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma4780_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.6857 | 0.4737 | -1.9476 | -0.0173 | 0.1316 | ok | RAN |
| ETHUSDT | 4 | `sma4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4780_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4780_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
