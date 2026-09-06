# Autonomy public-indicator hunt gen 1250

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T152130Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1104_neg_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7716 | 0.6602 | 4.3334 | 0.0190 | 0.3139 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1104_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.6746 | 0.6519 | 3.9235 | 0.0173 | 0.3228 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1104_neg_at_h` | one_head_filter_pi_star | 308 | 25.0564 | 1.8392 | 0.6429 | 4.4031 | 0.0127 | 0.3149 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1104_pos_at_h` | one_head_filter_pi_star | 26 | 2.4082 | 1.8914 | 0.6923 | 1.6213 | 0.0112 | 0.2308 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1104_neg_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 1.7051 | 0.6352 | 3.9879 | 0.0111 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1104_pos_at_h` | one_head_filter_pi_star | 28 | 2.3570 | 1.3363 | 0.6429 | 0.6674 | 0.0054 | 0.2857 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1104_pos_at_h` | one_head_filter_pi_star | 45 | 4.4180 | 0.9316 | 0.5111 | -0.2217 | -0.0038 | 0.2222 | ok | RAN |
| ETHUSDT | 8 | `ret1104_pos_at_h` | one_head_filter_pi_star | 18 | 1.7672 | 0.9259 | 0.5000 | -0.1480 | -0.0039 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1104_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4219 | 0.2857 | -1.1743 | -0.0497 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1104_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3092 | 0.2353 | -1.6326 | -0.0721 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1104_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1104_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
