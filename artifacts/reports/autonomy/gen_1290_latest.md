# Autonomy public-indicator hunt gen 1290

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T191339Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1144_neg_at_h` | one_head_filter_pi_star | 312 | 25.4875 | 1.6696 | 0.6538 | 3.9191 | 0.0172 | 0.3237 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1144_neg_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.6410 | 0.6472 | 3.6851 | 0.0163 | 0.3107 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1144_neg_at_h` | one_head_filter_pi_star | 323 | 26.4120 | 1.7296 | 0.6378 | 4.1366 | 0.0112 | 0.3189 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1144_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.6938 | 0.6328 | 4.0557 | 0.0108 | 0.3254 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1144_pos_at_h` | one_head_filter_pi_star | 45 | 4.2849 | 1.1776 | 0.5778 | 0.4758 | 0.0082 | 0.2889 | ok | RAN |
| SOLUSDT | 8 | `ret1144_pos_at_h` | one_head_filter_pi_star | 13 | 1.1449 | 1.2225 | 0.5385 | 0.3356 | 0.0039 | 0.3077 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1144_pos_at_h` | one_head_filter_pi_star | 35 | 3.4363 | 1.0283 | 0.5143 | 0.0757 | 0.0013 | 0.3143 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1144_pos_at_h` | one_head_filter_pi_star | 21 | 1.8495 | 0.9989 | 0.5714 | -0.0022 | -0.0000 | 0.2381 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1144_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0712 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1144_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0740 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1144_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1144_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
