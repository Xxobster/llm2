# Autonomy public-indicator hunt gen 1658

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T235509Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1512_pos_at_h` | one_head_filter_pi_star | 14 | 1.5613 | 2.6194 | 0.7143 | 1.6834 | 0.0279 | 0.2143 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1512_pos_at_h` | one_head_filter_pi_star | 18 | 1.6052 | 1.7186 | 0.6667 | 1.0212 | 0.0120 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1512_pos_at_h` | one_head_filter_pi_star | 20 | 6.0353 | 1.2449 | 0.5000 | 0.8177 | 0.0089 | 0.0500 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1512_neg_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 0.9957 | 0.5422 | -0.0332 | -0.0001 | 0.1235 | ok | RAN |
| SOLUSDT | 8 | `ret1512_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9894 | 0.5463 | -0.0844 | -0.0002 | 0.1373 | ok | RAN |
| ETHUSDT | 8 | `ret1512_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9532 | 0.5519 | -0.3903 | -0.0015 | 0.1395 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1512_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9311 | 0.5471 | -0.5642 | -0.0023 | 0.1398 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1512_pos_at_h` | one_head_filter_pi_star | 12 | 3.6212 | 0.6382 | 0.4167 | -1.3363 | -0.0185 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1512_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.6801 | 0.3077 | -0.5337 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1512_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4290 | 0.2222 | -1.2830 | -0.0621 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1512_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1512_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
