# Autonomy public-indicator hunt gen 1330

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T230748Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1184_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.6857 | 0.6523 | 3.9454 | 0.0178 | 0.3200 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1184_neg_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 1.6197 | 0.6433 | 3.6531 | 0.0162 | 0.3217 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1184_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.6886 | 0.6350 | 3.9630 | 0.0107 | 0.3313 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1184_neg_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 1.6484 | 0.6311 | 3.8247 | 0.0105 | 0.3262 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret1184_pos_at_h` | one_head_filter_pi_star | 15 | 1.6241 | 1.4052 | 0.5333 | 0.6243 | 0.0056 | 0.2000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1184_pos_at_h` | one_head_filter_pi_star | 41 | 3.9550 | 0.9809 | 0.5854 | -0.0601 | -0.0009 | 0.2195 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1184_pos_at_h` | one_head_filter_pi_star | 47 | 4.6144 | 0.8483 | 0.5106 | -0.5308 | -0.0078 | 0.2128 | ok | RAN |
| BTCUSDT | 8 | `ret1184_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1184_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1184_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1184_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1184_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
