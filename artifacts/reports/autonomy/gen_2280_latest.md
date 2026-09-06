# Autonomy public-indicator hunt gen 2280

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T221707Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5300_above_at_h` | one_head_filter_pi_star | 45 | 4.2251 | 2.4859 | 0.6667 | 2.3399 | 0.0184 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `sma5300_above_at_h` | one_head_filter_pi_star | 56 | 4.7685 | 2.0150 | 0.6429 | 1.9515 | 0.0137 | 0.1071 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5300_above_at_h` | one_head_filter_pi_star | 26 | 7.8459 | 1.0705 | 0.5769 | 0.2789 | 0.0029 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5300_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9849 | 0.5594 | -0.1227 | -0.0005 | 0.1333 | ok | RAN |
| SOLUSDT | 8 | `sma5300_below_at_h` | one_head_filter_pi_star | 291 | 23.6734 | 0.9657 | 0.5326 | -0.2514 | -0.0007 | 0.1375 | ok | RAN |
| SOLUSDT | 4 | `sma5300_below_at_h` | one_head_filter_pi_star | 301 | 24.4869 | 0.9560 | 0.5316 | -0.3332 | -0.0009 | 0.1329 | ok | RAN |
| ETHUSDT | 8 | `sma5300_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9628 | 0.5552 | -0.2988 | -0.0012 | 0.1343 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5300_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.9041 | 0.5294 | -0.4434 | -0.0046 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
