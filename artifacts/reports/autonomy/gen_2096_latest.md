# Autonomy public-indicator hunt gen 2096

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T213607Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma4840_above_at_h` | one_head_filter_pi_star | 58 | 4.8714 | 1.5626 | 0.5862 | 1.2631 | 0.0084 | 0.0862 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma4840_above_at_h` | one_head_filter_pi_star | 50 | 4.6240 | 1.6040 | 0.5800 | 1.2918 | 0.0081 | 0.1000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma4840_below_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 1.0039 | 0.5472 | 0.0293 | 0.0001 | 0.1321 | ok | RAN |
| SOLUSDT | 8 | `sma4840_below_at_h` | one_head_filter_pi_star | 297 | 24.2859 | 0.9912 | 0.5354 | -0.0646 | -0.0002 | 0.1414 | ok | RAN |
| ETHUSDT | 4 | `sma4840_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9830 | 0.5565 | -0.1341 | -0.0005 | 0.1339 | ok | RAN |
| ETHUSDT | 8 | `sma4840_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9677 | 0.5552 | -0.2604 | -0.0011 | 0.1343 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4840_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.8610 | 0.5135 | -0.8074 | -0.0071 | 0.1081 | ok | RAN |
| ETHUSDT | 8 | `sma4840_above_at_h` | one_head_filter_pi_star | 33 | 9.7370 | 0.8303 | 0.5152 | -0.8308 | -0.0086 | 0.1515 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4840_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4840_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
