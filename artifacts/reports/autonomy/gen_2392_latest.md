# Autonomy public-indicator hunt gen 2392

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T125335Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5580_above_at_h` | one_head_filter_pi_star | 60 | 5.1091 | 1.8713 | 0.6333 | 1.8375 | 0.0127 | 0.1000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5580_above_at_h` | one_head_filter_pi_star | 52 | 4.4279 | 1.8982 | 0.6346 | 1.7280 | 0.0115 | 0.1346 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5580_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 0.9872 | 0.5586 | -0.1032 | -0.0004 | 0.1291 | ok | RAN |
| SOLUSDT | 4 | `sma5580_below_at_h` | one_head_filter_pi_star | 322 | 26.1953 | 0.9773 | 0.5373 | -0.1765 | -0.0005 | 0.1273 | ok | RAN |
| SOLUSDT | 8 | `sma5580_below_at_h` | one_head_filter_pi_star | 319 | 25.9513 | 0.9745 | 0.5329 | -0.1985 | -0.0005 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `sma5580_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9696 | 0.5569 | -0.2507 | -0.0010 | 0.1312 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5580_above_at_h` | one_head_filter_pi_star | 33 | 9.6320 | 0.8014 | 0.5152 | -1.1158 | -0.0101 | 0.1212 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5580_above_at_h` | one_head_filter_pi_star | 42 | 12.3926 | 0.6973 | 0.4762 | -1.9893 | -0.0180 | 0.1667 | ok | RAN |
| ETHUSDT | 4 | `sma5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5580_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5580_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
