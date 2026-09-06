# Autonomy public-indicator hunt gen 507

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T182216Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma262_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0831 | 0.7027 | 4.6399 | 0.0250 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma262_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9819 | 0.6902 | 4.3771 | 0.0239 | 0.3859 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma262_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.2135 | 0.6914 | 4.1788 | 0.0171 | 0.3765 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma262_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2089 | 0.6882 | 4.2599 | 0.0170 | 0.3824 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma262_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2680 | 0.5990 | 1.3890 | 0.0089 | 0.2240 | ok | RAN |
| ETHUSDT | 4 | `sma262_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2640 | 0.6032 | 1.3533 | 0.0088 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `sma262_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.4013 | 0.5970 | 2.0192 | 0.0063 | 0.2587 | ok | RAN |
| SOLUSDT | 8 | `sma262_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.4016 | 0.5990 | 2.0601 | 0.0062 | 0.2624 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma262_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma262_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma262_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma262_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma262_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma262_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma262_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma262_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma262_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma262_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma262_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma262_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma262_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma262_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma262_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma262_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
