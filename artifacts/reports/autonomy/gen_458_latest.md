# Autonomy public-indicator hunt gen 458

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T151212Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret312_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.2407 | 0.7195 | 4.7079 | 0.0280 | 0.4268 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret312_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 2.1313 | 0.7063 | 4.1329 | 0.0242 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret312_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 1.8143 | 0.6705 | 3.4413 | 0.0126 | 0.3580 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret312_pos_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.3543 | 0.6268 | 1.5575 | 0.0116 | 0.2394 | ok | RAN |
| SOLUSDT | 4 | `ret312_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.6803 | 0.6471 | 2.9227 | 0.0109 | 0.3471 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret312_pos_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.7124 | 0.6225 | 2.7042 | 0.0106 | 0.2914 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret312_pos_at_h` | one_head_filter_pi_star | 168 | 13.7768 | 1.5689 | 0.6131 | 2.4821 | 0.0090 | 0.2976 | ok | RAN |
| ETHUSDT | 4 | `ret312_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1301 | 0.5956 | 0.7010 | 0.0048 | 0.2186 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret312_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0423 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret312_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret312_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret312_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
