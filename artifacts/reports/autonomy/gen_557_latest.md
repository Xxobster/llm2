# Autonomy public-indicator hunt gen 557

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T214217Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret87_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9396 | 0.6786 | 4.3086 | 0.0227 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret87_neg_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8053 | 0.6700 | 3.8488 | 0.0204 | 0.3645 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret87_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1404 | 0.6722 | 4.0916 | 0.0162 | 0.3667 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret87_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1030 | 0.6610 | 4.0359 | 0.0158 | 0.3785 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret87_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2381 | 0.6073 | 1.1952 | 0.0080 | 0.2199 | ok | RAN |
| ETHUSDT | 8 | `ret87_pos_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.2162 | 0.6124 | 1.0827 | 0.0073 | 0.2247 | ok | RAN |
| SOLUSDT | 8 | `ret87_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3765 | 0.6000 | 1.9220 | 0.0059 | 0.2632 | ok | RAN |
| SOLUSDT | 4 | `ret87_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3473 | 0.5979 | 1.8160 | 0.0056 | 0.2526 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret87_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret87_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret87_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret87_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret87_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret87_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret87_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret87_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret87_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret87_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret87_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret87_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret87_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret87_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret87_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret87_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
