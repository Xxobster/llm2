# Autonomy public-indicator hunt gen 402

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T024246Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret256_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0799 | 0.6947 | 4.6466 | 0.0248 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret256_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.9207 | 0.6882 | 3.7927 | 0.0227 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret256_neg_at_h` | one_head_filter_pi_star | 179 | 14.7339 | 1.8782 | 0.6648 | 3.5444 | 0.0133 | 0.3408 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret256_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.7586 | 0.6484 | 3.2285 | 0.0120 | 0.3462 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret256_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.5272 | 0.6186 | 2.4746 | 0.0081 | 0.2835 | ok | RAN |
| SOLUSDT | 4 | `ret256_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.5059 | 0.6099 | 2.2732 | 0.0079 | 0.2802 | ok | RAN |
| ETHUSDT | 4 | `ret256_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.1957 | 0.5989 | 0.9729 | 0.0068 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `ret256_pos_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.1065 | 0.5848 | 0.5533 | 0.0039 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret256_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret256_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret256_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret256_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
