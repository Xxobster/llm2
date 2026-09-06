# Autonomy public-indicator hunt gen 1402

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T060015Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1256_pos_at_h` | one_head_filter_pi_star | 16 | 1.8243 | 2.6097 | 0.7500 | 1.8034 | 0.0202 | 0.4375 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1256_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.7586 | 0.6606 | 4.4264 | 0.0189 | 0.3152 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1256_neg_at_h` | one_head_filter_pi_star | 319 | 25.9513 | 1.7477 | 0.6552 | 4.2744 | 0.0184 | 0.3229 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1256_neg_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.7320 | 0.6401 | 4.3122 | 0.0114 | 0.3245 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1256_neg_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.6711 | 0.6308 | 4.0982 | 0.0106 | 0.3256 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1256_pos_at_h` | one_head_filter_pi_star | 54 | 4.7631 | 0.9176 | 0.5370 | -0.2808 | -0.0038 | 0.2222 | ok | RAN |
| BTCUSDT | 8 | `ret1256_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5979 | 0.2778 | -0.7871 | -0.0304 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1256_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4048 | 0.2353 | -1.2585 | -0.0474 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1256_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret1256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1256_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1256_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1256_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
