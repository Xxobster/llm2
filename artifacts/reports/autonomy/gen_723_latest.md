# Autonomy public-indicator hunt gen 723

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T085036Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma442_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0241 | 0.6931 | 4.4903 | 0.0233 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma442_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9670 | 0.6939 | 4.3924 | 0.0225 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma442_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.8930 | 0.6667 | 3.6377 | 0.0137 | 0.3607 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma442_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.8831 | 0.6721 | 3.6981 | 0.0133 | 0.3552 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma442_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.6629 | 0.6196 | 2.8643 | 0.0100 | 0.2772 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma442_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2904 | 0.6000 | 1.4582 | 0.0100 | 0.2216 | ok | RAN |
| SOLUSDT | 4 | `sma442_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.6377 | 0.6257 | 2.7405 | 0.0096 | 0.2834 | ok | RAN |
| ETHUSDT | 8 | `sma442_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1933 | 0.5907 | 1.0211 | 0.0068 | 0.2176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma442_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma442_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma442_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma442_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
