# Autonomy public-indicator hunt gen 586

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T233721Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret440_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 2.1618 | 0.7152 | 4.3214 | 0.0264 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret440_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.9657 | 0.6875 | 3.9707 | 0.0220 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret440_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.6701 | 0.6510 | 3.0257 | 0.0111 | 0.3490 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret440_pos_at_h` | one_head_filter_pi_star | 98 | 8.2481 | 1.7408 | 0.6633 | 2.2611 | 0.0110 | 0.2959 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret440_neg_at_h` | one_head_filter_pi_star | 196 | 16.0500 | 1.6433 | 0.6429 | 2.9675 | 0.0104 | 0.3214 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret440_pos_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.5294 | 0.6078 | 2.2422 | 0.0087 | 0.3203 | ok | RAN |
| ETHUSDT | 4 | `ret440_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.2018 | 0.5843 | 0.9894 | 0.0074 | 0.2229 | ok | RAN |
| ETHUSDT | 8 | `ret440_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1530 | 0.5814 | 0.7818 | 0.0059 | 0.2209 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret440_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5490 | 0.2632 | -1.0008 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret440_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5490 | 0.2632 | -1.0008 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret440_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret440_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
