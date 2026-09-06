# Autonomy public-indicator hunt gen 466

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T154233Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret320_neg_at_h` | one_head_filter_pi_star | 148 | 12.0902 | 2.2842 | 0.7095 | 4.3743 | 0.0281 | 0.4324 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret320_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.2663 | 0.7079 | 4.7080 | 0.0271 | 0.3876 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret320_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.7900 | 0.6588 | 3.1177 | 0.0121 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret320_neg_at_h` | one_head_filter_pi_star | 167 | 13.5858 | 1.7671 | 0.6587 | 3.0163 | 0.0118 | 0.3533 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret320_pos_at_h` | one_head_filter_pi_star | 182 | 14.9249 | 1.7958 | 0.6429 | 3.2016 | 0.0113 | 0.2967 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret320_pos_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.6916 | 0.6159 | 2.8487 | 0.0106 | 0.2927 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret320_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.1987 | 0.5922 | 0.9997 | 0.0071 | 0.2179 | ok | RAN |
| ETHUSDT | 8 | `ret320_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.1483 | 0.5892 | 0.7723 | 0.0058 | 0.2324 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret320_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret320_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0486 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret320_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret320_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
