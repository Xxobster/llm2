# Autonomy public-indicator hunt gen 219

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T235134Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma48_cross_up` | one_head_filter_pi_star | 12 | 1.0171 | 31.3547 | 0.8333 | 2.7416 | 0.0672 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma48_cross_up` | one_head_filter_pi_star | 19 | 1.5795 | 10.9129 | 0.7368 | 2.9722 | 0.0524 | 0.2632 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma48_cross_down` | one_head_filter_pi_star | 29 | 2.4031 | 2.4172 | 0.6552 | 1.9560 | 0.0318 | 0.2759 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma48_cross_up` | one_head_filter_pi_star | 17 | 1.7206 | 1.7932 | 0.5882 | 1.1564 | 0.0257 | 0.2353 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma48_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.8832 | 0.6842 | 4.0534 | 0.0219 | 0.3732 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma48_cross_down` | one_head_filter_pi_star | 24 | 2.0484 | 2.6991 | 0.7083 | 1.7644 | 0.0218 | 0.2083 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma48_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.7779 | 0.6771 | 3.8826 | 0.0206 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma48_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2286 | 0.6909 | 4.2579 | 0.0186 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma48_below_at_h` | one_head_filter_pi_star | 154 | 12.5927 | 2.0645 | 0.6818 | 3.6931 | 0.0165 | 0.4156 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma48_cross_down` | one_head_filter_pi_star | 19 | 1.6488 | 1.4288 | 0.6316 | 0.6113 | 0.0129 | 0.2632 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma48_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2448 | 0.5988 | 1.1302 | 0.0074 | 0.2160 | ok | RAN |
| ETHUSDT | 8 | `sma48_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2329 | 0.5988 | 1.0744 | 0.0071 | 0.2099 | ok | RAN |
| SOLUSDT | 8 | `sma48_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3438 | 0.5991 | 1.8595 | 0.0050 | 0.2535 | ok | RAN |
| SOLUSDT | 4 | `sma48_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.2936 | 0.5924 | 1.6188 | 0.0044 | 0.2464 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma48_cross_down` | one_head_filter_pi_star | 17 | 1.4509 | 0.9916 | 0.5882 | -0.0144 | -0.0003 | 0.2353 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma48_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma48_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma48_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma48_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma48_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma48_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma48_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma48_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma48_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
