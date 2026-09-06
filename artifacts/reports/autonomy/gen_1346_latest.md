# Autonomy public-indicator hunt gen 1346

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T003810Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1200_neg_at_h` | one_head_filter_pi_star | 305 | 24.8124 | 1.7074 | 0.6525 | 3.9290 | 0.0173 | 0.3213 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1200_neg_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 1.6721 | 0.6509 | 3.9405 | 0.0172 | 0.3176 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1200_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.7500 | 0.6399 | 4.2592 | 0.0117 | 0.3274 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret1200_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.6205 | 0.6288 | 3.6203 | 0.0099 | 0.3190 | ok | RAN |
| SOLUSDT | 4 | `ret1200_pos_at_h` | one_head_filter_pi_star | 12 | 1.0430 | 1.1706 | 0.6667 | 0.2482 | 0.0030 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1200_pos_at_h` | one_head_filter_pi_star | 55 | 4.9752 | 0.9849 | 0.5455 | -0.0514 | -0.0008 | 0.2182 | ok | RAN |
| ETHUSDT | 8 | `ret1200_pos_at_h` | one_head_filter_pi_star | 34 | 3.2798 | 0.7943 | 0.5000 | -0.6001 | -0.0098 | 0.2647 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1200_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6452 | 0.3333 | -0.6698 | -0.0272 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1200_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5849 | 0.3000 | -0.8836 | -0.0397 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1200_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1200_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1200_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1200_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1200_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
