# Autonomy public-indicator hunt gen 1698

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T044108Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1552_pos_at_h` | one_head_filter_pi_star | 13 | 1.6380 | 1.0183 | 0.6154 | 0.0354 | 0.0003 | 0.1538 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1552_neg_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.0088 | 0.5465 | 0.0679 | 0.0002 | 0.1321 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1552_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9900 | 0.5433 | -0.0779 | -0.0002 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1552_neg_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9209 | 0.5473 | -0.6519 | -0.0026 | 0.1391 | ok | RAN |
| ETHUSDT | 8 | `ret1552_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.8735 | 0.5371 | -1.0715 | -0.0044 | 0.1365 | ok | RAN |
| ETHUSDT | 8 | `ret1552_pos_at_h` | one_head_filter_pi_star | 21 | 2.4677 | 0.7726 | 0.4762 | -0.6095 | -0.0148 | 0.2381 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1552_pos_at_h` | one_head_filter_pi_star | 15 | 4.5265 | 0.6747 | 0.4667 | -1.2071 | -0.0215 | 0.2000 | ok | RAN |
| BTCUSDT | 8 | `ret1552_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.6759 | 0.3077 | -0.5439 | -0.0292 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1552_pos_at_h` | one_head_filter_pi_star | 11 | 1.1554 | 0.3229 | 0.2727 | -1.6063 | -0.0760 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1552_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret1552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1552_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1552_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
