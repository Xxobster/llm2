# Autonomy public-indicator hunt gen 148

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T191109Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema60_cross_up` | one_head_filter_pi_star | 21 | 1.7799 | 6.3083 | 0.7143 | 2.8066 | 0.0427 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema60_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.8348 | 0.6863 | 4.0413 | 0.0211 | 0.3775 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema60_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8213 | 0.6780 | 3.9920 | 0.0209 | 0.3707 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema60_cross_down` | one_head_filter_pi_star | 31 | 2.6458 | 2.6139 | 0.6774 | 2.0467 | 0.0184 | 0.1290 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema60_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1558 | 0.6867 | 4.0666 | 0.0175 | 0.3976 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema60_below_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 2.0606 | 0.6795 | 3.7052 | 0.0165 | 0.4231 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema60_cross_up` | one_head_filter_pi_star | 14 | 1.4459 | 1.2748 | 0.5000 | 0.4258 | 0.0096 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema60_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2819 | 0.6037 | 1.2946 | 0.0086 | 0.2134 | ok | RAN |
| ETHUSDT | 4 | `ema60_cross_down` | one_head_filter_pi_star | 17 | 1.8269 | 1.2133 | 0.4706 | 0.4376 | 0.0084 | 0.2941 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema60_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.2470 | 0.6023 | 1.1663 | 0.0079 | 0.2159 | ok | RAN |
| SOLUSDT | 8 | `ema60_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3605 | 0.5943 | 1.9492 | 0.0053 | 0.2453 | ok | RAN |
| SOLUSDT | 4 | `ema60_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3124 | 0.5905 | 1.7101 | 0.0047 | 0.2476 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema60_cross_down` | one_head_filter_pi_star | 27 | 2.2374 | 0.9377 | 0.4815 | -0.1474 | -0.0028 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema60_cross_up` | one_head_filter_pi_star | 23 | 2.0018 | 0.9199 | 0.5217 | -0.1727 | -0.0040 | 0.3043 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema60_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema60_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema60_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema60_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
