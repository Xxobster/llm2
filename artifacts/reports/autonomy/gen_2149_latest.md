# Autonomy public-indicator hunt gen 2149

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T045431Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret350_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.2439 | 0.5978 | 1.3471 | 0.0075 | 0.2067 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret350_pos_at_h` | one_head_filter_pi_star | 159 | 12.9649 | 1.3403 | 0.5975 | 1.5317 | 0.0056 | 0.1132 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret350_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1420 | 0.5882 | 0.8111 | 0.0043 | 0.1941 | ok | RAN |
| SOLUSDT | 8 | `ret350_pos_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.2441 | 0.5733 | 1.1320 | 0.0041 | 0.1200 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret350_neg_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9754 | 0.5631 | -0.1530 | -0.0005 | 0.1311 | ok | RAN |
| SOLUSDT | 4 | `ret350_neg_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 0.9293 | 0.5442 | -0.4846 | -0.0015 | 0.1395 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret350_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 0.8298 | 0.5465 | -1.0056 | -0.0071 | 0.1047 | ok | RAN |
| ETHUSDT | 4 | `ret350_pos_at_h` | one_head_filter_pi_star | 209 | 17.1232 | 0.7878 | 0.5359 | -1.3512 | -0.0090 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret350_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret350_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0759 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret350_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret350_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret350_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret350_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret350_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret350_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret350_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret350_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret350_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret350_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret350_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret350_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret350_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret350_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
