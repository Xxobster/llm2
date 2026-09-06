# Autonomy public-indicator hunt gen 1498

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T023702Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1352_pos_at_h` | one_head_filter_pi_star | 21 | 1.7457 | 3.6402 | 0.7619 | 2.2945 | 0.0245 | 0.2381 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1352_pos_at_h` | one_head_filter_pi_star | 31 | 2.5769 | 3.1424 | 0.7419 | 2.5137 | 0.0209 | 0.2903 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1352_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.6233 | 0.6441 | 3.8450 | 0.0166 | 0.3059 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1352_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5796 | 0.6458 | 3.5148 | 0.0156 | 0.3036 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1352_neg_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.7690 | 0.6426 | 4.3390 | 0.0114 | 0.3153 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1352_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.7085 | 0.6380 | 4.1269 | 0.0109 | 0.3175 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1352_pos_at_h` | one_head_filter_pi_star | 21 | 2.0618 | 1.2731 | 0.5714 | 0.5428 | 0.0100 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1352_pos_at_h` | one_head_filter_pi_star | 30 | 2.9454 | 1.0480 | 0.5333 | 0.1203 | 0.0022 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1352_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6169 | 0.2667 | -0.7191 | -0.0343 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1352_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.4158 | 0.2308 | -1.1827 | -0.0585 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1352_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1352_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
