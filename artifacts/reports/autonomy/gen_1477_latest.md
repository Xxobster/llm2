# Autonomy public-indicator hunt gen 1477

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T003933Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret254_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.1893 | 0.7006 | 4.5679 | 0.0263 | 0.3898 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret254_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 2.0103 | 0.7000 | 4.0559 | 0.0249 | 0.3882 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret254_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.8939 | 0.6536 | 3.7015 | 0.0130 | 0.3520 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret254_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.7154 | 0.6404 | 3.1101 | 0.0116 | 0.3315 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret254_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.5886 | 0.6200 | 2.6679 | 0.0089 | 0.2850 | ok | RAN |
| SOLUSDT | 8 | `ret254_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4706 | 0.6134 | 2.1920 | 0.0074 | 0.2835 | ok | RAN |
| ETHUSDT | 4 | `ret254_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.1664 | 0.5843 | 0.8478 | 0.0060 | 0.2247 | ok | RAN |
| ETHUSDT | 8 | `ret254_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.0695 | 0.5714 | 0.3656 | 0.0027 | 0.2308 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret254_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0393 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret254_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret254_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret254_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret254_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret254_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret254_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret254_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret254_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret254_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret254_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret254_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret254_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret254_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret254_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret254_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
