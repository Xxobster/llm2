# Autonomy public-indicator hunt gen 1421

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T095156Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret246_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.1064 | 0.7016 | 4.6512 | 0.0255 | 0.3717 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret246_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0550 | 0.6927 | 4.4385 | 0.0247 | 0.3799 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret246_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.7994 | 0.6458 | 3.4925 | 0.0125 | 0.3490 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret246_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.7965 | 0.6486 | 3.4279 | 0.0121 | 0.3405 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret246_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.6958 | 0.6358 | 2.9226 | 0.0099 | 0.2890 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret246_pos_at_h` | one_head_filter_pi_star | 170 | 13.8619 | 1.6444 | 0.6353 | 2.7635 | 0.0097 | 0.2824 | ok | RAN |
| ETHUSDT | 4 | `ret246_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2502 | 0.6154 | 1.2246 | 0.0086 | 0.2363 | ok | RAN |
| ETHUSDT | 8 | `ret246_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2039 | 0.5967 | 1.0604 | 0.0074 | 0.2265 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret246_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret246_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret246_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret246_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret246_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret246_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret246_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret246_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret246_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret246_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret246_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret246_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret246_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret246_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret246_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret246_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
