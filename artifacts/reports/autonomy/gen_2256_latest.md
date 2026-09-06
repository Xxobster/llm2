# Autonomy public-indicator hunt gen 2256

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T192219Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5240_above_at_h` | one_head_filter_pi_star | 47 | 4.4129 | 2.4760 | 0.6596 | 2.3310 | 0.0168 | 0.1064 | ok | RAN |
| SOLUSDT | 4 | `sma5240_above_at_h` | one_head_filter_pi_star | 44 | 3.7467 | 2.1840 | 0.6591 | 1.8503 | 0.0153 | 0.1136 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5240_above_at_h` | one_head_filter_pi_star | 26 | 7.8459 | 1.1621 | 0.5769 | 0.6065 | 0.0065 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma5240_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 0.9829 | 0.5375 | -0.1277 | -0.0004 | 0.1336 | ok | RAN |
| SOLUSDT | 4 | `sma5240_below_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 0.9800 | 0.5382 | -0.1567 | -0.0004 | 0.1284 | ok | RAN |
| ETHUSDT | 8 | `sma5240_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9839 | 0.5582 | -0.1284 | -0.0005 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `sma5240_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9624 | 0.5569 | -0.3096 | -0.0012 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5240_above_at_h` | one_head_filter_pi_star | 39 | 11.3833 | 0.7758 | 0.4872 | -1.3434 | -0.0129 | 0.1795 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5240_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5240_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
