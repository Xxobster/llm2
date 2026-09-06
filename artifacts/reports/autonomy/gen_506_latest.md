# Autonomy public-indicator hunt gen 506

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T181805Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret360_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.3136 | 0.7152 | 4.7107 | 0.0285 | 0.4121 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret360_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.3877 | 0.7216 | 4.9746 | 0.0284 | 0.4034 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret360_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.8928 | 0.6506 | 3.3806 | 0.0124 | 0.3012 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret360_neg_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.7470 | 0.6588 | 3.3586 | 0.0112 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret360_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.7010 | 0.6599 | 3.1818 | 0.0109 | 0.3299 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret360_pos_at_h` | one_head_filter_pi_star | 155 | 12.6388 | 1.4751 | 0.6000 | 2.0559 | 0.0078 | 0.2968 | ok | RAN |
| ETHUSDT | 4 | `ret360_pos_at_h` | one_head_filter_pi_star | 201 | 16.4677 | 1.0952 | 0.5821 | 0.5316 | 0.0037 | 0.2338 | ok | RAN |
| ETHUSDT | 8 | `ret360_pos_at_h` | one_head_filter_pi_star | 182 | 14.9111 | 1.0913 | 0.5824 | 0.4833 | 0.0035 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret360_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret360_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret360_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret360_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
