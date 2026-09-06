# Autonomy public-indicator hunt gen 490

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T171601Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret344_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.1632 | 0.7039 | 4.5254 | 0.0258 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret344_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9307 | 0.6720 | 4.1234 | 0.0227 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret344_neg_at_h` | one_head_filter_pi_star | 212 | 17.2466 | 1.7947 | 0.6651 | 3.5739 | 0.0121 | 0.3255 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret344_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.7133 | 0.6548 | 3.3338 | 0.0116 | 0.3503 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret344_pos_at_h` | one_head_filter_pi_star | 167 | 13.6948 | 1.7419 | 0.6407 | 3.0064 | 0.0111 | 0.2814 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret344_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.7556 | 0.6266 | 2.9747 | 0.0110 | 0.2911 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret344_pos_at_h` | one_head_filter_pi_star | 201 | 16.4677 | 1.1625 | 0.6070 | 0.8463 | 0.0061 | 0.2289 | ok | RAN |
| ETHUSDT | 8 | `ret344_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.1546 | 0.5989 | 0.8001 | 0.0057 | 0.2088 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret344_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret344_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0638 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret344_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret344_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
