# Autonomy public-indicator hunt gen 523

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T192754Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma274_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9320 | 0.6878 | 4.1785 | 0.0228 | 0.3915 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma274_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8169 | 0.6809 | 3.8380 | 0.0207 | 0.3830 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma274_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1919 | 0.6946 | 4.1079 | 0.0166 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma274_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1376 | 0.6864 | 4.0363 | 0.0163 | 0.3728 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma274_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2130 | 0.5969 | 1.1158 | 0.0074 | 0.2245 | ok | RAN |
| ETHUSDT | 4 | `sma274_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.1841 | 0.5851 | 0.9714 | 0.0064 | 0.2234 | ok | RAN |
| SOLUSDT | 8 | `sma274_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.4090 | 0.6089 | 2.0729 | 0.0064 | 0.2574 | ok | RAN |
| SOLUSDT | 4 | `sma274_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3934 | 0.6031 | 1.9440 | 0.0062 | 0.2629 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma274_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma274_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma274_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma274_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma274_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma274_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma274_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma274_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma274_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma274_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma274_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma274_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma274_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma274_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma274_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma274_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
