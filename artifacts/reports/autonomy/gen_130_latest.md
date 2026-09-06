# Autonomy public-indicator hunt gen 130

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T180125Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema55_cross_up` | one_head_filter_pi_star | 14 | 1.1866 | 8.2239 | 0.7857 | 2.5358 | 0.0498 | 0.2857 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema55_cross_down` | one_head_filter_pi_star | 24 | 2.0484 | 5.3228 | 0.8333 | 2.7350 | 0.0279 | 0.0833 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema55_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8592 | 0.6827 | 4.0586 | 0.0214 | 0.3702 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema55_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8131 | 0.6832 | 3.8240 | 0.0207 | 0.3762 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema55_cross_up` | one_head_filter_pi_star | 15 | 1.3056 | 1.5878 | 0.6000 | 0.7628 | 0.0203 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema55_cross_down` | one_head_filter_pi_star | 23 | 1.9059 | 1.6179 | 0.5217 | 1.0814 | 0.0186 | 0.2609 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema55_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1070 | 0.6813 | 3.8563 | 0.0171 | 0.4250 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema55_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.0989 | 0.6770 | 3.8245 | 0.0170 | 0.4224 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema55_cross_down` | one_head_filter_pi_star | 12 | 1.1612 | 2.1284 | 0.7500 | 1.0963 | 0.0134 | 0.0833 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema55_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2570 | 0.6037 | 1.1759 | 0.0081 | 0.2134 | ok | RAN |
| ETHUSDT | 4 | `ema55_above_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.2420 | 0.6023 | 1.1311 | 0.0076 | 0.2105 | ok | RAN |
| SOLUSDT | 4 | `ema55_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3723 | 0.5962 | 1.9601 | 0.0055 | 0.2488 | ok | RAN |
| SOLUSDT | 8 | `ema55_above_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.3136 | 0.5865 | 1.7118 | 0.0047 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema55_cross_up` | one_head_filter_pi_star | 25 | 2.1695 | 0.6529 | 0.4400 | -0.9542 | -0.0192 | 0.2800 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema55_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema55_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema55_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema55_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema55_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema55_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema55_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
