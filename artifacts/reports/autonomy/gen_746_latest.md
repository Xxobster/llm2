# Autonomy public-indicator hunt gen 746

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T103100Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret600_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1168 | 0.7112 | 4.2863 | 0.0239 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret600_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9782 | 0.6984 | 4.2231 | 0.0219 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret600_neg_at_h` | one_head_filter_pi_star | 246 | 20.0126 | 1.7338 | 0.6423 | 3.6819 | 0.0120 | 0.3171 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret600_neg_at_h` | one_head_filter_pi_star | 220 | 17.8974 | 1.7467 | 0.6591 | 3.4572 | 0.0119 | 0.3182 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret600_pos_at_h` | one_head_filter_pi_star | 122 | 10.1398 | 1.7138 | 0.6311 | 2.5262 | 0.0098 | 0.2705 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret600_pos_at_h` | one_head_filter_pi_star | 117 | 9.6170 | 1.7209 | 0.6410 | 2.3263 | 0.0097 | 0.2650 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret600_pos_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.2327 | 0.5858 | 1.1839 | 0.0088 | 0.2189 | ok | RAN |
| ETHUSDT | 8 | `ret600_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.2199 | 0.5819 | 1.1583 | 0.0083 | 0.2203 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret600_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5856 | 0.2941 | -0.8239 | -0.0371 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret600_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5653 | 0.2778 | -0.8933 | -0.0373 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret600_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret600_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret600_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret600_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret600_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret600_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret600_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret600_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret600_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret600_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret600_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret600_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret600_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret600_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
