# Autonomy public-indicator hunt gen 860

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T212454Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema835_below_at_h` | one_head_filter_pi_star | 207 | 16.9100 | 2.0723 | 0.6957 | 4.3176 | 0.0235 | 0.3768 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema835_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.9334 | 0.6749 | 3.9098 | 0.0208 | 0.3645 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema835_below_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 1.8286 | 0.6583 | 3.8988 | 0.0127 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema835_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.7883 | 0.6524 | 3.7262 | 0.0121 | 0.3133 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema835_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.6321 | 0.6160 | 2.3091 | 0.0094 | 0.3200 | ok | RAN |
| ETHUSDT | 8 | `ema835_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 1.2235 | 0.6119 | 0.9856 | 0.0081 | 0.2164 | ok | RAN |
| SOLUSDT | 4 | `ema835_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.4443 | 0.6107 | 1.7774 | 0.0070 | 0.3282 | ok | RAN |
| ETHUSDT | 4 | `ema835_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1819 | 0.5882 | 0.9439 | 0.0068 | 0.2059 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema835_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema835_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0588 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema835_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema835_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema835_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema835_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema835_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema835_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema835_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema835_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema835_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema835_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema835_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema835_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema835_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema835_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
