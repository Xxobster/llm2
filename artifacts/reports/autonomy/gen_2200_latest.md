# Autonomy public-indicator hunt gen 2200

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T123244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5100_above_at_h` | one_head_filter_pi_star | 44 | 3.7467 | 2.0989 | 0.6136 | 1.8061 | 0.0141 | 0.0682 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma5100_above_at_h` | one_head_filter_pi_star | 66 | 5.5433 | 1.9488 | 0.6364 | 2.0735 | 0.0135 | 0.0909 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5100_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9873 | 0.5588 | -0.1014 | -0.0004 | 0.1353 | ok | RAN |
| SOLUSDT | 8 | `sma5100_below_at_h` | one_head_filter_pi_star | 294 | 23.9175 | 0.9719 | 0.5306 | -0.2070 | -0.0006 | 0.1327 | ok | RAN |
| ETHUSDT | 8 | `sma5100_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9793 | 0.5565 | -0.1655 | -0.0007 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `sma5100_below_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 0.9636 | 0.5329 | -0.2754 | -0.0008 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5100_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.9066 | 0.5294 | -0.4272 | -0.0044 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma5100_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.6770 | 0.4737 | -1.8357 | -0.0197 | 0.1842 | ok | RAN |
| ETHUSDT | 4 | `sma5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5100_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5100_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
