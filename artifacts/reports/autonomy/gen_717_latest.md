# Autonomy public-indicator hunt gen 717

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T082443Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret127_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.9138 | 0.6816 | 4.1126 | 0.0213 | 0.3575 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret127_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.8468 | 0.6823 | 3.8978 | 0.0211 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret127_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2238 | 0.6818 | 4.3249 | 0.0166 | 0.3807 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret127_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.1656 | 0.6813 | 4.2206 | 0.0157 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret127_pos_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.3178 | 0.6196 | 1.6198 | 0.0106 | 0.2391 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret127_pos_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.2538 | 0.6120 | 1.2953 | 0.0086 | 0.2350 | ok | RAN |
| SOLUSDT | 8 | `ret127_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3851 | 0.6010 | 1.9629 | 0.0063 | 0.2746 | ok | RAN |
| SOLUSDT | 4 | `ret127_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3894 | 0.6020 | 1.9567 | 0.0063 | 0.2602 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret127_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret127_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret127_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret127_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret127_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret127_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret127_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret127_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret127_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret127_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret127_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret127_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret127_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret127_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret127_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret127_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
