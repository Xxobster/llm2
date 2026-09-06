# Autonomy public-indicator hunt gen 1282

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T182930Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1136_neg_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.6987 | 0.6543 | 3.9837 | 0.0176 | 0.3086 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1136_neg_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.6488 | 0.6453 | 3.8730 | 0.0167 | 0.3058 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1136_pos_at_h` | one_head_filter_pi_star | 13 | 1.4308 | 1.7556 | 0.6154 | 1.0254 | 0.0113 | 0.3077 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1136_neg_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.6927 | 0.6331 | 4.0439 | 0.0106 | 0.3166 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1136_neg_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.6761 | 0.6313 | 3.9685 | 0.0106 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1136_pos_at_h` | one_head_filter_pi_star | 14 | 1.2330 | 1.3248 | 0.5714 | 0.4846 | 0.0051 | 0.2857 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1136_pos_at_h` | one_head_filter_pi_star | 35 | 3.3327 | 0.9377 | 0.5429 | -0.1745 | -0.0028 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1136_pos_at_h` | one_head_filter_pi_star | 46 | 4.3059 | 0.9275 | 0.5435 | -0.2224 | -0.0031 | 0.2391 | ok | RAN |
| BTCUSDT | 4 | `ret1136_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1136_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3142 | 0.2222 | -1.6016 | -0.0679 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1136_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1136_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
