# Autonomy public-indicator hunt gen 1154

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T052701Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1008_neg_at_h` | one_head_filter_pi_star | 282 | 23.0368 | 1.7035 | 0.6560 | 3.8876 | 0.0176 | 0.3369 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1008_neg_at_h` | one_head_filter_pi_star | 262 | 21.4030 | 1.6364 | 0.6489 | 3.4708 | 0.0166 | 0.3435 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1008_neg_at_h` | one_head_filter_pi_star | 274 | 22.4052 | 1.7698 | 0.6350 | 3.8935 | 0.0120 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1008_neg_at_h` | one_head_filter_pi_star | 282 | 23.0594 | 1.7798 | 0.6418 | 3.9461 | 0.0120 | 0.3262 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret1008_pos_at_h` | one_head_filter_pi_star | 49 | 4.0725 | 1.6816 | 0.6939 | 1.6674 | 0.0093 | 0.2653 | ok | RAN |
| SOLUSDT | 4 | `ret1008_pos_at_h` | one_head_filter_pi_star | 67 | 5.5689 | 1.4694 | 0.6418 | 1.3438 | 0.0074 | 0.2985 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1008_pos_at_h` | one_head_filter_pi_star | 76 | 6.5061 | 0.9868 | 0.5526 | -0.0516 | -0.0006 | 0.1974 | ok | RAN |
| ETHUSDT | 8 | `ret1008_pos_at_h` | one_head_filter_pi_star | 62 | 5.3076 | 0.9339 | 0.5484 | -0.2427 | -0.0032 | 0.2097 | ok | RAN |
| BTCUSDT | 8 | `ret1008_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4083 | 0.2667 | -1.2405 | -0.0505 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1008_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.1084 | 0.2000 | -2.3636 | -0.1002 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1008_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1008_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1008_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1008_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1008_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1008_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1008_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1008_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1008_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1008_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1008_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1008_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1008_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1008_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
