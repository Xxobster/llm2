# Autonomy public-indicator hunt gen 1117

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T010529Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret203_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 2.1404 | 0.6994 | 4.5380 | 0.0258 | 0.4049 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret203_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1327 | 0.7049 | 4.6499 | 0.0255 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret203_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.9662 | 0.6720 | 3.8123 | 0.0143 | 0.3710 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret203_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.9091 | 0.6629 | 3.6753 | 0.0137 | 0.3600 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret203_pos_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.4420 | 0.6133 | 2.0871 | 0.0068 | 0.2762 | ok | RAN |
| SOLUSDT | 8 | `ret203_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.4191 | 0.5954 | 1.9550 | 0.0066 | 0.2775 | ok | RAN |
| ETHUSDT | 8 | `ret203_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.0787 | 0.5773 | 0.4441 | 0.0030 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `ret203_pos_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.0720 | 0.5765 | 0.4000 | 0.0027 | 0.2194 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret203_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret203_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret203_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret203_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret203_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret203_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret203_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret203_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret203_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret203_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret203_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret203_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret203_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret203_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret203_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret203_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
