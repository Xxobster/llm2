# Autonomy public-indicator hunt gen 1386

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T042024Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1240_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.7692 | 0.6585 | 4.4194 | 0.0191 | 0.3169 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1240_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.6941 | 0.6559 | 4.1954 | 0.0178 | 0.3088 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1240_neg_at_h` | one_head_filter_pi_star | 356 | 28.9613 | 1.7493 | 0.6433 | 4.4236 | 0.0115 | 0.3118 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1240_neg_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.7375 | 0.6337 | 4.4179 | 0.0114 | 0.3227 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1240_pos_at_h` | one_head_filter_pi_star | 34 | 3.3381 | 0.7886 | 0.5000 | -0.6564 | -0.0105 | 0.3235 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1240_pos_at_h` | one_head_filter_pi_star | 49 | 4.5867 | 0.7110 | 0.4898 | -1.0861 | -0.0168 | 0.2245 | ok | RAN |
| BTCUSDT | 4 | `ret1240_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3142 | 0.2222 | -1.6016 | -0.0667 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1240_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3008 | 0.2222 | -1.6957 | -0.0698 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1240_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1240_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1240_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1240_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
