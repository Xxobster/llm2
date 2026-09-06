# Autonomy public-indicator hunt gen 1314

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T214043Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1168_neg_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.6482 | 0.6519 | 3.8822 | 0.0169 | 0.3068 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1168_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.6418 | 0.6545 | 3.8831 | 0.0166 | 0.3091 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1168_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 1.7230 | 0.6322 | 4.1250 | 0.0109 | 0.3191 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1168_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.7083 | 0.6266 | 3.9297 | 0.0109 | 0.3196 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1168_pos_at_h` | one_head_filter_pi_star | 14 | 1.2029 | 1.4960 | 0.6429 | 0.6184 | 0.0081 | 0.2143 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1168_pos_at_h` | one_head_filter_pi_star | 39 | 3.8290 | 0.9409 | 0.5128 | -0.1779 | -0.0028 | 0.2308 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1168_pos_at_h` | one_head_filter_pi_star | 52 | 4.7828 | 0.9265 | 0.4808 | -0.2457 | -0.0036 | 0.2115 | ok | RAN |
| BTCUSDT | 4 | `ret1168_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4048 | 0.2353 | -1.2585 | -0.0474 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1168_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0686 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1168_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1168_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1168_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
