# Autonomy public-indicator hunt gen 1266

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T165252Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1120_neg_at_h` | one_head_filter_pi_star | 306 | 24.9974 | 1.6719 | 0.6503 | 3.8739 | 0.0169 | 0.3301 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1120_neg_at_h` | one_head_filter_pi_star | 308 | 25.0564 | 1.6297 | 0.6494 | 3.7108 | 0.0161 | 0.3279 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1120_pos_at_h` | one_head_filter_pi_star | 29 | 2.4107 | 2.2005 | 0.7241 | 1.7619 | 0.0137 | 0.2759 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1120_neg_at_h` | one_head_filter_pi_star | 303 | 24.6496 | 1.7754 | 0.6370 | 4.1713 | 0.0118 | 0.3168 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1120_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.7381 | 0.6364 | 4.2233 | 0.0113 | 0.3303 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1120_pos_at_h` | one_head_filter_pi_star | 54 | 5.0547 | 1.0559 | 0.5556 | 0.1799 | 0.0026 | 0.2037 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1120_pos_at_h` | one_head_filter_pi_star | 11 | 0.9790 | 0.8439 | 0.4545 | -0.2475 | -0.0029 | 0.2727 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1120_pos_at_h` | one_head_filter_pi_star | 37 | 3.5231 | 0.7767 | 0.5135 | -0.6823 | -0.0111 | 0.1892 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1120_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0502 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1120_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1120_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1120_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1120_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1120_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
