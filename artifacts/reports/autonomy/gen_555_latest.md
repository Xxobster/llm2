# Autonomy public-indicator hunt gen 555

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T213435Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma304_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9488 | 0.6957 | 4.2273 | 0.0236 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma304_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8836 | 0.6809 | 4.1420 | 0.0216 | 0.3723 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma304_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2128 | 0.6886 | 4.2323 | 0.0168 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma304_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1539 | 0.6860 | 4.1612 | 0.0163 | 0.3779 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma304_above_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2160 | 0.5960 | 1.1580 | 0.0075 | 0.2172 | ok | RAN |
| ETHUSDT | 4 | `sma304_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.1960 | 0.5939 | 1.0261 | 0.0070 | 0.2284 | ok | RAN |
| SOLUSDT | 8 | `sma304_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.4458 | 0.6133 | 2.0878 | 0.0068 | 0.2652 | ok | RAN |
| SOLUSDT | 4 | `sma304_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3733 | 0.5920 | 1.9056 | 0.0059 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma304_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma304_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma304_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma304_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma304_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma304_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma304_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma304_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma304_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma304_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma304_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma304_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma304_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma304_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma304_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma304_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
