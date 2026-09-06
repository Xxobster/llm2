# Autonomy public-indicator hunt gen 1258

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T160743Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1112_neg_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.6801 | 0.6505 | 3.9287 | 0.0171 | 0.3301 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1112_neg_at_h` | one_head_filter_pi_star | 310 | 25.2191 | 1.6630 | 0.6484 | 3.8481 | 0.0168 | 0.3258 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1112_neg_at_h` | one_head_filter_pi_star | 300 | 24.5313 | 1.7888 | 0.6400 | 4.1256 | 0.0122 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1112_neg_at_h` | one_head_filter_pi_star | 296 | 24.2042 | 1.7251 | 0.6318 | 3.8898 | 0.0115 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret1112_pos_at_h` | one_head_filter_pi_star | 20 | 2.1236 | 1.1745 | 0.6000 | 0.3551 | 0.0034 | 0.3500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1112_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6262 | 0.3333 | -0.7003 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1112_pos_at_h` | one_head_filter_pi_star | 17 | 1.6690 | 0.4667 | 0.3529 | -1.3851 | -0.0431 | 0.2941 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1112_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3092 | 0.2353 | -1.6326 | -0.0721 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1112_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1112_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret1112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1112_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1112_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
