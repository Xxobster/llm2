# Autonomy public-indicator hunt gen 2456

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T202108Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5740_above_at_h` | one_head_filter_pi_star | 39 | 3.6618 | 2.3158 | 0.6667 | 2.0487 | 0.0188 | 0.1282 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma5740_above_at_h` | one_head_filter_pi_star | 54 | 4.8315 | 1.5210 | 0.6296 | 1.2218 | 0.0089 | 0.1296 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5740_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9909 | 0.5592 | -0.0738 | -0.0003 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `sma5740_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9763 | 0.5565 | -0.1927 | -0.0008 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `sma5740_below_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 0.9517 | 0.5382 | -0.3977 | -0.0010 | 0.1303 | ok | RAN |
| SOLUSDT | 8 | `sma5740_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9516 | 0.5343 | -0.3870 | -0.0010 | 0.1254 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5740_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.8553 | 0.5000 | -0.7006 | -0.0067 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma5740_above_at_h` | one_head_filter_pi_star | 41 | 12.0975 | 0.6651 | 0.4634 | -2.2001 | -0.0207 | 0.1463 | ok | RAN |
| ETHUSDT | 4 | `sma5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
