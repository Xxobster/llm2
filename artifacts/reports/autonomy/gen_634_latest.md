# Autonomy public-indicator hunt gen 634

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T024159Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret488_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 2.1339 | 0.6928 | 4.2122 | 0.0258 | 0.4052 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret488_neg_at_h` | one_head_filter_pi_star | 145 | 11.8452 | 2.1401 | 0.6966 | 4.0970 | 0.0258 | 0.4138 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret488_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8801 | 0.6701 | 3.6505 | 0.0132 | 0.3401 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret488_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.7189 | 0.6633 | 3.2169 | 0.0114 | 0.3417 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret488_pos_at_h` | one_head_filter_pi_star | 151 | 12.3126 | 1.6995 | 0.6159 | 2.6876 | 0.0105 | 0.2715 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret488_pos_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.6541 | 0.6241 | 2.5325 | 0.0100 | 0.2908 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret488_pos_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.1437 | 0.5769 | 0.7259 | 0.0056 | 0.2308 | ok | RAN |
| ETHUSDT | 8 | `ret488_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1325 | 0.5902 | 0.7007 | 0.0052 | 0.2350 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret488_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5653 | 0.2778 | -0.8933 | -0.0353 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret488_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret488_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret488_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret488_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret488_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret488_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret488_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret488_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret488_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret488_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret488_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret488_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret488_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret488_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret488_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
