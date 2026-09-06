# Autonomy public-indicator hunt gen 578

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T230455Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret432_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 2.1667 | 0.7161 | 4.1889 | 0.0254 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret432_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.1513 | 0.6923 | 4.2754 | 0.0250 | 0.3728 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret432_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.7466 | 0.6648 | 3.1057 | 0.0121 | 0.3464 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret432_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.6868 | 0.6627 | 3.0244 | 0.0119 | 0.3669 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret432_pos_at_h` | one_head_filter_pi_star | 172 | 14.1048 | 1.5744 | 0.5988 | 2.4814 | 0.0090 | 0.2965 | ok | RAN |
| SOLUSDT | 8 | `ret432_pos_at_h` | one_head_filter_pi_star | 160 | 13.0465 | 1.4815 | 0.6000 | 2.0708 | 0.0078 | 0.3187 | ok | RAN |
| ETHUSDT | 8 | `ret432_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.1757 | 0.5909 | 0.8856 | 0.0068 | 0.2273 | ok | RAN |
| ETHUSDT | 4 | `ret432_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1604 | 0.5814 | 0.8077 | 0.0061 | 0.2267 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret432_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0445 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret432_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0452 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret432_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret432_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
