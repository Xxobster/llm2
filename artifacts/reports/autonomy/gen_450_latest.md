# Autonomy public-indicator hunt gen 450

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T143231Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret304_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.3035 | 0.7152 | 4.8709 | 0.0284 | 0.4303 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret304_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 2.4175 | 0.7239 | 4.9426 | 0.0280 | 0.4049 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret304_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.9194 | 0.6647 | 3.5435 | 0.0140 | 0.3593 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret304_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.8761 | 0.6578 | 3.6213 | 0.0127 | 0.3369 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret304_pos_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2946 | 0.6306 | 1.3933 | 0.0098 | 0.2229 | ok | RAN |
| SOLUSDT | 8 | `ret304_pos_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.5447 | 0.6218 | 2.3317 | 0.0089 | 0.3013 | ok | RAN |
| SOLUSDT | 4 | `ret304_pos_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5216 | 0.6201 | 2.3945 | 0.0083 | 0.2793 | ok | RAN |
| ETHUSDT | 8 | `ret304_pos_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.1717 | 0.6023 | 0.8502 | 0.0063 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret304_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0432 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret304_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0454 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret304_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret304_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
