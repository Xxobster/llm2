# Autonomy public-indicator hunt gen 698

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T070140Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret552_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.1166 | 0.7048 | 4.2076 | 0.0247 | 0.3976 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret552_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0560 | 0.7039 | 4.3086 | 0.0240 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret552_neg_at_h` | one_head_filter_pi_star | 206 | 16.8689 | 1.7289 | 0.6408 | 3.2833 | 0.0117 | 0.3155 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret552_pos_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.2968 | 0.5987 | 1.4133 | 0.0109 | 0.2171 | ok | RAN |
| SOLUSDT | 4 | `ret552_neg_at_h` | one_head_filter_pi_star | 201 | 16.5447 | 1.6665 | 0.6418 | 3.0667 | 0.0109 | 0.3184 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret552_pos_at_h` | one_head_filter_pi_star | 153 | 12.6343 | 1.5653 | 0.6144 | 2.3620 | 0.0081 | 0.2680 | ok | RAN |
| SOLUSDT | 4 | `ret552_pos_at_h` | one_head_filter_pi_star | 153 | 12.6343 | 1.4942 | 0.6078 | 2.1315 | 0.0072 | 0.2680 | ok | RAN |
| ETHUSDT | 4 | `ret552_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1556 | 0.5824 | 0.7801 | 0.0060 | 0.2176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret552_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0521 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret552_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0535 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret552_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret552_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret552_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret552_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
