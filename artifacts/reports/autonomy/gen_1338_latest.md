# Autonomy public-indicator hunt gen 1338

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T235315Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1192_neg_at_h` | one_head_filter_pi_star | 308 | 25.1608 | 1.7455 | 0.6591 | 4.1193 | 0.0183 | 0.3312 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1192_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.6726 | 0.6519 | 3.8852 | 0.0168 | 0.3228 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1192_pos_at_h` | one_head_filter_pi_star | 16 | 1.4580 | 1.8177 | 0.6250 | 1.0934 | 0.0140 | 0.3125 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1192_pos_at_h` | one_head_filter_pi_star | 12 | 1.3548 | 1.9854 | 0.6667 | 1.1472 | 0.0139 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1192_neg_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 1.7000 | 0.6374 | 4.2111 | 0.0109 | 0.3173 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1192_neg_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 1.6930 | 0.6371 | 4.1187 | 0.0108 | 0.3229 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1192_pos_at_h` | one_head_filter_pi_star | 60 | 5.5186 | 1.0300 | 0.5667 | 0.1027 | 0.0014 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1192_pos_at_h` | one_head_filter_pi_star | 50 | 4.5988 | 0.8323 | 0.5000 | -0.5828 | -0.0084 | 0.2000 | ok | RAN |
| BTCUSDT | 8 | `ret1192_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1192_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3142 | 0.2222 | -1.6016 | -0.0667 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1192_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1192_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1192_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1192_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
