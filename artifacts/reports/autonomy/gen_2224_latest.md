# Autonomy public-indicator hunt gen 2224

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T153421Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5160_above_at_h` | one_head_filter_pi_star | 53 | 4.4515 | 1.7235 | 0.5849 | 1.4650 | 0.0104 | 0.0943 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5160_above_at_h` | one_head_filter_pi_star | 57 | 4.8537 | 1.6012 | 0.6140 | 1.3219 | 0.0086 | 0.1228 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma5160_below_at_h` | one_head_filter_pi_star | 313 | 25.4632 | 0.9868 | 0.5399 | -0.1000 | -0.0003 | 0.1310 | ok | RAN |
| ETHUSDT | 4 | `sma5160_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9758 | 0.5565 | -0.1936 | -0.0008 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `sma5160_below_at_h` | one_head_filter_pi_star | 312 | 25.3818 | 0.9615 | 0.5288 | -0.2959 | -0.0008 | 0.1314 | ok | RAN |
| ETHUSDT | 8 | `sma5160_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 0.9512 | 0.5526 | -0.3956 | -0.0016 | 0.1321 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5160_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.9057 | 0.5294 | -0.4526 | -0.0048 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma5160_above_at_h` | one_head_filter_pi_star | 40 | 11.8025 | 0.6257 | 0.4500 | -2.3677 | -0.0242 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `sma5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5160_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5160_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
