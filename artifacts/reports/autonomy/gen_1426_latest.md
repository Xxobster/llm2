# Autonomy public-indicator hunt gen 1426

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T122705Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1280_pos_at_h` | one_head_filter_pi_star | 16 | 1.5713 | 2.7742 | 0.7500 | 1.7024 | 0.0179 | 0.3125 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1280_neg_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.6165 | 0.6491 | 3.7641 | 0.0164 | 0.3041 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1280_neg_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.6075 | 0.6509 | 3.8197 | 0.0163 | 0.3107 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1280_pos_at_h` | one_head_filter_pi_star | 39 | 3.2414 | 2.0174 | 0.7179 | 1.7637 | 0.0137 | 0.3077 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1280_neg_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.8181 | 0.6422 | 4.4885 | 0.0121 | 0.3150 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1280_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.7365 | 0.6350 | 4.2789 | 0.0111 | 0.3116 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1280_pos_at_h` | one_head_filter_pi_star | 46 | 4.2309 | 1.2010 | 0.5652 | 0.5714 | 0.0083 | 0.2826 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1280_pos_at_h` | one_head_filter_pi_star | 30 | 2.7761 | 0.8939 | 0.5000 | -0.2770 | -0.0045 | 0.2333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1280_pos_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.7003 | 0.3333 | -0.6194 | -0.0272 | 0.0952 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1280_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0503 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1280_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1280_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
