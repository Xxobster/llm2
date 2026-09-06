# Autonomy public-indicator hunt gen 2176

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T090708Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5040_above_at_h` | one_head_filter_pi_star | 50 | 4.1995 | 1.8209 | 0.5600 | 1.5549 | 0.0108 | 0.0800 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5040_above_at_h` | one_head_filter_pi_star | 57 | 4.7874 | 1.5556 | 0.5789 | 1.2638 | 0.0081 | 0.1053 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5040_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9880 | 0.5582 | -0.0947 | -0.0004 | 0.1343 | ok | RAN |
| ETHUSDT | 4 | `sma5040_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 0.9788 | 0.5559 | -0.1707 | -0.0007 | 0.1329 | ok | RAN |
| SOLUSDT | 4 | `sma5040_below_at_h` | one_head_filter_pi_star | 298 | 24.2429 | 0.9653 | 0.5336 | -0.2592 | -0.0007 | 0.1342 | ok | RAN |
| SOLUSDT | 8 | `sma5040_below_at_h` | one_head_filter_pi_star | 296 | 24.2042 | 0.9645 | 0.5372 | -0.2614 | -0.0007 | 0.1385 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5040_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.7749 | 0.5000 | -1.3510 | -0.0121 | 0.1667 | ok | RAN |
| ETHUSDT | 8 | `sma5040_above_at_h` | one_head_filter_pi_star | 33 | 9.7370 | 0.7489 | 0.4848 | -1.4847 | -0.0131 | 0.1212 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5040_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5040_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
