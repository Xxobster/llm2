# Autonomy public-indicator hunt gen 669

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T050027Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret115_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.7292 | 0.6684 | 3.7106 | 0.0190 | 0.3583 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret115_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.7070 | 0.6703 | 3.4004 | 0.0178 | 0.3407 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret115_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 2.2258 | 0.6878 | 4.4601 | 0.0166 | 0.3704 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret115_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.1752 | 0.6740 | 4.2467 | 0.0163 | 0.3481 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret115_pos_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.5320 | 0.6461 | 2.4055 | 0.0163 | 0.2416 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret115_pos_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.4407 | 0.6433 | 2.0439 | 0.0137 | 0.2515 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret115_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.3792 | 0.5936 | 1.9012 | 0.0061 | 0.2620 | ok | RAN |
| SOLUSDT | 4 | `ret115_pos_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.3365 | 0.5906 | 1.6781 | 0.0057 | 0.2573 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret115_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret115_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret115_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret115_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret115_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret115_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret115_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret115_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret115_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret115_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret115_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret115_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret115_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret115_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret115_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret115_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
