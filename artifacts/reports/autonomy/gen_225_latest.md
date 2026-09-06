# Autonomy public-indicator hunt gen 225

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T001530Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema110_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0898 | 0.6990 | 4.7713 | 0.0249 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema110_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0160 | 0.6939 | 4.5316 | 0.0241 | 0.3724 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema110_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2346 | 0.6941 | 4.2747 | 0.0179 | 0.3882 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema110_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1817 | 0.6867 | 4.0961 | 0.0176 | 0.3976 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema110_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2330 | 0.5967 | 1.1313 | 0.0076 | 0.2210 | ok | RAN |
| ETHUSDT | 4 | `ema110_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1930 | 0.5989 | 0.9827 | 0.0066 | 0.2246 | ok | RAN |
| SOLUSDT | 8 | `ema110_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3129 | 0.5894 | 1.6341 | 0.0048 | 0.2657 | ok | RAN |
| SOLUSDT | 4 | `ema110_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.2977 | 0.5842 | 1.5666 | 0.0046 | 0.2624 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema110_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema110_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema110_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema110_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
